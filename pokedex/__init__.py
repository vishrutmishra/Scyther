from ConfigParser import SafeConfigParser
import os
#Update Current Path environment variable
os.environ["CURRENTPATH"] = os.path.dirname(__file__)

currentpath = os.environ["CURRENTPATH"]
envpath = 'vars.env'
env = os.path.abspath(os.path.join(currentpath, envpath))
parser = SafeConfigParser()
parser.read(env)
os.environ["ENV_FNM"] = parser.get("Config", "Environment")