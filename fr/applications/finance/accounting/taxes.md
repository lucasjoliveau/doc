# Taxes

Il existe de nombreux types de **taxes** et leur application varie
considérablement, en fonction principalement de la localisation de votre
entreprise. Pour s’assurer qu’elles soient enregistrées avec précision, le
moteur de taxes d’Konvergo ERP prend en charge toutes sortes d’utilisations et de
calculs.

## Taxes par défaut

Les **Taxes par défaut** définissent les taxes qui sont automatiquement
sélectionnées lorsqu’il n’y a aucune indication sur la taxe à appliquer. Par
exemple, Konvergo ERP préremplit le champ **Taxes** avec les Taxes par défaut lorsque
vous créez un nouveau produit ou ajoutez une nouvelle ligne sur une facture.

![Konvergo ERP remplit automatiquement le champ de taxe en fonction des Taxes par
défaut](../../../_images/default-invoice-line.png)

Pour changer vos **Taxes par défaut** , allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Taxes ‣ Taxes par défaut, sélectionnez les taxes appropriées pour
votre **Taxe de vente** et **Taxe d’achat** par défaut et cliquez sur
_Enregistrer_.

![Définir les taxes à utiliser par défaut sur Konvergo ERP](../../../_images/default-
configuration.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les <b>Taxes par défaut</b> sont automatiquement configurées en fonction du pays sélectionné lors de la création de votre base de données ou lorsque vous configurez un <a href="../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">package de localisation fiscale</span></a> pour votre entreprise.</p>
</div>

## Activer les Taxes de vente à partir de la vue Liste

Dans le cadre de votre [package de localisation
fiscale](../fiscal_localizations#fiscal-localizations-packages), la
plupart des taxes de vente de votre pays sont déjà préconfigurées dans votre
base de données. Cependant, seules quelques-unes sont activées par défaut,
afin que vous puissiez activer uniquement celles qui sont pertinentes pour vos
activités.

Pour activer les Taxes de vente, allez à Comptabilité ‣ Configuration ‣ Taxes
et utilisez le bouton à bascule _Actif_ pour activer ou désactiver une taxe.

![Activez les taxes préconfigurées dans Konvergo ERP
Comptabilité](../../../_images/list.png)

## Configuration

Pour modifier ou créer une **Taxe** , allez à Comptabilité ‣ Configuration ‣
Taxes et ouvrez une taxe ou cliquez sur _Créer_.

![Modification d'une taxe dans Konvergo ERP Comptabilité](../../../_images/edit.png)
<div class="alert alert-warning" id="taxes-labels">
<p class="alert-title">
Important</p><p>Les taxes ont trois étiquettes différentes, chacune ayant une utilisation spécifique. Reportez-vous au tableau suivant pour voir où elles sont affichés.</p>
<table class="table docutils">
<colgroup>
<col style="width: 26%"/>
<col style="width: 37%"/>
<col style="width: 37%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><a href="#taxes-name"><span class="std std-ref">Nom de la taxe</span></a></p></th>
<th class="head"><p><a href="#taxes-label-invoices"><span class="std std-ref">Étiquette sur facture</span></a></p></th>
<th class="head"><p><a href="#taxes-tax-group"><span class="std std-ref">Groupe de taxes</span></a></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Backend</p></td>
<td><p>Colonne <em>Taxes</em> sur les factures exportées</p></td>
<td><p>Au-dessus de la ligne <em>Total</em> sur les factures exportées</p></td>
</tr>
</tbody>
</table>
</div>

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

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Assurez-vous que l’ordre des taxes est correct, car l’ordre dans lequel elles se trouvent peut avoir un impact sur le calcul des montants des taxes, surtout si l’une des taxes <a href="#taxes-base-subsequent"><span class="std std-ref">affecte la base des suivantes</span></a>.</p>
</div>

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

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il n’est pas possible de supprimer des taxes déjà utilisées. Au lieu de cela, vous pouvez les désactiver pour empêcher une utilisation future.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ce champ peut être modifié depuis la <em>Vue de Liste</em>. Voir <a href="#taxes-list-activation"><span class="std std-ref">ci-dessus</span></a> pour plus d’informations.</p>
</div>

#### Portée de la taxe

La **Portée de la taxe** détermine l’application de la taxe, ce qui limite
également l’endroit où elle est affichée.

  * **Ventes** : Factures clients, taxes clients sur les produits, etc.

  * **Achats** : Factures fournisseurs, taxes fournisseurs sur les produits, etc.

  * **Aucun**

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez utiliser <b>Aucun</b> pour les taxes que vous souhaitez inclure dans un <a href="#taxes-computation"><span class="std std-ref">Groupe de taxes</span></a>, mais que vous ne souhaitez pas répertorier avec d’autres Taxes de vente ou d’achat.</p>
</div>

### Onglet Définition

Allouez avec précision le montant de la base imposable ou les pourcentages de
la taxe calculée sur plusieurs comptes et grilles fiscales.

![Allouer des montants de la taxe aux bons comptes et grilles
fiscales](../../../_images/definition.png)

  * **Basé sur** :

    * Base : le prix sur la ligne de facture

    * % de taxe : un pourcentage de la taxe calculée.

  * **Compte** : si défini, une écriture comptable supplémentaire est enregistrée.

  * **Grilles fiscales** : utilisées pour automatiquement générer des [déclarations de TVA](reporting/tax_returns), conformément à la réglementation en vigueur dans votre pays.

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
fonction des [positions fiscales](taxes/fiscal_positions).

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
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous avez besoin de définir avec précision des prix, hors taxes ou toutes taxes comprises, veuillez consulter la documentation suivante : <a href="taxes/B2B_B2C">Prix B2B (hors taxes) et B2C (toutes taxes comprises)</a>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p><b>Factures</b> : Par défaut, les sous-totaux de ligne affichés sur vos factures sont <em>hors taxes</em>. Pour afficher les sous-totaux de ligne <em>toutes taxes comprises</em>, allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Factures clients, sélectionnez <em>toutes taxes comprises</em> dans le champ <b>Affichage du sous-total des lignes</b> et cliquez sur <em>Enregistrer</em>.</p></li>
<li><p><b>eCommerce</b> : Par défaut, les prix affichés sur votre site web eCommerce sont <em>hors taxes</em>. Pour afficher les prix <em>toutes taxes comprises</em>, allez à Site Web ‣ Configuration ‣ Paramètres ‣ Tarif, sélectionnez <em>Toutes taxes comprises</em> dans le champ <b>Prix des produits</b> et cliquez sur <em>Enregistrer</em>.</p></li>
</ul>
</div>

#### Impacter la base des taxes ultérieures

Avec cette option, le total TTC devient la base imposable des autres taxes
appliquées au même produit.

Vous pouvez configurer un nouveau Groupe de Taxes pour inclure cette taxe ou
l’ajouter directement à une ligne de produit.

![L'écotaxe est prise en compte dans la base de la TVA de
21%](../../../_images/subsequent-line.png) <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>L’ordre dans lequel vous ajoutez les taxes sur une ligne de produit n’a aucun effet sur la façon dont les montants sont calculés. Si vous ajoutez les taxes directement sur une ligne de produit, seule la séquence des taxes détermine l’ordre dans lequel elles sont appliquées.</p>
<p>Pour réorganiser la séquence, allez à Comptabilité ‣ Configuration ‣ Taxes, et faites glisser et déposer les lignes avec les indicateurs situés à côté des noms de taxes.</p>
<img alt="La séquence des taxes dans Konvergo ERP détermine quelle taxe s'applique en premier" src="../../../_images/list-sequence.png"/>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="taxes/fiscal_positions">Positions fiscales (correspondances de taxes et de comptes)</a></p></li>
<li><p><a href="taxes/B2B_B2C">Prix B2B (hors taxes) et B2C (toutes taxes comprises)</a></p></li>
<li><p><a href="taxes/taxcloud">Intégration TaxCloud</a> (déclassement de l’intégration TaxCloud dans Konvergo ERP 17+)</p></li>
<li><p><a href="reporting/tax_returns">Déclaration d’impôt</a></p></li>
</ul>
</div>

  * [TVA sur encaissements](taxes/cash_basis)
  * [Retenues à la source](taxes/retention)
  * [Vérification des numéros de TVA (VIES)](taxes/vat_verification)
  * [Positions fiscales (correspondances de taxes et de comptes)](taxes/fiscal_positions)
  * [AvaTax integration](taxes/avatax)
    * [AvaTax use](taxes/avatax/avatax_use)
    * [Avalara (Avatax) portal](taxes/avatax/avalara_portal)
  * [Intégration TaxCloud](taxes/taxcloud)
  * [Vente à distance intracommunautaire UE](taxes/eu_distance_selling)
  * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](taxes/B2B_B2C)

