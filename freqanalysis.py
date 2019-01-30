import string

#to read input from a file
f=open("sample", "r")
if f.mode == 'r':
    contents = f.read()
print(contents.upper())
plaintext = contents.upper()

lengthplain = len(plaintext)
print(lengthplain)

#dictionary with letter frequencies
letterfreq1= {
"E": 12.7/100,
"T":9.1/100,
"A":8.2/100,
"O":7.5/100,
"I":7.0/100,
"N":6.7/100,
"S":6.3/100,
"H":6.1/100,
"R":6.0/100,
"L":4.0/100,
"D":4.3/100,
"C":2.8/100,
"U":2.8/100,
"M":2.4/100,
"W":2.4/100,
"F":2.2/100,
"G":2.0/100,
"Y":2.0/100,
"P":1.9/100,
"B":1.5/100,
"V":1.0/100,
"K":0.8/100,
"J":0.2/100,
"X":0.2/100,
"Q":0.1/100,
"Z":0.1/100
}

letterfreq1alphabet = list(letterfreq1.keys())


#all letters of alphabet
alphabet = list(string.ascii_uppercase)

#function to generate ciphertext
def encrypt(text,s):
    result=""
    #s represents shift order, s=3 for Caesar cipher
    for x in plaintext:
        if x in alphabet:
            result += chr((ord(x) + s-65) % 26 + 65)
        else:
            result += x
    return result

ciphertext = encrypt(plaintext, 3)
print(ciphertext)

def newfreqdist(ciphertext):
    letterfreq2 = {}
    a1=b1=c1=d1=e1=f1=g1=h1=i1=j1=k1=l1=m1=n1=o1=p1=q1=r1=s1=t1=u1=v1=w1=x1=y1=z1=otherchars=0
    for x in ciphertext:
        if x in alphabet:
            if x == alphabet[0]: a1+=1
            if x == alphabet[1]: b1+=1
            if x == alphabet[2]: c1+=1
            if x == alphabet[3]: d1+=1
            if x == alphabet[4]: e1+=1
            if x == alphabet[5]: f1+=1
            if x == alphabet[6]: g1+=1
            if x == alphabet[7]: h1+=1
            if x == alphabet[8]: i1+=1
            if x == alphabet[9]: j1+=1
            if x == alphabet[10]: k1+=1
            if x == alphabet[11]: l1+=1
            if x == alphabet[12]: m1+=1
            if x == alphabet[13]: n1+=1
            if x == alphabet[14]: o1+=1
            if x == alphabet[15]: p1+=1
            if x == alphabet[16]: q1+=1
            if x == alphabet[17]: r1+=1
            if x == alphabet[18]: s1+=1
            if x == alphabet[19]: t1+=1
            if x == alphabet[20]: u1+=1
            if x == alphabet[21]: v1+=1
            if x == alphabet[22]: w1+=1
            if x == alphabet[23]: x1+=1
            if x == alphabet[24]: y1+=1
            if x == alphabet[25]: z1+=1
        else:
            otherchars+=1
    length1 = lengthplain - otherchars
    letterfreq2["A"] = a1/length1
    letterfreq2["B"] = b1/length1
    letterfreq2["C"] = c1/length1
    letterfreq2["D"] = d1/length1
    letterfreq2["E"] = e1/length1
    letterfreq2["F"] = f1/length1
    letterfreq2["G"] = g1/length1
    letterfreq2["H"] = h1/length1
    letterfreq2["I"] = i1/length1
    letterfreq2["J"] = j1/length1
    letterfreq2["K"] = k1/length1
    letterfreq2["L"] = l1/length1
    letterfreq2["M"] = m1/length1
    letterfreq2["N"] = n1/length1
    letterfreq2["O"] = o1/length1
    letterfreq2["P"] = p1/length1
    letterfreq2["Q"] = q1/length1
    letterfreq2["R"] = r1/length1
    letterfreq2["S"] = s1/length1
    letterfreq2["T"] = t1/length1
    letterfreq2["U"] = u1/length1
    letterfreq2["V"] = v1/length1
    letterfreq2["W"] = w1/length1
    letterfreq2["X"] = x1/length1
    letterfreq2["Y"] = y1/length1
    letterfreq2["Z"] = z1/length1

    return letterfreq2

letterfreq2 = newfreqdist(ciphertext)

print("Given Frequency Analysis")
print(letterfreq1)
print()
print("Generated Frequency Analysis in CipherText")
print(letterfreq2)
print()
print(letterfreq1alphabet)

#letterfreq2list = list(letterfreq2.values())
#letterfreq2list = sorted(letterfreq2list, reverse=True)
#print(letterfreq2list)

###

listletters1=list(letterfreq1.keys()) #list containing the alphabet letters in plaintext

listcipher=list(letterfreq2.keys()) #list containing the alphabet letters in ciphertext

#print(listfreq1,type(listfreq1))
listfreq2=list(letterfreq2.values()) #list containing cipher letter frequencies

print(letterfreq2)

print()
print(listfreq2)

sorted_list=sorted(listfreq2,reverse=True)

print()

print(sorted_list)

guessed = {}

for i in sorted_list:
    count=0
    for j in letterfreq2:
        if(i == letterfreq2[j]):
            guessed[listcipher[count]]=listletters1[sorted_list.index(i)]
        count=count+1

# test1=sorted(guessed.keys())
# test2=sorted(guessed.values())
# print(test1)
# print()
# print(test2)

print()
print("The possible substitutions are:\n",guessed)

#print(len(guessed))

guessed_list_values = list(guessed.values())
#print(sorted(guessed_list_values))
guessed_list_keys = list(guessed.keys())
#print(sorted(guessed_list_keys))

#finalsubstitution = {}

#length_dict = len(guessed_list_values)
#print(length_dict)
#ii = jj = 0
#while (length_dict != 0):
#    finalsubstitution[guessed_list_values[ii]] = guessed_list_keys[jj]
#    length_dict = length_dict-1
#    ii+=1
#    jj+=1

print()

#print(finalsubstitution)
finalguessplaintext = ""
for x in ciphertext:
    if x in alphabet:
        finalguessplaintext += guessed[x]
    else:
        finalguessplaintext += x

print()
print("Original Plaintext :")
print(plaintext)
print("The guessed plaintext from new frequency analysis is :\n")
print(finalguessplaintext)
