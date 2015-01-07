Moving WordPress Blog to Amazon's EC2
#####################################
:slug: moving-wordpress-blog-to-amazons-ec2
:date: 2011-02-16 03:26
:category: English
:tags: english

[caption id=”attachment\_1337” align=”alignleft” width=”500”
caption=”King Cloud”]\ |King Cloud|\ [/caption]

You probably remember `reading <http://www.ogmaciel.com/?p=1303>`__
about my issues with running my **WordPress**-based blog on
**Dreamhost**'s environment, and how frustrated I was with the
experience of using their **Private Server** services. The short version
is that I eventually migrated my blog back to their shared hosting
environment, turned off most of the plugins and cried myself to sleep.

The very next day, after reading (and replying to) the comments I
received, one in particular caught my eye: **Amazon’s Free Usage Tier**
offering new customers the following **EC2** services each month for one
year:

-  750 hours of EC2 running Linux/Unix Micro instance usage
-  750 hours of **Elastic Load Balancing** plus 15 GB data processing
-  10 GB of **Amazon Elastic Block Storage** (EBS) plus 1 million IOs,
   1 GB snapshot storage, 10,000 snapshot Get Requests and 1,000
   snapshot Put Requests
-  15 GB of bandwidth in and 15 GB of bandwidth out aggregated across
   all AWS service

Sounds really good, doesn’t it? I took a good look around and saw a
couple of interesting
`blog <http://www.agileweboperations.com/migrate-your-wordpress-blog-to-a-bitnami-ec2-instance>`__
`posts <http://blog.jayway.com/2009/05/07/blogging-among-the-clouds/>`__
from people who took advantage of this offer to move their blogs “to the
clouds”, and being the adventurous guys that I am, I signed up for a new
account and proceeded to take the steps to move this blog to my own EC2
instance.

The first thing was to create a back up/dump of my blog’s database and
WordPress files. I then started looking for a good Linux appliance with
all the necessary applications (i.e. **Apache, MySQL, PHP**, etc) as I
didn’t feel like starting with a plain “bare bones” system and
installing individual packages. I looked for a **CentOS**-based
appliance but as I couldn’t really tell how good some of the ones that
came up in my search were, I ended up choosing the WordPress stack from
`Bitnami <http://bitnami.org/>`__. This proved to be the path of least
resistance in the end as several people seem to have used it to do the
same exact thing I wanted to do (and the fact that it has an active
community also means I can have some level of support).

I highly recommend the instructions from this
`post <http://www.agileweboperations.com/migrate-your-wordpress-blog-to-a-bitnami-ec2-instance>`__
for the process of taking your database dump and using it to populate
your new database (make sure to either create a new user that matches
your existing configuration OR modify your wp-config.py to use the
default user from the instance), and configuring the Apache web server.
Do make sure to read everything, specially the sections related to a
couple of issues that came up for the author, so that you can hopefully
sidestep them. Also, as the appliance already comes with WordPress
installed in  /opt/bitnami/apps/wordpress/htdocs/, you may want to
selectively choose what files to copy from your backup into this
directory, such as themes, plugins, uploads, etc.

Finally, setting up my current domain to redirect to my EC2 instance was
extremely easy to do, using Dreamhost’s DNS services (you can use this
`example <http://manual.squarespace.com/domain-setup/domain-mapping-with-dreamhost.html>`__
up to step 6, skipping step 5) in conjunction with Amazon’s Elastic IPs.

Today marks the 7th day I switched this blog to my EC2 instance and so
far I have had absolutely no issues or regrets! I feel very confident
that I can expand its capabilities and not worry about bogging it down.
Load average has been around 0.15 and I also have plenty of free RAM to
go around. Once my one year promotion expires, bar any unexpected
surprises, I feel pretty confident that I may continue to use it as a
paid user.

.. |King Cloud| image:: http://www.ogmaciel.com/wp-content/uploads/2011/02/704056791_63f1e492d8.jpg
   :target: http://www.ogmaciel.com/wp-content/uploads/2011/02/704056791_63f1e492d8.jpg
