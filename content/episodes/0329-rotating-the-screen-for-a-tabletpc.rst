Rotating the screen for a TabletPC
##################################
:slug: rotating-the-screen-for-a-tabletpc
:date: 2006-06-12 03:04
:category:
:tags: english

This was a very busy Sunday, with a lot of soccer on tv (or how we call
it outside the U.S., football), a lot of beer, and B-B-Q, like a good
brazilian should.Ã‚Â  ;)Ã‚Â  In between a lot of meat, beer, checking
translations, participating on a podcast, and an unexpected visit from
my in-laws, I somehow managed to “play” with my TabletPC and rotate the
screen.Ã‚Â  The tip came via a comment on my previous post, and involves
the addition of a simple line in the xorg.conf file:Option
Ã¢â‚¬Å“RandRRotationÃ¢â‚¬Â?

    Section Ã¢â‚¬Å“DeviceÃ¢â‚¬Â? Identifier Ã‚Â  Ã‚Â  Ã‚Â Ã¢â‚¬Â?NVIDIA
    Corporation NV17 [GeForce4 420 Go 32M]Ã¢â‚¬Â? Driver Ã‚Â  Ã‚Â  Ã‚Â 
    Ã‚Â  Ã‚Â Ã¢â‚¬Â?nvidiaÃ¢â‚¬Â? BusID Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â 
    Ã¢â‚¬Å“PCI:1:0:0Ã¢â‚¬Â³ **Option Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â 
    Ã‚Â Ã¢â‚¬Â?RandRRotationÃ¢â‚¬Â?** EndSection Section
    Ã¢â‚¬Å“MonitorÃ¢â‚¬Â? Identifier Ã‚Â  Ã‚Â  Ã‚Â Ã¢â‚¬Â?Generic
    MonitorÃ¢â‚¬Â? Option Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â Ã¢â‚¬Â?DPMSÃ¢â‚¬Â?
    HorizSync Ã‚Â  Ã‚Â  Ã‚Â  28-51 VertRefresh Ã‚Â  Ã‚Â  43-60
    EndSection

All you have to do is re-start X (pressing CTRL + ALT + BACKSPACE worked
for me) and, opening a terminal, typing the following command:

    xrandr -o { left \| right \| inverted \| normal }

As you can see in the screenshot abaixo, my TabletPC’s screen was
rotated 90 degrees: |image0| The only issue I had was with the mouse (or
even the stylus pen) not re-associating its axis, what made it very
difficult to take this screebshot.Ã‚Â  |;)| Ã‚Â  I don’t know if there’s
a graphical interface for xrandr, but I am already salivating at the
possibilities for writing my own.

.. |image0| image:: http://static.flickr.com/55/165396895_6e1712b9a7.jpg
   :target: http://static.flickr.com/55/165396895_6e1712b9a7_o.png
.. |;)| image:: http://blog.ogmaciel.com/wp-includes/images/smilies/icon_wink.gif
