# Rapports personnalisés

Odoo propose un cadre d’analyse puissant et facile d’utilisation. Le moteur
vous permet de créer de nouveaux rapports, tels que la **déclaration de TVA**
, le **bilan** ou le **compte de résultat** avec des **regroupements** et des
**mises en page spécifiques**.

Important

Activez le [mode développeur](../../../general/developer_mode.html#developer-
mode) pour accéder à l’interface de création des rapports comptables.

Pour créer un nouveau rapport, allez à Comptabilité ‣ Configuration ‣ Gestion
: Rapports comptables. À partir de là, vous pouvez créer soit un rapport
racine, soit une variante.

![Moteur des rapports comptables.](../../../../_images/engine-accounting-
reports.png)

## Rapports racines

Les rapports racines sont considérés comme des rapports comptables neutres et
génériques. Ils servent de modèles sur lesquels sont construites les versions
comptables locales. Si un rapport n’a pas de rapport racine, il est lui-même
considéré comme un rapport racine.

Example

Les déclarations d’impôt pour la Belgique et les États-Unis utiliseraient
toutes deux la même version générique comme base et seraient adaptées à leurs
réglementations nationales respectives.

Lors de la création d’un nouveau rapport racine, vous devez créer une
**rubrique** pour ce rapport. Pour ce faire, ouvrez le rapport et, sur ce même
rapport, cliquez sur Action ‣ Créer une rubrique. Actualisez la page ; le
rapport est désormais disponible sous Comptabilité ‣ Analyse.

Note

Les situations qui demandent la création d’un nouveau rapport racine sont
rares, par exemple lorsque les autorités fiscales d’un pays nécessitent un
nouveau type de rapport spécifique.

![Bouton de création de rubriques](../../../../_images/engine-create-menu-
item.png)

## Variantes

Les variantes sont des versions nationales des rapports racines et font donc
toujours référence à un rapport racine. Pour créer une variante, sélectionnez
un rapport (racine) générique dans le champ Rapport racine lors de la création
d’un nouveau rapport.

Lorsqu’un rapport racine est ouvert à partir d’un des menus principaux de
l’application Comptabilité, toutes ses variantes s’affichent dans le sélecteur
de variantes situé dans le coin supérieur droit de la vue.

Example

Dans l’image suivante, Déclaration à la TVA (BE) est la variante du rapport
racine Déclaration de TVA générique.

![Sélection des variantes de rapport.](../../../../_images/engine-variant.png)

## Lignes

Après avoir créé un rapport (racine ou variante), vous devez y ajouter des
lignes. Vous pouvez soit créer une nouvelle ligne en cliquant sur Ajouter une
ligne, soit modifier une ligne existante en cliquant dessus. Toutes les lignes
_demandent_ un Nom et peuvent avoir un Code supplémentaire facultatif (de
votre choix) si vous souhaitez utiliser leur valeur dans des formules.

![Moteur des options de ligne.](../../../../_images/engine-lines-options.png)

## Expressions

Chaque ligne peut contenir une ou plusieurs **expressions**. Les expressions
peuvent être considérées comme des **sous-variables** nécessaires à une ligne
de rapport. Pour créer une expression, cliquez sur Ajouter une ligne _dans_
une ligne de rapport.

Lors de la création d’une expression, vous devez attribuer un libellé afin de
faire référence à cette expression. Il doit donc être **unique** parmi les
expressions de chaque ligne. Vous devez également indiquer un Moteur de calcul
et une Formule. Le **moteur** définit comment vos **formules** et **sous-
formules** doivent être interprétées. Il est possible de mélanger des
expressions utilisant différents moteurs de calcul sur une même ligne si
nécessaire.

Note

Selon le moteur, des sous-formules peuvent également être nécessaires.

### Moteur “Domaine Odoo”

