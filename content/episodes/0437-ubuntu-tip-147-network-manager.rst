Ubuntu Tip #147:  Network Manager
#################################
:slug: ubuntu-tip-147-network-manager
:date: 2006-11-28 03:51
:category: English
:tags: portuguese

A primeira coisa que eu adiciono Ã  uma nova instalaÃ§Ã£o de Gnu/Linux
em um laptop, Ã© o programa Network Manager (sudo aptitude install
network-manager-gnome). Este programa foi a melhor invenÃ§Ã£o no mundo
Gnu/Linux desde a invenÃ§Ã£o do pÃ£o fatiado! Com ele vocÃª nÃ£o tem de
memorizar nomes e senhas para pontos de acesso de redes sem fio. Mas uma
coisa que eu notei foi que se vocÃª instalar o programa depois de
jÃ¡ ter acessado um ponto de acesso, ele simplesmente nÃ£o funciona!

A soluÃ§Ã£o Ã© bem simples, mas infelizmente nÃ£o intuitiva: edite o
arquivo de interfaces de rede, e remova qualquer linha referente ao seu
dispositivo de rede sem fio.

    sudo vim /etc/network/interfaces

Procure pelas linhas jÃ¡ configuradas do dispositivo e as remova:

    wireless-essid Mordor wireless-key theonetobindthemall

NÃ£o se esqueÃ§a de salvar o arquivo. Agora, desabilite o Network
Manager e o habilite novamente em seguida, para que o arquivo possa ser
recarregado, e pronto.
