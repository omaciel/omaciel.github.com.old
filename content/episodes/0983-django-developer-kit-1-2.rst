Django Developer Kit 1.2
########################
:slug: django-developer-kit-1-2
:date: 2010-05-18 09:00
:category:
:tags: english

[caption id=”attachment\_1038” align=”alignleft” width=”117”
caption=”Django”]\ |Django|\ [/caption] I’m really excited to announce
the release of my `Django Developer Kit
1.2 <http://www.rpath.org/web/project/djangodevkit>`__! Setting up a
Django-based project in the appliance is a piece of cake! Some of the
Django modules included are:

-  PIL=1.1.7-1-1
-  PyYAML=3.05-1-1
-  Pygments=1.3.1-1-1
-  bzr=2.0.0-1-1
-  bzrtools=2.0.1-1-1
-  cElementTree=1.0.5-1-1
-  coverage:source=3.3.1-2[]
-  django-ajax-selects:source=r24\_patched-2[]
-  django-authopenid:source=0.9.6-1[]
-  django-authority:source=0.4-1[]
-  django-cache-memcached=1.2-1-1[is: x86]
-  django-contact-form=r61-1-1[is: x86]
-  django-db-mysql=1.2-1-1
-  django-db-sqlite3=1.2-1-1[is: x86]
-  django-evolution=r165-1-1[is: x86]
-  django-favorites=b145949-1-1[is: x86]
-  django-filter=0.5.0-1-1[is: x86]
-  django-notification=0.1.5-1-1[is: x86]
-  django-pagination=1.0.5-1-1[is: x86]
-  django-piston=0.2.2-1-1[is: x86]
-  django-profile=r452-1-1[is: x86]
-  django-ratings=9e32d33-1-1[is: x86]
-  django-sorting=0.1-1-1[is: x86]
-  django-tagging=0.3.1-1-1[is: x86]
-  django-threadedcomments=ded46fc5bfd9a9d37a15-1-1[is: x86]
-  django-tinymce=r98-1-1[is: x86]
-  django=1.2-1-1[is: x86]
-  git=1.6.6.2-1-1[is: x86]
-  httplib2=0.4.0-1-1
-  ipython=0.10-1-1
-  mercurial=1.4.3-1-1
-  mod\_wsgi=3.2-1-1
-  mx=2.0.6-1-1
-  nginx=0.7.65-1-1
-  polib=0.5.1-1-1
-  psycopg2=2.2.0-1-1
-  pygooglechart=0.2.1-1-1
-  pysvn=1.7.0-2-1[~!bootstrap is: x86\_64]
-  python-cssutils=0.9.6a1-1-1
-  python-ctypes=1.0.2-2-1
-  python-feedparser=4.1-3-1
-  python-hashlib=20081119-1-1
-  python-markdown=2.0.3-2-1
-  python-memcached=1.45-1-1
-  scgi=1.14-1-1
-  south=0.7-1-1

There are several ways for you to play with the Django Developer Kit
appliance, so just head on down to the
`download <http://bit.ly/DjangoDevKit12>`__ page and pick from the
following image types:

-  x86 Amazon Machine Image (EC2)
-  x86 VMware (R) ESX Server Virtual Appliance
-  x86 VMware (R) ESX Server Virtual Appliance OVF 0.9
-  x86 VMware (R) ESX Server Virtual Appliance OVF 1.0
-  x86 VMware (R) Virtual Appliance
-  x86 Appliance Installable ISO
-  x86 Mountable Filesystem: Raw Filesystem Image
-  x86\_64 Amazon Machine Image (EC2)
-  x86\_64 Mountable Filesystem: Raw Filesystem Image
-  x86\_64 Appliance Installable ISO
-  x86\_64 VMware (R) Virtual Appliance
-  x86\_64 VMware (R) ESX Server Virtual Appliance
-  x86\_64 VMware (R) ESX Server Virtual Appliance OVF 0.9
-  x86\_64 VMware (R) ESX Server Virtual Appliance OVF 1.0

Once you’ve installed it (or launched it if using the **ESX**, **OVF**
or **Amazon Machine Image**), point your browser to the appliance’s IP
address plus port 8003 (i.e. xxx.xxx.xxx.xxx:8003, but this information
will be displayed in the console too), login as **admin** with the
default password of **password** and finish the wizard. You can then use
the **root password plugin** to set the password of the root user to ssh
into the box and start hacking.

[caption id=”” align=”aligncenter” width=”421” caption=”Django Dev Kit
appliance administrative interface”]\ |Django Dev Kit appliance
administrative interface|\ [/caption]

As always, comments and feedback are welcome!

.. |Django| image:: http://www.ogmaciel.com/wp-content/uploads/2010/05/djangologo.gif
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/05/djangologo.gif
.. |Django Dev Kit appliance administrative interface| image:: http://bit.ly/daSimg
