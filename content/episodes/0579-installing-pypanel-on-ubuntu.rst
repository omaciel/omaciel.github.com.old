Installing PyPanel on Ubuntu
############################
:slug: installing-pypanel-on-ubuntu
:date: 2007-06-15 20:40
:category: English
:tags: english

A while back I had written up a post (Brazilian Portuguese only)
explaining how I managed to get PyPanel running on my old Ubuntu Feisty
Herd 3 installation. The reason for the write up was to explain about
how I circunvented two issues that came up during the process of getting
PyPanel to actually run. Anyhow, ever since I started writing up about
`OpenBox <http://icculus.org/openbox/>`__, more and more people tried to
use PyPanel and seem to have gotten bitten by the same problems. So,
without much further ado, here is what I did:

Out of all the task bars out there,
`PyPanel <http://pypanel.sourceforge.net/>`__ is the one that pleases me
the most. However, getting it to run on Ubuntu is not the most straight
forward thing to do, and requires some serious “tweaking/hacking”.
Searching the net, you’ll see a great deal of conflicting information,
some telling you to compile dependencies and what not from the source
code, and some telling you to “trust” the package manager. Back then I
decided to give aptitude the benefit of the doubt and tried to do a more
thorough investigation.

As soon as I logged into my Openbox session and opened up a console, I
started PyPanel by running pypanel in the command line. Boy, was I
surprised when I was presented the following traceback:

    omaciel@gorgonzola:~$ pypanel Traceback (most recent call last):
    File “/usr/bin/pypanel”, line 893, in <module> from Xlib import X,
    display, error, Xatom, Xutil File
    “/var/lib/python-support/python2.5/Xlib/display.py”, line 30, in
    <module> import protocol.display File
    “/var/lib/python-support/python2.5/Xlib/protocol/display.py”, line
    751 SyntaxError: Non-ASCII character ‘xf6’ in file
    /var/lib/python-support/python2.5/Xlib/protocol/display.py on line
    750, but no encoding declared; see
    `http://www.python.org/peps/pep-0263.html <http://www.python.org/peps/pep-0263.html>`__
    for details

The keyword here is the phrase “Non-ASCII character in line 750. Opening
the file /var/lib/python-support/python2.5/Xlib/protocol/display.py as
root and browsing that specific line showed me:

    # Bug reported by Ilpo NyyssÃƒÂ¶nen

The problem was the letter **ÃƒÂ¶**. Since I was in a hurry, I simply
changed that specific character to a “normal” letter o, saved it and
tried pypanel again from the command line. This time around I was
presented the following nasty-gram:

    omaciel@gorgonzola:~$ Traceback (most recent call last): File
    “/usr/bin/pypanel”, line 957, in <module> PyPanel(display.Display())
    File “/var/lib/python-support/python2.5/Xlib/display.py”, line 80,
    in \_\_init\_\_ self.display = \_BaseDisplay(display) File
    “/var/lib/python-support/python2.5/Xlib/display.py”, line 67, in
    \_\_init\_\_ apply(protocol.display.Display.\_\_init\_\_, (self, ) +
    args, keys) File
    “/var/lib/python-support/python2.5/Xlib/protocol/display.py”, line
    123, in \_\_init\_\_ self.default\_screen =
    min(self.default\_screen, len(self.info.roots) - 1) File
    “/var/lib/python-support/python2.5/Xlib/protocol/rq.py”, line 1371,
    in \_\_getattr\_\_ raise AttributeError(attr) AttributeError: roots

Damn it! That’s when I remembered reading a message somewhere in the net
about a problem with the buffer size in the same exact file, but for
Python 2.5. I remembered that the reserved buffer size was 2048, and the
work around called for changing it to 4096. Once again I opened the file
and modified the line below:

    recv = self.socket.recv(2048)

It was only after performing this “operation” that I was able to finally
run PyPanel.

|openbox|

Well, hope this will be of help to anyone out there experiencing the
same problems… and if anyone thinks this is a serious bug/limitation,
I’ll be glad to take it to the next level!

.. |openbox| image:: http://farm1.static.flickr.com/163/385691397_00104ffd4e.jpg
   :target: http://farm1.static.flickr.com/163/385691397_00104ffd4e_b.jpg
