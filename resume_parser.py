from enum import unique
import spacy
from pdfminer.high_level import extract_text
import re
import os
import pandas as pd


# convert pdf to txt:
def smfPDF2Text(vsPDFFilename):
    textContent = extract_text(vsPDFFilename)
    return textContent

# parse content of the text:


def parse_content(vsFileContent):
    # load the language model
    nlp = spacy.load("en_core_web_sm")

    # Helper variables
    result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
    names = []
    phones = []
    emails = []
    skills = []

    # Some skills that we look in resumes:
    skillset = re.compile(
        'python|java|sql|hadoop|tableau|c|c++|c#|vb|vb.net|asp|asp.net')

    # phone_num credit https://stackoverflow.com/a/3868861
    phone_num = re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )

    doc = nlp(vsFileContent)

    sPersonName = [
        entity.text for entity in doc.ents if entity.label_ == "PERSON"][0]
    print("name = " + sPersonName)

    sEmailAddress = [word for word in doc if word.like_email == True][0]
    print("email = " + sEmailAddress)

    sPhoneNumber = str(re.findall(phone_num, vsFileContent.lower()))
    skills_list = re.findall(skillset, vsFileContent.lower())
    unique_skills_list = str(set(skills_list))
    names.append(sPersonName)
    emails.append(sEmailAddress)
    phones.append(sPhoneNumber)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")


for sPDFFilename in os.listdir('resumes/'):
    if sPDFFilename.endswith('.pdf'):
        sInputFilename = os.path.join('resumes/', sPDFFilename)
        print('Reading...' + sInputFilename)
        sFileContent = smfPDF2Text(sInputFilename)
        # backup in txt folder:
        sTXTFilename = os.path.basename(
            os.path.splitext(sInputFilename)[0]) + ".txt"
        sTXTFilename = os.path.join("output/txt/", sTXTFilename)

        objFile = open(sTXTFilename, 'w')
        objFile.write(sFileContent)
        objFile.close

        print("Text file created : " + sTXTFilename)

        if (sFileContent != ""):
            parse_content(sFileContent)
