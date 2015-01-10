Django Developer Kit Appliance: First Steps
###########################################
:slug: django-developer-kit-appliance-first-steps
:date: 2010-03-17 02:15
:category: English
:tags: rpath

I’ll make it quick so I can go back to watching TV:

Announcing my first attempt at a generic `Django Developer
Kit <http://bit.ly/DjangoDevKit>`__, a **CentOS** (powered by
`rPath <http://www.rpath.com>`__'s conary) based software appliance with
all you'd need to run a `Django <http://djangoproject.com/>`__ project.

[caption id=”attachment\_829” align=”aligncenter” width=”300”
caption=”Django Developer Kit Appliance”]\ |Django Developer
Kit|\ [/caption]

The current images are built on the development stage, which means it
includes the very latest `Django 1.2 code
line <http://code.djangoproject.com/>`__ straight from the subversion
repository. Currently, the following packages make up the base
appliance:

-  django
-  django-ajax-selects
-  django-authority
-  django-cache-memcached
-  django-contact-form
-  django-db-postgres
-  django-filter
-  django-notification
-  django-pagination
-  django-piston
-  django-profile
-  django-sorting
-  django-tagging
-  django-threadedcomments
-  file
-  gettext
-  httpd
-  less
-  mod\_python
-  mod\_ssl
-  mod\_wsgi
-  mx
-  openssh-clients
-  openssh-server
-  openssl
-  PIL
-  postgresql-server
-  psycopg2
-  python-ctypes
-  python-markdown
-  python-memcached
-  python-urlgrabber
-  PyYAML
-  scgi
-  sendmail
-  south
-  sqlite
-  sudo
-  tar
-  vim-enhanced

I’m still working out the kinks and have decided to not include
**openssl** by default until I have a generic way of generating a
certificate for the appliance. I will also be adding tools such as
**git**, **mercurial**, etc so that people can use the appliance as a
testing lab/environment for their own projects.

Once you’ve either installed the appliance or launched on **EC2** or
**ESX**, make sure to visit your appliance’s **htts://IP:8003** address
to configure the administrative interface (log in as **admin** with
**password** as your password). Then click the **Updates** plugin to get
updates as I will be making changes between now and the time I publish
this post.

`Download <http://www.rpath.org/web/project/djangodevkit/>`__ it today!

.. |Django Developer Kit| image:: http://www.ogmaciel.com/wp-content/uploads/2010/03/ddk01-300x169.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/03/ddk01.png
