import time
from time import gmtime, strftime

localTime = strftime("%A, %Y.%m.%d, %H:%M:%S %z", gmtime(time.time()))

print(localTime)