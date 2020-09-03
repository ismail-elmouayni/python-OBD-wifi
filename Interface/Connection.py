from    obd import OBD
from    obd import OBDStatus 
import  obd as lib

# Defining connnection constants. Note that those
# values are default values of OBD constructor  
LINK_ADDRESS    ="192.168.0.10"
LINK_PORT       = 35000

class Canal(object):
    """ description of class
        class responsable of establishing connection 
        with the carre and buiding quieries         """
        
    def __init__(self) : 
        self._canal = lib.OBD(LINK_ADDRESS,LINK_PORT)
        
    
    def isEstablished(self) : 
        return  self._canal.status() == OBDStatus.CAR_CONNECTED

    def status(self) : 
        return self._canal.status()

    def close(self) :
        self._canal.close()
        






