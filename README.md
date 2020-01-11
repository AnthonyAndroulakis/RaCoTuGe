# RaCoTuGe
Random & Constrained Tune Generator      

# prerequisites:
Mac OS      
python 3      
python modules:      
+ midiutil      
+ audiolazy      
+ numpy      

# running RaCoTuGe:
cd into RaCoTuGe directory      
```
chmod +x ./racotuge.sh      
```
```
./racotuge.sh 100 #for 100 tunes (.txt, .mid, and .wav files generated)      
```

# if you do not have Mac OS:
in python3 interpreter:     
`from run import maketune`      
`maketune(100) #for 100 tunes`  
only .mid and .txt files will be generated (no .wav files)

# Randomizations and Constraints:
```
### Semi-randomized (why? to control composer biases):
# randomized scale out of: (Maj: C,G,D,A,E,F,Bb,Eb,Ab; REL HARMONIC MINOR; no-sharps/flats + up-to-4-sharps/flats; 18 choices)
# randomized note in scale, can be anywhere in middle 3 octaves, 36 choices
# randomized tempo: 100-200 quarter notes per minute
# randomized note durations out of: options are eighth, quarter, dotted quarter, half, dotted half, whole


### Constrained (why? to ensure singability and relative memorability):
# at most 1 jump of a 3rd
# if eight note is not following a dotted quarter, only goes in one direction either 2 or 4 eighth notes (at note directly following has to be in same direction)
# if there's a dotted quarter note, it has to be directly followed by an eighth note
# dotted half and whole only allowed at end
#each tune must by exactly 3 seconds long
# if 4 notes long, at least 2 in same direction (1 move)
# if 5 notes long, at least 3 in same direction (2 moves)
# if 6 or 7 notes long, at least 4 in same direction (3 moves)
# if 8 notes in same direction, either: at least 5 notes in same direction, or 3 and 3 each in same directions
```
