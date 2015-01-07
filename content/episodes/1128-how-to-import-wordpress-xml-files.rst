How to import WordPress XML files
#################################
:slug: how-to-import-wordpress-xml-files
:date: 2012-04-23 20:59
:category: English
:tags: english, wordpress, python, PyPi, Github, Tumblr

… or, how I brought an old python code back from the dead!

|image0|

Inspired by **Kenneth Reitz**'s recent
`post <http://kennethreitz.com/repository-structure-and-python.html>`__
and spurred by recent events, I decided to turn an old python code I
wrote a while back into something that can be (hopefully) easier to get
to than by sheer luck.

I’m talking about
`ChoppedPress <http://omaciel.github.com/choppedpress/>`__, my script
that let’s you split **WordPress** exported **XML files** into smaller
files that can be easily imported into new WordPress installations. I’m
sure that some of you have experienced the frustration of not being able
to import this xml file due to size upload constraints on your host
providers… One of my close friends who provides mostly support for
WordPress gave me the idea a while back and that is how the script came
about. Little did I know that
`other <http://snarfed.org/pyblosxom2wxr>`__
`people <http://blog.ivandemarino.me/2010/10/12/From-Wordpress-to-Bloggart>`__
have find it useful too, specially for migrating ***away*** from
WordPress! As a matter of fact, I too used it when I moved to
**Tumblr**, but that another story.

So this afternoon I took some time during my lunch break to create a
`repository <https://github.com/omaciel/choppedpress>`__ and put
together some very basic structure to give **ChoppedPress** a proper
`home <http://omaciel.github.com/choppedpress/>`__ (yay **GitHub
Pages**!!!). For the first time I also uploaded something I created to
`PyPi <http://pypi.python.org/pypi/choppedpress/0.0.1>`__\ … Sure, this
may not be a big deal to some of you out there, but I can hardly contain
my excitement. :)

Overall, I’m still enjoying a nice buzz from the experience. Obviously,
I look forward to comments, suggestions and/or improvements to the code,
but more than anything, I hope this will be useful to you too!

.. |image0| image:: http://media.tumblr.com/tumblr_m2y9r6Wdw31r7yex1.png
