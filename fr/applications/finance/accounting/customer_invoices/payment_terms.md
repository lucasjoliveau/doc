# Conditions de paiement et plans de paiement échelonné

Les **Conditions de paiement** précisent toutes les conditions pour payer une
vente pour aider les clients à payer leurs factures correctement et à temps.

Les conditions de paiement sont générales définies sur des documents tels que
des commandes clients, des factures clients et des factures fournisseurs. Les
conditions de paiement couvrent :

  * La (les) date(s) d’échéance

  * Les escomptes

  * Toute autre condition de paiement

Un **plan de paiement échelonné** permet aux clients de régler une facture en
plusieurs fois, les montants et les dates de paiement étant définis
préalablement par le fournisseur.

<div class="alert alert-success">
<p class="alert-title">
Example</p><dl class="simple">
<dt>Paiement immédiat</dt><dd><p>Le paiement intégral est dû le jour de l’émission de la facture.</p>
</dd>
<dt>15 jours (ou Net 15)</dt><dd><p>Le paiement intégral est dû 15 jours après la date de facturation.</p>
</dd>
<dt>21 MFI</dt><dd><p>Le paiement intégral est dû pour le 21ème du mois suivant la date de facturation.</p>
</dd>
<dt>30% d’avance, fin du mois suivant</dt><dd><p>30% sont dus le jour de l’émission de la facture. Le solde est dû à la fin du mois suivant.</p>
</dd>
<dt>2% 10, Net 30 EOM</dt><dd><p>Un <a href="cash_discounts">escompte</a> de 2% est accordé si le paiement est reçu dans les dix jours. Sinon, le paiement intégral est dû à la fin du mois suivant la date de facturation.</p>
</dd>
</dl>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Il ne faut pas confondre les conditions de paiement et les <a href="../../../sales/sales/invoicing/down_payment">factures d’acompte</a>. Si vous émettez plusieurs factures à votre client pour une commande spécifique, il ne s’agit ni d’une condition de paiement, ni d’un plan de paiement échelonné, mais d’une politique de facturation.</p></li>
<li><p>Cette page parle des <em>conditions de paiement</em> et non des <a href="terms_conditions">conditions générales</a>, qui peuvent être utilisées pour déclarer des obligations contractuelles concernant l’utilisation du contenu, les politiques de retour et d’autres politiques relatives à la vente de biens et de services.</p></li>
</ul>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/payment-terms-1679">Tutoriels Konvergo ERP : conditions de paiement</a></p></li>
<li><p><a href="cash_discounts">Escomptes et réduction d’impôt</a></p></li>
</ul>
</div>

## Configuration

Pour créer de nouvelles conditions de paiement, suivez les étapes suivantes :

  1. Allez à Comptabilité ‣ Configuration ‣ Conditions de paiement et cliquez sur **Nouveau**.

  2. Saisissez un nom dans le champ **Conditions de paiement**. Ce champ est le nom affiché dans la base de données et ne s’affiche pas au client.

  3. Saisissez le texte à afficher sur le document (commande, facture, etc.) dans le champ **Description sur la facture**.

  4. Cochez la case **Afficher les conditions sur la facture** pour afficher le détail de chaque paiement et sa date d’échéance sur la facture si vous le souhaitez.

  5. Dans la section **Conditions** , ajoutez un ensemble de règles (délais) pour définir la somme à payer et à quelle(s) date(s) d’échéance. La définition des conditions permet de calculer automatiquement la (les) date(s) d’échéance des paiements. Cette fonction est particulièrement utile pour gérer les **plans de paiement échelonné** (conditions de paiement comportant plusieurs échéances).

