from datetime import datetime


class ThermalException(Exception):
    def __init__(self, message, filename="", trackid=""):
        Exception.__init__(self, message)
        self.trackid = trackid
        self.message = message
        self.date = datetime.utcnow()
        self.filename = filename

