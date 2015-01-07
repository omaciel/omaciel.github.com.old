Reunião da equipe de traduções do GNOME Brasil
#################################################
:slug: reuniao-da-equipe-de-traducoes-do-gnome-brasil
:date: 2009-10-19 01:35
:category:
:tags: portuguese

Na noite de outubro 16 de 2009 aconteceu a primeira reunião da equipe de
traduções do **GNOME Brasil** já sobre a nova coordenação do **Rodrigo
Flores**. Infelizmente perdi o início da reunião mas o **Rodrigo** fez
um excelente trabalho em resumir os pontos discutidos e enviou para
todos da lista de discussão. O que segue abaixo é o conteúdo deste
e-mail, formatado por mim para (espero) melhor destacar os assuntos
discutidos:

#. **Manter padrões**:

   -  Uma das coisas que as vezes falhamos é em manter os padrões. As
      vezes um tradutor menos experiente acaba colocando maiúsculas onde
      não deve e isso sai do padrão. O que podemos fazer é criar uma
      página no wiki com os padrões e ir discutindo eles aqui na lista.
      Nomes de aplicativos que podem confundir a gente coloca também
      coloca em tabela.

          Ex: \| Eye of GNOME \| Visualisador de Imagens do GNOME \|

#. **Adequação a nova ortografia**:

   -  Inicialmente houve 3 alternativas (uma delas meio “inviável):

      -  Revisar tudo manualmente (essa é a inviável)
      -  Script que corrige palavras, pegando as que mais aparecem (isso
         deixaria só metade corrigido).
      -  Rodar um corretor ortográfico (pareceu ser a mais viável).

   -  Há corretores ortográficos já atualizados como o Aspell [1] e
      dicionários online com a nova ortografia [2]. O **Vladimir**
      também sugeriu um dicionário de papel da ABL com a nova ortografia
      [3].
   -  Para quando faremos essa mudança ? Uma sugestão do **John
      Wendell** é termos tudo traduzido para o **GNOME 3.0** (que pode
      ser lançado em 5 meses ou 11 meses) e anunciar isso como uma
      feature.

#. **Regra de crédito de autoria**:

   -  Decidimos que alguém só pode por seu nome no crédito de autoria se
      ele traduziu/arrumou o fuzzy de pelo menos 10 mensagens. Mas mesmo
      que se traduza menos que isso, o nome de quem traduziu vai pro
      Last Translator e pra mensagem de commit. Esse número pode ser
      discutido, mas o povo da reunião concordou com 10.

#. **String Freeze Break**:

   -  O **John Wendell** esclareceu para os presentes (inclusive para
      mim) o que era o **String Freeze Break** (e por que alguns módulos
      no String Freeze apareciam novas mensagens):

      -  [22:36:19      ] rodrigoflores\_, deixa eu explicar
      -  [16 22:36:31] isso só acontece quando o programador \*erra\*
      -  [16 22:36:56] mas por default as strings novas só aparecem
         \*se\* forem aprovadas
      -  [16 22:37:17] a pessoa pede, se for aprovado, o cara faz o
         commit

   -  Uma sugestão que ele deu, e que eu concordo é que todos assinem
      a\ **i18n** [4]. Lá vocês ficam sabendo o que foi aprovado e o que
      não foi e etc.
   -  Precisamos também escrever algo no Wiki sobre isso. O
      **Flamarion** ficou encarregado disso :-).

#. **Mudança nas “regras” de promoção**:

   -  Sugeri adicionarmos o item “Ter traduzido algo não trivial” na
      regra de promoção tradutor -> revisor. Um dos objetivos
      pretendidos disso é tentar fazer com que tradutores já em fase de
      serem promovidos traduzam mais coisas não triviais. A alteração
      não foi aceita, e os motivos disso foram que traduzir quantidade é
      diferente de traduzir com qualidade e que, revisores só devem
      aceitar se acharem que o cara é realmente para termos a confiança
      de que se o cara mandou pode subir pro repositório sem dor de
      cabeça. Como quase todo mundo na reunião topou, fica a mudança
      rejeitada.

#. **Tradução via Web**:

   -  Uma coisa que eu pedi que todos pensássemos sempre é em como
      melhorar nosso processo de tradução e nossas ferramentas e uma das
      coisas que vem aparecendo é a tradução online. O que eu quis
      salientar é que, IMHO, se isso existir, sou a favor que funcione
      como é no DL, onde o cara reserva, só ele mexe e depois disso ele
      marca como pronto. Uma coisa que me contaram (**John**) e que eu
      não sabia é que já existem planos para isso ser integrado no DL.
      Então me dei por satisfeito.
   -  Uma coisa levantada nesse tópico (e em alguns pontos do resto da
      reunião) é que não temos muita documentação para iniciantes. Seria
      legal se tivéssemos Screencasts, e mais coisa no Wiki que ajude
      aos novos tradutores. Talvez uma seção “Comece Aqui” já fosse bom.
      O **Flamarion** sugeriu uma reunião na qual discutiríamos somente
      sobre o Wiki. Sou a favor disso e por mim já podemos marcar a data
      :-).

Pontos extras (que eu esqueci de comentar)

-  Tradução incremental de documentações grandes:

   -  Algumas documentações como o Anjuta são grandes e difíceis de
      serem traduzidas. Não seria bom se traduzissemos 50 ou 100 strings
      de cada vez e isso fosse revisado, submetido e a tradução
      continuasse, ao invés de se traduzir tudo e revisar tudo de uma
      vez? Isso deixaria o tradutor/revisor mais atencioso e podendo
      trabalhar aos poucos (isso obviamente pode ser feito por ele mesmo
      sozinho, mas acho que uma revisão externa sempre ajuda, além do
      que evitaria ter que corrigir erros recorrentes que estão na
      tradução inteira).

-  Revisão obrigatória para módulos grandes:

   -  Alguns módulos grandes (anjuta e evolution) tem muitas mensagens e
      um erro ou outro pequeno sempre tem mais chance de aparecer
      independente do tradutor e da revisão que ele mesmo acaba fazendo
      (independente se ele é tradutor, revisor ou coordenador). O que eu
      proponho é que essa revisão seja obrigatória. Isso certamente vai
      atrasar um pouco o trabalho mas acho que vai melhorar bastante
      nosso processo.

#. `http://leonardof.org/2009/07/05/dicionario-para-aspell-agora-com-o-acordo-ortografico/pt/ <http://leonardof.org/2009/07/05/dicionario-para-aspell-agora-com-o-acordo-ortografico/pt/>`__
#. `http://www.priberam.pt/DLPO/ <http://www.priberam.pt/DLPO/>`__
#. `http://www.jacotei.com.br/dicionario-escolar-da-lingua-portuguesa-academia-brasileira-de-letras-letras-academia-brasileira-9788504011883.html?ordenarpor=3 <http://www.jacotei.com.br/dicionario-escolar-da-lingua-portuguesa-academia-brasileira-de-letras-letras-academia-brasileira-9788504011883.html?ordenarpor=3>`__
#. `http://mail.gnome.org/mailman/listinfo/gnome-i18n <http://mail.gnome.org/mailman/listinfo/gnome-i18n>`__
#. `http://mail.gnome.org/mailman/listinfo/gnome-pt\_br-list <http://mail.gnome.org/mailman/listinfo/gnome-pt_br-list>`__

Se você tiver alguma dúvida, sugestão, bronca ou está interessado em
ajudar com as traduções do GNOME (e não estou falando de traduzir para o
Ubuntu ou qualquer outra distribuição), não use a seção de comentários
deste blog, mas sim se cadastre na lista de discussão[5].
