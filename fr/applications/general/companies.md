# Sociétés

Un environnement de gestion centralisé vous permet de sélectionner plusieurs
sociétés simultanément et de définir leurs entrepôts, clients, équipements et
contacts spécifiques. Il vous offre la possibilité de générer des rapports de
chiffres agrégés sans changer d’interface, ce qui facilite les tâches
quotidiennes et le processus de gestion global.

## Gérer les sociétés et les enregistrements

Allez aux Paramètres ‣ Gérer des sociétés et remplissez le formulaire avec les
informations relatives à votre société. Si une _Société mère_ est
sélectionnée, les enregistrements sont partagés entre les deux sociétés (tant
que les deux environnements sont actifs).

![Aperçu d'un formulaire d'une nouvelle société dans
Odoo](../../_images/create_js_store_us.png)

Astuce

Activez le [mode développeur](developer_mode.html#developer-mode) pour choisir
une _Favicon_ pour chacune de vos entreprises et facilement les identifier par
les onglets du navigateur. Définissez la taille des fichiers de vos favicons à
16x16 ou 32x32 pixels. Les extensions JPG, PNG, GIF et ICO sont acceptées.

![Vue d'un navigateur web et la favicon pour une société spécifique choisie
dans Odoo](../../_images/favicon.png)

Basculez entre ou sélectionnez plusieurs sociétés en cliquant sur leurs cases
de sélection pour les activer. La société grisée est celle dont
l’environnement est utilisé. Pour changer d’environnement, cliquez sur le nom
de l’entreprise. Dans l’exemple ci-dessous, l’utilisateur a accès à trois
entreprises, deux sont activées et l’environnement utilisé est celui de _JS
Store US_.

![Vue du menu des sociétés via le tableau de bord principal dans
Odoo](../../_images/multi_companies_menu_dashboard.png)

Les données telles que les produits, les contacts et l’équipement peuvent être
partagées ou configurées pour être affichées uniquement pour une entreprise
spécifique. Pour ce faire, sur leurs formulaires, choisissez entre :

  * _Un champ vide_ : l’enregistrement est commun à toutes les sociétés.

  * _Ajout d’une entreprise_ : l’enregistrement est visible pour les utilisateurs connectés à cette entreprise spécifique.

![Vue d'un formulaire de produit mettant en évidence le champ société dans
Odoo Ventes](../../_images/product_form_company.png)

## Accès des employés

Once companies are created, manage your employees” [Access
Rights](users/access_rights.html) for _Multi Companies_.

![Vue d'un formulaire d'utilisateur mettant en évidence le champ multi-
sociétés dans l'onglet des droits d'accès dans
Odoo](../../_images/access_rights_multi_companies.png)

Si un utilisateur a de multiples sociétés _activées_ dans sa base de données,
et qu’il **modifie** un enregistrement, la modification se produit sur la
société liée à l’enregistrement.

Exemple : si vous modifiez une commande client émise sous JS Store US tout en
travaillant sur l’environnement JS Store Belgium, les modifications sont
appliquées sous JS Store US (la société à partir de laquelle la commande
client a été émise).

Lors de la **création** d’un enregistrement, l’entreprise prise en compte est
:

  * La société actuelle (celle active) ou,

  * Aucune entreprise n’est définie (sur les produits et les formulaires de contacts par exemple) ou,

  * La société définie est celle liée au document (comme si un enregistrement est en cours d’édition).

## Format des documents

Pour définir les formats des documents en fonction de chaque entreprise,
_activez_ et _sélectionnez_ le format respectif et, sous _Paramètres_ ,
cliquez sur _Configurer la mise en page du document_.

![Vue de la page des paramètres mettant en évidence le champ mise en page du
document dans Odoo](../../_images/document_layout.png)

## Opérations inter-entreprises

Tout d’abord, assurez-vous que chacune de vos entreprises soit correctement
paramétrée concernant :

  * [Chart of Accounts](../finance/accounting/get_started/chart_of_accounts.html)

  * [Taxes](../finance/accounting/taxes.html)

  * [Fiscal Positions](../finance/accounting/taxes/fiscal_positions.html)

  * [Journals](../finance/accounting/bank.html)

  * [Fiscal Localizations](../finance/fiscal_localizations.html)

  * [Pricelists](../sales/sales/products_prices/prices/pricing.html)

Maintenant, activez l’option _Opérations inter-entreprises_ dans les
_Paramètres_. Avec la société respective _activée_ et _sélectionnée_ ,
choisissez si vous souhaitez que les opérations entre les sociétés soient
synchronisées au niveau des factures client/fournisseur ou au niveau de
commandes client/fournisseur.

![Vue de la page des paramètres mettant en évidence le champ opérations inter-
entreprises dans Odoo](../../_images/inter_company_transactions.png)

  * **Synchroniser les factures client et fournisseur** : génère une facture lorsqu’une entreprise confirme une facture client/fournisseur pour l’entreprise sélectionnée.

_Exemple :_ une facture publiée sur JS Store Belgium, pour JS Store US, crée
automatiquement une facture fournisseur sur JS Store US, à partir de JS Store
Belgium.

![Vue d'une facture pour JS Store US créée sur JS Store Belgium dans
Odoo](../../_images/invoice_inter_company.png)

  * **Synchroniser les commandes client et fournisseur** : génère un bon de commande/d’achat brouillon à l’aide de l’entrepôt de l’entreprise sélectionnée lorsqu’un bon de commande/d’achat est confirmé pour l’entreprise sélectionnée. Si au lieu d’un bon de commande en brouillon, vous préférez le valider, activez la fonctionnalité _Validation automatique_.

_Exemple :_ lorsqu’un bon de commande pour JS Store US est confirmé sur JS
Store Belgium, un bon d’achat sur JS Store Belgium est automatiquement créé
(et confirmé si la fonctionnalité _Validation automatique_ a été activée).

![Vue de l'achat créé sur JS Store US depuis JS Store Belgium dans
Odoo](../../_images/purchase_order_inter_company.png)

Note

Les produits doivent être configurés comme _Peuvent être vendus_ et doivent
être partagés entre les entreprises.

Astuce

N’oubliez pas de tester tous les flux de travail en tant qu’un utilisateur
autre que l’administrateur.

Pour plus d'infos

  * [Directives multi-sociétés](../../developer/howtos/company.html)

  * [Système multidevise](../finance/accounting/get_started/multi_currency.html)

  * [Digest emails](companies/digest_emails.html)
  * [Modèles d’email](companies/email_template.html)

