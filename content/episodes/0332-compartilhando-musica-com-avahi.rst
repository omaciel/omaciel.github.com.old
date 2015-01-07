Compartilhando mÃƒÂºsica com Avahi
######################################
:slug: compartilhando-musica-com-avahi
:date: 2006-06-12 15:03
:category:
:tags: portuguese

O que posso dizer, fou um fim de semana muito movimentadoÃ¢â‚¬Â¦Ã‚Â 
|;)| Ã‚Â  Antes de seguir o
`conselho <http://blog.canetatinteiro.org/2006/06/05/compartilhando-musicas-em-uma-rede-local-com-avahi-e-bansheerhythmbox/>`__
do meu amigo **OtÃƒÂ¡vio** sobre como compartilhar minha coleÃƒÂ§ÃƒÂ£o
de mÃƒÂºsica digital em casa entre os muitos dispositivos que possuo, eu
infelizmente copiava muitos gigabytes de arquivos \*.oggs pela minha
redeÃ¢â‚¬Â¦Ã‚Â  Como eu nÃƒÂ£o queria entupir meu TabletPC, eu decidi
tentar o tal do avahi.

    Ã¢â‚¬Å“Avahi is a system which facilitates service discovery on a
    local network. This means that you can plug your laptop or computer
    into a network and instantly be able to view other people who you
    can chat with, find printers to print to or find files being
    shared.Ã¢â‚¬Â?Ã‚Â  `Avahi.org <http://avahi.org/>`__

Ou seja, o avahi permite que dispositivos possam descobrir outros
dispositivos que estejam por perto, sem nenhuma configuraÃƒÂ§ÃƒÂ£o
necessÃƒÂ¡ria. SÃƒÂ³ de ler essa descriÃƒÂ§ÃƒÂ£o, vocÃƒÂª jÃƒÂ¡ pode
imaginar as possibilidadesÃ¢â‚¬Â¦Ã‚Â  De qualquer forma, como eu
jÃƒÂ¡ tinha o Rhythmbox instalado, tudo que eu tinha de fazer era
instalar o pacote avahi-daemon em ambos dispositivos: sudo apt-get
install avahi-daemon e pronto!Ã‚Â  Agora ÃƒÂ© sÃƒÂ³ configurar o seu PC
que contÃƒÂ©m a coleÃƒÂ§ÃƒÂ£o de mÃƒÂºsica a compartilhar via a aba
Ã¢â‚¬Å“ShareÃ¢â‚¬Â? no diÃƒÂ¡logo de preferÃƒÂªncias do Rhythmbox.
|image1| Assim que eu abri o Rhythmbox no meu TabletPC, a nova
coleÃƒÂ§ÃƒÂ£o compartilhada foi automagicamente detectada e tudo que
tive de fazer foi caminhar pela casa, curtindo minha nova
zeroconfÃ¢â‚¬â„¢ed (ou seja, sem nenhuma configuraÃƒÂ§ÃƒÂ£o) liberdade!
Por falar em Rhythmbox, eu gostaria muito que houvesse um recurso para
carregar/descarregar mÃƒÂºsica do meu iPod.Ã‚Â  Por enquanto, o Banshee
tem feito um excelente trabalho em fazer tudo isso, incluindo o
compartilhamento de mÃƒÂºsica, usando o pacote banshee-daap.
**OtÃƒÂ¡vio**:Ã‚Â  Gostaria tremendamente de vÃƒÂª-lo como autor do
`Planeta <http://planeta.ubuntubrasil.org/>`__!

.. |;)| image:: http://www.ogmaciel.com/wp-includes/images/smilies/icon_wink.gif
.. |image1| image:: http://static.flickr.com/53/165636617_defbb2956a.jpg
   :target: http://static.flickr.com/53/165636617_defbb2956a_o.png
