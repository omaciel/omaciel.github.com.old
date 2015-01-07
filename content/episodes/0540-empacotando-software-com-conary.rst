Empacotando software com Conary
###############################
:slug: empacotando-software-com-conary
:date: 2007-04-26 01:49
:category:
:tags: portuguese

Muitas pessoas jÃ¡ tinham me pedido para escrever um pequeno tutorial
sobre como empacotar software para o `Foresight
Linux <http://www.foresightlinux.org/pt/>`__. Para quem ainda nÃ£o
conhece o sistema de gerenciamento de pacotes
`Conary <http://wiki.rpath.com/wiki/Conary>`__, uma forma de
descrevÃª-lo seria comparÃ¡-lo com um sistema de controle de versÃµes e
gerenciamento de pacotes. Isso quer dizer que vocÃª tem um controle
sobre as modificaÃ§Ãµes do cÃ³digo no mesmo estilo do CVS ou SVN, e
qualquer modificaÃ§Ã£o feita pelo mantenedor do cÃ³digo original Ã©
implementado em seu pacote em fragmentos, equivalentes Ã s linhas que
foram adicionadas ou modificadas.

Agora que estou lendo o parÃ¡grafo acima, notei que a explicaÃ§Ã£o nÃ£o
foi muito bem feita. Quem sabe um exemplo mais simples ajudaria a causa?

Imagine entÃ£o que vocÃª instalou seu programa preferido de ler fontes
de notÃ­cias RSS. Beleza! Vamos entÃ£o imaginar que amanhÃ£ o
desenvolvidor/mantenedor deste programa descobre um erro, e rapidamente
modifica **uma linha** de seu cÃ³digo para consertar este bug. Note a
Ãªnfase em **uma linha**. Eu, como desenvolvidor do Foresight empacoto
esta versÃ£o e a habilito em nossos repositÃ³rios para consumo geral.
Quando um usuÃ¡rio atualizar seu sistema, ele estarÃ¡ baixando o
equivalente Ã  aquela **uma linha** de cÃ³digo… e sÃ³! Em qualquer outro
sistema de empacotamento, vocÃª tem de baixar o cÃ³digo (compilado) do
programa inteiro para atualizar, mas o Conary te permite atualizar
somente a diferenÃ§a (diff)!

Bem, vamos entÃ£o imaginar que vocÃª estÃ¡ preparado para empacotar algo
usando o Conary. Existem alguns passos importantes que sÃ£o necessÃ¡rios
antes de vocÃª poder empacotar, mas vou deixar estes detalhes para um
prÃ³ximo artigo. Por agora, vou usar o meu prÃ³prio programa,
`BillReminder <http://billreminder.sourceforge.net/>`__, como exemplo.

BillReminder Ã© um cÃ³digo escrito em python e pygtk, atualmente
hospedado no SourceForge.net. A versÃ£o atual disponibilizada para
download Ã© a versÃ£o 0.1.1. O motivo porque estou mencionando isso
ficarÃ¡ mais claro em alguns segundos.

