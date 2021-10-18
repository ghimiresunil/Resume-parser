import json

import spacy
import numpy as np

import warnings
warnings.filterwarnings('ignore')

from nltk.tag.stanford import StanfordNERTagger
from keras.models import load_model
import configuration as cfg
from mainfiles import informationparser, segmentresume,filereader
from configuration import Write2file
class Parser:

    def __init__(self):
        '''
        Initializer that instantiates the
        resume identifier ,instantiate object that
        segments the resume and also instantiates the
        resume parser itself.
        '''
        self.ner_tagger = StanfordNERTagger(cfg.NerModelPath, cfg.jarPath, encoding='utf8')
        self.nlp = spacy.load("en_core_web_sm" ,disable =['parser','ner','tagger'])
        self.model = load_model('./models/Resume_Identification_Model.h5')
        self.segmentationObj = segmentresume.ResumeSegmentCreator()
        self.parserObj = informationparser.InformationParser()

    def identifyResume(self,cleaned_text):
        '''
        This method is used to test whether a given document is a resume or not.

        :param cleaned_text: This method takes in a cleaned text of a document
        :type cleaned_text: str
        :return: 'True' if  the document is a resume and 'False' if it is not
        '''
        doc = self.nlp(cleaned_text)
        resume_tokens = [token.text for token in doc]
        word_pos = self.ner_tagger.tag(resume_tokens)
        NER_list = set([pos for word, pos in word_pos])
        resume_features = [
            int('PER' in NER_list),
            int('LOC' in NER_list),
            int('UNI' in NER_list),
            int('DEG' in NER_list),
            int('DATE' in NER_list),
            int('DESIG' in NER_list),
            int('ORG' in NER_list),
            int('EXP' in NER_list),
        ]

        #
        return True

    def resume_parser(self,file_path):
        '''
        This function takes the path of the resume and
        pass it to the resume identifier. Passes the document
        to the parser if its a valid resume else rejects the
        resume sending error warning.
        :param file_path: path of the resume in str
        :return: Parsed data in json if valid resume else sends the
        error report incase of the invalid resume
        '''
        actionSelector = {
                          True:self.parseCV,
                          False:self.rejectCV
                         }
        cv_content = filereader.read_cv(file_path)

        check_cv = self.identifyResume(cv_content)
        return actionSelector[check_cv](cv_content)

    def parseCV(self,cv_content):
        '''
        This method here takes the plain text of the resume in str format
        and then parses the information from the resume.
        :param cv_content: plain text in str format
        :return: parsed information in json format
        '''
        self.cv_tokens = cv_content.split(' ')
        resume_segment = self.segmentationObj.format_segment(cv_content)
        parsed_information = self.parserObj.getStructuredData(cv_content,resume_segment)
        return parsed_information

    def rejectCV(self,*args):
        '''
        This method displays the error message in case of the invaild
        resume.
        :param cv_content:
        :return: error message of type str
        '''
        return False



