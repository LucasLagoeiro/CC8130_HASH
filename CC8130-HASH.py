import hashlib
from hashDiff import Difference

file = open("text.txt", "r")
content=file.readlines()

show = Difference()

for i in range (len(content)):
    print("-----------------------------------------TEXT " + str(i) + "-----------------------------------------\n" )

    # Manipulating the string lines
    textLineSplit = content[i].split('" -')
    textLineConcatenate = textLineSplit[0]   
    myText = textLineConcatenate.replace('"', '')
    splitSHA256_MD5 = textLineSplit[1].split(' - ')
    fixMD5 = splitSHA256_MD5[1].replace('\n','')
    testSHA256 = splitSHA256_MD5[0]
    
    correctSHA256 = testSHA256[1:] 
    testMD5 = fixMD5

    SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()
 

    if (SHA256 == correctSHA256):
        SHA256_RESPONSE = True
    else:
        SHA256_RESPONSE = False

    if (MD5 == testMD5):
        MD5_RESPONSE = True
    else:
        MD5_RESPONSE = False


    print("O hash SHA256 está " + str(SHA256_RESPONSE))
    print("O hash MD5 está " + str(MD5_RESPONSE) + "\n")

    if (SHA256_RESPONSE == False):
        print("----------------------------SHA256---------------------------")
        RESPONSE_DIFF = show.difference(correctSHA256,SHA256)
        print("Os termos diferentes são: " + str(RESPONSE_DIFF[0]) + " e deveriam ser: " + str(RESPONSE_DIFF[1])+ "\n\n\n")
    if(MD5_RESPONSE == False):
        print("----------------------------MD5---------------------------")
        RESPONSE_DIFF = show.difference(testMD5,MD5)
        print("Os termos diferentes são: " + str(RESPONSE_DIFF[0]) + " e deveriam ser: " + str(RESPONSE_DIFF[1]) + "\n\n\n")
    if(MD5_RESPONSE == True and SHA256_RESPONSE == True):
        print("Ambos hashs estão corretos :)")




