#library import
from ConfigParser import SafeConfigParser
import os

#get environment variables
basepath = os.environ["BASEPATH"]
currentpath = os.environ["CURRENTPATH"]
env_fnm = os.environ["ENV_FNM"]

#environment program
def environment( section, field):
  env = os.path.abspath(os.path.join(currentpath, env_fnm))
  parser = SafeConfigParser()
  parser.read(env)
  return parser.get(section, field)


#config program
def config( section, field): 
  cfg = os.path.abspath(os.path.join(currentpath, environment( "Config", "Config")))
  parser = SafeConfigParser()
  parser.read(cfg)
  return parser.get(section, field)