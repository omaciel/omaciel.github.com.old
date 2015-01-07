BillReminder "It Puts the Lotion in the Basket" 0.3 released
############################################################
:slug: billreminder-it-puts-the-lotion-in-the-basket-03-release
:date: 2008-03-02 17:32
:category:
:tags: english

|About BillReminder|

It is with a great pleasure that I announce the release of my pet
project `BillReminder <http://billreminder.gnulinuxbrasil.org/>`__! The
road to 0.3 has been a very educational journey for me, and looking back
when I first decided to port my original code written in C# to Python
just so that I could learn more about Python, I can say that I have
learned quite a bit. I have also met some fabulous people along the way,
some of them very responsible for me keeping the project going. I can
trully say that whenever I find the time to work on this project, I lose
track of time. Whenever I feel insecure about my own skills (or when
people make me feel that way) I take a look at what I have done so far…
it may not be the best piece of software out there, but it is mine…
written from scratch!

My plan was to release BillReminder on February 15th, in honor of my
second daughter Kate’s first birthday. But unfeortunately time wasn’t on
my side, as work and my personal life caught up to me. I want to
sincerely thank all of those who took the time to test it and send in
feedback and even patches! I want to specially thank my friend **Luiz
Armesto** for sticking around and sharing the same enthusiasm at
creating something from scratch and having fun while at it!

So what is new with this release? A lot actually:

This was a massive rewrite of the entire application, and instead of
listing all files that have been changd, I’ll try to highlight the most
important changes and features instead.

**GLADE:** BillReminder 0.3 was entirely re-written in order to remove
all glade files and dependencies. The initial idea was to simply get rid
of the dependency, but it also served as a learning process for me (and
I believe the other contributors will agree with this as well).
**DBUS:** The DBUS layer received a bit more love from Luiz Armesto,
breaking it down into the proper calls so to separate the ‘engine’ per
se from the client. **UI**: The user interface has also gone a series of
changes and (hopefully) improvements. It is probably not 100% HIG
compliant yet, but we’ll gladly accept suggestions. **Bug management**:
Towards the last 8 weeks of development we’ve adopted the habit of
filing bug reports prior to fixing the issues that we encountered during
the development cycle. **Translations:** All prior contributors promptly
replied to my email asking them to update their translations:

-  de.po: Sebastian Haselbeck
-  es.po: Gilberto J. Miralla
-  no\_NB.po: Tommy Mikkelsen
-  no.po: Tommy Mikkelsen
-  pt\_BR.po: FÃƒÂ¡bio Nogueira
-  sv.po: Daniel Nylander

You can download the source code for BillReminder
`here <https://sourceforge.net/project/showfiles.php?group_id=161428>`__,
as well as Ubuntu Hardy and Fedora 8 packages, courtesy of Luiz Armesto.
Foresight users playing with the newer alpha 4 can install it using
conary… Mandriva and Arch Linux packages should be coming your way soon
too!

Please send your constructive feedback, comments, and patches to us via
our `tracker <https://sourceforge.net/tracker/?group_id=161428>`__.

.. |About BillReminder| image:: http://farm4.static.flickr.com/3257/2304206451_22fe1e67ce_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2304206451/
