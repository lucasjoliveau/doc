# Actifs immobilisés et immobilisations

Les **Actifs immobilisés** , également connus sous le nom d”**actifs à long
terme** sont des investissements dont la réalisation est attendue après un an.
Ils sont capitalisés au lieu d’être passés en charges et figurent au bilan de
l’entreprise. Selon leur nature, ils peuvent faire l’objet d’un
**amortissement**.

Les **immobilisations** sont un type d’actifs immobilisés et comprennent les
biens achetés pour leurs aspects productifs, tels que les bâtiments, les
véhicules, les équipements, les terrains et les logiciels.

Par exemple, nous achetons un véhicule pour 27.000 $. Nous prévoyons de
l’amortir sur cinq ans et de le vendre ensuite pour 7.000 $. En utilisant la
méthode d’amortissement linéaire, 4.000 $ sont passés en charges chaque année
au titre de **charges d’amortissement**. Après cinq ans, le montant de
l”**amortissement** cumulé indiqué sur le bilan est de 20.000 $, ce qui nous
laisse une valeur de 7.000 $ **non amortissable** ou de valeur de
récupération.

Odoo Comptabilité gère l’amortissement en créant des écritures d’amortissement
automatiquement en _mode brouillon_. Elles sont ensuite comptabilisées
périodiquement.

Odoo prend en charge les **méthodes d’amortissement** suivantes :

  * Linéaire

  * Dégressif

  * Dégressif puis linéaire

Note

Le serveur vérifie une fois par jour si une écriture doit être comptabilisée.
Il peut donc s’écouler jusqu’à 24 heures avant que l’écriture ne passe du
statut _brouillon_ à celui de _comptabilisé_.

## Conditions préalables

Ces transactions doivent être comptabilisées sur un **Compte d’actifs** plutôt
que sur le compte de charges par défaut.

### Configurer un compte d’actifs

Pour configurer votre compte dans le **Plan comptable** , allez à Comptabilité
‣ Configuration ‣ Plan comptable, cliquez sur _Créer_ et remplissez le
formulaire.

![Configuration d'un Compte d'actifs dans Odoo
Comptabilité](../../../../_images/assets01.png)

Note

Le type de ce compte doit être soit _Immobilisations_ , soit _Actifs
immobilisés_.

### Comptabiliser une charge sur le bon compte

#### Sélectionner le compte sur une facture fournisseur brouillon

Sur une facture fournisseur brouillon, sélectionnez le bon compte pour tous
les actifs que vous achetez.

![Sélection d'un Compte d'actifs sur une facture fournisseur brouillon dans
Odoo Comptabilité](../../../../_images/assets02.png)

#### Choisir un compte de charges différent pour des produits spécifiques

Commencez par éditer le produit, allez à l’onglet _Comptabilité_ ,
sélectionnez le bon **Compte de charges** et enregistrez.

![Modifiez le compte d'actifs d'un produit dans
Odoo](../../../../_images/assets03.png)

Astuce

Il est possible d”automatiser la création d’écritures d’actifs pour ces
produits.

#### Modifier le compte d’une écriture comptable comptabilisée

Pour ce faire, ouvrez votre Journal des achats en allant à Comptabilité ‣
Comptabilité ‣ Achats, sélectionnez l’écriture comptable que vous souhaitez
modifier, cliquez sur le compte et sélectionnez le compte approprié.

![Modification du compte d'une écriture comptable enregistrée dans Odoo
Comptabilité](../../../../_images/assets04.png)

## Écritures d’actifs

### Créer une nouvelle écriture

Une **Écriture d’actifs** génère automatiquement toutes les écritures
comptables en _mode brouillon_. Elles sont comptabilisées une par une au bon
moment.

Pour créer une nouvelle écriture, allez à Comptabilité ‣ Comptabilité ‣
Actifs, cliquez sur _Créer_ et remplissez le formulaire.

Cliquez sur **sélectionner les achats associés** pour relier une écriture
comptable existante à cette nouvelle écriture. Certains champs sont alors
remplis automatiquement et l’écriture comptable est désormais répertoriée dans
l’onglet **Achats associés**.

