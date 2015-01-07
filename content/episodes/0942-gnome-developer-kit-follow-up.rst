GNOME Developer Kit, follow up
##############################
:slug: gnome-developer-kit-follow-up
:date: 2010-03-10 05:24
:category: English
:tags: english

Just wanted to update everyone who showed interest in the new release of
`GNOME Developer Kit <http://bit.ly;GNOMEDevKit>`__ I announced
yesterday. Based on some **preliminary statistics** I collected in the
(less than) last 24 hours, it seems that the **VMware** image type got
the most download, followed closely by the **installable ISO** format. I
guess that was due to **VirtualBox** being able to use \*.vmdk files and
some people opting for the free virtualization tool.

Here are the preliminary results so far:

#. VMware image: **42** downloads
#. Installable ISO: **26** downloads
#. RAW filesystem image: **17** downloads

[caption id=”attachment\_825” align=”aligncenter” width=”300”
caption=”About GNOME 2.29.92”]\ |About GNOME 2.29.92|\ [/caption]

Due to the number of downloads and and comments I received, I felt that
I should provide with some background on how to install/remove packages
and update your system using the conary package management system. So
here you go:

The package management system behind the `GNOME Developer
Kit <http://bit.ly;GNOMEDevKit>`__ is called
`conary <http://docs.rpath.com/conary/Conaryopedia/index.html>`__ and is
considered by many as the next generation package management system when
compared to some of the popular options out there. One of the reasons
behind this claim is the fact that your entire system is actually
completely maintained in a versioned state, and conary is always “aware”
of what is installed on your system and what files and dependencies make
up the entire “set”. This allows for some pretty nifty operations such
as rolling back to a specific state of your system.

In order to check for new updates for your system, open a terminal and
run the command **sudo conary updateall**. conary will then check for
updates and prompt you to accept the update or not. Please keep in mind
that the first time you run conary for the first time, you will
experience a delay as your entire system gets analyzed in preparation
for the changes that are to take place. All subsequent actions performed
will be much faster, I promise. If after a while you don’t feel like
waiting for the prompt, add **—no-interactive** to the update command to
have your system updated automatically.

Now, let’s just say that you decided to install something new, such as
**Banshee**. Easy, just run **sudo conary update banshee** (remember to
add —no-interactive for no-hands updates) and voilÃ¡!

Want to know what was actually installed on your system? **conary q
banshee** will tell you what version of banshee was installed. How about
what files were installed? **conary q —ls banshee** will give you a list
of all the files that were installed and **conary q —lsl banshee** will
give you the long list with file permissions and modes.

Changed your mind and want to remove banshee from your system? **sudo
conary erase banshee** will take care of that. Want to actually roll
your system back to the state it was before you installed banshee
instead? **sudo conary rollback 1** will rollback your system exactly
one transaction. Want to go further back? Just increase that number to
represent how many transactions to roll back. Want to rollback but don’t
remember what point in time you want to go? **sudo conary rblist** will
display a list of all transactions and what was changed. Note that each
transaction is preceded by the letter “\ **r**\ ”, so if you want to
rollback to the point **r.15**, then use **sudo conary rollback r.15**
(and don’t forget that “r” or you’ll rollback exactly 15 transactions
instead).

How about searching for a package? If it is something that it is already
installed on your system, then **conary q [package name]** will give you
the information you want. If the package is not installed on your system
yet, then **conary rq [package name]** is what you need, though since
conary does not yet make use of metadata, you’ll need to know the exact
name of what you’re looking for. Now, let’s say you want to find out
what package provides the command **/sbin/service**? Use **conary q
—path /sbin/service** to find out that
**initscripts:runtime=8.81.2-0.11-1** is responsible for providing it
(use rq if you want to search the remote repository).

Well, I think this is enough to get you going. You’ll probably want to
install Flash and media codecs to enjoy browsing some sites and
listening to your media, so let’s apply what we’ve learned so far and
run: sudo conary update flashplayer group-codecs

If you’ve stayed with me until now, you may want to read up on `what
else conary can
do <http://docs.rpath.com/conary/Conaryopedia/index.html>`__ or even
consider `packaging for GNOME Developer
Kit <http://wiki.foresightlinux.org/display/~jesse/Gnome+Developer+Kit>`__.
Your help will be greatly appreciated!

.. |About GNOME 2.29.92| image:: http://www.ogmaciel.com/wp-content/uploads/2010/03/Screenshot-300x187.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/03/Screenshot.png
