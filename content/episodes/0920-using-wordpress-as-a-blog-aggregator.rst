Using WordPress as a blog aggregator
####################################
:slug: using-wordpress-as-a-blog-aggregator
:date: 2009-10-16 02:41
:category: English
:tags: english

One of the many things I maintain outside work is a `blog
aggregator <http://planeta.gnulinuxbrasil.org/>`__ (aka “planet”) for
blogs about open source and technology from the Brazilian community. I
try to invite new authors to this “planet” who have something
interesting to share about their lives, regardless of what Linux
distribution they use, gender, political views or religious beliefs. It
is not as popular as some of the other Brazilian news sites, but I think
it has a good number of subscribers.

The engine behind it was for the last 3 years the well known
`planetplanet <http://www.planetplanet.org/>`__ feed reader and for most
of the part it did its job well. Every now and then there would be a
hiccup here and there, mostly due to badly formatted feeds, but things
usually worked itself out without any intervention. Well, it turns out
that this aggregator had stopped working for quite some time without my
knowledge (what can I say, I’ve been busy and selectively picking what
emails to read) and people started complaining to me that they couldn’t
receive their news anymore.

To make a long story short, I spent many iterations trying to get rid of
all the brokenness by parsing the configuration file and error logs, and
whacking the “bad” feeds when it dawned on me: “This should be easier
like maintaining a blog!” The first thing that came to mind was to use
`WordPress <http://www.wordpress.org>`__ as the “framework” and see if
there was a plugin to turn it into a blog aggregator. A few hits on a
Google search brought me to
`FeedWordPress <http://feedwordpress.radgeek.com/>`__, “an
`open-source <http://feedwordpress.radgeek.com/wiki/license>`__ Atom/RSS
aggregator for the WordPress weblog software. It syndicates content from
feeds that you choose into your WordPress weblog; if you syndicate
several feeds you can use WordPress’s posts database and templating
engine as the back-end of an aggregator (“planet”) website.”

If that sounds too easy of a solution, then rest assured: **it is**!
After performing a standard WordPress installation, I added this plugin
and… voilÃ¡! The aggregator was born! There’s even an easy to use web
interface that not only allows you to copy and paste the url of the blog
you want to syndicate, but it validates it too! How convenient!

So far the web site seems to be running just fine, updating blogs as
they come fresh out of their respective sites. No more ssh’ing to my
server to enter new entries into a configuration file… Lots of already
developed/created plugins, widgets, themes, you name it out there for me
to use… and a huge user base to answer any question I may have about the
platform!

Now, I don’t know anything about performance issues and/or benchmark
numbers for running an aggreagtor with WordPress compared to any other
tool out there (if you do, please share), but if you need something done
quick and painless, you may want to try it yourself.
