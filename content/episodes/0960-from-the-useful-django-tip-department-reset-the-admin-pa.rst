From the "Useful Django Tip" Department: Reset The Admin Password
#################################################################
:slug: from-the-useful-django-tip-department-reset-the-admin-pa
:date: 2010-04-19 15:00
:category:
:tags: english

This comes straight from the **Useful Django Tip** department: How do
you reset the admin password for a Django project when you’ve forgotten
it?

`Bruce
Kroeze <http://coderseye.com/2007/howto-reset-the-admin-password-in-django.html>`__
suggested using Django’s shell to resolve this common issue and one of
the comments his post received nailed it:

.. code:: python

    [omaciel@crutches souschef]$ python manage.py shell
    Python 2.6.5 (r265:79063, Mar 22 2010, 10:30:12)
    Type "copyright", "credits" or "license" for more information.

    IPython 0.10 -- An enhanced Interactive Python.
    ?Â Â Â Â Â Â Â Â  -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    helpÂ Â Â Â Â  -> Python's own help system.
    object?Â Â  -> Details about 'object'. ?object also works, ?? prints more.

    In [1]: from django.contrib.auth.models import User

    In [2]: u = User.objects.get(username__exact="admin")

    In [3]: u.set_password('whatever');

    In [4]: u.save()

Thatâ€™s it!

**P.S.:** Back by popular demand, posts in its full content!
