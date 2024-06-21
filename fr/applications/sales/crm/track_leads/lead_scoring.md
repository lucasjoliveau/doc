# Assigner des pistes grâce à la notation prédictive des pistes

L’application _CRM_ d’Konvergo ERP peut automatiquement assigner des
pistes/opportunités aux équipes commerciales et vendeurs. Une pratique
courante consiste à assigner les pistes en fonction de la probabilité de
remporter chaque piste. Les entreprises peuvent donner la priorité aux pistes
qui ont le plus de chances de déboucher sur des affaires fructueuses en les
assignant rapidement aux vendeurs appropriés.

Konvergo ERP calcule automatiquement la probabilité de remporter chaque piste en
utilisant une méthode appelée _notation prédictive des pistes_.

## Notation prédictive des pistes

La notation prédictive des pistes est un modèle d’apprentissage automatique
qui utilise les données historiques de Konvergo ERP _CRM_ pour évaluer les
pistes/opportunités ouvertes.

Au fur et à mesure qu’une entreprise traite des opportunités dans le pipeline
CRM, Konvergo ERP recueille des données sur les opportunités gagnées et perdues. La
notation prédictive des pistes utilise ces données pour prédire la probabilité
de remporter chaque nouvelle piste ou opportunité.

Plus il y a d’opportunités envoyées à travers le pipeline CRM, plus Konvergo ERP
recueille de données, ce qui permet d’obtenir des probabilités plus précises.

Plus précisément, la notation prédictive des pistes d’Konvergo ERP utilise la
classification de probabilité _naïve bayésienne_ :

\\[\begin{equation} P(A | B) = \frac{P(A) \times P(B | A)}{P(B)} \end{equation}\\]

La probabilité de réussite de chaque opportunité est affichée sur le
formulaire de l’opportunité et elle se met à jour automatiquement au fur et à
mesure que l’opportunité progresse dans le pipeline CRM.

