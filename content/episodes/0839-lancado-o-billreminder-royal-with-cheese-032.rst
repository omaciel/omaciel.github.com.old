Lançado o BillReminder "Royale with cheese" 0.3.2
##################################################
:slug: lancado-o-billreminder-royal-with-cheese-032
:date: 2008-09-12 00:19
:category: English
:tags: portuguese

|BillReminder|

É com um enorme prazer que venho anunciar o lançamento do
`BillReminder <http://billreminder.gnulinuxbrasil.org>`__ **“Royale with
cheese”** versão **0.3.2**! Este lançamento teve como foco principal
consertar erros (bugs), adicionar mais traduções, e preparar o terreno
para futuros recursos de relatórios.

Diretamente do arquivo NEWS:

**Bugs**:

-  Paid/Not Paid entries exist in File and Edit menus; Make them
   toggle/untoggle appropriately (Bug
   `#13 <http://code.google.com/p/billreminder/issues/detail?id=13>`__)
-  Issues with date and time locale? (Bug
   `#12 <http://code.google.com/p/billreminder/issues/detail?id=12>`__)
-  Ambiguity with Alerts and Alarms in preferences dialog (Bug
   `#11 <http://code.google.com/p/billreminder/issues/detail?id=11>`__)
-  Make category names a unique field. (Bug
   `#1 <http://code.google.com/p/billreminder/issues/detail?id=1>`__)
-  Newly added categories should be selected automatically (Bug
   `#2 <http://code.google.com/p/billreminder/issues/detail?id=2>`__)
-  Make setting an alarm really optional. (Bug
   `#4 <http://code.google.com/p/billreminder/issues/detail?id=4>`__)

**Backend**:

-  Changed BillReminder to use GConf for is configuration values. Thanks
   **Wilson Pinto Junior**
-  Changed BillReminder’s command line parsing to use OptionParser. (Bug
   `#3 <http://code.google.com/p/billreminder/issues/detail?id=3>`__)

**Translations**:

-  cs.po:  Pavel Šefránek
-  de.po:  Lorenz
-  en\_CA.po:  Stuart Read
-  en\_GB.po:  Jen Ockwell
-  es.po:  Ramón Calderón
-  fi.po:  Ilkka Tuohela
-  fr.po:  Robert-André Mauchin
-  he.po:  Yaron
-  hr.po:  Mario Đanić
-  hu.po:  HORVATH, Akos
-  it.po:  Sergio Zanchetta
-  nb.po: Tommy Mikkelsen
-  nl.po:  Martijn Cielen
-  pl.po:  Tomasz Z. Napierala
-  pt\_BR.po:  Djavan Fagundes and Vladimir Melo
-  pt.po:  Susana Pereira
-  ro.po:  Ionuț Jula
-  ru.po:  Ilya B
-  sl.po:  Martin
-  sv.po:  Daniel Nylander
-  tl.po:  Jerome S. Gotangco
-  tr.po:  Rail Aliev

**Graphical Interface**:

-  Mnemonic labels/widgets and HIG work done to dialogs. Thanks **Wilson
   Pinto Junior**
-  Ask user for confirmation before editing an existing category.
-  Added pycairo as a dependency instead of python-Image. Color-coded
   categories now have a border around the colored tile.

**General**:

-  Renamed MANTAINERS to MAINTAINERS
-  Added uninstall method and versioning via autotools (Bug
   `#547768 <http://bugzilla.gnome.org/show_bug.cgi?id=547768>`__)

O código fonte pode ser encontrado na página de
`downloads <http://billreminder.gnulinuxbrasil.org/?page_id=26>`__ como
também um pacote para o Ubuntu. Por gentileza, relate qualquer problema,
comentários ou pedidos de recursos na página do
`Bugzilla <http://bugzilla.gnome.org/enter_bug.cgi?product=billreminder>`__
do projeto.

.. |BillReminder| image:: http://farm1.static.flickr.com/155/426001389_82fe3885b7_m.jpg
   :target: http://www.flickr.com/photos/ogmaciel/426001389/
