Monoglotism in TurboGears...
############################
:slug: monoglotism-in-turbogears
:date: 2006-12-08 04:32
:category: English
:tags: rpath, turbogears, raa

or how the support for localization in `Turbo
Gears <http://www.turbogears.org/>`__ seems to be borked!

I have spent several hours trying to get a very simple Turbo Gears
sample application to “speak” a different language, with no success.
This is all part of my research at work to localize our `rPath Appliance
Agent <http://wiki.rpath.com/wiki/rPathApplianceAgent:Including_rAA_with_an_Appliance>`__
to other idioms.

The rPath Appliance Agent (rAA) is a framework for administering
appliances built with rPath technologies through a web based user
interface. Including rAA with an appliance enables a central point of
control for administration, configuration, and maintenance functions,
such as logging and email notifications, user account preferences, and
software updates.

rAA uses among other things Turbo Gears under the hood, and for my
“experiment” I started a fairly simple project by running:

tg-admin quickstart mytest

and accepted the defaults by hitting enter at every prompt. I then
proceeded to modify the default welcome.kid template by removing the
standard “you got Turbo Gears to run, hurray hurray” stuff and simplied
it to:

````

Hello World!
------------

Now, after bumping my head against the wall a couple of times, I learned
(the hard way, off course) that the command line is not your best friend
for generating po files right now. Instead, I opened a separate console
and started the toolbox kit with:

tg-admin toolbox -n

and pointed my browser to http://localhost:7654. From there, I chose the
admin18n option and was presented a pretty simple and concise
explanation of how to localize your Turbo Gears applications… or so it
looked. I clicked through the options for generating the po, adding a
language (pt\_BR and pt), translating the only string (offline, using
vim), and compiling the “language module.” The one thing I noticed right
away was that even though the pt\_BR folder and po was created, it would
not be displayed as an available language. Heck, it wasn’t even
available in the dropdown list! :P

Anyhow, I finished the experiment by adding “i18n.run\_template\_filter
= True” and “session\_filter.on = True” to my dev.cfg file, and even
added a “turbogears.i18n.set\_session\_locale(‘pt\_BR’)” to my
controler.py to force the language to Brazilian Portuguese, but nothing!
No matter what I do, my page will always display Hello World! in english
only! Does anyone have a clue???
