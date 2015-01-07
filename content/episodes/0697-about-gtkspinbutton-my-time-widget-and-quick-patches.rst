About gtk.SpinButton, my time widget and quick patches
######################################################
:slug: about-gtkspinbutton-my-time-widget-and-quick-patches
:date: 2008-01-06 04:59
:category:
:tags: english

Today I fixed issue **1864094** “\ `Time widget for individual alarms
are too
long <https://sourceforge.net/tracker/index.php?func=detail&aid=1864094&group_id=161428&atid=819795>`__\ ”.
I ended up creating a brand new widget with gtk.SpinButtons instead of
gtk.ComboBoxes, since we determined that it would be useful for a
different dialog. This took me a bit longer than I expected because I
insisted that the hours should be zero padded (i.e. display 01, 02 and
not 1, 2, etc). After spending some time on this I finally gave him and
asked `Johan
Dahlin <http://bugzilla.gnome.org/describeuser.cgi?login=johan%40gnome.org>`__
if it was possible, to which I received a negative answer. I proceeded
to code my widget only to receive the news several minutes later that a
`patch <http://bugzilla.gnome.org/show_bug.cgi?id=507566>`__ had already
been created and is now awaiting for someone to review. Is this awesome
or what?

|New Time widget|

I have also merged all the code being done in the 0.3 branch back into
trunk. So if you’re looking for the latest stuff:

    *svn co
    `https://billreminder.svn.sourceforge.net/svnroot/billreminder/trunk <https://billreminder.svn.sourceforge.net/svnroot/billreminder/trunk>`__
    billreminder*

**Luiz** today merged some code that should take care of localized
currency, so please test it!

About the upcoming **Foresight Summit**, there’s now a sign up
`page <http://wiki.foresightlinux.org/display/marketing/Foresight+User+and+Developer+Conference>`__.

.. |New Time widget| image:: http://farm3.static.flickr.com/2277/2171076332_6b0ce39878_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2171076332/
