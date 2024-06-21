# Produits constatés d’avance

Les **produits constatés d’avance** sont des paiements effectués à l’avance
par les clients pour des produits qui n’ont pas encore été livrés ou des
services qui n’ont pas encore été fournis.

Ces paiements constituent un **passif** pour l’entreprise qui les reçoit
puisqu’elle doit encore ces produits ou services aux clients. L’entreprise ne
peut pas les reporter sur le **compte de résultat** ou **compte de pertes et
profits** actuel, puisque les paiements seront effectivement perçus à
l’avenir.

Ces revenus futurs doivent être constatés d’avance au bilan de l’entreprise
jusqu’au moment où ils peuvent être **comptabilisés** , en une fois ou sur une
période définie, dans le compte de résultat.

Par exemple, nous vendons une garantie étendue de cinq ans pour 350 $. Nous
recevons déjà l’argent maintenant, mais nous ne l’avons pas encore gagné. Par
conséquent, nous comptabilisons ce nouveau revenu dans un compte de produits
constatés d’avance et décidons de le comptabiliser sur une base annuelle.
Chaque année, pendant les 5 prochaines années, 70 $ seront comptabilisés en
tant que revenus.

Konvergo ERP Comptabilité gère les produits constatés d’avance en les répartissant
dans plusieurs écritures qui sont automatiquement créées en _mode brouillon_
puis comptabilisées périodiquement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le serveur vérifie une fois par jour si une écriture doit être comptabilisée. Il peut donc s’écouler jusqu’à 24 heures avant que l’écriture ne passe du statut <em>brouillon</em> à celui de <em>comptabilisé</em>.</p>
</div>

## Conditions préalables

Ces transactions doivent être comptabilisées sur un **compte de produits
constatés d’avance** plutôt que sur le compte des revenus par défaut.

### Configurer un compte de produits constatés d’avance

Pour configurer votre compte dans le **Plan comptable** , allez à Comptabilité
‣ Configuration ‣ Plan comptable, cliquez sur _Créer_ et remplissez le
formulaire.

