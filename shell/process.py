class Process:
    def __init__(self, command = '', argumentsList = None): 
        self.command = command
        if argumentsList is None:
            argumentsList = []
        self.arguments = argumentsList

    def __str__(self):
        rtn = "Command: {} \n".format(self.command)
        rtn += "Arguments: \n"
        for arg in enumerate(self.arguments):
            rtn += (str(arg[0]) + ": " + str(arg[1]))
        return rtn