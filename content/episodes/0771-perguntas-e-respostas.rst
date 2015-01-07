Perguntas e Respostas
#####################
:slug: perguntas-e-respostas
:date: 2008-05-09 08:04
:category: English
:tags: portuguese

Os meus artigos com os dois vídeo aula
(`1 <http://blog.ogmaciel.com/?p=413>`__,
`2 <http://blog.ogmaciel.com/?p=415>`__) me trouxeram bastante
comentários de pessoas me parabenizando e/ou me perguntando sobre alguma
coisa. Devido ao grande número de perguntas, e o teor de perguntas,
decidi colocá-las em um novo artigo para que outras pessoas possam
aproveitar também. Então vamos lá…

O **Gercino Jr** perguntou: “Gostaria de saber sua opinião sobre em qual
linguagem começar” e “E se não for abuso de minha parte gostaria de lhe
perguntar também em qual linguagem o seu aplicativo
(`BillReminder <http://billreminder.gnulinuxbrasil.org/>`__) foi
escrito”

A resposta da primeira pergunta é um pouco difícil de responder sem
saber o propósito do projeto/programa que você está trabalhando. Apesar
que existem formas de fazer a mesma coisa com a grande maioria das
linguagens de programação, existem vantagens e desvantagens para cada
uma delas. A decisão mais importante que um desenvolvedor dve fazer é
justamente escolher a tecnologia que não somente atende as necessidades
do momento, mas também o permitirá expandir o projeto de acordo com o
rumo que ele tomar. Mas assumindo que o objetivo é aprender sobre
programação e desenvolver aplicativos independente de plataforma, então
a minha sugestão seria Python ou C#. Sobre o BillReminder, ele tinha
sido originalmente escrito em C# mas hoje em dia está completamente
escrito em python.

O **Uplink** perguntou: “Tu achas que é possível aprender a programar
utilizando só material em (pt\_br e/ou pt\_pt)?”

Inicialmente eu diria que sim, mas isto baseado na minha falta de
experiência com o mundo de informática no Brasil. Como moro fora do país
há mais de 17 anos, eu realmente não sei como está a situação em termos
de acesso à este tipo de material. Mas depois de conversar com outras
pessoas, aparentemente ainda não existe uma boa quantidade de material
no nosso idioma… é verdade isso?

O meu amigo **DenisBR** perguntou: “Quando vou executar a aplicação, o
computador onde vai rodar a aplicação precisa ter o glade instalado ?”

Você teria de distribuir o arquivo glade e a pessoa precisa ter o
libglade instalado no sistema, mas isso você pode resolver empacotando o
código (RPM, DEB, etc) e adicionando as dependências da forma
apropriada.

O **Luis Henrique** perguntou: “E aquele “hack” para rodar direto do vim
hein?”

hehehe Aprendi aquele no trabalho… você digita :! python % e aperta
enter. O “python” seria qual o comando a ser executado e o “%” significa
“este arquivo”. Ou seja, execute este arquivo usando o python.

O **Rafael Lippert** perguntou: “você conhece algo sobre pygame?”

Pouquíssimo mas é uma área que um dia vou acabar me envolvendo já que
tenho em mente criar um joguinho para as minhas filhas. :)

O  **Rafael C. de B.** perguntou: “Eu tentei fazer um video sobre django
mas tive que converter para avi para poder fazer upload, como vc fez
para deixar com a qualidade boa no google?”

Acredite ou não, nada! hehehe Simplesmente joguei o arquivo \*.ogv lá e
o Google fez o resto.

Meu amigo **Thadeu Penna** perguntou: “por que você escolheu a licença
non-derivative ?”

A resposta curta? Foi a primeira que eu encontrei que me satisfez só de
passar os olhos. Só depois do seu comentário que fui dar uma lida mais
séria, e foi aí que vi Vedada a Criação de Obras Derivadas. Ainda nção
sei bem o que pensar sobre o assunto e pode ser que eu venha mudar de
opinião…

O  **Felipe Diesel** perguntou: “Já que há um outro método de fazer,
setando as propriedades de cada elemento via código, qual o melhor
metódo? Ou melhor, por que alguns desenvolvedores escolhem um ou o
outro?”

A minha intenção quando decidi usar somente código e abolir o uso do
Glade foi só para que eu pudesse realmente aprender mais sobre PyGTK e
Python, sem ficar com aquela impressão que alguma mágica estava
acontecendo por trás dos bastidores. E realmente aprendi bastante ao
fazer isso, descobrindo que apesar da facilidade inicial que você tem ao
criar a interface, você tem muito mais controle sobre os objetos criados
quando se faz tudo na “unha”. Existe também o fato que você está
removendo mais uma dependência do seu aplicativo na hora de distribuir.

Bem, espero que as minhas respostas possam ajudar não somente quem
deixou seu comentário nos meus artigos, mas também quem estiver lendo
este artigo. E este fim de semana sai mais um vídeo aula! :)
