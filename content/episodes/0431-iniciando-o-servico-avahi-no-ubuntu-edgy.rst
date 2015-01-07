Iniciando o servico Avahi no Ubuntu Edgy
########################################
:slug: iniciando-o-servico-avahi-no-ubuntu-edgy
:date: 2006-10-31 19:23
:category:
:tags: portuguese

Depois de quebrar a cabeca por 2 dias tentando descobrir porque eu nao
conseguia compartilhar minhas musicas usando avahi no Banshee, dei uma
vasculhada nos
`forums <http://ubuntuforums.org/showthread.php?t=281002&highlight=avahi+daemon>`__
e descobri que o servico avahi nao e’ habilitado por padrao no Ubuntu
Edgy!!! E nao e’ uma questao de iniciar o servico, invocando sudo
/etc/init.d/avahi-daemon nao!!!

O X da questao esta no arquivo /etc/default/avahi-daemon, onde a
variavel **AVAHI\_DAEMON\_START=0** “sabota” o script de inicializacao
do servico. Acontece que 0 (zero) nao deixa o servico iniciar, e 1
deixa!!!

Entao, e’ so’ ajustar:

    AVAHI\_DAEMON\_START=1

e reiniciar o servico:

    sudo /etc/init.d/avahi-daemon start
