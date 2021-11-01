# Resume-parser
A prototype resume parser for parsing the CVs

## Problem Statement 

Different people from different fields and different backgrounds have varied personalities. Similarly their CV writing pattern also fluctuates. They have worked on different types of projects and each of them possess a varied style of writing it down. Thus making each CV unique in itself. 

Some people may work in the HR department. He/She has to crawl hundreds of CVs from the internet. After gathering the CVs, they will call the executives used to summarize the CV, enter specific details into their database and then call the candidate for job consulting. An executive took around 10-15 mins per CV to summarize it and enter the details into the database. My job in this project is to automate this process. 

## Academic Questions

What would be the best approach to parse and extract the useful information from CV and Resume in an effective manner using various NLP algorithms. 

## Project Aims

- To take help of the cutting-edge and latest NLP technology to enhance their business processes.
- To extract the required information about candidates without having to go through each and every resume manually,  

## Project Objectives

- For information extraction, NLP model will be configured and reconfigured
- The system will replace slow and expensive human processing of resumes with extremely fast and cost-effective software
- By uploading CV/Resume of candidate in our system, it will convert the unstructured data into a structured form.
- The system will automatically segregates the information into various fields and parameters like contact information, educational qualification, work experience, skills, achievements, professional certifications to quickly help you identify the most relevant resumes based on criteria.

## Features

- Extract Name
- Extract Email
- Extract Mobile Number
- Extract Skills
- Extract Soft skills
- Extract Nationality
- Extract Language
- Extract Total Experience
- Extract College Name
- Extract Degree
- Extract Designation
- Extract Company Names
- Github Link
- Linkedin Link
- Date of Birth
- Gender
- Zipcode
- Project
- Rewards
- References

## Requirements

- Windows 10 / Linux / Mac
- Jupyter Notebook
- Python 
- Tensorflow
- Keras
- Sklearn
- SpaCy 
- Pillow
- Tika Parser
- docx2txt

## Results

```bash
{
    "PERSONAL_INFORMATION": {
        "First_Name": "Sunil",
        "Last_Name": "Ghimire",
        "Address": [],
        "Email": "sunilghimire64@gmail.com",
        "Phone_Number": "+977 9841070311",
        "Zip_Code": [],
        "Nationality": [
            "nepali"
        ],
        "github": [
            "github.com/ghimiresunil"
        ],
        "linkedin": [
            "linkedin.com/in/ghimiresunil"
        ],
        "birthdate": [],
        "Gender": []
    },
    "OBJECTIVE": " To obtain a position in life to utilize my technical skills, experience, and abilities and archive professional   growth while being innovative, flexible, and resourceful. Willingness to learn in making your esteemed   organization successful.   ",
    "SKILLS": {
        "Skills": [
            "Mysql",
            "C",
            "Java",
            "Python",
            "Tensorflow",
            "Linux",
            "Keras",
            "Conda",
            "Jupyter",
            "Opencv",
            "Matplotlib"
        ],
        "Soft_skills": []
    },
    "EDUCATION": {},
    "EXPERIENCE": {
        "Exp1": {
            "Designation": "Graduate Teaching Assistant",
            "location": "Kathmandu",
            "roles": "EXPERIENCE 1 . A Computer Vision Based Vehicle Detection & Counting System Description Proposes a video-based approach based on computer vision technologies for vehicle detection and counting . o Learning real data and real-world problems . o Dealing with importing messy data , cleaning data , merging and concatenating data , grouping and aggregating data , Exploratory Data Analysis through to preparing and processing data for Statistics , Machine Learning , NLP & Time Series and Data Presentation . o Cross validate the model o Practice and learning by doing ."
        },
        "Exp2": {
            "Designation": "Computer Engineer",
            "company": "CSAMIN & Bit4Stack Tech Inc.",
            "location": "Kathmandu",
            "roles": "( HCK ) Data Science ( Summer Class ) | Artificial Intelligence and Machine Learning ( Third Year ) o Working under the supervision of Mr. Jnaneshwar Bohara ("
        }
    },
    "LANGUAGES": [
        "English",
        "Hindi",
        "Nepali"
    ],
    "PROJECTS": "",
    "REWARDS": "",
    "REFERENCES": " Mr. Jnaneshwar Bohara Mr. Prakash Gautam Mr. Sachin Kafle   Computer Engineer Module Leader & Academic Head Author, Teacher   Government of Nepal Herald College Kathmandu Founder of CSAMIN & Bit4Stack Tech Inc.   boharag@gmail.com info@prakashgautam.com.np sachin.kafle@heraldcollege.edu.np    mailto:boharag@gmail.com  mailto:info@prakashgautam.com.np  mailto:sachin.kafle@heraldcollege.edu.np "
}
```
