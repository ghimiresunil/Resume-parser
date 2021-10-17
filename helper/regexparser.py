import re
import nltk
import spacy
import string

from spacy.matcher import Matcher
from formatter.formatdata import key_value_identifier

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

from wordsegment import load, segment
load()

def birth_gender_extractor(text):

    '''
    It takes a profile segment of the resume
    and parses the email,phones etc
    uses regex for email,phone number
    :param text:string
    :returns: email,phone number
    '''

    # regex_email = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
    regex_phone = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    regex_date = r'[0-9]{1,4}\s*[-]\s*[0-9]{1,2}\s*[-]\s*[0-9]{1,4}'
    regex_gender = r'[^:][A-Za-z]*[M|m]ale'
    # phone = re.findall(regex_phone, text)
    # email =  re.findall(regex_email, text)
    birthdate = re.findall(regex_date,text)
    gender = re.findall(regex_gender,text)
    # phone_number = [num.strip() for num in phone if len(num.strip()) > 10]
    return birthdate,gender

def extract_email(text):
    '''
    Helper function to extract email id from text
    :param text: plain text extracted from resume file
    '''
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", str(text))
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None

def extract_phone_number(text):
    phone = re.findall(re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'), text)

    if phone:
        phone_number = ''.join(phone[0])

        if text.find(phone_number) >= 0 and len(phone_number) < 16:
            return phone_number
    return None

def links_extractor(text):
    '''
    Function is a part of helper parser
    makes use of regex to extract the links
    like github links and linked in links
    :type text : str
    :return: linkedin,github links
    '''

    regex_git = r"github.com/[^ |^\n]+"
    regex_linkedin = r"linkedin.com/[^ |^\n]+"
    return (list(set(re.findall(regex_git, text))), list(set(re.findall(regex_linkedin, text))))

def zip_code_extractor(text):
    '''
    zip_code extractor takes the whole
    text of the resume and makes the search
    of zip code within the first 25% of the resume text
    :type text: string
    :return: zipcode
    '''
    splitted_text = text.split('\n')
    len_of_text = len(splitted_text)
    new_text = ''
    i = 0
    while i < len_of_text / 4:
        new_text += ' ' + splitted_text[i] + ','
        new_text = re.sub(r'\n+', '\n', new_text)
        i += 1
    regex_zip = r'(\b\d{5}-\d{4}\b|\b\d{5}\b\s)'
    possible_zip =  re.findall(regex_zip, text)
    zip =  [zip for zip in possible_zip if len(zip)>4 and len(zip) <=9 ]
    return zip

def nationality_extractor(text):
    punctuations = [':',"-",":-"]
    regex_nationality = r'[N|n]ationality\s*[:|-|:-]?\s*[^\n]*'
    try:
        nationality = nltk.word_tokenize(re.findall(regex_nationality,text)[0])
        extracted_nationality = [matched_item for matched_item in nationality
                                if matched_item.strip() not in punctuations
                                and matched_item.find('ational')== -1]
    except  Exception as e :
        print("Error at regexparser, Nationality Extractor ,passing the task to backup parser")
        return []

    return extracted_nationality

def key_value_parser(text):
    name, address,zip = "null", "null", "null"
    key_value_pair = key_value_identifier(text)
    for key,value in key_value_pair.items():
        if key=="name":
            name = value
        elif key == "address":
            address = value
        elif key == "zip":
            zip = value
    return name, address, zip

def extract_name(text):
    email = extract_email(text)
    email = email.rsplit('@', 1)[0]
    email = re.sub (r'([^a-zA-Z ]+?)', ' ', email)
    email = segment(email)
    first_name = string.capwords(email[0])
    last_name = string.capwords(email[-1])
    text = nlp(text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', [pattern])
    matches = matcher(text)
    for match_id, start, end in matches:
        span = text[start:end]
        if first_name in span.text:
            return span.text
        elif last_name in span.text:
            return span.text
        elif first_name.upper() in span.text:
            return span.text
        elif last_name.upper() in span.text:
            return span.text

def regex_parser(text,mode):
    '''
    The function here decides which
    function to call for extracting
    the personal information ,links
    and zipcode
    :type text:string
    :type mode:string
     '''
    options={"profile":birth_gender_extractor,
            "email": extract_email,
            "phone":extract_phone_number, 
             "links":links_extractor,
             "zipcode":zip_code_extractor,
             "nationality":nationality_extractor,
             "kv_parse": key_value_parser,
             "name": extract_name
             }

    return(options[mode](text))
