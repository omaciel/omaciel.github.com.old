Usando o Dropbox com o Openbox
##############################
:slug: usando-o-dropbox-com-o-openbox
:date: 2009-01-03 18:32
:category: Portuguese
:tags: rpath

Dando continuidade ao
`post <http://vladimirmelo.wordpress.com/2009/01/03/dropbox-simples-e-eficiente/>`__
do **Vladimir Melo**, gostaria de compartilhar minha experiência usando
o programa `Dropbox <http://www.getdropbox.com/>`__.

Mesmo sendo um usuário do GNU/Linux por tanto tempo, foi somente 2 anos
atrás que comecei a usá-lo o tempo todo. Como eu antes trabalhava como
um desenvolvedor de **.NET** e **Oracle** durante o dia para o
**Departamento de Educação** da cidade de **New York**, eu tinha um
ambiente padrão de desenvolvedor instalado em meu sistema e nada mais.
Isto significa que eu não podia instalar nenhum outro programa em meu
sistema devido as políticas super atiquadas adotadas pela gerência. Para
você ter uma idéia, eu não podia nem mesmo pesquisar por informações
online e fui aconselhado a fazer tudo isso de casa e trazer o resultado
no dia seguinte para o trabalho, mas isto é material para um outro post.

Uma forma que achei de diminuir meu sofrimento foi usando alguns
`aplicativos portáteis <http://portableapps.com/>`__ que podem ser
executados a partir de um pendrive, por exemplo, e por 2 anos fui um
ávido usuário do **Portable Firefox**. Eu também salvava meu código
pessoal neste mesmo pendrive para que eu pudesse então trabalhar de casa
altas horas da madrugada (pois é, não tinha acesso remoto também).
Depois de algum tempo, a tarefa de guardar meus favoritos, código e
arquivos sincronizados entre meu sistema Windows do trabalho e meu
sistema GNU/Linux de casa se transformou em algo muito chato de manter.

Adiante o filme alguns anos e você me encontra agora em meu trabalho
atual, `rPath <http://www.rpath.com/corp/>`__, uma companhia formada
pelos primeiros engenheiros da **Red Hat**, dedicada a simplificar a
distribuição de produtos no mundo virtual, no estado de North Carolina,
onde eu posso usar sistemas livres e abertos todos os dias! E eu que
pensava saber uma coisa ou duas sobre como usar e configurar sistemas e
aplicativos, aprendi bem rápido que ainda tinha muito que aprender!
Imediatamente parei de usar editores gráficos de texto (nada de mal com
o **gEdit**) e virei um fã de carteirinha do **vim**, também trocando o
**Firefox** e **Winamp** pelo **Epiphany** e **Rhythmbox**, e finalmente
pude voltar a usar o meu gerenciador de janelas predileto:
`Openbox <http://icculus.org/openbox/index.php/Main_Page>`__. Não que eu
tenha algo contra outros gerenciadores mas o Openbox tem sempre sido o
sistema que me agrada com sua simplicidade desde meus dias do
**Gentoo**.

Tudo estava indo muito bem na minha nova vida, aprendendo uma tonelada
de coisas novas e trabalhando com coisas de tencologia de ponta, mas… já
que a companhia me deu um laptop de trabalho, eu ainda tinha os mesmos
problemas sincronizando meus arquivos entre meus sistemas. Ok, ok,
existem algumas ferramentas por aí e é claro que poderia criar meu
próprio script para ajudar nesta tarefa, mas eu queria algo mais fácil!
Eu queria algo que funcionasse “out of the box” sem ter de investir
muito tempo ou mão de obra, com integração completa e 100% fácil de
usar. O dia que o `Dropbox <http://www.getdropbox.com/>`__ para o
GNU/Linux foi anunciado foi o dia que eu deixei de carregar um pendrive
comigo!

Como o meu intúito não é de fazer propaganda para o Dropbox, basta dizer
que:

    -  Dropbox facilita o armazenamento e compartilhamento de seus
       arquivos online.
    -  Executa no segundo plano de seu sistema, sem mais uma interface
       para você aprender a usar.
    -  Sincroniza seus arquivos automaticamente de seu sistema para a
       web.
    -  Conecte e acesse seus arquivos de qualquer lugar usando um
       navegador web ou dispositivo móvel.

