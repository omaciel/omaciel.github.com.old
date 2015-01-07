Importante:  Senha do root em Breezy fÃƒÂ¡cil de visualizar
###############################################################
:slug: importante-senha-do-root-em-breezy-facil-de-visualizar
:date: 2006-03-12 22:37
:category: English
:tags: portuguese

De acordo com
`este <http://www.ubuntuforums.org/showthread.php?t=143334>`__ thread,
existe um problema com a informaÃƒÂ§ÃƒÂ£o que fica registrada em seu
computador durante a instalaÃƒÂ§ÃƒÂ£o do Breezy. Aparentemente, a senha
do usuÃƒÂ¡rio que ÃƒÂ© criado na instalaÃƒÂ§ÃƒÂ£o padrÃƒÂ£o fica
armazenada em arquivos log que podem ser acessados por qualquer
usuÃƒÂ¡rio. Se vocÃƒÂª se lembra, esta tambÃƒÂ©m ÃƒÂ© a senha utilizada
para logar como root!!!

Os arquivos que podem ter esta informaÃƒÂ§ÃƒÂ£o sÃƒÂ£o:

    /var/log/installer/cdebconf/questions.dat
    /var/log/installer/cdebconf/questions.dat
    /var/log/debian-installer/cdebconf/questions.dat
    /var/log/debian-installer/cdebconf/questions.dat

Eu nÃƒÂ£o posso afirmar isto, mas acredito que estes arquivos podem ser
removidos sem nenhum problema ao sistema. AtÃƒÂ© agora, ninguÃƒÂ©m
comprovou este mesmo problema com o Dapper.

**AtualizaÃƒÂ§ÃƒÂ£o**:Ã‚Â  Um fix jÃƒÂ¡ foi lanÃƒÂ§ado e pode ser lido
`aqui <http://www.ubuntu.com/usn/usn-262-1>`__!
