import speech_recognition as sr
import serial
import time
from gtts import gTTS
import os

arduinoData = serial.Serial("COM8", 9600)
time.sleep(2)  # waits for connection to establish


def questionr():
    mytext = "turn me on"
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("commandini.mp3")
    os.system("commandini.mp3")


def questioncmd():
    otext = "ready for another command"
    language = 'en'
    myobj = gTTS(text=otext, lang=language, slow=False)
    myobj.save("commandini1.mp3")
    os.system("commandini1.mp3")
    time.sleep(2)


def warnmessg():
    ltext = "there is an obstacle in the path, linearly"
    language = 'en'
    myobj = gTTS(text=ltext, lang=language, slow=False)
    myobj.save("error1.mp3")
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

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result


def commandrec():
    questioncmd()
    while (1 == 1):
        if (arduinoData.inWaiting() > 0):
            myData=bytes_to_int(arduinoData.read())
            print(myData)
            if (myData > 5):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('Ready...')
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    x = r.recognize_google(audio)
                    print("you said" + x)

                if (x[0] == 'f'):
                    m_forward()
                if (x[0] == 'b'):
                    m_back()
                if (x[0] == 'l'):
                    m_left()
                if (x[0] == 'r'):
                    m_right()


        else:
            warnmessg()
            commandrec()


questionr()
while 1:
    commandrec()
