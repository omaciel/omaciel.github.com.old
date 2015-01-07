BillReminder "It Puts the Lotion in the Basket" 0.3 lanÃ§ado
##############################################################
:slug: billreminder-it-puts-the-lotion-in-the-basket-03-lancado
:date: 2008-03-02 17:32
:category:
:tags: portuguese

|About BillReminder|

Ã‰ com enorme orgulho que venho anunciar o lanÃ§amento do meu projeto
hobby `BillReminder <http://billreminder.gnulinuxbrasil.org/>`__! A
estrada para chegar atÃ© a versÃ£o 0.3 mostrou ser algo muito educativo
para mim, e hoje olhando com nostalgia no dia que decidi “portar” o
cÃ³digo original escrito em C# para Python com o intuito de aprender um
pouco mais sobre Python, eu posso dizer que aprendi muito. TambÃ©m
conheci muita gente bacana pelo caminho, algumas delas responsÃ¡veis por
me ajudarem a manter o projeto ativo. Eu posso honestamente dizer que
toda vez que eu achava tempo livre para trabalhar neste projeto, eu
simplesmente perdia a noÃ§Ã£o do tempo. Quando eu me sinto inseguro
sobre meu conhecimento na Ã¡rea de programaÃ§Ã£o (ou quando algue me faz
sentir assim) eu olho para o que eu fiz atÃ© agora… pode nÃ£o ser o
melhor software por aÃ­, mas ele Ã© meu… escrito do zero!

Meu plano era lanÃ§ar o BillReminder no dia 15 de fevereiro, em
homenagem ao primeiro aniversÃ¡rio da minha segunda filha Kate. Mas
infelizmente eu estava lutando contra o tempo, com meu trabalho e vida
pessoal entrando na equaÃ§Ã£o. Eu gostaria de agradecer todas as pessoas
que tiraram um pouco do seu tempo para me enviar feedback e atÃ© mesmo
patches! Eu quero especialmente agradecer meu amigo **Luiz Armesto** por
ter ficado comigo o tempo todo, e compartilhando o mesmo entusiasmo por
estar criando algo do zero e se divertindo ao mesmo tempo!

EntÃ£o, o que hÃ¡ de novo nesta versÃ£o? Um monte de coisas:

O cÃ³digo base foi completamente re-escrito, e invÃ©s de listar todos os
arquivos que foram modificados, acho melhor somente comentar sobre as
coisas mais importantes:

**GLADE:** BillReminder 0.3 foi completamente re-escrito para remover
todos os arquivos glade e dependÃªncias. A idÃ©ia inicial era
simplesmente remover a dependÃªncia, mas tambÃ©m servir como um um
processo de aprendizado para mim (e eu acredito que os outros
colaboradores tambÃ©m vÃ£o concordar com isso). **DBUS:** A camada DBUS
recebeu muita atenÃ§Ã£o do Luiz Armesto, que a quebrou em chamadas
especÃ­ficas para separar o “motor” do cliente. **UI**: A interface
grÃ¡fica do cliente passou por uma sÃ©rie de modificaÃ§Ãµes e (espero)
melhorias. Provavelmente ainda nÃ£o estÃ¡ 100% compatÃ­vel com o HIG,
mas aceitaremos de bom grado suas sugestÃµes. **Gerenciamento de
erros**: Durante as Ãºltimas 8 semanas de desenvolvimento adotamos o
hÃ¡bito de criar relatÃ³rios de erro antes de consertÃ¡-los.
**TraduÃ§Ãµes:** Todos os colaboradores da Ãºltima versÃ£o responderam
com prontidÃ£o meu e-mail pedindo para atualizar suas traduÃ§Ãµes:

-  de.po: Sebastian Haselbeck
-  es.po: Gilberto J. Miralla
-  no\_NB.po: Tommy Mikkelsen
-  no.po: Tommy Mikkelsen
-  pt\_BR.po: FÃ¡bio Nogueira
-  sv.po: Daniel Nylander

VocÃª pode baixar o cÃ³digo fonte do BillReminder
`aqui <https://sourceforge.net/project/showfiles.php?group_id=161428>`__,
assim como tambÃ©m pacotes para o Ubuntu Hardy e Fedora 8, cortesia do
Luiz Armesto. UsuÃ¡rios do Foresight usando o novo alpha 4 podem
instalÃ¡-lo usando o conary… Pacotes para o Mandriva e Arch Linux devem
estar saindo em breve tambÃ©m!

Por favor, envie seu feedback construtivo, comentÃ¡rios e patches usando
nosso `tracker <https://sourceforge.net/tracker/?group_id=161428>`__.

.. |About BillReminder| image:: http://farm4.static.flickr.com/3257/2304206451_22fe1e67ce_o.png
   :target: http://www.flickr.com/photos/ogmaciel/2304206451/
