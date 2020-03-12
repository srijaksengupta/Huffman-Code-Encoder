# (Programming environment - Mac OSX, Editor - Atom, Language - Python version 3.7)

#Importing the System-specific parameter and function library
import sys
#Importing the Text wrapping and filling
import textwrap

#Reading the contents of the file as a command
input_file = sys.argv[1]
with open(input_file) as file:
    cnt = file.read()

#Frequency of characters stored
frq = {}
for c1 in cnt:
    if not c1 in frq:
        frq[c1] = 0
    frq[c1] = frq[c1] + 1

#Function for sorting the tuple
def sorting(fr):
    return sorted( fr.items(), key = lambda x: (x[1], x[0]) )

#Storing sorted frequency of characters in main tuple
tupmain = sorting(frq)

#Initialising the codes
cd = {}
for c2 in tupmain:
    x = c2[0]
    cd[x] = ''

while ( len(tupmain) > 1):
    #Sorting the main again
    tupmain = sorted( tupmain, key = lambda x: (x[1], x[0]) )

    #Checking for which tree has lower ASCII values
    subtree = [tupmain.pop(0), tupmain.pop(0)]
    subtreesort = sorted(subtree)

    #Getting the first 2 nodes
    ltree = subtreesort.pop(0)
    rtree = subtreesort.pop(0)

    #Building the tree by giving 1 for nodes in right subtrees and 0 for nodes in left subtrees
    for c3 in ltree[0]:
        s1 = '0'
        cd[c3] = s1 + cd[c3]
    for c4 in rtree[0]:
        s2 = '1'
        cd[c4] = s2 + cd[c4]

    node = (ltree[0] + rtree[0], ltree[1] + rtree[1])
    tupmain.append(node)

#This variable represents the encoded message
encodedtxt = ''
for c5 in cnt:
    encodedtxt = encodedtxt + cd[c5]

#Here, we are sorting the codes
cd = sorted( cd.items(), key = lambda x: x[0] )

#Using the textwrap library to make sure that output file “encodemsg.txt” stores the encoded message with 80 0/1 characters on each row
rowtextwrap = textwrap.TextWrapper(width=80)
lineswrap = rowtextwrap.wrap(text=encodedtxt)
#The text wrapping process
with open("encodemsg.txt", "w") as f:
    for i in range(len(lineswrap)):
        if ( i == (len(lineswrap) - 1)):
            print(lineswrap[i], end='', file=f)
        else:
            print(lineswrap[i], file=f)

frqsum = 0
frqsumlen = 0
with open("code.txt", "w") as f:
    for i in range(len(cd)):
        if cd[i][0] == ' ':
            print("Space: " + cd[i][1], file=f)
            #We update frqsum here
            frqsum = frqsum + frq.get(cd[i][0])
            prod = len(cd[i][1]) * (frq.get(cd[i][0]))
            #We update frqsumlen here
            frqsumlen = frqsumlen + prod
        else:
            print(cd[i][0] + ": " + cd[i][1], file=f)
            #We update frqsum here
            frqsum = frqsum + (frq.get(cd[i][0]))
            prod = len(cd[i][1]) * (frq.get(cd[i][0]))
            #We update frqsumlen here
            frqsumlen = frqsumlen + prod
    avg = round( (frqsumlen/frqsum), 2)
    print("Ave = " + str(avg) + " bits per symbol", end='', file=f)
