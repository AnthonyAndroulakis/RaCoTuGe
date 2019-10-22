#Anthony Androulakis, 2019

from makeMIDI import makemidi

def maketune(num): #num = number of tunes to make
    for tunenumber in range(num):
        makemidi(tunenumber)

#maketune(5) #make 5 tunes and place them all in the racotuge/tunes/mid folder
