Servidor de músicas Bailout MT-Daapd
#####################################
:slug: servidor-de-musicas-bailout-mt-daapd
:date: 2009-01-02 17:35
:category: English
:tags: portuguese

No finalzinho do ano passado eu passei alguns dias trabalhando para
configurar um servidor de músicas bem simples para usar em casa. Como eu
estou sempre fazendo algo maluco no meu desktop/laptop que eventualmente
sempre me leva a re-instalar o meu sistema operacional, eu estou
constantemente movendo meus arquivos de música entre computadores e
discos externos. Quando você tem uma coleção de tamanho considerado,
este exercício se torna um pé no saco. Foi por isso que tive a idéia de
criar um servidor de músicas usando o  mt-daapd como minha ferramente
principal. O mt-daapd é tão fácil de usar que eu imediatamente comecei o
meu projeto.

O primeiro passo foi criar um novo produto (leia projeto) no site
`rBuilder Online <http://www.rpath.org>`__. Depois de pensar por uns 2
minutos decidi chamá-lo `Bailout <http://bailout.rpath.org>`__, algo
como que a fiança que se paga para sair da prisão, já que eu precisava
de algo para me liberar dos meus problemas de armazenamento e
compartilhamento de músicas.

O próximo passo foi então escolher quais componentes adicionar ao meu
produto. Como o rBuilder me permite começar com Just Enough Operating
System (ou JEOS, o que quer dizer que somente os componentes essenciais
para um sistema operacional serão usados), eu continuei configurando meu
produto, escolhendo o sistema operacional **rPath Linux 2** (minhas
outras opções eram **Ubuntu Hardy** e **CentOS**) e escolhendo a dedo
outros componentes que eu gostaria de disponibilizar em uma instalação
padrão. Acabei escolhendo os serviços smb, nfs e openssh para
conectividade, assim como o vim (caramba, se vou conectar por ssh neste
sistema para fazer qualquer configuração manual, então preciso do meu
editor de texto preferido). Tudo isso foi feito usando uma interface web
do rBuilder e até então tudo foi feito usando apenas o mouse e clicando
nas opções.

Agora sim chegou a hora da atração principal: o mt-daapd. Como este
componente não estava disponível no repositório padrão onde escolhi
todos os outros componentes, chegou a hora de tomar algumas decisões
importantes. O rBuilder permite o empacotamento de software pela
interface gráfica usando pacotes **RPM**, **DEB** ou tarballs binários,
mas optei por experimentar uma nova ferramente de empacotamento chamada
**rbuild** (não confundir com o rBuilder Online) para aqueles que como
eu, curtem usar a linha de comando e já conhecem um pouco mais sobre o
sistema de gerenciamento de pacotes **conary**, tecnologia desenvolvida
aqui onde trabalho e coração do rBuilder. Não vou entrar em detalhes
sobre como empacotei o mt-daapd usando o rbuild mas eu recomendo a
leitura dos
`posts <http://blogs.conary.com/index.php/mkj/2008/08/29/simplifying_assumptions>`__
(todos em inglês) escritos pelo Michael Johnson para aprender mais sobre
esta ferramenta.

Passados mais alguns minutos e o meu produto estava com todos os
componentes prontos. Com mais alguns cliques na interface iniciei o
processo de criação de uma imagen de instalação no formato ISO e VMWare,
permitindo que qualquer pessoa possa experimentar o Bailout em um
sistema virtual ou instalá-lo de verdade. Eu poderia ter escolhido
outros formatos para distribuir o meu produto como imagens para o
**Amazon EC2**, **Citrix**, ou **Xen** mas eu ainda posso editar minhas
preferências e adicionar estas opções mais tarde.

Uma vez minhas 2 imagens estavam finalizadas, chegou a hora de
testá-las. Escolhi gravar um CD com a imagem ISO e instalei o Bailout em
um computador que estava coletando poeira no closet do meu quarto. O
instalador é baseado no anaconda, usado pela Red Hat e Fedora entre
outras distribuições, e super fácil de usar. Depois que o processo
(super rápido) de instalação acabou e de um rápido reboot, me deparei
com um terminal todo preto e com instruções para me conectar ao sistema
de gerenciamento do produto, apontando meu navegador de web para um
endereço local IP. E lá fui eu.

