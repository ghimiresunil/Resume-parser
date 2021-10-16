import pickle
import json

import spacy
from nltk.tag.stanford import StanfordNERTagger

from helper.namedentityrecognition import StanfordNER
from helper.regexparser import regex_parser
from helper.secondaryparser import SecondParser
from helper.poolparser import languageparser,skillparser,nationalityparser
from formatter import formatdata
from mainfiles.filereader import clean_text
from configuration import *

class InformationParser:

    def __init__(self):
        '''
        constructor that initializes all the required models for
        the information extraction
        '''
        with open('./models/male_female_identifier.pickle', 'rb')as handle:
            self.gender_tokenizer = pickle.load(handle)
        with open('./models/male_female_tokenizer.pickle', 'rb') as handle:
            self.gender_model = pickle.load(handle)
        self.ner_tagger = StanfordNERTagger(NerModelPath, jarPath, encoding='utf8')
        self.nlp = spacy.load("en_core_web_sm")

    def personal_information_parser(self,profile_segment,allcontent):
        '''
        tries to get the profile information thrown by the segmentation code
        if segment is catched passes the segment to the regex parser and stanfordNER
        parser for extracting the profile information else passes the whole raw text
        to the secondary parser
        :returns : name,address,emails,github,linkedin,nationality,zipcode
        '''
        text = profile_segment
        if text:
            name,address = StanfordNER.ner_parser(self.ner_tagger,text,"profile")
            birthdate,gender = regex_parser(text,"profile")
        # elif text:
        #     name = regex_parser(self.cv_content,"name")
        else:
            name, address,birthdate,gender = SecondParser.second_personal_info_parser(
                                            self.ner_tagger,allcontent)
        name = regex_parser(self.cv_content, "name")
        email = regex_parser(self.cv_content, "email")
        phone = regex_parser(self.cv_content,"phone")
        github, linkedin = regex_parser(self.cv_content, "links")
        zipcode = regex_parser(self.cv_content, "zipcode")
        nationality = regex_parser(self.cv_content,'nationality')
        if not nationality:
            nationality = nationalityparser(self.nlp(self.cv_content))

        r_name,r_address,r_zip = regex_parser(self.cv_content,'kv_parse')
        if r_name !="null":
            name = r_name
        if r_address !="null":
            address = r_address
        if r_zip != "null":
            zipcode = r_zip
        return name,address,email,phone,zipcode,nationality,github,linkedin,birthdate,gender

    def skills_parser(self,cv_content,skill_segment):
        '''
        This function takes the skill segment as well as the whole resume text
        and tries to extract all possible skills from the skill segment as well
        well as the whole resume text.
        :param cv_content:
        :param skill_segment:
        :return: list of the skills of type str
        '''
        if skill_segment is not None:
            possible_skills = skill_segment
            skill_doc = self.nlp(possible_skills)
            skills = skillparser(skill_doc)
            if skills:
                return list(set(skills))
            else:
                possible_skills = cv_content
                skill_doc = self.nlp(possible_skills)
                skills = skillparser(skill_doc)
                return list(set(skills))
        else:
            possible_skills = cv_content
            skill_doc = self.nlp(possible_skills)
            skills = skillparser(skill_doc)
            return list(set(skills))


    def education_parser(self,cv_content,education_segment):
        '''
        This function takes the education segment and cv
        plain text. Tries to extract the academics from the
        respective segment. If it fails the segmentation then
        whole resume is taken as the input.
        :param cv_content
        :param education_segment
        :return: nested dict containing the academics information
        '''

        if education_segment is not None:
            possible_education = education_segment
        else:
            possible_education = cv_content
        possible_education = clean_text(possible_education)
        academics = StanfordNER.ner_parser(self.ner_tagger,possible_education,'academics')
        return academics

    def experience_parser(self,cv_content,experience_segment):
        '''
        This function takes the experience segment and cv
        plain text. Tries to extract the experience from the
        respective segment. Incase of the extraction failure
        from the experience segment it extracts the experience
        from whole resume's content
        :param cv_content:
        :param experience_segment:
        :return: the parsed resume in nested dict containing
                designation,date,organization,roles and
                responsibilities
        '''
        if experience_segment is not None:
            possible_experience = experience_segment
        else:
            possible_experience = cv_content
        possible_experience = clean_text(possible_experience)
        experiences = StanfordNER.ner_parser(self.ner_tagger,possible_experience,'experience')
        return experiences

    def language_parser(self,cv_content,language_segment):
        '''
        This function takes the resume_segment and cv plain text.
        Tries to extract the languages from the language segment
        and returns languages if successful else search for the
        language in the whole resume.
        :param cv_content:
        :param language_segment:
        :return: It returns the extracted languages in the list
                 of str
        '''
        if language_segment is not None:
            possible_language = language_segment
        else:
            possible_language = cv_content
        lang_doc = self.nlp(possible_language)
        languages = languageparser(lang_doc)
        if languages:
            return languages
        else:
            return ['English']

    def returnjson(self,personal_info,objective,skills,academics,experiences,language,projects,rewards,references):

        '''
        This function takes all the profile attributes
        and returns them in structured JSON format.
        :param personal_info:
        :param objective:
        :param skills:
        :param experiences
        :param language:
        :param projects:
        :param rewards:
        :param references:
        :return: It returns the profile attributes as structured JSON
        '''

        personalInfo = formatdata.formatPersonalinfo(personal_info)
        formatted_data = {"PERSONAL_INFORMATION":personalInfo,
                          "OBJECTIVE":objective,
                          "SKILLS": {
                            'Skills':skills,
                            'Soft_skills':[]
                                },
                          "EDUCATION":academics,
                          "EXPERIENCE":experiences,
                          "LANGUAGES":language,
                          "PROJECTS":projects,
                          "REWARDS":rewards,
                          "REFERENCES":references
                          }
        with open('parsed_output.json','w')as resume_input:
            json.dump(formatted_data,resume_input,indent=4)
            return formatted_data


    def getStructuredData(self,cv_content,resume_segment):
        self.cv_content = cv_content
        self.profile = resume_segment.get('profile')
        self.objective = resume_segment.get('objectives')
        self.skills = resume_segment.get('skills')
        self.education = resume_segment.get('academics')
        self.experience = resume_segment.get('experiences')
        self.language = resume_segment.get('language')
        personal_information = self.personal_information_parser(self.profile,cv_content)
        objective = self.objective
        skills = self.skills_parser(cv_content,self.skills)
        academics = self.education_parser(cv_content,self.education)
        experiences = self.experience_parser(cv_content,self.experience)
        language = self.language_parser(self.cv_content,self.language)
        projects = resume_segment.get('projects')
        rewards = resume_segment.get('rewards')
        references = resume_segment.get('references')
        formatted_data = self.returnjson(personal_information,objective,skills,academics,experiences,language,projects,rewards,references)
        return formatted_data





