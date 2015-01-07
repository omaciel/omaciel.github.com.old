Introducing PyLyglot
####################
:slug: introducing-pylyglot
:date: 2008-06-05 03:20
:category:
:tags: english

As everyone knows I’m very involved with the translation efforts of
several upstream projects and try to keep up with what’s going on with
every single one of them. Starting about 3 weeks ago I realized that I
relied too much on statistical information that wasn’t always up to date
and sometimes there would be a program that would get newer code
(sometimes resulting in changes to the translation strings) and go
unoticed. Since I was trying to get XFCE 100% translated, I decided to
write up a simple python script to help me keep an eye on those
packages… with every featured I added the script became more involved…
and `PyLyglot <http://code.google.com/p/pylyglot/>`__ was born.

Though I have added a simple UI as a proof of concept, PyLyglot is
mainly a command line utility that tells me exactly which packages on a
given repository needs attention, as well as which packages don’t yet
have translations.

|PyLyglot|

I have many ambitious plans for PyLyglot, getting it to work with other
applications to allow the translation of applications (i.e. poEdit,
gTranslator, or any text editor), integration with Open-Trans.eu and
Bugzilla, as well as a graphical interface that will let you cherry pick
which packages to follow, generate reports, and even commit (assuming
you have the correct permissions) your work back to the source
repository.

The code is still vey much tailored to my own usage and configurations,
but I can foresee a lot of changes that will abstract the repository
information out and turn it into a plugin-like framework, able to work
with other VCSs besides SVN. Why am I publishing this code? To get some
feedback, suggestions, help and patches… and with the hope that it will
be helpfull to other translators out there. Since this project is fairly
young, there’s room for anyone who’s seriously interested in lending a
hand.

.. |PyLyglot| image:: http://farm4.static.flickr.com/3255/2552910618_b5ec5ebe4a.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2552910618/
