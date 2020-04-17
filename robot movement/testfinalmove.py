import speech_recognition as sr
import serial
import time
from gtts import gTTS
import os
arduinoData=serial.Serial("COM13",9600)
time.sleep(2)        #waits for connection to establish
def questionr():
  mytext= "turn me on"
  language='en'
  myobj = gTTS(text=mytext, lang=language, slow=False)
  myobj.save("commandini.mp3")
  os.system("commandini.mp3")
def questioncmd():
  otext= "ready for another command"
  language='en'
  mlobj = gTTS(text=otext, lang=language, slow=False)
  mlobj.save("commandini1.mp3")
  os.system("commandini1.mp3")
def warnmessg():
  ltext= "there is an obstacle in the path, linearly"
  language='en'
  mmobj = gTTS(text=ltext, lang=language, slow=False)
  mmobj.save("error.mp3")
  m_stop()
  os.system("error.mp3")
def warnmessg1():
  mtext= "command not recognised"
  language='en'
  mnobj = gTTS(text=mtext, lang=language, slow=False)
  mnobj.save("error1.mp3")
  m_stop()
  os.system("error1.mp3")
def m_forward():
   arduinoData.write('1'.encode())
   time.sleep(3)
def m_right():
   arduinoData.write('3'.encode())
   time.sleep(3)
def m_left():
   arduinoData.write('4'.encode())
   time.sleep(3)

def m_back():
   arduinoData.write('2'.encode())
   time.sleep(3)
def m_stop():
   arduinoData.write('5'.encode())
   time.sleep(3)
def commandrec():
  questioncmd()
  while (1==1):
      if(arduinoData.inWaiting()>0):
          myData = arduinoData.read()
          if(myData > 5):
              r = sr.Recognizer()
              with sr.Microphone() as source:
                  r.pause_threshold = 1
                  r.adjust_for_ambient_noise(source, duration=1)
                  audio = r.listen(source)
                  x = r.recognize_google(audio)
                  print("you said : " + x)

          if "forward" in x.split():
              m_forward()
          elif "back" in x.split():
              m_back()
          elif "right" in x.split():
              m_right()
          elif "left" in x.split():
              m_left()
          elif "stop" in x.split():
              m_stop()
          else:
              warnmessg1()
      else:
          warnmessg()

questionr()
while 1 :
  commandrec()