#Anthony Androulakis, 2019

from midiutil import *
import math
from racotuge import tune
import makematrix

def makemidi(tunenumber):

    (midipitches,rhythm,truetempo,key,scale,sharporflat,pitchintervals)=tune() #get outputs of racotuge.py
    while False in [False if abs(x)>2 else True for x in [j-i for i, j in zip(midipitches[:-1], midipitches[1:])]]:
        (midipitches,rhythm,truetempo,key,scale,sharporflat,pitchintervals)=tune() #keep on running until no errors occur...

    makematrix.makeit(midipitches, rhythm, truetempo, tunenumber)
    
    listscale=['C','G','D','A','E','Am','Em','Bm','F#m','C#m','F','Bb','Eb','Ab','Dm','Gm','Cm','Fm']
    listscalenums=[0,1,2,3,4,0,1,2,3,4,1,2,3,4,1,2,3,4] #each element corresponds to number of sharps or flats in key

    track    = 0
    channel  = 0
    time     = 0    # In beats
    tempo    = truetempo   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                          # automatically)

    MyMIDI.addTempo(track, time, tempo)

    if 'm' not in key:
        if sharporflat=='sharp':
            MyMIDI.addKeySignature(0, 0, listscalenums[scale], SHARPS, MAJOR)
        else:
            MyMIDI.addKeySignature(0, 0, listscalenums[scale], FLATS, MAJOR)
    else:
        if sharporflat=='sharp':
            MyMIDI.addKeySignature(0, 0, listscalenums[scale], SHARPS, MINOR)
        else:
            MyMIDI.addKeySignature(0, 0, listscalenums[scale], FLATS, MINOR)

    MyMIDI.addTimeSignature(track, time, math.ceil(4*sum(rhythm)), 2, 24, notes_per_quarter=8)

    sumtime=0
    for i in range(len(midipitches)):
        MyMIDI.addNote(track, channel, midipitches[i], sumtime, rhythm[i]*4, volume)
        sumtime+=rhythm[i]*4

    tunenumber+=1
    print('TUNE TUNE TUNE TUNE TUNE')
    print('TUNE '+str(tunenumber))
    print('TUNE TUNE TUNE TUNE TUNE')

    with open("tunes/mid/tune"+str(tunenumber)+".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
