My Own Personal Translation Portal in the Cloud
###############################################
:slug: my-own-personal-translation-portal-in-the-cloud
:date: 2009-12-04 21:43
:category: English
:tags: rpath

Had some time today during lunch to work on the `Transifex
Appliance <https://www.rpath.org/ui/#/appliances?id=https://www.rpath.org/api/products/transifex>`__
and decided to play with the **newly added feature of supporting
subversion over https**. So I launched the\ **devel EC2** instance on
`Amazon Web Service <http://aws.amazon.com/>`__ and proceeded to add
`PCMan File Manager <http://pcmanfm.sourceforge.net/>`__ so that I could
translate it online. Before you ask, yes: I do have commit access to the
project and could have checked out the code locally and done the work as
I usually do, but that’s not fun! Besides, being the good citizen that I
am, I felt like testing this new feature (**remember**: this is only
available on tip!) and providing some feedback.

After updating my appliance to run the latest code, I took a stab at
trying to add PCManFM as a project and see if I could then work on trunk
code. To make a long story short, the code did not play well with
subversion repositories with invalid ssl certificates, and it fell flat
on its face. A quick look at the Transifex log files via the appliance’s
administrative interface, I was able to ping **diegobz** on
**#transifex** and with a very subtle crack of a whip got him to look
into the problem.

|Checking the logs|

We then proceeded to test and validate some of the changes he made on
the spot, and once we got it right, I updated the appliance to use the
new code. From then on, it was a matter of creating the project:

|Adding the PCManFM project|

Add the proper information to pull code from trunk (I set the **Root**
attribute to
**`https://pcmanfm.svn.sourceforge.net/svnroot/pcmanfm/trunk/ <https://pcmanfm.svn.sourceforge.net/svnroot/pcmanfm/trunk/>`__**
by the way):

|Pull code from trunk|

Configure it for submission directly to the upstream project (I could
also have chosen to send it as a patch via email to the mantainer):

|Allow submission|

And start working on my translations using the handy dandy Lotte editor:

|Lotte online editor|

A few minutes later I was submitting away my translation and getting it
committed automatically to the upstream project! This is how
translations should be done by the way: working directly with the
upstream project. :)

The **only** time I had to **ssh into the appliance** and do manual
configuration changes was when I entered my subversion credentials for
`SourceForge <http://sf.net>`__ (that’s where PCManFM’s code is hosted)
into the **/usr/share/transifex/settings/80-vcs-extras.conf** file. I
added the following line and restarted the apache server:

    SVN\_CREDENTIALS = {‘sourceforge.net’:
    (‘\ **MY\_SF\_USER\_NAME**\ ’, ‘\ **MY\_PASSWORD**\ ’)}

Yeah, I shouldn’t have to ssh into the appliance but I have bugged the
Transifex guys about this and am trying to convince them to make this
part of the project configuration process… It’s only a matter of time
‘til they crack! :)

Anyhow, there’s some pretty cool new features scheduled to come out with
the next release, like granular commit access…

|Granular access control|

… so, if you want to play with the **latest Transifex code**, make sure
to download the `Transifex
Appliance <https://www.rpath.org/ui/#/appliances?id=https://www.rpath.org/api/products/transifex>`__
**Devel** images and always keep it up to date using the web based
administrative interface. If you’ve never used it, just point your
browser to the **appliance’s IP address** but make sure to use **https**
and add port **8003**! For instance,
`https://ec2-75-101-171-187.compute-1.amazonaws.com:8003 <https://ec2-75-101-171-187.compute-1.amazonaws.com:8003>`__
\*

-  don’t bother trying this url for it will be shutdown soon :)

As always, feel free to ask me anything related to the appliance, and
file issues and/or send your thank-you notes to the Transifex guys! :)

.. |Checking the logs| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/transifex_rpa.png
.. |Adding the PCManFM project| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/project-300x279.png
.. |Pull code from trunk| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/component-300x279.png
.. |Allow submission| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/component_submission-300x279.png
.. |Lotte online editor| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/lotte-300x279.png
.. |Granular access control| image:: http://www.ogmaciel.com/wp-content/uploads/2009/12/project_accesscontrol-300x279.png
