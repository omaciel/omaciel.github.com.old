Network Manager Tip
###################
:slug: network-manager-tip
:date: 2006-11-28 04:08
:category: English
:tags: english

The very first thing I do with a new laptop installation of Gnu/Linux is
to install Network Manager (sudo aptitude install
network-manager-gnome). Eventhough I have met people who have claimed to
hate it to death, I still consider it to be the best invention since the
invention of sliced bread!

However, something very peculiar happens if you install it after you’ve
already used your laptop to access a.. uhh… access point: the little
Network Manager applet won’t detect the wireless device!

The solution, though not very intuitive, is to edit the network
interfaces file and restart the program.

    sudo vim /etc/network/interfaces

Search for lines related to your wireless device and remove them as
shown below (my actual file):

    wireless-essid Mordor wireless-key theonetobindthemall

After you save the file, disable and re-enable the Network Manager
applet by right-clicking on it, and that is it! ;)
