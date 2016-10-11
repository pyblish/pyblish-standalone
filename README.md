### Pyblish Standalone

This repository wraps Pyblish and it's GUI to provide for a method of running it via the command-line.

**Usage**

```bash
$ python -m pyblish_standalone
```

It has a number of arguments.

```bash
$ python -m pyblish_standalone -h
usage: __main__.py [-h] [-d key value] [--path PATH] [--register-host HOSTNAME] [--register-gui GUINAME] [-debug]

optional arguments:
  -h, --help            Show this help message and exit
  -d KEY VALUE, --data KEY VALUE
                        Append data to context, can be called multiple times.
  --path PATH           Append path to PYBLISHPLUGINPATH, can be called
                        multiple times.
  -rh HOSTNAME, --register-host HOSTNAME
                        Register host name before starting the Pyblish.
  -rg GUINAME, --register-gui GUINAME
                        Validates and uses the gui name in the order specified.
  --debug               Registers mock plugins for debugging.
```

You can also pass in a file, which will become the current file in the context

```bash
$ python -m pyblish_standalone "/path/to/file"
```
```python
>>> context.data["currentFile"]
"/path/to/file"
```

- See [the main Pyblish repository](https://github.com/pyblish/pyblish) for more information.
