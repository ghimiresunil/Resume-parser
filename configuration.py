import os
'''<------------Directory Absolute Paths------------------------------>'''
RootDir = os.path.dirname(os.path.abspath(__file__))
ParserDir = RootDir + '/cvparser'
ScorerDir = RootDir + '/cvscorer'
CommonDir = RootDir + '/common'
tempStorage = RootDir +'/temp'

'''<------------------------Paths------------------------------------->'''
'''<--------for parser only -------------->'''
ResumeIdentifierModelPath = ParserDir + '/models/Resume_Identification_Model.h5'
ResumeSegmentationModelPath = ParserDir + '/models/segment_identifier.pkl'
MaleFemaleIdentifierModelPath = ParserDir +'/models/male_female_identifier.pickle'

'''<--------for scorer only--------------->'''
Word2vecModelPath = ScorerDir+'/models/model.bin'

'''<---------for both/common usage --------->'''

jarPath = CommonDir +'/stanfordNER/stanford-ner.jar'
NerModelPath = CommonDir +'/stanfordNER/NER_model.ser.gz'

'''<---------------------Preprocessors-------------------------------->'''
'''<---------for parser only--------------->'''
MaleFemaleTokenizer = ParserDir + '/models/male_female_tokenizer.pickle'


'''<-------------------Tuning Parameters------------------------------>'''
ResumeIdentifierThreshold = 0.0468

'''<--------------------pandas database ------------------------------->'''
Languagefiles = ParserDir +'/datahouse/languages.csv'
Skillsfiles = ParserDir + '/datahouse/technical_skills.csv'
Nationalityfiles = ParserDir + '/datahouse/nationality_data.csv'

"<---------------------Write to file ----------------------------------->"
Write2file = True




