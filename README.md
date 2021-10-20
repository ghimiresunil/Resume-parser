# Resume-parser
A prototype resume parser for parsing the CVs

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
