VocÃª quer aprender a traduzir os programas do Linux?
#######################################################
:slug: voce-quer-aprender-a-traduzir-os-programas-do-linux
:date: 2007-06-24 23:10
:category: English
:tags: portuguese

Quase todos os dias eu encontro alguÃ©m que acabou de experimentar o
Linux pela primeira vez… e a grande maioria destas pessoas, ainda
(talvez) curtindo um pouco desta adrenalina que acontece com todos que
experimentam o potencial do software livre, me falam:

    "Og, eu gostaria muito de poder retribuir com esta comunidade, mas
    nÃ£o sei programar!"

Bem, seus problemas estÃ£o solucionados entÃ£o! A maioria das pessoas
que me conhecem sabem que apesar de trabalhar como programador, minha
maior participaÃ§Ã£o/contribuiÃ§Ã£o com a comunidade de software livre
tem sido com traduÃ§Ãµes e advocacia! Ou seja, vocÃª nÃ£o precisa ser um
excelente programador ou ser um nerd para ajudar!

    "Mas Og, eu nÃ£o sei por onde comeÃ§ar / tenho preguiÃ§a de ler toda
    a documentaÃ§Ã£o / nÃ£o entendo bulufas!"

Mais uma vez, seus problemas serÃ£o resolvidos meus amigos. Aproveitando
um momento de (i)lucidez causado pelo forte calor e humidade aqui na
Carolina do Norte, estou me propondo a ensinar 3 ou mais pessoas a
trabalharem com as traduÃ§Ãµes dos manuais dos programas do GNOME! Sabe
aquelas vezes que vocÃª fica na dÃºvida de como um certo programa ou
recurso funciona, e quando se aventura a ler a documentaÃ§Ã£o, fica
decepcionado por ver tudo escrito em inglÃªs? Pois Ã©… quer melhor forma
de contribuir com a comunidade que te trouxe estes programas? VocÃª
sonha em ver seu nome associado Ã  documentaÃ§Ã£o de algo que
ajudarÃ¡ literalmente milhares de pessoas? EntÃ£o venha comigo…

A minha lista de documentos a serem traduzidos Ã© bem pequena, e olha
que um deles contÃ©m somente 20 frases (ou “strings” como sÃ£o
conhecidos pelos tradutores)! As “tarefas” serÃ£o distribuÃ­das por
ordem de pedido via um comentÃ¡rio aqui no meu blog. Durante este
perÃ­odo estarei completamente ao dispor destes voluntÃ¡rios
selecionados, seja por e-mail, mensageiro instantÃ¢neo, ou Skype, para
ajudÃ¡-los a completar suas tarefas.

A primeira coisa que vocÃªs precisam fazer Ã© escolher dentre os
seguintes documentos:

-  `GNOME Control
   Center <http://l10n.gnome.org/POT/gnome-control-center.HEAD/docs/help.HEAD.pot>`__
-  `GNOME 2.14 Desktop System Administration
   Guide <http://l10n.gnome.org/POT/gnome-user-docs.HEAD/docs/system-admin-guide.HEAD.pot>`__
-  `Bug
   Buddy <http://l10n.gnome.org/POT/bug-buddy.HEAD/docs/help.HEAD.pot>`__

Ao clicar nos links acima, vocÃª vai abrir um arquivo em formato de
texto simples. Este arquivo, chamado de catÃ¡logo de mensagens, contÃ©m
nada mais, nada menos que todas as mensagens que sÃ£o exibidas pelo
programa. O que acontece Ã© que estas mensagens uma vez traduzidas, sÃ£o
entÃ£o compiladas e distribuÃ­das junto com o programa, para que os
mesmos possam ser utilizados em uma lingua/idioma que nÃ£o seja a
linguagem original.

    "Uhhh… como?"

Vamos dar uma olhada no primeiro documento chamado GNOME Control Center.
Clique no link acima, e salve este arquivo, mantendo seu nome original.
Agora, abra o seu editor de texto favorito e olhe as seguintes linhas:

.. code::

    #: C/control-center.xml:11(para)

    msgid "The GNOME Control Center provides a central place for the user to setup their GNOME experience. It can let you configure anything from the behavior of your window borders to the default font type."

    msgstr ""

Gostaria de chamar a sua atenÃ§Ã£o para a linha que comeÃ§a com a
palavra **msgid**. Este marcador indica que a(s) prÃ³xima(s) linha(s)
representa(m) uma mensagem que Ã© exibida pelo programa durante sua
execuÃ§Ã£o, ou no caso de manuais, quando vocÃª procurar no menu de
ajuda.

Agora, olhe a linha que comeÃ§a com a palavra **msgstr**. Este marcador
indica aos tradutores (e durante a fase de compilar as traduÃ§Ãµes) onde
sua traduÃ§Ã£o deve ser feita. EntÃ£o, no caso da frase acima, vocÃª
adicionaria sua traduÃ§Ã£o dentro das aspas logo apÃ³s o marcador
**msgstr**, ficando assim:

.. code::

    #: C/control-center.xml:11(para)

    msgid "The GNOME Control Center provides a central place for the user to setup their GNOME experience. It can let you configure anything from the behavior of your window borders to the default font type."

    msgstr "O Controle Central do GNOME Ã© um local onde vocÃª poderÃ¡ configurar o seu ambiente do GNOME. Blah blah balh..."

    "Mas Og, vocÃª nÃ£o traduziu ao pÃ© da letra!"

Sim, mas foi de propÃ³sito mesmo… Ã‰ importante lembrar que nÃ£o estamos
trabalhando em uma documentaÃ§Ã£o que serÃ¡ usada por cientistas e
robos, mas sim por usuÃ¡rios que provavelmente nunca viram nada
semelhante. Sou da opiniÃ£o que mais vale um documento claro e fÃ¡cil de
se entender, do que aqueles manuais super complicados que a grande
maioria joga fora!

Bem, estes arquivos de mensagens sÃ£o bem parecidos e uma vez vocÃª
entenda como um “funciona”, o resto Ã© resto. Ainda existe todo um
processo de verificaÃ§Ã£o do arquivo final, e algumas outras formas de
editar estes arquivos sem o uso de um editor de texto, mas vou deixar
este assunto para conversar com os voluntÃ¡rios que se comunicarem
comigo. Claro que terei o maior prazer em responder qualquer pergunta
feita aqui ou enviada por e-mail.

    "Mas Og, eu nÃ£o me sinto muito fluente em inglÃªs… e agora?"

Mais importante que traduzir um documento Ã© revisÃ¡-lo por erros de
gramÃ¡tica, ortografia, ou atÃ© mesmo ver se o texto faz sentido! Essas
pessoas que nÃ£o sabem bem o inglÃªs mas lembram-se de todas aquelas
regrinhas que aprendemos na escola sÃ£o **fundamentais** para qualquer
equipe de traduÃ§Ã£o! Eu mesmo devo ter escrito coisas medonhas nos
parÃ¡grafos acima, mas felizmente posso culpar meus 16 anos nos Estados
Unidos! hehehe

EntÃ£o Ã© isso aÃ­! Os interessados a participar deste projeto podem
primeiro ler os comentÃ¡rios aqui (para ver se alguÃ©m jÃ¡ se encarregou
de trabalhar em um dos arquivos. Depois, baixem o arquivo usando os
links acima e me avisem sobre seu interesse. O prÃ³ximo passo seria
combinar uma reuniÃ£o (dou preferÃªncia a reuniÃµes pelo Skype) com
todos para acertarmos a pontaria e responder a qualquer dÃºvida que
aparecer.

**Let the games begin!**
