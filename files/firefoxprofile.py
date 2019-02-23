import ConfigParser
import os
import sys
Config = ConfigParser.ConfigParser()
Config.read(os.path.expanduser("~"+sys.argv[1]+"/.mozilla/firefox/profiles.ini"))
for section in Config.sections():
    #loop all profiles ignoring General block which is not a profile
    if section != "General" and Config.get(section,"Name") == sys.argv[2].rstrip():
        print Config.get(section,"Path")
        exit(0)
exit(1)