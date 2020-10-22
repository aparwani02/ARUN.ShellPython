# ARUN.ShellPython
Arun Parwani
Language Used: Python
https://github.com/aparwani02/ARUN.ShellPython.git


This program takes a number of Command Line Inputs, and returns an output/exits based on the user's input. 

If the User inputs Ctrl-D, the program exits immediately.
If the user inputs Ctrl-C, the program outputs "Shell Exiting..." then exits.

The user can also input a command, and a number of arguments for a process. Processes are separated by either |, <, or >. Words can be separated by |, <, >, or a space. The first word in the process is its command, all subsequent words are arguments for the process. Quotes can also be used to enclose one "word." However, mismatched quotes (e.g. " hello ') will result in the following error: Error: Mismatched quotes."

Each of these inputs will result in an output like the following:

Process <NUMBER>
Command: <Command From Input>
Arguments:
0: <Argument0>
1: <Argument1>
2: ...

The program will take a string argument, such as that in the input, and return an array of Processes


---------------------

I originally did this program in C++. However, I started having issues with my compiler, and was wasting a lot of time trying to debug that so I could run my program. Therefore, I switched to Python.