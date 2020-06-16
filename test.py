import ttactlogging
import time

ttactlogging.Logger.log(time.time(),"Log","Started Test Utility...\n")
ttactlogging.Logger.log(time.time(),"Warning","This is a test warning log...\n")
ttactlogging.Logger.log(time.time(),"Error","This is a test error log...\n")
ttactlogging.Logger.log(time.time(),"Separator","")
ttactlogging.Logger.log(time.time(),"Info","This is a test information log...\n")
ttactlogging.Logger.log(time.time(),"Validation","This is a test validation log...\n")
