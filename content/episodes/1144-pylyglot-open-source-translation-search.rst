Pylyglot: Open Source Translation Search
########################################
:slug: pylyglot-open-source-translation-search
:date: 2012-08-17 15:04
:category: English
:tags: english, django, pylyglot, translations

It’s been a while since I wrote about
`Pylyglot <http://www.pylyglot.org>`__, my translation searching tool
that I use whenever I translate open source applications. Have not heard
about Pylyglot? Read the \ `About <http://pylyglot.org/about>`__ page
for more info!

The reasons for the long hiatus are too many to enumerate, but suffice
to say that the project is very much alive and I intend to keep updating
the translations database as often as possible.

So, what’s new? For starters, there’s a new and fancy language selector
that let’s you also search for a language as you type:

|Language selector|

There’s also support for pagination as searching for certain terms could
return quite a bit of results:

|Pagination|

Lastly, the translations are only a couple of weeks old and should be
updated again soon!

One thing that I removed was the ability to ask **Google Translate** to
provide the translation for a term. It is very unfortunately for I was
also working on a feature that would let you upload a translation file
(e.g. nautilus.po) and get back a fully translated file, where all
strings that were changed automatically were flagged as “fuzzy” by
default so that someone could then review the end result. But alas, due
to the somewhat recent changes to Google Translate policy, I decided
that it was not worth supporting this feature anymore.

Work and my personal life has kept me busy but I still intend to
maintain this project alive and hopefully turn it into something useful
for those who work on translations. There are a few things that I’d like
to do, such as update the code to be more **Django 1.4** “compliant” and
turn the process of updating translations more dynamic and “on demand”.
Unfortunately hosting Pylyglot on a shared **Dreamhost** environment and
using a “shotgun” approach doesn’t work well as they have some very
restrictive memory consumption threshold for individual processes.

Anyhow, feel free to `fork <https://github.com/omaciel/pylyglot>`__ the
code and send your suggestions (or pull requests). :)

.. |Language selector| image:: https://dl.dropbox.com/u/102224/selector.png
.. |Pagination| image:: https://dl.dropbox.com/u/102224/pagination.png
