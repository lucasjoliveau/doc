# Authentification à deux facteurs

L’authentification à deux facteurs (« 2FA ») est un bon moyen d’améliorer la
sécurité d’un compte, de réduire les risques qu’une autre personne parvienne à
se connecter à votre place.

Concrètement, cela signifie stocker un secret dans un _authenticator_
(généralement votre téléphone portable) et échanger un code de l’authenticator
lorsque vous essayez de vous connecter.

Cela signifie qu’un attaquant doit _à la fois_ avoir deviné (ou trouvé) votre
mot de passe et accéder (ou voler) votre authenticator, ce que est plus
difficile que simplement l’un ou l’autre.

## Exigences

Note

Ces listes ne sont que des exemples et ne constituent pas une recommandation
d’un logiciel spécifique.

Si vous n’en avez pas déjà un, vous devrez choisir un authenticator.

Les authenticators basés sur le téléphone sont les plus simples et les plus
courants, nous supposerons donc que vous en choisirez un et en installerez un
sur votre téléphone, par exemple [Authy](https://authy.com/),
[FreeOTP](https://freeotp.github.io/), [Google
Authenticator](https://support.google.com/accounts/answer/1066447?hl=en),
`LastPass Authenticator <https://lastpass.com/auth/ >`_, [Microsoft
Authenticator](https://www.microsoft.com/en-
gb/account/authenticator?cmp=h66ftb_42hbak), …; les gestionnaires de mots de
passe incluent également généralement la prise en charge de 2FA, par ex.
[1Password](https://support.1password.com/one-time-passwords/),
[Bitwarden](https://bitwarden.com/help/article/authenticator-keys/), …

À des fins de démonstration, nous utiliserons Google Authenticator (non pas
parce qu’il est meilleur, mais parce qu’il est assez courant).

## Configuration de l’authentification à deux facteurs

Une fois que vous avez votre authenticator de choix, accédez à l’instance Odoo
que vous souhaitez configurer 2FA, puis ouvrez Préférences (ou Mon profil):

![../../../_images/preferences.png](../../../_images/preferences.png)

Ouvrez l’onglet Sécurité du compte, puis cliquez sur le bouton Activer
l’authentification à deux facteurs:

![../../../_images/sec_tab.png](../../../_images/sec_tab.png)

Comme il s’agit d’une action sensible à la sécurité, vous devrez saisir votre
mot de passe :

![../../../_images/sec_enhanced.png](../../../_images/sec_enhanced.png)

Après quoi vous verrez cet écran avec un code-barres :

![../../../_images/totp_scan.png](../../../_images/totp_scan.png)

Dans la plupart des applications, vous pouvez simplement _scanner le code-
barres_ via l’authenticator de votre choix, l’authenticator se chargera alors
de toute la configuration :

![../../../_images/scan_barcode.jpg](../../../_images/scan_barcode.jpg)

Note

Si vous ne pouvez pas scanner l’écran (par exemple, parce que vous effectuez
cette configuration sur le même téléphone que l’application de
l’authenticator), vous pouvez cliquer sur le lien fourni ou copier le code
secret pour configurer manuellement votre authenticator :

![../../../_images/secret_visible.png](../../../_images/secret_visible.png)

![../../../_images/input_secret.png](../../../_images/input_secret.png)

Une fois cela fait, l’authenticator doit afficher un _code de vérification_
avec quelques informations d’identification utiles (par exemple, le domaine et
la connexion dont le code est) :

![../../../_images/authenticator.png](../../../_images/authenticator.png)

Vous pouvez maintenant saisir le code dans le champ Code de vérification, puis
cliquer sur le bouton Activer l’authentification à deux facteurs.

Félicitations, votre compte est maintenant protégé par une authentification à
deux facteurs !

![../../../_images/totp_enabled.png](../../../_images/totp_enabled.png)

## Se connecter

Vous devez maintenant vous déconnecter pour poursuivre.

Sur la page de connexion, saisissez le nom d’utilisateur et le mot de passe du
compte pour lequel vous avez configuré la 2FA, plutôt que d’entrer
immédiatement dans Odoo, vous obtiendrez maintenant un deuxième écran de
connexion :

![../../../_images/2fa_input.png](../../../_images/2fa_input.png)

Ouvrez votre authenticator, saisissez le code qu’il fournit pour le domaine et
le compte, validez et vous êtes à présent connecté.

Et voilà. À partir de maintenant, à moins que vous ne désactiviez 2FA, vous
aurez un processus de connexion en deux étapes plutôt que l’ancien processus
en une étape.

Danger

Ne perdez pas votre authenticator, si cela devait se produire, il faudra qu’un
_administrateur Odoo_ désactive 2FA sur le compte.

  *[2FA]: authentification à deux facteurs

