Django Developer Kit 1.2 Release Candidate 1
############################################
:slug: django-developer-kit-1-2-release-candidate-1
:date: 2010-05-07 15:00
:category: English
:tags: rpath

|Django|

I’m really excited to announce the release of my `Django
Developer Kit <http://www.rpath.org/web/project/djangodevkit>`__ 1.2
RC1! The highlights for this release include the first **Release
Candidate** for the upcoming **Django 1.2**, as well as a switch of the
underlying platform, from **CentOS** to **rPath Linux 2**. All kinks
have been worked out and setting up a Django-based project in the
appliance is a piece of cake! Some of the Django modules included are:

-  django=r13117-1-1
-  django-ajax-selects=r24\_patched-2-1
-  django-authopenid=0.9.6-1-1
-  django-authority0.4-1-1
-  django-cache-memcached=r13117-1-1
-  django-contact-formr61-1-1
-  django-db-mysql=r13117-1-1
-  django-db-postgres=r13117-1-1
-  django-db-sqlite3=r13117-1-1
-  django-evolution=r165-1-1
-  django-favorites=b145949-1-1
-  django-filter=0.5.0-1-1
-  django-notification=0.1.5-1-1
-  django-pagination=1.0.5-1-1
-  django-piston=0.2.2-1-1
-  django-profile=r422-1-1
-  django-ratings=9e32d33-1-1
-  django-sorting=0.1-1-1
-  django-tagging=0.3.1-1-1
-  django-threadedcomments=0.5.2-1-1

There are several ways for you to play with the Django Developer Kit
appliance, so just head on down to the
`download <http://bit.ly/DjangoDevKitRC1>`__ page and pick from the
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

|Django Dev Kit appliance administrative interface|

As always, comments and feedback are welcome!

.. |Django| image:: http://www.ogmaciel.com/wp-content/uploads/2010/05/djangologo.gif
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/05/djangologo.gif
.. |Django Dev Kit appliance administrative interface| image:: http://bit.ly/daSimg
