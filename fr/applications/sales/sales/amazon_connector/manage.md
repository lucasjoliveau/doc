# Gestion des commandes Amazon

## Synchronisation des commandes

Les commandes sont automatiquement récupérées d’Amazon et synchronisées dans
Konvergo ERP à des intervalles réguliers.

La synchronisation est basée sur le statut Amazon : seules les commandes dont
le statut a changé depuis la dernière synchronisation sont récupérées
d’Amazon. Cela inclut les changements d’un côté ou de l’autre (Amazon ou
Konvergo ERP).

Pour _FBA_ (Fulfilled by Amazon), seules les commandes _expédiées_ et
_annulées_ sont récupérées.

Pour _FBM_ (Fulfilled by Merchant), la même chose est faite pour les commandes
_non expédiées_ et _annulées_. Pour chaque commande synchronisée, une commande
client et un client sont créés dans Konvergo ERP (si le client n’est pas déjà
enregistré dans la base de données).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsqu’une commande est annulée dans Amazon et qu’elle a déjà été synchronisée dans Konvergo ERP, la commande correspondante est automatiquement annulée dans Konvergo ERP.</p>
</div>

## Forcer la synchronisation

Afi de forcer la synchronisation d’une commande, dont le statut n’a **pas**
changé depuis la dernière synchronisation, commencez par activer le [mode
développeur](../../../general/developer_mode#developer-mode). ela inclut
des changements d’un côté ou de l’autre (Amazon ou Konvergo ERP).

Allez ensuite au compte Amazon dans Konvergo ERP (application Ventes ‣ Configuration ‣
Paramètres ‣ Connecteurs ‣ Synchronisation Amazon ‣ Comptes Amazon), et
modifiez la date sous Suivi des commandes ‣ Synchronisation de la dernière
commande.

Assurez-vous de choisir une date antérieure au dernier changement de statut de
la commande à synchroniser et à enregistrer. Cela permettra d’assurer une
synchronisation correcte.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour synchroniser immédiatement les commandes d’un compte Amazon, passez en <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez sur le compte Amazon dans Konvergo ERP, et cliquez sur <b>Synchroniser les commandes</b>. Vous pouvez en faire de même avec les transferts en cliquant sur <b>Synchroniser les transferts</b>.</p>
</div>

## Gérer les livraisons en FBM

Lorsqu’une commande FBM (Fulfilled by Merchant) est synchronisée dans Konvergo ERP, un
transfert est créé immédiatement dans l’application _Inventaire_ , en même
temps qu’une commande et un client. Vous pouvez ensuite décider d’expédier
tous les produits commandés au client en une fois ou d’expédier une partie des
produits en utilisant des reliquats.

Lorsqu’un transfert lié à la commande est confirmé, une notification est
envoyée à Amazon qui, à son tour, informe le client que la commande (ou une
partie de celle-ci) est en route.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Amazon demande aux utilisateurs de fournir une référence de suivi avec chaque livraison. Cette référence est nécessaire pour attribuer un transporteur.</p>
<p>Si le transporteur ne fournit pas automatiquement une référence de suivi, celle-ci doit être définie manuellement. Cette règle s’applique à toutes les marketplaces d’Amazon.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le transporteur choisi n’est pas pris en charge par Konvergo ERP, un transporteur portant le même nom peut être créé (par ex. créer un transporteur intitulé <code>easyship</code>). Le nom utilisé n’est <b>pas</b> sensible à la casse, mais veillez à éviter les fautes de frappe. S’il y a des fautes de frappe, Amazon ne les reconnaîtra <b>pas</b>. Ensuite, créez un transporteur intitulé <code>Self Delivery</code> pour informer Amazon que l’utilisateur fera les livraisons. Même avec cette route, vous <b>devez</b> toujours fournir une référence de suivi. N’oubliez pas que le client est informé par email de la livraison et que le transporteur, ainsi que la référence de suivi, sont affichés dans l’email envoyé au client.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../inventory_and_mrp/inventory/shipping_receiving/setup_configuration/third_party_shipper">Third-party shipping carriers</a></p>
</div>

## Suivre des livraisons en FBA

Lorsqu’une commande FBA (Fulfilled by Amazon) est synchronisée dans Konvergo ERP, un
mouvement de stock est enregistré dans l’application _Inventaire_ pour chaque
article de commande. De cette façon, il est enregistré dans le système.

Les gestionnaires d’inventaire peuvent accéder à ces mouvements de stock en
allant à l’application Inventaire ‣ Analyse ‣ Historique des mouvements.

Pour les commandes FBA, le mouvement de stock est créé automatiquement dans
Konvergo ERP par le connecteur Amazon, grâce au statut d’expédition d’Amazon. Lors de
l’envoi de nouveaux produits à Amazon, l’utilisateur doit créer un transfert
(bon de livraison) manuellement pour transférer ces produits de leur entrepôt
à l’emplacement Amazon.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour suivre le stock <em>Amazon (FBA)</em> dans Konvergo ERP, effectuez un ajustement d’inventaire après le réassort. Vous pouvez également déclencher un réassort automatisé à partir de règles de réapprovisionnement sur l’emplacement Amazon.</p>
</div>

L’emplacement Amazon peut être configuré en allant au compte Amazon géré dans
Konvergo ERP. Pour accéder aux comptes Amazon dans Konvergo ERP, allez à l’application Ventes
‣ Configuration ‣ Paramètres ‣ Connecteurs ‣ Synchronisation Amazon ‣ Comptes
Amazon.

Tous les comptes de la même société utilisent le même emplacement Amazon par
défaut. Cependant, il est possible de suivre le stock filtré par marketplace.

Pour ce faire, supprimez d’abord la marketplace, où se trouve le stock à
suivre séparément de la liste des marketplaces synchronisées, qui peut être
trouvée en allant à l’application Ventes ‣ Configuration ‣ Paramètres ‣
Connecteurs ‣ Synchronisation Amazon ‣ Comptes Amazon.

Ensuite, créez un autre enregistrement pour ce compte et supprimez toutes les
marketplaces— **à l’exception** de la marketplace que l’on souhaite isoler des
autres.

Enfin, assignez un autre emplacement de stock au deuxième enregistrement du
compte.

## Facturer et enregistrer des paiements

### Émettre des factures

En raison de la politique d’Amazon de ne pas partager les adresses email des
clients, il n’est **pas** possible d’envoyer des factures directement aux
clients Amazon à partir d’Konvergo ERP. Cependant, il **est** possible de télécharger
manuellement les factures générées à partir d’Konvergo ERP vers le backend d’Amazon.

De plus, pour les clients B2B, il est actuellement requis de récupérer
manuellement les numéros de TVA à partir du backend d’Amazon **avant** de
créer une facture dans Konvergo ERP.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour les utilisateurs de <a href="../../../finance/accounting/taxes/taxcloud">TaxCloud</a> : les factures créées à partir des commandes Amazon ne sont <b>pas</b> synchronisées avec TaxCloud, puisqu’Amazon les inclut déjà sans sa propre déclaration de TVA à TaxCloud.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>L’intégration TaxCloud sera désactivée dans Konvergo ERP 17+.</p>
</div>

### Enregistrer les paiements

Comme les clients paient Amazon en tant qu’intermédiaire, il est recommandé de
créer un journal de _Banque_ dédié (par ex. intitulé `Paiements Amazon`), avec
un compte intermédiaire _Banque et Espèces_ dédié.

De plus, comme Amazon effectue un seul paiement mensuel, il est nécessaire de
sélectionner toutes les factures liées à un seul paiement lors de
l’enregistrement des paiements.

Pour ce faire, utilisez le **Journal** approprié dédié aux paiements Amazon et
sélectionnez **Dépôt par lots** comme **Mode de paiement**.

Sélectionnez ensuite tous les paiements générés et cliquez sur Actions ‣ Créer
un paiement par lot ‣ Valider.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez effectuer la même action avec les factures fournisseurs d’Amazon dédiées aux commissions.</p>
<p>Lorsque le solde est reçu sur le compte bancaire à la fin du mois et les relevés bancaires sont enregistrés, créditez le compte intermédiaire Amazon du montant reçu.</p>
</div>

## Suivre les ventes Amazon dans l’analyse des ventes

Sur le profil du compte Amazon dans Konvergo ERP, une équipe commerciale est définie
sous l’onglet **Suivi des commandes**.

Cela permet d’accéder rapidement aux métriques importantes liées aux analyses
des ventes. Par défaut, l’équipe commerciale du compte Amazon est partagée
entre tous les comptes de la société.

Si vous le souhaitez, vous pouvez changer l’équipe commerciale sur le compte,
afin d’effectuer une analyse séparée des ventes de ce compte.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est également possible d’effectuer des analyses par marketplace.</p>
<p>Supprimez d’abord la marketplace souhaitée de la liste des marketplaces synchronisées.</p>
<p>Pour accéder à la liste des marketplaces synchronisées dans Konvergo ERP, allez à l’application Ventes ‣ Configuration ‣ Paramètres ‣ Connecteurs ‣ Synchronisation Amazon ‣ Comptes Amazon.</p>
<p>Créez ensuite un autre enregistrement pour ce compte et supprimez toutes les marketplaces <b>à l’exception</b> de celle à isoler.</p>
<p>Enfin, assignez une autre équipe commerciale à l’un des deux enregistrements du compte.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour synchroniser immédiatement les commandes d’un compte Amazon, passez en <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a>, allez sur le compte Amazon dans Konvergo ERP, et cliquez sur <b>Synchroniser les commandes</b>. Vous pouvez en faire de même avec les transferts en cliquant sur <b>Synchroniser les transferts</b>.</p>
</div>0

