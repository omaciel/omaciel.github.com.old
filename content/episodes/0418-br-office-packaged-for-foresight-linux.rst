BR-Office empacotado para o Foresight Linux
###########################################
:slug: br-office-packaged-for-foresight-linux
:date: 2006-10-13 19:25
:category: English
:tags: portuguese

Aproveitei o dia hoje para empacotar o
`Br-Office <http://openoffice.org.br/>`__ para o `Foresight
Linux <http://www.foresightlinux.com/>`__!!! Como podem ver, esta’
rodando “redondinho”! :) No processo de empacota-lo, acabei descobrindo
um `bug <http://issues.rpath.com/browse/RPL-713>`__ no glibc. Mas o
pessoal da rPath ja’ tinha um patch e assim que o glibc for arrumado e
for liberado no repositorio oficial, voces poderao usufruir do Br-Office
tambem.

|image0|

Para instala-lo:

    sudo conary update broffice.org

Caso voce ainda tenha a versao oficial do OpenOffice instalado, nao se
esqueca de remove-lo:

    sudo conary update broffice.org -openoffice.org

.. |image0| image:: http://static.flickr.com/92/268734323_fc5248714f.jpg
   :target: http://static.flickr.com/92/268734323_fc5248714f_b.jpg
