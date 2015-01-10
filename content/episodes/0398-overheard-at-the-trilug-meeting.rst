Overheard at the TriLUG meeting
###############################
:slug: overheard-at-the-trilug-meeting
:date: 2006-09-14 22:38
:category: English
:tags: trilug

Interesting:

    **evilaptop**: Dude, CHICKS DIG UNIX **evilaptop**: Everyone knows
    that **evilaptop**: Right?? **JasonF**: that’s almost as
    unattractive as someone who scripts festival to sing “99 bottles of
    beer on the wall” at a party

Funny how a lot of the attendees were also chatting on #trilug! hehehe

What??? You’re actually interested in how to do it??? Ok, ok… The source
code was also provided! hehehehe

#. #!/usr/bin/python
#.
#. # 99 bottles of beer on the wall.
#. # Inspired by (who’d of thunk) beer!
#.
#. from os import popen
#. from time import sleep
#.
#. def printsay(sometext):
#. print sometext
#. voicehandle.write("(SayText ""+sometext+"”)”)
#. # Start talkin’ you varmint!
#. voicehandle.flush()
#. # It’d be nice if festival would tell us when it’s done talking.
#. sleep(3)
#.
#. # 2 bottles, 1 bottle, no bottles
#. def pluralize(somenumber,sometext):
#. if ( somenumber > 1 ):
#. retval = str(somenumber)+" "+sometext+"s"
#.
#. if ( somenumber == 1):
#. retval = str(somenumber)+" "+sometext
#.
#. if ( somenumber == 0):
#. retval = "No "+sometext+"s"
#.
#. return retval
#.
#. # Open up a pipe to festival so we don’t keep respawning
#. voicehandle = popen("festival","w")
#.
#. # Start with 99 bottles
#. num\_bottles = 99
#.
#. # Do what now?
#. refrain = "Take one down, pass it around."
#.
#. # As long as there’s beer, we drink!
#. while ( num\_bottles > 0 ):
#. printsay(pluralize(num\_bottles,"bottle")+" of beer on the wall.")
#. printsay(pluralize(num\_bottles,"bottle")+" of beer.")
#. printsay(refrain)
#. num\_bottles = num\_bottles - 1
#. printsay(pluralize(num\_bottles,"bottle")+" of beer on the wall.")
#. print "—-"

**Update**:Ã‚Â  Got to meet `Daniel T
Chen <https://launchpad.net/people/crimsun>`__ at the end of the
meeting.Ã‚Â  What a great guy!Ã‚Â  Hope to see him soon again!
