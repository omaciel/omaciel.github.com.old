FauxFactory 0.2.1
#################
:date:   2014-05-09 17:00:00
:category: English
:tags: python, testing, qe

.. figure:: https://farm4.staticflickr.com/3373/3204502310_f8025dbd75_m.jpg
   :alt: paper bag release

Short on its heels, today I'm releasing **FauxFactory 0.2.1** to fix a
`brown paper bag
bug <http://catb.org/jargon/html/B/brown-paper-bag-bug.html>`__ I
encountered last night before going to bed.

Basically, the new "Lorem Ipsum" generator was not honoring the
**words** parameter if you asked for a string longer than 70 characters.
I have fixed the issue as well as added a new test to make sure that the
generator does the right thing.

The package is available on
`Pypi <https://pypi.python.org/pypi/fauxfactory/0.2.0>`__ (sadly the
page is **still** not rendering correctly... suggestions welcome) and
can be installed via **pip install fauxfactory**.

If you have any constructive feedback, suggestions, or file a bug report
or feature request, please use the
`Github <https://github.com/omaciel/fauxfactory>`__ page.

*Image: **Cry** by `LLewleyn Williams a.k.a.
SCUD <https://secure.flickr.com/photos/privatenobby/>`__, some rights
reserved*.
