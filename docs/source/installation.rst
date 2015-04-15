Installation
============

The following instructions will install flatlib from the source files. In the future, binaries may be made available
and the instructions will be updated accordingly.

Windows
-------

If you don't have Python 3 installed on your system, download and install the latest Python 3.4 for Windows from 
https://www.python.org/downloads/. You can check if the interpreter was correctly installed by executing ``py`` on the 
command line.

Open a Windows command prompt (or exit the Python interactive shell) and install flatlib using ``py -m pip install 
flatlib``.

If you get an error such as  **Microsoft Visual C++ 10.0 is required (Unable to find vcvarsall.bat)**, you will have
to install a C compiler. The compiler is required to build *pyswisseph* - the Python port of the Swiss Ephemeris.

There are several C compilers for Windows, such as Cygwin and MinGW, but Visual C++ 2010 is the most used for compiling
Python 3 extensions on Windows. Download Microsoft Visual C++ 2010 Express from http://go.microsoft.com/?linkid=9709949 
(it may require the creation of a free Windows Developer account). After the installation, execute the following on
the command line::

   set CL=-DWIN32
   py -m pip install flatlib

You should now have flatlib installed in your system.

OS X
----

Latest versions of OS X are bundled only with Python 2. The preferred way to install Python 3 in OS X is using the
homebrew package manager (http://brew.sh/). Install homebrew and then install Python 3 using ``brew install python3``.

Before you install flatlib, you must have a C compiler in your system. This is because flatlib depends on the Swiss 
Ephemeris which is implemented in C. Fortunatelly, Apple provides the *Xcode Command Line Tools* which bundles a C 
compiler. To install it, open the terminal (Applications/Utilities/Terminal) and execute ``gcc``. 
You'll see an alert box if you don't have a compiler installed:

.. image:: _static/xcode-command-line-tools.png
   :align: center

If you don't need the entire Xcode (about 2.5GB) just press **Install**..

Finally, to install flatlib use ``pip3 install flatlib``.


Linux
-----

Python 3 is already included on most of the newer distributions. The simplest way to test for the existence of Python 3 
is to open the terminal and execute ``python3`` to start the interactive python interpreter. 
If the interpreter is not found, you will have to install it from your distribution's repo. 

To install flatlib, use ``pip3 install flatlib``. It may require you to install *pip* and other python 3 development 
libraries.

If you get a Permission Denied error, execute the previous command with ``sudo``.


Testing the installation
------------------------

Start the python3 interactive interpreter (``python3`` on Linux and Mac, and ``py`` on Windows) and execute the 
following::

   >>> import flatlib
   >>> flatlib
   <module 'flatlib' from '/usr/local/lib/python3.4/dist-packages/flatlib/__init__.py'>
   
If you don't get an import error, flatlib is installed in your system.


Upgrading from a previous version
---------------------------------

To upgrade from a previous version, run:

* ``pip3 install flatlib --upgrade`` in Linux and Mac. 
* ``py pip install flatlib --upgrade`` in Windows. 


Uninstalling
------------

Just do ``pip3 uninstall flatlib`` on Linux and Mac or ``py pip uninstall flatlib`` on Windows.
