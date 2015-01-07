Transifex "Magneto" Appliance 0.8 is out!
#########################################
:slug: transifex-magneto-appliance-0-8-is-out
:date: 2010-03-03 03:52
:category:
:tags: english

Following the tradition of releasing simultaneously with the
`Transifex <http://transifex.org>`__ project, I’m pleased to present you
the `Transifex “Magneto” Appliance 0.8 <http://bit.ly/Transifex>`__!
There are just too many cool features to mention here… so I won’t! Just
go ahead and read the `release
notes <http://docs.transifex.org/releases/0.8.html>`__ instead.

+-------------------------------------------------------------------------------------------------------------------+
| |image1|                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------+
| From `Transifex v8.0 featutes <http://picasaweb.google.com/og.maciel/TransifexV80Featutes?feat=embedwebsite>`__   |
+-------------------------------------------------------------------------------------------------------------------+

As far as the appliance goes, the most important thing to know is that I
dropped **MySQL** and replaced it with **Postgresql**, so if you’re
thinking of updating an existing deployment, you’ll have to backup your
data and handle the restoration process. If you’re installing for the
first time, choose from the following image types:

-  Installable ISO (x86)
-  Installable ISO (x86\_64)
-  VMware (x86)
-  VMware (x86\_64)
-  Amazon EC2 Small (**ami-af8669c6**)
-  Amazon EC2 Large (**ami-b7a54ade**)

The appliance is pre-configured with 2 unique users: **editor** and
**guest** (with passwords **editor** and **guest** respectively) and
several projects for you to play!Â  To keep it up to date, log in to the
web based administrative interface by connecting to your appliances
**url** using **https** and adding port **8003** at the end. Then, login
as **admin** (the initial password is **password** but you’ll be
prompted to change it during the initial wizard). I can proudly say that
the Transifex Appliance has been downloaded several hundred times in the
last 2 months and is currently being used by several companies and
projects that are either test driving **Transifex** or decided to host
their own instance like the `Xfce <http://xfce.org>`__ project for their
`translations <https://translations.xfce.org/>`__!

As always the development branch of the appliance will follow the
development code line of **Transifex** and provide a playground for
anyone who wants to help out the project, such as the
`tasks <http://is.gd/9sGz3>`__ created ahead of the upcoming **Google
Summer of Code**. :) Download the appliance today and see why projects
such as **Meego**, **LXDE**, **Xfce**, **Fedora**, and many more chose
**Transifex** to manage their translations!

.. |image0| image:: http://lh3.ggpht.com/_9QQeITShNa0/S43G8AjZppI/AAAAAAACOrw/QqcR3LumhE8/s400/transifex0.8.png
   :target: http://picasaweb.google.com/lh/photo/PtSus-A20J79iTJtfgS_SQ?feat=embedwebsite
.. |image1| image:: http://lh3.ggpht.com/_9QQeITShNa0/S43G8AjZppI/AAAAAAACOrw/QqcR3LumhE8/s400/transifex0.8.png
   :target: http://picasaweb.google.com/lh/photo/PtSus-A20J79iTJtfgS_SQ?feat=embedwebsite
