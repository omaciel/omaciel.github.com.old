Pare pra' pensar, pense muito bem!
##################################
:slug: pare-pra-pensar-pense-muito-bem
:date: 2007-02-11 19:38
:category: English
:tags: portuguese

Continuando com a saga de personalizar a minha instalacao do Openbox, a
primeira coisa que eu geralmente faco e’ criar um script contendo os
programas e as configuracoes que eu quero ter ao iniciar a sessao. O
script nao tem nada de avancado, e simplesmente contem comandos bem
simples, terminados com o simbolo “&” para que eles possam ter “vida
propria” depois que o script for executado.

Primeiro, eu criei meu script (chamado startOpenBox) em meu diretorio
pessoal, e adicionei os seguintes comandos:

    #!/bin/bash gnome-settings-daemon & gnome-volume-manager &
    gnome-power-manager & Esetroot -s ~/images/wallpaper.png & pypanel &
    update-notifier & exec openbox

Note que o comando de abrir o openbox e’ o ultimo a ser executado, e que
o mesmo possui o comando “exec”. Outra coisa que estou fazendo e’
aproveitando certos comandos do Gnome para usufruir de certos recursos,
como a deteccao e auto-montagem de despositivos externos, gerenciamento
de energia (para laptops, por exemplo), e aspectos de estetica do gtk. O
papel de fundo e’ definido com o comando Esetroot (minha escolha
pessoal, mas existem outros metodos), e o sistema de notificacao de
atualizacoes (update-notifier) me deixa saber quando alguma coisa nova
aparece. A unica “regra” e’ que a ultima linha deve conter o exec
openbox, mas de resto, o ceu e’ o limite!

Depois e’ necessario fazer este script reconhecido e carregado toda vez
que voce iniciar sua sessao usando Openbox. Para tanto, vamos primeiro
modificar o arquivo que o gerenciador de sessoes (gdm) usa, localizado
em */usr/share/xsessions/openbox.desktop*, e modificando a linha:

    Exec=openbox

para

    Exec=startOpenBox

Agora, vamos colocar o nosso escript em um caminho “conhecido” pelo seu
sistema e torna-lo executavel:

sudo cp ~/startOpenBox /usr/local/bin/startOpenBox sudo chmod +x
/usr/local/bin/startOpenBox

Pronto! Agora toda vez que voce iniciar sua sessao, seu sistema estara’
todo personalizado e usufruindo de varias recursos interessantes.

|Another Openbox screenshot|

Para o meu proximo artigo, pretendo explicar como personalizar o menu do
Openbox para que voce tenha os seus programas preferidos super
acessiveis, incluindo atalhos de teclado.

.. |Another Openbox screenshot| image:: http://farm1.static.flickr.com/155/386767516_b9c3c2b165.jpg
   :target: http://www.flickr.com/photos/25563799@N00/386767516/
