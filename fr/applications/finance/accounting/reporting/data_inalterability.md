# Rapport de vérification de l’inaltérabilité des données

Les autorités fiscales de certains pays demandent aux sociétés de **prouver
que leurs écritures comptables enregistrées sont inaltérables** , ce qui
signifie que l’écriture, une fois comptabilisée, ne peut plus être modifiée.

Pour ce faire, Konvergo ERP peut utiliser l”**algorithme SHA-256** pour créer une
empreinte unique pour chaque écriture comptabilisée. Cette empreinte est
appelée un hachage. Le hachage est généré en prenant les données essentielles
d’une écriture (les valeurs des champs `date`, `journal_id`, `company_id`,
`debit`, `credit`, `account_id`, et `partner_id`), en les concaténant et en
les saisissant dans la fonction de hachage SHA-256, qui produit alors une
chaîne de caractères de taille fixe (256 bits). La fonction de hachage est
déterministe (la même entrée produit toujours le même résultat) : toute
modification mineure des données d’origine changerait complètement le hachage
obtenu. Par conséquent, l’algorithme SHA-256 est souvent utilisé, entre
autres, à des fins de vérification de l’intégrité des données.

De plus, le hachage de l’écriture précédente est toujours ajouté à l’écriture
suivante pour former une **chaîne de hachage**. Cela permet de s’assurer
qu’une nouvelle écriture n’est pas ajoutée après coup entre deux écritures
comptabilisées, car cela briserait la chaîne de hachage.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les hachages générés par l’algorithme SHA-256 ne sont théoriquement pas uniques, car il existe un nombre fini de valeurs possibles. Toutefois, ce nombre est exceptionnellement élevé : 2²⁵⁶, ce qui est beaucoup plus grand que le nombre d’atomes dans l’univers connu. C’est la raison pour laquelle les hachages sont considérés comme uniques dans la pratique.</p>
</div>

## Verrouiller les écritures comptabilisées avec hachage

Pour commencer à utiliser la fonction de hachage, allez à Comptabilité ‣
Configuration > Journaux. Ouvrez le journal pour lequel vous souhaitez activer
la fonctionnalité, allez à l’onglet **Paramètres avancés** et activez
**Verrouiller les écritures comptabilisées avec hachage**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Une fois que vous enregistrer une écriture sur un journal verrouillé, vous ne pouvez plus désactiver la fonctionnalité ou modifier une écriture comptabilisée.</p>
</div>

## Télécharger le rapport

Pour télécharger le rapport de vérification de l’inaltérabilité des données,
allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Analyse et cliquez sur
**Télécharger le rapport de vérification de l’inaltérabilité des données**.

La première section du rapport est une vue d’ensemble de tous vos journaux et
leur configuration. Dans la colonne Contrôle d’inaltérabilité, vous pouvez
voir si les écritures comptables comptabilisées sont verrouillées avec un
hachage (V) ou non (X). La colonne Couverture vous indique quand les écritures
comptabilisées ont commencé à être verrouillées.

![Configuration du rapport pour deux journaux](../../../../_images/journal-
overview.png)

La deuxième section présente le résultat du contrôle de cohérence des données
pour chaque journal haché. Vous pouvez visualiser la première écriture hachée
et le hachage correspondant et la dernière écriture hachée et le hachage
correspondant.

![Rapport de contrôle de cohérence des données pour un
journal](../../../../_images/data-consistency-check.png)

