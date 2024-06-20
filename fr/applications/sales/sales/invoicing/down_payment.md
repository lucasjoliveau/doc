# Acomptes

Un acompte est un paiement partiel effectué par l’acheteur lors de la
conclusion d’un contrat de vente. Il implique l’engagement total des deux
parties (vendeur et acheteur) à honorer le contrat.

Avec un acompte, l’acheteur paie une partie du montant total dû tout en
s’engageant à payer le reste à une date ultérieure. En échange, le vendeur
fournit les biens ou les services à l’acheteur après avoir accepté l’acompte,
en espérant que le reste sera payé ultérieurement.

## Créer les factures

Lorsqu’une commande client est confirmée, il est possible de créer une facture
en cliquant sur le bouton Créer une facture, situé dans le coin supérieur
gauche du formulaire de commande. Lorsque l’on clique sur le bouton, une
fenêtre contextuelle Créer les factures apparaît.

![Fenêtre contextuelle permettant de créer des factures dans Odoo
Ventes.](../../../../_images/create-invoices-popup-form.png)

Note

Les factures sont automatiquement créées en brouillon, pour qu’elles puissent
être révisées avant validation.

Dans la fenêtre contextuelle Créer les factures, vous avez le choix entre
trois options dans le champ Créer une facture :

  * Facture normale

  * Acompte (pourcentage)

  * Acompte (montant fixe)

Note

Si vous sélectionnez Facture normale, les autres champs disparaissent, car ils
ne sont nécessaires que dans une configuration d’acompte.

## Demande d’acompte initial

Sur la fenêtre contextuelle Créer factures, les options d’acompte sont les
suivantes :

  * Acompte (pourcentage)

  * Acompte (montant fixe)

Une fois que vous avez choisi l’option d’acompte dans le champ Créer une
facture dans la fenêtre contextuelle, indiquez le montant souhaité, sous forme
de pourcentage ou en tant que montant fixe, dans le champ Montant de
l’acompte.

Sélectionnez ensuite le compte des revenus approprié pour la facture dans le
champ Compte des revenus. Ensuite, sélectionnez un montant de taxe, le cas
échéant, dans le menu déroulant Taxes à la vente.

![Une fenêtre contextuelle permettant de créer des factures avec les champs
d'acompte complétés.](../../../../_images/create-invoices-popup-form-filled-
out.png)

Une fois que tous les champs sont remplis, cliquez sur le bouton Créer une
facture brouillon. En cliquant sur ce bouton, Odoo affiche la Facture client
en brouillon.

Dans l’onglet Lignes de facture de la Facture client brouillon, l’acompte qui
vient d’être configuré dans la fenêtre contextuelle Créer des factures
s’affiche comme un Produit.

![L'acompte comme un produit dans l'onglet Lignes de facture d'une facture
client brouillon dans Odoo.](../../../../_images/down-payment-product-inv-
draft.png)

Note

Lorsque vous cliquez sur le produit Acompte dans l’onglet Lignes de facture,
Odoo ouvre le formulaire du produit d’acompte.

Par défaut, le Type de produit des produits d’acompte générés pour les
factures est défini comme Service, avec la Politique de facturation définie
sur Prépayé/Prix fixe.

![Le formulaire du produit d'acompte avec le type de produit service et le
champ de la politique de facturation.](../../../../_images/down-payment-
product.png)

Ce produit peut être modifié à tout moment.

Avertissement

Si vous avez choisi Basé sur la quantité livrée (manuelle) en tant que
Politique de facturation, il ne sera **pas** possible de créer une facture.

## Exemple : demander un acompte de 50 %

Note

L’exemple suivant implique le paiement d’un acompte de 50 % sur un produit
(Armoire avec portes) avec la Politique de facturation définie sur Quantités
commandées.

![Formulaire de produit de l'armoire avec portes avec plusieurs détails et
champs en évidence.](../../../../_images/cabinet-product-details.png)

Pour plus d'infos

[Facturation basée sur les quantités livrées ou
commandées](invoicing_policy.html)

Allez d’abord à l’application Ventes ‣ Nouveau, et ajoutez un Client au devis.

Cliquez ensuite sur Ajouter un produit dans l’onglet Lignes de commande et
sélectionnez le produit Armoire avec portes.

Une fois la commande confirmée (en cliquant sur le bouton Confirmer), le devis
se transforme en commande. Ensuite, créez et visualisez la facture en cliquant
sur Créer une facture.

![La commande de l'armoire avec portes a été confirmée dans l'application Odoo
Ventes.](../../../../_images/cabinet-sales-orders-confirmed.png)

Ensuite, dans la fenêtre contextuelle Créer les factures qui s’ouvre,
sélectionnez l’option Acompte (pourcentage), et saisissez `50` dans le champ
Montant de l’acompte.

Note

Les champs Compte des revenus et Taxes à la vente ne sont _pas_ obligatoires
et ils n’apparaissent _pas_ s’ils ont été configurés auparavant dans les
demandes d’acompte précédentes.

Pour plus d’informations, consultez la documentation sur la modification des
taxes à la vente sur les acomptes et la modification du compte des revenus sur
les acomptes.

Enfin, cliquez sur Créer une facture brouillon pour créer et visualiser la
facture brouillon.

En cliquant sur Créer une facture brouillon, la facture brouillon s’ouvre et
inclut l’acompte en tant que Produit dans l’onglet Lignes de facture.

À partir de là, la facture peut être confirmée et comptabilisée en cliquant
sur Confirmer. La confirmation de la facture fait passer son statut de
Brouillon à Comptabilisé. Elle fait également apparaître une nouvelle série de
boutons en haut de la page.

