# Charges constatées d’avance et acomptes

Les **charges constatées d’avance** et les **acomptes** sont des coûts qui se
sont déjà produits pour des produits non consommés ou des services à recevoir.

Ces coûts constituent des **actifs** pour l’entreprise qui les paie
puisqu’elle a déjà payé pour des produits ou des services qu’elle n’a pas
encore reçus ou qui n’ont pas encore été utilisés. L’entreprise ne peut pas
les faire figurer sur le **Compte de résultat** ou **Compte de pertes et
profits** en cours, puisque les paiements seront effectivement comptabilisés
en charges à l’avenir.

Ces charges futures doivent être reportées dans le bilan de l’entreprise
jusqu’au moment où elles peuvent être **comptabilisées** , en une fois ou sur
une période définie, dans le compte de résultat.

Par exemple, nous payons 1.200 $ en une seule fois pour une année d’assurance.
Nous avons déjà payé le coût, mais nous n’avons pas encore utilisé le service.
Par conséquent, nous comptabilisons cette nouvelle dépense dans un _compte
d’acompte_ et décidons de la comptabiliser sur une base mensuelle. Chaque
mois, pendant les 12 prochains mois, 100 $ seront comptabilisés en tant que
charge.

Odoo Comptabilité gère les charges constatées d’avance et les acomptes en les
répartissant en plusieurs écritures qui sont automatiquement créées en _mode
brouillon_ puis comptabilisées périodiquement.

Note

Le serveur vérifie une fois par jour si une écriture doit être comptabilisée.
Il peut donc s’écouler jusqu’à 24 heures avant que l’écriture ne passe du
statut _brouillon_ à celui de _comptabilisé_.

## Conditions préalables

Ces transactions doivent être comptabilisées sur un **compte de charges
constatées d’avance** plutôt que sur le compte des charges par défaut.

### Configurer un compte de charges constatées d’avance

Pour configurer votre compte dans le **Plan comptable** , allez à Comptabilité
‣ Configuration ‣ Plan comptable, cliquez sur _Créer_ et remplissez le
formulaire.

![Configuration d'un compte de charges constatées d'avance dans Odoo
Comptabilité](../../../../_images/deferred_expenses01.png)

Note

Ce type de compte doit être soit _Actifs circulants_ , soit _Acomptes_.

### Comptabiliser une charge sur le bon compte

#### Sélectionner le compte sur une facture fournisseur brouillon

Sur une facture brouillon, sélectionnez le bon compte pour tous les produits
dont les charges doivent être reportées.

![Sélection d'un compte de charges constatées d'avance sur une facture
fournisseur brouillon dans Odoo
Comptabilité](../../../../_images/deferred_expenses02.png)

#### Choisir un compte de charges différent pour des produits spécifiques

Commencez par éditer le produit, allez à l’onglet _Comptabilité_ ,
sélectionnez le bon **Compte de charges** et enregistrez.

![Modifier le Compte des charges d'un produit dans
Odoo](../../../../_images/deferred_expenses03.png)

Astuce

Il est possible d’automatiser la création des écritures de charges pour ces
produits (voir : Automatiser les charges constatées d’avance).

#### Modifier le compte d’une écriture comptable comptabilisée

Pour ce faire, ouvrez votre Journal des achats en allant à Comptabilité ‣
Comptabilité ‣ Achats, sélectionnez l’écriture comptable que vous souhaitez
modifier, cliquez sur le compte et sélectionnez le compte approprié.

![Modification du compte d'une écriture comptable enregistrée dans Odoo
Comptabilité](../../../../_images/deferred_expenses04.png)

## Écritures de charges constatées d’avance

### Créer une nouvelle écriture

Une **écriture de charges constatées d’avance** génère automatiquement toutes
les écritures comptables en _mode brouillon_. Elles sont ensuite
comptabilisées une par une au bon moment jusqu’à ce que le montant total de la
charge est comptabilisé.

Pour créer une nouvelle écriture, allez à Comptabilité ‣ Comptabilité ‣
Charges constatées d’avance, cliquez sur _Créer_ et remplissez le formulaire.

Cliquez sur **sélectionner les achats associés** pour relier une écriture
comptable existante à cette nouvelle écriture. Certains champs sont alors
remplis automatiquement et l’écriture comptable est désormais répertoriée dans
l’onglet **Charges associées**.

![Écriture de charges constatées d'avance dans Odoo
Comptabilité](../../../../_images/deferred_expenses05.png)

