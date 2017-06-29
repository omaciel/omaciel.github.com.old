Just What Is A Quality Engineer? Part 1
#######################################
:date: 2017-06-29
:authors: Og Maciel
:category: English
:tags: 
:description: 

.. figure:: images/batman-is-qe.jpeg
   :alt: Picture of `Batman`_
   :align: left
   :scale: 50 %

Whenever I meet someone for the first time, after we get past the initial niceties typically involved during the initial awkward moments, eventually the conversation shifts to work and what one does for a living. Inevitably I'm faced with what, at a first glance, may sound like a simple question:

* New acquaintance: "What do you do at Red Hat?"
* Me: "I manage a team of quality engineers for a couple of different products."
* New acquaintance: "Oh, you mean quality assurance, right? QA?"
* Me: "No, quality **engineers**. QE."

What follows then is a lengthy monologue (me) whereby I spend usually around ten to fifteen minutes explaining what the difference between QA and QE is and what, in my opinion, sets these two professions apart. Now, before I get too deep into this topic, I have to add a disclaimer here so not to give folks the impression that what I'm about to talk about is backed by any official definition or some type of professional trade organization! The following are my own definitions and conclusions, none of which were pulled out of thin air, but backed by (so far) 10 years of experience working on the field of delivering quality products. If there are formal definitions out there, I'm not aware of them but feel free to send them to me.

Why the term 'Quality Engineer' is not well known I'm not sure, but I have a hunch that it may be related to something I noticed throughout the 10 years that I have spend on this field. In my personal experience, 'quality' is something that is not always considered as part of the creation of a new company, product or project. Furthermore, the term 'quality' is also not well defined or understood by those involved in actually attempting to 'get more' of it.

In my experience, folks usually forget about the word 'quality', whatever that may be, happily plan and develop their new ideas/products and eventually ship it to their customers. If the customer complains that something is not working or performing as advertised or it doesn't meet their expectations, no problem. Someone will convey the feedback back to the developers, a fix will eventually be provided and off it goes to the customer. Have you every seen this before? I have!

Eventually, assuming that the business is doing well and are attracting more paying customers, it is very likely that support requests or requests for new features will increase. After all, who wants to pay for something that doesn't work as as expected? Who doesn't want a new feature of their own either? Depending on the size of company and the number of new requests going into their backlog, I'd expect that either one of the following events would take place:

* More tasks from the backlog would be added to individual's 'plates', or
* New associates would be hired to handle the volume of tasks

I guess one could also stop accepting new requests for support or new features, but that would not make your customers happy, wouldn't it?

Regardless of the outcome, the influx of new tasks has been dealt with and if things get out of control again, one could always try to get an intern or distribute tasks more evenly. Now, notice how the word 'quality' has not been mentioned yet? It is no accident that to solve an increase of more work, most often than not the number one solution used is to throw more resources at it. There's even a name for this type of 'solution': `The Mythical Man-Month`_.

You see, sadly, 'quality' is something that usually only becomes important as an afterthought. It is the last piece added to the puzzle that comprises the machinery of delivering something to an end user. It is only when enough angry and unsatisfied paying customers make enough noise about the unreliability or usability of the product that folks start asking: "Was this even tested before being put on the market?"

If the pain being inflicted by customer feedback is sharp enough, a **Quality Assurance** (QA) is hastily put together. Most of the time in my experience, this is a Team of One usually made up of one of the developers who were dragged kicking and screaming and eventually beat into accepting his new role as a button pusher, text field filler, testing guy. Issues are then assigned to QE and a general sense of relief is experienced by all. Have you also seen this before? I have! I'm 2 for 2 so far!

The idea is that, by creating a team of one to sit in the receiving end of the product release cycle, nothing would get shipped until some level of 'quality' is achieved. The fallacy with this statement, however, is that no matter how agile your team may be, the assurance of the quality for a product somehow is still part of a `waterfall model`_. Wouldn't it be better if problems were caught as early as possible in the process instead of waiting until the very end? To me that is a no brainer but somehow the process of testing a product is still relegated to the end, usually when the date for the release is just around the corner.

Why is the term **Quality Engineer** not well known then? I feel that the answer is comprised of several parts:

* 'Quality' doesn't come into the picture, if every, until the very end of the game;
* If there is a QA team, nobody outside of that team really knows what they do. It has something to do with testing...
* Engineering is usually identified with skills related to writing code and designing algorithms, usually by a developer and not by QA;

No surprise that quality engineering is something foreign to most!
  most people working around I.T. are not familiar 

OK, so what **is** a **Quality Engineer** then? Glad you asked! The answer to that I shall provide in a subsequent post, as I still need to cover some more ground and talk about what 'quality' is, what someone in QA does and finally what is a QE!

Please bear with me as I take you on this journey through the land of Quality and Engineering, and in the meantime, let me know what you think about this subject.


.. Links
.. _Batman: http://spiderguile.deviantart.com/art/Batman-Videsh-Colors-104228245
.. _The Mythical Man-Month: https://en.wikipedia.org/wiki/The_Mythical_Man-Month
.. _Waterfall model: https://en.wikipedia.org/wiki/Waterfall_model
