TabletPC 4: Entrei de gaiato no navio
#####################################
:slug: tabletpc-4-entrei-de-gaiato-no-navio
:date: 2006-06-12 03:05
:category:
:tags: portuguese

O domingo foi super corrido, com muito jogo de futebol, regado ÃƒÂ 
muita cerveja (belga, ÃƒÂ© claro!) e churrasco, como todo brasileiro que
se preze.Ã‚Â  Entre carne, cerveja, revisÃƒÂ£o de traduÃƒÂ§ÃƒÂµes,
gravaÃƒÂ§ÃƒÂ£o de podcast, e visita inesperada dos sogros, consegui
arrumar tempo para brincar com o TabletPC e girar a tela.Ã‚Â  A dica
veio via um comentÃƒÂ¡rio no meu blog em inglÃƒÂªs, e involve a
inclusÃƒÂ£o de uma simples linha no arquivo xorg.conf: Option
“RandRRotation”

    Section “Device” Identifier Ã‚Â  Ã‚Â  Ã‚Â ”NVIDIA Corporation NV17
    [GeForce4 420 Go 32M]” Driver Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â ”nvidia” BusID
    Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  “PCI:1:0:0” **Option Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â 
    Ã‚Â ”RandRRotation”** EndSection Section “Monitor” Identifier Ã‚Â 
    Ã‚Â  Ã‚Â ”Generic Monitor” Option Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â  Ã‚Â ”DPMS”
    HorizSync Ã‚Â  Ã‚Â  Ã‚Â  28-51 VertRefresh Ã‚Â  Ã‚Â  43-60
    EndSection

Tudo que falta agora seria re-iniciar o X (apertando CTRL + ALT +
BACKSPACE funcionou para mim) e, abrindo um terminal, digitando o
comando:

    xrandr -o { left \| right \| inverted \| normal }

Como vocÃƒÂª pode ver na foto abaixo,Ã‚Â  a tela do meu TabletPC foi
girada 90 graus:

|image0|

O ÃƒÂºnico incoveniente que tive foi devido ao mouse (ou mesmo o stylus
pen) nÃƒÂ£o inverter seus “eixos”, o que dificultou muito conseguir
tirar este screebshot.Ã‚Â  ;)Ã‚Â  NÃƒÂ£o sei se existe uma interface
grÃƒÂ¡fica para o xrandr, mas com certeza jÃƒÂ¡ estou com milhÃƒÂµes de
idÃƒÂ©ias para desenvolver uma.

.. |image0| image:: http://static.flickr.com/55/165396895_6e1712b9a7.jpg
   :target: http://static.flickr.com/55/165396895_6e1712b9a7_o.png
