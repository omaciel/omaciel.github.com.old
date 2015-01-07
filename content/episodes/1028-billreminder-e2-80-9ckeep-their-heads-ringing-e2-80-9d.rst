BillReminder “Keep Their Heads Ringing” Released
####################################################
:slug: billreminder-e2-80-9ckeep-their-heads-ringing-e2-80-9d
:date: 2010-12-31 21:04
:category:
:tags: english

[caption id=”attachment\_1268” align=”alignleft” width=”300”
caption=”BillReminder “Keep Their Heads Ringing” 0.4.0”]\ |BillReminder
"Keep Their Heads Ringing" 0.4.0|\ [/caption]

Just in time before the new year, it is with great pleasure that I
announce the release of
`BillReminder <http://billreminder.gnulinuxbrasil.org/>`__ “\ **Keep
Their Heads Ringing**" 0.4.0 after a **27-month** hiatus! During this
period I tried many different approaches and techniques to both improve
the user interface as well as the overall experience. Many of the “core”
changes were performed only to satisfy my own curiosity and
experimentation with other technologies out there, but overall you
should have a good time playing with it.

`BillReminder <http://billreminder.gnulinuxbrasil.org/>`__ is not a
replacement for your accounting system or elaborate services such as
**Mint.com**. It’s purpose is to **provide an easy way for getting
notified about upcoming payments keeping yourself ahead of your bills**!

BillReminder “Keep Their Heads Ringing” 0.4.0 can be downloaded from:
`http://ftp.gnome.org/pub/GNOME/sources/billreminder/0.4/ <http://bit.ly/BillReminder-0_4_0>`__

-  `billreminder-0.4.0.tar.bz2 <http://bit.ly/hCdgEm>`__ (**sha256sum**
   6a89584a1c90f661a7954a0c5c8bd392b8e2712d6cfd759fb6e588548ac8ff4e )
-  `billreminder-0.4.0.tar.gz <http://bit.ly/iaxXGG>`__ (**sha256sum**
   9a81ac46f3688a2a25d3114de2ffbc88760ec50d55d12827fc6d83a9859e9cef)

**Features**:

-  Switched most of the user interface code to **Glade** files with the
   hope that it will ease future contributions from ui developers.
-  Support for configuring notification alarms.
-  Switched database layer from custom code to **SQLAlchemy**.
-  Changed license from **BSD** to **GPL v3**.
-  A set of default categories are now created by default on
   new installations.
-  Better overall data validation when adding or editing bills.
-  Changed menu to use standard “\ **File**" entry instead of
   previous "**Bill**\ " menu entry.
-  Borrowed **GConf** handler from the **Conduit** project and register
   gconf schema by default.
-  Added **charting support** from the **Hamster** project for better
   visualization of your expenditure.
-  A new **calendar widget** has been added to replace the calendar from
   the add/edit dialog. In order to display the calendar, it is
   necessary to expand the widget by clicking on the displayed date.
-  **Recurring bills** are now handled by selecting a frequency (the
   current allowed values are: **once, weekly, and monthly**) and
   setting the end date. Multiple records will then be added using the
   start and end date to figure out their correct due date.
-  A new **timeline widget** has been added to replace the calendar from
   the main window. You can now use it to change the way you view your
   bills by selecting an specific date with a single click as well as
   drag the timeline to view past and/or future bills. The following
   keyboard shortcuts are available:

   -  right arrow     go to next day
   -  left arrow      go to previous day
   -  Ctrl + right    go to same day next month
   -  Ctrl + left     go to same day previous month
   -  + (plus)        zoom in
   -  - (minus)       zoom out
   -  HOME            go to today’s date
   -  PAGEUP          scroll to next screen\ **\***
   -  PAGEDOWN        scroll to previous screen

**\*** *go to current day plus the number of days displayed in widget.*

**Bug Fixes**:

-  #551953: It should be possible to add bills without an amount
   defined.
-  #553890: Different install/data paths.
-  #554228: Changed Record to Bill to be consistent with nomenclature.
-  #555136: Import sqlite3 if using python 2.5, or pysqlite2 if using
   python 2.4.
-  #556748: Don’t try to cast a dbus.String into an int type, if catId
   is ‘None’.
-  #561550: Make ‘notes’ widget scroll when number of lines go beyond
   the widget’s height.
-  #561751: UI Doesn’t refresh when deleting a record.
-  #563736: Warn users of overlapping dates for recurring bills.
-  #569023: Timeline widget will not support displaying multiple bills
   with different states on the same day.

**Translations**:

-  ca, courtesy of **Jordi Estrada**
-  ca@valencia, courtesy of **Francesc Dorca i Badia**
-  cs, courtesy of **Marek ?ernocký**
-  da, courtesy of **Joe Hansen**
-  de, courtesy of **Mario Blättermann**
-  el, courtesy of **??????? ???????????**
-  en\_GB, courtesy of **Jen Ockwell**
-  es, courtesy of **Jorge González**
-  fi, courtesy of **Ilkka Tuohela**
-  fr, courtesy of **Bruno Brouard**
-  gl, courtesy of **Fran Diéguez**
-  he, courtesy of **Yaron Shahrabani**
-  hr, courtesy of **Mario ?ani?**
-  hu, courtesy of **Gabor Kelemen**
-  it, courtesy of **Sergio Zanchetta**
-  lv, courtesy of **Toms Bau?is**
-  nb, courtesy of **Tommy Mikkelsen**
-  nl, courtesy of **Martijn Cielen**
-  pl, courtesy of **Tomasz Z. Napierala**
-  pt\_BR, courtesy of **Mateus Zenaide**
-  pt, courtesy of **Susana Pereira**
-  ro, courtesy of **Ionu? Jula**
-  ru, courtesy of **Ilya B**
-  sl, courtesy of **Andrej Žnidarši?**
-  sv, courtesy of **Daniel Nylande**\ r
-  tl, courtesy of **Jerome S. Gotangco**
-  tr, courtesy of **Rail Aliev**
-  zh\_CN, courtesy of **du baodao**

A special “\ **THANK YOU**" goes out to \ **Toms Bau?is** for keeping me
excited about programming by making the **Hamster** project an awesome
tool, never shying away from lending me a hand every now and then and
for letting me bounce ideas whenever I feel like trying some new
approach to a problem!

.. |BillReminder "Keep Their Heads Ringing" 0.4.0| image:: http://www.ogmaciel.com/wp-content/uploads/2010/12/billreminder-0.4.0-300x300.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/12/billreminder-0.4.0.png
