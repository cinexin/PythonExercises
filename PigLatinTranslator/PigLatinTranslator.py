""" Pig Latin Game proposed as part of CodeAcademy Tutorial
"""
import sys

print "WELCOME TO THE PIG Latin TRANSLATOR!!"
original = raw_input ("Enter a word: ")

if (len(original) == 0) or not original.isalpha():
     print "Input string is empty or contains numeric chars"
     sys.exit(-1)

pig = "ay"
word = original.lower()
firstLetter = word[0]
translatedWord = word + firstLetter + pig
translatedWord = translatedWord[1:len(translatedWord)]
print "Translated word: " + translatedWord