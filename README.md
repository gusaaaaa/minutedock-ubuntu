Minutedock for Ubuntu
=====================

The application displays Minutedock's current entry in the application 
indicator, allowing to start and pause the timer.

Requirements
------------

* Python 2.7.3 or up
* Works on Ubuntu
* A Minutedock account
* An internet connection while the app is open

Configuration
-------------

* Obtain your API key from your Minutedock's profile page.
* Export the key to the MINUTEDOCK\_KEY environment variable:
      `export MINUTEDOCK_KEY=your_key_here`

Usage
-----

From the command line execute:

    python minutedock.py

