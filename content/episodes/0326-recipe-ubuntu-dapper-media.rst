Recipe: Ubuntu Dapper Media
###########################
:slug: recipe-ubuntu-dapper-media
:date: 2006-06-10 17:03
:category:
:tags: english

With the release of Ubuntu Dapper, many were the new users who initiated
the linux world without any knowledge of how to configure their systems
for a complete nirvana experience. Sure the default instalation takes
care of supplying the majority of tools and applications a “normal” home
user would need “out of the box”, but there are certain technologies
which, due to some licensing issues (mostly related to distribution,
etc), are not installed automatically.It is with thys type of end user
that I present here my recipe. The steps below were performed as soon as
I finished the default installation, using the command line. Obviously,
the Synaptic Package Manager can also be used for a graphical
experience.For a faster and simpler browsing experience, I recommend the
installation of the Epiphany web browser:

    sudo apt-get install epiphany-browser epiphany-extensions

To add support to some of the default, but unfortunately proprietary,
web tecnologies:

    sudo apt-get install flashplugin-nonfree sun-java5-plugin

During the installation process for Flash and Java, confirm that you
accept the terms of their licences, by checking the appropriate check
box. To add support for multimedia contents, including MP3 and other
video formats:

    sudo apt-get install gstreamer0.10-plugins-bad sudo apt-get install
    gstreamer0.10-plugins-bad-multiverse sudo apt-get install
    gstreamer0.10-plugins-ugly sudo apt-get install
    gstreamer0.10-plugins-ugly-multiverse sudo apt-get install
    gstreamer0.10-pitfdll sudo apt-get install gstreamer0.10-ffmpeg

If you’ve seen some the old Clint Eastwood’s movies and have seen
Ã¢â‚¬Å“\ `The Good, the Bad, and the
Ugly <http://www.imdb.com/title/tt0060196/>`__\ Ã¢â‚¬Å“, will notice
that the packages gstreamer0.10-plugins-good\* are already installed
(default) in your system. |;)| And now, to add support for all other
types of proprietary media content (Ewwww!) which unfortunately plague
the WWW world , download the W32codecs package, pasting the following
URL into your favorite web browser (which by now should be Epiphany,
right?):

    `http://distrib-coffee.ipsl.jussieu.fr/pub/linux/plf/ubuntu/plf/pool/dapper/i386/non-free/w32codecs/w32codecs\_20050412-1plf4\_i386.deb <http://distrib-coffee.ipsl.jussieu.fr/pub/linux/plf/ubuntu/plf/pool/dapper/i386/non-free/w32codecs/w32codecs_20050412-1plf4_i386.deb>`__

After downloading it, double-click it with the left button of your mouse
to iniciate the installation process. When the “smoke” clears, you
should have a system ready for prime time usage! \* Thank you **Kai D.
Lahmann** for the tip (comment below). ;) \* Thank you **Brunno** for
pointing out my original mistake about the epiphany package. ;) \* Thank
you **slomo** for the gstreamer0.10-ffmpeg tip! ;)

.. |;)| image:: http://blog.ogmaciel.com/wp-includes/images/smilies/icon_wink.gif