Avec ce moteur, une formule est interprétée comme un [domaine
Odoo](../../../../developer/reference/backend/orm.html#reference-orm-domains)
ciblant des objets `account.move.line`.

La sous-formule vous permet de définir comment les lignes d’écriture
correspondant au domaine sont utilisés pour calculer la valeur de l’expression
:

`sum`

    

Le résultat est la somme de tous les soldes des lignes d’écritures
correspondantes.

`sum_if_pos`

    

Le résultat est la somme de tous les soldes des lignes d’écriture
correspondantes si ce montant est positif. Sinon, il est égal à `0`.

`sum_if_neg`

    

Le résultat est la somme de tous les soldes des lignes d’écriture
correspondantes si ce montant est négatif. Sinon, il est égal à `0`.

`count_rows`

    

Le résultat est le nombre de sous-lignes de cette expression. Si la ligne
parente a une valeur group-by, cela correspondra au nombre de clés de
regroupement distinctes dans les lignes d’écriture correspondantes. Sinon, il
s’agira du nombre de lignes d’écriture correspondantes.

Vous pouvez également placer un signe `-` au début de la sous-formule pour
**inverser** le signe du résultat.

![Ligne d'expression dans une ligne de rapport](../../../../_images/engine-
expressions.png)

### Moteur des “Étiquettes de taxes”

Une formule faite pour ce moteur consiste en un nom utilisé pour faire
correspondre les étiquettes de taxes. Si ces étiquettes n’existent pas au
moment de créer l’expression, elles seront créées.

Lors de l’évaluation de l’expression, le calcul de l’expression peut être
grossièrement exprimé comme suit : **(montant des lignes d’écriture avec une
étiquette** `+` **)** `-` **(montant des lignes d’écriture avec une
étiquette** `-` **)**.

Example

Si la formule est `tag_name`, le moteur fait correspondre les étiquettes de
taxes `+tag_name` et `-tag_name`, les créant si nécessaire. Pour illustrer
davantage : deux étiquettes sont mises en correspondance par la formule. Si la
formule est `A`, elle demandera (et créera si nécessaire) les étiquettes `+A`
et `-A`.

### Moteur “Agréger d’autres formules”

Utilisez ce moteur si vous devez réaliser des opérations arithmétiques sur les
montants obtenus pour d’autres expressions. Les formules sont composées de
références aux expressions séparées par l’un des opérateurs arithmétiques de
base (addition `+`, soustraction `-`, division `/`, et multiplication `*`).
Pour faire référence à une expression, saisissez le **code** de sa ligne
parent, suivi d’un point `.` et du **libellé** de l’expression (par ex.
**code.label**).

Les **sous-formules** peuvent être l’une des suivantes :

`if_above(CUR(amount))`

    

La valeur de l’expression arithmétique ne sera renvoyée que si elle est
supérieure à la borne fournie. Sinon, le résultat sera `0`.

`if_below(CUR(amount))`

    

La valeur de l’expression arithmétique ne sera renvoyée que si elle est
inférieure à la borne fournie. Sinon, le résultat sera `0`.

`if_between(CUR1(amount1), CUR2(amount2))`

    

La valeur de l’expression arithmétique ne sera renvoyée que si elle est
strictement comprise entre les bornes fournies. Sinon, elle sera ramenée à la
borne la plus proche.

`if_other_expr_above(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`

    

La valeur de l’expression arithmétique ne sera renvoyée que si la valeur de
l’expression désignée par le code de ligne et le libellé d’expression fournis
est supérieure à la borne fournie. Sinon, le résultat sera `0`.

`if_other_expr_below(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`

    

La valeur de l’expression arithmétique ne sera renvoyée que si la valeur de
l’expression désignée par le code de ligne et le libellé d’expression fournis
est inférieure à la borne fournie. Sinon, le résultat sera `0`.

`CUR` est le code de la devise en lettres capitales et `amount` est le montant
de borne exprimée dans cette devise.

Vous pouvez également utiliser la sous-formule `cross_report` pour mettre en
correspondance une expression trouvée dans un autre rapport.

### Moteur “Préfixe des codes de compte”

Ce moteur est utilisé pour mettre en correspondance des montants effectués sur
des comptes en utilisant les préfixes des codes de ces comptes en tant que
variables dans une expression arithmétique.

Example

`21`

Les expressions arithmétiques peuvent également être un simple préfixe, comme
dans cet exemple.

Example

`21 + 10 - 5`

Cette formule additionne les soldes des lignes d’écritures effectuées sur les
comptes dont les codes commencent par `21` et `10`, et soustrait le solde des
lignes sur des comptes dont le préfixe est `5`.

Il est également possible d’ignorer une sélection de sous-préfixes.

Example

`21 + 10\(101, 102) - 5\(57)`

Cette formule fonctionne de la même façon que l’exemple précédent, mais ignore
les préfixes `101`, `102`, et `57`.

Vous pouvez appliquer un “sous-filtrage” sur les **crédits et débits** à
l’aide des suffixes `C` et `D`. Dans ce cas, un compte ne sera pris en
considération que si son préfixe correspond _et_ si le solde total des lignes
d’écriture effectuées sur ce compte est **créditeur/débiteur**.

Example

Le compte `210001` a un solde de -42 et le compte `210002` a un solde de 25.
La formule `21D` correspond uniquement au compte `210002`, et renvoie donc 25.
`210001` n’est pas pris en considération, car son solde est _créditeur_.

Les exclusions de préfixes peuvent être mélangées avec les suffixes `C` et
`D`.

Example

`21D + 10\(101, 102)C - 5\(57)`

Cette formule additionne les soldes des lignes d’écritures effectuées sur les
comptes dont le code commence par `21` _si_ c’est débiteur (`D`) et par `10`
_si_ c’est créditeur (`C`), mais ignore les préfixes `101`, `102`, et
soustrait le solde des lignes effectuées sur les comptes avec le préfixe `5`,
tout en ignorant le préfixe `57`.

Pour faire correspondre la lettre `C` ou `D` à un préfixe et ne pas l’utiliser
comme un suffixe, utilisez une exclusion vide `()`.

Example

`21D\()`

Cette formule correspond aux comptes dont le code commence par `21D`, quel que
soit le signe de leur solde.

In addition to using code prefixes to include accounts, you can also match
them with **account tags**. This is especially useful, for example, if your
country lacks a standardized chart of accounts, where the same prefix might be
used for different purposes across companies.

Example

`tag(25)`

This formula matches accounts whose associated tags contain the one with id
_25_.

If the tag you reference is defined in a data file, an xmlid can be used
instead of the id.

Example

`tag(my_module.my_tag)`

This formula matches accounts whose associated tags include the tag denoted by
_my_module.my_tag_.

You can also use arithmetic expressions with tags, possibly combining them
with prefix selections.

Example

`tag(my_module.my_tag) + tag(42) + 10`

The balances of accounts tagged as _my_module.my_tag_ will be summed with
those of accounts linked to the tag with ID _42_ and accounts with the code
prefix `10`

`C` and `D` suffixes can be used in the same way with tags.

Example

`tag(my_module.my_tag)C`

This formula matches accounts with the tag _my_module.my_tag_ and a credit
balance.

Prefix exclusion also works with tags.

Example

`tag(my_module.my_tag)\(10)`

This formula matches accounts with the tag _my_module.my_tag_ and a code not
starting with `10`.

### Moteur “Valeur externe”

Le moteur “valeur externe” est utilisé pour faire référence aux **valeurs
manuelles** et aux **valeurs reportées**. Ces valeurs ne sont pas stockées
avec `account.move.line`, mais avec `account.report.external.value`. Chacun de
ces objets pointe directement vers l’expression qu’il affecte, de sorte qu’il
n’y a pas grand-chose à faire concernant leur sélection ici.

Les **formules** peuvent être l’une des suivantes :

`sum`

    

Si le résultat doit être la somme de toutes les valeurs externes de la
période.

`most_recent`

    

Si le résultat doit être la valeur de la dernière valeur externe de la
période.

De plus, les **sous-formules** peuvent être utilisées de deux manières :

`rounding=X`

    

En remplaçant `X` par un nombre, on demande d’arrondir le montant à X
décimales.

`editable`

    

Indique que cette expression peut être éditée manuellement, ce qui déclenche
l’affichage d’une icône dans le rapport, permettant à l’utilisateur
d’effectuer cette action.

Note

Les valeurs manuelles sont créées à la `date_to` actuelle sélectionnée dans le
rapport.

Les deux sous-formules peuvent être utilisées ensemble en les séparant par un
`;`.

Example

`editable;rounding=2`

est une sous-formule correcte qui utilise les deux comportements.

### Moteur “Fonction Python personnalisée”

Ce moteur est un moyen pour les développeurs d’introduire des calculs
d’expressions personnalisés au cas par cas. La formule est le nom d’une
**fonction python** à appeler et la sous-formule est une **clé** à récupérer
dans le **dictionnaire** renvoyé par cette fonction. N’utilisez cette formule
que si vous construisez votre propre module personnalisé.

## Colonnes

Les rapports peuvent afficher un **nombre indéfini** de colonnes. Chaque
colonne obtient ses valeurs des **expressions** déclarées sur les **lignes**.
Le champ expression_label de la colonne donne le libellé des expressions dont
la valeur s’affiche. S’il y a aucune **expression** dans ce champ, rien n’est
affiché dans cette colonne. Si plusieurs colonnes sont requises, vous devez
utiliser des libellés d”**expression** différents.

![Colonnes du rapport.](../../../../_images/engine-columns.png)

Lorsque vous utilisez la fonctionnalité **comparaison de période** que vous
trouvez dans l’onglet Options d’un rapport comptable, toutes les colonnes sont
répétées dans et pour chaque période.