![La probabilité de réussite affichée sur le formulaire de
l'opportunité.](../../../../_images/probability-opportunity-form.png)

Lorsqu’une opportunité passe à l’étape suivante, sa probabilité de réussite
augmente automatiquement en fonction de l’algorithme de notation prédictive
des pistes.

### Configuration

La notation prédictive des pistes est toujours activée dans Konvergo ERP _CRM_.
Cependant, les variables utilisées pour calculer la probabilité de réussite
peuvent être personnalisés dans les paramètres.

Pour personnaliser les variables utilisées par la notation prédictive des
pistes, allez à CRM ‣ Configuration ‣ Paramètres. Sous **Notation prédictive
des pistes** , cliquez sur le bouton **Mettre à jour les probabilités**.

Ensuite, cliquez sur le menu déroulant pour choisir les variables qui seront
prises en compte par la notation prédictive des pistes.

![La fenêtre Mettre à jour les probabilités dans les paramètres de la Notation
prédictive des pistes.](../../../../_images/update-probabilities.png)

Chacune des variables suivantes peut être activée :

  * **État** : l’état géographique d’où provient l’opportunité

  * **Pays** : le pays géographique d’où provient l’opportunité

  * **Qualité du téléphone** : si un numéro de téléphone est indiqué pour l’opportunité

  * **Qualité de l’email** : si une adresse email est indiquée pour l’opportunité

  * **Source** : la source d’une opportunité (par ex. moteur de recherche, réseaux sociaux)

  * **Langue** : la langue parlée indiquée pour l’opportunité

  * **Étiquettes** : les étiquettes apposées sur l’opportunité

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les variables <code>Étape</code> et <code>Équipe</code> sont toujours actives. <code>Étape</code> fait référence à l’étape du pipeline CRM dans laquelle se trouve une opportunité. <code>Équipe</code> fait référence à l’équipe commerciale à laquelle est assignée l’opportunité. La notation prédictive des pistes prend <em>toujours</em> en compte ces deux variables, quelles que soient les variables optionnelles sélectionnées.</p>
</div>

Cliquez ensuite sur le champ de date à côté de l’option **Prendre en compte
les pistes créées à partir du :** pour sélectionner la date à partir de
laquelle la notation prédictive des pistes commencera à calculer.

Enfin, cliquez sur **Confirmer** pour enregistrer les changements.

### Modifier la probabilité manuellement

La probabilité de réussite d’une opportunité peut être modifiée manuellement
sur le formulaire de l’opportunité. Cliquez sur le chiffre de probabilité pour
la modifier.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>La modification manuelle de la probabilité supprime les mises à jour automatiques de la probabilité pour cette opportunité. La probabilité ne sera plus mise à jour automatiquement au fur et à mesure que l’opportunité franchit les différentes étapes du pipeline.</p>
</div>

Pour réactiver la probabilité automatique, cliquez sur l’icône d’engrenage à
côté du pourcentage de probabilité.

![L'icône d'engrenage utilisée pour réactiver la probabilité automatique sur
un formulaire d'opportunité.](../../../../_images/probability-gear-icon.png)

## Assigner des pistes d’après leur probabilité

Konvergo ERP _CRM_ peut assigner des pistes/opportunités aux équipes commerciales et
aux vendeurs en fonction de règles spécifiques. Créez des règles d’assignation
basées sur la probabilité de réussite des pistes afin de donner la priorité à
celles qui ont le plus de chances de réussir.

### Configurer l’assignation basée sur des règles

Pour activer l” _assignation basée sur des règles_ , allez à CRM ‣
Configuration ‣ Paramètres et activez l”**Assignation basée sur des règles**.

Il est possible de configurer la fonctionnalité d’assignation basée sur des
règles pour qu’elle s’exécute **Manuellement** , ce qui signifie qu’un
utilisateur d’Konvergo ERP doit lancer l’assignation manuellement ou **De façon
répétée** , ce qui signifie qu’Konvergo ERP déclenche automatiquement l’assignation en
fonction de la période sélectionnée.

Pour configurer l’assignation automatique des pistes, sélectionnez **De façon
répétée** pour la section **Exécution**. Ensuite, personnalisez la fréquence à
laquelle Konvergo ERP déclenchera l’assignation automatique dans la section **Répéter
tou(te)s les**.

![Le paramètre Assignation basée sur des règles dans les paramètres de
CRM.](../../../../_images/rule-based-assignment.png)

Si l’assignation basée sur des règles est configurée pour s’exécuter **de
façon répétée** , l’assignation peut toujours être déclenchée manuellement à
l’aide de l’icône de flèche circulaire dans les paramètres **Assignation basée
sur des règles** (ou à l’aide du bouton **Assigner des pistes** sur la page de
configuration de l’équipe commerciale).

### Configurer des règles d’assignation

Ensuite, configurez les _règles d’assignation_ pour chaque équipe commerciale
et/ou vendeur. Ces règles déterminent quelles pistes Konvergo ERP assigne à quelles
personnes. Pour démarrer, allez à CRM ‣ Configuration ‣ Équipes commerciales
et sélectionnez une équipe commerciale.

Sur le formulaire de configuration de l’équipe commerciale, sous **Règles
d’assignation** , cliquez sur **Modifier le domaine** pour configurer les
règles qu’Konvergo ERP utilise pour déterminer l’assignation des pistes pour cette
équipe commerciale. Ces règles peuvent inclure tout ce qui peut être pertinent
pour cette entreprise ou équipe et un nombre illimité de règles peut être
ajouté.

Cliquez sur **Ajouter un filtre** pour commencer à créer des règles
d’assignation. Cliquez sur le signe **+** à droite de la règle d’assignation
pour ajouter une autre ligne. Cliquez sur le symbole **x** pour supprimer la
ligne.

Pour créer une règle d’assignation basée sur la probabilité de réussite d’une
opportunité, cliquez sur le menu déroulant à l’extrême gauche d’une ligne de
règle d’assignation et sélectionnez **Probabilité**.

Dans le menu déroulant du milieu, sélectionnez le symbole d’équation
souhaité—le plus souvent le symbole correspondant à _plus grand que_ , _plus
petit que_ , _plus grand ou égal à_ , ou _plus petit ou égal à_.

Dans le champ situé à l’extrême droite, saisissez la valeur numérique
souhaitée pour la probabilité. Enfin, cliquez sur **Enregistrer** pour
enregistrer les modifications.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Pour configurer une règle d’assignation de manière à ce qu’une équipe commerciale reçoive les pistes avec une probabilité de réussite plus grande ou égale à 20%, créez une ligne de <b>Domaine</b> comme suit : <code>Probabilité &gt;= 20</code>.</p>
<img alt="Domaine d'équipe commerciale défini sur une probabilité plus grande ou égale à vingt pour cent." class="align-center" src="../../../../_images/probability-domain.png"/>
</div>

Des règles d’assignation séparées peuvent également être configurées pour
chaque membre de l’équipe. Depuis la page de configuration de l’équipe
commerciale, cliquez sur un membre de l’équipe dans l’onglet **Membres** et
modifiez la section **Domaine**. Cliquez sur **Enregistrer** pour enregistrer
les changements.

Si l’assignation automatique des pistes est configurée dans les paramètres,
l’équipe commerciale et chaque membre de l’équipe ont la possibilité
d”**Ignorer l’assignation automatique**. Cochez cette case pour éviter qu’une
équipe commerciale ou un vendeur ne se voie assigner des pistes
automatiquement par la fonctionnalité d’assignation basée sur des règles
d’Konvergo ERP. Si l’option **Ignorer l’assignation automatique** est activée,
l’équipe commerciale ou le vendeur peut toujours se voir assigner des pistes
manuellement.

Pour assigner manuellement des pistes à cette équipe commerciale, cliquez sur
le bouton **Assigner des pistes** en haut de la page de configuration de
l’équipe commerciale. Cette opération permet d’assigner des pistes qui n’ont
pas encore été assignées et qui correspondent au domaine spécifique de
l’équipe.

