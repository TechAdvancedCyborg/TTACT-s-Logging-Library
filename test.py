from ttactlogging import Logger
import time

Logger.log(time.time(),"Log","Started Test Utility...\n")
Logger.log(time.time(),"Warning","This is a test warning log...\n")
Logger.log(time.time(),"Error","This is a test error log...\n")
Logger.log(time.time(),"Separator","")
Logger.log(time.time(),"Info","This is a test information log...\n")
Logger.log(time.time(),"Validation","This is a test validation log...\n")
