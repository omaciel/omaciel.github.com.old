Migrating to Google Code Follow up #1
#####################################
:slug: migrating-to-google-code-follow-up-1-2
:date: 2008-04-02 10:49
:category: English
:tags: english

So I have finally migrated
`BillReminder <http://code.google.com/p/billreminder/>`__ to **Google
Code**, thanks to the helping hand of a few gents from Google. I did
expect a full, smooth migration process but, for better or worse, there
are a lot of manual steps that **you** have to perform before you can
have the same structure (well, not the same but something usefull) from
`SourceForge <http://www.sf.net>`__. I figured I’d mention here some of
the things I had to do for those who may find themselves wanting to do
the same thing.

I **strongly** recommend that you subscribe to the `Hosting at Google
Code <http://groups.google.com/group/google-code-hosting>`__ discussion
group… this is where you can expect some good help and pointers!

Once you have your project set up, you’ll probably want to migrate your
source code repository from SourceForge. That can be easily done by
executing the following command:

    svnsync init —username **[your username]** https://\ **[your
    project]**.googlecode.com/svn https://\ **[your
    project]**.svn.sourceforge.net/svnroot/\ **[your project]** svnsync
    sync —username **[your username]** https://\ **[your
    project]**.googlecode.com/svn

Obviously, you want to change the commands above with your information.
It is also important to fetch your repository’s password (not to confuse
with your gmail’s password) from your project’s settings page, as you’ll
be prompted for it.

The second command responsible for synching up your new repository
failed for me a couple of times… but do not dispair. For me, **four
times** was a charm! :)

From that point onward, I tweaked the settings for my project a bit and
even managed to add the latest release to the downloads page.
Unfortunately my bugs, patches and feature/support requests were not
part of the migration and I’m yet to read up on how to do it (hopefully)
without too much complications. More on that on another follow up post,
as well as how to set up mailing lists and commit lists for your
developers.

So don’t forget to update the source code repository the next time you
feel the urge to contribute with BillReminder:

    ``svn checkout http://billreminder.googlecode.com/svn/trunk/ billreminder-read-only``