Une fois cela fait, vous pouvez cliquer sur _Calculer le report_ (à côté du
bouton _Confirmer_) pour générer toutes les valeurs du **Tableau des
charges**. Ce tableau vous montre toutes les écritures qu’Odoo enregistrera
pour comptabiliser votre charge, et à quelle date.

![Tableau des charges dans Odoo
Comptabilité](../../../../_images/deferred_expenses06.png)

#### Que signifie « Prorata Temporis » ?

La fonctionnalité **Prorata Temporis** est utile pour comptabiliser vos
charges le plus exactement possible.

Grâce à cette fonctionnalité, la première écriture du tableau des charges est
calculée sur la base du temps restant entre la _Date au prorata_ et la
_Première date de comptabilisation_ , plutôt que sur la base du temps par
défaut entre deux comptabilisations.

Par exemple, le tableau des charges présente une première charge d’un montant
de 70,97 $ plutôt que 100,00 $. Par conséquent, la dernière écriture est
également inférieure et s’élève à 29,03 $.

### Écriture à reporter à partir du Journal des achats

Vous pouvez créer une écriture à reporter à partir d’une écriture comptable
spécifique dans votre **Journal des achats**.

Pour ce faire, ouvrez votre Journal des achats en allant à Comptabilité ‣
Comptabilité ‣ Achats, et sélectionnez l’écriture comptable que vous souhaitez
reporter. Assurez-vous qu’elle est enregistrée dans le bon compte (voir:
Modifier le compte d’une écriture comptable enregistrée).

Ensuite, cliquez sur _Action_ , sélectionnez **Créer une écriture à reporter**
et remplissez le formulaire de la même manière que vous le feriez pour créer
une nouvelle écriture.

![Créez une écriture à reporter à partir d'une écriture comptable dans Odoo
Comptabilité](../../../../_images/deferred_expenses07.png)

## Modèles de charges constatées d’avance

Vous pouvez créer des **Modèles de charges constatées d’avance** pour créer
vos écritures de charges constatées d’avance plus rapidement.

Pour créer un modèle, allez à Comptabilité ‣ Configuration ‣ Modèles de
charges constatées d’avance, cliquez sur _Créer_ et remplissez le formulaire
de la même manière que vous le feriez pour créer une nouvelle écriture.

Astuce

Vous pouvez également convertir une _écriture de charges constatées d’avance
confirmées_ en un modèle en l’ouvrant depuis Comptabilité ‣ Comptabilité ‣
Charges constatées d’avance puis, en cliquant sur le bouton _Enregistrer le
modèle_.

### Appliquer un modèle de charges constatées d’avance à une nouvelle
écriture

Lorsque vous créez une nouvelle écriture de charges constatées d’avance,
remplissez le **Compte de charges constatées d’avance** avec le bon compte de
comptabilisation.

De nouveaux boutons avec tous les modèles liés à ce compte apparaissent en
haut du formulaire. En cliquant sur le bouton d’un modèle, le formulaire se
remplit en fonction de ce modèle.

![Bouton Modèle de charges constatées d'avance dans Odoo
Comptabilité](../../../../_images/deferred_expenses08.png)

## Automatiser les charges constatées d’avance

Lorsque vous créez ou modifiez un compte dont le type est soit _Actifs
circulants_ , soit _Acomptes_ , vous pouvez le configurer pour qu’il crée
automatiquement les charges qui y sont créditées.

Vous avez le choix entre trois options pour le champ _Automatiser les charges
constatées d’avance*_ :

  1. **Non :** c’est la valeur par défaut. Rien ne se passe.

  2. **Créer en brouillon :** chaque fois qu’une transaction est enregistrée sur le compte, une _écriture de charges constatées d’avance_ brouillon est créée, mais pas validée. Vous devez d’abord compléter le formulaire dans Comptabilité ‣ Comptabilité ‣ Charges constatées d’avance.

  3. **Créer et valider :** vous devez également sélectionner un modèle de charges constatées d’avance (voir : Modèles de charges constatées d’avance). Chaque fois qu’une transaction est enregistrée sur le compte, une _écriture de charges constatées d’avance_ est créée et immédiatement validée.

![Automatisez les charges constatées d'avance sur un compte dans Odoo
Comptabilité](../../../../_images/deferred_expenses09.png)

Astuce

Vous pouvez, par exemple, sélectionner ce compte comme le **Compte des
charges** par défaut d’un produit pour automatiser complètement son achat
(voir : Choisir un compte de charges différent pour des produits spécifiques).

Pour plus d'infos

  * [Plan comptable](../get_started/chart_of_accounts.html)

