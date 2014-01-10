
import types, random
from pywps.Process import WPSProcess                                

class Process(WPSProcess):

    def __init__(self): 

        WPSProcess.__init__(self,
                identifier="random_gen",
                title="Simple WPS process random generator.",
                abstract="""Simple WPS synchrous process test.""",
                version="1.0",
                storeSupported=False,
                statusSupported=False)

        # declare process inputs 
        self.textIn = self.addLiteralInput(identifier="input", title="Input text." , type=types.IntType )

        # declare process outputs 
        self.textOut = self.addLiteralOutput(identifier="output", title="" , type=types.StringType )


    def execute( self ) : 

        output = []
        random.seed()
        for i in range(self.textIn.getValue()):
            output.append(random.random())

        self.textOut.setValue(','.join(map(str, output))) 

        return 
