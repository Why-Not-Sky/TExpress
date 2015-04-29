import os, sys
import site

PYTHON_LIB = '/Library/Frameworks/Python.framework/Versions/2.7/'
sys.path.append(PYTHON_LIB)
#PYTHON_LIB = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages'
sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')

#virtualenv tExpress
PROJECT_DIR = '/Users/sky_wu/Sites/tExpress'
#activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
#execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

os.chdir("/Users/sky_wu/Sites/tExpress")

from server import app as application
