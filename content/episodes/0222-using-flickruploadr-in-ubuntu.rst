Using FlickrUploadr in Ubuntu
#############################
:slug: using-flickruploadr-in-ubuntu
:date: 2006-01-19 16:28
:category:
:tags: english

Every time I need to add an image to one of my posts, I use a very
simple tool to upload it to my `Flickr <http://www.flickr.com>`__
account first. Once the image is uploaded, all there is left to do is
write the post and paste the corresponding URL from the Flickr site for
every image you want to publish together with your article. Even though
most tools out there used to perform this task were written for the
Windows plataform, I know of a few that were written for the Linux
community, such as `F-Spot <http://www.gnome.org/projects/f-spot/>`__
and `FlickrUploadr <http://micampe.it/things/flickruploadr>`__. F-Spot
is a great tool but somehow a bit too “heavy” for this very simple
procedure. `FlickUploadr <http://micampe.it/things/flickruploadr>`__ on
the other hand just feels right.

The first thing you need to do is download the source code for
FlickrUploadr
(`this <http://micampe.it/files/FlickrUploadr-0.6.0.tar.gz>`__ seems to
be the latest version) into your home directory. Since this application
requires certain python libraries that do not get installed during a
default Ubuntu Linux instalation, the next logical step is to install
the python2.4-dev package:

    sudo apt-get install python2.4-dev

**Instaling FlickrUploadr**

Now, assuming that you have opened and decompressed the source code into
your home directory and that your user name is godofredo (don’t ask me
why this name… hehehe), navigate via the console to the newly created
FlickrUploadr-0.6.0 folder and execute the instalation script:

    sudo python setup.py install

|Instaling FlickrUploadr|

Before you can say “Supercalifragilisticexpialidocious” the program will
be completely installed and ready to be used! You can now invoke
FlickrUploadr from the console with the following comand:

    Uploadr

But why use the console when you have a great windows manager like Gnome
installed and available??? What do you say we create a very simple
applet/shortcut to access FlickrUploadr from one of the Gnome bars?
Alright! Let’s go then:

**Creating the Applet**

Click with the right button of your mouse into the upper Gnome task bar
on your desktop e choose the option to add an applet. In the following
pop up window choose to create a custom launcher.

|Creating an Applet|

**Configuring the Applet**

The next step would be to provide the information about the program to
be launched through the applet:

|Configuring the Applet|

**Starting FlickrUploadr**

Once we’re done, we can start FlickrUplodr by clicking on the finished
applet:

|Starting FlickrUploadr|

**Configuring FlickrUploadr**

Now, drag and drop any image you want to upload into your Flickr account
into the small area of FlickrUploader and watch the “magic”!

|Configuring o FlickrUploadr|

**Parla!!!**

Depending on your internet conection speed, it should take a few seconds
(or minutes) for your image to be completely uploaded. You can then add
any other adicional comments or tags.

|Final product|

.. |Instaling FlickrUploadr| image:: http://static.flickr.com/9/86892308_18d9cfaf47.jpg
.. |Creating an Applet| image:: http://static.flickr.com/9/86893241_bceeb79664.jpg
.. |Configuring the Applet| image:: http://static.flickr.com/38/86893703_004dc82226.jpg
.. |Starting FlickrUploadr| image:: http://static.flickr.com/6/86894017_e1151b5e8a.jpg
.. |Configuring o FlickrUploadr| image:: http://static.flickr.com/43/86894925_dd89f8cad6.jpg
.. |Final product| image:: http://static.flickr.com/9/86895584_4208bfe476.jpg
