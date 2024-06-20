# Traiter des réceptions et des livraisons en une étape

Par défaut, les réceptions sont configurées pour être reçues directement dans
le stock et les expéditions sont configurées pour être livrées directement
depuis le stock au client ; le paramètre par défaut pour les entrepôts dans
Odoo est une réception et une livraison en une étape.

Note

Les réceptions et les expéditions ne doivent pas être nécessairement
configurées avec le même nombre d’étapes. Par exemple, les produits peuvent
être reçus en une étape, mais expédiés en trois.

Dans l’exemple suivant, les réceptions et les expéditions seront réalisées en
une étape.

## Configurer l’entrepôt

Si une autre configuration de réception ou d’expédition est définie pour
l’entrepôt, il est facile de revenir à la configuration en une étape.

Commencez par aller à Inventaire ‣ Configuration ‣ Entrepôts et cliquez sur
l’entrepôt souhaité pour le modifier. Ensuite, dans l’onglet Configuration de
l’entrepôt, dans la section Expéditions, sélectionnez Recevoir les
marchandises directement (1 étape) pour les Réceptions et/ou Livrer les
marchandises directement (1 étape) pour les Expéditions.

![Définissez les options de réception et d'expédition sur recevoir et livrer
en une étape.](../../../../../_images/one-step-warehouse-config.png)

## Recevoir les marchandises directement (1 étape)

### Créer un bon de commande

Sur le tableau de bord principal de l’application Achats, commencez par faire
un nouveau devis en cliquant sur Nouveau. Ensuite, sélectionnez (ou créez) un
Fournisseur dans le champ déroulant, ajoutez un Produit stockable aux lignes
de commande et cliquez sur Confirmer la commande pour finaliser le devis et le
transformer en bon de commande.

Un bouton intelligent Réception apparaîtra dans le coin supérieur droit du bon
de commande - le fait de cliquer dessus affiche le reçu associé au bon de
commande.

![Un bouton intelligent Réception apparaît sur le bon de commande
confirmé.](../../../../../_images/one-step-po-receipt.png)

Astuce

Vous pouvez également trouver les réceptions des bons de commande dans
l’application Inventaire, cliquez sur le bouton intelligent # à traiter sur la
carte kanban Réceptions.

![Carte kanban des réceptions avec le bouton intelligent 1 à
traiter.](../../../../../_images/one-step-to-process-btn.png)

### Traiter la réception

Lors de la visualisation de la réception (associée au bon de commande ci-
dessus), cliquez sur Valider pour ensuite finaliser la réception.

![Validez le bon de commande via le bouton intelligent
Valider.](../../../../../_images/one-step-po-validate.png)

Note

Si les Emplacements de stockage sont activés, le fait de cliquer sur l’icône
des détails ≣ (liste à puces) à côté de l’icône de suppression 🗑️ (corbeille)
fait apparaître la fenêtre contextuelle des Opérations détaillées. Ceci permet
de préciser le ou les emplacements pour le ou les produits reçus.

![Sélectionnez l'emplacement de stockage pour les produits en cours de
réception dans la fenêtre contextuelle des Opérations
détaillées.](../../../../../_images/receive-storage-location.png)

Une fois la réception validée, le produit quitte l”Emplacement fournisseur et
entre dans WH/Emplacement de stock. Dès qu’il arrive à cet emplacement, il
sera disponible pour la fabrication, la vente, etc. Ensuite, le statut du
document passe à Fait, finalisant donc le processus de réception en une étape.

## Livrer les marchandises directement (1 étape)

### Créer une commande client

Commencez par aller au tableau de bord principal de l’application Ventes et
faites un nouveau devis en cliquant sur Nouveau. Sélectionnez (ou créez)
ensuite un Client dans le champ déroulant, ajoutez un Produit stockable qui
est en stock aux lignes de commande et cliquez sur Confirmer pour transformer
le devis en commande client.

Un bouton intelligent Réception apparaîtra dans le coin supérieur droit du bon
de commande - le fait de cliquer dessus affiche le reçu associé au bon de
commande.

Un bouton intelligent Livraison apparaîtra dans le coin supérieur droit de la
commande client - le fait de cliquer dessus affiche le bon de livraison
associé à la commande client.

![Le bouton intelligent Livraison apparaît après la confirmation de la
commande.](../../../../../_images/one-step-sales-order.png)

Astuce

Vous pouvez également trouver les bons de commande dans l’application
Inventaire. Sur le tableau de bord Aperçu, cliquez sur le bouton intelligent #
à traiter sur la carte kanban Bons de livraison.

![Carte kanban des bons de livraison avec le bouton intelligent 1 à
traiter.](../../../../../_images/one-step-delivery-to-process.png)

### Traiter la livraison

Lors de la visualisation du bon de livraison (associé à la commande ci-
dessus), cliquez sur Valider pour ensuite finaliser la livraison.

![Validez le bon de livraison.](../../../../../_images/validate-one-step-
sales-order.png)

Une fois le transfert validé, le produit quitte WH/Emplacement de stock et se
déplace vers Partenaires/Emplacement client. Ensuite, le statut du document
passe à Fait, finalisant donc la livraison en une étape.

