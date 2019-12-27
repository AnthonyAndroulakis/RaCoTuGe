#Anthony Androulakis, 2019
#random & constrained tune generator (racotuge)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#durations: indicated by proportions, so quarter note is 1/4, whole note is 1, etc.
#notes: indicated as follows, 1-25, 48-83, C3-B5

###Randomized (why? to remove uncontrollable composer biases):
#randomized scale (Maj: C,G,D,A,E,F,Bb,Eb,Ab; REL HARMONIC MINOR; no-sharps/flats + up-to-4-sharps/flats; 18 choices)
#randomized note in scale, can be anywhere in keyboard, 36 choices
#randomized tempo: 100-200 quarter notes per minute
#randomized note durations: options are eighth, quarter, dotted quarter, half, dotted half, whole


###Constrained (why? to ensure singability and relative memorability):
#at most 1 jump of a 3rd
#if eight note is not following a dotted quarter, only goes in one direction either 2 or 4 eighth notes (at note directly following has to be in same direction)
#if there's a dotted quarter note, it has to be directly followed by an eighth note *
#at most 3 quarter notes moving in the same direction X DO NOT DO THIS
#no consecutive: dotted quarter, half, dotted half, or whole X DO NOT DO THIS
#dotted half and whole only allowed at end *
#each tune must by exactly 3 seconds long *
#if 4 notes long, at least 2 in same direction (1 move)
#if 5 notes long, at least 3 in same direction (2 moves)
#if 6 or 7 notes long, at least 4 in same direction (3 moves)
#if 8 notes in same direction, at least 5 notes in same direction, or 3 and 3 each in same directions (4 moves, or 2 and 2)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#python3
#racotuge.py
#Anthony Androulakis, 2019

import random
import itertools
import numpy as np

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*STEP 1: FIND FIRST NOTE, KEY, AND ATTEPTED TEMPO*#*#*#*#*#*#*#*#*#*#*#*#*##
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

