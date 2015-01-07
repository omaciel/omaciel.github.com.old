Pylyglot, Now With More Translations
####################################
:slug: pylyglot-now-with-more-translations
:date: 2010-10-08 01:38
:category:
:tags: english

[caption id=”attachment\_1210” align=”alignleft” width=”300” caption=”In
Every Language”]\ |In Every Language|\ [/caption]

What a difference a day makes! Thanks to some feedback I got both here
and in private, and thanks to a contributor with some extra free cycles
at hand, `Pylyglot <http://pylyglot.org>`__ got anotherÂ face
liftÂ today.

So what’s new? There are now **245 total packages and 3,165,335
translations** from yesterday’s **61 packages and 954,884
translations**! You can also now link to a query using the resulting url
from your searches using the format language=FOO&query=BAR, where
**FOO** is the language’s ISO code and **BAR** is the term you’re
searching.

Generating the data to fuel **Pylyglot** took approximately 2 hours and
a lot of CPU from my personal desktop, yielding a database dump file of
**451 MB**. I’m still investigating sponsorship opportunities and
partnerships to try to get a dedicated virtual server to handle the data
parsing process as well as host the site (and avoid having to use my own
desktop and scp the dump file up to **Dreamhost**).

What next? I still want to improve the search algorythm and return more
precise and reliable results. I also want to add packages from other
projects other than **GNOME** and make the data parsing process web
driven via the Django administrative interface. Finally, I want to
incorporate results from **Google’s** translation service so that you’ll
have more options to choose from.

There are some long term goals I want to tackle too but those will be
left for another blog post. In the meantime, please file issues,
requests, and perhaps some patches using the project’s **Github**
`page <http://github.com/omaciel/pylyglot>`__. Until my next update
then…

.. |In Every Language| image:: http://www.ogmaciel.com/wp-content/uploads/2010/10/2476125646_c16090b3bd-300x228.jpg
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/10/2476125646_c16090b3bd.jpg
