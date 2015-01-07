Django Debug Toolbar
####################
:slug: django-debug-toolbar
:date: 2010-04-12 00:47
:category:
:tags: english

I meant to write about the `Django Debug
Toolbar <http://github.com/robhudson/django-debug-toolbar>`__ before but
other things kept getting on the way. Basically, if you work with
`Django <http://www.djangoproject.com/>`__ then you’ll appreciate this
“configurable set of panels that display various debug information about
the current request/response and when clicked, display more details
about the panel’s content.”

[caption id=”attachment\_875” align=”aligncenter” width=”300”
caption=”Django Debug Toobar”]\ |image0|\ [/caption]

Imagine working on your application and being able to get a list of all
of its settings, HTTP headers, display GET/POST/cookie/session
variables, templates and context used and their template paths, SQL
queries including time to execute and links to EXPLAIN each query, list
of signals, their arguments and receivers,… want more? There is also the
super nifty debugsqlshell command that outputs the sql statements that
gets executed when you work with your models in the Python interactive
shell.

|The debugsqlshell command|

Now, usually when adding django modules, one has to read through README
or INSTALL files to understand what needs to g0 and where. But this time
you’re in for a treat as the developer has taken the time to distill the
steps needed to get the Django Debug Toolbar working with your
application so that you can spend less time reading documentation and
more time hacking. Simply modify your existing settings.py to include
the following 3 lines:

|Using Django Debug Toolbar in 3 easy steps|

It is that easy! Make sure to read up on all the possible tweaks you can
make with it and let the developer know what you think of this awesome
tool!

.. |image0| image:: http://www.ogmaciel.com/wp-content/uploads/2010/04/Screenshot-Django-Bookmarks-300x261.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/04/Screenshot-Django-Bookmarks.png
.. |The debugsqlshell command| image:: http://www.ogmaciel.com/wp-content/uploads/2010/04/debugsqlshell-300x226.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/04/debugsqlshell.png
.. |Using Django Debug Toolbar in 3 easy steps| image:: http://www.ogmaciel.com/wp-content/uploads/2010/04/django-debug-toolbar-settings-300x163.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/04/django-debug-toolbar-settings.png
