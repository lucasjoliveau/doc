# Taxes

Il existe de nombreux types de **taxes** et leur application varie
considérablement, en fonction principalement de la localisation de votre
entreprise. Pour s’assurer qu’elles soient enregistrées avec précision, le
moteur de taxes d’Odoo prend en charge toutes sortes d’utilisations et de
calculs.

## Taxes par défaut

Les **Taxes par défaut** définissent les taxes qui sont automatiquement
sélectionnées lorsqu’il n’y a aucune indication sur la taxe à appliquer. Par
exemple, Odoo préremplit le champ **Taxes** avec les Taxes par défaut lorsque
vous créez un nouveau produit ou ajoutez une nouvelle ligne sur une facture.

![Odoo remplit automatiquement le champ de taxe en fonction des Taxes par
défaut](../../../_images/default-invoice-line.png)

Pour changer vos **Taxes par défaut** , allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Taxes ‣ Taxes par défaut, sélectionnez les taxes appropriées pour
votre **Taxe de vente** et **Taxe d’achat** par défaut et cliquez sur
_Enregistrer_.

![Définir les taxes à utiliser par défaut sur Odoo](../../../_images/default-
configuration.png)

Note

Les **Taxes par défaut** sont automatiquement configurées en fonction du pays
sélectionné lors de la création de votre base de données ou lorsque vous
configurez un [package de localisation
fiscale](../fiscal_localizations.html#fiscal-localizations-packages) pour
votre entreprise.

## Activer les Taxes de vente à partir de la vue Liste

Dans le cadre de votre [package de localisation
fiscale](../fiscal_localizations.html#fiscal-localizations-packages), la
plupart des taxes de vente de votre pays sont déjà préconfigurées dans votre
base de données. Cependant, seules quelques-unes sont activées par défaut,
afin que vous puissiez activer uniquement celles qui sont pertinentes pour vos
activités.

Pour activer les Taxes de vente, allez à Comptabilité ‣ Configuration ‣ Taxes
et utilisez le bouton à bascule _Actif_ pour activer ou désactiver une taxe.

![Activez les taxes préconfigurées dans Odoo
Comptabilité](../../../_images/list.png)

## Configuration

Pour modifier ou créer une **Taxe** , allez à Comptabilité ‣ Configuration ‣
Taxes et ouvrez une taxe ou cliquez sur _Créer_.

![Modification d'une taxe dans Odoo Comptabilité](../../../_images/edit.png)

Important

Les taxes ont trois étiquettes différentes, chacune ayant une utilisation
spécifique. Reportez-vous au tableau suivant pour voir où elles sont affichés.

Nom de la taxe | Étiquette sur facture | Groupe de taxes  
---|---|---  
Backend | Colonne _Taxes_ sur les factures exportées | Au-dessus de la ligne _Total_ sur les factures exportées  
  
### Options de base

#### Nom de la taxe

Le **nom de la taxe** tel que vous souhaitez l’afficher pour les utilisateurs
du backend. Il s’agit de l”étiquette que vous voyez lors de la modification
des commandes clients, des factures, des produits, etc.

#### Calcul de la taxe

  * **Groupe de taxes**

La taxe est une combinaison de plusieurs sous-taxes. Vous pouvez ajouter
autant de taxes que vous le souhaitez, dans l’ordre dans lequel vous souhaitez
qu’elles soient appliquées.

Important

Assurez-vous que l’ordre des taxes est correct, car l’ordre dans lequel elles
se trouvent peut avoir un impact sur le calcul des montants des taxes, surtout
si l’une des taxes affecte la base des suivantes.

  * **Fixe**

La taxe a un montant fixe dans la devise par défaut. Le montant reste le même,
quel que soit le prix de vente.

Par exemple, un produit a un prix de vente de 1.000$ et nous appliquons une
taxe fixe de _10$_. Nous obtenons alors :

Prix de vente du produit | Prix hors taxe | Taxe | Total  
---|---|---|---  
1.000 | 1.000 | 10 | 1.010,00  
  * **Pourcentage du prix**

Le _Prix de vente_ est la base imposable : le montant de la taxe est calculé
en multipliant le Prix de Vente par le pourcentage de la taxe.

Par exemple, un produit a un prix de vente de 1000$ et nous appliquons une
taxe de _10% du prix_. Nous obtenons alors :

Prix de vente du produit | Prix hors taxe | Taxe | Total  
---|---|---|---  
1.000 | 1.000 | 100 | 1.100,00  
  * **Pourcentage du prix toutes taxes comprises**

Le _Total_ est la base imposable : le montant de la taxe est un pourcentage du
Total.

Par exemple, un produit a un prix de vente de 1000$ et nous appliquons une
taxe de _10% du prix TTC_. Nous obtenons alors :

Prix de vente du produit | Prix hors taxe | Taxe | Total  
---|---|---|---  
1.000 | 1.000 | 111,11 | 1.111,11  

#### Actif

Seules les taxes **actives** peuvent être ajoutées aux nouveaux documents.

Important

Il n’est pas possible de supprimer des taxes déjà utilisées. Au lieu de cela,
vous pouvez les désactiver pour empêcher une utilisation future.

Note

Ce champ peut être modifié depuis la _Vue de Liste_. Voir ci-dessus pour plus
d’informations.

#### Portée de la taxe

La **Portée de la taxe** détermine l’application de la taxe, ce qui limite
également l’endroit où elle est affichée.

  * **Ventes** : Factures clients, taxes clients sur les produits, etc.

  * **Achats** : Factures fournisseurs, taxes fournisseurs sur les produits, etc.

  * **Aucun**

Astuce

Vous pouvez utiliser **Aucun** pour les taxes que vous souhaitez inclure dans
un Groupe de taxes, mais que vous ne souhaitez pas répertorier avec d’autres
Taxes de vente ou d’achat.

### Onglet Définition

Allouez avec précision le montant de la base imposable ou les pourcentages de
la taxe calculée sur plusieurs comptes et grilles fiscales.

![Allouer des montants de la taxe aux bons comptes et grilles
fiscales](../../../_images/definition.png)

  * **Basé sur** :

    * Base : le prix sur la ligne de facture

    * % de taxe : un pourcentage de la taxe calculée.

  * **Compte** : si défini, une écriture comptable supplémentaire est enregistrée.

  * **Grilles fiscales** : utilisées pour automatiquement générer des [déclarations de TVA](reporting/tax_returns.html), conformément à la réglementation en vigueur dans votre pays.

### Onglet Options avancées

#### Étiquettes sur les factures

L’étiquette de la taxe, telle qu’elle s’affiche sur chaque ligne de facture
dans la colonne **Taxes**. Il s’agit de l”étiquette visible par les
utilisateurs _frontend_ , sur les factures exportées, sur leurs portails
clients, etc.

![L'étiquette sur les factures s'affiche sur chaque ligne de
facture](../../../_images/invoice-label.png)

#### Groupe de taxes

Sélectionnez à quel **groupe de taxes** appartient la taxe. Le nom du groupe
de taxes est l”étiquette affichée au-dessus de la ligne _Total_ sur les
factures exportées et les portails clients.

Les groupes de taxes comprennent différentes itérations de la même taxe. Cela
peut être utile lorsque vous devez enregistrer différemment la même taxe en
fonction des [positions fiscales](taxes/fiscal_positions.html).

![Le nom du groupe de taxes est différent de l'étiquette sur les
factures](../../../_images/invoice-tax-group.png)

Dans l’exemple ci-dessus, vous voyez une taxe de 0% pour les clients intra-
communautaires en Europe. Elle enregistre les montants sur des comptes
spécifiques et avec des grilles fiscales spécifiques. Pourtant, pour le
client, il s’agit d’une taxe à 0%. C’est pourquoi l”étiquette sur la facture
indique _0% UE_ et le nom du groupe de taxes, au-dessus de la ligne _Total_ ,
indique _0%_.

#### Inclure dans le coût analytique

Lorsque cette option est activée, le montant de la taxe est affecté au même
**compte analytique** que la ligne de facture.

#### Inclus dans le prix

Quand cette option est activée, le total (TTC) est égal au **Prix de vente**.

Total = Prix de vente = Prix calculé hors taxes + Taxes

Par exemple, un produit a un prix de vente de 1.000$ et nous appliquons une
taxe de _10% du prix_ , qui est _incluse dans le prix_. Nous obtenons alors :

Prix de vente du produit | Prix hors taxe | Taxe | Total  
---|---|---|---  
1.000 | 900,10 | 90,9 | 1.000,00  
  
Note

Si vous avez besoin de définir avec précision des prix, hors taxes ou toutes
taxes comprises, veuillez consulter la documentation suivante : [Prix B2B
(hors taxes) et B2C (toutes taxes comprises)](taxes/B2B_B2C.html).

Note

  * **Factures** : Par défaut, les sous-totaux de ligne affichés sur vos factures sont _hors taxes_. Pour afficher les sous-totaux de ligne _toutes taxes comprises_ , allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Factures clients, sélectionnez _toutes taxes comprises_ dans le champ **Affichage du sous-total des lignes** et cliquez sur _Enregistrer_.

  * **eCommerce** : Par défaut, les prix affichés sur votre site web eCommerce sont _hors taxes_. Pour afficher les prix _toutes taxes comprises_ , allez à Site Web ‣ Configuration ‣ Paramètres ‣ Tarif, sélectionnez _Toutes taxes comprises_ dans le champ **Prix des produits** et cliquez sur _Enregistrer_.

#### Impacter la base des taxes ultérieures

Avec cette option, le total TTC devient la base imposable des autres taxes
appliquées au même produit.

Vous pouvez configurer un nouveau Groupe de Taxes pour inclure cette taxe ou
l’ajouter directement à une ligne de produit.

![L'écotaxe est prise en compte dans la base de la TVA de
21%](../../../_images/subsequent-line.png)

Avertissement

L’ordre dans lequel vous ajoutez les taxes sur une ligne de produit n’a aucun
effet sur la façon dont les montants sont calculés. Si vous ajoutez les taxes
directement sur une ligne de produit, seule la séquence des taxes détermine
l’ordre dans lequel elles sont appliquées.

Pour réorganiser la séquence, allez à Comptabilité ‣ Configuration ‣ Taxes, et
faites glisser et déposer les lignes avec les indicateurs situés à côté des
noms de taxes.

![La séquence des taxes dans Odoo détermine quelle taxe s'applique en
premier](../../../_images/list-sequence.png)

Pour plus d'infos

  * [Positions fiscales (correspondances de taxes et de comptes)](taxes/fiscal_positions.html)

  * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](taxes/B2B_B2C.html)

  * [Intégration TaxCloud](taxes/taxcloud.html) (déclassement de l’intégration TaxCloud dans Odoo 17+)

  * [Déclaration d’impôt](reporting/tax_returns.html)

  * [TVA sur encaissements](taxes/cash_basis.html)
  * [Retenues à la source](taxes/retention.html)
  * [Vérification des numéros de TVA (VIES)](taxes/vat_verification.html)
  * [Positions fiscales (correspondances de taxes et de comptes)](taxes/fiscal_positions.html)
  * [AvaTax integration](taxes/avatax.html)
    * [AvaTax use](taxes/avatax/avatax_use.html)
    * [Avalara (Avatax) portal](taxes/avatax/avalara_portal.html)
  * [Intégration TaxCloud](taxes/taxcloud.html)
  * [Vente à distance intracommunautaire UE](taxes/eu_distance_selling.html)
  * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](taxes/B2B_B2C.html)

