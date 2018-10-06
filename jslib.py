# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:56:05 2018

@author: Jayant
"""
import json
import requests
from urllib.request import urlopen

def get_account_info(username):
    
    #api_url = '{0}'.format(api_url_base)
    api_token = '062fd3133768bcf04b45aa1e2ed8ee1309b8e022'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(api_token)}
    api_url = 'https://api.github.com/users/' +username
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
def download_file(download_url, outputpath):
    print(download_url)
    r = requests.get(download_url, allow_redirects=True)
    open(outputpath, 'wb').write(r.content)
    
    r = requests.get(download_url, stream=True)
    
    with open(outputpath, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
        
    print("Completed")
    
import re
def return_skills():
    text_file = open('skills.txt', "r")
    lines = re.split('\t|\n',text_file.read())
    lines = [x.lower() for x in lines]
    text_file.close()
    return lines


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
#    text1 = text.decode().split('\n')
    text1 = set(re.split("\n|\n\n|,",text.decode()))
    text1 = list(text1)
    text2 = []
    for i in range(0, len(text1)):
        st = text1[i]
        text2.append(st)
        listt = st.split(' ')
        text2.extend(listt)
    text1 = text2
    text1 = [x.lower() for x in text1]
    fp.close()
    device.close()
    retstr.close()
    return text1

def common_member(a, b): 
    common = set()
    a_set = set(a) 
    b_set = set(b) 
    common = (a_set & b_set)
    return common

