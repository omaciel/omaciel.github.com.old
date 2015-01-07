Announcing the Transifex Appliance
##################################
:slug: announcing-the-transifex-appliance
:date: 2009-05-20 17:11
:category:
:tags: english

Does your role within a project have you asking the following questions?

-  How do I provide an interface for translators to submit translations
   to multiple projects, regardless of the type of the underlying VCS?
-  How do I reduce the overhead a project maintainer usually undertakes
   to administrate accounts for translators?
-  How do I help translators do more by eliminating the need to
   subscribe to each VCS and learn its commands and tricks?
-  How do I encourage collaboration between developers and maintainers
   and thus, increase the language coverage of the participant projects?

Then boy, have I got some good news for you. I’d like to announce the
birth of the `Transifex
Appliance <http://www.rpath.org/project/transifex>`__! That’s right,
your own translation platformat your fingertips! Designed from the
ground up to serve as a bridge between source code repositories and
translators starving to flex their multilingual skills, it completely
obliterates all the initial administrative and infra structural needs
and allows you to just get it done!

Long gone are the days where you had to migrate your well established
source code to a different management provider in order to take
advantage of much needed features. It doesn’t matter where your code
lives, Transifex will allow your translators to reserve files for
translation and then submit them back via an intuitive web interface.
Better yet, configure your project to automatically commit these
translations from trusted translators and never have to worry about
synching work again! Get notified at every step during the translation
cycle and get up to the second access to statistical information and
find out who is doing what and when!

Sure you could just
`download <http://www.transifex.org/wiki/Download>`__ the source code
and manually install every single dependency, including setting up and
configuring a web server and a database, but why bother? Hit the ground
running with a software appliance!

|Transifex Appliance running on Amazon Machine Image (EC2)|

The `Transifex Appliance <http://www.rpath.org/project/transifex>`__ was
built using the amazing `rBuilder Online <http://www.rpath.org>`__ tool,
using a real `Lifecycle Management
Platform <http://www.rpath.com/corp/products/rpath-appliance-platform>`__,
which will allow me to maintain a development branch of the appliance
and make sure I can test every change happening in the development of
future releases of the `Transifex <http://www.transifex.org>`__ project
(think continuos testing and QA) while at the same time providing stable
updates by promoting well tested code to a release/stable label.

Do you feel like playing with the `Transifex
Appliance <http://www.rpath.org/project/transifex>`__ right now? Got
some spare machine sitting around? Maybe some type of virtualizaton
tool? Perhaps you have neither and still want to try it? I have provided
with the first release ISOs, VMware (R) and Amazon Machine Image (EC2)
for your delight. Just head down to the project’s
`page <http://www.rpath.org/project/transifex>`__ and take your pick.

This release is based on the **0.6** stable release of Transifex. A
couple of projects have already been created for you to play with. Log
in using either **guest/gues**\ t or **editor/editor** as your user name
and password combination and tinker to your heart’s content! Once the
appliance is up and running, you can either connect to the Transifex
instance by pointing your web browser to the appliance’s IP (i.e.
`http://xxx.xxx.xxx.xxx <http://xxx.xxx.xxx.xxx>`__) or manage it by
pointing your browser to that same IP but using the secure 8003 port
(i.e. `https://xxx.xxx.xxx.xxx:8003 <https://xxx.xxx.xxx.xxx:8003>`__)
and log in using admin/password as your credentials.

Also make sure to send all of your comments, suggestions, feature
requests, bug reports and kudos to the awesome Transifex crew, who have
more than once or twice (ok, a few times) taken the time to provide me
useful information and test drive this appliance!

.. |Transifex Appliance running on Amazon Machine Image (EC2)| image:: http://farm4.static.flickr.com/3542/3548073779_8c0759d8f8.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3548073779/
