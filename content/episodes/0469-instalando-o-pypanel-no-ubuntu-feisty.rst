Instalando o PyPanel no Ubuntu Feisty
#####################################
:slug: instalando-o-pypanel-no-ubuntu-feisty
:date: 2007-02-10 20:36
:category:
:tags: portuguese

Acabei de instalar o Ubuntu Feisty Herd 3 (versao ainda em
desenvolvimento; apesar de estar rodando redondinho aqui, recomendo que
nao atualizem ate’ a versao final ser lancada oficialmente) no meu
computador, e ja’ de imediato instalei o
`OpenBox <http://icculus.org/openbox/>`__.Â  Para quem gosta de um
gerenciador de janelas bem “leve” e sem frescuras, eu realmente
recomendo.

Mas como eu geralmente tenho 10 desktops virtuais, e uso programas que
enviam notificacoes (por exemplo, quando alguem te manda uma mensagem de
chat, mas voce esta’ em outro terminal checando emails), sinto a
necessidade de ter uma area de notificacao para estes programas.Â  De
todos os paineis (leia barra) que eu conheco, o
`PyPanel <http://pypanel.sourceforge.net/>`__ e’ o que mais me agrada.Â 
Porem, faze-lo funcionar no Ubuntu nao e’ uma coisa muito direta, e
requere um pouco de “hacking”.Â  Existem varias fontes de informacao na
net, algumas indicando que voce remova os programas instalados pelo
gerenciador de pacotes (synaptic ou aptitude), e compile voce mesmo a
fonte.Â  Mas desta vez decidi dar uma colher de cha’ para o aptitude, e
decidi averiguar mais a fundo.

Logo depois de adicionar os repositorios universe e multiverse aos meus
repositorios (`saiba
como <http://wiki.ubuntu-br.org/GerenciamentoDePacotes>`__), e depois de
instalar o driver do nVidia (`saiba
como <http://wiki.ubuntu-br.org/InstalandoNvidia>`__), instalei os
seguintes programas:

-  libimlib2
-  libimlib2-dev
-  openbox
-  openbox-themes
-  pypanel

O legal de instalar o openbox-themes e’ que “ganhei” o
`obconf <http://tr.openmonkey.com/pages/obconf/>`__ de bonus! ;)Â  O
obconf te permite modificar temas, entre outras coisas, do OpenBox.

Sai entao do Gnome e escolhi o OpenBox como minha sessao padrao.Â 
Digitei minha senha na tela de log in e… pronto!Â  Na fracao de 1
segundo (fracao **MESMO**!) eu ja’ estava rodando o OpenBox!

Depois vou adicionar mais detalhes sobre como modificar o OpenBox para
obter um sistema mais personalizado, como adicionar um papel de fundo,
atalhos de teclado, etc.Â  Mas o pypanel e’ a bola da vez.

Executando pelo console o pypanel me mostrou o seguinte erro:

    omaciel@gorgonzola:~$ pypanel Traceback (most recent call last):
    File “/usr/bin/pypanel”, line 893, in <module> from Xlib import X,
    display, error, Xatom, Xutil File
    “/var/lib/python-support/python2.5/Xlib/display.py”, line 30, in
    <module> import protocol.display File
    “/var/lib/python-support/python2.5/Xlib/protocol/display.py”, line
    751 SyntaxError: Non-ASCII character ‘xf6’ in file
    /var/lib/python-support/python2.5/Xlib/protocol/display.py on line
    750, but no encoding declared; see
    `http://www.python.org/peps/pep-0263.html <http://www.python.org/peps/pep-0263.html>`__
    for details

A palavra chave para mim foi o “Non-ASCII character na linha 750.Â 
Abrindo o arquivo
/var/lib/python-support/python2.5/Xlib/protocol/display.py e checando a
linha 750 me mostrou o seguinte:

    # Bug reported by Ilpo NyyssÃ¶nen

O problema esta’ na letra **Ã¶**.Â  Como eu estava com pressa,
simplesmente mudei a letra para um o “normal”, salvei o arquivo, e
executei novamente o pypanel:

    omaciel@gorgonzola:~$ Traceback (most recent call last): File
    “/usr/bin/pypanel”, line 957, in <module> PyPanel(display.Display())
    File “/var/lib/python-support/python2.5/Xlib/display.py”, line 80,
    in \_\_init\_\_ self.display = \_BaseDisplay(display) File
    “/var/lib/python-support/python2.5/Xlib/display.py”, line 67, in
    \_\_init\_\_ apply(protocol.display.Display.\_\_init\_\_, (self, ) +
    args, keys) File
    “/var/lib/python-support/python2.5/Xlib/protocol/display.py”, line
    123, in \_\_init\_\_ self.default\_screen =
    min(self.default\_screen, len(self.info.roots) - 1) File
    “/var/lib/python-support/python2.5/Xlib/protocol/rq.py”, line 1371,
    in \_\_getattr\_\_ raise AttributeError(attr) AttributeError: roots

Caramba!!!Â  Foi ai’ que me lembrei de ter visto ha’ algum tempo uma
mensagem na net falando de um problema de tamanho de buffer neste mesmo
arquivo, mas do python2.5.Â  Me lembrei que o tamanho reservado estava
como 2048, mas precisava ser o dobro, 4096.Â  Mais uma vez abri o mesmo
arquivo e procurei pelo numero 2048, e encontrei a linha abaixo:

    recv = self.socket.recv(2048)

Como havia dito acima, editei esta linha, substituindo 2048 por 4096,
salvei o arquivo, e finalmente consegui executar o pypanel.

|openbox|

Nao podia faltar um screenshot da primeira vez usando a combinacao
Ubuntu Feisty + Openbox + Pypanel.Â  Logo, logo sai mais noticias… ;)

.. |openbox| image:: http://farm1.static.flickr.com/163/385691397_00104ffd4e.jpg
   :target: http://farm1.static.flickr.com/163/385691397_00104ffd4e_b.jpg
