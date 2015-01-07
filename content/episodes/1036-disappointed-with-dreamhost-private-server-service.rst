Disappointed With Dreamhost Private Server Service
##################################################
:slug: disappointed-with-dreamhost-private-server-service
:date: 2011-01-31 05:00
:category: English
:tags: english

[caption id=”attachment\_1304” align=”alignleft” width=”300”
caption=”Sad Face”]\ |Sad Face|\ [/caption]

This year I decided to do something I’ve wanted to do for a very long
time: get my own private Linux server! A place where I could have total
control (i.e. root access) and be able to install or run anything I
wanted! Better yet, I wanted a **conary** managed system that could
leverage all the packaging that I have already done for `Foresight
Linux <http://www.foresightlinux.org>`__ and be dead simple to maintain!

Ever since I started maintaining some type of a personal web site,
starting with my **AOL**'s members' pages and eventually “graduating” to
**Geocities**, it became obvious that sharing the resources of a single
server with who knows how many other people wasn’t going to cut it for
me. Early on there were too many restrictions imposed on anyone who
wanted to “color outside the lines” and today you still have to limit
yourself to a quota (disk, RAM, etc) somehow.

So during the short break I had for last year’s Christmas holidays, I
did a little bit of research looking for something that would be easy to
use and affordable. What I really wanted was to use my `Django Developer
Kit <https://www.rpath.org/ui/#/appliances?id=https://www.rpath.org/api/products/djangodevkit>`__
appliance on **EC2** but that was a bit out of my league at this
juncture. I also thought of using a physical box that I keep in the
closet and see if I could get someone to work out the DNS mapping for
me, but I didn’t really feel comfortable with the implications of asking
such a favor as the first thing people asked for was administrative
access to it too.

To make a long story short, I ended up going with
`Dreamhost <http://www.dreamhost.com/hosting-vps.html>`__ since that is
where all of my web sites are currently hosted. At USD $15/month for
300MB I felt that I should be able to host two of my most visited web
sites and an **irssi** screen session without breaking a sweat. A few
clicks later I was set up!

The first week with my private server was sheer bliss, specially because
Dreamhost gives you **2300 MB** of RAM free of charge for the first week
so that you can gauge what your needs are. This blog right here, after
migrated, went from choking and giving me 500s  whenever I enabled the
**WordPress Stats** plugin to being super snappy! The other site was
also enjoying solid stability and after 2 weeks of use and studying my
resource consumption patterns, I felt I had made a good choice after
all.

That feeling didn’t last long, however. After about 10 days of using my
private server, I realized that both of my sites were down. SSHing to it
showed me that the Apache server had gone down. I quickly got online
with Dreamhost’s support techs and was told that my problem was due to a
run away process that used all of my 300MB and brought the web server
crashing down.

That was pretty disappointing and though I’m not completely ignorant on
how to check system logs I thought that it was pretty safe to believe
the technician. The next few days I experienced slowness to my irssi
session and even a few 500s started creeping up on me. Reluctantly I
turned off the Stats plugin and managed to make the problem go away.

A few days later I completely lost connection to my system. No SSH
either! The technician was once again summoned and for the next 45
minutes we went back and forth between having connection/access to
seeing my system crash and burn before my own eyes. Now, the technician
was very polite and responsive (as all Dreamhost technicians I’ve dealt
with are) but I just couldn’t get a straight answer as to what was
causing my system to die, even after several reboots.

I decided to humor him and followed his suggestion of moving one of my
sites **back** to the shared environment, only to see the private server
crash again! “Move the second site back too”, he suggested. By this time
I was pretty frustrated with the whole thing and didn’t feel like having
a discussion about how silly this trial and error was. “Go read our wiki
and figure out how to lower your memory consumption”, he offered, to
which I replied: “My systems run ok in the shared server, so it doesn’t
make any sense to me why it would choke when it has 300MB of dedicated
memory. Besides, I’m the customer here and am asking you to help me.”

In the end, even by moving my second site back to the shared environment
and killing my irssi session, the server would still go down. WTH,
right? So my sad story ends with me cancelling my Private Server and
going back to my shared environment. As I’m no system administrator and
my experience dealing with faulty systems revolve around my day-to-day
maintenance of my personal systems, I never really learned what the
problem was. I expected Dreamhost to provide me with solid information
but was sorely disappointed at their lack of commitment to help me
understand what was wrong. You see, I was ready to accept that, for
whatever reason, 300MB wasn’t enough for my needs. But being told to go
read a wiki page and figure things out on my own was a major let down
for me.

.. |Sad Face| image:: http://www.ogmaciel.com/wp-content/uploads/2011/01/259997124_0523ad0ce8-300x225.jpg
   :target: http://www.ogmaciel.com/wp-content/uploads/2011/01/259997124_0523ad0ce8.jpg
