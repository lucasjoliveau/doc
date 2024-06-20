# Prospection de pistes

La prospection de pistes est une fonctionnalité qui permet aux utilisateurs de
CRM de générer de nouvelles pistes directement dans leur base de données Odoo.
Pour garantir la qualification des pistes, les résultats de la prospection
sont déterminés par une série de critères de filtrage, tels que le pays, la
taille de l’entreprise et le secteur d’activité.

## Configuration

Pour démarrer, allez à CRM ‣ Configuration ‣ Paramètres et activez Prospection
de pistes.

![Activer la prospection de pistes dans les paramètres d'Odoo
CRM.](../../../../_images/activate-lead-mining.png)

## Générer des pistes

Après avoir activé le paramètre Prospection de pistes, un nouveau bouton
appelé Génération de pistes est disponible pour être utilisé le pipeline CRM.
Les demandes de prospection de pistes sont également disponibles via CRM ‣
Configuration ‣ Demandes de prospection de pistes, ou via CRM ‣ Pistes ‣
Pistes où le bouton Générer des pistes est également disponible.

![Le bouton Générer des pistes pour utiliser la fonctionnalité de prospection
de pistes.](../../../../_images/generate-leads-button.png)

Cliquez sur le bouton Générer des pistes et une fenêtre apparaîtra offrant une
variété de critères pour générer des pistes.

![La fenêtre contextuelle avec les critères de sélection afin de générer des
pistes dans Odoo.](../../../../_images/generate-leads-popup.png)

Choisissez de générer des pistes pour des Sociétés pour obtenir uniquement des
informations sur la société ou Sociétés et leurs contacts pour obtenir des
informations sur la société et des coordonnées des employés individuels. En
ciblant Sociétés et leurs contacts, vous pouvez filtrer les contacts sur Rôle
ou sur Séniorité.

Des options de filtrage supplémentaires comprennent :

  * Taille: filtrer des pistes en fonction du nombre d’employés de l’entreprise

  * Pays: filtrer des pistes en fonction du pays (ou des pays) dans lequel (lesquels) elles sont situées

  * États: filtrer davantage les pistes en fonction de l’État dans lequel elles sont situées, le cas échéant

  * Secteurs d’activité: filtrer des pistes en fonction du secteur d’activité spécifique dans lequel elles sont actives

  * Équipe commerciale: choisir l’équipe commerciale à laquelle les pistes seront attribuées

  * Vendeur: choisir à quelle(s) personne(s) de l’équipe commerciale les pistes seront attribuées

  * Étiquettes par défaut: choisir les étiquettes qui s’appliquent directement aux pistes une fois trouvées.

Note

Assurez-vous d’être au courant des dernières réglementations de l’UE lorsque
vous recevez des coordonnées. Vous trouverez plus d’informations sur le
Règlement général sur la protection des données sur [Odoo
RGPD](http://odoo.com/gdpr).

## Tarification

La prospection de pistes est une fonctionnalité _Achats In-App_ et chaque
piste générée coûte un crédit.

L’option de générer Sociétés et leurs contacts coûte un crédit additionnel par
contact généré.

Note

Obtenez ici plus d’informations sur la tarification: [Génération de pistes par
Odoo IAP](https://iap.odoo.com/iap/in-app-services/167?).

Pour acheter des crédits, allez à CRM ‣ Configuration ‣ Paramètres. Dans la
section Génération de pistes, sous la fonctionnalité Prospection de pistes,
cliquez sur Acheter des crédits.

![Acheter des crédits depuis les paramètres de la prospection de
pistes](../../../../_images/buy-lead-mining-credits-setting.png)

Il est aussi possible d’acheter des crédits en allant aux Paramètres ‣
Paramètres généraux. Dans la section Achats In-App, sous la fonctionnalité
Odoo IAP, cliquez sur Voir mes services.

![Acheter des crédits via les paramètres Odoo IAP.](../../../../_images/view-
my-services-setting.png)

Note

Enterprise Odoo users with a valid subscription get free credits to test IAP
features before deciding to purchase more credits for the database. This
includes demo/training databases, educational databases, and one-app-free
databases.

Pour plus d'infos

[In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

  *[IAP]: In-App Purchase

