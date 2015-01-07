Nokia N800 Update and Tip #1
############################
:slug: nokia-n800-update-and-tip-1
:date: 2007-07-06 17:49
:category:
:tags: english

Today was announce the much antecipated release of the `Internet Tablet
OS 2007 edition <http://maemo.org/news/view/1183705330.html>`__, which
“includes Skype client support, AdobeÃ‚Â® FlashÃ‚Â® 9 browser plug-in,
improvements in online use times and single memory card support up to
8 GB. Also delightful new pre-installed content is available.”

Instructions on how to perform the update can be found
`here <http://maemo.org/community/wiki/howto_flashlatestnokiaimagewithlinux/>`__,
but lemme save you some time and give you a quick solution. First off,
download the `flasher-3.0 <http://maemo.org/downloads/d3.php,>`__ and
the `upgrade <http://tablets-dev.nokia.com/nokia_N800.php>`__ file (for
my N800 it is the RX-34\_2007SE\_4.2007.26-8\_PR\_COMBINED\_MR0\_ARM.bin
file).

**NOTE**: Now, the process of updating your device’s system (or flashing
it) **will** whipe out your user settings and installed applications.
**I recomend you make back ups of important files before proceeding.**

Turn off your device and plug it to a PC via an USB cable. Then, whip up
a console terminal and flash out your device’s system with the command:

    sudo ./flasher-3.0 -f -F
    RX-34\_2007SE\_4.2007.26-8\_PR\_COMBINED\_MR0\_ARM.bin -R

The following message will be displayed on the console:

    Suitable USB device not found, waiting

Don’t worry about it… just turn your device back on now and watch the
messages scroll. Once the process is finished, simply unplug your device
from the PC and turn it back on to see your new, shiny system. The -R in
the command above is supposed to reboot the device after the update, but
it only turned it off for me.

The nice little trick I learned today was how to enable root access in
your device without having to install the gainroot package. Once again,
turn it off and plug it to your PC. From the command terminal issue the
following command:

    sudo ./flasher-3.0 —enable-rd-mode

Turn the device back on and *voilÃƒÂ¡*! The next time your reboot,
you’ll see some text messages in green font appear on the screen. Then
install the Xterm package in your device and gain root access by issuing
the command:

    sudo gainroot

Thanks goes to **mgedmin** and **soothsayer** from #maemo for guiding me
through the flashing process and **etrunko** for several pointers,
including the root access tip!

There’s also a nice list of repositories for both N770 and
N800 \ `here <http://www.gronmayer.com/n800/repos/index.php?lang=en>`__!
