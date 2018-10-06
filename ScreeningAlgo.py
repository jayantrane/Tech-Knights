# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:42:44 2018

@author: Jayant
"""

import numpy as np
import pandas as pd
import jslib

import pandas as pd
import smtplib

datafile = pd.read_csv('kjsce.csv')
finaldata = pd.DataFrame();
skills = jslib.return_skills()
#Github Links
fields = {'frontend' : ['html','css','bootstrap'],
'backend': ['mysql'],
'frameworks' : ['flask','php'],
'coding' : ['competitive programming','c','cpp','java','python'],
'ai' : ['machine learning', 'deep learning'],
'development': ['android studio','arduino programming'] }
imp_skills =[]
for k, v in fields.items():
    imp_skills.extend(v)

#normalize scores
nohackwon_h = 3
nohackwon_l = 0
nohack_h = 10
nohack_l = 0
skillcount_h = 20
skillcount_l = 3
gitpublicrepos_h = 35
gitpublicrepos_l = 4
gitfollowers_h = 20
gitfollowers_l = 0

def init():
    for i in range(0,len(datafile)):
        name = datafile.loc[i,'Name']
        email = datafile.loc[i,'Email Address']
        mobno = datafile.loc[i,'Mobile Number']
        clgname = datafile.loc[i,'College name ']
        resumelink = datafile.loc[i,'Resume']
        nohackwon = datafile.loc[i,'No of Hackathons Won']
        nohack = datafile.loc[i,'No of Hackathons']
        githublink = datafile.loc[i,'Github Link']
        appliid = i+1
        
        finaldata.loc[i,'application_id'] =  appliid
        finaldata.loc[i,'name'] = name
        finaldata.loc[i,'email'] = email
        finaldata.loc[i,'mobno'] = mobno
        finaldata.loc[i,'nohackwon'] = nohackwon
        finaldata.loc[i,'nohack'] = nohack
        
        #Spliting text and finding 3rd element
        githublinksplit = githublink.split('/')
        username = githublinksplit[3]
        #Makng url
        account_info = jslib.get_account_info(username)
        
        finaldata.loc[i,'gitpublicrepos'] = account_info['public_repos']
        finaldata.loc[i,'gitfollowers'] = account_info['followers']
        gitpublicrepos = account_info['public_repos']
        gitfollowers=account_info['followers']
        #Resume
        #resumepath = 'resume/'+'sdf.pdf'
        
        path = 'resume/'+str(appliid)+'.pdf'
        resumedata = jslib.convert_pdf_to_txt(path)
        interests = jslib.common_member(resumedata, skills)
        interests.remove('')
        skillcount = 0
        for k, v in fields.items():
            finaldata.loc[i,k] = False
            for ii in v:
                if ii in interests:
                    skillcount+=1
                    finaldata.loc[i,k] = True
        finaldata.loc[i,'skillcount'] = skillcount
                
        interest =  ','.join(list(interests))
        finaldata.loc[i,'interests']  = interest
        
        #give_ranking
        
        
        try:
            norm_nohackwon = (nohackwon-nohackwon_l)/(nohackwon_h-nohackwon_l)
            if norm_nohackwon<0 and nohackwon>nohackwon_h:
                norm_nohackwon = 1
            elif norm_nohackwon<0:
                norm_nohackwon = 0
        except:
            norm_nohackwon = 0
        try:
            norm_nohack = (nohack-nohack_l)/(nohack_h-nohack_l)
            if norm_nohack<0 and nohack>nohack_h:
                norm_nohack = 1
            elif norm_nohack<0:
                norm_nohack = 0
        except:
            norm_nohack=0
        try:     
            norm_skillcount = (skillcount-skillcount_l)/(skillcount_h-skillcount_l)
            if norm_skillcount<0 and skillcount>skillcount_h:
                norm_skillcount = 1
            elif norm_skillcount<0:
                norm_skillcount = 0
        except:    
            norm_skillcount=0
        try:
            norm_gitpublicrepos = (gitpublicrepos-gitpublicrepos_l)/(gitpublicrepos_h-gitpublicrepos_l)
            if norm_gitpublicrepos<0 and gitpublicrepos>gitpublicrepos_h:
                norm_gitpublicrepos = 1
            elif norm_gitpublicrepos<0:
                norm_gitpublicrepos = 0
        except:  
            norm_gitpublicrepos=0
        try:
            norm_gitfollowers = (gitfollowers-gitfollowers_l)/(gitfollowers_h-gitfollowers_l)
            if norm_gitfollowers<0 and gitfollowers>nohackwon_h:
                norm_gitfollowers = 1
            elif norm_gitfollowers<0:
                norm_gitfollowers = 0
        except:
            norm_gitfollowers=0
            
        norm_score = norm_nohackwon+norm_nohack+norm_skillcount+norm_skillcount+norm_gitpublicrepos+norm_gitfollowers
        finaldata.loc[i,'norm_score']  = norm_score
        
        finaldata.sort_values('norm_score', inplace=True,ascending=False)
        
        #print(interests)
    
    finaldata.to_csv('finaldata.csv',index=False)
    
def mail_shortlist(filename, evename, noofcandidates):
    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    #Next, log in to the server
    server.starttls()
    server.login("shreyakhatal1@gmail.com", "srkvij015")
    file=pd.read_csv(filename)
    n=int(noofcandidates)
    for i in range(0,n):
        email_id=file.loc[i,'email']
        server.sendmail("shreyakhatal1@gmail.com",email_id, "You are shortlisted for event "+evename+"\nCongratulation")
        print("Mail sent to "+ email_id)
    return 

def find_potential_candidates(eventname, requirement, noofcandidates):
    init()
    requirement = requirement.split(' ')
    #for i in requirement:
        #for k, v in fields.items():
           # if i!=k:
             #   requirement.remove(i)
            
    finaldata = pd.read_csv('finaldata.csv')
    ename = pd.DataFrame(columns=['name','email'])
    #print(eventname)
    listt = []
    count = -1
    for j in range(0,len(finaldata)):
        for i in requirement:
            if finaldata.loc[j,i]==True:
                count+=1
                listt.append(j)
                ename.loc[count]=[finaldata.loc[j,'name'],finaldata.loc[j,'email']]
#                ename['Name'] = finaldata.loc[j,'name']
#                ename['Email'] = finaldata.loc[j,'email']
    strin = eventname+'.csv'
    ename.to_csv(strin,index=False)
    x = mail_shortlist(strin, eventname, noofcandidates)


def search_for_interest(v):
    listt = []
    for i in range(0, len(finaldata)):
        flag = False
        interests = finaldata.loc[i,'interests'].split(',')
        for j in interests :
            if j in v :
                listt.append(i)
                flag = True
    return listt
    


