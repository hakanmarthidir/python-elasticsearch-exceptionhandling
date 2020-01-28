from src.exceptions.thermalexception import ThermalException


class ThermalValidationException(ThermalException):
    def __init__(self, message, parametername, filename="", trackid=""):
        ThermalException.__init__(self, message, filename, trackid)
        self.parametername = parametername
