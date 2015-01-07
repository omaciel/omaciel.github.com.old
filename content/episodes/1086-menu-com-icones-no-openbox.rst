Menu com ícones no Openbox
###########################
:slug: menu-com-icones-no-openbox
:date: 2011-08-02 23:43
:category: English
:tags: portuguese

|Openbox "fancy" menu|

O \ **Openbox 3.5.0** foi
`lançado <http://openbox.org/wiki/Openbox:Changelog>`__ ontem, e com ele
vários problemas (bugs) foram resolvidos e alguns novos recursos foram
adicionados. Dentre estes novos recursos, o que eu gostei mais foi poder
adicionar **ícones aos menus** (e submenus também)! Tá, eu sei que
outros gerenciadores fazem isso, mas para alguém que como eu curto o
Openbox por sua simplicidade e possibilidades ilimitadas de atalhos de
teclado, eu fiquei super empolgado de ver um pouco de “eye candy” ser
adicionado ao projeto.

Então, se você estiver interessado em experimentar isso, certifique-se
que sua distribuição já atualizou o Openbox e que ele foi compilado
com\ **Imlib2**. Aí, adicione a seguinte linha na seção \ **<menu>** do
seu arquivo \ ***rc.xml***:

    <showIcons>yes</showIcons>

Depois é modificar o seu arquivo ***menu.xml*** à gosto, adicionando um
atributo **icon** no ítem de menu ou menu desejado.

::

    <menu id="apps-net-menu" icon="/usr/share/icons/Tango/24x24/apps/internet-web-browser.png"/>
    <menu id="apps-net-menu" label="Internet">
        <menu id="apps-net-browsers" label="Browsers">
            <item label="Firefox" icon="/usr/share/icons/hicolor/24x24/apps/firefox.png">
            <action name="Execute">
              <command>firefox</command>
              <startupnotify>
                <enabled>yes</enabled>
                <wmclass>Firefox</wmclass>
              </startupnotify>
            </action>
            </item>
            .
            .
            .
    </menu>

Lembre-se de re-iniciar o openbox e curta o seu novo menu!

.. |Openbox "fancy" menu| image:: http://en.ogmaciel.com/wp-content/uploads/2011/08/openboxmenu.png
   :target: http://en.ogmaciel.com/wp-content/uploads/2011/08/openboxmenu.png
