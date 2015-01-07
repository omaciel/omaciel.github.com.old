Setting up Vim for Clojure development notes
############################################
:slug: setting-up-vim-for-clojure-development-notes
:date: 2012-05-16 20:41
:category: English
:tags: Eclipse, Clojure, vim, repl, lein, Dropbox, english

Started the process of getting jiggy with
`Clojure <http://clojure.org/>`__ at work and didn’t like the idea of
using **Eclipse** for my day to day work… so I started looking at how to
make **vim** and **clojure** get along and came across a great
`post <http://writequit.org/blog/?p=386>`__! Here are the distilled
notes plus minor tweaks to get anyone out there trying to do the same
thing going:

#. Download **VimClojure**
   (`http://www.vim.org/scripts/script.php?script\_id=2501 <http://www.vim.org/scripts/script.php?script_id=2501>`__)
#. Download **VimSlime**
   (`https://github.com/jpalardy/vim-slime <https://github.com/jpalardy/vim-slime>`__)
#. Extract these files into your **~/.vim** folder
#. Add the following lines to **~/.vimrc**:

   -  " Settings for VimClojure
   -  let vimclojure#HighlightBuiltins = 1
   -  let vimclojure#ParenRainbow = 1
   -  " Send entire file to repl
   -  nmap <C-m> ggVG<C-c><C-c>

#. Start a repl session inside screen:

   -  screen -S clojure
   -  lein repl

#. Open a clojure file with vim and highlight the method you want to
   evaluate
#. Press ctrl + c twice

   -  For session name prompt, enter ‘clojure’ which is the name of the
      screen session
   -  For window name prompt, accept the default number displayed

#. The selected code should be evaluated in the screen session
#. Press ctrl + c, v to get prompt again

|Vim and Clojure sitting on a tree|

**NOTES**:

-  I chose to start a repl using
   `lein <https://github.com/technomancy/leiningen>`__ but you can use
   whatever you’re familar with to get a repl started
-  I have lein inside a directory in my **Dropbox** as well as all of my
   vim files and plugins. I then created soft links to them in my $HOME
   directory which makes this whole thing very easy to access from
   different systems as long as Dropbox is installed :)

.. |Vim and Clojure sitting on a tree| image:: http://dl.dropbox.com/u/102224/vim_clojure.png
