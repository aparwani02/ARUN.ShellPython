import sys
import signal
from . import *

def signal_handler(sig, frame): #if ctrl-C is pressed, the program displays this message and exits
	print("\nShell Exiting...")
	sys.exit(0)


if __name__ == '__main__':
	end = False
	while not end:
		signal.signal(signal.SIGINT, signal_handler)
		print('> ')
		input = sys.stdin.readline()

		if len(input) == 0:
			break

		if input:
			try: #formats the process (process number, command, argument), and outputs it
				procList = inputToProcesses(input)
				for process in enumerate(procList):
					print('--------------------')
					print('Process: ' + str(process[0]))
					print('--------------------')
					print(process[1])
			except Exception as exception: #outputs error if there's a mismatched quote
				print('Error: ', exception)
			
		else:
			sys.exit(0)
			
