Using Dropbox with Openbox
##########################
:slug: using-dropbox-with-openbox
:date: 2008-10-23 14:02
:category:
:tags: english

I’ve been a GNU/Linux user for quite some time now, but it wasn’t until
2 years ago that I became a fulltime user. Being a .NET and Oracle
developer by day working for the Department of Education of NYC, I had a
standard developer environment at my desk and nothing else. That means
that I could not install anything else on my system, due to some
extremelly archaic policies put in place by the employer (I couldn’t
even search for information online and was told I should do it from home
and bring the results to work the next day!!!), but that’s material for
a different post.

The one way I work around the limitations was by using some of those
`portable applications <http://portableapps.com/>`__ that can run off a
thumbdrive, and for 2 years I was an avid user of Portable Firefox. I
also used to save some of my code in that same thumbdrive so that I
could work on it from home after hours (yeah, no remote access either).
After a while, keeping bookmarks, code and files in sync between my
Windows system at work and my GNU/Linux system at home became a chore
and just down painfull.

Fast foward the movie and you’ll find me now at a different employer
(heck, a different state too!) where I get to use open source all the
time! If I thought I knew a thing of two about using and configuring
systems and applications, I learned quickly that I had a lot to learn! I
quit using graphical text editors (no offense to gedit) and became an
avid vim user, traded my Firefox and Winamp for Epiphany and Rhythmbox,
and was able to go back to using one of my all time favorite windows
manager: `Openbox <http://icculus.org/openbox/index.php/Main_Page>`__.
Don’t get me wrong, I have absolutely nothing against other windows
managers, but it is Openbox that has always tickled me the right way
since my Gentoo days.

So there I was, a happy open source user learning tons of new stuff and
doing some pretty cool work, but… since I was given a work laptop, I
still had issues with synching files between my home and work systems.
Yeah, yeah, there were some tools out there and obviously I could now
(or write my own) scripts to help out but that was still painful! I
wanted something that worked without a lot of work out of the box with
seamless synchronization, always on and easy to use. The day
`Dropbox <http://www.getdropbox.com/>`__ for GNU/Linux was announced was
the day I stopped carrying a thumbdrive!

Since I’m not trying to pimp Dropbox, suffice to say that:

    -  Dropbox is the easiest way to share and store your files online.
    -  No complicated interfaces to learn. Dropbox runs in the
       background on your desktop.
    -  Sync your files automatically to your computers and the web.
    -  Sign in and access your files from any browser or mobile device.
    -  Sharing files with your friends and family is just two clicks
       away.

Sounds interesting, doesn’t it? Well, there’s more! The free account
offers you 2GB of storage on Amazon’s S3 systems, and all of your files
are transferred over SSL and encrypted with AES-256 and stored as a
delta sync of the previous state. Can you say “versioning control”?

|Dropbox|

Well, there is a downside to this whole thing though, as it turns out
that Dropbox claims that it integrates really well with Nautilus, which
pretty much locks out non-GNOME users… or does it?

The other night I was complaining about this same issue to a good friend
when he suggested, “why don’t you see if the daemon is running and doing
its thing without Nautilus?” So I switched over to Openbox and… no
Dropbox! I pushed on and ``ps aux | grep drop`` told me that the
dropboxd “daemon” was started from my ``$HOME/.dropbox-dist/``
directory. I quickly added a ``"~/.dropbox-dist/dropboxd &"`` line to my
``$HOME/.config/openbox/autostart.sh`` file, restarted Openbox and… it
worked! I didn’t get the nice little tray icon in my pypanel, but it
worked as I made changes to a file and saw the information about the
changes I made appear in my dropbox home page! Ohhh, the
possibilities!!!

The first thing I did was to create a dotfiles directory inside of the
newly created ``$HOME/Dropbox`` directory, and moved all my dot files
(.vimrc, .bashrc, etc) there. I then created symbolic links in their
places so that my dotfiles were all links to the files in the
``$HOME/Dropbox/dotfiles`` as such:

    $HOME/.vimrc -> Dropbox/dotfiles/.vimrc $HOME/.bashrc ->
    Dropbox/dotfiles/.bashrc

I also added all of my $HOME/.config/openbox directory and replaced it
with a symlink to garantee that my Openbox environment, menus and
customizations would be available to me, as well as my $HOME/.ssh and
$HOME/.gnupg directories. Are you drooling yet?

The next day I went to work (I rarely open my work laptop at home) and
installed Dropbox followed by creating those same symlinks as my home
system, and that was it! My work system was an exact mirror of my home
system, and best of all, every time I make any changes to any of those
files, they get automatically synchronized and made available to both
systems!

|Openbox with Dropbox (not seen) makes for a great system|

In conclusion, Openbox with Dropbox is really a great combination for
anyone looking for a light and powerful windows manager with an easy to
use automatic backup/synchronization system! I highly recommend it! A
couple of things that I’d like to see happening with future versions of
Dropbox is a standardization of the location for the dropboxd daemon and
official support for any type of file manager. Also, an easy way to
revert changes to a file (remember that they are all versioned) without
having to overwrite them would be nice… Keep up the good work and I look
forward to any new feature you may add in the future releases! :)

.. |Dropbox| image:: https://www.getdropbox.com/static/images/tour3b.png
.. |Openbox with Dropbox (not seen) makes for a great system| image:: http://farm4.static.flickr.com/3003/2948601731_c75de0fd08.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2948601731/
