State of RssReaderNET
#####################
:slug: state-of-rssreadernet
:date: 2005-05-06 19:25
:category: English
:tags: english

|image0|

`RssReaderNET - v0.0.2 <http://www.flickr.com/photos/25563799@N00/12678075/>`__

Originally uploaded by `omaciel <http://www.flickr.com/people/25563799@N00/>`__.

Haven’t received any offers of help with my RssReader.NET application…
but it’s not like I was expecting offers anyhow. :) Yesterday and today
I spent some time making some changes to the UI as well adding some new
functionality. UI changes include:

-  Removed ComboBox control - Users will have to add new feeds via an
   interface.
-  Switched ListView control for a TreeView control - Will allow for
   expansion/collapsing of feeds and increase visibility of available
   posts.
-  Added a few buttons - These will disappear and are being used for
   testing purpose only.


New functionality include:

-  Add new feeds - Works!
-  Save (serializes) existing feeds - For offline reading. Needs some
   work.
-  Loads saved feeds - Same as above.


Right now I’m stuck due to some problems in serializing some of the
objects (RssFeedCollection to be exact). Help figuring this out will be
deeply appreciated. Maybe I should start a project in
`SourceForge <http://www.sourceforge.net>`__\ …

.. |image0| image:: http://photos11.flickr.com/12678075_cbf9730de9_m.jpg
   :target: http://www.flickr.com/photos/25563799@N00/12678075/
