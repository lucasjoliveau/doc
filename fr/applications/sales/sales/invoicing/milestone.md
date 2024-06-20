# Facturer les jalons d’un projet

La facturation basée sur les jalons d’un projet peut être utilisée pour les
projets coûteux ou de grande envergure. La série de jalons d’un projet
représente une séquence claire de travail qui aboutira inévitablement à
l’achèvement d’un projet et/ou d’un contrat.

Cette méthode de facturation garantit à l’entreprise un flux d’argent constant
tout au long du projet. Les clients peuvent suivre de près chaque phrase du
développement du projet au fur et à mesure qu’il se déroule, en plus de payer
une facture importante en plusieurs fois, plutôt qu’en une seule fois.

## Créer des produits de jalon

Dans Odoo, chaque jalon d’un projet est considéré comme un produit individuel.

Pour créer et/ou configurer les produits, allez d’abord à l’application Ventes
‣ Produits ‣ Produits. Puis cliquez sur un produit ou créez-en un nouveau en
cliquant sur Nouveau.

L’option de facturer sur la base des jalons n’est disponible que pour certains
types de produits.

Sur le formulaire du produit, dans l’onglet Informations générales le champ
Type de produit _doit_ être défini sur l’une des options suivantes : Service,
Ticket d’événement, Stand d’événement, ou Cours.

![Le menu déroulant du champ Politique de facturation et ses options sur le
formulaire du produit.](../../../../_images/product-type-field.png)

Si l’un de ces Types de produit est sélectionné, choisissez Basé sur les
jalons dans le menu déroulant Politique de facturation.

![Le menu déroulant du champ Politique de facturation et ses options sur le
formulaire du produit.](../../../../_images/invoicing-policy-field.png)

En dessous se trouve le champ Créer à la commande.

Pour assurer que les flux de travail soient aussi transparents que possible,
il est recommandé de sélectionner une option dans le champ Créer à la
commande.

Note

Le fait de laisser l’option Rien par défaut n’aura pas d’incidence négative
sur le flux de travail souhaité. Cependant, un projet _doit_ être créé
directement à partir d’une commande avec ce produit spécifique. Une fois qu’un
produit est créé, les jalons et les tâches peuvent être créés et configurés
_par la suite_.

Lorsque vous cliquez sur l’option par défaut Rien dans le champ Créer à la
commande Order, un menu déroulant s’affiche et propose les options suivantes :

  * Tâche : Odoo crée une tâche associée à ce produit de jalon dans l’application _Projets_ lorsque ce produit spécifique est commandé.

  * Projet & Tâche : Odoo crée un projet et une tâche associés à ce projet de jalon dans l’application _Projets_ lorsque ce produit spécifique est commandé.

  * Projet : Odoo crée un projet associé à ce produit de jalon dans l’application _Projets_ lorsque ce produit spécifique est commandé.

Lorsque vous sélectionnez Tâche, un champ Projet apparaît. Dans ce champ,
sélectionnez à quel projet existant dans l’application _Projets_ cette tâche
créée doit être liée.

![Le champ Projet apparaît lorsque l'option Tâche est choisie dans le champ
Créer à la commande.](../../../../_images/task-option-project-field.png)

Lorsque vous sélectionnez Projet & Tâche ou Projet, deux nouveaux champs
apparaissent : Modèle de projet et Modèle d’espace de travail.

![Les champs Modèle de projet et Modèle d'espace de travail qui apparaissent
sur le projet de jalon.](../../../../_images/project-task-option-project-
workspace-fields.png)

Le champ Modèle de projet fournit des options de modèle à utiliser pour le
projet qui sera créé lorsque ce produit spécifique est commandé.

Le champ Modèle d’espace de travail fournit des options de modèle à utiliser
pour l’espace de travail (pour l’application _Documents_ et non l’application
_Projets_) qui sera automatiquement généré pour le projet lorsque ce produit
spécifique est commandé.

Astuce

Pour des raisons d’organisation, cliquez sur l’onglet Ventes sur le formulaire
du produit et saisissez une description du “Jalon” dans le champ Description
vente. Ces informations apparaissent dans la colonne Description de l’onglet
Lignes de commande de la commande.

Ou, modifiez directement le champ Description de l’onglet Lignes de commande
de la commande.

Ceci n’est _pas_ obligatoire.

## Facturer des jalons

Note

Le flux suivant présente un trio de produits de jalon qui dont le Type de
produit est Service et le champ Créer à la commande est défini sur Tâche.

> ![Produit avec le "Type de produit" Service et le champ Créer à la commande
> défini sur "Tâche".](../../../../_images/settings-for-workflow.png)

Ces tâches sont alors associées à un Projet préexistant, qui, dans ce cas,
s’intitule Projets de rebranding.

Pour facturer les jalons, créez une commande avec le ou les produits de jalon.
Pour ce faire, allez à l’application Ventes ‣ Nouveau. Cette opération fait
apparaître un formulaire de devis vierge.

Dans ce formulaire de devis, ajoutez un Client. Puis cliquez sur Ajouter un
produit dans l’onglet Lignes de commande. Ajoutez ensuite le ou les produits
de jalon dans l’onglet Lignes de commande.

Une fois que le ou les produits de jalon correspondants ont été ajoutés,
cliquez sur Confirmer pour confirmer la commande, ce qui transforme le devis
en commande.

Lorsque la commande est confirmée, de nouveaux boutons intelligents
apparaissent en haut de la commande en fonction de ce qui a été sélectionné
dans le champ Créer à la commande sur le formulaire du produit.

À partir de la commande, cliquez sur le bouton intelligent Jalons. Cette
opération fait apparaître une page Jalons vierge. Cliquez sur Nouveau pour
ajouter des jalons.

