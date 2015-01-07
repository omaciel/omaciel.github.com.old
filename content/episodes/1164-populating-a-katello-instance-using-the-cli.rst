Populating a Katello instance using the CLI
###########################################
:slug: populating-a-katello-instance-using-the-cli
:date: 2013-06-04 22:21
:category:
:tags: english, katello, Red Hat

Lately I have been asked a lot about my previous
`script <http://bit.ly/13jSmSx>`__ to automatically populate a
`Katello <http://www.katello.org/>`__ server instance with real data (hi
**reyc**!) I wrote that a while back and though it still does contain
some helpful commands, I figured it was about time I updated it. Well,
it took me longer than I expected to find some time and clean it up, but
I think I can now show you a brand new script which also includes the
extra feature of downloading a manifest file directly from **Red Hat**'s
portal and importing it as part of the process.

Currently the script assumes that you have the following information
(either as environmental variables or substituted into the script:

    **RHN\_USERNAME**: A valid username for
    `https://access.redhat.com/ <https://access.redhat.com/>`__

    **RHN\_PASSWORD**: A valid password for
    `https://access.redhat.com/ <https://access.redhat.com/>`__

    **DISTRIBUTOR**: An existing distributor UUID with access to Red Hat
    Enterprise Linux 6 Server products

The `new script <http://bit.ly/15Fk4di>`__ is know to work with the very
**latest Katello nightly build**. If you have any suggestions or
constructive feedback, feel free to leave me a comment here or fork the
`gist <http://bit.ly/15Fk4di>`__ and send me a pull request!
