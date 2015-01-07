I got your latest GNOME right here!
###################################
:slug: i-got-your-latest-gnome-right-here
:date: 2009-07-30 21:22
:category: English
:tags: english

Just wanted to re-enforce what
`Zhang <http://blog.zhangsen.org/2009/07/release-gnome-developer-kit-22720090727.html>`__
said earlier today about the bleeding edge `GNOME Developer’s
Kit <http://live.gnome.org/GnomeDeveloperKit>`__, now with extra sauce!

What is it? It is a **continuous** build of GNOME packages all bundled
up into a distribution (in this case, `Foresight
Linux <http://www.foresightlinux.org>`__) and distributed in a few
different formats, such as ISO and VMware.

|GNOME Developer Kit|

"What’s so special about it", you ask? Is it the fact that different
image types can be generated at will? Nah, generating images is
children’s play, just ask the **Suse Studio** guys. What is special is
the sauce used to not only allow the quick and painless releases but
also managing it as if the entire system was under a version control.
Did I say “as if”? I meant to say, “manage it under a version control”!
If you want to try this succulent sauce, ask your favorite release and
management provider for
`conary <http://en.wikipedia.org/wiki/Conary_(package_manager)>`__!

So Zhang has created a mechanism that allows him to package (and
maintain and update) the GNOME applications directly from their
respective **Git** repositories on a daily basis and bundling it all up
under a distribution. Every day you can then ask
`PackageKit <http://live.gnome.org/PackageKit>`__ to update your system
to whatever was built the previous day (or you can run *sudo conary
updateall* from the command line) and check what new things have
arrived.

If you are a **developer**, you could then push your code to your
repository and see what it looks like running under the **GNOME
Developer’s Kit** without having to jump through many hoops!

If you are a **contributor**, you could test these applications and
report issues right away to the developers so that they can look into
it. Better yet, you could even generate a patch and send it along with
your report! Want to kick it up a notch? Learn `how to package that same
application with your
patches <http://live.gnome.org/GnomeDeveloperKit/BuildingPackages>`__
and play with it before sending it in!

If you’re a **translator** or writing docs, imagine being able to see
the application you’re trying to translate running right in front of
you! As the GNOME Developer’s Kit already comes with a lot of tools such
as **gettext**, **intltool** and **poEdit**, you got your work cut out
for you!

|Doing GNOME translations|

So, are you interested? Go `download <http://gnome.rpath.org/>`__ it
right now and join us on #foresight on irc.freenode.net today!

.. |GNOME Developer Kit| image:: http://farm3.static.flickr.com/2580/3773369282_f3ee0e66b7.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3773369282/
.. |Doing GNOME translations| image:: http://farm4.static.flickr.com/3563/3773369348_1d04793f0e.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3773369348/