![Un exemple de facture brouillon avec acompte mentionné dans Odoo
Ventes.](../../../../_images/draft-invoice-sample.png)

À partir de ces boutons, vous pouvez enregistrer le paiement en cliquant sur
Enregistrer un paiement.

![Présentation du bouton Enregistrer un paiement sur une facture client
confirmée.](../../../../_images/register-payment-button.png)

Une fenêtre contextuelle Enregistrer un paiement s’ouvre et est déjà rempli
avec les informations nécessaires. Validez les informations fournies ou faites
tous les changements nécessaires. Lorsque vous avez terminé, cliquez sur le
bouton Créer un paiement.

![Présentation de la fenêtre contextuelle Enregistrer un paiement avec le
bouton Créer un paiement.](../../../../_images/register-payment-pop-up-
window.png)

Après avoir cliqué sur Créer un paiement, Odoo affiche la facture client, avec
une bannière verte En paiement dans le coin supérieur droit.

![Facture client avec une bannière verte En paiement dans le coin supérieur
droit.](../../../../_images/customer-invoice-green-payment-banner.png)

Désormais, lorsque le client souhaite payer le montant restant de la commande,
vous devez créer une autre facture. Pour ce faire, retournez à la commande via
le fil d’Ariane.

De retour sur la commande, une nouvelle section Acomptes figure dans l’onglet
Lignes de commande, ainsi que l’acompte qui vient d’être facturé et
comptabilisé.

![La section acomptes dans l'onglet lignes de commande d'une
commande.](../../../../_images/down-payments-section-order-lines.png)

Ensuite, cliquez sur le bouton Créer une facture.

Dans la fenêtre contextuelle Créer les factures qui s’ouvre, vous trouverez
deux nouveaux champs : Déjà facturé et Montant à facturer.

![L'option de déduction des acomptes sur la fenêtre contextuelle de création
de factures dans Odoo Ventes.](../../../../_images/create-invoices-pop-up-
already-invoiced.png)

Si le montant résiduel est prêt à être payé, sélectionnez l’option Facture
normale. Odoo créera une facture pour le montant exacte requis pour compléter
le paiement total, comme il est indiqué dans le champ Montant à facturer.

Une fois que vous avez terminé, cliquez sur Créer une facture brouillon.

Cette opération fait ouvrir une autre page Facture client brouillon,
répertoriant _toutes_ les factures pour cette commande en particulier dans
l’onglet Lignes de facture. Chaque ligne de facture affiche toutes les
informations nécessaires relatives à chaque facture.

Pour compléter le flux, cliquez sur Confirmer, ce qui fait passer le statut de
la facture de Brouillon à Comptabilisé. Cliquez ensuite sur Enregistrer un
paiement.

À nouveau, la fenêtre contextuelle Enregistrer un paiement dont tous les
champs sont remplis automatiquement avec les informations nécessaires, y
compris le montant restant à payer de la commande.

![La deuxième fenêtre contextuelle permettant d'enregistrer un paiement dans
Odoo Ventes.](../../../../_images/second-register-payment-popup.png)

Après avoir validé ces informations, cliquez sur Créer un paiement. Cette
opération fait apparaître la Facture client finale avec une bannière verte En
paiement dans le coin supérieur droit. De plus, les deux acomptes figurent
dans l’onglet Lignes de facture.

![La deuxième facture d'acompte avec la bannière En paiement dans Odoo
Ventes.](../../../../_images/second-down-payment-in-payment-invoice.png)

Le flux est maintenant terminé.

Note

Ce flux est également possible avec l’option d’acompte Montant fixe.

Important

Si un acompte est utilisé avec un produit dont la politique de facturation est
définie sur Quantités livrées, les acomptes ne pourront **pas** être déduites
au moment de facturer le client.

En effet, en raison de la politique de facturation, le ou les produits doivent
être livrés _avant_ de pouvoir créer la facture finale.

Si rien n’a été livré, un Avoir est créé, annulant la facture brouillon créée
après l’acompte.

Pour utiliser l’option d”Avoir, l’application _Inventaire_ doit être
installée, afin de confirmer la livraison. Sinon, la quantité livrée peut être
saisie manuellement directement sur la commande.

## Modification des taxes à la vente sur les acomptes

Pour ajuster le compte des revenus et les taxes à la vente liés à un acompte,
allez à la page Produits (App Ventes ‣ Produits ‣ Produits), recherchez le
produit `Acompte` dans la barre de recherche et sélectionnez-le pour afficher
les détails du produit.

Sur la page du produit Acompte, dans l’onglet Informations générales, les
taxes à la vente peuvent être modifiées dans le champ Taxes à la vente.

![Comment modifier le lien entre le compte des revenus et les
acomptes.](../../../../_images/customer-taxes-field.png)

## Modification du compte des revenus sur les acomptes

Pour modifier ou ajuster le compte des revenus lié à la page du produit
Acompte, l’application _Comptabilité_ **doit** être installée.

Lorsque l’application _Comptabilité_ est installée, l’onglet Comptabilité
devient disponible sur la page du produit. Cet onglet ne sera **pas**
accessible si l’application _Comptabilité_ n’est pas installée.

Dans l’onglet Comptabilité, le compte des revenus peut être modifié dans le
champ Compte des revenus dans la section Créances.

![Comment modifier le lien entre le compte des revenus et les
acomptes.](../../../../_images/income-account.png)

Pour plus d'infos

[Facturation basée sur les quantités livrées ou
commandées](invoicing_policy.html)

