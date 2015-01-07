Getting Jiggy With Translations
###############################
:slug: getting-jiggy-with-translations
:date: 2006-07-29 13:25
:category:
:tags: english

This past weekend the `Ubuntu Brazilian Portuguese
Translators <https://launchpad.net/people/ubuntu-l10n-pt-br>`__ and the
`Brazilian Documentation
Team <http://wiki.ubuntubrasil.org/TimeDeDocumentacao>`__ put together a
3-day **boot camp** for translators and new volunteers. The online
classes were held every evening at #ubuntu-br-tradutores, and covered
all the steps and methods involved in the process of translating Ubuntu
to Brazilian Portuguese, as well as showing people how they can
participate in the community.. The very last session, taught by
**CÃƒÂ¡ssio Martini** (and me in the back stage), was performed with
live demos and participation of the “students” in real time. I can say,
without false modesty, that it was a great way to close the event! I
wrote this article (originally in portuguese) approximately 30 minutes
prior to the session started, so to serve as a guideline that people
could follow online. It is assumed that the reader has already
subscrived to our `mailing
list <http://listas.ubuntubrasil.org/mailman/listinfo/tradutores>`__,
criated a GnuPG `key <http://wiki.ubuntubrasil.org/GnuPG>`__,
`signed <http://wiki.ubuntubrasil.org/AssinarCodigoDeConduta>`__ the
`Code of Conduct <http://wiki.ubuntubrasil.org/CodigoDeConduta>`__, and
also registered for a free “account” with the
`Launchpad <https://launchpad.net/>`__ system. All of these topics were
(extremelly well) covered in the first 2 sessions by my friend **Alex
Rocha**. We urge all volunteers interested in joining our team to read
this `document <http://wiki.ubuntubrasil.org/l10n>`__, which gives a
brief introduction about the different systems we currently use, as well
as some great `tips <http://wiki.ubuntubrasil.org/l10n/BoasPraticas>`__
for when translating packages.

The first step would be to visit our
`page <http://wiki.ubuntubrasil.org/EdgyPacotes>`__ with a list of all
the programs/packages that still need to be translated, kept in order
and closely mantained by my good friend `AndrÃƒÂ©
Noel <http://drenoel.wordpress.com/>`__. This is without a doubt the
most important page for any member of the `Ubuntu Brazilian Portuguese
Translators <https://launchpad.net/people/ubuntu-l10n-pt-br>`__ team,
whom not only are responsible for their own tasks but must always
refvise every suggestion sent by our volunteers! The main difeerence
between an official member and a volunteer, besides the ones already
mentioned, is that translation suggestions done by a member
are\ **automatically**\ accepted by Rosetta, while the suggestions sent
by the volunteers must be accepted (or rejected) by a member. Since
Rosetta at its current version does not have a means for a member to see
which packages have received new suggestions, sometimes they
(suggestions) will sit tight for quite some time until a member, per
chance, decides to browse the specific package. This can be very
frustrating, and some people have told me this was one of the reasons
why they gave up before. That is why I developed the “system” show
below, where we have been very successfull tracking modifications and
getting volunteers and members to work closer together.

|image0|

Since this page is part of a wiki, anyone with a valid (FREE) account
has the capability to modify it. As you can see, though it is written in
portuguese, the table keeps track of the package name, total numbers of
strings, percent translated, translator, and revisor.. Here’s how the
system works:

#. The individual interested in translating a package (program) modifies
   this page, adding his name (as registered in the wiki) in the
   **Tradutor** (translator) column. Assuming that user Daffy Duck
   registers himself in the wiki as **Daffy** and is interested in
   translating the **atlantik** package, he would add **Daffy** in the
   **Tradutor**\ column.
#. Now, he would add the name of one of the offical members from our
   team in the **Revisor** column. For this example, Daffy Duck would
   add the official member **Bugs Bunny** as his **Revisor**.
#. Lastly, save the page.

