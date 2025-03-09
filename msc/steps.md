## steps I followed

```bash
conda install -c conda-forge ffmpeg
```






sxx@raspberrypi:~/Station/UdeMHack $ python pc.py 
Traceback (most recent call last):
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/_core/__init__.py", line 23, in <module>
    from . import multiarray
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/_core/multiarray.py", line 10, in <module>
    from . import overrides
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/_core/overrides.py", line 8, in <module>
    from numpy._core._multiarray_umath import (
ImportError: libopenblas.so.0: cannot open shared object file: No such file or directory

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/__init__.py", line 114, in <module>
    from numpy.__config__ import show as show_config
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/__config__.py", line 4, in <module>
    from numpy._core._multiarray_umath import (
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/_core/__init__.py", line 49, in <module>
    raise ImportError(msg)
ImportError: 

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy C-extensions failed. This error can happen for
many reasons, often due to issues with your setup or how NumPy was
installed.

We have compiled some common reasons and troubleshooting tips at:

    https://numpy.org/devdocs/user/troubleshooting-importerror.html

Please note and check the following:

  * The Python version is: Python3.9 from "/usr/bin/python"
  * The NumPy version is: "2.0.2"

and make sure that they are the versions you expect.
Please carefully study the documentation linked above for further help.

Original error was: libopenblas.so.0: cannot open shared object file: No such file or directory


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/sxx/Station/UdeMHack/pc.py", line 7, in <module>
    from find_symptom import find_most_relevant_symptom
  File "/home/sxx/Station/UdeMHack/find_symptom.py", line 3, in <module>
    from scipy.spatial.distance import cosine
  File "/home/sxx/.local/lib/python3.9/site-packages/scipy/__init__.py", line 47, in <module>
    from numpy import __version__ as __numpy_version__
  File "/home/sxx/.local/lib/python3.9/site-packages/numpy/__init__.py", line 119, in <module>
    raise ImportError(msg) from e
ImportError: Error importing numpy: you should not try to import numpy from
        its source directory; please exit the numpy source tree, and relaunch
        your python interpreter from there.