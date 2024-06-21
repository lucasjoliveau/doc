# Paiements par lot : Prélèvement SEPA (SDD)

SEPA, l’espace unique de paiements en euros, est une initiative d’intégration
des paiements de l’Union européenne en vue de simplifier les virements
bancaires en euros. Grâce au **Prélèvement SEPA** (SEPA Direct Debit - SDD),
vos clients peuvent signer un mandat qui vous autorise à prélever les
paiements futurs sur leurs comptes bancaires. C’est particulièrement utile
pour les paiements récurrents basés sur un abonnement.

Vous pouvez enregistrer les mandats des clients dans Konvergo ERP et générer des
fichiers `.xml` contenant les paiements en attente effectués avec un mandat
SDD.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><div class="line-block">
<div class="line">Le prélèvement SEPA est pris en charge par tous les pays SEPA, ce qui inclut les 27 États membres de l’Union européenne ainsi que d’autres pays.</div>
<div class="line"><a href="https://www.europeanpaymentscouncil.eu/document-library/other/epc-list-sepa-scheme-countries">Liste de tous les pays SEPA</a>.</div>
</div>
</div>

## Configuration

Allez à l’application Comptabilité ‣ Configuration ‣ Paramètres, activez
**Prélèvement SEPA (SDD)** , et cliquez sur **Enregistrer**. Saisissez
l”**Identifiant créancier** de votre entreprise. Ce numéro est fourni par
votre établissement bancaire ou par l’autorité chargée de les délivrer.

![Ajoutez un Identifiant créancier SEPA à Konvergo ERP
Comptabilité](../../../../_images/creditor-identifier.png)

## Mandats de prélèvement SEPA

### Créer un mandat

Le mandat SDD est le document que vos clients signent pour vous autoriser à
prélever de l’argent directement sur leurs comptes bancaires.

Pour créer un nouveau mandat, allez à l’application Comptabilité ‣ Clients ‣
Mandats de prélèvement, sur **Créer** , et complétez le formulaire. Exportez
le fichier PDF en cliquant sur **Imprimer**. Il incombe alors à votre client
de signer ce document. Une fois le document signé, chargez-le et cliquez sur
**Valider** pour lancer l’exécution du mandat.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Assurez-vous que les <b>coordonnées bancaires IBAN</b> sont correctement enregistrés dans la fiche de contact du débiteur, dans l’onglet <b>Comptabilité</b> et dans vos propres paramètres de <a href="../bank">Compte bancaire</a>.</p>
</div>

### Le prélèvement SEPA comme mode de paiement

Le prélèvement SEPA peut être utilisé comme un mode de paiement à la fois sur
votre **eCommerce** et sur le **Portail client** en activant Prélèvement SEPA
en tant que **Fournisseur de paiement**. Avec ce mode, vos clients peuvent
créer et signer eux-mêmes leurs mandats.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Fournisseurs de
paiement, cliquez sur _Prélèvement SEPA_ et configurez-le selon vos besoins.
Pour ce faire, allez à l’application Comptabilité ‣ Configuration ‣
Fournisseurs de paiement, cliquez sur **Prélèvement SEPA**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Assurez-vous de changer le champ <b>Statut</b> en <b>Activé</b> et de cocher l’option <b>Signature en ligne</b>, puisqu’elle est nécessaire pour autoriser vos clients à signer leurs mandats.</p>
</div>

Les clients utilisant le prélèvement SEPA comme mode de paiement sont invités
à ajouter leur IBAN, leur adresse email et à signer leur mandat de prélèvement
SEPA.

### Résilier ou révoquer un mandat

Les mandats de prélèvement sont automatiquement résiliés après leur **Date de
fin**. Si ce champ est laissé vide, le mandat continue à être **Actif**
jusqu’à ce qu’il est **Résilié** ou **Révoqué**.

En cliquant sur **Résilier** la date de fin du mandat est mise à jour à la
date du jour. Cela signifie que les factures émises après cette date ne seront
plus traitées par un paiement SDD.

En cliquant sur **Révoquer** , vous désactivez immédiatement le mandat. Aucun
paiement SDD ne peut plus être enregistré, quelle que soit la date de la
facture. Toutefois, les paiements qui ont déjà été enregistrés sont toujours
inclus dans le prochain fichier SDD `.xml`.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Une fois qu’un mandat a été <b>résilié</b> ou <b>révoqué</b>, il ne peut pas être réactivé.</p>
</div>

## Être payé avec les paiements par lot du prélèvement SEPA

### Factures clients

Vous pouvez enregistrer des paiements SDD pour les factures émises aux clients
qui ont un mandat de prélèvement SEPA actif.

Pour ce faire, ouvrez la facture, cliquez sur **Enregistrer un paiement** et
choisissez **Prélèvement SEPA** comme mode de paiement.

### Générer des fichiers de prélèvement SEPA `.XML` pour soumettre des
paiements

Les fichiers `.xml` contenant toutes les instructions de paiement SDD peuvent
être chargés dans l’interface de votre banque en ligne pour traiter tous les
paiements en une seule fois.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les fichiers générés par Konvergo ERP respectent les spécifications du prélèvement SEPA <b>PAIN.008.001.02</b>, conformément aux <a href="https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-credit-transfer-customer-psp-implementation">directives d’implémentation</a> du SEPA entre clients et banques, ce qui garantit la compatibilité avec les banques.</p>
</div>

Pour générer votre fichier `.xml` de plusieurs paiements SDD en attente, vous
pouvez créer un paiement par lot. Pour ce faire, allez à l’application
Comptabilité ‣ Clients ‣ Paiements, sélectionnez les paiements nécessaires,
puis cliquez sur **Action** , et finalement sur **Créer un paiement par lot**.
Une fois que vous avez cliqué sur **Valider** , le fichier `.xml` est
immédiatement disponible pour le téléchargement.

![Générez un fichier .XML pour vos paiements par prélèvement SEPA dans Konvergo ERP
Comptabiltié](../../../../_images/xml.png)

Enfin, chargez ce fichier dans l’interface de votre banque en ligne afin de
traiter les paiements.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez récupérer tous les fichiers SDD <code>.xml</code> générés en allant à l’application Comptabilité ‣ Clients ‣ Paiements par lot.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="batch">Paiements par lot par dépôt bancaire</a></p></li>
<li><p><a href="../bank">Comptes bancaires et d’espèces</a></p></li>
<li><p><a href="https://www.europeanpaymentscouncil.eu/document-library/other/epc-list-sepa-scheme-countries">Liste de tous les pays SEPA</a></p></li>
<li><p><a href="https://www.europeanpaymentscouncil.eu/document-library/implementation-guidelines/sepa-credit-transfer-inter-psp-implementation-guidelines">Directives SEPA</a></p></li>
</ul>
</div>

  *[SDD]: prélèvement SEPA

