Splitting WordPress Export File with ChoppedPress
#################################################
:slug: splitting-wordpress-export-file-with-choppedpress
:date: 2010-04-29 15:00
:category: English
:tags: english, lxml, python, optparse, wordpress

|Four Views of a Book Press by 802|

You’re all probably tired of hearing me talking about my script to split
the XML-like file that **WordPress** generates when you use the
**Export** feature. Tonight I have finally added the final touches to it
and can now share it here with you.

If you don’t remember, I wrote it because my good friend **Evandro**
from `QuartoEstudio.com <http://www.quartoestudio.com/en/>`__ is always
getting asked by some of his clients to migrate an existing web blog to
a new host/domain and hands him a tarball containing the exported
content of a **WordPress** blog in **XML** format. The problem resides
on the issue that some web hosting providers will limit how big a file
can be uploaded via a POST method, and depending on how big this XML
file is, you may have to manually break it into smaller files first.

Along the way I learned a bit more about
`OptParse <http://bit.ly/amtEtM>`__,
`LXML <http://codespeak.net/lxml/>`__ and `Beautiful
Soup <http://www.crummy.com/software/BeautifulSoup/>`__, so the entire
experience was very productive and fun. In the end, I solved my issue by
simple using the ***strip\_cdata=False*** argument to the **XMLParser**
class. Got to love when the solution is that simple!

So, without further ado, I present you
**ChoppedPress**\ (`download <https://bitbucket.org/omaciel/playground/raw/2e2a4cef1bac/choppedpress>`__)!
In the next few days (or weeks, depending on what my schedule looks
like) I will make it more robust and add more error handling, etc. In
the meantime, I hope you will find it useful.

.. code:: python

    # -*- coding: utf-8 -*-

    """
    Copyright (c) 2010, Og Maciel 

    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, are permitted
    provided that the following conditions are met:

        * Redistributions of source code must retain the above copyright notice, this list of
          conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright notice, this list
          of conditions and the following disclaimer in the documentation and/or other materials
          provided with the distribution.
        * Neither the name of the Og Maciel nor the names of its contributors may be used to
          endorse or promote products derived from this software without specific prior written
          permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    â€œAS ISâ€ AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
    CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
    NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """

    import os
    import sys

    try:
        from lxml import etree
    except ImportError:
        print "Please install lxml and try again: http://codespeak.net/lxml/"
        sys.exit(-1)

    from optparse import OptionParser

    # This is the default xml tag for wordpress
    WP_TAG = "/rss/channel/item"
    OUTFILE = "outfile"
    CHUNKSIZE = 2
    TMPFILE = "/tmp/template.xml"

    # Function found on ActiveState Code
    # Licensed under the PSF license
    # http://code.activestate.com/recipes/425397-split-a-list-into-roughly-equal-sized-pieces/
    def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])

        return newseq

    def chopit(xmlfile, outfile=OUTFILE, xmltag=WP_TAG, chunksize=CHUNKSIZE):
        parser = etree.XMLParser(resolve_entities=False, encoding="utf-8", strip_cdata=False)
        doc = etree.parse(xmlfile, parser)

        matches = doc.xpath(xmltag)
        print "Found %s blog posts!" % len(matches)
        matcheslist = split_seq(matches, chunksize)

        channel = doc.getroot().find('channel')

        # Create an empty wordpress xml file
        for e in matches:
            channel.remove(e)
        doc.write(TMPFILE, encoding="utf-8", method="xml", pretty_print=True)

        # Now, create smaller wordpress xml files
        ctr = len(matcheslist)
        print "Breaking WordPress XML into %s smaller files." % ctr
        for entities in matcheslist:
            doc = etree.parse(TMPFILE)
            channel = doc.getroot().find('channel')
            for entity in entities:
                channel.append(entity)

            output = '%s%03d.xml' % (outfile, ctr)
            doc.write(output, encoding='utf-8', method="xml", pretty_print=True)
            print " - File %s has %s posts." % (output, len(entities))
            ctr -= 1
        print "Done!"

    def main():

        description = "ChoppedPress lets you split the WordPress XML export file " 
        "into smaller files that can be used to import your posts, comments, tags" 
        " and categories into a new WordPress installation."

        usage = "Usage:  %prog  [[] [] []]"
        epilog = "Constructive comments and feedback can be sent to ogmaciel at gnome dot org."
        version = "%prog version 0.1"

        parser = OptionParser(usage=usage, description=description, epilog=epilog, version=version)
        parser.add_option('-i', '--infile', dest='infile', metavar='', help='The XML file generated by WordPress')
        parser.add_option('-o', '--outfile', dest='outfile', default='out', metavar='', help='The name for the smaller XML files. [default: %default]')
        parser.add_option('-t', '--tag', dest='tag', default='/rss/channel/item', help='The XML tag that represents your data. [default: %default]')
        parser.add_option('-n', '--number', dest='number', default=2, type=int, help='How many new files should be generated. [default: %default]')

        # Verify arguments
        (opts, args) = parser.parse_args()

        if not opts.infile:
            parser.print_help()
            sys.exit(-1)

        chopit(opts.infile, opts.outfile, opts.tag, opts.number)

    if __name__ == "__main__":
        main()

The usage should be pretty straight forward too:

.. code:: python

    $ python choppedpress
    Usage:  choppedpress  <INFILE> [[<OUTFILE>] [<TAG>] [<NUMBER>]]

    ChoppedPress lets you split the WordPress XML export file into smaller files
    that can be used to import your posts, comments, tags and categories into a
    new WordPress installation.

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -i , --infile=
                            The XML file generated by WordPress
      -o , --outfile=
                            The name for the smaller XML files. [default: out]
      -t TAG, --tag=TAG     The XML tag that represents your data. [default:
                            /rss/channel/item]
      -n NUMBER, --number=NUMBER
                            How many new files should be generated. [default: 2]

    Constructive comments and feedback can be sent to ogmaciel at gnome dot org.

If you have any constructive comment or suggestion, please drop me a
line or comment here.

.. |Four Views of a Book Press by 802| image:: http://bit.ly/aFbsJG
   :target: http://www.flickr.com/photos/802/85806375/
