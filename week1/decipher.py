#!/bin/python
out = ""
phrases = ["Cyberspace.",
"A consensual hallucination",
"experienced daily by billions of legitimate operators,",
"in every nation, by children being taught mathematical concepts... ",
"A graphic representation of data",
"abstracted from banks of every computer in the human system.",
"Unthinkable complexity.",
"Lines of light ranged in the nonspace of the mind,",
"clusters and constellations of data.",
"Like city lights, receding...",
"-",
"William Gibson, Neuromancer 2z"]

indexes = ["2:2:4","10:1:2","8:1:1","10:1:3","3:7:4","7:2:2",
"5:1:1","9:5:1","3:4:1","12:4:2","1:1:1","4:9:4","6:5:3",
"6:3:1","12:4:1","4:7:3","10:4:9","2:2:2","4:3:1","8:10:2",
"8:2:1","9:3:3"]

for i in indexes:
    ind = i.split(":")
    try: 
        line = phrases[int(ind[0])-1]
        word = line.split(" ")[int(ind[1])-1]
        letter = word[int(ind[2])-1]
    except IndexError as e:
        print ind
        letter = "!"
    out += letter

print out

