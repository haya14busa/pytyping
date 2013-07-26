#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
import os
import readline
from col import black,red,green,yellow,blue,purple,cyan,white

def userChoice(prompt, c):
	"""prompt - a string containing the prompt to display.
	   c - a tuple containing list of valid input choices."""
	userInput = raw_input(prompt)
	while (userInput not in c):
		print prompt
		userInput = raw_input(prompt)
	return userInput

def makelist():
	"""makes the list of words from words.txt file"""
	liopen = open("words.txt")
	theList = []
	for entry in liopen:
		entry = entry.strip()
		theList.append(entry)
	liopen.close()
	return theList

def randomword(theList):
	"""chooses a random word from the wordlist"""
	return random.choice(theList)

def rules():
	"""Rules of the game"""
	print cyan("Welcome\nTest your typing skills...\nType as many words as you can in under 60 seconds and get your RAW words per minute and actual words per minute\n")
	raw_input(red('Press Enter'))
	menu()

def play():
	"""Play function of the game."""
	usedtime = 0.0
	remtime = 0.0
	twords = 0
	cwords = 0
	inp = 'ttemp'
	alllen = 0
	i = 1
	listi = makelist()
	while True:
		try:
			x = int(raw_input("How many sentence will you type?\n>>"))
			break
		except ValueError:
			print red("Oops!  That was no valid number.  Try again...")
	raw_input('>>Press Enter to start the game')
	start = time.time()
	while (i <= x):
		word = randomword(listi)
		i += 1
		alllen += len(word)
		listi.remove(word)
		#remtime = 60.0 - usedtime
		#print remtime
		os.system('clear')
		print time.time() - start
		while (inp != word):
			print purple("-" * 90)
			print '>>' + cyan(word)
			print purple("-" * 90)
			inp = raw_input('>>')
			print "\n\n"
			if (inp == 'quit'):
				return 0
			
	end = time.time()
	usedtime = (end - start)
		#twords += 1
	os.system('clear')
	print red("\nIt's done!")
	print "-" * 90
	print "time:" + str(usedtime)
	mtime = usedtime/60
	wcount = alllen/5
	print yellow("WPM:" + str(wcount/mtime))
	print "Words Count:" + str(alllen)
	print "-" * 90
	'''
	print "Total no. of words:", twords
	incwords=twords - cwords
	print "No. of incorrect words", incwords
	raw=(twords/usedtime) * 60.0
	print "RAW words per minute %.2f" %raw
	actual=(cwords/usedtime) * 60.0
	print "Actual words per minute: %.2f"%actual
	scores=scorelist()
	addscore(scores,actual)
	writescore(scores)
	'''
	menu()

def menu():
	"""Menu for the game"""
	print cyan('Menu')
	prompt = "P)lay\n"
	prompt = prompt + "R)ules of the game\n"
	prompt = prompt + "D)isplay high scores\n"
	prompt = prompt + "Q)uit\n"
	prompt = prompt + "Please choose one:"
	choices = ("P", "p", "R", "r", "D", "d", "Q", "q")
	c = userChoice(prompt, choices)
	if c=='q' or c=='Q':
			print "You quit..."
			return 0
	elif c=='p' or c=='P':
		play()
	elif c=='d' or c=='D':
		os.system('clear')
		scorelist()
	elif c=='r' or c=='R':
		os.system('clear')
		rules()
	'''else:
		c = userChoice(prompt, choices)'''
	'''
	else:
		while c!='q' or c!='Q':
			if (c=='p') or (c=='P'):
				play()
				c='q'
			elif (c=='r') or (c=='R'):
				rules()
				c='q'
	'''

## --------------------------------------------------------##
## HIGHSCORE FUNCTIONS!

def scorelist():
	"""returns the list of scores"""
	scores=[]
	try:
		fout = open("highscore.csv", "r")	
		for entry in fout:
			entry=entry.strip()
			entrie=entry.split(",")
			record=(entrie[0], entrie[1])
			scores.append(record)
		fout.close()
		return scores
	except IOError as e:
		return scores
		
def bubbleSort(theList):
	"""Bubblesorts the list"""
	lastIndex = len(theList)-2
	while lastIndex >= 0:
		i = 0
		while i <= lastIndex:
			if theList[i][1] < theList[i+1][1]:
				theList[i], theList[i + 1] = theList[i + 1], theList[i]
			i +=1
		lastIndex -= 1

def eligible(theList,score):
	"""Returns True if the score is to be added to the list, otherwise False"""
	bubbleSort(theList)
	if len(theList) < 10:
		return True
	else:
		if score > theList[-1][1]: #the value of the last score in the list.
			return True
	return False # score is not eligible

def addscore(theList, score):
	"""adds the eligible score to theList"""
	if eligible(theList, score):
		print "Congrats! You made the top 10."
		name = raw_input("What is your name: ")
		entry=(name, score)
		theList.append(entry)
		bubbleSort(theList)
		print theList

		if len(theList)>10:
			#only keep top 10 values
			theList.pop()
		return theList
	else:
		print "BOOOOOOOO!"
		return theList

def writescore(theList):
	"""writes the scores present in theList to the file"""
	fout = open("highscore.csv", "w")
	bubbleSort(theList)
	for entry in theList:
		record= entry[0]+","+str(entry[1])+"\n"
		fout.write(record)
	fout.close()

def main():
	menu()

if __name__ == '__main__':
	main()
