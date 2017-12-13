Installation using pip
======================

System-wide
-----------

::

    sudo pip install --install-option='-O2' sqlconvert


User mode
---------

::

    pip install --user --install-option='-O2' sqlconvert

Virtual envs
------------

::

    pip install --install-option='-O2' sqlconvert

Installation from sources
=========================

To install the library from sources system-wide run run the following
command:

::

    sudo python setup.py install -O2

If you don't want to install it system-wide you can install it in your
home directory; run run the following command:

::

    python setup.py install --user -O2

Option '--user' installs sqlconvert into
$HOME/.local/lib/python$MAJOR.$MINOR/site-packages/ where python finds it
automatically. It also installs sqlconvert scripts into $HOME/.local/bin;
add the directory to your $PATH or move the scripts to a directory in your
$PATH.
