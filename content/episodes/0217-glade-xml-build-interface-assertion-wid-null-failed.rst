glade_xml_build_interface: assertion `wid != NULL' failed
#########################################################
:slug: glade-xml-build-interface-assertion-wid-null-failed
:date: 2006-01-04 04:05
:category:
:tags: english

Spent a good 2 nights trying to figure out what the following error
meant:

    glade\_xml\_build\_interface: assertion \`wid != NULL’ failed

The error was genetated when I tried to compile a small C#Ã‚Â  program I
wrote using Glade for the UI.Ã‚Â  As a good netizen, I googled for the
meaning of this but just couldn’t get usefull info…Ã‚Â  until now!Ã‚Â 
Apparently, the error results from setting up the Glade.XML object and
not using the same exact name for your forms/windows as you gave them in
your .glade file.Ã‚Â  For instance, the code:

    Glade.XML gxml = new Glade.XML (null, “billreminder.glade”,
    “frmMain”, null);

expects the real name of the glade file generated during the UI design
(well, that’s a no brainer, but that is not where the error occurs) and
the exact name you gave your form/window… and THAT is the part that
wasn’t obvious to me…Ã‚Â  In other words, instead of using “frmMain”, as
I named my form/window in Glade, I put something else, assuming that it
was supposed to be the title I wanted to show up at the form/window’s
title bar….

*ref*:
`http://mail.python.org/pipermail/tutor/2003-September/025114.html <http://mail.python.org/pipermail/tutor/2003-September/025114.html>`__
