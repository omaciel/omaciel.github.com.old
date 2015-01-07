Sharing music via Avahi
#######################
:slug: sharing-music-via-avahi
:date: 2006-06-12 14:31
:category:
:tags: english

What can I say, it was a busy weekend…Ã‚Â  ;)Ã‚Â  Prior to following my
friend Otavio’s
`advice <http://blog.canetatinteiro.org/2006/06/05/compartilhando-musicas-em-uma-rede-local-com-avahi-e-bansheerhythmbox/>`__
(pt\_BR only) on how to properly share my private music library at home
with the many devices I own, I sadly used to copy the many gigabytes of
\*.oggs across the network…Ã‚Â  Since I didn’t want to clog up my
TabletPC, I decided to give avahi a try.

    "Avahi is a system which facilitates service discovery on a local
    network. This means that you can plug your laptop or computer into a
    network and instantly be able to view other people who you can chat
    with, find printers to print to or find files being shared."Ã‚Â 
    `Avahi.org <http://avahi.org/>`__

Just reading this short description, one can already imagine the
possibilities…Ã‚Â  Anyhow, I already had Rhythmbox installed so all I
really needed was to install the avahi-daemon package in both devices:

sudo apt-get install avahi-daemon

and that was it!Ã‚Â  All there’s left to do is to configure the PC that
has your music library to share the goodies via the proper “Share” tab
in Rhythmbox’s preference dialog.

|image0|

The moment I opened Rhythmbox in my TabletPC, it automagically detected
the shared library and all there was left to do was walk around the
house listening to my zeroconf’ed new freedom!

Speaking of Rhythmbox, I wish it had the feature to load/unload music
files to my iPod.Ã‚Â  So far, Banshee is doing a great job at doing all
of the above, including sharing music, by using the banshee-daap
package.

.. |image0| image:: http://static.flickr.com/53/165636617_defbb2956a.jpg
   :target: http://static.flickr.com/53/165636617_defbb2956a_o.png
