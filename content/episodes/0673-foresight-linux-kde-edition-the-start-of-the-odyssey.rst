Foresight Linux KDE Edition: The start of the odyssey!
######################################################
:slug: foresight-linux-kde-edition-the-start-of-the-odyssey
:date: 2007-11-14 02:56
:category:
:tags: english

As I mentioned in my previous post, I decided to give KDE a chance on my
home system. For the last 5 days I’ve been neck deep in KDE land, with
some fairly minor trips to non-KDE applications when I can’t figure out
how to get something done (more on the soon).

The first step was to download the brand spanking alpha ISO for
**Foresight Linux KDE Edition**
(x86 `here <http://www.rpath.org/rbuilder/project/foresight/build?id=13206>`__
and
x86\_64 \ `here <http://www.rpath.org/rbuilder/project/foresight/build?id=13207>`__)
and bring it home. I waited until everyone was asleep to backup my files
and got ready for the long install… AND BOY WAS I DISAPPOINTED! The
install, including formatting my 200GB hard drive took 4 MINUTES!

|Foresight, KDE Edition|

Once I rebooted the machine I was faced with a pretty vanilla KDE
installation, with pretty much most of the applications out there
already installed for me. Since the last time I played with KDE was
several years ago, I took my time learning the applications and tweaking
my desktop look and feel to my heart’s content. The first thing that
captured my fancy was **Amarok**! WOW! I loaded my 22 GB of music in
there and let it sort it all out, including getting covers for the
albums, and moved on to **Akregator**. Having been a Liferea user for
quite some time, I felt right at ease with it and was able to import my
old feeds and start reading my news in no time.

Another application that has been tested and beaten to death is
**Konqueror**, and so far I have had only a few issues. Mind you that
**Firefox** is installed by default, but I wanted to have the whole KDE
experience and only used it for one single task. Right away I tried to
check my gmail and was warned that my browser wasn’t fully supported…
WHAT? The work around was to “fake” the site to think I was running
Firefox and the warning message was gone. If anyone from Google is
reading this, using my (really bad) Brooklyn accent: “Hey! Wasamatter
with you?” That is just ridiculous and I hope Konqueror gets its much
deserved love from Google. Now, the only issue I had with Konqueror was
when I tried to upload pictures into my
`Flickr <http://www.flickr.com/photos/ogmaciel/2009708182/>`__ account
(by the way, my PRO account expires today). For some reason, the browser
would bring me right back to the upload form as soon as I hit the save
button… that is when I fired up Firefox to bail me out. Weird.

Back to the distro, up until now the KDE edition has pretty much been
handled by a couple of guys (hey **jtate** and **int**!) and not much
time has been invested into making it more organized and give it some
proper love. I noticed that there were lots and lots of redundant
applications around and in some cases some categories were left out. The
only video player available was **Noatun** and it didn’t really work for
me (something related to being compiled against a conflicting arts
plugin). So the solution was to take advantage of a couple of free hours
here and there, coupled with the awesome power of the `conary packaging
system <http://wiki.rpath.com/wiki/Conary>`__ to start shaping it into…
errr… shape. I mean, I have never packaged anything in my life before
using conary, and so far I have taken on the maintenance of a few
packages. Obviously I have had help along the way, and `Ken
Vandine <http://ken.vandine.org/>`__ and `AntÃƒÂ³nio “doniphon”
Meireles <http://sbin.reboot.sh>`__ have taught me a lot! Anyone
interested in learning more about packaging or just curious about conary
should stop by #foresight and #conary on Freenode.

My idea is to make a list of all the current, installed by default
applications in each category and pick one to be installed by default.
Under “Internet”, leave Konqueror, Firefox, Kopete, Konversation,
Akregator and maybe KTorrent? Under “Multimedia”, Amarok (no brainer),
Kaffeine… WAIT!!! Kaffeine is not available! Luckily, a mere 9 lines of
python-like syntax yielded a brand new
`Kaffeine <http://kaffeine.kde.org>`__ application, packaged and ready
to be used by the masses! Let me say that again: **NINE** lines and it
was packaged! I told you conary was powerfull!

|Just packaged Kaffeine for Foresight|

So, what can you do to lend us a hand? Well, there are lots to do and
there’s room for everyone! You can start by downloading the ISO and
playing with it. If you’re interested in learning about conary so you
can help out with packaging, read the
`FAQ <http://wiki.foresightlinux.com/confluence/display/docs/FAQ>`__,
`Quick Reference <http://wiki.rpath.com/wiki/Conary:QuickReference>`__
and joining us on #foresight. Is art design your bag? We still don’t
have a nice green theme yet! How would you like to have your art in our
distro??? Remember, **Foresight is Green**!

My KDE Odyssey has just begun! More to come…

.. |Foresight, KDE Edition| image:: http://farm3.static.flickr.com/2004/2009708182_a4f58903da.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2009708182/
.. |Just packaged Kaffeine for Foresight| image:: http://farm3.static.flickr.com/2419/2009708180_c3978106fe.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2009708180/
