Wish list: Distutils best practice guide
########################################
:slug: wish-list-distutils-best-practice-guide
:date: 2010-03-26 19:22
:category: English
:tags: english

[caption id=”” align=”alignleft” width=”500” caption=”Prayers by
Xerones”]\ |Prayers by Xerones|\ [/caption]

When it comes to distributing source code, specially python code, I
really wish there was a concise and detailed best practice guide for
using `distutils <http://docs.python.org/distutils/>`__! Don’t get me
wrong, the documentation is pretty good and covers a lot of ground, but
what I really want is a standard “template” if you will, that python
developers can take and do some minimal modifications to customize it to
their needs.

For instance, and don’t ask me why as I don’t have a clue, Ubuntu seems
to insist that data files should go to /usr/local/share whereas other
distros expect them to live on /usr/share. It would be nice to have
specific examples on how to handle situations like this, as well as how
to properly handle gconf schema installation. This last one, as a matter
of fact, was the main reason why I switched from distutils was my
difficulty getting this to work 100%!

During my research I did come across a `Distutils
CookBook <http://wiki.python.org/moin/Distutils/Cookbook>`__, but the
few “\ **recipes**" don’t really show the whole picture. So in order to
really understand how to use them, it felt like one has to first learn
how to make **galantines served chaud-froid**!

.. |Prayers by Xerones| image:: http://farm1.static.flickr.com/15/19717875_99fde3f6db_d.jpg
   :target: http://www.flickr.com/photos/xerones/19717875/
