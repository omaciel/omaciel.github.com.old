Xml Performance Checklist
#########################
:slug: xml-performance-checklist
:date: 2005-08-09 13:38
:category: English
:tags: english

Straight from Microsoft’s `Improving .NET Application Performance and
Scalability: Improving XML
Performance <http://msdn.microsoft.com/library/en-us/dnpag/html/scalenetchapt09.asp>`__:

Design Considerations
~~~~~~~~~~~~~~~~~~~~~

Check

Description

\*

Choose the appropriate XML class for the job.

\*

Consider validating large documents.

\*

Process large documents in chunks, if possible.

\*

Use streaming interfaces.

\*

Consider hard-coded transformations.

\*

Consider element and attribute name lengths.

\*

Consider sharing the **XmlNameTable**.

Parsing XML
~~~~~~~~~~~

Check

Description

\*

Use **XmlTextReader** to parse large XML documents.

\*

Use **XmlValidatingReader** for validation.

\*

Consider combining **XmlReader** and **XmlDocument**.

\*

On the **XmlReader**, use the **MoveToContent** and **Skip** methods to
skip unwanted items.

Validating XML
~~~~~~~~~~~~~~

Check

Description

\*

Use **XmlValidatingReader**.

\*

Do not validate the same document more than once.

\*

Consider caching the schema.

Writing XML
~~~~~~~~~~~

Check

Description

\*

Use **XmlTextWriter**.

XPath Queries
~~~~~~~~~~~~~

Check

Description

\*

Use **XPathDocument** to process XPath statements.

\*

Avoid the // operator by reducing the search scope.

\*

Compile both dynamic and static XPath expressions.

XSLT Processing
~~~~~~~~~~~~~~~

Check

Description

\*

Use **XPathDocument** for faster XSLT transformations.

\*

Consider caching compiled style sheets.

\*

Consider splitting complex transformations into several stages.

\*

Minimize the size of the output document.

\*

Write efficient XSLT.

Atsushi Eno from the `Mono project <http://www.mono-project.com/>`__
took his time to write what he thinks `the “true” Checklists: XML
Performance <http://monkey.workarea.jp/lb/archive/2005/8-08.html>`__
should be. I can see how some of his (different as compared to
Microsoft’s recommendation) points could be valid based on his personal
experience but he confused me with his very first statement:

    Avoid XML as long as possible.

Will have to email him and clarify…

**UPDATE**: I did email Atsushi Eno and he graceously took the time to
answer some of my questions! Neat!
