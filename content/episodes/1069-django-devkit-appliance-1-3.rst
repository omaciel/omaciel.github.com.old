Django DevKit Appliance 1.3
###########################
:slug: django-devkit-appliance-1-3
:date: 2011-05-21 01:09
:category: English
:tags: english

[caption id=”attachment\_853” align=”alignleft” width=”300”
caption=”Django”]\ |Django logo|\ [/caption]

It’s been a while since I pimped my **Django Dev Kit Appliance**, mostly
because I have been really busy with work, projects and my kid’s end of
the school year. Anyhow, I rebuilt the appliance to use the latest
`Django 1.3
release <http://www.djangoproject.com/weblog/2011/mar/23/13/>`__ plus
several other updated packages such as git and mercurial. I have also
**stopped building Amazon EC2** images and will from now on only provide
**ISO**\ s and **Raw Filesystem** images.

Speaking of Raw Filesystem images, here’s how I currently use it  with
**QEMU**. In my .bashrc file I have an alias that will boot them and
redirect it’s internal ports **80** and **22** (apache and ssh) to my
system’s port **8080** and **2222** respectively. I also forward port
**3389** for Windows systems.

``sudo qemu-kvm -m 2048 -hda "$1" -boot c -soundhw ac97 -redir tcp:8080::80 -redir tcp:2222::22 -redir tcp:9999::3389``

So when I call my alias and pass a raw filesystem image as an argument,
I can then use localhost as the destination to my http and ssh
connections.

[caption id=”attachment\_1417” align=”aligncenter” width=”300”
caption=”Running under QEMU”]\ |Running under QEMU|\ [/caption]

I also have a special configuration in my .ssh/config file to make it
easier for me to ssh to these virtual systems and not have to change my
known\_hosts file every time I boot a different system and try to ssh to
localhost on port 2222:

``Host qemu User root Port 2222 Hostname localhost StrictHostKeyChecking no UserKnownHostsFile /dev/null``

If you want to play with this appliance, feel free to download it in the
following formats:

-  `Django DevKit Raw Filesystem
   x86 <http://downloads.ogmaciel.com/djangodevkit-1-x86.hdd.gz>`__
   (379 MB - SHA1: 7d643506a4787b095876c9d706701f60bbf5122e)
-  `Django DevKit Raw Filesystem
   x86\_64 <http://downloads.ogmaciel.com/djangodevkit-1-x86_64-disc1.iso>`__
   (521 MB - SHA1: f48298e72092e514b4204f5465313fe421dbc0f6)
-  `Django DevKit ISO
   x86 <http://downloads.ogmaciel.com/djangodevkit-1-x86-disc1.iso>`__
   (502 MB - SHA1: 1ab5d72513d724b976bd405bf6dbe31e6e1c8a5c)
-  `Django DevKit ISO
   x86\_64 <http://downloads.ogmaciel.com/djangodevkit-1-x86_64.hdd.gz>`__
   (392 MB - SHA1: 9a7ea35794b9773fc54cab387612ed9f38370407)

.. |Django logo| image:: http://www.ogmaciel.com/wp-content/uploads/2010/03/django-logo-negative-300x136.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/03/django-logo-negative.png
.. |Running under QEMU| image:: http://www.ogmaciel.com/wp-content/uploads/2011/05/Screenshot-QEMU-1-300x176.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2011/05/Screenshot-QEMU-1.png
