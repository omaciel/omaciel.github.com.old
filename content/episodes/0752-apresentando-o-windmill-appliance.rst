Apresentando o Windmill Appliance
#################################
:slug: apresentando-o-windmill-appliance
:date: 2008-04-14 12:35
:category:
:tags: portuguese

Tenho um grande orgulho em apresentar o lançamento do `Windmill
Appliance <http://www.rpath.org/rbuilder/project/windmill/releases>`__!
Construido com a tecnologia inovadora da
`rPath <http://www.rpath.com>`__, está disponível para download como um
ISO assim como também uma  imagem VMWare para a sua alegria.

"Mas para que exatamente serve este windmill appliance?", você pergunta.
Que bom que você perguntou… O
`Windmill <http://windmill.osafoundation.org/>`__ é um **framework de
testes em AJAX para interfaces web de código livre**. Pelos últimos
meses eu tenho usado e abusado deste software para estar apropriadamente
a interface web de um de nossos produtos, e os resultados tem sido muito
agradaveis. Melhor ainda, a interação com os desenvolvedores principais
(eu estou sempre pelo canal #windmill na Freenode) tem sido extremamente
beneficial no meu ponto de vista.

O fato que eu posso empacotar e distribuir o windmill em literalmente
minutos usando o `Conary <http://wiki.rpath.com/wiki/Conary>`__ e
`rBuilder <http://www.rpath.com/corp/products-rbuilder.html>`__ me
permite providenciar um retorno muito mais rápido aos desenvolvedores
que, tenho de admitir, tem sido bem considerados com o meu abuso. :)
Este appliance é minha forma de agradecê-los por seu trabalho, como
também uma forma de ajudar outros desenvolvedores que precisam de uma
forma eficiente para testar a interface web de seus projetos.

Desenhado para funcionar de forma “headless”, ou seja, sem monitor,
teclado ou mouse, um servidor Vnc é automaticamente iniciado no boot
(usando a porta 5901) assim como o servidor SSH para que você possa
conduzir os seus testes remotamente. A idéia é iniciar o appliance em
algum nódulo de sua rede (ou até mesmo vários em um cluster) e iniciar
seus testes sem “poluir” o seu sistema.

Por favor, fique à vontade de me perguntar qualquer coisa sobre o
appliance aqui ou no canal #windmill, como também responder perguntas
sobre como personalizá-lo para as suas necessidades.