![Écriture d'actifs dans Odoo Comptabilité](../../../../_images/assets05.png)

Une fois cela fait, vous pouvez cliquer sur _Calcul des amortissements_ (à
côté du bouton _Confirmer_) pour générer toutes valeurs dans le **Tableau
d’amortissement**. Ce tableau vous montre toutes les écritures qu’Odoo
enregistrera pour amortir votre actif, et à quelle date.

![Tableau d'amortissement dans Odoo
Comptabilité](../../../../_images/assets06.png)

#### Que signifie « Prorata Temporis » ?

La fonctionnalité _Prorata Temporis*_ est utile pour amortir vos actifs le
plus exactement possible.

Grâce à cette fonctionnalité, la première écriture du Tableau d’amortissement
est calculée sur la base du temps restant entre la _Date de prorata_ et la
_Première date d’amortissement_ plutôt que sur la base du temps par défaut
entre amortissements.

Par exemple, le tableau d’amortissement présente un premier amortissement d’un
montant de 241,10 $ au lieu de 4.000,00 $. Par conséquent, la dernière
écriture est également inférieure et s’élève à 3.758,90 $.

#### Quelles sont les différentes méthodes d’amortissement

La **Méthode d’amortissement linéaire** divise la valeur amortissable initiale
par le nombre d’amortissements prévus. Toutes les écritures d’amortissement
ont le même montant.

La **Méthode d’amortissement dégressif** multiplie la valeur amortissable par
le **Taux dégressif** pour chaque écriture. Chaque écriture d’amortissement a
un montant inférieur à l’écriture précédente. La dernière écriture
d’amortissement n’utilise pas le taux dégressif, mais a plutôt un montant
correspond au solde de la valeur amortissable, pour qu’il atteigne 0 $ à la
fin de la durée définie.

La **Méthode d’amortissement dégressif puis linéaire** utilise la méthode
dégressive, mais avec un amortissement minimum égal à la méthode linéaire.
Cette méthode garantit un amortissement rapide au début, suivi d’un
amortissement constant par la suite.

### Actifs à partir du Journal des ventes

Vous pouvez créer une écriture d’actifs à partir d’une écriture comptable
spécifique dans votre **Journal des achats**.

Pour ce faire, ouvrez votre Journal des achats en allant à Comptabilité ‣
Comptabilité ‣ Achats, et sélectionnez l’écriture comptable que vous souhaitez
enregistrer comme un actif. Assurez-vous qu’elle est enregistrée dans le bon
compte (voir : Modifier le compte d’une écriture comptable comptabilisée).

Ensuite, cliquez sur _Action_ , sélectionnez **Créer un actif** et remplissez
le formulaire de la même manière que vous le feriez pour créer une nouvelle
écriture.

![Créez une écriture d'actifs à partir d'une écriture comptable dans Odoo
Comptabilité](../../../../_images/assets07.png)

## Modification d’un actif

Vous pouvez modifier les valeurs d’un actif pour augmenter ou diminuer sa
valeur.

Pour ce faire, ouvrez l’actif que vous souhaitez modifier et cliquez sur
_Modifier l’amortissement_. Remplissez ensuite le formulaire avec les
nouvelles valeurs d’amortissement et cliquez sur _Modifier_.

Une **diminution de valeur** comptabilise une nouvelle pièce comptable pour la
**diminution de valeur** et modifie toutes les écritures comptables _non
comptabilisées_ futures énumérées dans le tableau d’amortissement.

Une **augmentation de valeur** vous oblige à remplir des champs
supplémentaires liés aux mouvements de compte et crée une nouvelle écriture
d’actifs avec l”**augmentation de valeur**. Vous pouvez accéder à l’écriture
d’actifs d’augmentation brute en cliquant sur le bouton intelligent.

![Bouton de l'augmentation brute dans Odoo
Comptabilité](../../../../_images/assets08.png)

## Cession d’immobilisations

Pour **vendre** une immobilisation ou la **céder** , elle doit être supprimée
du bilan.

Pour ce faire, ouvrez l’immobilisation que vous voulez céder, cliquez sur
**Vendre ou céder** et remplissez le formulaire.

![Cession d'immobilisations dans Odoo
Comptabilité](../../../../_images/assets09.png)

Odoo Comptabilité génère ensuite toutes les écritures comptables nécessaires à
la cession de l’immobilisation, y compris le gain ou la perte sur la vente,
basé sur la différence entre la valeur comptable de l’actif au moment de la
vente et le montant pour lequel il est vendu.

Note

Pour enregistrer la vente d’un actif, vous devez d’abord comptabiliser la
facture client correspondante afin de pouvoir relier la vente de l’actif à
cette facture.

## Modèles d’actifs

Vous pouvez créer des **Modèles d’actifs** pour créer vos écritures d’actifs
plus rapidement. C’est particulièrement utile si vous achetez fréquemment le
même type d’actifs.

Pour créer un modèle, allez à Comptabilité ‣ Configuration ‣ Modèles d’actifs,
cliquez sur _Créer_ et remplissez le formulaire de la même manière que vous le
feriez pour créer une nouvelle écriture.

Astuce

Vous pouvez également convertir une _écriture d’actifs confirmée_ en modèle en
l’ouvrant à partir de Comptabilité ‣ Comptabilité ‣ Actifs et en cliquant
ensuite sur le bouton _Enregistrer le modèle_.

### Appliquer un modèle d’actif à une nouvelle écriture

Lorsque vous créez une nouvelle écriture d’actifs, remplissez le **Compte
d’immobilisation** avec le bon compte d’actif.

De nouveaux boutons avec tous les modèles liés à ce compte apparaissent en
haut du formulaire. En cliquant sur le bouton d’un modèle, le formulaire se
remplit en fonction de ce modèle.

![Bouton modèle d'actifs dans Odoo
Comptabilité](../../../../_images/assets10.png)

## Automatiser les actifs

Lorsque vous créez ou modifiez un compte dont le type est soit _Actifs
immobilisés_ , soit _Immobilisations_ , vous pouvez le configurer pour qu’il
crée automatiquement des actifs pour les charges qui y sont créditées.

Vous avez trois choix pour le champ **Automatiser des actifs** :

  1. **Non :** c’est la valeur par défaut. Rien ne se passe.

  2. **Créer en brouillon :** chaque fois qu’une transaction est enregistrée sur le compte, une _écriture d’actifs_ brouillon est créée, mais pas validée. Vous devez d’abord remplir le formulaire dans Comptabilité ‣ Comptabilité ‣ Actifs.

  3. **Créer et valider :** vous devez également sélectionner un modèle d’actif (voir : Modèles d’actifs). Chaque fois qu’une transaction est enregistrée sur le compte, une _écriture d’actifs_ est créée et immédiatement validée.

![Automatisez les actifs sur un compte dans Odoo
Comptabilité](../../../../_images/assets11.png)

Astuce

Vous pouvez, par exemple, sélectionner ce compte comme le **Compte de
charges** par défaut d’un produit pour automatiser complètement son achat.
(voir : Choisir un compte de charges différent pour des produits spécifiques).

Pour plus d'infos

  * [Plan comptable](../get_started/chart_of_accounts.html)

