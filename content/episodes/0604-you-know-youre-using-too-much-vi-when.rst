You know you're using too much Vi when...
#########################################
:slug: you-know-youre-using-too-much-vi-when
:date: 2007-07-19 19:55
:category:
:tags: english

… you press ESC after filling out web forms!

I really started using **Vim** full-time when I started working at
**rPath** last October. Every now and then I learn a new trick and I
figured I’d share them here, as well as make sure I can always search
for them later (talk about killing 2 birds with a stone!).

The first one if is for those times you want to make a generic search
and replace action on a file you’re working on. I learned a while back
that if I were searching for Foo and wanted to replace it with Bar, the
following command would do the trick:

    :%s/Foo/Bar/g

The problem is that this will replace every occurrence of the word Foo,
whether it is Foo, Foomatic, or Food! I have always wanted to know how
to make it so that I’d be prompted before making the change. My buddy
**Stu** showed me the trick. Just add a ‘c’ to the end of the command
and that is it!

    :%s/Foo/Bar/gc

The second trick, courtesy of Stu again, is how you can execute a
command while still inside Vim. I already knew how to run a command and
insert its output into the document currently open, but his trick was
useful for those occasions you want to test a piece of code you’re
working on. So, let’s say you’re working on a python code and wants to
test it. After you save it, still inside of Vim, execute:

    :! python %

This will execute your code, and once it is completed, prompt you to
either enter another command or just press ENTER to go back to Vim.

Sure, this is nothing Earth-shattering but it made my day! :)
