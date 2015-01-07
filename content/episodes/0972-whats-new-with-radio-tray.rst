What's new with Radio Tray?
###########################
:slug: whats-new-with-radio-tray
:date: 2010-05-03 15:00
:category: English
:tags: english

` <http://radiotray.sourceforge.net/>`__

[caption id=”” align=”alignleft” width=”128”
caption=”RadioTray”]\ |RadioTray|\ [/caption]

`Radio Tray <http://radiotray.sourceforge.net/>`__, your favorite light
weight online radio streaming application, has gone under some more
development churn since its last release. Namely, there is now a **dbus
interface** to allow other applications to interact with it! So you
write a “remote control” for Radio Tray and change the volume, change
stations, extract metadata from the stream being played, etc. Here’s
what’s currently supported:

-  listRadios()
-  getCurrentRadio()
-  playRadio(name)
-  turnOff()
-  volumeUp()
-  volumeDown()
-  getCurrentMetaData()

Fancy learning a bit about adding a dbus interface to your own
application? Want to add new features to Radio Tray? A new
“\ **testdbus.py**" script has been added to the repository to help you
understand how things work and get you to hit the ground running! Just
clone the repository and take a peek:

``hg clone http://radiotray.hg.sourceforge.net:8000/hgroot/radiotray/radiotray``

Oh, and if you can help us **translate it into different languages**,
join our `effort <http://www.transifex.net/projects/p/radiotray/>`__ and
start helping today!

.. |RadioTray| image:: http://bit.ly/RadioTrayLogo
   :target: http://radiotray.sourceforge.net/
