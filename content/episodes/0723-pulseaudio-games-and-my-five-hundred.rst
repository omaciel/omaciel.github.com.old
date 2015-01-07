PulseAudio + Games and My Five Hundred
######################################
:slug: pulseaudio-games-and-my-five-hundred
:date: 2008-02-24 19:31
:category:
:tags: english

Been using `PulseAudio <http://www.pulseaudio.org>`__ for several months
now and was extremelly happy with the end result. The ability of
controlling the volume for specific applications alone made it very
worth the change. But there was one little issue that bothered me a lot:
not being able to play my games with support for audio! Back when I
started searching for a solution, I didn’t find anything that would
resolve this issue and I eventually accepted that as a fact.

Today I came across
`this <http://www.pulseaudio.org/wiki/PerfectSetup#SDL>`__ awesome
source of information (it was most likely under my nose for quite some
time) for those with the same scenario and I can now confirm that it
works!

I can now run **Enemy Territory** by simply exporting the following
environment variable:

    export SDL\_AUDIODRIVER=esd et

And **World of Padman**:

    padsp WoP

Life is good now!

On a different subject, there’s been a lot of talk about the number five
these days, but nobody has mentioned that you do not need to be a hacker
to participate. Nobody mentioned that you can also help out by
translating open source software! The only difference is that we usually
work on a much higher scale… So for those of us working on translations,
what is your **500**? :)

***My 500**:
`518005 <http://bugzilla.gnome.org/show_bug.cgi?id=518005>`__ -
`518006 <http://bugzilla.gnome.org/show_bug.cgi?id=518006>`__ -
`518007 <http://bugzilla.gnome.org/show_bug.cgi?id=518007>`__ -
`518008 <http://bugzilla.gnome.org/show_bug.cgi?id=518008>`__*
