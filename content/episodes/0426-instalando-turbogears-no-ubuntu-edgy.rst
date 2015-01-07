Instalando TurboGears no Ubuntu Edgy
####################################
:slug: instalando-turbogears-no-ubuntu-edgy
:date: 2006-10-25 03:54
:category:
:tags: portuguese

Devido ao meu trabalho com python e
`TurboGears <http://www.turbogears.org>`__ em meu novo emprego, decidi
procurar informaÃ§Ãµes sobre como instalar o TurboGears no Ubuntu
Edgy.Â  A
“\ `receita <http://trac.turbogears.org/turbogears/wiki/UbuntuInstall>`__"
foi mais simples de achar que eu tinha imaginado:

#. Primeiro, baixe o script ez-setup nesta
   `pÃ¡gina <http://www.turbogears.org/download/nix.html>`__.
#. Caso vocÃª tenha uma instalaÃ§Ã£o ainda recente, instale o **gcc**
   com o comando:

-  sudo aptitude install gcc

Depois, instale os pacotes **libc6-dev** e **python-dev**:

-  sudo aptitude install libc6-dev python-dev

Execute o script ez-setup:

-  sudo python ez\_setup.py

Execute:

-  sudo easy\_install -f
   `http://www.turbogears.org/download/index.html <http://www.turbogears.org/download/index.html>`__
   —script-dir /usr/local/bin TurboGears

Por Ãºltimo, instale python-profiler:

-  sudo aptitude install python-profiler.

Para testar sua instalaÃ§Ã£o, inicie o TubroGears com o comando:

    tg-admin toolbox start -n

… e aponte seu navegador preferido para http://localhost:7654 e
pronto!Â  Seja bem vindo Ã  interface de ferramentas do TurboGears!Â  ;)
