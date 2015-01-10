My first conary package
#######################
:slug: my-first-conary-package
:date: 2006-10-05 17:56
:category: English
:tags: rpath, conary

W00t!!! With the help (and lots of patience) from
`Ken <http://ken.vandine.org/>`__, I was able to cook up my very first
package using the
`Conary <http://wiki.rpath.com/wiki/Conary:Concepts>`__ system! The
package was the `Drivel <http://www.dropline.net/drivel/>`__ blogging
tool and it has already been pushed up to rPath Contrib.

Packaging for any conary-based system is as simple as writing up a
recipe (for nostalgia, mine is included below) and “cooking” it with
conary!

::

    class Drivel(AutoPackageRecipe):
       name = 'drivel'
       version = '2.0.3'
       buildRequires = ['GConf:devel', 'GConf:runtime', 'ORBit2:devel', 'aspell:devel', 'atk:devel', 'cairo:devel', 'curl:devel', 'dbus-glib:devel', 'dbus:devel', 'desktop-file-utils:runtime', 'e2fsprogs:devel', 'expat:devel', 'fontconfig:devel', 'freetype:devel', 'gettext:runtime', 'glib:devel', 'gnome-keyring:devel', 'gnome-vfs:devel', 'gtk:devel', 'gtk:runtime', 'gtksourceview:devel', 'gtkspell:devel', 'krb5:devel', 'libICE:devel', 'libSM:devel', 'libX11:devel', 'libXrender:devel', 'libart_lgpl:devel', 'libbonobo:devel', 'libbonoboui:devel', 'libglade:devel', 'libgnome:devel', 'libgnomecanvas:devel', 'libgnomeprint:devel', 'libgnomeui:devel', 'libpng:devel', 'libxml2:devel', 'openssl:devel', 'pango:devel', 'perl:runtime', 'pkgconfig:devel', 'popt:devel', 'scrollkeeper:runtime', 'shared-mime-info:runtime', 'zlib:devel']

       def unpack(r):
           r.addArchive('mirror://sourceforge/%(name)s/')

Anyone interested in learning about Conary and how to package stuff,
sign up for a free account at
`rBuilder <http://www.rpath.com/rbuilder/>`__ and check out the
documentation.
