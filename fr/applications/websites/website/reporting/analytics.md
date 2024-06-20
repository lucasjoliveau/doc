# Analytique du site web

Website analytics helps website owners monitor how people use their site. It
provides data on visitor demographics, behavior, and interactions, helping
improve websites and marketing strategies.

You can track your Odoo website’s traffic using Plausible.io or Google
Analytics. We recommend using Plausible.io as it is privacy-friendly,
lightweight, and easy to use.

Le tableau de bord analytique de Plausible est également intégré à Odoo et est
accessible via Site Web ‣ Analyse ‣ Analytique.

## Plausible.io

Odoo hosts its own Plausible.io server and provides a free and ready-to-work
Plausible.io solution for **Odoo Online** databases. Odoo automatically
creates and sets up your account. You can start using it by going to Website ‣
Reporting ‣ Analytics.

Note

**Si vous avez déjà un compte Plausible.io** et si vous voulez le connecter à
votre base de données Odoo Online, vous devez créer deux
`ir.config.parameters` pour utiliser les serveurs Plausible.io’s. Pour ce
faire, activez le [mode
développeur](../../../general/developer_mode.html#developer-mode) et allez aux
Paramètres généraux ‣ Technique – Paramètres système. Cliquez sur Nouveau et
remplissez les champs Clé et Valeur suivants :

Clé | Valeur  
---|---  
`website.plausible_script` | `https://plausible.io/js/plausible.js`  
`website.plausible_server` | `https://plausible.io`  
  
Suivez ensuite les étapes ci-dessous pour connecter votre compte existant avec
les serveurs Plausible.io.

Si votre base de données est hébergée sur **Odoo.sh** ou **On-premise** ou si
vous voulez utiliser votre propre compte Plausible.io, procédez comme suit :

  1. Créez ou connectez-vous à un compte Plausible en cliquant sur le lien suivant : <https://plausible.io/register>.

  2. Si vous créez un nouveau compte, suivez les étapes de l’inscription et d’activation. Lorsqu’il vous est demandé de fournir les détails de votre site web, ajoutez son Domaine sans `www` (par ex. `example.odoo.com`) et modifiez le Fuseau horaire d’analyse si nécessaire. Cliquez sur Ajouter un snippet pour procéder à l’étape suivante. Ignorez les instructions pour Ajouter un snippet JavaScript et cliquez sur Commencer à collecter des données.

  3. Lorsque vous avez terminé, cliquez sur le logo de Plausible dans la partie supérieure gauche de la page pour accéder à [votre liste de sites web](https://plausible.io/sites), puis cliquez sur l’icône d’engrenage à côté du site web.

![Cliquez sur l'icône d'engrenage dans la liste des sites
web.](../../../../_images/plausible-gear-icon.png)

  4. Dans la barre latérale, sélectionnez Visibilité, puis cliquez sur \+ Nouveau lien.

  5. Saisissez un Nom, laissez le champ Mot de passe vide, puisque l’intégration du tableau de bord de Plausible Analytics dans Odoo ne le prend pas en charge, puis cliquez sur Créer un lien partagé.

![Création d'identifiants pour le nouveau lien
partagé](../../../../_images/plausible-create-sharedlink.png)

  6. Copiez le lien partagé.

![Copier l'URL du lien partagé de Plausible.io](../../../../_images/plausible-
copy-sharedlink.png)

  7. Dans Odoo, allez à Site Web ‣ Configuration ‣ Paramètres.

  8. Dans la section Référencement, activez l’option Plausible Analytics, puis copiez le Lien partagé et cliquez sur Enregistrer.

Astuce

Si vous avez [plusieurs sites web](../configuration/multi_website.html),
ajoutez vos sites web à votre compte Plausible.io en allant à
<https://plausible.io/sites> et en cliquant sur \+ Ajouter un site web. Dans
Odoo, dans les **paramètres de Site Web** , assurez-vous de sélectionner le
site web dans le champ Paramètres du site web avant de coller le Lien partagé.

Note

Odoo vise automatiquement deux objectifs personnalisés : `Génération de
pistes` et `Boutique`.

Pour plus d'infos

[Documentation de Plausible Analytics](https://plausible.io/docs)

## Google Analytics

Pour suivre le trafic de votre site Odoo avec Google Analytics :

  1. Créez ou connectez-vous à un compte Google en utilisant le lien suivant : <https://analytics.google.com>.

  2.      * Si vous configurez Google Analytics pour la première fois, cliquez sur Commencer à mesurer et passez par l’étape de création de compte.

     * Si vous avez déjà un compte Google Analytics, connectez-vous et cliquez sur l’icône d’engrenage dans le coin inférieur gauche de la page pour accéder à la page **Admin**. Puis, cliquez sur \+ Créer une propriété.

![ID de mesure dans Google Analytics.](../../../../_images/GA-add-
property.png)

  3. Complétez les étapes suivantes : [création de propriété](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property), les détails de l’entreprise et les objectifs de l’entreprise.

  4. À l’étape de la **Collecte de données** , choisissez la plateforme Web.

![Choisissez une plateforme pour votre propriété Google
Analytics.](../../../../_images/GA-platform.png)

  5. Configurez votre flux de données : Précisez l”URL de votre site web et un Nom de flux, puis cliquez sur Créer un flux.

  6. Copiez l”ID de mesure.

![ID de mesure dans Google Analytics.](../../../../_images/GA-measurement-
id.png)

  7. Dans Odoo, allez à Site Web ‣ Configuration ‣ Paramètres.

  8. Dans la section Référencement, activez l’option Google Analytics, puis collez l”ID de mesure et cliquez sur Enregistrer.

Astuce

Si vous avez [plusieurs sites web](../configuration/multi_website.html) avec
des domaines distincts, il est recommandé de créer [une
propriété](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property)
par domaine. Dans Odoo, dans les **paramètres de Site Web** , assurez-vous de
sélectionner le site web dans le champ Paramètres du site web avant de coller
l”ID de mesure.

Pour plus d'infos

[Documentation de Google sur la configuration d’Analytics pour un site
web](https://support.google.com/analytics/answer/1008015?hl=en/)

## Google Tag Manager

GTM is a tag management system that allows you to easily update measurement
codes and related code fragments, collectively known as tags on your website
or mobile app, directly through the code injector.

Avertissement

Google Tag Manager may not be compliant with local data protection
regulations.

To use GTM, proceed as follows:

  1. Create or sign in to a Google account by going to <https://tagmanager.google.com/>.

  2. In the Accounts tab, click Create account.

  3. Enter an Account Name and select the account’s Country.

  4. Enter your website’s URL in the Container name field and select the Target platform.

  5. Click Create and agree to the Terms of Service.

  6. Copy the `<head>` and `<body>` codes from the popup window. Then, go to your website, click Edit, go to the Themes tab, scroll down to the Website Settings section, then click <head> and </body> to paste the codes.

![Install Google Tag Manager](../../../../_images/gtm-codes.png)

Note

The data is collected in the marketing tools used to monitor the website
(e.g., Google Analytics, Plausible, Facebook Pixel), not in Odoo.

  *[GTM]: Google Tag Manager

