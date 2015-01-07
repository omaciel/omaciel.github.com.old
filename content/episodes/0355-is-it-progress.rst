Is it progress?
###############
:slug: is-it-progress
:date: 2006-07-14 18:49
:category:
:tags: english

It has been roughly a week since I learned about the “new” repository
created by Canonical to distribute certain proprietary packages.Ã‚Â  I’m
refering to the *dapper-commercial*\ repository, which supposedly
contains packages such as skype, realplayer 10, w32codecs, and
opera.Ã‚Â  I say supposedly because I haven’t tried yet.Ã‚Â  Since I
manually downloaded and installed the .deb files for my w32codecs and
other needs, I didn’t feel the need to add the repository to my
list.Ã‚Â  Come to think of it, it was only after reading my good friend
`Thomaz Leite <http://blog.thomazleite.com/>`__'s blog (pt\_BR) entry
that I remember about it.Ã‚Â  I did manage to take a quick peak at the
repository from work but only saw opera and real player packages…

Anyhow, if you want to take advantage of this, simply add the following
line into your /etc/apt/sources:

    deb
    `http://archive.canonical.com/ubuntu <http://archive.canonical.com/ubuntu>`__
    dapper-commercial main

… followed by:

    sudo apt-get update

Now, you could install the Opera web browser for instance, using your
favorite package manager.

I can’t help but feel a bit of a (personal) conflict of interests with
this move.Ã‚Â  I particularly would prefer to invest in and support open
source alternatives instead…Ã‚Â  But I know how important it is these
days to be able to access media content and new tecnologies.Ã‚Â 
Canonical must know how important it is to maintain Ubuntu as an
attractive alternative for people shopping for an operating system.Ã‚Â 
With this new repository, anyone will be able to install skype without
having to worry if they have all appropriate dependencies or have
compiled a bunch of libraries that begin with the word lib\*… and this
is great!Ã‚Â  But in one hand, I can’t help but think that we’ll be
sabottaging any chance the ekigas e wengos would have against the skypes
out there!
