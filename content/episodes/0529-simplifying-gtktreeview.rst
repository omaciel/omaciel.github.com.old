Simplifying gtk.TreeView?
#########################
:slug: simplifying-gtktreeview
:date: 2007-04-12 02:12
:category:
:tags: english

One of these days I was working on a new graphical interface for a new
application in python, when I noticed something familiar. Every time I
need to add a gtk.TreeView widget to one of my programs, I end up
re-writing the same code, over and over again and again… so I thought:

"Why not create my own kit/widget and stop rehashing code?"

Since I had a pretty uneventfull Saturday, I ended up creating
**GenericList**, my own abstraction of a generic grk.TreeView.

|A very generic gtk.TreeView base class|

Now, every time I need to add a list to one of my programs, all I have
to do is instantiate this class, “feeding” it only the layout of the
columns I need. Or, subclass it:

|Subclassing the generic list|

The code for the subclass is all here (above)… Inside my code I
instantiate it and then I can add, remove, etc records/rows simply
calling the generic methods add(), remove(), etc, etc, as shown below:

    from billlistview import BillListView as ListView self.list =
    ListView() pixbuf = gtk.gdk.pixbuf\_new\_from\_file(‘coin.jpg’) list
    = [[pixbuf, ‘Verizon’, ‘$ 49,00’, ‘04/27/2007’], [pixbuf,
    ‘T-Mobile’, ‘$ 55,99’, ‘04/15/2007’], [pixbuf, ‘Cable’, ‘$ 111,99’,
    ‘04/15/2007’]] self.list.addList(list)

|A little test application|

Obiously, I could not finish this post without a screenshot of the
exemplo above in execution.

|A sample demo|

I still want to add a few more methods before adding it to
`BillReminder <http://billreminder.sourceforge.net/>`__.

.. |A very generic gtk.TreeView base class| image:: http://farm1.static.flickr.com/252/456015767_28555b03d4.jpg
   :target: http://www.flickr.com/photos/25563799@N00/456015767/
.. |Subclassing the generic list| image:: http://farm1.static.flickr.com/252/456015819_4d8b64dd30.jpg
   :target: http://www.flickr.com/photos/25563799@N00/456015819/
.. |A little test application| image:: http://farm1.static.flickr.com/245/456016226_d409606743.jpg
   :target: http://www.flickr.com/photos/25563799@N00/456016226/
.. |A sample demo| image:: http://farm1.static.flickr.com/178/456016228_e7c4899286_o.png
   :target: http://www.flickr.com/photos/25563799@N00/456016228/