Pour ajouter une échéance, cliquez sur **Ajouter une ligne** , définissez le
**Type d’échéance** et la **Valeur** et remplissez les champs appropriés pour
définir la date d’échéance de l’échéance, y compris les éventuelles
[remises](cash_discounts). Les dates d’échéance sont calculées en prenant
la date de facturation, en ajoutant d’abord les **Mois** et puis les
**Jours**. Si l’option **Fin de mois** est activée, la date d’échéance sera
alors la fin de ce mois, plus les **Jours après la fin du mois**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Au lieu de préciser un nombre de jours <em>avant la fin du mois</em>, utilisez une valeur négative dans le champ <b>Jours après la fin du mois</b>.</p>
</div>

Pour tester que vos conditions de paiement sont configurées correctement,
saisissez un montant et une date de facture dans la section **Exemple** pour
générer les paiements qui seraient dus et leurs dates d’échéance en utilisant
ces conditions de paiement.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Les conditions sont calculées dans l’ordre de leurs échéances.</p></li>
<li><p>Le <b>solde</b> doit toujours être utilisé pour la dernière ligne.</p></li>
</ul>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><p>Dans l’exemple suivant, 30% sont dus le jour de l’émission de la facture et le solde est dû à la fin du mois suivant.</p>
<img alt="Exemple de conditions de paiement. La dernière ligne est le solde dû le 31ème du mois suivant." src="../../../../_images/configuration.png"/>
</div>

## Utiliser des conditions de paiement

Les conditions de paiement peuvent être définies par le biais du champ
**Conditions de paiement** dans :

  * **Contacts :** Pour automatiquement configurer des conditions de paiement sur les nouvelles commandes, factures clients et factures fournisseurs d’un contact. Elles peuvent être modifiées dans le fiche du contact, dans l’onglet **Ventes & Achats**.

  * **Devis/Commandes :** Pour automatiquement définir des conditions de paiement sur toutes les factures générées à partir d’un devis ou d’une commande.

Les conditions de paiement peuvent être définies dans le champ **Date
d’échéance** , à l’aide de la liste déroulante **Conditions** sur :

  * **Factures clients :** Pour définir des conditions de paiement spécifiques sur une facture client.

  * **Factures fournisseurs :** Pour définir des conditions de paiement sur une facture fournisseur.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>La définition de conditions de paiement sur une facture fournisseur est surtout utile pour gérer des conditions de paiement du fournisseur avec plusieurs versements ou escomptes. Sinon, il suffit de définir manuellement la <b>date d’échéance</b>. Si des conditions de paiement sont déjà définies, videz le champ pour sélectionner une date.</p>
</div>

## Pièces comptables

Les factures avec des conditions de paiement spécifiques génèrent différentes
_pièces comptables_ , avec une _écriture comptable_ pour chaque _date
d’échéance_ calculée.

Cela facilite les [suivis](../payments/follow_up) et le
[lettrage](../bank/reconciliation), car Konvergo ERP prend en compte chaque date
d’échéance, plutôt que la seule date d’échéance du solde. Cela permet
également d’obtenir une [balance âgée des
clients](../customer_invoices#customer-invoices-aging-report) précise.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Le montant débité du compte client est divisé en deux écritures comptables avec des dates d'échéance distinctes" src="../../../../_images/journal-entry.png"/>
<p>Dans cet exemple, une facture de 1.000 $ a été émise avec les conditions de paiement suivantes : <em>30% sont dus le jour de l’émission et le solde est dû à la fin du mois suivant.</em></p>
<table class="table docutils">
<colgroup>
<col style="width: 42%"/>
<col style="width: 25%"/>
<col style="width: 17%"/>
<col style="width: 17%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Compte</p></th>
<th class="head"><p>Date d’échéance</p></th>
<th class="head"><p>Débit</p></th>
<th class="head"><p>Crédit</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Compte client</p></td>
<td><p>21 février</p></td>
<td><p>300</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>Compte client</p></td>
<td><p>31 mars</p></td>
<td><p>700</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>Ventes de produits</p></td>
<td></td>
<td></td>
<td><p>1.000</p></td>
</tr>
</tbody>
</table>
<p>Les 1.000 $ débités du compte client sont divisés en deux écritures comptables distinctes. Les deux ont leur propre date d’échéance.</p>
</div>

