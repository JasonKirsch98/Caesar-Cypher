#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:28:21 2017

@author: jasonkirschsmacbookpro
"""

#Project 5
#Caesar Cypher
#Input cyphered text
#Output decyphered text

def get_most_common_char(s): #Obtains E as most common letter
    mostCommon = 'E'
    mostCommonNum = 0
    for i in range(0,len(s)):
        count = 0
        if(s[i] != ' ' and s[i] != '.'): #ignores space, periid, etc
            for x in range(0,len(s)):
                if s[i] == s[x]:
                    count+=1
            if count > mostCommonNum:
                mostCommonNum = count
                mostCommon = s[i]
    return mostCommon
    pass

def parse_ignore(ignore): #Allows multiple prompts/attempts
    mostCommon = 'E'
    chars = "ZQXJKVBPYGFWMUCLDRHSNIOATE"
    for i in range(0,len(chars)):
        isIgnored = False
        for x in range(0,len(ignore)):
            if chars[i] == ignore[x]:
                isIgnored = True
        if not isIgnored:
            mostCommon = chars[i]
    return mostCommon
    pass

def get_char(ch,shift): #Returns shifted decoding
    if(ord(ch) >= 65 and ord(ch) <= 90): #Loop to stay in range
        val = (ord(ch) + shift) 
        if val < 65:
            val += 26
        elif val > 90:
            val -= 26
        return chr(val)
    else:
        return ch
    pass

def get_shift(s,ignore): # Used to find next most common characters
    ch = get_most_common_char(s)
    i = parse_ignore(ignore)
    return (ord(i) - ord(ch))
    pass

def output_plaintext(s,shift): # Outputs code with shift, upper case
    returnStr = ""
    for i in range(0,len(s)):
        returnStr = returnStr + get_char(s[i],shift)
    return returnStr
    pass
    
def main(): # allows more easy access to test programs, comment out main
    notLegible = True #Continues to prompt user until legible English is returned
    ignr = " "
    string = input("Input cyphertext: ")
    string = string.upper()
    while(notLegible):
        result = output_plaintext(string,get_shift(string,ignr))
        print(result)
        answer = input("Is this readable? (yes,no):")
        if(answer == "yes"):
            notLegible = False
        else:
            ignr += parse_ignore(ignr)
    pass
main()



#7
#4
#5
#5
#7