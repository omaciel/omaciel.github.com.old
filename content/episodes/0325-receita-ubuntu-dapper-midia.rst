Receita Ubuntu Dapper MÃƒÂ­dia
##################################
:slug: receita-ubuntu-dapper-midia
:date: 2006-06-10 16:21
:category:
:tags: portuguese

Com o novo lanÃƒÂ§amento do Ubuntu Dapper, foram muitas as pessoas que
iniciaram no mundo linux sem saber como configurar seu sistema para a
melhor experiÃƒÂªncia possÃƒÂ­vel. Claro que a instalaÃƒÂ§ÃƒÂ£o
padrÃƒÂ£o jÃƒÂ¡ possui a maioria das ferramentas e aplicativos que um
usuÃƒÂ¡rio possivelmente vai precisar, mas existem certas tecnologias
que, devido ÃƒÂ  licenÃƒÂ§as um pouco mais restritivas (em relaÃƒÂ§ÃƒÂ£o
ÃƒÂ  sua distribuiÃƒÂ§ÃƒÂ£o, etc), nÃƒÂ£o sÃƒÂ£o instaladas de forma
automÃƒÂ¡tica.

Justamente com este tipo de usuÃƒÂ¡rio em mente, venho entÃƒÂ£o
apresentar a minha receita. Os passos abaixo foram seguidos logo apÃƒÂ³s
a instalaÃƒÂ§ÃƒÂ£o padrÃƒÂ£o, e usando a linha de comando. Claro que o
gerenciador de pacotes Synaptic pode ser utilizado para uma
experiÃƒÂªncia grÃƒÂ¡fica.

Para uma experiÃƒÂªncia de navegaÃƒÂ§ÃƒÂ£o mais rÃƒÂ¡pida e simples,
instale o navegador Epiphany:

    sudo apt-get install epiphany-browser epiphany-extensions

Para adicionar suporte ÃƒÂ  tecnologias web padronizadas, mas
infelizmente proprietÃƒÂ¡rias:

    sudo apt-get install flashplugin-nonfree sun-java5-plugin

Durante a instalaÃƒÂ§ÃƒÂ£o do Flash e Java, confirme que vocÃƒÂª aceita
os termos das licenÃƒÂ§as, marcando as caixas de opÃƒÂ§ÃƒÂµes
apropriadas.

Para adicionar suporte ÃƒÂ  elementos de mÃƒÂ­dia, incluindo suporte
ÃƒÂ  MP3 e outros tipos de vÃƒÂ­deo:

    sudo apt-get install gstreamer0.10-plugins-bad sudo apt-get install
    gstreamer0.10-plugins-bad-multiverse sudo apt-get install
    gstreamer0.10-plugins-ugly sudo apt-get install
    gstreamer0.10-plugins-ugly-multiverse sudo apt-get install
    gstreamer0.10-pitfdll sudo apt-get install gstreamer0.10-ffmpeg

Se vocÃƒÂª conhece os antigos filmes do Clint Eastwood e jÃƒÂ¡ assistiu
“\ `The Good, the Bad, and the
Ugly <http://www.imdb.com/title/tt0060196/>`__\ ”, vai notar que os
pacotes gstreamer0.10-plugins-good\* jÃƒÂ¡ estÃƒÂ£o instalados por
padrÃƒÂ£o. ;)

E para adicionar suporte ÃƒÂ  todos os outros tipos de mÃƒÂ­dia
proprietÃƒÂ¡rios (Eca!) que infelizmente assolam o mundo WWW, baixe o
arquivo W32codecs, colando o seguinte link em seu navegador favorito
(que eu espero ser o Epiphany):

    `http://distrib-coffee.ipsl.jussieu.fr/pub/linux/plf/ubuntu/plf/pool/dapper/i386/non-free/
    w32codecs/w32codecs\_20050412-1plf4\_i386.deb <http://distrib-coffee.ipsl.jussieu.fr/pub/linux/plf/ubuntu/plf/pool/dapper/i386/non-free/w32codecs/w32codecs_20050412-1plf4_i386.deb>`__

Depois de baixÃƒÂ¡-lo, de um clique duplo no mesmo para iniciar o
processo de instalaÃƒÂ§ÃƒÂ£o. Quando a “massa do bolo subir”, vocÃƒÂª
terÃƒÂ¡ com certeza um sistema bem mais completo que o inicial.

-  A dica do gstreamer0.10-pitfdll foi de **Kai D. Lahmann**, que deixou
   um comentÃƒÂ¡rio em meu blog em inglÃƒÂªs.

-  O **Brunno** merece crÃƒÂ©dito por indicar meu equÃƒÂ­voco sobre o
   pacote do Epiphany.