def tune():
    #####for visual representation of melodies##### vvvvv
    allnotessharp=['C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5']
    allnotesflat=['C3','Db3','D3','Eb3','E3','F3','Gb3','G3','Ab3','A3','Bb3','B3','C4','Db4','D4','Eb4','E4','F4','Gb4','G4','Ab4','A4','Bb4','B4','C5','Db5','D5','Eb5','E5','F5','Gb5','G5','Ab5','A5','Bb5','B5']
    ##########

    #this decision stays consistent vvvvv
    listscale=['C','G','D','A','E','Am','Em','Bm','F#m','C#m','F','Bb','Eb','Ab','Dm','Gm','Cm','Fm']
    scale=random.randint(0,17)
    tempo=random.randint(100,150) #quarter note gets the beat, ##program will try to match this tempo, but no guarantees can be made
    numnotes=random.randint(4,8)
    wholetempo=tempo/4 #whole note gets the beat

    if 'C' in listscale[scale] and '#' not in listscale[scale]: #next 4 lines are here to prevent error "IndexError: list index out of range" from occurring when the scale is built
        startingOctave=random.randint(3,5)
    else:
        startingOctave=random.randint(3,4)

    #startingOctave=random.randint(3,5)

    options=listscale[scale]

    print('key: '+listscale[scale])
    print('attempted tempo: '+str(tempo))
    print('number of notes (not guaranteed): '+str(numnotes))
    #print('whole tempo: '+str(wholetempo))
    print('###########')

    #finding location of first note vvvvv
    #for loc in range(0,36): #for all possible keys
    if scale in range(0,10): #if scale with sharps
        sharporflat='sharp'
        if 'm' not in options: #if major
            for loc in range(0,36): #for all possible keys
                if allnotessharp[loc]==listscale[scale]+str(startingOctave): #if note found
                    location=loc #set location number
                    break #then break loop
        else: #if minor
            for loc in range(0,36): #for all possible keys
                if allnotessharp[loc]==listscale[scale][0:-1]+str(startingOctave):
                    location=loc
                    break
    else: #if scale with flats
        sharporflat='flat'
        if 'm' not in options: #if major
            for loc in range(0,36): #for all possible keys
                if allnotesflat[loc]==listscale[scale]+str(startingOctave): #if note found
                    location=loc #set location number
                    break #then break loop
        else: #if minor
            for loc in range(0,36): #for all possible keys
                if allnotesflat[loc]==listscale[scale][0:-1]+str(startingOctave):
                    location=loc
                    break

    print('sharp or flat?: '+sharporflat)
    print('location: '+str(location))
    print('###########')

    #pitch options (in other words, the scale spelled out) vvvvv
    major=[2,2,1,2,2,2]
    minor=[2,1,2,2,1,3] #harmonic minor
    if 'm' not in listscale[scale]:
        options=[listscale[scale]+str(startingOctave)] #this is an array with a string
    else:
        options=[listscale[scale][0:-1]+str(startingOctave)]

    sumnum=0
    if sharporflat=='sharp': #check if sharp
        if 'm' not in listscale[scale]: #check if major
            for i in range(0,6):
                sumnum+=major[i]
                options.append(allnotessharp[location+sumnum])
                print(options)
        else: #else if minor
            for i in range(0,6):
                sumnum+=minor[i]
                options.append(allnotessharp[location+sumnum])
                print(options)
    else: #else if flat
        if 'm' not in listscale[scale]: #check if major
            for i in range(0,6):
                sumnum+=major[i]
                options.append(allnotesflat[location+sumnum])
                print(options)
        else: #else if minor
            for i in range(0,6):
                sumnum+=minor[i]
                options.append(allnotesflat[location+sumnum])
                print(options)

    print('scale: ', end =" ")
    print(options)
    print('###########')

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*STEP 2: FIND RHYTHM*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

    #duration options (proportions) vvvvv
    lengthOptions=[0.125,0.125,0.125,0.125,0.25,0.25,0.25,0.375,0.5,0.75] #eighth (40% chance), quarter (30% chance), dotted-quarter (10% chance), half (10% chance), dotted-half (10% chance); 15 bpm=1 quarter note every second
    endingLengthOptions=[0.5,0.75,1] #each with equal probability

    #find, according to picked tempo, how long in proportions can tune last (1=whole note)
    #length=0.25*((3*tempo)/60) #attemping target length according to tempo
    length=(3*wholetempo)/60 #calculate attempted length from whole-notes-per-minute tempo, 3 is there for 3 seconds
    lastduration=random.choice(endingLengthOptions) #pick last note duration
    #print('last duration: '+str(lastduration))
    print('attempted length in number of whole notes in tune: '+str(length))

    ########################here comes the code to decide all the rhythms, thanks user 'AGN Gazer' from 'https://stackoverflow.com/questions/48655612/find-all-numbers-that-sum-closest-to-a-given-number-python'
    numbers=lengthOptions
    target=[length-lastduration]

    #numbers = numbers[:]
    for t in target:
        if not numbers:
            break
        combs = sum([list(itertools.combinations(numbers, r))
        for r in range(1, len(numbers)+1)], [])
        combssums = np.asarray(list(map(sum, combs))) #this is directly linked to tempo
        combslens = np.asarray(list(map(len, combs))) #must be between 3 and 7 (I'm ignoring the last note, which is picked before this function is run)

        TUPLElocsofcorrectlength=np.where(np.logical_and(combslens>=(numnotes-1), combslens<=(numnotes-1))) #find locations of lens where len is between 4 and 8 notes
        locsofcorrectlength=list(itertools.chain.from_iterable(TUPLElocsofcorrectlength)) #tuple to list

        newcombs=[]
        for i in range(len(locsofcorrectlength)):
            newcombs.append(combs[locsofcorrectlength[i]])
        newcombssums = np.asarray(list(map(sum, newcombs))) #this is directly linked to tempo
            
        bestnewcomb = newcombs[np.argmin(np.abs(np.asarray(newcombssums) - t))] #this is of type tuple

        truewholetempo=(60*(sum(bestnewcomb)+lastduration))/3
        truetempo=truewholetempo*4
        truelength=sum(bestnewcomb)
        
        print("Target length (beats) (without last duration): {}, target tempo: {}, combination: {}, true tempo: {}, true length (beats) (without last duration): {}, total duration (seconds) (with last duration): {}".format(t, tempo, bestnewcomb, truetempo, truelength, (60*(truelength+lastduration))/(truetempo/4)))

    #print('test rhythm:')
    #print([i for i in bestnewcomb])
    rhythm=[i for i in bestnewcomb]
    random.shuffle(rhythm) #shuffle rhythm to ensure randomness, last duration is not added yet
    rhythm.append(lastduration)

    print('rhythm: ', end =" ")
    print(rhythm)
    print('###########')
    ########################


    ########################here comes the code to find odd occurrences of 0.375 in rhythm, thanks 'https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/'
    def getOddOccurrence(arr): 
        for i in range(0,len(arr)): 
            count = 0
            for j in range(0, len(arr)): 
                if arr[i] == arr[j]: 
                    count+=1    
            if (count % 2 != 0): 
                return arr[i] 
        return -1
    ########################

    if getOddOccurrence(rhythm)==0.375:
        if 0.125 in rhythm:
            print('0.375 in rhythm, but MOST is good since 0.125 is in there as well...still have to make sure that the 0.125 directly follows the 0.375')
            if rhythm.index(0.375)+1 != rhythm.index(0.125): #if 0.125 does not directly follow 0.375
                placetoputeighth=rhythm.index(0.375)+1 #find (index of 0.375)+1
                rhythm.remove(0.125) #remove 0.125 from it's current spot
                rhythm.insert(placetoputeighth,0.125) #and place 0.125 right after 0.375
                print('new rhythm: ', end =" ")
                print(rhythm)
            else:
                print('0.125 directly follows 0.375. All is good')
        else:
            print('DISREGARD PREVIOUSLY FOUND RHYTHM, TRUE RHYTHM IS LISTED BELOW')
            rhythm = rhythm[:-1] #temporarily cut off the last duration
            placetoaddextra=rhythm.index(0.375) #find where that 0.375 is hiding...
            rhythm.remove(0.375) #remove it
            tobeornottobe=random.choice([0.125, 0.25]) #choose between those two, trying not to change number of notes by too much
            rhythm.insert(placetoaddextra,tobeornottobe) #insert first value in
            rhythm.insert(placetoaddextra+1,0.375-tobeornottobe) #insert second value in
            rhythm.append(lastduration) #and add that last duration back on
            print('new rhythm: ', end =" ")
            print(rhythm)
            numnotes=len(rhythm) #new tune length (technically 1+old tune length)
            print('new tune length: '+str(numnotes)) #print new tune length

    print('###############################')
    print('')
    print('MELODY INFO SO FAR:')
    print('')
    print('Rhythm: ', end =" ")
    print(rhythm)
    print('Tempo: '+str(truetempo))
    print('Key: '+listscale[scale])
    key=listscale[scale]
    print('Pitch options: ', end =" ")
    print([i[:-1] for i in options])
    print('Number of notes: '+str(numnotes))
    print('Tune duration: '+str((60*(truelength+lastduration))/(truetempo/4)))
    print('')
    print('###############################')

    #this decision changes with every note vvvvv

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*STEP 3: FIND REMAINING PITCHES*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*##
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

    #CREATE NEW SCALE FROM OCTAVE 3 TO OCTAVE 5 *****

    fullScaleLocations=[] #initialize as list
    fullscale=[] #initialize as list
    snipoptions=[i[:-1] for i in options]

    if sharporflat=='sharp':
        for s in range(len(snipoptions)):
            fullScaleLocations.append([i for i, x in enumerate([j[:-1] for j in allnotessharp]) if x == snipoptions[s]])
        flattenedlist=sum(fullScaleLocations,[])
        flattenedlist.sort()
        for u in range(len(flattenedlist)):
            fullscale.append(allnotessharp[flattenedlist[u]])
        print('full scale (across octaves): ', end =" ")
        print(fullscale)
    else:
        for s in range(len(snipoptions)):
            fullScaleLocations.append([i for i, x in enumerate([j[:-1] for j in allnotesflat]) if x == snipoptions[s]])
        flattenedlist=sum(fullScaleLocations,[])
        flattenedlist.sort()
        for u in range(len(flattenedlist)):
            fullscale.append(allnotesflat[flattenedlist[u]])
        print('full scale (across octaves): ', end =" ")
        print(fullscale)

    # *****

    #make sure you stay within the boundaries of fullscale, pitches will not be added just yet, only locations
    if numnotes==4: #then len(pitchintervals)=3, none consecutive the same #44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444 NUMNOTES
        #find all permutations, options are -1,1,2 with no restrictions; but 2 is not needed...so first decide between -1 and 1, and then decide whether or not to add 2, then decide where to add 2 if 2 is being added
        allperms=list(itertools.permutations([-1,1,-1,1],3)) #options -1 and 1 with equal probability, 3 decisions to be made, indices will be 0,1,2
        pitchintervals=list(allperms[random.randint(0,len(allperms)-1)]) #this is a list of length 3
        thirdornot=random.choice([0,1]) #choose whether or not a skip of a third should be included
        if thirdornot==1:
            pitchintervals[random.randint(0,2)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
        print('pitch intervals')
        print(pitchintervals)
    elif numnotes==5: #then len(pitchintervals)=4, 2 consecutive the same #555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555 NUMNOTES
        #find all permutations
        pitchintervals=[] #initialize pitchintervals
        allperms=list(itertools.permutations([-1,1,-1,1],4)) #options -1 and 1 with equal probability, 4 decisions to be made, indices will be 0,1,2,3
        while not any(y >=2 for y in [len(list(g[1])) for g in itertools.groupby(pitchintervals) if g[0]==-1 or g[0]==1]): #tests if a repetition of 2 or greater does not exist in list (not made yet)
            pitchintervals=list(allperms[random.randint(0,len(allperms)-1)]) #this is a list of length 4, will keep on picking a list randomly until it finds one with at least [-1,-1] or [1,1]
        #once out of while loop, repetition requirements have been met
        locsofrep=[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([-1,-1])] == [-1,-1], range(len(pitchintervals) - len([-1,-1]) + 1)))) if x == True]+[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([1,1])] == [1,1], range(len(pitchintervals) - len([1,1]) + 1)))) if x == True]
        locsofrep.sort() #locsorrep only contains starting indices of repeated intervals ([-1,-1] or [1,1])
        print('locsofrep: ', end =" ")
        print(locsofrep)
        thirdornot=random.choice([0,1])
        pitchind=[0,1,2,3] #because pitchintervals is of length 4
        parttochop=pitchind.index(random.choice(locsofrep))
        del pitchind[parttochop:parttochop+2]
        print('pitchind: ', end =" ")
        print(pitchind)
        if thirdornot==1:
            pitchintervals[random.choice(pitchind)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
        print('pitch intervals')
        print(pitchintervals)
    elif numnotes==6: #then len(pitchintervals)=5 #6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666 NUMNOTES
        #find all permutations #not done
        pitchintervals=[] #initialize pitchintervals
        allperms=list(itertools.permutations([-1,1,-1,1,-1,1],5)) #options -1 and 1 with equal probability, 5 decisions to be made, indices will be 0,1,2,3,4
        while not any(y >=3 for y in [len(list(g[1])) for g in itertools.groupby(pitchintervals) if g[0]==-1 or g[0]==1]): #tests if a repetition of 3 or greater does not exist in list (not made yet)
            pitchintervals=list(allperms[random.randint(0,len(allperms)-1)]) #this is a list of length 5, will keep on picking a list randomly until it finds one with at least [-1,-1,-1] or [1,1,1]
        #once out of while loop, repetition requirements have been met
        locsofrep=[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([-1,-1,-1])] == [-1,-1,-1], range(len(pitchintervals) - len([-1,-1,-1]) + 1)))) if x == True]+[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([1,1,1])] == [1,1,1], range(len(pitchintervals) - len([1,1,1]) + 1)))) if x == True]
        locsofrep.sort() #locsorrep only contains starting indices of repeated intervals ([-1,-1,-1] or [1,1,1])
        print('locsofrep: ', end =" ")
        print(locsofrep)
        thirdornot=random.choice([0,1])
        pitchind=[0,1,2,3,4] #because pitchintervals is of length 5
        parttochop=pitchind.index(random.choice(locsofrep))
        del pitchind[parttochop:parttochop+3]
        print('pitchind: ', end =" ")
        print(pitchind)
        if thirdornot==1:
            pitchintervals[random.choice(pitchind)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
        print('pitch intervals')
        print(pitchintervals)
    elif numnotes==7: #then len(pitchintervals)=6 #7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777 NUMNOTES
        #find all permutations #not done
        pitchintervals=[] #initialize pitchintervals
        allperms=list(itertools.permutations([-1,1,-1,1,-1,1],6)) #options -1 and 1 with equal probability, 6 decisions to be made, indices will be 0,1,2,3,4,5
        while not any(y >=3 for y in [len(list(g[1])) for g in itertools.groupby(pitchintervals) if g[0]==-1 or g[0]==1]): #tests if a repetition of 3 or greater does not exist in list (not made yet)
            pitchintervals=list(allperms[random.randint(0,len(allperms)-1)]) #this is a list of length 6, will keep on picking a list randomly until it finds one with at least [-1,-1,-1] or [1,1,1]
        #once out of while loop, repetition requirements have been met
        locsofrep=[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([-1,-1,-1])] == [-1,-1,-1], range(len(pitchintervals) - len([-1,-1,-1]) + 1)))) if x == True]+[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([1,1,1])] == [1,1,1], range(len(pitchintervals) - len([1,1,1]) + 1)))) if x == True]
        locsofrep.sort() #locsorrep only contains starting indices of repeated intervals ([-1,-1,-1] or [1,1,1])
        print('locsofrep: ', end =" ")
        print(locsofrep)
        thirdornot=random.choice([0,1])
        pitchind=[0,1,2,3,4,5] #because pitchintervals is of length 6
        parttochop=pitchind.index(random.choice(locsofrep))
        del pitchind[parttochop:parttochop+3]
        print('pitchind: ', end =" ")
        print(pitchind)
        if thirdornot==1:
            pitchintervals[random.choice(pitchind)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
        print('pitch intervals')
        print(pitchintervals)
    elif numnotes==8: #then len(pitchintervals)=7 #8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888 NUMNOTES
        #find all permutations
        fiveOrThree=random.choice([5,3]) #pick between doing 5 in a row or 3&3
        if fiveOrThree==5:
            print('5 for numnotes 8')
            #find all permutations #not done
            pitchintervals=[] #initialize pitchintervals
            allperms=list(itertools.permutations([-1,1,-1,1,-1,1,-1,1],7)) #options -1 and 1 with equal probability, 7 decisions to be made, indices will be 0,1,2,3,4,5,6
            while not any(y >=4 for y in [len(list(g[1])) for g in itertools.groupby(pitchintervals) if g[0]==-1 or g[0]==1]): #tests if a repetition of 4 or greater does not exist in list (not made yet)
                pitchintervals=list(allperms[random.randint(0,len(allperms)-1)]) #this is a list of length 7, will keep on picking a list randomly until it finds one with at least [-1,-1,-1,-1] or [1,1,1,1]
            #once out of while loop, repetition requirements have been met
            locsofrep=[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([-1,-1,-1,-1])] == [-1,-1,-1,-1], range(len(pitchintervals) - len([-1,-1,-1,-1]) + 1)))) if x == True]+[i for i, x in enumerate(list(map(lambda x: pitchintervals[x:x + len([1,1,1,1])] == [1,1,1,1], range(len(pitchintervals) - len([1,1,1,1]) + 1)))) if x == True]
            locsofrep.sort() #locsorrep only contains starting indices of repeated intervals ([-1,-1,-1,-1] or [1,1,1,1])
            print('locsofrep: ', end =" ")
            print(locsofrep)
            thirdornot=random.choice([0,1])
            pitchind=[0,1,2,3,4,5,6] #because pitchintervals is of length 7
            parttochop=pitchind.index(random.choice(locsofrep))
            del pitchind[parttochop:parttochop+4]
            print('pitchind: ', end =" ")
            print(pitchind)
            if thirdornot==1:
                pitchintervals[random.choice(pitchind)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
            print('pitch intervals')
            print(pitchintervals)
        else:
            print('3&3 for numnotes 8')
            allperms=[(1,0,0,0,0,1,0),(0,1,0,0,0,1,0),(0,0,1,0,0,1,0),(0,0,0,1,0,1,0),(1,0,0,0,1,0,0),(1,0,0,1,0,0,0),(1,0,1,0,0,0,0),(0,0,1,0,1,0,0),(0,1,0,1,0,0,0)] #this is not the same format as the allperms variable in the other situations, in this allperms variable, 1 stands for start of 3 group (or 2 consecutive)
            prepitchintervals=list(random.choice(allperms)) #does not contain pitch intervals, only location of 3 group (or 2 consecutive)
            steplocations=[i for i, x in enumerate(prepitchintervals) if x == 1] #find all instances of 1 in list through list comprehension
            one=random.choice([-1,1]) #decide between [-1,-1] or [1,1] on 1st 3 group
            two=random.choice([-1,1]) #decide between [-1,-1] or [1,1] on 2nd 3 group
            prepitchintervals[steplocations[0]]=one #changing prepitchintervals based on those decisions
            prepitchintervals[steplocations[0]+1]=one
            prepitchintervals[steplocations[1]]=two
            prepitchintervals[steplocations[1]+1]=two
            pitchintervals=[x if x!=0 else random.choice([-1,1]) for x in prepitchintervals] #putting in the rest of the intervals (except for the skip of a 3rd)
            thirdornot=random.choice([0,1])
            thirdlocs=[0,1,2,3,4,5,6] #initialize and partially declare
            del thirdlocs[steplocations[1]+1] #delete right most steplocation first
            del thirdlocs[steplocations[1]]
            del thirdlocs[steplocations[0]+1]
            del thirdlocs[steplocations[0]] #delete left most steplocation last
            if thirdornot==1:
                pitchintervals[random.choice(thirdlocs)]=random.choice([-2,2]) #at random location, replace interval with down third or up third
            print('pitch intervals')
            print(pitchintervals)

    #####YAY the correct intervals have been found and placed in pitchintervals, now change these to note names#####

    pitches = None
    while pitches is None or len(pitches)<numnotes: #keep trying until there's no error (this means if there's an out of bounds error, pick a different starting point
        try:
            pitches=random.choice(fullscale) #get first note
            notelocation=fullscale.index(pitches) #find where in fullscale is the first note, needed in a bit, value will change in a bit
            pitches=[pitches]
            locationsums=notelocation #initialize and declare
            for y in range(numnotes-1): #first note has already been put in, hence the numnotes-1
                locationsums+=pitchintervals[y]
                pitches.append(fullscale[locationsums])
        except:
             pass

    print('#################################')
    print('Pitches: ', end =" ")
    print(pitches)
    print('#################################')
    #####ALL DONE YIPEE!#####

    print('')
    print('THE FOLLOWING TUNE WAS GENERATED:')
    print('Pitches:')
    print(pitches)
    print('Rhythm:')
    print(rhythm)
    print('')

    #48-83, in this part convert strings to midi numbers
    allnotesmidi=[48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
    midipitches=[]
    if sharporflat=='sharp':
        #allnotessharp
        for h in range(numnotes):
            midipitches.append(allnotesmidi[allnotessharp.index(pitches[h])])
    else:
        #allnotesflat
        for h in range(numnotes):
            midipitches.append(allnotesmidi[allnotesflat.index(pitches[h])])

    print('midipitches: ', end =" ")
    print(midipitches)

    print('')
    print('TUNE GENERATED SUCCESSFULLY')
    print('')
    print('##############')
    print('racotuge.py tune outputs:')
    print('')
    print('midipitches: ')
    print(midipitches)
    print('rhythm: ')
    print(rhythm)
    print('tempo: '+str(truetempo))
    print('scale number: '+str(scale))
    print('key: '+key)
    print('sharporflat: '+sharporflat)
    print('pitchintervals: ')
    print(pitchintervals)
    print('')
    return midipitches,rhythm,truetempo,key,scale,sharporflat,pitchintervals #key is a string, scale is a number (index from listscale)

#from racotuge import tune
#(midipitches,rhythm,truetempo,key,scale,sharporflat,pitchintervals)=tune() #to run the code elsewhere
