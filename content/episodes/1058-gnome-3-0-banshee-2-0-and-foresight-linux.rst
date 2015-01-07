GNOME 3.0, Banshee 2.0 and Foresight Linux
##########################################
:slug: gnome-3-0-banshee-2-0-and-foresight-linux
:date: 2011-04-06 23:01
:category: English
:tags: english

[caption id=”attachment\_1388” align=”alignleft” width=”200”
caption=”GNOME 3.0”]\ |GNOME 3.0|\ [/caption]

First off, congratulations to everyone involved in the release of `GNOME
3.0 <http://www.gnome.org/news/2011/04/gnome-3-0-has-arrived/>`__! In
the past, my contributions were mostly related to translating
applications to `Brazilian
Portuguese <http://l10n.gnome.org/languages/pt_BR/>`__, but my role on
that front was very minimal this time and consisted of a handful of
translations and several commits of the awesome work done by others.
Most of my contributions for 3.0 are related to the work I do for the
**GNOME Foundation Board of Directors**, but I won’t bore you to tears!

Also, a huge congrats to the **Banshee** crew with their
`2.0 <http://gburt.blogspot.com/2011/04/banshee-20-is-here.html>`__
release! I wonder what is the next platform they’re going to take on now
that both Windows and Mac are already supported. ;)

I wanted to inform anyone who’s currently running `Foresight
Linux <http://www.foresightlinux.org>`__ what to expect as far as when
**GNOME 3.0** will be available via an update. Basically, in order to
bring this new release to our Foresight users, the following tasks (in
ascending degree of complexity and potential risk to stability and
usability) must be tackled:

#. Update **Glib** and create a separate **Gtk3** package that can
   co-exist with **Gtk2**
#. Update all packages that have a dependency on
   **gobject-introspection**
#. Update packages to use new **Gtk3** package, considering that some
   packages may have duo-binding to **Gtk2** and **Gtk3**
#. Re-build **all GNOME packages** as well as anything that has a
   dependency on **Gtk2/Gtk3**

The biggest concern right now is breaking our existing **KDE** and
**Xfce** packages, so will do our best to throughly test the update and
migration processes **before** making GNOME 3.0 available. In the
meantime, other packages will be updated and made available to you
(`Banshee
2.0 <http://gburt.blogspot.com/2011/04/banshee-20-is-here.html>`__ is
already available!)  via the usual command: ***sudo conary updateall***

Work has also started to bring **PackageKit** back to **Foresight** to
provide a graphical interface for all your package management needs. The
future promises!

.. |GNOME 3.0| image:: http://www.ogmaciel.com/wp-content/uploads/2011/04/iamgnome.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2011/04/iamgnome.png
