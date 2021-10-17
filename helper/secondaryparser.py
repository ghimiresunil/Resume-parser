import re

from helper.regexparser import regex_parser
from helper.namedentityrecognition import StanfordNER

class SecondParser:

    @staticmethod
    def second_personal_info_parser(model,text):
        '''
        This function takes the text containing
        personal info the text is formatted and
        regex is applied to match emails and phone numbers
        and model as the text is also passed
        in model it determines the Named-Entity
        from the text tokens or group of tokens
        :param model:
        :param text:string(text)
        :return: Returns the fields (emails,phone,name,address)
        as the personal information
        '''
        splitted_text=text.split('\n')
        len_of_text=len(splitted_text)
        new_text=''
        i=0
        while i<len_of_text/4:
            new_text+='\n'+ splitted_text[i] +','
            new_text=re.sub(r'\n+','\n',new_text)
            i+=1
        emails,phone,birthdate,gender=regex_parser(new_text,"profile")
        name,address= StanfordNER.ner_parser(model,new_text,"profile")
        return emails,phone,name,address,birthdate,gender
