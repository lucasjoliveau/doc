# Envoi postal

L’envoi de courrier direct peut être une stratégie efficace pour attirer
l’attention des gens, en particulier lorsque leurs boîtes de réception
d’emails sont surchargés. Avec Konvergo ERP, vous avez la possibilité d’envoyer des
factures et des rapports de suivi par courrier postal dans le monde entier,
tout cela à partir de votre base de données.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Factures clients pour
activer l’option **Envoi postal**.

Pour faire de l’option une fonctionnalité par défaut, cochez la case à côté de
**Envoyer par la poste** dans la section **Options d’envoi par défaut**.

![Dans les paramètres, activez la fonctionnalité Envoi postal dans Konvergo ERP
Comptabilité.](../../../../_images/setup-snailmail.png)

## Envoyer des factures par la poste

Ouvrez votre facture, cliquez sur **Envoyer & Imprimer** et sélectionnez
**Envoyer par la poste**. Assurez-vous que l’adresse de votre client est
correcte, y compris le pays, avant d’envoyer la lettre.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Votre document doit respecter les règles suivantes pour passer la validation avant d’être envoyé :</p>
<ul>
<li><p>Les marges doivent être de <b>5 mm</b> de chaque côté. Comme Konvergo ERP force les marges extérieures en les remplissant de blanc avant d’envoyer le document par la poste, il peut arriver que la personnalisation de l’utilisateur soit coupée si elle dépasse les marges. Pour vérifier les marges, activez le <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez aux Paramètres généraux ‣ Technique ‣ Section Analyse : Format de papier.</p></li>
<li><p>Un carré de <b>15 mm sur 15 mm</b> dans le coin inférieur gauche doit rester libre.</p></li>
<li><p>The postage area has to stay clear (<a download="" href="../../../../_downloads/5b14d01e129cc51a32303602599b291f/snailmail-template.pdf"><code>download the snailmail PDF template</code></a> for more details).</p></li>
<li><p>Pingen (le fournisseur de services d’envoi postal d’Konvergo ERP) scanne la zone pour traiter l’adresse, donc si quelque chose est écrit en dehors de la zone, il n’est pas compté comme faisant partie de l’adresse.</p></li>
</ul>
</div>

## Tarification

Snailmail is an [In-app purchases
(IAP)](../../../essentials/in_app_purchase) service that requires prepaid
stamps (=credits) to work. Sending one document consumes one stamp.

Pour acheter des timbres, allez à Comptabilité ‣ Configuration ‣ Paramètres ‣
Factures clients : Envoi postal, cliquez sur **Acheter des crédits** , ou
allez aux Paramètres ‣ Achats In-App : Konvergo ERP IAP, et cliquez sur **Voir mes
services**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://iap.odoo.com/privacy#header_4">Konvergo ERP’s IAP Privacy Policy</a></p>
</div>

