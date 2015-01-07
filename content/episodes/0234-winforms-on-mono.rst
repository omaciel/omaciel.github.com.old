WinForms on Mono
################
:slug: winforms-on-mono
:date: 2006-02-14 03:51
:category: English
:tags: english

Been spending some time converting my pet application BillReminder
(written in C# using Microsoft Visual Studio .NET) so that it can run on
Linux… but this time, without the Gtk# libraries for all the graphical
rendering! Since I’m currently running Mono version 1.1.3 that comes
bundled with Ubuntu Dapper, I can tap on to the new features including
the port of the System.Windows.Forms namespace!!!

I must confess, the conversion process has been very minimal, and the
only thing I have to pick on is the native look of the widgets… I’m not
sure if I’m missing some other package, but the quality, or lack of, of
all widgets needs some serious work… But is ok… Just the fact that I can
write code that has the potential of being executed in several other
plataforms is exactly what I’ve been looking for all along! Sure I can
do that with some other languages (python, java and Tc come to mind),
but that fact is that the job market has been divided between Java and
.NETÃ¢â‚¬Â¦ And the ability to execute code in multiple platforms
without much loss is something that could influence any employer when
they have to choose between candidates who have that experience and
those who don’t! |image0|

.. |image0| image:: http://static.flickr.com/43/98804629_0852133753.jpg
   :target: http://static.flickr.com/43/98804629_0852133753_o.png
