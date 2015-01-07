Brincando com o screen
######################
:slug: brincando-com-o-screen
:date: 2006-03-27 21:35
:category: English
:tags: portuguese

Depois de tomar uma surra configurando o meu postfix para funcionar na
modalidade de satelite (e nÃƒÂ£o como um servidor), finalmente consegui
graÃƒÂ§as ao MÃƒÂ¡rio partir para a prÃƒÂ³xima etapa: configurar o
acesso ÃƒÂ  meu email usando o `Mutt <http://www.mutt.org>`__ com
autenticaÃƒÂ§ÃƒÂ£o ÃƒÂ  base de sasl. Acredito que agora jÃƒÂ¡ estou
pronto para criar minha prÃƒÂ³pria “receita” caso eu precise fazer isso
novamente.

O motivo pelo qual eu me coloquei nesta posiÃƒÂ§ÃƒÂ£o foi devido ÃƒÂ s
restriÃƒÂ§ÃƒÂµes de acesso ÃƒÂ  internet da minha companhia. Tudo aqui
ÃƒÂ© super bloqueado e a maioria das portas sÃƒÂ£o bloqueadas… bem,
maioria, mas nÃƒÂ£o todas como eu descobri “por acidente” um dia destes.
Acontece que talvez por pressa do administrador ou por subestimarem seus
prÃƒÂ³prios usuÃƒÂ¡rios, tudo realmente foi bloqueado excepto pelas 2
portas mais ÃƒÂ³bvias: 80 e 443!!! Todo mundo que precisa acessar a net
tem seu browser (todos usam Internet Explorer… eu uso a versÃƒÂ£o
portÃƒÂ¡til do Firefox no meu thumb drive) configurado para usar o proxy
pela porta 91. Um dia, “P” da vida por nÃƒÂ£o poder acessar certos sites
de cÃƒÂ³digo, mudei minha configuraÃƒÂ§ÃƒÂ£o pra usar a porta 80 e
pronto! Liberdade quase que total! O ÃƒÂºnico problema era acessar
certas coisas como o IRC, IMAP email, e escutar internet rÃƒÂ¡dios!
Pouco a pouco fui descobrindo formas de burlar a “seguranÃƒÂ§a” mas
ainda faltava o acesso ÃƒÂ  meu email e toda a parefernalha que eu
geralmente uso para assinar meus emails, como o pgp. Andei perguntando
por aÃƒÂ­ e aparentemente nÃƒÂ£o existe um sistema via web para acessar
seu email e assinÃƒÂ¡-las com pgp…DaÃƒÂ­ o Mutt!

O que eu posso fazer agora ÃƒÂ© conectar no meu server usando Putty (no
trabalho uso windows 2000) e conecto em uma sessÃƒÂ£o que eu criei pelo
screen. Para quem nÃƒÂ£o conhece o screen, ele ÃƒÂ© um programa que te
permite iniciar sessÃƒÂµes virtuais que podem ser interrompidas,
mantidas “vivas”, e restauradas depois sem perda de dados. Um exemplo
seria quando vocÃƒÂª conecta em casa via ssh, resolve instalar algo, mas
antes que o processo possa terminar, decide que tem de desconectar para
fazer alguma outra coisa. Usando o screen vocÃƒÂª poderia entÃƒÂ£o
iniciar uma sessÃƒÂ£o virtual e dar-lhe um nome, como “apt-get remoto”
por exemplo.

    screen -S “apt-get remoto”

VocÃƒÂª notarÃƒÂ¡ que seu console vai mudar para uma nova tela virtual…
Agora vocÃƒÂª inicia o processo que queira da forma normal…Ã‚Â  Vamos
pretender que queremos fazer um apt-get upgrade do sistema.

    sudo apt-get update sudo apt-get upgrade

Neste exato momento, seu chefe entra em seu escritÃƒÂ³rio e de joelhos
implora para que vocÃƒÂª o ajude a remover o Windows e instalar Ubuntu
Dapper Drake (para que ele possa se gabar de ser l33t h4x0r depois). Mas
vocÃƒÂª nÃƒÂ£o quer deixar sua instalaÃƒÂ§ÃƒÂ£o executando sozinha…
VocÃƒÂª poderia trancar seu pc e deixar o processo executando… mas
vocÃƒÂª se considera l33t tambÃƒÂ©m e quer aproveitar a ocasiÃƒÂ£o para
exibir para o chefe os seus skillz. VocÃƒÂª simplesmente clica a
combinaÃƒÂ§ÃƒÂ£o CRTL + “a” (apertando as teclas CTRL e A juntas ao
mesmo tempo e soltando-as), “d” e pronto. Sua sessÃƒÂ£o “apt-get remoto”
continua ativa mas agora estÃƒÂ¡ em segundo plano. A diferenÃƒÂ§a entre
fazer isso com o screen e enviar um processo para o segundo plano
(usando bg ou CTRL + Z por exemplo) ÃƒÂ© que caso vocÃƒÂª desconecte da
sua sessÃƒÂ£o ssh inicial, a sessÃƒÂ£o “apt-get remoto” continua ativa e
pode ser re-conectada depois a qualquer momento. Vamos entÃƒÂ£o assumir
que durante o tempo que vocÃƒÂª esteve fora de seu escritÃƒÂ³rio,
alguÃƒÂ©m resolveu desligar o seu pc para poder conectar o microondas e
fazer pipoca! NÃƒÂ£o tem problema! Assim que vocÃƒÂª pegar um pouco de
pipoca como consolo pelos danos causados, conecte seu pc e entre
novamente em seu pc remoto via ssh. Como nÃƒÂ³s sabemos o nome da
sessÃƒÂ£o do screen, podemos re-conectar usando o comando:

    screen -r “apt-get remoto”

e para a surpresa de todos, se o processo de atualizar o seu pc ainda
nÃƒÂ£o estiver acabado, vocÃƒÂª poderÃƒÂ¡ acompanha o desenvolvimento
como se nada tivesse acontecido.

Legal mesmo ÃƒÂ© usar o screen para acessar seu email (como eu faÃƒÂ§o
agora usando o Mutt) ou atÃƒÂ© mesmo entrar no IRC usando algo como o
BitchX! Existem muitas outras coisas legais que podem ser feitas pelo
screen (como trabalhar em um arquivo ao mesmo tempo com outra pessoa de
forma interativa), mas isso provavelmente vai virar um outro post. Para
mais detalhes, cheque o man pages… e para animar os interessados, abaixo
seguem alguns comandos para serem usados no screen. Divirtam-se!

    screen -r: re-conecta screen -x: sessÃƒÂ£o compartilhada screen
    -list: lista de todas sessÃƒÂµes screen abertas screen -r

JÃƒÂ¡ dentro do screen:

    ctrl + a, c - cria uma nova sessÃƒÂ£o screen ctrl + a, ctrl + a -
    alternar entre sessÃƒÂµes ctrl + d - desconecta de uma sessÃƒÂ£o
    (sem finalizÃƒÂ¡-la) ctrl + [nÃƒÂºmero] - pula para janela x ctrl +
    ” - menu interativo listando todas sessÃƒÂµes
