# Taxes flexibles (positions fiscales)

Lorsque vous gérez une entreprise, vous pouvez être amené à appliquer
différentes taxes et à enregistrer des transactions sur différents comptes en
fonction de la localisation et du type d’activité de vos clients et
fournisseurs.

La fonctionnalité **positions fiscales** vous permet d’établir des règles qui
sélectionnent automatiquement les bonnes taxes et les bons comptes à utiliser
pour chaque transaction.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../finance/accounting/taxes/fiscal_positions">Positions fiscales (correspondances de taxes et de comptes)</a></p></li>
<li><p><a href="../../../finance/accounting/taxes">Taxes</a></p></li>
</ul>
</div>

## Configuration

Pour activer la fonctionnalité, allez à Point de Vente ‣ Configuration ‣
Paramètres, descendez jusqu’à la section **Comptabilité** et activez **Taxes
flexibles**.

Ensuite, définissez une position fiscale qui devrait s’appliquer à toutes les
ventes dans le PdV sélectionnez dans le champ **Par défaut**. Vous pouvez
également ajouter d’autres positions fiscales dans le champ **Autorisé**.

![../../../../_images/flexible-taxes-
setting.png](../../../../_images/flexible-taxes-setting.png)

Selon le [package de localisation
fiscale](../../../finance/fiscal_localizations) activé, plusieurs
positions fiscales sont préconfigurées et peuvent être définies et utilisées
dans le PdV. Cependant, vous pouvez également [créer de nouvelles positions
fiscales](../../../finance/accounting/taxes/fiscal_positions#fiscal-
positions-mapping).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous ne définissez pas de position fiscale, la taxe reste telle qu’elle est définie dans le champ <b>taxes client</b> de la fiche produit.</p>
</div>

## Utiliser des positions fiscales

Ouvrez une [session PdV](../../point_of_sale#pos-session-start) pour
utiliser l’une des positions fiscales autorisées. Ensuite, cliquez sur le
bouton **Taxe** à côté de l’icône en forme de **livre** et sélectionnez une
position fiscale dans la liste. Les règles définies s’appliquent alors
automatiquement à tous les produits soumis aux réglementations de la position
fiscale choisie.

![../../../../_images/set-tax.png](../../../../_images/set-tax.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si une position fiscale par défaut est définie, le bouton de taxe affiche le nom de la position fiscale.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/accounting/taxes/fiscal_positions">Positions fiscales (correspondances de taxes et de comptes)</a></p>
</div>

