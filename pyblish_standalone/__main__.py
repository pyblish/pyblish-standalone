import os
import sys
import argparse

import executable
import pyblish_standalone


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", nargs=2, action="append",
                        metavar=("key", "value"),
                        help="Append data to context")

    try:
        kwargs = parser.parse_args(sys.argv[1:])
    except SystemExit as e:
        raise Exception(e)

    # Store reference to keyword arguments, for Collection
    pyblish_standalone.kwargs = kwargs

    plugins_path = os.path.join(os.path.dirname(__file__), 'plugins')
    try:
        os.environ['PYBLISHPLUGINPATH'] += os.pathsep + plugins_path
    except:
        os.environ['PYBLISHPLUGINPATH'] = plugins_path

    executable.start()

    print("Press any key to quit..")
    raw_input()

    # Close GUI on terminal session end
    executable.stop()


if __name__ == '__main__':
    cli()