|Appliance Management|

Caso você decida brincar com o Bailout você verá na seção de downloads
algumas instruções sobre qual o nome de usuário e senha padrão do
sistema de gerenciamento, mas para aqueles que se esqueceram de ler
isso, use **admin** e **password** para conectar. Não se preoculpe com a
senha super fácil de quebrar… você vai mudá-la no próximo passo.

|Wizard: Setup a password|

A primeira vez que você conecta no Bailout, você será requisitado a
mudar sua senha. Certifique-se que a nova senha é algo seguro já que com
ela você será capaz de administrar seu servidor de músicas.

O próximo (opcional) passo é configurar como você gostaria de ser
notificado sobre as atividades do seu servidor como também sobre
atualizações disponíveis para o seu sistema. Como eu gosto de receber
estes tipos de notificações, adicionei a informação necessária e
continuei com o wizard (dica: Caso você não queira completar este passo,
clique no botão **save**).

|Wizard: Setup a password for root|

Finalmente, escolha uma senha segura para o usuário root do sistema.

|Landing page|

E pronto! Seja bem-vindo ao seu servidor de músicas! O sistema de
administração web possui várias outras funções que te permite efetuar
tarefas como atualizar, fazer backups…

|Managing running services|

… gerenciar serviços, configurar a rede…

|System Information|

… checar o status do sistema e até mesmo restaurar o sistema de volta a
um estado anterior.

|MT-Daapd service web page|

Agora podemos apontar o nosso navegador web para o mesmo endereço do
sistema de administração web, mudando a porta para 3689 e usando
**admin**/**mt-daapd** como credenciais para conectar no sistema de
gerenciamento web do mt-daapd. Você deve também ver um novo
compartilhamento de músicas aparecer no seu reprodutor de mídia favorito
(assumindo que o servidor Bailout e o sistema onde o reprodutor de
músicas estão na mesma rede).

|Banshee using a mt-daapd music share|

Por enquanto o servidor é configurado para usar o diretório /mnt/mp3
como armazenamento de mídia e não está configurado para varrer seu
conteúdo automaticamente, mas isso e outras opções podem ser modificadas
conectando por ssh no servidor e editando manualmente o arquivo
/etc/mt-daapd.conf. Uma versão mais recente (mas ainda em
desenvolvimento) do mt-daapd, batizado de FireFly, permite que todas
estas configurações sejam feitas pela interface web. Com certeza terei
este versão atualizado em breve para que fique ainda mais fácil
configurar o servidor de músicas. Obviamente, se você quer me dar uma
mão, é só entrar em contato comigo.

Então aproveite o começo de um novo ano e faça o download do servidor de
músicas `Bailout <http://bailout.rpath.org>`__ hoje!

.. |Appliance Management| image:: http://farm4.static.flickr.com/3227/3087612648_23a5164936.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087612648/
.. |Wizard: Setup a password| image:: http://farm4.static.flickr.com/3218/3086775491_bb6ee9acd6.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086775491/
.. |Wizard: Setup a password for root| image:: http://farm4.static.flickr.com/3228/3087612788_1e44136a71.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087612788/
.. |Landing page| image:: http://farm4.static.flickr.com/3050/3086776079_e03069c47b.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776079/
.. |Managing running services| image:: http://farm4.static.flickr.com/3198/3086776183_1b03d6363d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776183/
.. |System Information| image:: http://farm4.static.flickr.com/3033/3086776791_7100cd5479.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086776791/
.. |MT-Daapd service web page| image:: http://farm4.static.flickr.com/3077/3087613296_2f78daff21.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3087613296/
.. |Banshee using a mt-daapd music share| image:: http://farm4.static.flickr.com/3038/3086941341_6586e3754d.jpg
   :target: http://www.flickr.com/photos/ogmaciel/3086941341/
