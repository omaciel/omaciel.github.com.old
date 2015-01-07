Do you conary?
##############
:slug: do-you-conary
:date: 2007-02-05 23:38
:category:
:tags: portuguese

Hoje conversando com crimeboy no #ubuntu-br sobre Openbox, fiquei
salivando para usa-lo no trabalho, em meu Foresight Linux. Apesar que o
pacote do openbox ja’ existe para o Foresight, algumas ferramentas que
eu gosto de usar ainda nao estavam empacotadas. Para quem nunca
empacotou nada, isso deve gerar ate’ mesmo pesadelos… mas isso e’ porque
voces nao conhecem o sistema de gerenciamento de pacotes que usamos,
chamado **conary**:

O Conary Ã© um sistema distribuÃ­do de gerÃªncia de software, para
distribuiÃ§Ãµes Linux. Ele substitui soluÃ§Ãµes tradicionais de
gerÃªncia de pacotes (tais como RPM e dpkg) com uma abordagem projetada
para permitir uma colaboraÃ§Ã£o flexÃ­vel por meio da Internet.

O Conary permite que conjuntos de repositÃ³rios distribuÃ­dos e
frouxamente conectados definam os componentes que sÃ£o instalados em um
sistema Linux. Ao invÃ©s de usar uma distribuiÃ§Ã£o completa vinda de um
Ãºnico fabricante, ele permite que administradores e desenvolvedores
criem versÃµes derivadas (branches) de uma dada distribuiÃ§Ã£o, mantendo
as partes adequadas ao seu ambiente e ao mesmo tempo utilizando
componentes de outros repositÃ³rios na Internet.

Entao la’ fui eu empacotar o pypanel, que no Ubuntu infelizmente
continua quebrado. Tudo que foi necessario foi criar a minha “receita”:

    class PyPanel(PackageRecipe): name = ‘pypanel’ version = ‘2.4’
    buildRequires = [] def setup(r):
    r.addArchive(‘mirror://sourceforge/%(name)s/PyPanel-%(version)s.tar.gz’)
    r.PythonSetup()

Esta “receita” e’ bem simples e tem uma sintaxe bem “pythonica”.
Basicamente voce cria uma classe com o nome do pacote que voce esta’
gerando, e adiciona, na linha r.addArchive, a informacao de onde
encontrar a fonte do mesmo. Uma coisa bem legal e’ que, uma vez uma nova
versao do pacote saia, voce pode atualizar a variavel “version” e o
conary sabera’ onde pega-lo e atualizar tudo. Na verdade, a maioria das
“receitas” para programas que usam nomenclatura normal (pypanel usa
camel case, o que nao e’ certo) nem precisa modificar nada, ja’ que o
conary e’ esperto o suficiente para pegar a versao mais recente.

Depois de “cozinhar” a receita, o conary me fala que e’ melhor (e
recomendavel) adicionar as dependencias do pacote que ele sozinho
encontrou!!! Eu modifico mais uma vez a receita, desta vez adicionando
as dependencias:

    class PyPanel(PackageRecipe): name = ‘pypanel’ version = ‘2.4’
    buildRequires = [‘python-setuptools:python’, ‘freetype:devel’,
    ‘glibc:devel’, ‘imlib2:devel’, ‘libX11:devel’, ‘libXext:devel’,
    ‘libXft:devel’, ‘python-xlib:python’, ‘zlib:devel’] def setup(r):
    r.addArchive(‘mirror://sourceforge/%(name)s/PyPanel-%(version)s.tar.gz’)
    r.PythonSetup()

Agora e’ so’ fechar a tampa da panela e instalar o danado! Aproveitei e
empacotei mais outros pacotes que sao importantes para o pypanel
(infelizmente, estas dependencias tambem continuam quebradas no Ubuntu),
como o python-xlib e imlib2.

`|image0|\ |Screenshot| <http://farm1.static.flickr.com/135/380964427_ece56744b7_b.jpg>`__"
alt="openbox" />

Agora sim, isso e’ um sistema leve! :)

.. |image0| image:: <a%20href=
.. |Screenshot| image:: http://farm1.static.flickr.com/135/380964427_ece56744b7.jpg
