Ubuntu Tip #1974: Vim
#####################
:slug: ubuntu-tip-1974-vim
:date: 2006-12-03 04:56
:category: English
:tags: portuguese

Hoje conversando com o `KurtKraut <http://kurtkraut.wordpress.com/>`__
pelo Ekiga, descobri por acidente que o pacote vim nÃ£o vem instalado
por padrÃ£o no Ubuntu Edgy!!!Â  Pode isso?Â  Por algum motivo, o vim foi
subsituÃ­do pelo vim-common, que nÃ£o possui (atÃ© onde pude comprovar)
todos os recursos do vim “normal”.

EntÃ£o, para reparar este grave erro:

    sudo aptitude install vim

Agora, para testar a colorizaÃ§Ã£o de sintaxe automÃ¡tica, por exemplo,
digite no vim:

    :syntax on
