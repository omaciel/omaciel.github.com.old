Videocast: Usando o Dropbox
###########################
:slug: videocast-usando-o-dropbox
:date: 2009-02-07 14:26
:category:
:tags: portuguese

No começo do ano eu tinha escrito um
`post <http://blog.ogmaciel.com/?p=500>`__ sobre como usar o programa
`Dropbox <https://www.getdropbox.com>`__ junto com o gerenciador de
janelas `Openbox <http://icculus.org/openbox/index.php/Main_Page>`__
para criar um mecanismo de armazenamento, backup e sincronização de
arquivos com outros sistemas. Como meu sistema do trabalho é diferente
do sistema que uso em casa, o dropbox me ajuda a sincronizar de forma
super rápida e simples o conteudo de meus arquivos entre os sistemas, o
que me permite ter a mesma configuração de um programa não importa qual
computador eu esteja usando.

O vídeo abaixo tenta mostrar como usar o dropbox para sincronizar seus
arquivos de configurações usando links simbólicos. Este método funciona
bem com o GNU/Linux, Windows e o Mac OS, como demonstrado no vídeo.

(caso o vídeo não apareça em seu leitor de notícias, clique
`aqui <http://video.google.com/videoplay?docid=2320732265509847286&hl=en>`__)

O meu script-zinho que eu uso toda vez que instalo o dropbox em um
sistema novo para criar os links segue abaixo:

`` cd rm -rf .gnupg ln -s Dropbox/dotfiles/.gnupg . ln -s Dropbox/dotfiles/.vim . ln -s Dropbox/dotfiles/.vimrc . ln -s Dropbox/dotfiles/commit.tpl . rm .bashrc ln -s Dropbox/dotfiles/.bashrc . ln -s Dropbox/dotfiles/.gnome-rdp.db . ln -s Dropbox/dotfiles/.hgrc . ln -s Dropbox/dotfiles/.conaryrc . ln -s Dropbox/dotfiles/.rmakerc . cd ~/.config ln -s Dropbox/dotfiles/conary . ``

Espero que vocês gostem do vídeo e qualquer dúvida é só me deixar um
comentário por aqui.
