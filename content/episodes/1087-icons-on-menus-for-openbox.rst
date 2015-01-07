Icons on menus for Openbox
##########################
:slug: icons-on-menus-for-openbox
:date: 2011-08-02 23:44
:category:
:tags: english

|Openbox "fancy" menu|

**Openbox 3.5.0** was
`released <http://openbox.org/wiki/Openbox:Changelog>`__ yesterday, and
with it several bugs got fixed and a few new features were added. Out of
these features the one that I liked most was the ability to add **icons
to menus** (and submenus as well)! Yeah, I know some other managers
already do this but for someone who enjoys running Openbox because of
its simplicity and keyboard binding limitless possibilities, I was sure
glad to see some eye candy make its way to it.

So, if you want to try it, make sure that your distribution has the new
Openbox compiled with Imlib2. Next, add the following line to the
**<menu>** section of your ***rc.xml*** file:

    <showIcons>yes</showIcons>

Then, modify your ***menu.xml*** by adding an icon attribute to what
ever menu item or menu you want to add an icon.

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

Make sure to restart openbox and enjoy your fancy new menu!

.. |Openbox "fancy" menu| image:: http://en.ogmaciel.com/wp-content/uploads/2011/08/openboxmenu.png
   :target: http://en.ogmaciel.com/wp-content/uploads/2011/08/openboxmenu.png
