#
# The very first sample synchronous WPS process.
#

from pywps.Process import WPSProcess                                

class Process(WPSProcess):

    def __init__(self): 

        WPSProcess.__init__(self,
                identifier = "test00",
                title="Simple WPS process test.",
                abstract="""Simple WPS synchrous process test.""",
                version = "1.0",
                storeSupported = False,
                statusSupported = False)

        # declare process inputs 
        self.textIn = self.addLiteralInput(identifier="input", title = "Input text." , type="String" )

        # declare process outputs 
        self.textOut = self.addLiteralOutput(identifier="output", title = "Ouput text." , type="String" )


    def execute( self ) : 

        self.textOut.setValue( self.textIn.getValue() ) 

        return 
