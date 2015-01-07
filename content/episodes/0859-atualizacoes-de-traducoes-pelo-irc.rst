Atualizações de traduções pelo IRC
######################################
:slug: atualizacoes-de-traducoes-pelo-irc
:date: 2008-10-24 15:41
:category: English
:tags: portuguese

Algum tempo atrás eu criei o canal **#tradutores** na Freenode, um lugar
onde pessoas que trabalham com traduções de software livre podem bater
papo e tirar dúvidas, sem vínculos com nenhuma distribuição ou projeto
em específico. Lá você encontrará pessoas que trabalham no **GNOME, KDE,
XFCE, Fedora, Foresight, Ubuntu**, todos trabalhando com o mesmo
intuito: melhorar a qualidade das traduções em nosso idioma!

Uma coisa que eu sempre quiz ter foi uma forma de ser notificado toda
vez que algum projeto tivesse a tradução de algum programa (ou pacote no
nosso “jargão”) atualizado. Ou seja, se o **Amarok, Totem, Firefox**, ou
**Thunar** tiverem suas traduções (Português do Brasil) atualizadas, eu
queria ser notificado. Um dia procurando por algo que pudesse fazer
isso, encontrei o site `CIA.vc <http://cia.vc/>`__, um enorme agregador
de mensagens de commit de vários projetos do mundo open source! Eu
imediatamente comecei a usar os seus serviços para acompanhar o commit
de alguns projetos como o GNOME (ele inteiro, o que gera centenas de
mensagens diariamente) e até mesmo o
`BillReminder <http://billreminder.gnulinuxbrasil.org>`__. Depois
adicionei um bot no canal **#billreminder** na Freenode para anunciar
por lá toda vez que algum commit fosse enviado. Eu estava bem feliz com
o serviço até que ontem descobri mais um recurso que completamente fez o
meu dia: filtros!

Depois de apanhar bastante, consegui finalmente hoje criar um novo bot
que filtra todo e qualquer commit de qualquer projeto de open source
registrado no CIA.vc, desde que a palavra “\ **Brazilian**\ ” esteja na
mensagem de envio. Por que Brazilian? Porque é costume adicionar a frase
“\ **Updated Brazilian Portuguese**\ …” nas mensagens de commit, o que
facilita bastante na hora de filtrar somente mensagens relacionadas a
traduções.

|cia.cv bot for Brazilian Portuguese translations|

Como pode ser visto acima, logo depois de enviar a tradução do programa
**Dates**, o bot **CIA-60** informou sobre o evento no canal. :)

Gostaria então de convidar todas as pessoas que estão trabalhando em
projetos de tradução para aparecer no #tradutores, conversar com outros
tradutores, e compartilhar sua experiência e idéias.

.. |cia.cv bot for Brazilian Portuguese translations| image:: http://farm4.static.flickr.com/3008/2969952342_c040d0c790.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2969952342/
