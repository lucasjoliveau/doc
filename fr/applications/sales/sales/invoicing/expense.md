# Refacturer des notes de frais aux clients

Lorsqu’ils travaillent sur un projet pour un client, les employés doivent
souvent dépenser leurs propre argent pour diverses dépenses liées au projet.

Par exemple, un employé peut avoir besoin de payer un hôtel, alors qu’il
fournit un service sur site pour son client. En tant qu’entreprise, cette
dépense doit être refacturée au client. Avec Konvergo ERP, ce type de dépenses peut
rapidement être refacturé au client dans le cadre du projet.

## Application Notes de frais

Pour pouvoir refacturer une dépense à un client, vous **devez** installer
l’application _Notes de frais_.

Pour installer l’application _Notes de frais_ , allez au tableau de bord
principal d’Konvergo ERP ‣ Apps, et cliquez sur **Installer** sur le bloc de
l’application _Notes de frais_. Lorsque vous cliquez dessus, Konvergo ERP installe
l’application, actualise la page et revient au tableau de bord principal.

## Ajouter des dépenses aux commandes

Pour commencer, confirmez une commande dans l’application _Ventes_ , à
laquelle vous pouvez ajouter une dépense refacturée. Vous pouvez également
créer une nouvelle commande à partir de zéro. Pour ce faire, allez à
l’application Ventes ‣ Nouveau. Cette opération fait apparaître un formulaire
de devis vierge.

Ajoutez ensuite un **Client** , et ajoutez un produit à l’onglet **Lignes de
commande** en cliquant sur **Ajouter un produit**. Sélectionnez ensuite un
produit dans le menu déroulant.

Cliquez sur **Confirmer** pour confirmer la commande.

![Voici à quoi ressemble une commande confirmée dans l'application Konvergo ERP
Ventes.](../../../../_images/confirmed-sales-order.png)

Une fois la commande confirmée, il est temps de créer une note de frais.

Pour ce faire, allez à l’application _Notes de frais_ via le tableau de bord
principal d’Konvergo ERP ‣ Notes de frais.

Ensuite, dans le tableau de bord des _Notes de frais_ , cliquez sur
**Nouveau** pour ouvrir une note de frais vierge.

![Une note de frais vierge dans l'application Konvergo ERP Notes de
frais.](../../../../_images/blank-expenses-form.png)

Sur la note de frais, ajoutez une **Description** pour facilement référencer
la dépense.

Ensuite, dans le champ **Catégorie** , sélectionnez l’une des options
suivantes dans le menu déroulant :

  * **Communication** : toute forme de communication liée à un projet/une commande.

  * **Autres** : une dépense qui ne rentre dans aucune autre catégorie.

  * **repas** : toute forme de frais de repas liés à un projet/une commande.

  * **Cadeaux** : toute forme de frais de cadeaux liés à un projet/une commande.

  * **Kilométrage** : toute for de frais de carburant liés à un projet/une commande.

  * **Voyage & Hébergement** : toute forme de frais de voyage ou d’hébergement liés à un projet/une commande.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez créer de nouvelles catégories de dépenses à partir d’une note de frais en cliquant sur le menu déroulant du champ <b>Catégorie</b>, en sélectionnant <b>Voir tout</b>, et en cliquant sur <b>Nouveau</b> dans la fenêtre contextuelle <b>Recherche : Catégorie</b>.</p>
<img alt="La fenêtre contextuelle Recherche : Catégorie à partir d'une note de frais vierge dans Konvergo ERP Notes de frais." class="align-center" src="../../../../_images/expense-category-pop-up.png"/>
</div>

Pour cet exemple de flux, qui refacture un client pour un bref séjour à
l’hôtel, la **Catégorie** est **[TRANS & ACC] Voyage & Hébergement**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’exemple suivant nécessite que les applications <em>Ventes</em>, <em>Comptabilité</em> et <em>Notes de frais</em> soient installées pour pouvoir voir/modifier tous les champs mentionnés dans le flux.</p>
</div>

