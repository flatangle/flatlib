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

Linux
-----
