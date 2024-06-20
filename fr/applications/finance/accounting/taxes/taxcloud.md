# Intégration TaxCloud

Avertissement

L’intégration TaxCloud d’Odoo a commencé son déclassement, à partir d’Odoo 17.
Les nouvelles installations sont interdites dans Odoo 17. Dans Odoo 18, le(s)
module(s) TaxCloud **n’existera(ont)** plus du tout. Odoo recommande
l’utilisation de la plateforme Avatax.

Pour plus d'infos

[AvaTax integration](avatax.html)

TaxCloud calcule le taux de la taxe de vente en temps réel pour chaque État,
ville et juridiction spéciale des États-Unis. Il garde une trace des produits
qui sont exemptés de la taxe de vente et des États dans lesquels chaque
exonération s’applique.

## Inscription à TaxCloud

Enregistrez un compte sur [TaxCloud.com](https://taxcloud.com/register) et
terminez la configuration. Une fois en ligne, obtenez les TaxCloud API Keys en
cliquant sur Stores, en ensuite sur Get Details.

![Exemple des Clés API TaxCloud d'une boutique](../../../../_images/taxcloud-
api-keys.png)

## Activer TaxCloud

  1. Allez à Comptabilité ‣ Configuration ‣ Paramètres et dans la section Taxes, activez TaxCloud.

  2. Ajoutez le Login ID de la boutique dans le champ ID d’API et la Clé de la boutique dans le champ CLÉ API. Cliquez sur Enregistrer.

  3. Cliquez sur le bouton Rafraîchir (🗘) à côté de la Catégorie par défaut pour importer les TIC Taxability Information Codes des catégories de produits de TaxCloud. Certaines catégories peuvent impliquer des taux d’imposition ou des exonérations spécifiques.

  4. Sélectionnez une catégorie par défaut et cliquez sur Enregistrer. La catégorie par défaut s’applique lorsqu’aucune catégorie de TaxCloud n’est définie sur vos produits ou vos catégories de produits ou si aucun produit n’est trouvé sur une commande/facture.

![Compléter les clés API TaxCloud dans Odoo](../../../../_images/taxcloud-
settings.png)

## Définir des catégories TaxCloud sur des produits

Si vous devez utiliser plus d’une catégorie TIC (c’est-à-dire, la catégorie
par défaut), allez à l’onglet Informations générales du produit et
sélectionnez une catégorie TaxCloud.

Si vous souhaitez configurer plusieurs produits en même temps, assurez-vous
qu’ils partagent la même catégorie de produits et cliquez sur le bouton de
lien externe (🡕) pour définir une catégorie TaxCloud sur la catégorie de
produits.

Note

Si vous définissez une catégorie TaxCloud sur un produit et une autre sur sa
catégorie de produits, Odoo prend uniquement en compte la catégorie TaxCloud
définie sur le produit.

Une catégorie TaxCloud définie sur une **catégorie de produits mère** ne
s’applique pas à ses **catégories de produits enfants**. Par exemple, si vous
définissez une catégorie TaxCloud sur la catégorie de produits _Tous_ , elle
ne s’applique pas à la Product Category _Tous/Ventes_.

Important

Assurez-vous que l’adresse de votre entreprise est complète, y compris l’État
et le code postal. Allez à Paramètres ‣ Sociétés : Mise à jour de
l’information pour ouvrir et modifier l’adresse de votre entreprise.

## Comptabiliser automatiquement les taxes dans le bon compte de taxes à
payer

Pour vous assurer que les nouvelles taxes générées par l’intégration TaxCloud
sont créées avec le bon compte de **Taxes à payer** , créez une **valeur par
défaut de l’utilisateur**. Ce processus doit être répété pour chacune de vos
sociétés qui utilisent TaxCloud.

Avertissement

Une valeur par défaut de l’utilisateur a un impact sur tous les
enregistrements à la création. Cela signifie que **chaque** nouvelle taxe est
configurée pour enregistrer les revenus dans le compte de taxes à payer
précisé, à moins que la taxe ne soit modifiée manuellement pour spécifier un
compte de revenu différent (ou si une autre valeur par défaut définie de
l’utilisateur est prioritaire).

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Comptabilité : Plan
comptable, trouvez le compte Taxes à payer de l’entreprise et cliquez sur
Configuration. Prenez note du chiffre qui se trouve après `id=` dans la chaîne
URL ; il s’agit de l”**ID du compte des taxes à payer** , qui sera utilisé
ultérieurement.

![Exemple de l'ID d'un compte de taxes à payer dans la chaîne
URL](../../../../_images/tax-payable-id.png)

Activez le [mode développeur](../../../general/developer_mode.html#developer-
mode), allez ensuite à Paramètres ‣ Technique ‣ Actions : Valeurs par défaut
de l’utilisateur et cliquez sur Créer.

Cliquez sur le menu déroulant de Champ et ensuite sur Recherche avancée.

![Recherche dans le champ Valeurs par défaut définies de
l'utilisateur](../../../../_images/user-defaults-search-more.png)

Utilisez la barre de recherche pour filtrer le modèle Ligne de répartition de
la taxe et utilisez-la une deuxième fois pour filtrer le champ Compte.
Sélectionnez la ligne avec Ligne de répartition de la taxe dans la colonne
Modèle.

![Rechercher le modèle Ligne de répartition de la taxe et le champ
Compte](../../../../_images/user-defaults-search-filters.png)

Une fois que vous êtes revenu à la création des Valeurs par défaut de
l’utilisateur, entrez l”**ID du compte des taxes à payer** que vous avez noté
auparavant dans le champ Valeur par défaut (format JSON).

Sélectionnez l’entreprise à laquelle cette configuration doit s’appliquer dans
le champ Société et cliquez sur Enregistrer.

![Exemple d'une configuration de valeurs par défaut de
l'utilisateur](../../../../_images/user-defaults-complete-configuration.png)

## Détecter automatiquement la position fiscale

Les taxes de vente sont calculées dans Odoo en fonction des [positions
fiscales](fiscal_positions.html). Une position fiscale pour les États-Unis est
créée lors de l’activation de TaxCloud.

Vous pouvez configurer Odoo pour détecter automatiquement à quels clients la
position fiscale doit s’appliquer. Pour ce faire, allez à Comptabilité ‣
Configuration ‣ Comptabilité : Positions fiscales et sélectionnez Automatic
Tax Mapping (TaxCloud). Activez la fonction Détecter automatiquement et
cliquez ensuite sur Enregistrer.

![La fonction détecter automatiquement sur la position fiscale
TaxCloud](../../../../_images/fiscal-position-detect.png)

À présent, cette position fiscale est définie automatiquement sur toute
commande ou facture si le client provient des _États-Unis_. Cela déclenche le
calcul automatisé de la taxe.

Note

Pour obtenir les taxes de vente sur une commande client, confirmez-la ou
cliquez sur le bouton Mise à jour de la taxe à côté du bouton Ajouter
l’expédition.

## Interaction avec des coupons et des promotions

Si vous utilisez les **Programmes de coupon** ou **de promotion** ,
l’intégration avec TaxCloud pourrait se comporter de manière inattendue. En
effet, comme TaxCloud n’accepte pas les lignes avec des montants négatifs dans
le cadre du calcul de la taxe, le montant des lignes ajoutées par le programme
de promotion doit être déduit du total des lignes qu’il impacte.

Important

Cela signifie, entre autres complications, que les commandes utilisant des
coupons ou des promotions avec une position fiscale TaxCloud **doivent** être
facturées intégralement - vous ne pouvez pas créer de factures pour des
livraisons partielles, etc.

Vous pourriez voir un autre comportement inattendu. Par exemple, vous vendez
un produit pour lequel vous avez un programme de promotion qui prévoit une
remise de 50%. Si la TVA du produit est de 7%, la TVA calculée à partir de
l’intégration TaxCloud affiche 3,5%. En effet, la remise est comprise dans le
prix envoyé à TaxCloud. Toutefois, dans Odoo, la remise se trouve sur une
toute autre ligne. Pourtant, le calcul de la taxe est correct. Effectivement,
une taxe de 3,5% sur le prix total équivaut à une taxe de 7% sur la moitié du
prix, mais cela peut être inattendu du point de vue de l’utilisateur.

Pour plus d'infos

[Positions fiscales (correspondances de taxes et de
comptes)](fiscal_positions.html)

