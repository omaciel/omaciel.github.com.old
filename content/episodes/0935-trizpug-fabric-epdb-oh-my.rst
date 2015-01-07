TriZPUG, Fabric, epdb, oh my!
#############################
:slug: trizpug-fabric-epdb-oh-my
:date: 2010-01-29 20:48
:category: English
:tags: english

Yesterday I attended my first `TriZPUG <http://trizpug.org/>`__ meeting
to check out `Kurt Grandis <http://kurtgrandis.com/>`__' talk on
`Fabric <http://docs.fabfile.org/0.9.0/>`__, “\ *a Python library and
command-line tool for streamlining the use of SSH for application
deployment or systems administration tasks.*\ ”

It was pretty cool to see a bunch of guys who share the same interests
take some time on a Thursday to hang out, drink beers, and chat about
python, django, zope, and other stuff. After the original talk was over
and some of the other lightening talks that succeeded it was over, a
couple of things became very clear to me:

-  There was a real need to make it easier for system administrators and
   OPS people to handle the difficult task of deploying and maintaining
   systems, cloud or not;
-  Some of the tools and/or tool implementations presented were being
   used in an attempt to minimize this pain, but you were still pretty
   much had no control over what made its way to the systems in the end
   of the process;

Having been using `rBuilder Online <http://www.rpath.org>`__ to manage
and maintain my `Transifex Appliance <http://bit.ly/Transifex>`__, and
being somewhat “spoiled” with the ability of having fine grained control
over the entire software stack and having the option of deploying my
final “product” on several different cloud environments, I couldn’t help
but offer to speak a bit about my experience. I sure hope my impromptu
presentation didn’t come across as being “just a sell’s pitch” and I
definitely tried my best not to sound like I was selling something. I
truly feel that the technology developed here at
`rPath <http://www.rpath.com>`__ can solve many of the typical issues
that people have getting their product through the many different life
cycles and eventually out the door and into the hands of their
customers!

Today I started going through Fabric’s documentation and am already
making plans to include it in some of the test automation tools we’re
developing here!

Anyhow, after my presentation there was a quick intro to
`epdb <http://bitbucket.org/dugan/epdb/>`__, the “Extended Python
Debugger”, a very cool python debugger developed by an ex-rPathian and
something I use on a daily basis! Turns out that the **epdb** currently
packaged for `Foresight Linux <http://foresightlinux.org>`__ was
outdated, so I spent a few minutes during my lunch today to update it.
If you’re running Foresight, just run ***conary update epdb=:2-devel***
or wait for it to make its way to the stable label. If you’ve never
heard of epdb, I strongly suggest you give it a try!
