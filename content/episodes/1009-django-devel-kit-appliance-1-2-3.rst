Django Devel Kit Appliance 1.2.3
################################
:slug: django-devel-kit-appliance-1-2-3
:date: 2010-09-11 19:24
:category:
:tags: english

[caption id=”attachment\_1191” align=”alignleft” width=”300”
caption=”Oops!”]\ |Oops!|\ [/caption]

No, this is not a repeat from yesterday’s post. Turns out there was
another `security
release <http://www.djangoproject.com/weblog/2010/sep/10/123/>`__ for
**Django** yesterday (thanks **Zygmunt** for the heads up), so here’s
the release of ï»¿\ `Django Developer Kit Appliance
1.2.3 <http://bit.ly/byzBLV>`__.

As always, choose from the following image types:

-  Amazon EC2 AMI Large (**ami-ba996cd3**)
-  Amazon EC2 AMI Small (**ami-a0996cc9**)
-  `ISO
   x86 <https://www.rpath.org/downloadImage?fileId=42099&urlType=0>`__
   (SHA1 11811571ee8f8f2a0d7778c9e4275060de73f271)
-  `ISO
   x86\_64 <https://www.rpath.org/downloadImage?fileId=42109&urlType=0>`__
   (SHA1 065b1c5dfa410cffeec9950d577cddd15f369bad)
-  `Raw Filesystem
   x86 <https://www.rpath.org/downloadImage?fileId=42102&urlType=0>`__
   (SHA1 141427d7c84449ccc7eacbee7d527b8ba6f7ca48)
-  `Raw Filesystem
   x86\_64 <https://www.rpath.org/downloadImage?fileId=42105&urlType=0>`__
   (SHA1 482ecbbd2c177e3fdc33b18dc0ee65c83d681956)
-  `VMware ESX
   x86 <https://www.rpath.org/downloadImage?fileId=42106&urlType=0>`__
   (SHA1 10757fd1f0ec119fe236f3402bf38dfde25cb40a)
-  `VMware ESX x86 OVF
   1.0 <https://www.rpath.org/downloadImage?fileId=42108&urlType=0>`__
   (SHA1 7c535f1514a969118f08f4bdf9c9559b492c72d6)
-  `VMware ESX
   x86\_64 <https://www.rpath.org/downloadImage?fileId=42114&urlType=0>`__
   (SHA1 a710d469e74124f2988591362b6943cee9589e46)
-  `VMware ESX x86\_64 OVF
   1.0 <https://www.rpath.org/downloadImage?fileId=42116&urlType=0>`__
   (SHA1 c7a11c380f2d5e0cfc96220cbfe81a88876eb201)
-  `VMware Desktop
   x86 <https://www.rpath.org/downloadImage?fileId=42104&urlType=0>`__
   (SHA1 29eb739b88d90a172815c2274aafb0b1ffe4228a)
-  `VMware Desktop
   x86\_64 <https://www.rpath.org/downloadImage?fileId=42113&urlType=0>`__
   (SHA1 f3ba1c95fc04260bf60ad3fef8552eda6be5f12d)

Remember that the appliance comes with its own management system that
can be accessed by pointing your browser to
**https://YOUR-APPLIANCE-IP:8003** and logging in as the **admin** user
(the default password the first time you boot your appliance is
**password**, but you will immediately be asked to change it during the
1-step setup wizard). From there you can also **configure backups**,
**updates**, and **manage system services**.

If you are already running the appliance, then you can update it to get
the latest code. Just use the **Update** plugin in the web based
management system or run **conary updateall** from the command line as
the **superuser**.

.. |Oops!| image:: http://www.ogmaciel.com/wp-content/uploads/2010/09/508647245_178fc7941d-300x199.jpg
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/09/508647245_178fc7941d.jpg
