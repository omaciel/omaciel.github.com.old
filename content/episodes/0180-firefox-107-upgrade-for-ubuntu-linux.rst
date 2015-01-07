Firefox 1.0.7 Upgrade for Ubuntu Linux
######################################
:slug: firefox-107-upgrade-for-ubuntu-linux
:date: 2005-09-24 14:45
:category:
:tags: english

Yesterday a lot of people hanging out on #ubuntu @ FREENODE were
complaining of Firefox crashes in Ubuntu Linux after upgrading to the
latest 1.0.7 version. This will only happen if you’ve enabled Ubuntu
Backports in your apt-get setup. Luckly, Cyphase took the time to write
up a small
`HowTo <http://cyphase.homelinux.com/blog/2005/09/23/the-firefox-107-upgrade-in-ubuntu-hoary/>`__
that will help you fix this minor glitch. For the console-afficionado
out there just execute:

``sudo apt-get remove firefox firefox-gnome-support mozilla-firefox mozilla-firefox-gnome-support sudo apt-get install mozilla-firefox mozilla-firefox-gnome-support``

**Update:** I noticed that some people never actually checked the
original article and used the instructions above to fix their problem.
Well, it turns out that firefox was already running for some people and
the fix “didn’t work” for them… or did it? Yes… You have got to find the
ID for the firefox process that’s still running by using the following
code:

``sudo ps aux |grep firefox``

Then, kill the process with:

``sudo kill -9 [firefox ID]``

or, as `Cyphase <http://cyphase.homelinux.com>`__ suggested:

``killall firefox-bin firefox``
