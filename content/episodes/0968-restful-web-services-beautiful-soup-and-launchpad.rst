RESTful Web Services, Beautiful Soup and Launchpad
##################################################
:slug: restful-web-services-beautiful-soup-and-launchpad
:date: 2010-04-28 15:00
:category:
:tags: english

[caption id=”” align=”alignleft” width=”160” caption=”Pumpkin Black Bean
Soup by neon.mamacita”]\ |Pumpkin Black Bean Soup by
neon.mamacita|\ [/caption]

Last night I attended two short presentation by `Leonard
Richardson <http://www.crummy.com/>`__, author of the O’Reilly book
`RESTful Web Services <http://oreilly.com/catalog/9780596529260/>`__ and
developer on `Launchpad.net <http://launchpad.net/>`__. Unfortunately it
took me a while to find a parking spot near `UNC’s Chapman
Hall <http://www.hotline.unc.edu/index.cfm?fuseaction=classroom.classview&roomID=366>`__,
so I missed 90% of the first one, titled “\ **A Spotter’s Guide to
RESTful Web Services**\ ”. Based on the number of questions that were
asked at the end, it seemed to me that this is an area where there are
way too many possible ways people can get lost attempting to implement
it…

The next presentation, “\ **Six Years of BeautifulSoup**" hit a bit
closer for me, as I have been working on a side project that takes the
exported XML-like file from **WordPress** blogs and splits it into
smaller pieces to facilitate the import process. My main issue is that
I’ve been using **LXML** and it seems that when you use it to parse XML
files, it will convert some reserved HTML characters that are part of
any HTML tag present in the XML nodes into HTML entities. In other
words, any <, > and & in your HTML will be converted to &lt;, &gt;, etc.

Part of the presentation was spent with **Leonard** showing how
`Beautiful Soup <http://www.crummy.com/software/BeautifulSoup/>`__ is
being used by different projects, specially spammers and notorious
illegal arms dealers! Now, that is a claim that not all open source
projects can claim! :)

[caption id=”attachment\_988” align=”alignleft” width=”225”
caption=”Now, that is what I call a Beautiful Soup!”]\ |Now, that is
what I call a Beautiful Soup!|\ [/caption]

Interesting fact I did not know prior to last night’s presentation:
Leonard is the **creator and maintainer** of Beautiful Soup. So after
the second presentationÂ  was over and everyone had left, I was
introduced to Leonard by **Brad Crittenden** as “another Crazy
Brazilian” and had a chance to talk to him about my little problem. I
was glad to learn that, even though Beautiful Soup will convert HTML
reserved characters into HTML entities, you can easily turn this
behavior off, something I just could not figure out how to do with
LXML!Â  Nothing like having a chance to chat with the creator of a
project and hear him talking about his baby! :)

A big thanks to the folks from `TriZPUG <http://trizpug.org/>`__ for
putting yet another great presentation together! I can hardly wait for
the next one!

.. |Pumpkin Black Bean Soup by neon.mamacita| image:: http://bit.ly/9RA20B
   :target: http://www.flickr.com/photos/windompark/1748339802/
.. |Now, that is what I call a Beautiful Soup!| image:: http://www.ogmaciel.com/wp-content/uploads/2010/04/leonard-225x300.jpg
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/04/leonard.jpg
