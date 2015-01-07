To the Transifex Appliance users out there
##########################################
:slug: to-the-transifex-appliance-users-out-there
:date: 2009-10-16 17:23
:category: English
:tags: english

Some time around the middle of **2008** I was asked if I would be
interested in joining the very young **QA** department for
`rPath <http://www.rpath.com>`__. I had already been working as a
software engineer for them since late 2006, spending a larger chunk of
my time working on a single project and not being able to experiment
with the cool technology we were developing outside of my project.
Somehow the idea of doing QA felt very appealing to me as I would then
be able to see, first hand, what type of products we were publishing, as
well as experience what our customers and users were going through. I
jumped on the opportunity and the rest is history.

Shortly after the initial conversion and learning curve factor from
going to thinking like a developer to thinking like a user were over, I
decided that the best thing for me to do was to start using our tools on
a daily basis. Not as I validated issues and tried to test use cases,
but as a user or customer. Eat our own dog food! I started looking
around for a good project to convert into an appliance, something that
would benefit from a dynamic versioned controlled system. So about 1
year ago (12 months and 6 days to be exact) I started a new project on
`rBuilder Online <https://www.rpath.org/>`__ called “\ `Transifex
appliance <https://www.rpath.org/ui/#/appliances?id=https://www.rpath.org/api/products/transifex>`__"
based on the `Transifex <http://www.transifex.org>`__ project.

What is the **Transifex** project, you may ask? From their web site:

    Transifex is a highly scalable localization platform with a focus on
    integrating well with the existing workflow of both translators and
    developers. It aims in making it dead-simple for content providers
    to receive quality translations from big translation communities, no
    matter where the project is hosted.

|Using Lotte to do online translations|

The **Transifex Appliance** is a self contained, all parts included with
just enough operating system based on the **rPath Linux** distribution
that allows you to get a full fledged **Transifex** installation ready
to be used! Several image formats are available, including an **EC2**
image that can be deployed on `**Amazon’s
AWS** <http://aws.amazon.com/>`__ clouds with a single click of a
button. It comes pre-populated with a couple of users and projects that
you can play with as well as with its own web based appliance management
interface so that you can manage system tasks such as taking a backup,
updating it, start or stop services, view system logs, among other
things.

|Transifex logs|

Early on I decided to maintain the appliance to work in synchrony with
the **Transifex** project itself, following the **development** (main)
code line and finding issues as the code was being developed, and
keeping a **stable** branch and updating it whenever a new released was
published. This has worked fairly well for the project as they can
identify issues right away and make sure they are handled before making
it available to the public. It has also served as an excellent means for
delivering quality software as the appliance itself is a pristine
environment with no “contamination” from external dependencies and
making sure that what gets developed is what you get!

During the course of working on this project I developed a very healthy
relationship with the developers and the fruits of this “investment”
have been returned to me (and I believe to the project as well) many
times fold! I have learned a lot about the tools we’re developing here
at work and have actually become a “perfect use case” for how our
customers use our tools! The appliance has been downloaded a few hundred
times in the last few weeks and this is what brought me to write this
post!

You see, early on I had to choose a database to use for the appliance
and the first thing that came to mind was the
`MySQL <http://www.mysql.com/>`__ database. Turns out that when the
**Transifex** project decided to launch a free web portal to showcase
their product in the shape of `Transifex.net <http://transifex.net>`__,
they chose to use `PostgreSQL <http://www.postgresql.org/>`__. I’m not
facing the situation where I also want to switch the appliance to use
postgreSQL but with so many downloaded images out in the wild, I wanted
to know from the users:

#. Would you mind the switch?
#. Would you want a migration script to move your data between
   databases?
#. Would you want this to be done automatically on update?

I really look forward to your feedback and please feel free to leave
your questions or suggestions in the comments section of my blog.

.. |Using Lotte to do online translations| image:: http://farm4.static.flickr.com/3514/3814640609_732eee28a4.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3814640609/
.. |Transifex logs| image:: http://farm3.static.flickr.com/2563/3816586880_eb81c56bc3.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3816586880/
