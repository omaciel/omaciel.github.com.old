Criando seu prÃƒÂ³prio Multi-Boot Pendrive
##############################################
:slug: criando-seu-proprio-multi-boot-pendrive
:date: 2006-02-15 20:57
:category: English
:tags: portuguese

Estou tÃƒÂ£o acostumado a usar Linux que passo aperto quando visito
pessoas que ainda usam Windows… Muitas vezes me pego procurando pelo
console ou algum programa do Linux para fazer algo, e acabo perdendo um
bom tempo procurando uma soluÃƒÂ§ÃƒÂ£o nÃƒÂ£o-open source. Comecei
entÃƒÂ£o a carregar comigo (levei comigo quando fui ao Brasil no ano
passado) um pendrive SanDisk carregado de programas portÃƒÂ¡teis para
facilitar a transiÃƒÂ§ÃƒÂ£o… Programas como o Putty, e o Firefox e
Thunderbird portÃƒÂ¡teis sÃƒÂ£o indispensÃƒÂ¡veis nestas horas! Mas, e
se vocÃƒÂª quisesse usar o Linux de forma portÃƒÂ¡til? Claro que existem
versÃƒÂµes “Live” do Linux (Knoppix, Damn Small Linux, Ubuntu, etc), mas
eu queria algo mais simples ainda… E se eu estivesse em algum lugar onde
eu nÃƒÂ£o tivesse acesso ao CD-ROM? Como a maioria destes Live CDs
precisam ser boot-ados para iniciar o sistema operacional, vocÃƒÂª
nÃƒÂ£o teria mais opÃƒÂ§ÃƒÂµes… A nÃƒÂ£o ser que houvesse uma forma de
iniciar uma sessÃƒÂ£o de Linux **dentro do Windows**!!! Procurei online
e achei uma receita legal para fazer isso, usando o `Damn Small
Linux <http://www.damnsmalllinux.org/>`__ (DSL). Vamos lÃƒÂ¡ entÃƒÂ£o…

O que vocÃƒÂª precisa:

-  USB pendrive / chaveiro, 64 MB ou mais (preferÃƒÂªncia por 128);
-  Um computador que pode ser inicado pelo USB e CD-ROM, com pelo menos
   100MB livres de disco;
-  O
   `ISO <ftp://distro.ibiblio.org/pub/linux/distributions/damnsmall/current/current.iso>`__
   do DSL e o arquivo compactado do `DSL
   embedded <http://distro.ibiblio.org/pub/linux/distributions/damnsmall/current/>`__;
-  Muita paciÃƒÂªncia!

Procedimento:

-  "Queime" o arquivo .iso em um CD;
-  Conecte seu pendrive em seu computador;
-  Re-inicie seu sistema com este novo CD na bandeja do CD-ROM;
-  Agora vamos completamente **formatar** seu pendrive e colocar o linux
   bootloader!!!

#. Clique em qualquer lugar da ÃƒÂ¡rea de trabalho (desktop) em seu
   computador;
#. Selecione Apps —> Tools —> Install to USB pendrive —> For USB-HDD
   pendrive;
#. Siga as intruÃƒÂ§ÃƒÂµes do assistente e no final vocÃƒÂª terÃƒÂ¡ o
   DSL instalado e pronto para ser usado!

-  Agora vamos adicionar o toque final e acrescentar um emulador (QEMU)
   no pendrive! Isso vai te permitir iniciar o DSL dentro de uma janela,
   em ambos Linux e Windows!

#. Inicie seu computador de volta para o seu sistema normal;
#. Agora, descompacte o arquivo dsl-embedded.zip no arquivo root de seu
   pandrive, sobrescrevendo o que o USB-HDD fez (tudo que querÃƒÂ­amos
   do USB-HDD era criar o boot sector);
#. Agora vocÃƒÂª deveria ter 2 scripts no diretÃƒÂ³rio root de seu
   pendrive: dsl-windows.bat e dsl-linux.sh

Dependendo de qual arquivo vocÃƒÂª abrir, e qual o sistema operacional
que vocÃƒÂª estiver usando, a versÃƒÂ£o do QEMU apropriada
serÃƒÂ¡ executada e DSL iniciarÃƒÂ¡ dentro de uma janela, utilizando
todas configuraÃƒÂ§ÃƒÂµes do sistema hÃƒÂ³spede (ex: rede, som, etc)
como se fossem dele mesmo!

Este truque merece um prÃƒÂªmio! ;)

**Obs**: Obrigado **Lucas** por ter me passado um link melhor para o
.iso! ;)

**Obs2**: Obrigado **Guilherme** por me avisar sobre o link quebrado
para o DSL Embedded!Ã‚Â  ;)


