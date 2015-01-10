Bailout MT-Daapd Appliance
##########################
:slug: bailout-mt-daapd-appliance
:date: 2008-12-06 21:38
:category: English
:tags: rpath

For the past few days I’ve been working on setting up a minimalistic
music server for home. As I am always doing some crazy things to my
desktop/laptop that eventually leads me to re-install my operating
system, I find myself constantly moving music files between computers
and external media. When you have a decent sized music library, this
excercise starts to become a major pain. That’s how I came up with the
idea of creating a media server using mt-daapd as my tool of choice.
mt-daapd is so easy to use that I wasted no time and got started right
away.

The first step was to register a new product (think project) in
`rBuilder Online <http://www.rpath.org>`__. After spending less than 2
minutes thinking up a name I decided to call it
`Bailout <http://bailout.rpath.org>`__, as I needed something to bail me
out of my music sharing issues (though I’d like some of the bailout
money that our goverment is giving out these days).

The next step was to pick and choose what bits I wanted to add to my
appliance. since rBuilder allows you to start with Just Enough Operating
System (or JEOS for short) components, I proceeded to defining the
configuration of my product, choosing the rPath Linux 2 operating system
(other choices were Ubuntu Hardy and CentOS) and cherry picked some
other components I wanted to make available out of the box. They were
smb, nfs and openssh for some choices of connectivity, as well as vim
(hey, if I want to ssh into the box and do some manual tweaks I got to
have my favorite text editor). This is all done via the web interface in
rBuilder and up until now I basically clicked my way through.

Now it was time to add the main attraction of the show: mt-daapd. This
component was not available to me from the default software repository
and it was time for me to make some important decisions. rBuilder allows
you to package software via the web interface using RPMs, DEBs or binary
tarballs but I opted for trying out a brand new building tool called
rbuild (not to confuse with rBuilder) for those who like to tinker with
the command line and already know a bit about the conary package
management system. I will not go into details on how I packaged mt-daapd
using rbuild but I highly recommend the blog
`posts <http://blogs.conary.com/index.php/mkj/2008/08/29/simplifying_assumptions>`__
written by Michael Johnson for more details about this powerful tool.

Fast forward a few more minutes and my appliance was all ready to go. A
few more clicks and I kicked off the build of an installable ISO and a
VMWare image for this first “batch”. I could have chosen other formats
of delivering my appliance, such as Amazon EC2, Citrix, or Xen but I
still have time to go back and edit my product definitions later.

Once my 2 images were available, it was time to smoke test it. I chose
to burn a CD using the installable ISO image and used it to install the
Bailout appliance to an older computer I have under my desk. The
installer is anaconda-based and it is pretty trivial to follow. After
the (very quick) installation process and a quick reboot I was face to
face with a blank terminal console and instructions to log on to the
appliance’s management system by pointing a browser to a local IP
address. and so I did.

|Appliance Management|

If you decide to play with the Bailout appliance you’ll see in the
download section some instructions about the default credentials for the
web based management system, but for those who may have skipped reading
the text I put together, you should login using **admin** as your user
and **password** as your… err, password. Don’t worry, you’ll change this
in the very next step.

|Wizard: Setup a password|

The first time you login to the appliance, you’ll be prompted to set a
new password for the web management user’s account. Make sure you choose
something secure as this user is reponsible for the management and
maintenance of your appliance.

The next (optional) step is to set up how you’d like to be notified
about your appliance’s activities as well as about future updates. As I
want to be informed of updates for this appliance, I entered the
information necessary and proceeded with the wizard (hint: if you want
to skip this step, just click on the save button).

|Wizard: Setup a password for root|

Finally, pick a secure password for the root account of your appliance.
Needless to say, this is a very important step in the setup of any
GNU/Linux system.

|Landing page|

And that is it! Welcome to your your brand new appliance! The web based
management system has several options that will allow you to perform
many tasks on your appliance, such as updates, backups…

|Managing running services|

… manage services, configure the network…

|System Information|

… check the overall status and restore your system to a previous stage.

|MT-Daapd service web page|

Now you can point your browser to the same address of your web
management system, changing the port to 3689 and using
**admin**/**mt-daapd** as credentials to log in to the web management
page for mt-daap. You should also be able to see a new music share show
up in your media player of choice (assuming that the Bailout appliance
and the system where the media player is running are in the same
network).

|Banshee using a mt-daapd music share|

Right now the appliance is configured to use /mnt/mp3 as its media
folder and is not configured to scan it automatically, but this and
other settings can be changed by connecting to the appliance (ssh) and
manually tweaking the /etc/mt-daapd.conf file. Since the web management
system has a rich documented API and allows for the creation of custom
plugins, I will most likely create a plugin that will allow you to do
this from the web in the days to come. I also want to play with
`ushare <http://sourceforge.net/projects/ushare>`__ and uPnp to share
more than just music files and also allow for sharing with other devices
such as a XBox or a Nokia N810 tablet, but only time will tell when I’ll
get to it. Obviously, if you want to lend a helping hand, just get in
touch with me.

So go out and download a copy of the
`Bailout <http://bailout.rpath.org>`__ appliance today! So far is has
proven to be very useful to me!

.. |Appliance Management| image:: http://farm4.static.flickr.com/3227/3087612648_23a5164936.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087612648/
.. |Wizard: Setup a password| image:: http://farm4.static.flickr.com/3218/3086775491_bb6ee9acd6.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086775491/
.. |Wizard: Setup a password for root| image:: http://farm4.static.flickr.com/3228/3087612788_1e44136a71.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087612788/
.. |Landing page| image:: http://farm4.static.flickr.com/3050/3086776079_e03069c47b.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776079/
.. |Managing running services| image:: http://farm4.static.flickr.com/3198/3086776183_1b03d6363d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776183/
.. |System Information| image:: http://farm4.static.flickr.com/3033/3086776791_7100cd5479.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776791/
.. |MT-Daapd service web page| image:: http://farm4.static.flickr.com/3077/3087613296_2f78daff21.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087613296/
.. |Banshee using a mt-daapd music share| image:: http://farm4.static.flickr.com/3038/3086941341_6586e3754d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086941341/
