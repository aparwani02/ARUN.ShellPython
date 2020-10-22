import unittest
import shell

class ArgumentTests(unittest.TestCase):
    def testNoQuotesProcess(self): #tests user input, sees if it recognizes the amount of processes present with no quotes
        procList = shell.inputToProcesses('ls | ps aux | du -d 1 -h\n')
        self.assertEqual(len(procList), 3)

    def testNoQuotesCommands(self): #tests user input, sees if it lists the commands present with no quotes
        commands = []
        for process in shell.inputToProcesses('ls | ps aux | du -d 1 -h\n'): 
            commands.append(process.command)
        self.assertEqual(commands, ['ls', 'ps', 'du'])

    def testNoQuotesArguments(self): #tests user input, sees if it lists the arguments present with no quotes
        arguments = []
        for process in shell.inputToProcesses('ls | ps aux | du -d 1 -h\n'): 
            arguments.append(process.arguments)
        self.assertEqual(arguments, [[], ['aux'], ['-d', '1', '-h']])

   
   
    def testSingleQuotesProcess(self): #tests user input, sees if it recognizes the amount of processes present with single quotes
        procList = shell.inputToProcesses('ls \'Welcome to | the jungle\' | ps aux\n')
        self.assertEqual(len(procList), 2)

    def testSingleQuotesCommands(self): #tests user input, sees if it lists the commands present with single quotes
        commands = []
        for process in shell.inputToProcesses('ls \'Welcome to | the jungle\' | ps aux\n'):
            commands.append(process.command)
        self.assertEqual(commands, ['ls', 'ps'])

    def testSingleQuotesArguments(self): #tests user input, sees if it lists the arguments present with single quotes
        arguments = []
        for process in shell.inputToProcesses('ls \'Welcome to | the jungle\' | ps aux\n'):
            arguments.append(process.arguments)
        self.assertEqual(arguments, [['Welcome to | the jungle'], ['aux']])



    def testDoubleQuotesProcess(self): #tests user input, sees if it recognizes the amount of processes present with double quotes
        procList = shell.inputToProcesses('ls "Welcome to | the jungle" | ps aux\n')
        self.assertEqual(len(procList), 2)

    def testDoubleQuotesCommands(self): #tests user input, sees if it lists the commands present with double quotes
        commands = []
        for process in shell.inputToProcesses('ls "Welcome to | the jungle" | ps aux\n'): 
            commands.append(process.command)
        self.assertEqual(commands, ['ls', 'ps'])

    def testDoubleQuotesArguments(self): #tests user input, sees if it lists the arguments present with double quotes
        arguments = []
        for process in shell.inputToProcesses('ls "Welcome to | the jungle" | ps aux\n'):
            arguments.append(process.arguments)
        self.assertEqual(arguments, [["Welcome to | the jungle"], ['aux']])

    
    
    def testMismatchedQuotes(self): #tests user input, sees if it recognizes the mismatched quotes, and throws the appropriate exception
        self.assertRaises(Exception, shell.inputToProcesses, 'ls \"Welcome to | the jungle | ps aux\n') 
       