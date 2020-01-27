from src.exceptions.thermalexception import ThermalException


class ThermalOperationException(ThermalException):
    def __init__(self, message, operation,filename="", trackid=""):
        ThermalException.__init__(self, message, filename, trackid)
        self.operation = operation

