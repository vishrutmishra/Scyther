from ConfigParser import SafeConfigParser
import os
#Update Current Path environment variable
os.environ["CURRENTPATH"] = os.path.dirname(__file__)

currentpath = os.environ["CURRENTPATH"]
envpath = 'vars.env'
env = os.path.abspath(os.path.join(currentpath, envpath))
parser = SafeConfigParser()
parser.read(env)

for section_name in parser.sections():
    for name, value in parser.items(section_name):
        env_var = section_name + '_' + name
        os.environ[env_var] = value