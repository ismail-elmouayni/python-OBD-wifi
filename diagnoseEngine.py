# Simple script doing car diagnose using python-OBD
import sys
import os
 

# Importing additional classes to the sys path
sys.path.insert(0,os.path.dirname(__file__) + "/Interface")

import Input
import Connection

myCanal = Connection.Canal()

if(not myCanal.isEstablished()) : 
    print("failed to establish connection")
else : 
    print("canal is successfully established")
    # Here add several functionalites 

    reader = Input.Reader(myCanal)
    reader.display(Input.Reader.RPM)






















