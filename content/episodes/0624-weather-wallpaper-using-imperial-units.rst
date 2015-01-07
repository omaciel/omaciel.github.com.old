Weather Wallpaper using Imperial Units
######################################
:slug: weather-wallpaper-using-imperial-units
:date: 2007-08-29 03:18
:category:
:tags: english

Yesterday I heard/read from someone about this cool application that
would fetch weather information and convert it into a wallpaper that got
refreshed every so often. This program is called
`Weather-Wallpaper <http://mundogeek.net/weather-wallpaper/>`__!

Since we like cool and simple applications, we quickly packaged it for
`Foresight Linux <http://foresightlinux.org/>`__ but realized that the
weather information being displayed was using the metric system. Now,
without starting stupid arguments about the fact that the United States
uses the `imperial
system <http://en.wikipedia.org/wiki/Imperial_units>`__, I took upon
myself to add that feature to the still young code.

|weather-wallpaper|

Since this was written in python, it was pretty straight forward to make
the changes for a working prototype. The limitations at this point are
strictly limited to the limitations on
`PyMETAR <http://www.schwarzvogel.de/software-pymetar.shtml>`__, an
important part of this application… but this can be solved too! I’ve
sent my hack, errr… code to the author and if he accepts it, I may even
contribute to a configuration window and more! :)

.. |weather-wallpaper| image:: http://farm2.static.flickr.com/1178/1262810045_41811cd10d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/1262810045/
