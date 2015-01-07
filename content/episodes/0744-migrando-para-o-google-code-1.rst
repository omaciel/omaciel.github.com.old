Migrando para o Google Code #1
##############################
:slug: migrando-para-o-google-code-1
:date: 2008-04-01 22:25
:category: English
:tags: portuguese

Na semana passada eu tinha `escrito <http://www.ogmaciel.com/?p=453>`__
no meu blog em Inglês sobre minha tentativa frustrada em migrar o meu
projeto `BillReminder <http://code.google.com/p/billreminder/>`__ para o
**Google Code**. Bem, graças a algumas boas almas da Google, eu
finalmente consegui migrar o projeto!

Eu realmente tinha a expectativa de um processo completo e tranquilo mas
(felizmente?) existem vários passos manuais que **você** deve efetuar
antes de ter a mesma estrutura (hmmm… não igual, mas algo útil) da
`SourceForge <http://www.sf.net>`__. Imaginei que isso serviria para
mais alguém que esteja passando pela mesma situação e decidi escrever
aqui os passos que tomei. Espero que seja útil.

Eu **realmente** recomendo que você se cadastra na lista de discussão
`Hosting at Google
Code <http://groups.google.com/group/google-code-hosting>`__\ … vai ser
lá que você vai encontrar ajuda e boas dicas!

Uma vez você tenha o seu projeto criado (foi um processo manual feito
por um empregado da Google), você provavelmente vai querer migrar o
código fonte do seu projeto na SourceForge. Isso pode ser feito bem
fácil executando os seguintes comandos:

    svnsync init —username **[usuário]**
    https://\ **[projeto]**.googlecode.com/svn
    https://\ **[projeto]**.svn.sourceforge.net/svnroot/\ **[projeto]**
    svnsync sync —username **[**\ **usuário**\ **]**
    https://\ **[projeto]**.googlecode.com/svn

Obviamente você vai ter de modificar os comandos acima para usarem a sua
informação pessoal. É importante que você tenha a senha do seu
repositório (não confundir com a senha do gmail) que pode ser encontrada
na página de configurações do seu projeto, pois isso será utilizado.

O segundo comando, responsável por sincronizar o seu novo repositório
falhou para mim algumas vezes… mas não se desespere. Para mim, **quatro
vezes** foi o número mágico! :)

Deste ponto em diante, eu modifiquei algumas configurações do meu
projeto e até mesmo consegui adicionar o lançamento mais recente na
página de downloads. Infelizmente os meus relatórios de erros, patches e
recursos e pedidos de ajuda não foram parte da migração e eu ainda tenho
de ler sobre como fazer isso (espero) sem muita complicação. Mais sobre
o assunto em um próximo post, onde também pretendo discutir sobre como
criar listas de discussão e commits para os desenvolvedores.

Então, não se esqueça de atualizar o endereço do repositório do código
do BillReminder:

    ``svn checkout http://billreminder.googlecode.com/svn/trunk/ billreminder-read-only``
