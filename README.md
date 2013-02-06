Minutedock for Ubuntu
=====================

The application displays Minutedock's current entry in the application 
indicator, allowing to start and pause the timer.

So far, it works (it was tested) in the following desktop environments:

* Unity
* KDE

If you find it works fine in other environments (or even other Linux
distributions), let us know!

Contributions are welcome.

Downloading the application
---------------------------

Clone the application repository:

        git clone git@github.com:gusaaaaa/minutedock-ubuntu.git

Requirements
------------

* Git (to download the application)
* Python 2.7.3 or up
* Works on Ubuntu
* A Minutedock account
* An internet connection while the app is open

Configuration
-------------

* Obtain your API key from your Minutedock's profile page.
* Export the key to the MINUTEDOCK\_KEY environment variable:
      `export MINUTEDOCK_KEY=your_key_here`

To avoid exporting the key every time before executing the app, it's
recommended to create a shell script named `minutedock` containing
following commands:

        export MINUTEDOCK_KEY=your_key_here
        python minutedock.py &

Notice that the script must be located in the app's base directory,
at the same level as minutedock.py file.

Then, make the script executable:

        $ chmod +x minutedock

Usage
-----

If you've created the shell script, from the app's base directory
write:

        $ ./minutedock

If you have not, write:

        $ export MINUTEDOCK_KEY=your_key_here
        $ python minutedock.py &

