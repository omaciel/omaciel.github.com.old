[RESOLVIDO] HTML Scraping com Ruby
##################################
:slug: html-scraping-com-ruby
:date: 2006-07-14 15:19
:category:
:tags: portuguese

Tenho pelejado com um script em ruby para apanhar (ou em inglÃƒÂªs,
“scrap”) conteÃƒÂºdo de pÃƒÂ¡ginas de web de sites que usam o protocolo
https. SÃƒÂ³ para ilustrar o meu problema, vou usar o site que visito
todos os dias. ;)

    require ‘net/https’ host = “www.launchpad.net” port = 443 proxy =
    nil proxyport = nil h = Net::HTTP.new(host, port, proxy, proxyport)
    h.use\_ssl = true response, data = h.get(“/”, nill)

Quando executo este pequeno script (aqui usando o irb), recebo a
seguinte mensagem de erro:

    Net::HTTPBadResponse: wrong status line: “” from
    d:/ruby/lib/ruby/1.8/net/http.rb:1990:in \`read\_status\_line’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:1977:in \`read\_new’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:1046:in \`request’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:1033:in \`request’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:545:in \`start’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:1031:in \`request’ from
    d:/ruby/lib/ruby/1.8/net/http.rb:771:in \`get’ from (irb):7

AlguÃƒÂ©m sabe como posso fazer isso?

**AtualizaÃƒÂ§ÃƒÂ£o:** Aparentemente eu tinha usado **net/http**
invÃƒÂ©s de **net/https**\ … Como diz Homer Simpson: “Doh!”
