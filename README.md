### Pyblish Standalone

This repository wraps Pyblish and it's GUI to provide for a method of running it via the command-line.

**Usage**

```bash
$ python -m pyblish_standalone
```

It has a number of arguments.

```bash
$ python -m pyblish_standalone -h
usage: __main__.py [-h] [-d key value] [--path PATH]

optional arguments:
  -h, --help            show this help message and exit
  -d key value, --data key value
                        Append data to context, can be called multiple times
  --path PATH           Append path to PYBLISHPLUGINPATH, can be called
                        multiple times
```

- See [the main Pyblish repository](https://github.com/pyblish/pyblish) for more information.
