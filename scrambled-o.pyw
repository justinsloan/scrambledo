#!/usr/bin/env python3
'''
This is a simple word scramble game made for my second-grade daughter
to help her study for her spelling tests.  It uses a modified version
of John Zelle's graphics.py package to allow for Text Box lebel
objects to have a font size up to 64.  If you do not use the modified
version of graphics.py you will receive an "Invallid option value"
error.

The list of words to study should be put into a plain text file named
word_list.txt with one word per line and placed in the same directory 
as scrambled-o.py.

Version 1.1
13 December 2017
'''

import random, os
from graphics import *
from button import *

verboseMode = False
debugMode = False
allowCapitalLetter = True

def printVerbose(line):
	if verboseMode == True:
		print(line)


def printDebug(line):
	if debugMode == True:
		print(line)



class ScrambledO:
	#This class implements a Scrambled-O GUI Game

	def __init__(self):
		#Create the GUI interface for the game
		win = GraphWin("Scrambled-O!! (v1.1)",900,450)  #Instantiates a Window object
		win.setCoords(0,0,10,5)
		self.win = win #Makes the object part of the class

		lblWord = Text(Point(5,4),"Scrambled-O!!")  #Instantiates a Text object
		lblWord.setSize(64)
		lblWord.draw(win)
		self.lblWord = lblWord

		lblMessage = Text(Point(5,3),"")  #Instantiates a Text object
		lblMessage.setSize(24)
		lblMessage.draw(win)
		self.lblMessage = lblMessage

		txtUserAnswer = Entry(Point(5,2),15)  #Instantiates a Entry object
		txtUserAnswer.setSize(36)
		txtUserAnswer.setFill("white")
		txtUserAnswer.draw(win)
		self.txtUserAnswer = txtUserAnswer

		#Create the Buttons
		btnStart = Button(self.win, Point(4,1), 1.5, .50, "Start")
		printDebug("btnStart instantiated")
		self.btnStart = btnStart
		self.btnStart.activate()
		printDebug("btnStart activated")

		btnQuit = Button(self.win, Point(6,1), 1.5, .50, "Quit")
		printDebug("btnQuit instantiated")
		self.btnQuit = btnQuit
		self.btnQuit.activate()
		printDebug("btnQuit activated")


	def __readWordList(self, WordFile):
		WordList = []

		fileDirectory = os.path.dirname(os.path.realpath(__file__))
		printDebug("OS Real Path: " + fileDirectory)
		
		WordFile = fileDirectory + "/" + WordFile
		printDebug("WordFile Path: " + WordFile)

		printVerbose("Reading word list from " + str(WordFile))

		with open(WordFile) as f:
			for line in f.readlines():
				if allowCapitalLetter == True:
					NewWord = line.strip()
				else:
					NewWord = line.strip().lower()
				printVerbose("Added " + NewWord)
				WordList.append(NewWord)
				NewWord = ""
		random.shuffle(WordList)
		printDebug("WordList Array: " + str(WordList))
		return WordList


	def __scrambleWord(self, TheWord):
		UserAnswer = ""
		ScrambledWord = "".join(random.sample(TheWord,len(TheWord)))

		while True:
			self.lblWord.setText(ScrambledWord)
			self.lblWord.setTextColor("black")
			printDebug("TheWord is: " + TheWord)

			theKey = ""

			while theKey != "Return":
				theKey = self.win.getKey()
				printDebug(theKey)
			
			UserAnswer = self.txtUserAnswer.getText().lower()

			if UserAnswer == TheWord.lower():
				self.lblWord.setText("GREAT JOB!")
				self.lblWord.setTextColor("green")
				self.lblMessage.setText("Press ENTER to continue.")
				self.win.getKey()
				self.lblMessage.setText("")
				self.lblWord.setText("")
				self.txtUserAnswer.setText("")
				return True
			else:
				self.lblWord.setText("Sorry, try again!")
				self.lblWord.setTextColor("red")
				self.lblMessage.setText("Press ENTER to continue.")
				self.win.getKey()
				self.lblMessage.setText("")


	def __getUserInput(self):
		#Waits for button to be clicked then either starts a game
		# or quits. The 'while True:' statement creats an
		# infinite loop
		while True:
			self.lblMessage.setText("Click Start to play.")
			printDebug("Waiting for user input")
			pt = self.win.getMouse()
			if self.btnQuit.clicked(pt):
				printDebug("btnQuit.clicked if statement")
				#Do nothing and continue to the close() procedure
				self.__endGame()
			elif self.btnStart.clicked(pt):
				printDebug("btnStart.clicked if statement")
				self.lblMessage.setText("")
				self.__startGame()

	def __startGame(self):
		printDebug("__startGame procedure")
		self.btnStart.deactivate()
		self.btnQuit.deactivate()

		WordList = self.__readWordList('word_list.txt')
		for EachWord in WordList:
			self.__scrambleWord(EachWord)

		self.lblWord.setText("All done, GREAT JOB!")

		self.btnStart.activate()
		self.btnQuit.activate()

	def __endGame(self):
		printDebug("__endGame procedure")
		self.lblMessage.setText("Bye!")
		self.win.close()    # Close window when done


	def run(self):
		#Infinite 'event loop' to process user input
		while True:
			key = self.__getUserInput()

		self.lblMessage.setText("Bye!")
		self.win.close()    # Close window when done


	


def main():
	theGame = ScrambledO()
	theGame.run()
	sys.exit(0)


if __name__ == '__main__':
	main()