Interessante, não? Mas ainda tem mais! O cadastro completamente **free**
oferece **2GB** de armazenamento usando o sistema **S3** da **Amazon**,
e todos seus arquivos são transferidos por **SSL** **criptografados**
com AES-256 e armazenados como a diferença (delta) do estado anterior,
como um **sistema de controle de versões** igual o SVN, CVS, Mercurial,
Git, etc

|Dropbox|

Infelizmente existe um problema com este aplicativo, já que o Dropbox
anuncia que se integra muito bem com o **Nautilus**, o que indica que
somente usuários do **GNOME** podem desfrutar de seus recursos… ou será?

Outra noite eu estava reclmando sobre este problema com um amigo quando
ele sugeriu, “por quê você não verifica se o serviço está rodando e veja
se ele funciona sem o Nautilus?” Então eu entrei no Openbox e… nada do
Dropbox! Continuei investigando e o comando ``ps aux | grep drop`` me
disse que o serviço dropboxd era iniciado a partir do diretório
``$HOME/.dropbox-dist/``. Sem pensar duas vezes adicionei mais uma linha
contendo ``"~/.dropbox-dist/dropboxd &"`` no meu arquivo 
``$HOME/.config/openbox/autostart.sh``, re-iniciei o Openbox e… tudo
funcionando! Tudo bem que eu não tinha o ícone na bandeja do sistema
aparecendo no **pypanel**, mas tudo estava funcionando como pude
verificar ao modificar um arquivo e vi a informação sobre esta
modificação aparecer na minha página pessoal do Dropbox! Ahhh, as
possibilidades!!!

A primeira coisa que fiz foi criar uma pasta chamada **dotfiles** dentro
do novo diretório que foi criado em meu sistema chamado
``$HOME/Dropbox``, e movi todos os meus arquivos que começam com um
ponto (por exemplo, .vimrc, .bashrc, etc) para lá. Então criei links
simbólicos em seus lugares originais assim fazendo que todos meus
arquivos de configuração fossem links para os arquivos dentro da pasta
``$HOME/Dropbox/dotfiles``:

    $HOME/.vimrc -> Dropbox/dotfiles/.vimrc $HOME/.bashrc ->
    Dropbox/dotfiles/.bashrc

Também adicionei todos os meus arquivos de configuração do Openbox que
vivem em $HOME/.config/openbox e  os substituí por links para garantir
que meu ambiente Openbox, menus e personalizações estariam disponíveis
para mim quando usando outros sistemas, assim como também adicionei meu
$HOME/.ssh e $HOME/.gnupg. Já está babando?

No dia seguinte fui para o trabalho (eu raramente uso meu laptop quando
estou em casa, preferindo usar meu desktop) e instalei o Dropbox. Logo
em seguida criei os mesmos links simbólicos que criei em casa (hoje em
dia tenho um script armazenado no próprio Dropbox que faz tudo isso!) e
pronto! Meu sistema de trabalho parecia uma cópia fiel do meu sistema de
casa, e melhor de tudo, toda vez que eu modifico qualquer um destes
arquivos, eles são automaticamente sincronizados e disponibilizados em
ambos sistemas!

|Openbox with Dropbox (not seen) makes for a great system|

Em conclusão, o conjunto Openbox com Dropbox é realmente uma excelente
combinação para aqueles que preferem um sistema leve com uma forma fácil
de sincronizar/fazer backup seu sistema! Eu realmente recomendo! Algumas
coisas que eu gostaria de ver acontecer com as próximas versões do
Dropbox seria a padronização do lugar onde o serviço dropboxd é
instalado e suporte oficial para outros gerenciadores de arquivos.
Também gostaria de ver uma forma mais fácil de restaurar modificações
feitas em um arquivo (lembre-se que tudo é controlado por um sistema de
versões) sem ter de sobrescrevè-los. Vou ficar na expectativa que o
pessoal do Dropbox implemente mais recursos bacanas neste novo ano! :)

.. |Dropbox| image:: https://www.getdropbox.com/static/images/tour3b.png
.. |Openbox with Dropbox (not seen) makes for a great system| image:: http://farm4.static.flickr.com/3003/2948601731_c75de0fd08.jpg
   :target: http://www.flickr.com/photos/ogmaciel/2948601731/
