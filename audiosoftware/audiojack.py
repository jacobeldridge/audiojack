import eel
import random
from datetime import datetime
from playsound import playsound
import os
from pynput.keyboard import Key, Listener

sounds=[]
order=[]
numberofloops = 0
songcounter = 0
loopbool = False
textfile = open("web/everything/song_order.txt", "r")


for line in textfile:
  stripped_line = line.rstrip()
  sounds.append(stripped_line)
textfile.close()



# def filescheck():
#     global sounds
    
#     newsounds = []
#     for fname in os.listdir('web\_audio_'):

#         if fname.endswith('.wav') or fname.endswith('.wav'):
#             # do stuff on the file
            
#             newsounds.append(fname)
            

#         else:
#             print("noooo stuuff")
#             return False
#     if newsounds == sounds:
#         pass

#     else:
#         sounds = newsounds
        
#     return True

eel.init('web')


@eel.expose
def eelstoppy():
    return
@eel.expose
def play(): 
    for i in range(numberofloops + 1):
        playsound("web/everything/_audio_/"+sounds[songcounter])
            

@eel.expose
def loop(num):
    global numberofloops  
    numberofloops = num


@eel.expose
def crease(num):
    global songcounter
    global sounds
    numcheck = songcounter + num
    if numcheck in range(0, len(sounds)):
        songcounter = numcheck    
    else:
        pass

@eel.expose
def effectpy():
    return str(sounds[songcounter] + "\n"+str(songcounter))     
    


@eel.expose
def getlist():
    return sounds

    




eel.start('index.html')
