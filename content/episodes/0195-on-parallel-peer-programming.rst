On Parallel Peer Programming
############################
:slug: on-parallel-peer-programming
:date: 2005-10-19 17:49
:category: English
:tags: english

Reading Scott James Remnant’s latest
`post <http://www.netsplit.com/blog/work/canonical/parallel_peer_programming.html>`__
on what he calls “Parallel Peer Programming” got me wondering if the
same approach could work for the small project I’ve been secretly
working on.

Scott fired up 3 separate screem sessions to which his co-worker Gustavo
Niemeyer synced to. From that point one, they could see what each other
was doing “live” in their respective terminals/laptops. Scott would
write test cases in one terminal (to which Gustavo could now “watch”),
Gustavo would then write the code in the second terminal to make sure it
would pass the test, and use the third terminal to test it.

I have finally convinced
`SupertoadMan <http://www.supertoadman.com/cs/blogs/supertoadman/default.aspx>`__
to join me and provide some needed help. Since we live far from each
other (he lives in Farm land, err… near Boston and I live near NYC) and
rarely get a chance to just sit down and code, this may just work. The
only obstacle I can foresee is convincing him to ssh into my server
(he’s a Windows OS guy and barfs when he has to use a console) using
Putty…
