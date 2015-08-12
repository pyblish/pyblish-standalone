import os

import executable


plugins_path = os.path.join(os.path.dirname(__file__), 'plugins')
try:
    os.environ['PYBLISHPLUGINPATH'] += os.pathsep + plugins_path
except:
    os.environ['PYBLISHPLUGINPATH'] = plugins_path

executable.main()

raw_input()
