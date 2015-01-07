Rosetta takes a great step toward supporting upstream translations
##################################################################
:slug: rosetta-takes-a-great-step-toward-supporting-upstream-tr
:date: 2008-12-26 16:18
:category: English
:tags: english

`Danilo Å egan <http://danilo.segan.org/blog/>`__, lead developer for
the `Rosetta <https://www.launchpad.net/rosetta>`__ translation tool
sent an email to the Ubuntu translators list yesterday with some great
news related to the policy of how upstream translations are managed:

    Launchpad Translations has changed the translation precedence policy
    with the December release: now upstream (“packaged”) translations
    will be given more priority in specific cases. Yet, Launchpad
    Translations keeps the ability to override any specific upstream
    translation if so is desired. To illustrate when upstream
    translations have precedence, here’s an example: 1. GNOME Panel,
    message “\_Open”, untranslated 2. Ubuntu GNOME Panel message for
    “\_Open” is untranslated 3. Someone translates Ubuntu message in
    Launchpad to “\_Foo” 4. Upstream translates “\_Open” to “\_Bar” 5.
    When new upstream translation arrives, Launchpad makes “\_Bar”
    active over “\_Foo” (making “\_Foo” a suggestion) Example case where
    Launchpad translation takes precedence is: 1. GNOME Panel, message
    “\_Open”, translated to “Foow” 2. Ubuntu GNOME Panel translation for
    “\_Open” is imported and is now “Foow” 3. Someone fixes translation
    in Ubuntu to “\_Foo” 4. Upstream changes translation for “\_Open” to
    “Foo” 5. When new upstream translation arrives, Launchpad keeps
    “\_Foo” active over upstream’s “Foo”

Danilo also left me a comment on my last post, telling me that Rosetta
has supported gettext’s context feature for a while now which, if
properly used by the developers, could help giving translators a bit
more context information when doing their thing.

I’m so happy that I could literally cry right now!
