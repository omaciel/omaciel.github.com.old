Playing World of Warcraft on Linux with Wine
############################################
:slug: playing-world-of-warcraft-on-linux-with-wine
:date: 2010-06-11 15:00
:category:
:tags: english

[caption id=”attachment\_1109” align=”aligncenter” width=”300”
caption=”World of Warcraft”]\ |World of Warcraft|\ [/caption]

Yes, I’m still alive and kicking. Been really busy at work and haven’t
had the time or energy to write anything here. I have however kept my
**New Year’s resolution** of reading a book during lunch break every
day! I’m currently reading 2 books at the same time (check what other
books I have read and those I have still waiting on my queue in the
front page of my blog):

-  **For The Win** by Cory Doctorow
-  **The Fourth Part of the World** by Toby Lester

I feel that it is impossible to read Doctorow’s book and not feel the
urge to play `World of
Warcraft <http://www.worldofwarcraft.com/index.xml>`__ (WoW).
Impossible! I think the last time I played this game I still lived in
**Northern New Jersey** and was an **Ubuntu user** (yeah, I’ve matured
since then).

So I wanted to play WoW really bad after reading a chapter but wasn’t
sure how to do it since I only run **GNU/Linux** and didn’t feel like
setting up a **Windows VM** just to play a game! Talking to my long time
friend `Vinny <http://awkward-silence.com/>`__ I suddenly realized that
I never tried to run the game using `Wine <http://www.winehq.org/>`__,
so I decided that once I got home I’d take it for a spin.

After downloading a 3.3MB installer from Blizzard, and installing Wine
(*sudo conary update wine*), I went ahead and ran *wineÂ TryWoW.exe*.
What followed was a series of screens where I simply accepted the
defaults and clicked my way through. There were times when a dialog with
no messages popped up where all you could do was click on the OK button…
so I did.

The installation did require access to the internet and a bundle of
approximately 35MB was downloaded in the process. Once the wizard
finished I had the option to play the game right there and then! How
exciting!

The game takes a few extra seconds to start but eventually I was face to
face with the login window. However, I noticed that I had no audio and
the video quality lacked a bit. Googling around brought me to
theseÂ \ `instructions <https://help.ubuntu.com/community/WorldofWarcraft>`__.
So I modified my configuration file to include:

    SET gxApi “opengl”
    SET Sound\_SoundOutputSystem “1”
    SET Sound\_SoundBufferSize “150”

That was it!!! I spent the next 45 minutes playing the game using my
trial account and had to be dragged by my wife and kids to the kitchen
to eat diner with them! :)

I’m very satisfied with the experience and extremely pleased with the
stability of Wine! Since I have 2 monitors at home, my game window shows
up in one monitor while my “normal” desktop is on the other and I have
to be careful not to click outside of the game. If I do, then I cannot
go back into the game again and have to kill the process and start over.

Well, I still have a few more days until my trial period expires. Will I
then update to a full blown account and waste spend my free time
investing on my character? To be determined! :)

.. |World of Warcraft| image:: http://www.ogmaciel.com/wp-content/uploads/2010/06/Screenshot-300x84.png
   :target: http://www.ogmaciel.com/wp-content/uploads/2010/06/Screenshot.png
