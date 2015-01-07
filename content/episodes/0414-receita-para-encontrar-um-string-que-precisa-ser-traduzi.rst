Receita para encontrar um string que precisa ser traduzido
##########################################################
:slug: receita-para-encontrar-um-string-que-precisa-ser-traduzi
:date: 2006-10-11 14:54
:category: English
:tags: portuguese

Alguem compartilhou um script que ajuda na hora de procurar o pacote que
contem uma mensagem que precisa ser traduzida ou revisada. Crie um novo
arquivo e cole o seguinte codigo:

    #!/bin/bash string=”^\_:” if [ “$1” != “” ] ; then string=$1 fi for
    i in /usr/share/locale-langpack/pt\_BR/LC\_MESSAGES/\*.mo do if
    msgunfmt $i 2> /dev/null \| msggrep -T -e “$string” 2>/dev/null \|
    grep “.” ; then echo $i echo fi done

E’ importante checar se o caminho **/usr/share/locale-langpack/** existe
em sua distribuicao. Como no trabalho uso o `Foresight
Linux <http://www.foresightlinux.com/>`__, o caminho e’ na verdade
**/usr/share/locale/**. Depois voce pode executa-lo pelo console e,
depois de descobrir o nome do pacote que contem a mensagem com
problemas, procura-lo
`aqui <https://launchpad.net/distros/ubuntu/edgy/+lang/pt_BR>`__. Ai’
sim, voce podera’ adicionar uma sugestao para esta mensagem na propria
pagina (assumindo que voce esta’ cadastrado(a) no
`Rosetta <https://launchpad.net/rosetta>`__) ou se preferir, enviar uma
mensagem para os
`tradutores <https://launchpad.net/people/ubuntu-l10n-pt-br>`__, nos
explicando sobre o problema e onde encontra-lo.

**Interessado em aprender mais sobre o Ubuntu em portuguÃªs? Comece
`aqui <http://wiki.ubuntubrasil.org/ComeceAqui>`__!**

**Atualizacao**: Caso voce tenha salvo este arquivo com o nome de
findString.sh e esteja recebendo muito “lixo” na saida, redirecione o
resultado para um arquivo e os erros para outro (ou para /dev/null).

    . findString.sh *[palavra a ser procurada]* 2>/dev/null >
    results.txt
