# Plans d’abonnement

Les _plans d’abonnement_ sont des [modèles de
devis](../sales/send_quotations/quote_template) utilisés pour
préconfigurer des devis avec des produits d’abonnement. Utilisez des plans
d’abonnement pour rapidement créer des commandes d’abonnement.

## Configurer des plans d’abonnement

Pour configurer les plans d’abonnement, allez à Abonnements ‣ Configuration ‣
Plans. Cliquez ensuite sur **Nouveau** pour créer un nouveau plan ou
sélectionnez un plan existant pour l’modifier.

Puisque l’application _Abonnements_ d’Konvergo ERP est étroitement intégrée à
l’application _Ventes_ , les plans d’abonnement sont basés sur le même
formulaire que les modèles de devis.

![Formulaire de configuration des plans d'abonnement \(des modèles de
devis\)](../../../_images/subplan-quotation-template.png)

Le formulaire de plan d’abonnement contient les options suivantes :

  * **Nom** : Donnez un nom au plan d’abonnement en haut de la page.

  * **Le devis expire après** : Saisissez le nombre de jours après lesquels le devis expire, à partir du jour auquel le devis est envoyé au client. Laissez ce champ à zéro pour que le devis n’expire jamais.

  * **Confirmation en ligne** : Cochez les cases à côté de **Signature** ou **Paiement** pour permettre au client de confirmer leur commande d’abonnement en signant ou en payant le devis. Activez les deux options pour laisser le choix au client. Activez aucune option pour uniquement confirmer le devis dans le backend.

  * **Confirmation Mail** : Select an [email template](../../general/companies/email_template) for the confirmation email that is automatically sent to the customer after the quotation is confirmed. Leave this field blank to send nothing.

    * Pour créer un nouveau modèle d’email, donnez un nom au modèle et cliquez sur **Créer et modifier**.

    * Pour modifier un modèle d’email existant, sélectionnez-en un dans le menu déroulant et cliquez sur la flèche du **lien interne** à la fin de la ligne.

  * **Récurrence** : Sélectionnez la période de récurrence utilisée pour le plan. Les périodes de récurrence disponibles sont les mêmes que celles qui sont configurées dans Abonnements ‣ Configuration ‣ Périodes de récurrence.

La sélection d’une **Récurrence** transforme le modèle de devis en un plan
d’abonnement et active les options supplémentaires suivantes :

  * **Durée** : Choisissez si le plan d’abonnement n’a pas de date de fin (**Pour toujours**) ou une durée **Fixe**.

    * Si la durée est définie sur **Pour toujours** , le plan d’abonnement sera renouvelé en permanence jusqu’à ce que soit le client, soit l’entreprise mette manuellement fin à l’abonnement.

    * Si la durée est **fixe** , choisissez une date à côté de **Résilier après** , qui détermine le nombre de jours après lesquels l’abonnement sera automatiquement résilié.

  * **Auto-résiliable** : Cochez cette case pour permettre au client de résilier lui-même son abonnement à partir du [portail client](../../websites/ecommerce/ecommerce_management/customer_accounts).

  * **Résiliation automatique** : Saisissez le nombre de jours après lesquels les abonnements _impayés_ dont la date d’échéance est _dépassée_ sont automatiquement résiliés.

  * **Journal de facturation** : Sélectionnez le journal comptable dans lequel les factures relatives à ce plan d’abonnement sont enregistrées. Laissez ce champ vide pour utiliser le journal des ventes avec la séquence la plus basse.

![Un plan d'abonnement avec la récurrence
sélectionnée.](../../../_images/subplan-recurrence.png)

Dans l’onglet **Lignes** , créez les lignes de commande pour le devis. Cliquez
sur **Ajouter un produit** , sélectionnez un produit à inclure dans le plan et
saisissez ensuite la **Quantité** et l”**Unité de mesure**. Ajoutez autant de
produits que vous le souhaitez aux lignes de commande.

Dans l’onglet **Produits optionnels** , saisissez tous les produits optionnels
que le client peut ajouter à leur devis avant de confirmer la commande.

Si le plan d’abonnement a des [Conditions
générales](../../finance/accounting/customer_invoices/terms_conditions)
uniques, ajoutez-les dans l’onglet **Conditions générales**. Si les conditions
générales sont précisées sur un plan, celles-ci seront utilisées au lieu des
conditions générales par défaut définies dans les paramètres de l’application
_Ventes_.

![L'onglet Conditions générales du plan
d'abonnement.](../../../_images/subplan-terms-conditions.png)

## Utiliser les plans d’abonnement sur les devis

Les devis pour les produits d’abonnement peuvent être créés à la fois dans
l’application _Abonnements_ et l’application _Ventes_.

À partir du tableau de bord des **Abonnements** , cliquez sur **Nouveau** pour
créer un nouveau devis. Sélectionnez ensuite un plan d’abonnement dans le
champ **Plan d’abonnement**.

La **Récurrence** , les produits et les autres informations du plan sont
automatiquement complétés. Le devis peut ensuite être modifié à votre guise.

À partir du tableau de bord des **Ventes** , cliquez sur **Nouveau** pour
créer un nouveau devis. Sélectionnez ensuite un plan d’abonnement dans le
champ **Modèle de devis**.

Toutes les commandes d’abonnement apparaissent sur le tableau de bord des
**Abonnements** , qu’elles aient été créées dans l’application _Abonnements_
ou dans l’application _Ventes_.

