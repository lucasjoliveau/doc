# Processus de facturation

En fonction de vos activités et des applications que vous utilisez, il existe
différentes façons d’automatiser la création des factures clients dans Konvergo ERP.
En général, les factures brouillon sont créées par le système (en prenant des
informations d’autres documents tels que les commandes clients ou les
contrats) et le comptable n’a plus qu’à valider les factures brouillon et
envoyer les factures par lot (par la poste ou par email).

Selon vos activités, vous pouvez choisir l’une des méthodes suivantes pour
créer des factures brouillon :

## Ventes

### Commande client ‣ Facture

Dans la plupart des entreprises, les vendeurs créent des devis qui deviennent
des commandes clients une fois qu’ils sont validés. Ensuite, des factures
brouillon sont créées sur la base des commandes. Vous avez différentes options
telles que :

  * Facturation manuelle : utilisez un bouton sur la commande client pour générer la facture brouillon

  * Facturation avant livraison : facturez la commande complète avant la génération du bon de livraison

  * Facturation basée sur le bon de livraison : voir la section suivante

La facturation avant la livraison est habituellement utilisée par
l’application d’eCommerce lorsque le client paie à la commande et que
l’expédition se fait ultérieurement. (pré-paiement)

Pour la plupart des autres cas d’utilisation, il est recommandé de facturer
manuellement. Cela permet au vendeur de générer la facture à la demande avec
les options suivantes : facturer l’intégralité de la commande, facturer un
pourcentage (acompte), facturer certaines lignes, facturer un acompte fixe.

Ce processus convient aussi bien aux services qu’aux produits physiques.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../sales/sales/invoicing/proforma">Factures pro forma</a></p></li>
</ul>
</div>

### Commande client ‣ Bon de livraison ‣ Facture

Les détaillants et les sites d’eCommerce facturent généralement sur la base
des bons de livraison, au lieu des commandes. Cette approche convient aux
entreprises pour lesquelles les quantités livrées peuvent différer des
quantités commandées : denrées alimentaires (facture sur la base des kg
réels).

De cette manière, si vous livrez une commande partiel, vous ne facturez que ce
que vous avez réellement livré. Si vous effectuez des reliquats (livraison
partielle et le reste plus tard), le client recevra deux factures, une pour
chaque bon de livraison.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../sales/sales/invoicing/invoicing_policy">Facturation basée sur les quantités livrées ou commandées</a></p></li>
</ul>
</div>

### Commande eCommerce ‣ Facture

Une commande d’eCommerce générera également la création de la commande
lorsqu’elle est intégralement payée. Si vous autorisez le paiement des
commandes par chèque ou par virement bancaire, Konvergo ERP crée uniquement une
commande et la facture sera générée après la réception du paiement.

## Contrats

### Contrats réguliers ‣ Factures

Si vous utilisez des contrats, vous pouvez générer les factures sur la base du
temps et du matériel utilisé, des dépenses ou des lignes fixes de
services/produits. Chaque mois, le vendeur générera une facture sur la base
des activités prévues dans le contrat.

Les activités peuvent être :

  * des produits/services fixes, provenant d’une commande liée à ce contrat

  * des matériels achetés (que vous refacturez)

  * du temps et du matériel basés sur des feuilles de temps ou sur des achats (sous-traitance)

  * des dépenses comme les frais de déplacement que vous refacturez au client

Vous pouvez facturer à la fin du contrat ou générer des factures
intermédiaires. Cette approche convient aux sociétés de services qui facturent
la plupart du temps sur la base du temps et du matériel. Quant aux entreprises
de services qui facturent un prix fixe, elles utilisent plutôt une commande
régulière.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../sales/sales/invoicing/time_materials">Facturation basée sur le temps et les matériaux</a></p></li>
<li><p><a href="../../../sales/sales/invoicing/expense">Refacturer des notes de frais aux clients</a></p></li>
<li><p><a href="../../../sales/sales/invoicing/milestone">Facturer les jalons d’un projet</a></p></li>
</ul>
</div>

### Contrats récurrents ‣ Factures

Pour les abonnements, une facture est émise périodiquement et automatiquement.
La fréquence de la facturation et les services/produits facturés sont définis
dans le contrat.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../sales/subscriptions">Abonnements</a></p></li>
</ul>
</div>

## Autres

### Créer une facture manuellement

Les utilisateurs peuvent également créer des factures manuellement sans
utiliser des contrats ou des commandes clients. Cette approche est recommandée
si vous n’avez pas besoin de gérer le processus de vente (devis) ou la
livraison des produits ou services.

Même si vous générez la facture à partir d’une commande client, vous pouvez
être amené à créer des factures manuellement dans des cas d’utilisation
exceptionnels :

  * si vous devez créer un remboursement

  * Si vous devez accorder une remise

  * si vous voulez modifier une facture créée à partir d’une commande client

  * si vous voulez facturer quelque chose qui n’est pas lié à votre activité principale

### Modules spécifiques

Quelques modules spécifiques peuvent également générer des factures brouillon
:

  * **Adhésion** : facturez vos membres sur base annuelle

  * **réparations** : facturez vos services d’après-vente

### Réordonnancement des factures

Il est toujours possible de réordonner les factures, mais en respectant
quelques limites :

  1. La fonctionnalité ne fonctionne pas lorsque les écritures sont antérieures à une date de verrouillage.

  2. La fonctionnalité ne fonctionne pas si la séquence n’est pas cohérente avec le mois de l’écriture.

  3. Elle ne fonctionne pas si la séquence génère un doublon.

  4. L’ordre de la facture reste inchangé.

  5. C’est utile pour les personnes qui utilisent la numérotation d’un autre logiciel et qui veulent continuer l’année en cours sans la reprendre depuis le début.

### Numérisation des factures grâce à la reconnaissance optique de caractères
(OCR)

La **numérisation des factures** consiste à encoder automatiquement des
factures papier traditionnelles dans les formulaires de factures de votre
comptabilité.

Konvergo ERP utilise les technologies OCR et d’intelligence artificielle pour
reconnaître le contenu des documents. Les factures fournisseurs et les
factures clients sont créées automatiquement et remplies sur la base des
factures numérisées.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../vendor_bills/invoice_digitization">Numérisation de documents assistée par IA</a></p></li>
</ul>
</div>

