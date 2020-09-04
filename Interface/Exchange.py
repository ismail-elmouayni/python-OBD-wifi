import obd 


class QrManager(object) :
    """ Class managing queries. Use get() to build 
        a quiery regarding a specific command 
        Use class constant identifiers to access
        commands identifiers such as SPEED, RPM etc."""
    
    def __init__(self, connection): 
        self._canal = connection

    SPEED       = "SPEED" 
    ELM_VERSION = "ELM_VERSION"
    ELM_VOLTAGE = "ELM_VOLTAGE"
    PIDS_A      = "PIDS_A"
    STATUS      = "STATUS"
    FREEZ_DTC   = "FREEZE_DTC"
    RPM         = "RPM"

    # Use get to provide a query regarding 
    # and OBD supported command. Use constant 
    # to identify command or provide command 
    # name as a string 
    def get(self,command) : 
        print(self._canal.query(obd.commands[command]))