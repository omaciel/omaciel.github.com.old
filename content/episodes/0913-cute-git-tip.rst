Cute Git Tip
############
:slug: cute-git-tip
:date: 2009-07-17 15:56
:category: English
:tags: english

[caption id=”” align=”alignnone” width=”500” caption=”Happiness by
Sabrina Campagna cc-by”]\ |Happiness by Sabrina Campagna
cc-by|\ [/caption]

I was hanging out in the lobby of the `Catalina Park
Appartments <http://www.catalinapark.es/>`__ last week writing some code
when I was approached by **Diederik van der Boor** (of **KMess** fame)
who was also hacking away and had a question about Git.

-  **Diederik**: are you an expert on git by any chance?
-  **Me**: hardly, but what is the question?
-  **Diederik**: I just made a few changes to a single file and was
   wondering if it is possible to commit specific chunks?
-  **Me**: hmmmm… don’t think so but that would be really cool!!!

He went back to his chair and I immediately starting scouring the web
for more information about this. Luckly, one of the very first hits I
got back was **Ryan Tomayko**'s post called “\ `The Thing About
Git <http://tomayko.com/writings/the-thing-about-git>`__\ ”! I had
barely read the entire article when I shouted to Diederik: “\ **I think
I found a solution! You better come over here and sit down!**" What
followed then were several minutes of more reading, sprinkled with a lot
of drooling and happy exclamations from both of us!

I highly recommend you read the article, but the short answer is to use:

::

    git add --patch [modifed-file-name]

In other words, say you’ve modifed the files foo.py and bar.py.
Committing these 2 files with all their changes is straight forward, but
what if you only wanted to perform a partial commit of your changes to
bar.py? Easy enough! Commit foo.py as usual and use the —patch “flag” to
commit bar.py.

    "This instructs Git to display all changes to the files specified on
    a hunk-by-hunk basis and lets you choose one of the following
    options for each hunk:

    -  *y* â€“ stage this hunk
    -  *n* â€“ do not stage this hunk
    -  *a* â€“ stage this and all the remaining hunks in the file
    -  *d* â€“ do not stage this hunk nor any of the remaining hunks in
       the file
    -  *j* â€“ leave this hunk undecided, see next undecided hunk
    -  *J* â€“ leave this hunk undecided, see next hunk
    -  *k* â€“ leave this hunk undecided, see previous undecided hunk
    -  *K* â€“ leave this hunk undecided, see previous hunk

    *s* â€“ split the current hunk into smaller hunks” (`Ryan
    Tomayko <http://tomayko.com/writings/the-thing-about-git>`__)

So, in other words:

::

    git add foo.py
    git add --patch bar.py

I don’t know about you but this neat little trick made my day!

.. |Happiness by Sabrina Campagna cc-by| image:: http://farm4.static.flickr.com/3092/2620922750_bfcd2cf29e_d.jpg
   :target: http://www.flickr.com/photos/mar1lyn84/2620922750/