![Ajout de jalons à une commande avec des produits de
jalon.](../../../../_images/adding-milestones.png)

Donnez un Nom au jalon. Ensuite, appliquez-le à l”Article de commande
correspondant. Enfin, attribuez une Date limite au jalon, si vous le
souhaitez.

Répétez ce processus pour tous les articles de commande.

Retournez ensuite à la commande via le fil d’Ariane. À partir de la commande,
cliquez sur le bouton intelligent, Tâches. Cette opération fait apparaître une
page Tâches avec une tache pour chaque article de commande dont l’option est
désignée dans le champ Créer à la commande.

![Exemple de page de tâches accessible via le bouton intelligent à partir
d'une commande avec des produits de jalon.](../../../../_images/tasks-
page.png)

Pour assigner manuellement un jalon configuré à une tâche, cliquez sur la
tâche souhaitée, ce qui fait apparaître son formulaire. Sur le formulaire,
sélectionnez le jalon approprié auquel cette tâche doit être associée, dans le
champ Jalon.

![Le champ Jalon sur le formulaire lorsqu'il s'agit de produits de jalon dans
Odoo Ventes.](../../../../_images/milestone-field-on-task-form.png)

Répétez ce processus pour toutes les tâches de jalon.

Une fois ces tâches correctement configurées, les employés enregistrent leur
progression au fur et à mesure qu’ils travaillent sur la tâche, en plus
d’ajouter toutes les notes liées à la tâche.

Ensuite, lorsque cette tâche est terminée, cela signifie que le jalon a été
atteint. Il est alors temps de facturer ce jalon.

Pour facturer un jalon, retournez d’abord à la commande — soit via le fil
d’Ariane, soit en allant à l’application Ventes ‣ Commandes ‣ Commandes et
choisissez la commande appropriée.

De retour sur le formulaire de commande, cliquez sur le bouton intelligent
Jalons et cochez la case dans la colonne Atteint pour cette tâche en
particulier.

![A quoi ressemble le marquage d'un jalon comme atteint via le bouton
intelligent jalons.](../../../../_images/reached-milestone.png)

Ensuite, retournez à la commande — soit en cliquant sur Afficher le bon de
commande sur la page des Jalons, soit via le fil d’Ariane.

De retour sur la commande, la colonne Livré est rempli pour la ligne
correspondant au jalon. C’est parce que le jalon a été atteint, et donc livré.

![Un produit de jalon qui a été atteint, marqué comme livré sur la commande
dans Odoo.](../../../../_images/delivered-milestone-product-sales-order.png)

Cliquez sur Créer une facture dans le coin supérieur gauche, ce qui fait
apparaître une fenêtre contextuelle Créer les factures.

![La fenêtre contextuelle permettant de créer des factures qui s'affiche
lorsque vous cliquez sur le bouton Créer une
facture.](../../../../_images/create-invoices-pop-up.png)

Dans la fenêtre contextuelle Créer les factures, laissez l’option Créer une
facture sur la sélection Facture normale par défaut et cliquez sur le bouton
Créer une facture brouillon.

Lorsque vous cliquez sur Créer une facture brouillon, Odoo ouvre la Facture
client brouillon, ne montrant _que_ ce jalon atteint dans l’onglet Lignes de
facture.

![Une facture client brouillon qui ne montre que le produit de jalon qui a été
atteint.](../../../../_images/invoice-draft-milestone.png)

Sur cette page de facture, cliquez sur le bouton Confirmer pour confirmer la
facture. Ensuite, lorsque le client a payé ce jalon, cliquez sur Enregistrer
un paiement.

Une fois que vous avez cliqué sur Enregistrer un paiement, une fenêtre
contextuelle Enregistrer un paiement s’affiche.

![La fenêtre contextuelle permettant d'enregistrer un paiement qui s'affiche
lorsque vous cliquez sur Enregistrer un
paiement.](../../../../_images/register-payment-pop-up.png)

Dans cette fenêtre contextuelle, vérifiez les champs qui se sont remplis
automatiquement, puis cliquez sur Créer un paiement.

Lorsque vous cliquez dessus, la fenêtre contextuelle disparaît et Odoo revient
à la facture de ce jalon, pour laquelle s’affiche désormais une bannière verte
En paiement dans le coin supérieur droit. Cette bannière signifie que la
facture a été payée.

![Une facture avec un produit de jalon qui a été payé avec une bannière En
paiement.](../../../../_images/in-payment-invoice.png)

Retournez ensuite à la commande via le fil d’Ariane. De retour sur la
commande, dans l’onglet Lignes de commande, le jalon atteint qui a été facturé
et payé, a désormais sa colonne Facturé remplie.

![La colonne Facturé d'un produit de jalon qui a été payé est
remplie.](../../../../_images/invoiced-column-filled-milestone.png)

Il y a également un nouveau bouton intelligent Factures en haut de la
commande. En cliquant sur ce bouton, toutes les factures associées à cette
commande s’affichent.

![Le bouton intelligent Factures qui s'affiche en haut de la commande avec des
jalons.](../../../../_images/invoices-smart-button.png)

Il suffit de répéter le processus susmentionné pour chaque jalon au fur et à
mesure qu’il est travaillé, puis achevé.

Poursuivez ce processus jusqu’à ce que l’ensemble du projet soit achevé, que
chaque étape ait été facturée et que la commande ait été entièrement payée.

Pour plus d'infos

  * [Facturation basée sur le temps et les matériaux](time_materials.html)

  * [Factures pro forma](proforma.html)

  * [Facturation basée sur les quantités livrées ou commandées](invoicing_policy.html)

