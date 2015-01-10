VocÃª sabe que estÃ¡ usando muito o Vim quando...
#####################################################
:slug: voce-sabe-que-esta-usando-muito-o-vim-quando
:date: 2007-07-20 02:56
:category: Portuguese
:tags: rpath

… vocÃª aperta a tecla ESC depois de preencher um formulÃ¡rio na web!

Eu realmente comecei a usar o **Vim** em tempo integral quando comecei a
trabalhar na **rPath** em outubro do ano passado. De vez em quando eu
aprendo um truque novo e resolvi compartilhÃ¡-los aqui com vocÃªs, e ao
mesmo tempo mantÃª-los em um lugar que eu possa sempre pesquisar (o
famoso “matar 2 pÃ¡ssaros com uma pedrada sÃ³!”).

O primeiro truque Ã© para aqueles momentos que vocÃª precisa fazer uma
substituiÃ§Ã£o genÃ©rica em um arquivo. Eu tinha aprendido antes que se
eu estivesse procurando pela palavra **Rei** e queria substituÃ­-la pela
palavra **Rainha**, o seguinte comando daria conta do recado:

    :%s/Rei/Rainha/g

O problema Ã© que este comando irÃ¡ substituir todas as ocorrÃªncias da
palavra **Rei**, incluindo **Reinaldo**, **Reino** Unido, e
derivaÃ§Ãµes! Eu sempre quiz saber como fazer o Vim me “perguntar” antes
de efetuar a substituiÃ§Ã£o. Foi meu amigo do trabalho **Stu** que me
mostrou o truque. Ã‰ sÃ³ adicionar um ‘c’ no final do comando:

    :%s/Rei/Rainha/gc

O segundo truque, tambÃ©m cortesia do Stu, mostra como vocÃª pode
executar um comando enquanto ainda dentro do Vim. Eu jÃ¡ sabia como
executar um comando e adicionar sua saÃ­da no prÃ³prio arquivo, mas o
truque dele Ã© Ãºtil quando vocÃª deseja testar um cÃ³digo que vocÃª
estÃ¡ editando. Por exemplo, imagina que vocÃª estÃ¡ editando um cÃ³digo
em Python e deseja testÃ¡-lo. Depois de salvar qualquer modificaÃ§Ã£o,
ainda dentro do vim, execute:

    :! python %

Isso irÃ¡ executar seu cÃ³digo, e uma vez ele tenha completado, vocÃª
serÃ¡ perguntado para digitar mais um comando ou simplesmente apertar a
tecla ENTER para voltar ao Vim.

Tudo bem que nÃ£o Ã© nada espetacular, mas valeu o meu dia! :)
