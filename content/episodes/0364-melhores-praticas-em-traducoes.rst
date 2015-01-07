Melhores PrÃƒÂ¡ticas em TraduÃƒÂ§ÃƒÂµes
###################################################
:slug: melhores-praticas-em-traducoes
:date: 2006-07-21 19:22
:category:
:tags: portuguese

Quando trabalhamos com as traduÃƒÂ§ÃƒÂµes do Ubuntu Linux pelo sistema
do Rosetta, sempre nos deparamos com umas mensagens que sÃƒÂ£o super
simples de traduzir, tipo… “The book is on the table” heheheÃ‚Â  Mas…
nem todas sÃƒÂ£o tÃƒÂ£o obvias assim.Ã‚Â  Nossa equipe de tradutores
criou um `documento <http://wiki.ubuntubrasil.org/l10n>`__ que, alÃƒÂ©m
de explicar algumas coisas sobre o sistema de traduÃƒÂ§ÃƒÂµes, tambÃƒÂ©m
possui uma seÃƒÂ§ÃƒÂ£o dedicada ÃƒÂ  estas frases “cabeludas”.

Este artigo tem como objetivos demonstrar, de uma forma mais grÃƒÂ¡fica,
algumas das melhores prÃƒÂ¡ticas quando vocÃƒÂª se deparar com um destes
casos.

**Primeiro caso**:Ã‚Â  Uma mensagem “normal”

|image0|

Como podemos ver acima, todas variÃƒÂ¡veis permanecem na mensagem
traduzida final, jÃƒÂ¡ que queremos que eles sejam substituÃƒÂ­das por
seus valores na hora da execuÃƒÂ§ÃƒÂ£o do cÃƒÂ³digo.

**Segundo caso**:Ã‚Â  Lidando com o caractereÃ‚Â  [tab]

|image1|

Este ÃƒÂ© um erro comum encontrado nas traduÃƒÂ§ÃƒÂµes.Ã‚Â  Como a
explicaÃƒÂ§ÃƒÂ£o (em inglÃƒÂªs) encontrada entre as duas caixas de texto
menciona, o caractere nÃƒÂ£o deve ser traduzido ou substituÃƒÂ­do por
uma tabulaÃƒÂ§ÃƒÂ£o.

**Terceiro caso**:Ã‚Â  Lidando com o caractere Ã¢â€ Âµ

|image2|

Mais um erro muito comum.Ã‚Â  Esta seta representa o caractere de uma
nova linha.Ã‚Â  Ao contrÃƒÂ¡rio do [tab], aqui vocÃƒÂª realmente quer
substituir a seta por uma nova linha, pressionando a tecla ENTER.

**Quarto caso**:Ã‚Â  Lidando com o caractere Ã¢â‚¬Â¢

|image3|

Outro caractere que deve ser substituÃƒÂ­do, desta vez por um espaÃƒÂ§o
em branco.Ã‚Â  Para cada caractere destes, vocÃƒÂª deve inserir um
espaÃƒÂ§o em branco em sua mensagem traduzida final.

Podemos ver que a mensagem acima foi derivada do arquivo Tray.cs, linha
219 do programa Tomboy.Ã‚Â  Caso vocÃƒÂª queira verificar de perto,
baixe o cÃƒÂ³digo fonte do Tomboy e procure pela linha 219 do arquivo
Tray.cs.

|image4|

**Quinto caso**:Ã‚Â  Lidando com texto dentro de marcadoresde XML

|image5|

Por ÃƒÂºltimo, um exemplo de como lidar com aquelas mensagens que
possuem texto embutido dentro de marcadores de XML.Ã‚Â  Como vocÃƒÂª
pode ver acima, somente o texto que ÃƒÂ© cercado pelos marcadores deve
ser traduzido, e no caso acima, isso seria a palavra “here”.

Bem, espero que este artigo seja ÃƒÂºtil e desperte um pouco de sua
curiosidade.Ã‚Â  Pretendo ainda explicar em um prÃƒÂ³ximo artigo sobre o
processo de traduÃƒÂ§ÃƒÂµes em detalhe.

.. |image0| image:: http://static.flickr.com/69/194901576_78c2577694.jpg
.. |image1| image:: http://static.flickr.com/57/194901577_c4c8e3aaa1.jpg
.. |image2| image:: http://static.flickr.com/61/194901578_0a3d89e42a.jpg
.. |image3| image:: http://static.flickr.com/60/194901579_9dd0da099e.jpg
.. |image4| image:: http://static.flickr.com/63/194901580_5d5c628239.jpg
.. |image5| image:: http://static.flickr.com/63/194901581_cbd25f14bd.jpg
