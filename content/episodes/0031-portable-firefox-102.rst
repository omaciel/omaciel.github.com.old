Portable FireFox 1.0.2
######################
:slug: portable-firefox-102
:date: 2005-03-24 13:47
:category:
:tags: english

For all you crazy USB-Portable-Device-Lovers out there: `Portable
FireFox 1.0.2 <http://johnhaller.com/jh/mozilla/portable_firefox/>`__
has been released!!! My favorite new features are:

    **COMMANDLINE PASSING** - The Portable Firefox launcher now supports
    commandline passing! That’s right, you can drag an HTML file onto
    PortableFirefox.exe and drop it and it will open it right up. You
    can even manually set PortableFirefox.exe to be your default browser
    in Windows and it will open up URLs correctly. It will only pass in
    one commandline parameter and it is expecting it to be a URL. For
    the curious developers, I was able to add commandline passing by
    moving all paths in the launcher to relative from the EXE allowing
    me to avoid using the FullPath functions (which break the
    commandline reader). **LOCAL PROFILE ADJUSTMENT** - The new launcher
    now allows you to use your local profile within Portable Firefox.
    Just copy the contents of your local profile into the profile
    directory within Portable Firefox and the Portable Firefox launcher
    will make the necessary adjustments for you. It will not adjust
    anything within prefs.js, though, so some extensions and themes will
    not work.

Get full details at
`this <http://forums.mozillazine.org/viewtopic.php?p=1303444>`__
mozillaZine thread.
