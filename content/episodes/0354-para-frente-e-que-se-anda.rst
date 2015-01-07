Para Frente Ãƒâ€° Que Se Anda
###################################
:slug: para-frente-e-que-se-anda
:date: 2006-07-14 18:22
:category:
:tags: portuguese

JÃƒÂ¡ faz mais ou menos uma semana que fiquei sabendo que a Canonical
criou um novo repositÃƒÂ³rio para distribuir certos pacotes
proprietÃƒÂ¡rios.Ã‚Â  Estou me referindo ao repositÃƒÂ³rio
dapper-commercial.Ã‚Â  Como eu jÃƒÂ¡ tinha baixado e instalado o skype,
w32codecs, e opera direto de seus prÃƒÂ³prios sites, nÃƒÂ£o tinha ainda
testado o reposÃƒÂ­torio, mas graÃƒÂ§as ÃƒÂ  dica de meu amigo `Thomaz
Leite <http://blog.thomazleite.com/articles/2006/07/09/novo-reposit%C3%B3rio-dapper-commercial-no-ubuntu-linux>`__,
venho tambÃƒÂ©m anunciar o procedimento em meu blog.

Primeiramente, adicione o novo repositÃƒÂ³rio em seu arquivo
/etc/apt/sources.list e inclua a seguinte linha:

    deb
    `http://archive.canonical.com/ubuntu <http://archive.canonical.com/ubuntu>`__
    dapper-commercial main

Depois ÃƒÂ© sÃƒÂ³ efetuar uma atualizaÃƒÂ§ÃƒÂ£o:

    sudo apt-get update

E instalar o opera por exemplo.Ã‚Â  Aparentemente o skype e w32codecs
tambÃƒÂ©m estariam disponÃƒÂ­veis neste repositÃƒÂ³rio mas infelizmente
ainda nÃƒÂ£o pude verificar.

Eu sinto que esta decisÃƒÂ£o de suportar pacotes proprietÃƒÂ¡rios pela
Canonical mostram de uma certa forma, um pouco de conflito de
interesses.Ã‚Â  Eu, particularmente, achei um pouco estranho pois o fato
ÃƒÂ© que estarÃƒÂ­amos desta forma apoiando o uso de software
proprietÃƒÂ¡rio, invÃƒÂ©s de apoiar o desenvolvimento de opÃƒÂ§ÃƒÂµes
livres para as mesmas tecnologias.

Hoje em dia, todo usuÃƒÂ¡rio quer ter acesso ÃƒÂ  sua multimÃƒÂ­dia e
ÃƒÂ  novas tecnologias, e a Canonical sabe que ÃƒÂ© vital para o seu
futuro manter o Ubuntu entre as possÃƒÂ­veis opÃƒÂ§ÃƒÂµes/alternativas
de software livre. Se agora eu quero usar o skype, ÃƒÂ© sÃƒÂ³
selecionÃƒÂ¡-lo da lista de software disponÃƒÂ­vel pelos repositÃƒÂ³rios
e pronto!Ã‚Â  Nada de configurar ou compilar pacotes com nomes que
comeÃƒÂ§am com a palavra lib\*.Ã‚Â  Mas de uma certa forma, eu nÃƒÂ£o
consigo deixar de pensar que ao fazer isso, estarÃƒÂ­amos “sabotando” as
chances que um ekiga ou wengo da vida teria para competir contra os
skypes da vida!
