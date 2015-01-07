Using Python to Control Katello
###############################
:slug: using-python-to-control-katello
:date: 2013-09-13 00:36
:category: English
:tags: katello, english, python

|Emacs editor with python code|

I usually like to use python to script my day to day tests against
`Katello <http://www.katello.org/>`__ (you may have seen some of my
`previous <http://ogmaciel.tumblr.com/post/52170839167/populating-a-katello-instance-using-the-cli>`__
`posts <http://ogmaciel.tumblr.com/post/29571582261/script-to-populate-a-katello-instance-with-valid-data>`__
about using the Katello CLI for the same purpose) and I figured I’d
start showing some basic examples for anyone else out there who may be
interested.

Assuming you have already installed and configured your Katello instance
(learn how to do this
`here <https://fedorahosted.org/katello/wiki/Install>`__) with the
default configurations, we now have a few options to proceed:

#. write and run your scripts in the same environment as your server
#. install the
   `katello-cli <https://pypi.python.org/pypi/katello-cli/>`__ package
   (*pip install katello-cli*)
#. Use git to clone the katello-cli
   `repository <https://github.com/Katello/katello-cli>`__ (*git
   clone https://github.com/Katello/katello-cli.git*) and make sure to
   include it into your **PYTHONPATH**.

**Option 1** is by far the easiest approach since you should have all
the dependencies (namely **kerberos** and **M2Crypto**) already
installed, but I like **Option 3** as it allows me to always have the
latest code to play with.

Now we’re ready to write some code! The first thing we’ll do is import
some of the Katello modules:

     from katello.client import server
     from katello.client.server import BasicAuthentication
     from katello.client.api.organization import OrganizationAPI
     from katello.client.api.system\_group import SystemGroupAPI

Next, we establish a connection to the Katello server
(**qetello01.example.com** in my case), using the default credentials of
**admin**/**admin**:

    katello\_server = server.KatelloServer(host='qetello01.example.com',
    path\_prefix='/katello/', port=443)
    katello\_server.set\_auth\_method(BasicAuthentication(username='admin',
    password='admin'))
    server.set\_active\_server(katello\_server)

 

Let’s now instantiate the Organization API object and use it to fetch
the “\ **ACME\_Corporation**" that gets automatically created for a
default installation:

 

    organization\_api = OrganizationAPI()

    org = organization\_api.organization('ACME\_Corporation')
    print org
    {u’apply\_info\_task\_id’: None,
    u’created\_at’: u’2013-09-12T20:15:06Z’,
    u’default\_info’: {u’distributor’: [], u’system’: []},
    u’deletion\_task\_id’: None,
    u’description’: u’ACME\_Corporation Organization’,
    u’id’: 1,
    u’label’: u’ACME\_Corporation’,
    u’name’: u’ACME\_Corporation’,
    u’owner\_auto\_attach\_all\_systems\_task\_id’: None,
    u’service\_level’: None,
    u’service\_levels’: [],
    u’updated\_at’: u’2013-09-12T20:15:06Z’}

| 

Lastly, let’s create a brand new organization:

 

    new\_org = organization\_api.create(name='New Org', label='new-org',
    description='Created via API')
    print new\_org
    {u’apply\_info\_task\_id’: None,
    u’created\_at’: u’2013-09-12T21:48:55Z’,
    u’default\_info’: {u’distributor’: [], u’system’: []},
    u’deletion\_task\_id’: None,
    u’description’: u’Created via API’,
    u’id’: 283,
    u’label’: u’new-org’,
    u’name’: u’New Org’,
    u’owner\_auto\_attach\_all\_systems\_task\_id’: None,
    u’service\_level’: None,
    u’service\_levels’: [],
    u’updated\_at’: u’2013-09-12T21:48:55Z’}

| 

As you can see, it is pretty straight forward to use python to create
some useful scripts to drive a Katello server, whether you want to
populate it with a pre-defined set of data (e.g. default users, roles,
permissions, organizations, content, etc) or to test core functionality
as I do with `Mangonel <https://github.com/omaciel/mangonel>`__, my pet
project.

 

Here’s a
`Gist <https://gist.github.com/anonymous/71c0527841d30b80424b>`__ of the
code mentioned in this post, and let me know if this was useful to you.

.. |Emacs editor with python code| image:: http://bit.ly/14Q0fhi
