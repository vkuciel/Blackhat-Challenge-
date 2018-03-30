import random 
import string 

# Victor Kuciel-CPEG472-010
# Blackhat Challenge: VIGENERE DECODER

def charShift(c, n): # Determining shift
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))
    
def charFrequency(text): # For finding frequency
    frequency = {}
    for ascii in range(ord('a'), ord('a')+26):
        frequency[chr(ascii)] = float(text.count(chr(ascii)))/len(text)
    fSum = 0.0
    for ltr in frequency:
        fSum += frequency[ltr]*frequency[ltr]
    return fSum

listOfFrequencies = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}

#########################################################
    
def keyFinder(key, flag, text):
    num1 = .065
    num2 = .014
    num3 = .008
    count = 0.0
    numSum = 0.0
    for k in range(key):
        sCipher = text[k::key]
        frequency = {}
        for ascii in range(ord('a'), ord('a')+26):
            frequency[chr(ascii)] = float(sCipher.count(chr(ascii)))/len(sCipher)
        for viableKey in range(1, 26):
            squareSum = 0.0
            for ltr in listOfFrequencies:
                estimation = charShift(ltr, viableKey)
                squareSum += listOfFrequencies[ltr]*frequency[estimation]
            if abs(squareSum - num1) < num2:
                numSum = numSum + squareSum
                count = count + 1
                if flag:
                    print "P: ", k," Shift: ", viableKey, " Frequency: ", squareSum, " Key: ", key
    if count > 0:
        if abs((numSum/count) - num1) < num3:
            print "Average = ", numSum/count, "Key = ", key
        
def isKey(text):
    for key in range(1,50):
        keyFinder(key, False, text)
        
def analyzer(filename):
    readFile = file(filename,'r')
    text = readFile.read()
    engLtr = filter(lambda x: x.isalpha(), text)
    text = engLtr.lower() # Make lowercase
    readFile.close()
    return text
    
def decodeFinal(text, func, key):
    solution = ""
    for i in range(len(text)):
        position = i % func
        solution = solution + str(charShift(text[i],-1*(ord(key[position])-ord('a'))))
    return solution
    
##############################################  

# Steps : 

#isKey(analyzer('blackhat3.txt')) # Find the key
# 16 is the best solution, so this will be used for the nest step

#print keyFinder(16, True, analyzer('blackhat3.txt')) # Shift output

'''
Correct shift outputs:
24: y
19: t
20: u
6: g
7: h
7: h
8: i
23: x
21: v
25: z
8: i
13: n
12: m
10: k
4: e
16: q
'''

# Final step to decrypt the message
plaintextFinal = decodeFinal(analyzer('blackhat3.txt'), 16, "ytughhixvzinmkeq")
print plaintextFinal
