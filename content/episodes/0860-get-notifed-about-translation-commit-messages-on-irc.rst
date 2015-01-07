Get notifed about translation commit messages on IRC
####################################################
:slug: get-notifed-about-translation-commit-messages-on-irc
:date: 2008-10-26 15:35
:category:
:tags: english

A few years back I created the irc channel **#tradutores** (translators
in Brazilian Portuguese) on the Freenode server, a place where anyone
involved with the translation process of open source software could hang
out, chat, ask questions and share their experience with other fellow
translators. A place with no association to a given project or
distribution, where you could find people working for several groups
such as **GNOME, KDE, XFCE, Fedora, Foresight, Ubuntu**, all sharing the
same goal: improve the quality of open source translations for Brazilian
Portuguese!

One thing that I have always felt a need for was a notification system
for every time any given project had a commit related to Brazilian
Portuguese translation. In other words, is someone committed new
translations for **Amarok, Totem, Firefox**, or **Thunar** I wanted to
be notified. One day I found out about `CIA.vc <http://cia.vc/>`__, this
huge aggregator of open source commits for lack of a better description.
I imediately started using their services to follow commit messages for
a couple of projects such as GNOME (the entire project, which gives me
hundreds of messages on a daily basis) and even my pet project
`BillReminder <http://billreminder.gnulinuxbrasil.org>`__. Soon after I
added a bot to the channel **#billreminder** on Freenode to notify of
every commit to the project, and life was good! But it wasn’t until last
week that I read this `post <http://blog.hartwork.org/?p=160>`__ and
found about about a cool feature that I had not yet explored: filters!

After many hours trying to figure out how to write the proper filter, I
finally managed to create a new bot that would listen for commit
messages that contained the word “\ **Brazilian**" in the log message.
Why Brazilian? Because it is a common procedure to add the message
"**Updated Brazilian Portuguese**\ …” in the log messages, which gave me
a good way to filter out only the translations commit messages out of
the many generated every day.

|cia.cv bot for Brazilian Portuguese translations|

As you can see above, as soon as I committed my translations for the
**Dates** program, my bot **CIA-60** notified me of the event in the
channel. :)

If you are involved with translating open source projects into Brazilian
Portuguese, please stop by #tradutores on Freenode and introduce
yourself. I’d love to hear about your ideas.

.. |cia.cv bot for Brazilian Portuguese translations| image:: http://farm4.static.flickr.com/3008/2969952342_c040d0c790.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2969952342/