Para empacotar qualquer coisa com o Conary, tudo que vocÃª precisa fazer
Ã© criar um arquivo com instruÃ§Ãµes sobre onde e como conseguir o
cÃ³digo fonte, entre outras coisas. Este arquivo, conhecido pelas
pessoas acostumados com o Conary como “recipe”, ou “receita” em
portuguÃªs, possui uma sintaxe bem “pythÃ´nica”, simples e clara. Segue
abaixo minha pequena receita:

    class BillReminder(PackageRecipe): name = ‘billreminder’ version =
    ‘0.1.1’ buildRequires = [] def setup(r):
    r.addArchive(‘mirror://sourceforge/%(name)s/’) r.PythonSetup()

Este modelo de receita Ã© bem bÃ¡sico, especial para empacotar programas
escritos em python. Note as informaÃ§Ãµes bÃ¡sicas, como nome, versÃ£o,
e localizaÃ§Ã£o do cÃ³digo fonte. Devido ao seu “sabor” de python,
podemos utilizar de expansÃ£o de variÃ¡veis para criar um URL dinÃ¢mico.
a linha

    r.addArchive(‘mirror://sourceforge/%(name)s/’)

entÃ£o Ã© “traduzida” para: baixe a fonte em algum mirror do
sourceforge.net, e procure pelo programa %(name)s, ou seja,
billreminder. O sistema conary consegue “adivinhar” de forma lÃ³gica
qual o pacote fonte para baixar, utilizando o nome e a versÃ£o para
distinguir de qualquer outro programa ou versÃ£o disponÃ­vel no mesmo
local. Se vocÃª fosse entÃ£o empacotar outro programa que tambÃ©m
estivesse hospedado no Sourceforge.net, bastaria vocÃª modificar a
variÃ¡vel “name” e “version”. Caso o cÃ³digo fonte estivesse em um outro
servidor (sem mirrors), vocÃª modificaria o URL.

    r.addArchive(‘http://[servidor]/%(name)s/’)

Depois de fazer e salvar nossa receita como billreminder.recipe (o final
do nome do arquivo tem de ser .recipe), Ã© hora de “cozinharmos”.
Geralmente, vocÃª “cozinha” sua receita 2 vezes. Na primeira vez, o
sistema conary irÃ¡ baixar o cÃ³digo fonte, compilÃ¡-lo, e completamente
(e automaticamente) nos informar sobre todas as dependÃªncias
necessÃ¡rias para empacotar o programa. Rodando o comando:

    cvc cook billreminder.recipe

nos devolve, entre muitas linhas de saÃ­da, a seguinte lista de
dependÃªncias:

    'python-setuptools:python', 'dbus-python:python',
    'desktop-file-utils:runtime', 'notify-python:python',
    'pygobject:python', 'pygtk:python', 'python-sqlite:python'

Ou seja, estes sÃ£o os nomes dos pacotes e componentes requeridos pelo
BillReminder. Editamos mais uma vez nossa “receita”, adicionando as
dependÃªncias na variÃ¡vel “buildRequires”.

    class BillReminder(PackageRecipe): name = ‘billreminder’ version =
    ‘0.1.1’ buildRequires = [‘python-setuptools:python’,
    ‘dbus-python:python’, ‘desktop-file-utils:runtime’,
    ‘notify-python:python’, ‘pygobject:python’, ‘pygtk:python’,
    ‘python-sqlite:python’] def setup(r):
    r.addArchive(‘mirror://sourceforge/%(name)s/’) r.PythonSetup()

e cozinhamos mais uma vez com o mesmo comando anterior. Depois de mais
alguns minutos, um arquivo contendo o programa compilado e todos os
arquivos por ele usado serÃ¡ gerado. O nome deste arquivo Ã© geralmente
formado pelo nome do programa, billreminder, e a versÃ£o, 0.1.1,
separados por um hÃ­fen, e terminando com um “.css”. Para instalar o
programa, basta agora usar o conary.

sudo conary update billreminder-0.1.1.css

e pronto! Como eu tinha mencionado antes, existem algumas coisas que eu
nÃ£o mencionei aqui, coisas que te ajudam a disponibilizar este pacote
em um repositÃ³rio para que outros possam consumÃ­-lo. Prometo que vou
detalhar estes detalhes em um prÃ³ximo artigo, mas sÃ³ para terminar o
processo, uma vez que seu pacote esteja em um repositÃ³rio, outras
pessoas poderÃ£o instalÃ¡-lo usando somente o nome do pacote (sem a
versÃ£o e o .css).

Uma outra coisa muito interessante do conary, Ã© o novo recurso de
“cozinhar” cÃ³digo diretamente de um repositÃ³rio SVN, CVS, ou
Mercurial. Este recurso foi lanÃ§ado ainda ontem (conary versÃ£o 1.1.23)
e eu jÃ¡ tenho planos de empacotar o BillReminder desta forma.

Bem, espero nÃ£o ter sido muito tÃ©cnico ou vago neste artigo. Ainda
estou aprendendo sobre o conary, e pretendo descrever em meu blog mais
detalhes desta fascinante tecnologia!
