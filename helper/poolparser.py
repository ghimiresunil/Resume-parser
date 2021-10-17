import pandas as pd

from helper.createngrams import get_ngrams
from formatter.standarizedata import capitalizeinput
from configuration import Languagefiles,Skillsfiles,Nationalityfiles

def languageparser(lang_doc):
    '''
    This function here extracts all the possible
    languages present in the resume. It does so by
    comparing the predefined language tokens and
    bigrams with the tokens and bigrams of the resume.
    :param lang_doc: spaCy doc
    :return: This returns the capitalized languages in
            the form of list of str.
    '''
    languagebigrams = get_ngrams(lang_doc,2)
    languages = pd.read_csv('./datahouse/languages.csv')
    language_tokens = [token.text for token in lang_doc]
    languagebigrams.extend(language_tokens)
    total_languages = [language.lower() for language in languagebigrams ]
    languages['matched'] = languages['value'].apply(lambda x: 1 if x.lower() in total_languages else 0)
    matched_languages = languages.value.loc[languages['matched'] == 1]
    matched_languages = matched_languages.tolist()
    formatted_languages = map(capitalizeinput,matched_languages)
    return [language for language in formatted_languages]

def skillparser(skill_doc):
    '''
    This function here extracts all the possible
    skill present in the resume. It does so by
    comparing the predefined skills tokens and
    bigrams with the tokens and bigrams of the resume.
    :param skill_doc: spaCy doc
    :return: This returns the capitalized skills in
            the form of list of str.
    '''
    skillbigrams = get_ngrams(skill_doc,2)
    skill_tokens = [token.text for token in skill_doc]
    skills = pd.read_csv('./datahouse/technical_skills.csv')
    skillbigrams.extend(skill_tokens)
    total_skills = [skill.lower() for skill in skillbigrams]
    skills['matched'] = skills['Predefined_skills'].apply(lambda x: 1 if x.lower() in total_skills else 0)
    matched_skills = skills.Predefined_skills.loc[skills['matched'] == 1].values
    matched_skills = matched_skills.tolist()
    formatted_skills = map(capitalizeinput, matched_skills)
    return [skill for skill in formatted_skills]

def nationalityparser(cvdoc):
    '''
    this fucntion takes the cv content
    and searches for the nationality
    :param profiledoc:
    :return: nationality
    '''
    nationalitybigrams = get_ngrams(cvdoc, 2)
    cv_tokens = [token.text for token in cvdoc]
    nationality = pd.read_csv('./datahouse/nationality_data.csv')
    nationalitybigrams.extend(cv_tokens)
    total_nationality = [token.lower() for token in nationalitybigrams]
    nationality['matched'] = nationality['Nationality'].apply(lambda x: 1 if x in total_nationality else 0)
    matched_nationality = nationality.Nationality.loc[nationality['matched'] == 1].values
    matched_nationality = matched_nationality.tolist()
    if matched_nationality:
        return matched_nationality
    else:
        return ['Nepali']
