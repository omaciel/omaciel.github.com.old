AtualizaÃ§Ãµes para o Nokia N800 e Dica #1
##############################################
:slug: atualizacoes-para-o-nokia-n800-e-dica-1
:date: 2007-07-06 18:16
:category:
:tags: portuguese

Hoje foi anunciado o lanÃ§amento da antecipada atualizaÃ§Ã£o do
`Internet Tablet OS 2007
edition <http://maemo.org/news/view/1183705330.html>`__, que inclui
suporte para o Skype. plug-in para navegadores AdobeÂ® FlashÂ® 9,
melhorias no uso online e suporte para cartÃµes de memÃ³ria de atÃ©
8 GB. TambÃ©m um pouco de “perfumaria” incluÃ­do neste lanÃ§amento! :)

InstruÃ§Ãµes sobre como atualizar seu sistema pode ser encontrado
`aqui <http://maemo.org/community/wiki/howto_flashlatestnokiaimagewithlinux/>`__,
mas vou quebrar teu galho e te dar uma soluÃ§Ã£o mais simples e
mastigada. Primeiramente, baixe o arquivo
`flasher-3.0 <http://maemo.org/downloads/d3.php,>`__ e o
`arquivo <http://tablets-dev.nokia.com/nokia_N800.php>`__ de
atualizaÃ§Ã£o (para o meu N800 eu baixei o arquivo
RX-34\_2007SE\_4.2007.26-8\_PR\_COMBINED\_MR0\_ARM.bin file).

**OBSERVAÃ‡Ã‚O**: O processe de atualizar o sistema do seu dispositivo
tambÃ©m chamado de flashing) vai **apagar** todas as suas
personalizaÃ§Ãµes e configuraÃ§Ãµes. **Eu recomendo que vocÃª faÃ§a
cÃ³pias de seguranÃ§a de seus arquivos importantes antes de continuar.**

Desligue seu dispositivo e conecte-o ao seu PC via um cabo USB. Agora,
abra um terminal e atualize seu sistema com o seguinte comand:

    sudo ./flasher-3.0 -f -F
    RX-34\_2007SE\_4.2007.26-8\_PR\_COMBINED\_MR0\_ARM.bin -R

**Nota**: Caso vocÃª receba uma mensagem de erro de permissÃ£o, adicione
a permissÃ£o de execuÃ§Ã£o com o comando: chmod +x flasher-3.0

A seguinte mensagem serÃ¡ exibida no seu console:

    Suitable USB device not found, waiting

NÃ£o se preoculpe… Simplesmente ligue seu dispositivo e observe as
mensagens rolarem pelo terminal. Uma vez o processo tenha terminado,
desconecte seu dispositivo do PC e ligue-o para ver seu novo sistema. O
-R no comando acima Ã© suposto de re-iniciar o dispositivo apÃ³s a
atualizaÃ§Ã£o, mas para mim nÃ£o funcionou, e o dispositivo desligou.

O truque legal que eu aprendi hoje foi como habilitar o acesso do
usuÃ¡rio root no dispositivo sem ter de instalar qualquer pacote. Mais
uma vez, desligue seu dispositivo e conecte-o ao seu PC via o cabo USB.
Do terminal, execute o seguinte comando:

    sudo ./flasher-3.0 —enable-rd-mode

Ligue o dispositivo novamente e *voilÃ¡*! A prÃ³xima vez que vocÃª
reinicÃ¡-lo, vocÃª verÃ¡ vÃ¡rias mensagens em verde na tela, confirmando
que o processo funcionou. Agora Ã© sÃ³ instalar o Xterm e obter acesso
como root usando o comando:

    sudo gainroot

Agradecimentos para o **mgedmin** do canal #maemo por me guiar durante o
processo de atualizaÃ§Ã£o e **etrunko** por vÃ¡rias dicas, inclusive a
dica de acesso como root!

Existe tambÃ©m uma lista de repositÃ³rios para ambosN770 e
N800 \ `aqui <http://www.gronmayer.com/n800/repos/index.php?lang=en>`__!
