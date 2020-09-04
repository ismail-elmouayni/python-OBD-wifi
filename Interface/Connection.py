# -*- coding: utf-8 -*-
from    obd import OBD
from    obd import OBDStatus 
import  obd as lib

# Defining connnection constants. Note that those
# values are default values of OBD constructor  
LINK_ADDRESS    ="192.168.0.10"
LINK_PORT       = 35000


class Canal(OBD):
    """ description of class
        class representing a connection canal 
        with elm327 using OBD-II protocol """
        
    def __init__(self) : 
        super(Canal,self).__init__(LINK_ADDRESS,LINK_PORT)   
        self.print_commands()
    
    def isEstablished(self) : 
        return not self.status() == OBDStatus.NOT_CONNECTED


   










