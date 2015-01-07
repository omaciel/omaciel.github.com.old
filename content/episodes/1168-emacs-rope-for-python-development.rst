Emacs + Rope for Python Development
###################################
:slug: emacs-rope-for-python-development
:date: 2013-12-09 19:30
:category:
:tags: Emacs, Python, Rope, Pymacs, gnome

|screenshot|

***Disclaimer:** This is more of a note for myself than a proper
tutorial or howto, so I make no promises that this will work for you.
The setup used through this post was a Mac OS laptop upgraded to the
very latest version of the OS.*

Ever since I started doing **Python** development using **Emacs**, I
have unsuccessfully tried to configure
**`Rope <http://rope.sourceforge.net/>`__,**"a python refactoring
library"… until last Friday. Turns out I wasn’t too far off the mark
during the many iterations I went through to get it done, but the
following post was tremendously helpful to
me: \ `http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/ <http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/>`__

Here’s what worked for me:

Install **Pymacs** (Emacs part):

-  `Download <https://github.com/pinard/Pymacs/tarball/v0.2>`__ latest
   (0.25 as of the writing of this post)
-  cd to the source code directory
-  make
-  mkdir ~/.emacs.d/vendor/pymacs
-  cp pymacs.el ~/.emacs.d/vendor/pymacs/pymacs.el
-  `emacs -batch -eval ‘(byte-compile-file
   “~/.emacs.d/vendor/pymacs/pymacs.el”)’ <https://github.com/pinard/Pymacs/tarball/v0.25>`__

`Install Pymacs
( <https://github.com/pinard/Pymacs/tarball/v0.25>`__\ Python part):

-  sudo pip install
   `https://github.com/pinard/Pymacs/tarball/v0.2 <https://github.com/pinard/Pymacs/tarball/v0.2>`__

Install \ **ropemacs** and **rope** with sudo pip install
`http://bitbucket.org/agr/ropemacs/get/tip.tar.gz <http://bitbucket.org/agr/ropemacs/get/tip.tar.gz>`__

Now configure Emacs by adding the following lines to your init.el file:

| (require ‘pymacs)
| (pymacs-load “ropemacs” “rope-“)
| (setq ropemacs-enable-autoimport t)

Finally, start up Emacs and make sure to read this
`document <https://bitbucket.org/agr/ropemacs>`__ for some examples on
how to use Rope.

.. |screenshot| image:: https://farm3.staticflickr.com/2875/11294955694_5450819b65_z_d.jpg
