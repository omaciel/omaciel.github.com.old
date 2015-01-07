DiÃ¡logos e brincando com o wbar
##################################
:slug: dialogos-e-brincando-com-o-wbar
:date: 2008-02-11 02:28
:category: English
:tags: portuguese

Nas Ãºltimas 2 semanas eu sÃ³ consegui trabalhar por 3 horas no
`BillReminder <http://billreminder.gnulinuxbrasil.org/>`__! O que posso
dizer, Ã s vezes vocÃª tem de colocar seus hobbies de lado enquanto a
vida real toma conta do seu tempo. :/

Uma das coisas que estava me incomodando era o antigo diÃ¡logo de
preferÃªncias. Ele estava muito cheio de controles e informaÃ§Ã£o, e o
que mais me incomodava era um ComboBox usado para escolher o horÃ¡rio
preferido para receber um alarme. Haviam entradas para cada hora com
intervalos de 30 minutos (ou seja, 01:00, 01:30, 02:00, etc), resultando
em uma lista enorme que nem cabia na tela.

|Old Preferences Dialog|

EntÃ£o eu dei um uma “massageada” no diÃ¡logo! Fiz algumas
modificaÃ§Ãµes na disposiÃ§Ã£o dos controles e troquei o ComboBox por um
controle de horÃ¡rio personalizado usando SpinButtons. Ainda nÃ£o Ã©
exatamente o que eu queria mas pelo menos nÃ£o estou mais incomodado com
ele. Existem mais 2 coisas que quero resolver antes de lanÃ§ar uma nova
versÃ£o, mas infelizmente nÃ£o sei como minha semana vai ser. :/

|New Preferences Dialog|

Hoje reservei 30 minutos para empacotar o
`wbar <http://freshmeat.net/projects/wbar/>`__ (meu repositÃ³rio
pessoal) e o adicionei Ã  uma distro que estou desenvolvendo, usando o
`Openbox <http://www.icculus.org/openbox>`__ como gerente de janelas
padrÃ£o. Ele parece ser bem leve e rÃ¡pido sem nem mesmo nenhum X
compositing. I experimentei mover o pypanel para o topo mas nÃ£o sei se
gostei do resultado. TambÃ©m tentei fazer o **GDM** considerar o Openbox
como sua sessÃ£o padrÃ£o e acabei tento de modificar o **Xsession** para
conseguir o que queria. HorrÃ­vel mas funcionou.

|Perere Linux with wbar and pypanel|

TambÃ©m tive uma boa briga tentando fazer o **PulseAudio** iniciar
automaticamente. Minha estratÃ©gia foi colocar um arquivo
pulseaudio-openbox.desktop dentro do diretÃ³rio /etc/xdg/autostart, que
executava um script para iniciar o PulseAudio… mas aparentemente isso
sÃ³ funciona com gerentes de sessÃµes, e o Openbox nÃ£o possui um.
Acabei tendo de modificar o script openbox-session script para conseguir
o que queria. Qualquer feedback serÃ¡ muito apreciado.

.. |Old Preferences Dialog| image:: http://farm3.static.flickr.com/2152/2254574149_a11e85bac8_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2254574149/
.. |New Preferences Dialog| image:: http://farm3.static.flickr.com/2055/2255356186_719bb260a2_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2255356186/
.. |Perere Linux with wbar and pypanel| image:: http://farm3.static.flickr.com/2039/2255962057_9e4722c96b.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2255962057/