![Configuration d'un compte de produits constatés d'avance dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues01.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ce type de compte doit être soit <em>Passifs circulants</em>, soit <em>Passifs immobilisés</em>.</p>
</div>

### Enregistrer un revenu sur le bon compte

#### Sélectionner le compte sur une facture brouillon

Sur une facture brouillon, sélectionnez le bon compte pour tous les produits
dont les revenus doivent être reportés.

![Sélection d'un compte de produits constatés d'avance sur une facture
brouillon dans Konvergo ERP Comptabilité](../../../../_images/deferred_revenues02.png)

#### Choisir un compte des revenus différent pour des produits spécifiques

Commencez par éditer le produit, allez à l’onglet _Comptabilité_ ,
sélectionnez le bon **Compte des revenus** et enregistrez.

![Modifiez le Compte des revenus d'un produit dans
Konvergo ERP.](../../../../_images/deferred_revenues03.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Il est possible d’automatiser la création des écritures de revenus pour ces produits (voir : <a href="#automate-the-deferred-revenues">Automatiser les produits constatés d’avance</a>).</p>
</div>

#### Modifier le compte d’une écriture comptable comptabilisée

Pour ce faire, ouvrez votre Journal des ventes en allant à Comptabilité ‣
Comptabilité ‣ Ventes, sélectionnez l’écriture comptable que vous souhaitez
modifier, cliquez sur le compte et sélectionnez le compte approprié.

![Modification du compte d'une écriture comptable enregistrée dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues04.png)

## Écritures de produits constatés d’avance

### Créer une nouvelle écriture

Une **écriture de produits constatés d’avance** génère automatiquement toutes
les écritures comptables en _mode brouillon_. Elles sont ensuite enregistrées
une par une au bon moment jusqu’à ce que le montant total du revenu est
comptabilisé.

Pour créer une nouvelle écriture, allez à Comptabilité ‣ Comptabilité ‣
Produits constatés d’avance, cliquez sur _Créer_ et complétez le formulaire.

Cliquez sur **sélectionner les achats associés** pour relier une écriture
comptable existante à cette nouvelle écriture. Certains champs sont alors
remplis automatiquement et l’écriture comptable est désormais répertoriée dans
l’onglet **Ventes associées**.

![Écriture de produits constatés d'avance dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues05.png)

Une fois cela fait, vous pouvez cliquer sur _Calcul des produits_ (à côté du
bouton _Confirmer_) pour générer toutes les valeurs du **Tableau des
produits**. Ce tableau vous montre toutes les écritures qu’Konvergo ERP enregistrera
pour comptabiliser vos produits, et à quelle date.

![Tableau des produits dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues06.png)

#### Que signifie « Prorata Temporis » ?

La fonctionnalité **Prorata temporis** est utile pour comptabiliser vos
produits le plus exactement possible.

Grâce à cette fonctionnalité, la première écriture du tableau des produits est
calculée sur la base du temps restant entre la _Date de prorata_ et la
_Première date de comptabilisation_ , plutôt que sur la base du temps par
défaut entre comptabilisations.

Par exemple, le tableau des produits présente un premier produit d’un montant
de 4,22 $ au lieu de 70,00 $. Par conséquent, la dernière écriture est
également inférieure et s’élève à 65,78 $.

### Écriture à reporter à partir du Journal des ventes

Vous pouvez créer une écriture à reporter à partir d’une écriture comptable
spécifique dans votre **Journal des ventes**.

Pour ce faire, ouvrez votre Journal des ventes en allant à Comptabilité ‣
Comptabilité ‣ Ventes, et sélectionnez l’écriture comptable que vous souhaitez
reporter. Assurez-vous qu’elle est enregistrée dans le bon compte (voir :
Modifier le compte d’une écriture comptable enregistrée).

Ensuite, cliquez sur _Action_ , sélectionnez **Créer une écriture à reporter**
et remplissez le formulaire de la même manière que vous le feriez pour créer
une nouvelle écriture.

![Créez une écriture à reporter à partir d'une écriture comptable dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues07.png)

## Modèles de produits constatés d’avance

Vous pouvez créer des **modèles de produits constatés d’avance** pour créer
vos écritures de produits constatés d’avance plus rapidement.

Pour créer un modèle, allez à Comptabilité ‣ Configuration ‣ modèles de
produits constatés d’avance, cliquez sur _Créer_ , et complétez le formulaire
de la même manière que vous le feriez pour créer une nouvelle écriture.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez également convertir une <em>écriture de produits constatés d’avance confirmée</em> en un modèle en l’ouvrant à partir de Comptabilité ‣ Comptabilité ‣ Produits constatés d’avance puis en cliquant sur le bouton <em>Enregistrer le modèle</em>.</p>
</div>

### Appliquer un modèle de produits constatés d’avance à une nouvelle
écriture

Lorsque vous créez une nouvelle écriture de produits constatés d’avance,
remplissez le **Compte de produits constatés d’avance** avec le bon compte de
comptabilisation.

De nouveaux boutons avec tous les modèles liés à ce compte apparaissent en
haut du formulaire. En cliquant sur le bouton d’un modèle, le formulaire se
remplit en fonction de ce modèle.

![Bouton du modèle de produits constatés d'avance dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues08.png)

## Automatiser les produits constatés d’avance

Lorsque vous créez ou modifiez un compte dont le type est soit _Passifs
circulants_ , soit _Passifs immobilisés_ , vous pouvez le configurer pour
qu’il reporte automatiquement les produits qui y sont crédités.

Vous avez le choix entre trois options pour le champ **Automatiser les
produits constatés d’avance** :

  1. **Non :** c’est la valeur par défaut. Rien ne se passe.

  2. **Créer en brouillon :** chaque fois qu’une transaction est enregistrée sur le compte, une _écriture de produits constatés d’avance_ est créée en brouillon, mais pas validée. Vous devez d’abord remplir le formulaire dans Comptabilité ‣ Comptabilité ‣ Produits constatés d’avance.

  3. **Créer et valider :** vous devez également sélectionner un modèle de produits constatés d’avance (voir : Modèles de produits constatés d’avance). Chaque fois qu’une transaction est enregistrée sur le compte, une _écriture de produits constatés d’avance_ est créée et immédiatement validée.

![Automatiser les produits constatés d'avance sur un compte dans Konvergo ERP
Comptabilité](../../../../_images/deferred_revenues09.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez, par exemple, sélectionner ce compte comme le <b>Compte des revenus</b> par défaut d’un produit pour automatiser complètement sa vente (voir : <a href="#choose-a-different-income-account-for-specific-products">Choisir un compte des revenus différent pour des produits spécifiques</a>).</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../get_started/chart_of_accounts">Plan comptable</a></p></li>
<li><p><a href="https://www.odoo.com/r/EWO">Konvergo ERP Académie : Produits constatés d’avance (Comptabilisation)</a></p></li>
</ul>
</div>

