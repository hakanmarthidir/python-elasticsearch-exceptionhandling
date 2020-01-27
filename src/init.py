import os

from src.elasticmanager.elasticlogger import ElasticLogger
from src.exceptions.thermalexception import ThermalException
from src.exceptions.thermaloperationexception import ThermalOperationException


logger = ElasticLogger()

try:
    print("Operation 1")
    print("Operation 2")
    #a = 0
    #b = 3
    #c = b / a
    raise ThermalOperationException(message="Error Message", operation="XX")

except ThermalException as a:
    print(a.operation)
    print(a.__class__.__name__)
    print(os.path.basename(__file__))
    logger.write(a)

except Exception as e:
    logger.write(ThermalException(str(e), "BlaBla", os.path.basename(__file__), "Track-111" ))