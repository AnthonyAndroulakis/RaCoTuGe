#Anthony Androulakis, 2019
#makes MATLAB-style matricies of frequencies and times of each tune

from audiolazy import midi2freq

def makeit(midipitches, rhythm, truetempo, tunenumber):
    frequencies=[]
    for i in range(len(midipitches)):
        frequencies.append(midi2freq(midipitches[i]))
    times=[]
    for j in range(len(rhythm)):
        times.append((60/truetempo)*4*rhythm[j])

    thestring="OHz=["
    for k in range(len(frequencies)):
        thestring=thestring+" "+str(frequencies[k])
    thestring=thestring+";"
    for l in range(len(times)):
        thestring=thestring+" "+str(times[l])
    thestring=thestring+"]"
    print(thestring)
    tunenumber+=1
    with open("tunes/matricies/tune"+str(tunenumber)+".txt", "w") as matrix_file:
        matrix_file.write(thestring)
