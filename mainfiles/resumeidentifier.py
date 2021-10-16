import spacy
import numpy as np
from nltk.tag.stanford import StanfordNERTagger
from keras.models import load_model
import configuration as cfg
from keras.backend import clear_session

class ResumeIdentifier:

    def __init__(self):
        '''
        Initializer for this class which identifies whether the uploaded
        file is resume or not resume
        initializes stanford NER tagger for the Named Entity Recognition
        for feature selection
        also loads the resume identifier model which will predict the
        resume not resume using the features created by NER tagger
        '''
        self.ner_tagger = StanfordNERTagger(cfg.NerModelPath, cfg.jarPath,  encoding='utf8')
        self.nlp = spacy.load("en_core_web_md")
        self.model = load_model(cfg.ResumeIdentifierModelPath)

    def identifyResume(self,cleaned_text):
        '''
        This method is used to test whether a given document is a resume or not.

        :param cleaned_text: This method takes in a cleaned text of a document
        :type cleaned_text: str
        :return: 'True' if  the document is a resume and 'False' if it is not
        '''
        clear_session()
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

        result = (self.model.predict(np.array([resume_features])))[0]
        if result > cfg.ResumeIdentifierThreshold:
            return True
        else:
            return False
