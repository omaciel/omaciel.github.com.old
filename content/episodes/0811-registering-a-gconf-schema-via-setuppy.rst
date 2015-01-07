Registering a gconf schema via setup.py?
########################################
:slug: registering-a-gconf-schema-via-setuppy
:date: 2008-07-13 04:05
:category: English
:tags: english

I spent a good chunk of my evening trying to implement the automatic
registration of a gconf schema file via a setup.py and… got nowhere.
Seems that most people who wanted to do the same ended up running
gconftool-2 directly as such:

    GCONF\_CONFIG\_SOURCE=\`gconftool-2 —get-default-source\`
    gconftool-2 —makefile-install-rule /etc/gconf/schemas/\*.schemas

Has anyone got any advice (patches wouldÂ  be awesome) to go with my
`code <http://code.google.com/p/billreminder/source/browse/trunk/setup.py>`__?
