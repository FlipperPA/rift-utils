# Rift Utils

Utilities for the game Rift. Right now, just a Python script to run on a cron and notify when certain events are running.

# First Time Installation (Instructions for Windows; will install on Desktop)

* Download and install the latest Python from here: https://www.python.org/downloads/
* Download this package to desktop and unzip: https://github.com/FlipperPA/rift-utils/archive/master.zip
* Edit the file `rift-utils\rift.py` and fill in your email addresses on the two lines given, and enter the names of Zone Events in the list you want to track.
* Start the Windows command prompt. (Press the Windows Key + R, then type `cmd` and hit enter)
* Issue the following commands:

```
cd Desktop\rift-utils-master
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python rift.py
```

If you want to run it every minute (recommended), you'll have to set it up as a Windows scheduled task.
