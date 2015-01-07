Google Highly Open Participation Contest e TraduÃ§Ãµes
##########################################################
:slug: google-highly-open-participation-contest-e-traducoes-2
:date: 2007-12-29 22:35
:category: English
:tags: portuguese

Se vocÃª estÃ¡ participando do `Google Highly Open Participation
Contest <http://code.google.com/opensource/ghop/2007-8>`__ e
estÃ¡ ajudando com o processo de traduÃ§Ãµes, ou estÃ¡ procurando por
uma forma garantida de testar suas traduÃ§Ãµes com o GNOME mais recente
(ainda em desenvolvimento), entÃ£o vÃ¡ buscar sua cÃ³pia do `GNOME
Developer Kit agora <http://live.gnome.org/GnomeDeveloperKit>`__!

VocÃª poderÃ¡ entÃ£o baixar o catÃ¡logo de mensagens para a aplicaÃ§Ã£o
que vocÃª deseja traduzir (no meu caso eu baixei o arquivo do Empathy)
para o seu idioma e use o **poEdit** (jÃ¡ incluÃ­do) para mandar bala na
sua traduÃ§Ã£o. VocÃª poderÃ¡ tambÃ©m aproveitar o **translate-toolkit**
e realmente fazer um excelente trabalho de QA!

Uma vez que vocÃª tenha seguido os passos acima, a melhor coisa a fazer
Ã© criar um relatÃ³rio de `erro <http://bugzilla.gnome.org/>`__
escolhendo a categoria **Translations** e anexando sua obra prima. Eu
recomendo que vocÃª entre em contato com o coordenador da equipe
primeiro para certificar que ninguÃ©m mais estÃ¡ trabalhando na mesma
traduÃ§Ã£o, e assim evitar trabalho dobrado.

Agora vem a melhor parte: testar o seu trabalho! Note que o programa
empathy estÃ¡ parcialmente traduzido no screenshot abaixo (olhe a
traduÃ§Ã£o dos botÃµes):

|Empathy running on GNOME Live|

Um dos benefÃ­cios de usar o poEdit nas suas traduÃ§Ãµes (algumas
pessoas gostam de usar uma combinaÃ§Ã£o do poEdit e um editor de texto,
como o vim… eu por exemplo!) Ã© que ele automaticamente checa o arquivo
por formataÃ§Ã£o E gera uma versÃ£o compilada de sua traduÃ§Ã£o. Ã‰
justamente esta versÃ£o compilada, um arquivo com a extensÃ£o .mo, que
Ã© usada pelas aplicaÃ§Ãµes para exibir suas mensagens no idioma
escolhido.

O que precisamos fazer Ã© uma cÃ³pia de seguranÃ§a do arquivo compilado
original e substituÃ­-lo com a sua nova versÃ£o:

    cp /usr/share/locale/pt\_BR/LC\_MESSAGES/empathy.mo
    $HOME/original\_empathy.mo cp empathy.mo
    /usr/share/locale/pt\_BR/LC\_MESSAGES/empathy.mo

Agora re-inicie a aplicaÃ§Ã£o e… voilÃ¡:

|Empathy running on GNOME Live, 100% translated|

Agora, lembra aquele relatÃ³rio de erro (aqui estÃ¡ o
`meu <http://bugzilla.gnome.org/show_bug.cgi?id=504373>`__) que criamos
antes? Bem, uma vez alguÃ©m da equipe de traduÃ§Ãµes do seu idioma tiver
revisado e enviado o seu trabalho, Ã© sÃ³ esperar pelo
`conary <http://wiki.rpath.com/wiki/Conary>`__ (o sistema gerenciador de
pacotes por trÃ¡s do Developer Kit) te notificar quando a nova versÃ£o
estiver disponÃ­vel para atualizaÃ§Ã£o. Abaixo Ã© um screenshot do meu
sistema rodando um sistema sem modificaÃ§Ãµes do GNOME 2.21 em
PortuguÃªs do Brasil:

|GNOME Live in Brazilian Portuguese|

Tem alguma pergunta? Fique Ã  vontade de me contactar.

.. |Empathy running on GNOME Live| image:: http://farm3.static.flickr.com/2313/2123268702_99005f40d7.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2123268702/
.. |Empathy running on GNOME Live, 100% translated| image:: http://farm3.static.flickr.com/2238/2123268708_cc88d32fee.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2123268708/
.. |GNOME Live in Brazilian Portuguese| image:: http://farm3.static.flickr.com/2166/2123268698_e1f1a4c640.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2123268698/