Since all of our members must check this page **every single day** to
see if there are any packages in need of revision, nothing else needs to
be done by a volunteer. It would be better if a volunteer contacts his
revisor in order to determine his availability. Since we are all
volunteers ourselves, it is not garanteed that any given member will be
available that same day. Believe me, this could avoid any delay in
gettings your suggestions approved. A semi-complete list of all members
can be see below. For an up to date list, as well as emails of all
members, visite our pagge in Launchpad.

|image1|

Now, we’re ready to start translating! First, we should
`login <https://launchpad.net/+login>`__ to Launchpad: |image2|

Fill out the appropriate fields with your email and password. Note that
this page can also be used to register a new account.

|image3|

After you’ve connected, you can browse the main
`page <https://launchpad.net/distros/ubuntu/dapper/+lang/pt_BR/+index?start=0&batch=2000>`__
which contains a complete list of all packages being translated by our
team.

|image4|

For this article, we’ll assume that Daffy Duck decided to translate the
package
`textinfo <https://launchpad.net/distros/ubuntu/dapper/+source/tetex-bin/+pots/textinfo/pt_BR/+translate>`__:

|image5|

As you can see below, the interface contains, among other things, the
messages that need to be translated in english, and a text box below it
where you can type in your suggestion. Note below that messages 1 and 2
have already been translated. But let’s just assume that Daffy does not
agree with the translation of the word “character”, and wishes to change
it from “caracter” to the correct translation of “caractere”. For those
who don’t speak the language, the difference is very minor. Well, all
Daffy needs to do is overwrite the message that is currently in the text
field, adding his own suggestion. Rosetta is “smart” enough to
“distinguish” between suggestions (from a volunteer) and a translation
(from a member).Ã‚Â  Since Daffy is a volunteer, his suggestion will be
stored so that a member can later approve it or reject it. |image6|

There’s also a filtering system built-in which allows you to select
**untranslated** messages, those that **need revision**, **translated**,
or **all**. To apply a filter, make your selection from the drop-down
box and click the **Filter** button. Unfortunately, the option “Someone
should review this translation” can only be used by members to alert
others of dubious translations.Ã‚Â  Volunteers are urged to send their
notifications via email.

|image7|

Assuming Daffy chose the “untranslated” filter, he would then get the
messages dispplayed above.Ã‚Â  It is very important to point out that
you do **not** have to translate all messages in order.Ã‚Â  We recommend
that you send only suggestions to those strings you feel confortable
translating.Ã‚Â  Note that you can always use the links Ã‚Â« First
Ã¢â‚¬â€? Previous Ã¢â‚¬â€? Next Ã¢â‚¬â€? Last Ã‚Â» to navigate your way
around the pages, specially if you decide to skip any given page.Ã‚Â 
Once you’re done, don’t forget to click on the **Save & Continue**
button.

|image8|

Well, thid is pretty much the process we use for our translations! Once
again I hope this will help other people interested in either helping us
or some other translation effort.Ã‚Â  I have to thank `Luciano
Pacheco <http://lucmult.blogspot.com/>`__, source of the inspiration for
this article! :)

.. |image0| image:: http://static.flickr.com/73/195665080_d86cbb0d5c.jpg
.. |image1| image:: http://static.flickr.com/72/195137463_7475bea0ff.jpg
.. |image2| image:: http://static.flickr.com/75/195136755_5513a7a407.jpg
.. |image3| image:: http://static.flickr.com/66/195136756_72f5672c99.jpg
.. |image4| image:: http://static.flickr.com/73/195136757_adae63dd40.jpg
.. |image5| image:: http://static.flickr.com/61/195136758_5a87eee492.jpg
.. |image6| image:: http://static.flickr.com/76/195137461_472c9abbcb.jpg
.. |image7| image:: http://static.flickr.com/73/195697205_56af3e1ac8.jpg
.. |image8| image:: http://static.flickr.com/76/195136759_d9bdb1c908.jpg
