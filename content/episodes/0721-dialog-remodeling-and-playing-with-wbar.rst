Dialog remodeling and playing with wbar
#######################################
:slug: dialog-remodeling-and-playing-with-wbar
:date: 2008-02-11 02:30
:category:
:tags: english

I have spent a total of 3 hours working on
`BillReminder <http://billreminder.gnulinuxbrasil.org/>`__ these last 2
weeks! What can I say, sometimes you have to put your pet projects in
the back burner while real life takes over. :/

One of the things that annoyed me was the old, cluttered preferences
dialog. It was just too bulky and with too many things going on,
specially with the ComboBox for selecting the prefered time for an
alarm. It had entries for every hour in intervals of 30 minutes (i.e.
01:00, 01:30, 02:00, etc) for a huge, scroll off your screen list.

|Old Preferences Dialog|

So I took it behind the shed and let it have it! I made some layout
changes and replaced the ComboBox with a custom time widget with
SpinButtons. It is not all I wanted it to be but I’m not as annoyed
about it anymore.There are 2 other things I want to get done before
releasing a newer version, but I’m not sure what my schedule will be
like this week. :/

|New Preferences Dialog|

Today I took 30 minutes to package
`wbar <http://freshmeat.net/projects/wbar/>`__ (my local repository) and
added it to an `Openbox <http://www.icculus.org/openbox>`__ by default
distro I’ve been working on. It feels very light and snappy, without any
X compositing going on. I’ve also experienced with moving pypanel to the
top but am not sure what to make out of it. I also experienced getting
**GDM** to consider Openbox its default session and ended up having to
make a few changes to **Xsession** to get it working. Ugly but worked.

|Perere Linux with wbar and pypanel|

I also had a major fight getting **PulseAudio** to start automatically.
My approach was to drop a pulseaudio-openbox.desktop file in
/etc/xdg/autostart, which called a shell script to start PulseAudio… but
apparently this will only work for session managers and Openbox doesn’t
have one. I ended up having to change openbox-session script to make it
work. Any insights would be appreciated.

.. |Old Preferences Dialog| image:: http://farm3.static.flickr.com/2152/2254574149_a11e85bac8_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2254574149/
.. |New Preferences Dialog| image:: http://farm3.static.flickr.com/2055/2255356186_719bb260a2_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2255356186/
.. |Perere Linux with wbar and pypanel| image:: http://farm3.static.flickr.com/2039/2255962057_9e4722c96b.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2255962057/
