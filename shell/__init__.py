import sys
from .process import Process

def inputToProcesses(input): #takes user input, converts it into processes
	isEnd = False
	procList = []
	currProcess = Process()

	startCopy = 0
	index = 0
	oneQuote = False
	doubleQuote = False

	for character in input: #if the program finds the initial single quote, it makes note of it
		
		if character == '\'' and not oneQuote:
			oneQuote = True
			startCopy += 1

		elif character == '\"' and not doubleQuote: #if the program finds the initial double quote, it makes note of it
			doubleQuote = True
			startCopy += 1

		elif character == '\'' and oneQuote: #if the program finds the final single quote, it adds the commands, then the arguments to be printed out later
			if currProcess.command == '':
				temp = input[startCopy:index]
				if temp != '':
					currProcess.command = temp
				startCopy = index + 1
			else:
				temp = input[startCopy:index]
				if temp != '':
					currProcess.arguments.append(temp)
				startCopy = index + 1
			oneQuote = False #now that the quotes have ended, the boolean resets

		elif character == '\"' and doubleQuote: #if the program finds the final double quote, it adds the commands, then the arguments to be printed out later
			if currProcess.command == '':
				temp = input[startCopy:index]
				if temp != '':
					currProcess.command = temp
				startCopy = index + 1
			else:
				temp = input[startCopy:index]
				if temp != '':
					currProcess.arguments.append(temp)
				startCopy = index + 1
			doubleQuote = False #now that the quotes have ended, the boolean resets
		
		elif index == len(input)-1 and oneQuote or index == len(input)-1 and doubleQuote: #if the program spots mismatched quotes, it will raise an exception
			raise Exception("Mismatched quotes")

		if not oneQuote and not doubleQuote: #if there are no quotes around the words, removes spaces, adds the commands and then the arguments to be outputted
			if character == ' ':
				if currProcess.command == '':
					temp = input[startCopy:index].strip() #removes any spaces using the .strip() method
					if temp != '':
						currProcess.command = temp
					startCopy = index + 1
				
				else:
					temp = input[startCopy:index].strip()
					if temp != '':
						currProcess.arguments.append(temp)
					startCopy = index + 1
			
			if character == '|' or character == '<' or character == '>': #these characters mark the end of processes, so the program notes it using the isEnd boolean
				isEnd = True
			
			if isEnd or character == '\n': #when the program finds the end of a process, it removes spaces, then adds the commands and then arguments
				if currProcess.command == '':
					temp = input[startCopy:index].strip()
					if temp != '':
						currProcess.command = temp
					startCopy = index + 1

				else:
					temp = input[startCopy:index].strip()
					if temp != '':
						currProcess.arguments.append(temp)
				
				startCopy = index + 1

				procList.append(currProcess) #the commands and arguments from the previous if statements are added to the end of a list, which is returned and will be outputted
				currProcess = Process()
				isEnd = False #boolean is reset for the next time this function is called
		
		index += 1

	return procList
		