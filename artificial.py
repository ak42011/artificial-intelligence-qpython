import androidhelper
import urllib.request
import time
import requests
from bs4 import BeautifulSoup
import datetime


droid = androidhelper.Android() 

republic1="Republic Day is a national holiday in India. It honours the date on which the Constitution of India came into effect on 26 January 1950 replacing the Government of India Act as the governing document of India and thus, turning the nation into a newly formed republic."

#TEMPERATUTE WEATHER
def temperature():
    
    url = requests.get("http://google.com/search?q=weather+report")
    
    url=url.text
    
    soup=BeautifulSoup(url,"html5lib")
    
    d=soup.find("div",{"class":"tAd8D"})
    
    e=soup.find("div",{"class":"iBp4i"})
    
    
    speck("temperature is "+e.text)
    
def wiki(search):
    
    search=search.replace("wikipedia search"," ")
    search=search.replace(" ","+")
    url= urllib.request.urlopen("https://en.m.wikipedia.org/w/index.php?search="+search+"&title=Special%3ASearch&profile=default&fulltext=1&ns0=1")
    bu= BeautifulSoup(url,"html5lib")
    bi= bu.select(".mw-search-result-heading a")
    bk=bi[0].get("href")
    url= urllib.request.urlopen("https://en.m.wikipedia.org/"+bk)
    bu= BeautifulSoup(url,"html5lib")
    a= bu.find_all("p")
    for i in a[:]:
        if len(i)==0 or len(i)==1:
            pass
        else:
            spr=i.text
            se=spr.split(".")
            for l in  se[:5]:
                print(l)
            speck(i.text)
            break
    
def meaning(men):
    
     
    url = requests.get("http://google.com/search?q=+"+men+"+meaning+in+hindi")
    
    url=url.text
    
    soup=BeautifulSoup(url,"html5lib")
    
    a=soup.find("div",{"id":"lrtl-transliteration-text"})
    
    speck(a.text)

#CALL
def call():
    
    #v=droid.pickContact()
    
    b=input("dial number:")
    
    droid.startActivity("android.intent.action.VIEW",uri="tel:"+b)
    
#NAME

def name():
    
    speck('my  name  is   lakshmi  kumari.')                                        

#INTRODUCTION OF LAKSHMI
      
def artificial():
    
    speck('my  name  is  lakshmi  kumari. I  am  artificial  intelligence .  avinash  kumar   abhay   and  vivek  build  me  on  the  26   january  2021.')   
      
    
def date():
    
    dat= str(datetime.datetime.now().day)
    
    speck("the current date is:")
    
    speck(dat)
    
    dat= str(datetime.datetime.now().month)
    
    speck(dat)
    
    dat= str(datetime.datetime.now().year)
    
    speck(dat)
    
    
#TIME 
def Time():
    
    tim= datetime.datetime.now().strftime("%I:%M:%S")
    
    speck("the current time is "+tim)
        
    
#MUSIC PLAYER

def music():
    
    droid.mediaPlay("/sdcard/26.mp4")
    
#MY  LOCATION

def location():
    
    droid.view("https://www.google.com/maps")
  
#OPEN GOOGLE PLAY STORE

def playStore():
    
    droid.view("https://play.google.com")
    
   
def googleDrive():
    
    droid.view("https://drive.google.com/file/d/1VcFLN71OrgjdB7EocVvlCHy8LErOpS6D/view?usp=drivesdk")  
     
#OPEN GOOGLE CHROME

def openGoogle():
    
    droid.startActivity(action="android.intent.action.VIEW",uri="http://www.google.com")

def searchGoogle(sr):
    
    droid.startActivity(action="android.intent.action.VIEW",uri="http://www.google.com/search?q="+sr)

#OPEN GALLERY CHROME

def openGalary():
    
    droid.startActivity(action="android.intent.action.VIEW",uri="content://",type="image/*")

#WISH  REPUBLIC DAY

def wishRepublic():
    
    droid.mediaPlay("/sdcard/qpython/scripts3/music/wish.mp3")                                          


# WEATHER REPORT

def weather():
    
    temperature()

#OPEN YOUTUBE

def openYoutube():
    
    droid.startActivity(action="android.intent.action.VIEW",uri="https://youtu.be/9w18bnz5Yts")

#OPEN FACEBOOK

def openFacebook():
    
    droid.startActivity(action="android.intent.action.VIEW",uri="http://www.facebook.com")

#SPEECH  RECOGNITION

def voice():
    
    speech= droid.recognizeSpeech()
    
    return speech.result

#ASSISTENT  SPEAK

def speck(sound):
    
    droid.ttsSpeak(sound)

