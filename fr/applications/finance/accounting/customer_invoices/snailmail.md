# Envoi postal

L’envoi de courrier direct peut être une stratégie efficace pour attirer
l’attention des gens, en particulier lorsque leurs boîtes de réception
d’emails sont surchargés. Avec Odoo, vous avez la possibilité d’envoyer des
factures et des rapports de suivi par courrier postal dans le monde entier,
tout cela à partir de votre base de données.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Factures clients pour
activer l’option Envoi postal.

Pour faire de l’option une fonctionnalité par défaut, cochez la case à côté de
Envoyer par la poste dans la section Options d’envoi par défaut.

![Dans les paramètres, activez la fonctionnalité Envoi postal dans Odoo
Comptabilité.](../../../../_images/setup-snailmail.png)

## Envoyer des factures par la poste

Ouvrez votre facture, cliquez sur Envoyer & Imprimer et sélectionnez Envoyer
par la poste. Assurez-vous que l’adresse de votre client est correcte, y
compris le pays, avant d’envoyer la lettre.

Important

Votre document doit respecter les règles suivantes pour passer la validation
avant d’être envoyé :

  * Les marges doivent être de **5 mm** de chaque côté. Comme Odoo force les marges extérieures en les remplissant de blanc avant d’envoyer le document par la poste, il peut arriver que la personnalisation de l’utilisateur soit coupée si elle dépasse les marges. Pour vérifier les marges, activez le [mode développeur](../../../general/developer_mode.html#developer-mode), allez aux Paramètres généraux ‣ Technique ‣ Section Analyse : Format de papier.

  * Un carré de **15 mm sur 15 mm** dans le coin inférieur gauche doit rester libre.

  * The postage area has to stay clear ([`download the snailmail PDF template`](../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf) for more details).

  * Pingen (le fournisseur de services d’envoi postal d’Odoo) scanne la zone pour traiter l’adresse, donc si quelque chose est écrit en dehors de la zone, il n’est pas compté comme faisant partie de l’adresse.

## Tarification

Snailmail is an [In-app purchases
(IAP)](../../../essentials/in_app_purchase.html) service that requires prepaid
stamps (=credits) to work. Sending one document consumes one stamp.

Pour acheter des timbres, allez à Comptabilité ‣ Configuration ‣ Paramètres ‣
Factures clients : Envoi postal, cliquez sur Acheter des crédits, ou allez aux
Paramètres ‣ Achats In-App : Odoo IAP, et cliquez sur Voir mes services.

Pour plus d'infos

[Odoo’s IAP Privacy Policy](https://iap.odoo.com/privacy#header_4)