Sous le champ **Catégorie** , saisissez le montant que vous voulez refacturer
dans le champ **Total**.

Ensuite, précisez s’il y a des **Taxes comprises** dans le montant **Total**.
Si un montant de taxe préconfiguré est sélectionné dans le champ **Taxes
comprises** , Konvergo ERP calcule automatiquement le montant taxé, en fonction du
montant saisi dans le champ **Total**.

Choisissez ensuite l”**Employé** qui était responsable de la dépense et
choisissez une option dans le champ **Payé par** : **Employé (à rembourser)**
ou **Société**.

Dans ce cas, notre employé a payé l’hôtel de son propre argent, donc il faut
choisir l’option **Employé (à rembourser)**.

Sur la partie droite de la note de frais, il est possible d’ajouter une
**Référence de facture**. En dessous, les champs **Date de la dépense** et
**Compte** se remplissent automatiquement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez modifier les champs <b>Date de la dépense</b> et <b>Compte</b>, si vous le voulez.</p>
</div>

Ensuite, dans le champ **Client à refacturer** , cliquez sur le champ vierge
pour faire apparaître un menu déroulant. Dans ce menu déroulant, sélectionnez
la commande appropriée à laquelle cette dépense doit être ajoutée. Ce champ
**doit** être complété, pour pouvoir refacturer cette dépense à un client.

Enfin, il est possible de modifier les champs **Distribution analytique** et
**Société**. Ces champs ne sont _pas_ obligatoires pour compléter une dépense
refacturée à un client, mais peuvent être modifiés si nécessaire.

En outre, au bas de la note de frais, il y a une section **Notes…** , dans
laquelle toute note relative à cette note de frais peut être ajoutée, si
nécessaire.

![Une note de frais complétée dans l'application Konvergo ERP Notes de
frais.](../../../../_images/filled-in-expense-form.png)

En haut de la note de frais, il y a des boutons pour **Joindre le reçu** ,
**Créer le rapport** , et **Fractionner la note de frais**.

Si vous devez joindre un reçu physique ou numérique à la dépense, cliquez sur
**Joindre le reçu**.

Si le coût de cette dépense doit être fractionné, cliquez sur **Fractionner la
note de frais**. Cette option peut être utilisée pour plusieurs raisons
(diviser la note avec un autre employé, prendre en compte des taux
d’imposition différents, etc.).

Si aucune de ces options n’est nécessaire, cliquez sur **Créer le rapport**
pour confirmer la note de frais qui vient d’être configurée.

Cette opération fait apparaître un **Résumé de la note de frais** pour la
nouvelle dépense.

![Un résumé de la note de frais dans l'application Konvergo ERP Notes de
frais.](../../../../_images/expense-report-summary-form.png)

Après avoir validé les détails de la note de frais, cliquez sur **Soumettre au
manager**. La note de frais sera envoyée au manager, qui examinera la dépense.

Le manager en charge d’examiner et d’approuver la note de frais vérifiera les
détails de la dépense et si tout est en ordre, il cliquera sur le bouton
**Approuver** — qui apparaît _uniquement_ dans la vue du manager du **Résumé
de la note de frais** que l’employé a soumis au manager.

![Un résumé de la note de frais qu'un manager doit approuver avec le bouton
Approuver.](../../../../_images/expense-report-summary-manager-approve.png)

Une fois la note de frais approuvée, les boutons en haut du **Résumé de la
note de frais** changent à nouveau. À ce stade, les boutons en haut du
**Résumé de la note de frais** sont les suivants : **Enregistrer les pièces
comptables** , **Rapporter dans la prochaine fiche de paie** , **Refuser** ,
et **Remettre en brouillon**.

![Un résumé de note de frais avec le bouton Enregistrer les pièces comptables
en haut du formulaire.](../../../../_images/expense-report-summary-manager-
post-journal.png)

Lorsque le manager est d’accord avec le **Résumé de la note de frais** , il
doit cliquer sur **Enregistrer des pièces comptables**.

