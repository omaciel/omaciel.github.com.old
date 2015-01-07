Instalando o Enlightenment 17 no Ubuntu
#######################################
:slug: instalando-o-enlightenment-17-no-ubuntu
:date: 2006-09-17 21:10
:category: English
:tags: portuguese

Uma receitazinha para nao perder o costume. :) Eu sempre estive
interessado em experimentar o
`Enlightenment <http://enlightenment.sourceforge.net/>`__ DR17, um
gerenciado de janelas famoso por ser bem elegante e conter bastante
efeitos graficos. O problema e’ que a versao atual, DR16, esta’
demorando muito para ser empacotada e liberada com os recursos que a
versao em desenvolvimento, DR17, oferece. Semana passada, conversando
com o Julio Valsesia pelo IRC, ele me passou um repositorio que ja’
possui os pacotes do DR17 para o Dapper e Edgy.

Para efetuar a instalacao, basta adicionar o novo repositorio em seu
arquivo /etc/apt/sources.list

    deb
    `http://edevelop.org/pkg-e/ubuntu <http://edevelop.org/pkg-e/ubuntu>`__
    dapper e17

seguido de:

    wget
    `http://lut1n.ifrance.com/repo\_key.asc <http://lut1n.ifrance.com/repo_key.asc>`__
    sudo apt-key add repo\_key.asc sudo aptitude update sudo aptitude
    install e17

Pronto! Os dois primeiros comandos sao necessarios para adicionarmos a
chave publica do repositorio em seu computador, e assim permitir que o
aptitude (ou apt-get) “confie” nos pacotes do novo repositorio.

Para testar o Enlightenment, saia do Gnome e escolha-o da lista nas
opcoes de sessoes. Depois de uma olhada no site
`Get-E.org <http://www3.get-e.org/>`__ para pegar uns temas e wallpapers
legais, incluindo um wallpaper animado!

Uma coisa que ainda nao descobri como resolver e’ uma forma de mudar a
acentuacao do teclado, ja’ que no Gnome eu uso um applet que me permite
fazer isso com um atalho de teclado.

Claro que nao podia faltar uns screenshots.

`Screenshot
1 <http://static.flickr.com/95/245803474_44bc44d59b_b.jpg>`__:

|image0|

`Screenshot
2 <http://static.flickr.com/92/245803475_09d96e18f3_b.jpg>`__:

|image1|

**Atualizacao**: Observe o novo repositorio (valeu slipttees) e
consequentemente uma nova chave a ser importada.

.. |image0| image:: http://static.flickr.com/95/245803474_44bc44d59b.jpg
.. |image1| image:: http://static.flickr.com/92/245803475_09d96e18f3.jpg
