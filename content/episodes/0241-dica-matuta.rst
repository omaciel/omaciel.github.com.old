Dica Matuta
###########
:slug: dica-matuta
:date: 2006-02-23 23:22
:category: English
:tags: portuguese

Sei que tenho andado meio sumido este ÃƒÂºltimos dias, mas com a minha
primeira prova para a certificaÃƒÂ§ÃƒÂ£o do RHCE marcada para amanhÃƒÂ£,
tenho ralado bastante, sem tempo livre para quase nada… Mesmo assim,
achei uma dica muito interessante hoje e parei um pouco com meu estudo
para compartilhar com vocÃƒÂªs…

VocÃƒÂª sabia que ext2 e ext3, por padrÃƒÂ£o, reservam %5 da capacidade
de cada partiÃƒÂ§ÃƒÂ£o para o root? Bem, eu nÃƒÂ£o sabia deste detalhe…
O motivo ÃƒÂ© para que, caso os usuÃƒÂ¡rios consumam todo o espaÃƒÂ§o
alocado na partiÃƒÂ§ÃƒÂ£o, qualquer programa que estiver sendo executado
como root (ou comandos que o root estiver executando) nÃƒÂ£o falhem
imediatamente.

Para recuperar este espaÃƒÂ§o, ÃƒÂ© sÃƒÂ³ usar o comando tune2fs. Como
meu laptop tem um disco de 30GB, o comando df -h / me diz:

    omaciel@merlin:~$ sudo df -h / Password: Filesystem Size Used Avail
    Use% Mounted on /dev/hda1 27G 3.9G 22G 16% /

Usando tune2fs com o parÃƒÂ¢metro -m para configurar a porcentagem de
espaÃƒÂ§o alocado para o root:

    omaciel@merlin:~$ sudo tune2fs -m 0 /dev/hda1 tune2fs 1.38
    (30-Jun-2005) Setting reserved blocks percentage to 0% (0 blocks)
    omaciel@merlin:~$ sudo df -h / Filesystem Size Used Avail Use%
    Mounted on /dev/hda1 27G 3.9G 23G 15% /

Ok, sÃƒÂ³ ganhei 1GB na brincadeira… Mas e se meu disco fosse de 200GB?
Ou 200TB? JÃƒÂ¡ imaginou reservar %5 deste espaÃƒÂ§o sÃƒÂ³ em caso as
partiÃƒÂ§ÃƒÂµes fiquem usadas?

Bem, de volta aos livros…