En cliquant sur **Enregistrer des pièces comptables** , ce bouton disparaît et
la colonne **Distribution analytique** de l’onglet **Note de frais** se
remplit avec la commande initialement configurée pour la dépense dans le champ
**Client à refacturer**.

## Refacturer une dépense

Une fois ces étapes terminées, il est temps de revenir à la commande pour
terminer la refacturation de la dépense au client.

Pour ce faire, allez au tableau de bord principal d’Konvergo ERP ‣ application Ventes,
et sélectionnez la commande appropriée qui doit être refacturée pour la
dépense.

Sur la commande, la note de frais nouvellement configurée se trouve maintenant
dans l’onglet **Lignes de commande** , avec sa colonne **Livré** remplie et
prête à être facturée.

![Une commande avec la note de frais configurée prête à être facturée dans
l'onglet Lignes de commande.](../../../../_images/sales-order-with-expense-
order-lines.png)

Après avoir confirmé les détails de la note de frais, cliquez sur **Créer une
facture** en haut de la commande. Lorsque vous cliquez sur ce bouton, une
fenêtre contextuelle **Créer les factures** s’ouvre.

![Une fenêtre contextuelle permettant de créer des factures qui s'affiche
lorsque vous cliquez sur le bouton Créer une
facture.](../../../../_images/create-invoices-popup.png)

Dans cette fenêtre, laissez le champ **Créer une facture** sur la sélection
**Facture normale** par défaut et cliquez sur **Créer une facture brouillon**.

Cette opération fait apparaître une **Facture client brouillon** , qui montre
_uniquement_ la note de frais dans l’onglet **Lignes de facture**.

![Une facture client brouillon avec la note de frais dans l'onglet Lignes de
facture.](../../../../_images/customer-invoice-draft-with-expense.png)

Si toutes les informations relatives à la note de frais sont correctes,
cliquez sur **Confirmer`pour confirmer la facture. Ceci fait passer le statut
de la facture de :guilabel:`Brouillon** à **Comptabilisé**.

Pour envoyer la facture au client, cliquez sur **Envoyer & Imprimer**. Une
fenêtre contextuelle **Envoyer** s’ouvre avec un message préconfiguré et une
facture en PDF dans le corps du message. Le message peut être modifié si vous
le souhaitez.

Lorsque vous avez terminé, cliquez sur **Envoyer & Imprimer** pour envoyer la
facture au client. En cliquant sur le bouton, la fenêtre contextuelle
disparaît et Konvergo ERP envoie le message/la facture au client. De plus, un PDF de
la facture est automatiquement téléchargé à des fins d’archivage et/ou
d’impression.

De retour sur la **Facture client** , cliquez sur le bouton **Enregistrer un
paiement** lorsque le client paie la note de frais facturée.

![Une facture client avec le bouton Enregistrer un
paiement.](../../../../_images/customer-invoice-register-payment.png)

Lorsque vous cliquez sur le bouton **Enregistrer un paiement** , une fenêtre
contextuelle **Enregistrer un paiement** s’ouvre. Dans cette fenêtre
contextuelle, les champs nécessaires sont remplis automatiquement avec les
bonnes informations. Après avoir vérifié les informations, cliquez sur **Créer
un paiement**.

![Une fenêtre contextuelle permettant d'enregistrer un paiement sur une
facture client dans Konvergo ERP Ventes.](../../../../_images/register-payment-
popup.png)

Une fois que vous avez cliqué sur **Créer un paiement** , la fenêtre
contextuelle disparaît et une bannière verte **En paiement** apparaît dans le
coin supérieur droit de la facture, ce qui signifie que cette facture est
entièrement payée. Le flux de travail est ainsi terminé.

![Une fenêtre contextuelle permettant d'enregistrer un paiement sur une
facture client dans Konvergo ERP Ventes.](../../../../_images/expense-invoice-in-
payment-banner.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="invoicing_policy">Facturation basée sur les quantités livrées ou commandées</a></p></li>
<li><p><a href="time_materials">Facturation basée sur le temps et les matériaux</a></p></li>
<li><p><a href="milestone">Facturer les jalons d’un projet</a></p></li>
</ul>
</div>

