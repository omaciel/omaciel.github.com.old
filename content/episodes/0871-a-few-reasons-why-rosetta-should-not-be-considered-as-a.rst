A few reasons why Rosetta should not be considered as a translation platform for existing open source projects
##############################################################################################################
:slug: a-few-reasons-why-rosetta-should-not-be-considered-as-a
:date: 2008-12-24 17:49
:category:
:tags: english

Last week I received an invitation to join the
`LXDE <http://lxde.org/>`__ project, “an extremely faster, performing
and energy saving desktop environment maintained by an international
community of developers”, to collaborate and help organize their
translation effort. As I have maintained the Brazilian Portuguese
translation for
`Openbox <http://icculus.org/openbox/index.php/Main_Page>`__, one of the
components that make up LXDE, and am very much involved with the
translation of GNOME, KDE, XFCE, and other modules, I felt very
compelled to accept the invitation.

One of the very first questions posed to the translation guys was which
tool/platform to use in order to empower collaborators and provide an
easy way to organize and maintain the translation effort. A
`poll <http://forum.lxde.org/viewtopic.php?f=12&t=163>`__ was set up
giving people 3 choices of platforms to vote on:

-  Launchpad’s `Rosetta <https://www.launchpad.net/rosetta>`__;
-  `Transifex <http://www.transifex.org/>`__ hosted at
   `fedorahosted.org <https://fedorahosted.org/transifex/>`__;
-  Transifex hosted at LXDE.org;

The initial result showed that Transifex was the favorite choice by the
majority, who also opted to have it hosted locally instead of taking
advantage of the instance already setup by the Fedora project. Those of
you who have followed my work from afar may be surprised to know that I
also voted for that same option, going as far as pointing out that
Launchpad’s Rosetta should not be considered for this enterprise. Those
of you who have followed my work more closely probably know that through
the years I have reduced my use of Rosetta to zero, choosing to do my
translations directly with the upstream projects instead.

I have been asked about my reasons for not supporting the same tool that
helped me get started in the open source world, most of which were
replied to via personal emails. I have also spoken to some close friends
about this same topic, who have encouraged me to write a blog post
exposing my position and maybe allow more people to learn how strongly I
feel against the use of Rosetta for existing open source projects.

**Disclaimer**

First of all, I want to make sure a few things are very clear so to
avoid confusion of my intentions. For a long time Rosetta was my tool of
choice and the one I recommended to anyone wanting to join the
translation hordes. The reason?

-  It was dead easy to use!
-  It bridged the (huge) gap between regular users and open source
   projects!
-  Being web based meant anyone could contribute from anywhere, using
   any OS, so long as you had internet connection (yeah, you could also
   download a PO file and work offline)!

For quite a while I was probably one of the most active Rosetta users
(at least that is what I was told by someone really close to Rosetta)
out there and a huge supporter. I still believe that the 3 points above
are very much valid today. Rosetta has a lot of potential and I whole
heartily believe that its developers are trying really hard to tighten
it up.

Now that I have added my disclaimer, let me explain what caused me to go
from being a great supporter to someone who doesn’t recommend it for
translating existing open source projects.

**Seeing the tree but not the forest**

A common work flow for someone using Rosetta is to search for modules
that need some work done (either missing translations or messages that
need to be reviewed) and then filter it to display only those messages
that need to be worked on. Great, right? Not quite! What if you were
translating the fictitious application “Mouse Trap”, a board game where
you move a cute little mouse through a maze to get to a pile of cheese,
and asked Rosetta to only display messages that had yet to be
translated?

Let’s just say that after filtering for the untranslated messages, you
are then presented with the string “\ **Mouse**\ ”.Â  Since the context
here is a board game with a little mouse, one could fairly easy be
tempted to translate **mouse** as the equivalent word in your language
that describes an actual mouse, a **rodent**. That was easy and once you
commit your work you’ll have a 100% translated game. However, what if
that specific message was located in the configuration dialog for this
game where the user can select how to control the mouse through the
maze? Since we’ve specifically filtered for untranslated messages only,
we missed the previous message that provided some useful messages
“\ **Please select how to control the character:**" and
"**Keyboard**\ ”, which were already translated. If you speak Brazilian
Portuguese you’d probably be confused with the choices to control the
game via a keyboard or an actual (the rodent) mouse, as there are 2
different words to differentiate between the animal from the pointing
device.

Obviously this is not a problem with Rosetta per se, as I believe that
in order to keep quality translations a team should always look at the
whole picture before committing their work. Unfortunately to Rosetta,
this feature has most definitely generated a lot of issues similar to
the one I’ve attempted to describe above. Before someone starts using it
to contribute with translations, instructions about the team’s work flow
and processes should be something that a new contributor gets as part of
their “welcome” package.

**RReedduunnddaaccyy**

Through the years it became apparent to me that there was a lot of
redundancy happening with the work being done by the translation teams.
Since most open source projects have their own translation teams, we
often had situations where (for instance) GNOME and Ubuntu Brazilian
Portuguese teams would work translating the same piece of software in
parallel. Because the GNOME team (from now on called upstream) already
had their own vocabulary and process in place, it was trivial for
someone to overwrite their work in Rosetta, something that
understandably ticked off many upstream translators. The Ubuntu
Brazilian team got such a bad rap for this that we would be immediately
spurned from IRC channels, or mailing lists related to upstream
projects. Heck, I was even called names by the Brazilian KDE / Latin
America representative (or whatever that asshole’s “title” is) just for
introducing my self and trying to start a collaborative relationship so
to avoid redundancy.

**Swimming against the flow**

The real problem in my opinion, and the reason why I believe Rosetta is
flawed from design, is that the work done by anyone using Rosetta will
only benefit Ubuntu and its derivatives. There is no two-way traffic
happening as far as translations goes, and **none** of the many
thousands (yes, **thousands**) of strings that I’ve translated during
the many hundreds of hours I spent translating with Rosetta ever made
its way back up to upstream, where other distributions could also use
them.

Everyone who’s worked with open source projects know that if you’re
going to make use of it, the least you can do is send any, if not all,
improvements made back to the source. It doesn’t necessarily mean that
your patch/work will be taken or incorporated but it is something a good
citizen from the open source world should do, specially a project like
Ubuntu that is so popular among the generic GNU/Linux user base!

**What to do then?**

I have many times attempted to provide more feedback and action plans to
improve these areas in Rosetta, even presenting during this year’s
FOSSCamp at Boston in February to a small group including Mark
Shuttleworth and `Troy
Unrau <http://troy-at-kde.livejournal.com/>`__\ representing the KDE
project. My last attempt was when I wrote this
`blueprint <https://blueprints.edge.launchpad.net/rosetta/+spec/translation-workflow-and-notification-system>`__
trying to detail a possible new translation workflow whereby quality
wouldn’t be sacrificed in favor of quantity and contributions done via
Rosetta would start to make their way back to the upstream projects.
Unfortunately nothing has ever come out of my attempts, which after a
while became less frequent from my part. I understand that the Rosetta
team is fairly shorthanded with the huge list of issues and features
pilling up on their queue, so it is not their fault that some of the
massive features can’t get implemented in the short term. But as I have
talked to many people during these last few months about this same
topic, I dare to ask:

Could the reason why Rosetta is still doing things backwards be more
aligned with how much return these features could fetch Canonical from
enterprise users?
