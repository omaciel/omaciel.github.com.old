The new GNOME Display Manager (GDM)
###################################
:slug: the-new-gnome-display-manager-gdm
:date: 2008-05-22 14:22
:category: English
:tags: english

I started today using the new GNOME Display Manager, aka GDM. This new
version (under development) was initially written before the GNOME 2.22
release but never made it on time for that release.

Some of new features are:

-  Better fast-user-switching support (`bug
   #343539 <http://bugzilla.gnome.org/show_bug.cgi?id=343539>`__ etc)

-  Enable a smarter people chooser in the greeter
-  Better `ConsoleKit <http://live.gnome.org/ConsoleKit>`__ integration
   (seat awareness, coordination etc)

-  Facilitate creating a new blingier greeter
-  Dynamically configure displays
-  Allow session agents to run in the greeter session
   (gnome-power-manager etc)
-  Have the ability to only run a single greeter per seat (currently
   gdmflexiserver will start any number of them)
-  Use `PolicyKit <http://live.gnome.org/PolicyKit>`__ for reboot etc
   authorization/handling

-  Use a better configuration mechanism that is more compatible with a
   hypothetical systemwide D-Bus based GConf
-  Provide a D-Bus API so that agents like fast-user-switch applet can
   be written more easily and operate more efficiently
-  Fix all the horrible non-reentrant POSIX signal handling and various
   race conditions in the current code (`bug
   #336549 <http://bugzilla.gnome.org/show_bug.cgi?id=336549>`__ etc)

-  Make it easier to do “hot desking” type things

-  Use a more modern design to simplify maintence and enhance
   flexibility (use of GObject etc)
-  Use a more robust, secure, and flexible IPC

… and many more. For a complete list, take a peak at their new design
`page <http://live.gnome.org/GDM/NewDesign>`__.

You can see the GDM’s “greeter” with the new user selector:

|The new login screen|

Once you choose your user account, you’ll see some options related to
the session and language:

|Chosing your user|

When you lock a session…

|Locked session|

… and when you unlock it:

|Unlock the session|

Since it is still under development, don’t forget to report any bug or
issues you find.

Once you have entered your credentials, you can then have your desktop
enviroment loaded and ready to use (in this case,
`Openbox <http://icculus.org/openbox/index.php/Main_Page>`__):

|My Openbox desktop|

.. |The new login screen| image:: http://farm3.static.flickr.com/2378/2513932416_676d4a06cb.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2513932416/
.. |Chosing your user| image:: http://farm3.static.flickr.com/2056/2513932290_9a0d64de4d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2513932290/
.. |Locked session| image:: http://farm4.static.flickr.com/3047/2513932060_10eda63eca.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2513932060/
.. |Unlock the session| image:: http://farm3.static.flickr.com/2042/2513932168_eb858824c6.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2513932168/
.. |My Openbox desktop| image:: http://farm3.static.flickr.com/2205/2513932562_0d3489793c.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2513932562/
