The Windmill Appliance
######################
:slug: the-windmill-appliance
:date: 2008-04-14 12:04
:category: English
:tags: english

I’m proud to announce the release of the `Windmill
Appliance <http://www.rpath.org/rbuilder/project/windmill/releases>`__!
Built with the technology provided by `rPath <http://www.rpath.com>`__,
it is currently available as a downloadable installable ISO as well as a
VMWare image for you pleasure.

Now, just what is the windmill appliance for, you may ask? Glad you did…
`Windmill <http://windmill.osafoundation.org/>`__ is an **Open Source
AJAX Web UI Testing framework**. For the last couple of months I have
relied heavily on this software to properly test the web UI of one of
our products, and the results have been quite pleasant. Moreover, the
interaction that I have developed with the core developers (I’m always
lurking on #windmill at Freenode) has proved to be extremely beneficial
from my point of view.

The fact that I can get the windmill software packaged and deployed,
ready for use in literally minutes using
`Conary <http://wiki.rpath.com/wiki/Conary>`__ and
`rBuilder <http://www.rpath.com/corp/products-rbuilder.html>`__ allows
me to provide quick feedback to the developers who, I must say, have
been very accomodating to my pestering. :) This appliance is my way to
thank them for their hard work, and also as means to help out other
fellow developers in need of an efficient way to test their project’s
web ui.

It was designed to work as a headless (i.e. simplistic and minimal)
appliance where you can remotely conduct your tests. A Vnc server is
automatically started on port 5901 for you, as well as SSH so you can
get things rolling really quickly. You just start it up somewhere in
your network (or even several of them in a cluster) and fire your tests
at will leaving your system intact.

Please feel free to ask me either here or on #windmill about the
appliance as well as how you too can customize it for your own needs.

**UPDATE**: The user for the VMWare appliance is root with a blank
password. Change it quick! :)
