# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 07:55:17 2020

@author: Deepanshu
"""

def tuber():
    print("Select the symptoms that you are getting")
    print("press 1 if you are Feeling pain in the chest else 0")
    y=int(input())
    print("press 1 if you are not feeling pain but having cough else 0")
    y1=int(input())
    print("press 1 if you are coughing for last 2 or 3 days else 0")
    y2=int(input())
    print("press 1 if you are coughing for last 1 months else 0")
    y3=int(input())
    print("press 1 if you are bleeding while coughing else 0")
    y4=int(input())
    if y==1 and y3==1 and y4==1 :
        print("++++You are having symptoms of tuberculosis++++")
    else:
        print("++++you are having normal viral++++")
    
def Dia():
    print("Select the symptoms that you are getting")
    print("press 1 if you are having loose motion inbetween every hours else press 0")
    y=int(input())
    print("press 1 if you are facing abdominal cramp else 0")
    y1=int(input())
    print("press 1 if you are having blood in stool else press 0")
    y2=int(input())
    print("press 1 if you are having mucous instool else press 0")
    y3=int(input())
    if y==1 and y1==1 and y2==1 and y3==1:
        print("++++you are having symptoms of Diarohhea++++")
    else:
        print("++++you are safe from diarohea++++")

def cholera():
    print("Select the symptoms that you are getting")
    print("press 1 if you are vomiting for more then 1 day else press 0")
    y=int(input())
    print("press 1 if you are feeling dehydrated on hourly basis else press 0")
    y1=int(input())
    print("press 1 if you are having muscle cramp else press 0")
    y2=int(input())
    print("press 1 if you are feeling like shock in your body else press 0")
    y3=int(input())
    if y==1 and y1==1 and y2==1 and y3==1:
        print("++++ you are having symptoms of cholera ++++")
    else:
        print("++++ you are safe from cholera ++++")

def corona():
    print("Select the symptoms that you are getting")
    print("press 1 if you are getting water from your nose else 0")
    y=int(input())
    print("press 1 if you are having pain in your head else 0")
    y1=int(input())
    print("press 1 if you face anykind of problem during respiration else press 0")
    y2=int(input())
    print("press 1 if you are having cold else press 0")
    y3=int(input())
    print("press 1 if you are sneezing from more then 4 days else 0")
    y4=int(input())
    if y==1 and y1==1 and y2==1 and y4==1:
        print("++++ you are having symptoms of COVID 19 virus ++++")
    else:
        print(" ++++you are safe from covid 19 virus and having normal fever contact your doctor ++++")

def dib():
    print("Select the symptoms that you are getting")
    print("press 1 if you are peeing more often and being thirstier else press 0")
    y=int(input())
    print("press 1 if you are having dry mouth and itchy skin else press 0")
    y1=int(input())
    print("press 1 if you are observing continuess loss in your weight over a constant period of time else press 0")
    y2=int(input())
    print("press 1 if you are observing a blurred vision in recent interval of time else press 0")
    y3=int(input())
    if y==1 and y1==1 and y2==1 and y3==1:
        print("++++ you are having symptoms of Dibatese ++++")
    else:
        print("++++ you are safe from Dibatese ++++")
    
def asthma():
    print("Select the symptoms that you are getting")
    print("press 1 if you are facing any problem in repiration else press 0")
    y=int(input())
    print("press 1 if you are facing it for more then a month else press 0")
    y1=int(input())
    print("press 1 if you feel any respiratory problem while jogging or running else press 0")
    y2=int(input())
    if y==1 and y1==1 and y2==1:
        print("++++ you are having symptoms of Asthma ++++")
    else:
        print("++++ you are safe from Asthma ++++")

def jaundice():
    print("Select the symptoms that you are getting")
    print("press 1 if you are facing abdominal pain else press 0")
    y=int(input())
    print("press 1 if you are vomiting in last couple of days else press 0")
    y1=int(input())
    print("press 1 if you are having dark urine as compared to normal else 0")
    y2=int(input())
    print("press 1 if you are feeling like fever every time else press 0")
    y3=int(input())
    if y==1 and y1==1 and y2==1 and y3==1:
        print(" ++++ you are having symptoms of Jaundice ++++")
    else:
        print("++++ you are safe from Jaundice ++++")
        
def loose():
    print("Select the symptoms that you are getting")
    print("press 1 if you are having pain in your stomach else press 0")
    y=int(input())
    print("press 1 if you are running towards toilet in every 1/2 hours else press 0")
    y1=int(input())
    if y==1 and y1==1:
        print("++++ you are having symptoms of Loose motions ++++")
    else:
        print("++++ you are safe from Loose motions ++++")
        
def mal():
    print("Select the symptoms that you are getting")
    print("press 1 if you are having cold above 100 degree else press 0")
    y=int(input())
    print("press 1 if you are feeling headache else press 0")
    y1=int(input())
    print("press 1 if you are facing chills else press 0")
    y2=int(input())
    print("press 1 if you are facing muscle pain and fatigue else press 0")
    y3=int(input())
    if y==1 and y1==1 and y2==1 and y3==1:
        print(" ++++ you are having symptoms of Malaria ++++ ")
    else:
        print(" ++++ you are safe from Malaria ++++ ")
        
def cough():
    print("+++ if you are coughing from more then 3 days you are having symptoms of other diseases like tuberculosis go and search for that disease!!! ++++")   

print("**********welcome in district hospital**********")
print("press 1 if you want checkup")
print("press 2 if you want your report")
print("press 3 if you want to buy medicines")
choice=int(input())
if choice==1:
    print("select the kind of disease for which you want checkup")
    print("press 1 for Tuberculosis")
    print("press 2 for Diarohea")
    print("press 3 for Cholera")
    print("press 4 for Chorona")
    print("press 5 for Diabetese")
    print("press 6 for Asthama")
    print("press 7 for Jaundise")
    print("press 8 for Loose Motion")
    print("press 9 for Malaria")
    print("press 10 for Coughing")
    disease=int(input())
    if disease==1:
        tuber();
    if disease==2:
        Dia();
    if disease==3:
        cholera();
    if disease==4:
        corona();
    if disease==5:
        dib();
    if disease==6:
        asthma();
    if disease==7:
        jaundice();
    if disease==8:
        loose();
    if disease==9:
        mal();
    if disease==10:
        cough();
if choice==2:
    print("your report is ready you have to cantact to pathology labs for further")
choice=int(input())
if choice==3:
    print("you have to contact to medical shop inside or outside the hospital")
choice=int(input())
