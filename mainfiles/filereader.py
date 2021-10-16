import os
import re

from subprocess import Popen,PIPE
# import Image
from pytesseract import image_to_string
import docx2txt
from PIL import Image
from tika import parser

def clean_text(text):
    '''
    function that takes the text containing noise
    and tries to clean it as much as possible
    :param text: str
    :return: cleaned text of type str
    '''
    text = re.sub(r' +',' ', text)
    text = re.sub(r'\t',' \n, ', text)
    text = re.sub(r'\n+',' \n ,', text)
    text = re.sub(r',+',',', text)
    text = text.encode('ascii', errors='ignore').decode("utf-8")
    cleaned_lines = [re.sub(r'^[\W]+','',line) for line in text.split("\n")]
    text = '\n'.join(cleaned_lines)
    return text

def pdf_to_text(filepath):
    '''
    Takes the resume in Pdf format and
    extracts the text from the pdf file
    :param filepath: type str
    :return: cleaned text of type str
    '''
    pdf_file = parser.from_file(filepath)
    text = pdf_file["content"]
    text = clean_text(text)
    return text


def docx_to_text(filepath):
    '''
    Takes the resume in docx format and
    extracts the text from the word docx file
    :param filepath: type str
    :return: cleaned text of type str
    '''
    text = ""
    text += docx2txt.process(filepath)
    text = clean_text(text)
    return text

def txt_to_text(filepath):
    '''
    Takes the resume in txt format and
    extracts the text from the txt file
    :param filepath: type str
    :return: cleaned text of type str
    '''
    text = ""
    with open(filepath, mode='r', encoding='unicode_escape', errors='strict', buffering=1) as file:
        data = file.read()
    text += data

    text = clean_text(text)
    return text

def doc_to_text(filepath):
    '''
    This function takes the doc file
    from the file path param and returns
    the cleaned the text from the file.
    :param filepath: path/directory of the doc file in the system
    :return: Returns the cleaned text from the file
    '''
    text = ""
    cmd = ['antiword', filepath]
    p = Popen(cmd, stdout=PIPE)
    stdout, stderr = p.communicate()
    text += stdout.decode('utf-8', 'ignore')
    text = clean_text(text)
    return text

def img_to_text(filepath):
    '''
    This function takes the image file
    from the file path param and returns
    the cleaned the text from the  image file.
    :param filepath: path/directory of the image file in the system
    :return: Returns the cleaned text from the image file
    '''
    text = image_to_string(Image.open('test.png'))
    text = clean_text(text)
    return text

def read_cv(file_path):
    '''
    This function identifies the file extensions
    of the cv and will parse the text from those file
    according to the extensions using the other file
    parsing methods and returns the cleaned text accordingly.
    :param file_path: path/directory of the file in the system to be parsed
    :return: returns the text(str) with respect to file extentions.
    '''

    image_extensions=['.jpeg','.png','.jpg','.psd','.ai']
    _,file_extension=(os.path.splitext(file_path))
    if file_extension.lower() in image_extensions:
            file_extension='.img'
    else:
        pass

    options={
            '.pdf':pdf_to_text,
            '.docx':docx_to_text,
            '.txt':txt_to_text,
            '.doc':doc_to_text,
            '.img':img_to_text,
            }
    try:
        text=options[file_extension](file_path)
        return text
    except Exception as e:
        print("Exception at fileReader:"+str(e))
