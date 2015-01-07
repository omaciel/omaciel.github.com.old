My Daily WTF
############
:slug: my-daily-wtf
:date: 2006-08-01 20:05
:category: English
:tags: english

I’ve been extremelly busy at work since my boss resigned about 3 weeks
ago.Ã‚Â  To worsen the situation, some other developer has also left,
leaving me as the new maintainer for his “legacy” application.Ã‚Â  The
so called “program” is entirely written in Java, acting as a “wrapper”
for Oracle and Sybase procedural code, written in PL/SQL and T-SQL
respectively.

It turns out that every quarter this application gets modified to
satisfy the new “business rules” that are “engineered” by the major
stakeholders in order to satisfy their needs.Ã‚Â  After several
iterations and undocumented modifications done to the program, the beast
has turn into a major, stinking “onion”, full of layer upon layer of
patches.

Well, it is that time of the year, and I am now in charge of supporting
this onion!Ã‚Â  There are so many sections of useless and non-sense code
that I could probably write a book on how not to write code!Ã‚Â  Today I
came across this beautiful “pearl” and just could not resist sharing it
with the world!Ã‚Â  ;)Ã‚Â  In case you fail to appreciate the “beauty”
of it, just keep moving along…Ã‚Â  Names have been removed to protect
the victims… no, not the author of this monstrosity, but the users, who
would probably throw themselves out their office’s window if they
learned about some of this stuff!Ã‚Â  :) **Line 34:**

    update costactual\_cip set phase = ‘\ **FandE**' where phase in
    ('Cm', 'Scope', 'Design', 'Construction', 'Contingency') and
    llwnumber in (select llwnumber from projectcip where llw\_type =
    '**RESOAP**\ ’);

**Line 570:**

    update costactual\_cip set phase = ‘Construction’ where phase in
    (‘Scope’, ‘Design’, ‘Cm’, ‘Contingency’, ‘\ **FandE**\ ’,
    ‘Unspecified’) and llwnumber in (select llwnumber from projectcip
    where llw\_type = ‘\ **RESOAP**\ ’);
