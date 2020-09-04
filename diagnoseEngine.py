# Simple script doing car diagnose using python-OBD
import sys
import os


# Importing additional classes to the sys path
sys.path.insert(0,os.path.dirname(__file__) + "/Interface")

# Importing Interface classes 
from    Interface import Exchange
from    Interface import Connection


myCanal = Connection.Canal()


if(not myCanal.isEstablished()) : 
    print("failed to establish connection")
else : 
     # Here add several functionalities 
    print("canal is successfully established")
   
    # Communicate with CAR CALCULATOR  
    queryMg = Exchange.QrManager(myCanal)
 
    queryMg.get("RPM")
    queryMg.get("SPEED")
    queryMg.get("INTAKE_PRESSURE") 

    # Display diagnose codes 
    queryMg.get("GET_DTC")
 

    # Closing connection...
    myCanal.close()
    




















