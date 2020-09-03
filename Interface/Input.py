import obd 

class Reader(object) :
    
    def __init__(self, conncetion): 
        self._canal = connection

    SPEED       = "SPEED" 
    ELM_VERSION = "ELM_VERSION"
    ELM_VOLTAGE = "ELM_VOLTAGE"
    PIDS_A      = "PIDS_A"
    STATUS      = "STATUS"
    FREEZ_DTC   = "FREEZE_DTC"
    RPM         = "RPM"

    def display(self,command) : 
        self._canal.query(obd.commands[command])