#speck(voice())
run=True
Time()
date()
while run:
    
  print("\033[02J")
  
  print("\033[0;0H")
  
  
  ab= input("press enter too speak ....")
  
  if ab=='stop':
      
      speck(' ')
      
  if ab=='exit':
      
      break
      
  sp=str(voice()).lower()
  
   
  if 'bye' in sp:
      
      
      speck("thank you sir. i  hope  you enjoy. jay bhim")                                         

      
      run=False
      
  elif 'what is republic day' in sp:
      
      speck(republic1)
      
  elif 'when india celebrating republic day' in sp:
      
      #speck("Every  year  Republic  Day  is  celebrated  in  India  on  26th  January  with  zeal  and  enthusiasm. Spectacular  parades  at  Janpath, New Delhi, consisting the Indian National Army and national flag hoisting in various parts of the country are common practices followed on this day ")
      pass
  elif 'what is constitution' in sp:
      
      speck("A constitution is an aggregate of fundamental principles or established precedents that constitute the legal basis of a polity, organisation or other type of entity and commonly determine how that entity is to be governed")
      
  elif 'open youtube' in sp:
      
      openYoutube()
      
      speck("youtube is  open")
  
  elif 'open google' in sp:
      
      openGoogle()
      
      speck("google is  open") 
     
  elif 'open facebook' in sp:
      
      openFacebook()
      
      speck("facebook is  open")
           
  elif 'open gallery' in sp:
      
      openGalary()
      
      speck("gallery is  open")
  
  elif 'play music' in sp :
      
      music()
      
      speck("enjoy")
  
  elif 'search google' in sp :
      
      sp=sp.replace("search google",'')
      
      searchGoogle(sp)
      
  elif 'wikipedia search' in sp :
         
      wiki(sp)
      
  elif 'meaning of' in sp:
      
      sp=sp.replace("meaning of",' ')
      meaning(sp)
      
  elif 'my location' in sp :     
      
      location()
            
  elif 'play store' in sp :     
      
      playStore()
            
  elif 'google  drive ' in sp:
      
      googleDrive()
    
  elif 'who are you' in sp:
      
      artificial()
      
  elif 'introduce yourself' in sp:
      
      artificial()
        
  elif 'what is your name' in sp:
      
      name()
   
  elif 'bhim' in sp:  
      
      speck("he was born on 14 april 1891.he was  independent  India's  first  Minister  of  Law  and  Justice,  and  considered  as  the chief  architect  of  the  Constitution  of   India,  and  a  founding  father  of  the  Republic  of  India ")
   
  elif 'nehru' in sp:
      
      speck("he was born on 14 November 1889.he was an Indian independence activist and, subsequently, the first Prime Minister of India, as well as a central figure in Indian politics both before and after independence")
      
  elif 'patel' in sp:
      
      speck('Vallabhbhai Jhaverbhai Patel (31 October 1875 – 15 December 1950), popularly known as Sardar Patel, was an Indian politician. He served as the first Deputy Prime Minister of India')
   
  elif 'prasad' in sp:
      
      speck('Rajendra Prasad (3 December 1884 – 28 February 1963) was an Indian independence activist, lawyer, scholar and subsequently, the first President of India, in office from 1950 to 1962.')
   
  elif 'gandhi' in sp:
      
      speck("Mohandas Karamchand Gandhi, also known as Mahatma Gandhi, was an Indian lawyer, anti-colonial nationalist, and political ethicist, who employed nonviolent resistance to lead the successful campaign for India's independence from British rule, and in turn inspired movements for civil rights and freedom across the world.")
      	
  elif 'time' in sp :
      
      Time()
            
  elif 'date' in sp :
      
      date()
            
  elif 'call' in sp:
      
      call()
      
  elif 'what is artificial intelligence' in sp:
      
      speck("Artificial  intelligence   is  intelligence  demonstrated  by  machines,  unlike  the  natural  intelligence  displayed  by  humans  and  animals,  which  involves  consciousness  and  emotionality")
    
  elif 'who teaching us networking' in sp:
      
      speck("mr  murlidhar  verma  sir  teaching us networking")
      
  elif 'who teaching us programming'  in sp:
      
      speck("mr  naushad ahmad  sir  teaching  as  programming.")
   
  elif 'who is counselor' in sp:
      
      speck("mr upender  sir is  our  counselor")   
         
  elif 'director' in sp:
      
      speck("mr mohan sir  is a  director of  m i m t college")    
   
  elif 'who is aunty' in sp:
      
      speck("sheela  devi  is  aunty  ji  in m i m t  college")  
      
  elif 'who teaching us financial' in sp:
      
      speck("mr.  akram sir teaching us  financial")
            
  elif 'stupid' in sp:    
  
      speck("sorry  sir  i  trying to do my best")  
      
  elif 'how are you' in sp:
      
      speck("i  am  good  tell me  about  yourself")    

  elif 'temperature' in sp:
      
      weather()   
 
  elif 'who build you' in sp:
      
      speck("avinash kumar  vivek  and  abhay  build me.")                                     
  
  elif 'father' in sp:
      
      speck("avinash kumar  vivek  and  abhay  build me so  they  are  my  every thing")                                     
  
  elif 'mother' in sp:
      
      speck("my  engineer  are  every  things  for me.")
      
  else:      
    
      speck("i  am  not  understanding ...")
