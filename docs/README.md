# Flatlib documentation

This document explains how you can setup your environment to build and contribute to the flatlib documentation.


## Readthedocs

Flatlib's documentation is available at [http://flatlib.readthedocs.org/](http://flatlib.readthedocs.org/). Every change to this repository triggers an immediate documentation build on the readthedocs server. 


## Installing Sphinx and Sphinx-autobuild

### Sphinx

The flatlib documentation is built from reStructuredText sources using [Sphinx](http://sphinx-doc.org/). 
The preferred way of installing Sphinx is with pip:

* `pip install sphinx` on Linux or Mac.
* `py pip install sphinx` on Windows.

Refer to the [Sphinx documentation](http://sphinx-doc.org/install.html) for alternative ways to install Sphinx in your environment.

### Sphinx-autobuild

Sphinx-autobuild is a tool to watch a Sphinx directory and rebuild the documentation when a change is detected. 
To install sphinx-autobuild use:

* `pip install sphinx-autobuild` on Linux or Mac.
* `py pip install sphinx-autobuild` on Windows.


## Build the documention

There are two ways for building the documentation, both made possible by the available makefiles. Open a terminal or command prompt and *cd* into the *docs* directory: 

* To build the HTML documentation, execute `make html`. The generated documentation will be at *docs/build/html*.
* Execute `make livehtml` to start the autobuild server. Visit the webpage served at `localhost:8000`, and the server will autoreload the page when a change is detected. Quit the server by pressing Ctrl+C (or Command+C).