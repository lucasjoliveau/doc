# Les essentiels de Sondages

Les entreprises utilisent souvent des sondages pour recueillir des
informations précieuses auprès de leurs clients et employés, ce qui leur
permet de prendre des décisions commerciales plus éclairées.

Dans Konvergo ERP, les sondages sont utilisés pour recueillir les retours des clients,
évaluer le succès d’un événement récent, mesurer la satisfaction des clients
(ou des employés) et obtenir plus d’informations sur les sentiments changeants
du marché.

## Commencer

Pour démarrer, ouvrez l’application **Sondages** et cliquez sur **Créer**.
Konvergo ERP redirige ensuite la page vers un formulaire de modèle de sondage vierge.

Sur le formulaire du sondage, ajoutez un **Titre du sondage** et ajoutez une
image de couverture au sondage en survolant l’icône photo et en cliquant sur
**Modifier (crayon)**. Lorsque la fenêtre de l’explorateur de fichiers
s’ouvre, choisissez une image dans vos fichiers.

Sous le **Titre du sondage** se trouvent plusieurs onglets dans lesquels les
questions et le format du sondage peuvent être créés et personnalisés. Ces
onglets sont libellés comme suit :

  * **Questions** : la liste des questions à poser dans le sondage

  * **Description** : informations contextuelles pour faciliter la compréhension du sondage

  * **Options** : choix des réponses aux questions pour les personnes interrogées

![Divers onglets qui peuvent être trouvés sur la page du modèle de
sondage.](../../../_images/questions-description-options.png)

## Onglet Questions

Ajoutez des questions et des sections au sondage dans l’onglet **Questions**.
Une section divise le sondage en plusieurs parties afin de regrouper
visuellement des questions similaires. Pour créer une section, cliquez sur
**Ajouter une section** et saisissez un nom de section. Ensuite, ajoutez des
questions ou glissez et déposez des questions dans les sections séparées.

Le fait de cliquer sur **Ajouter une question** ouvre la fenêtre contextuelle
**Créer sections et questions** et vous permet de personnaliser la question du
sondage.

![La fenêtre contextuelle d'une question du sondage.](../../../_images/survey-
question-pop-up.png)

### Créer des questions

Dans la fenêtre contextuelle **Créer sections et questions** , saisissez la
question dans le champ **Question**. Choisissez ensuite le **Type de
question**. Un aperçu du type de question s’affiche dans la fenêtre d’aperçu.

Choisissez parmi les **Types de questions** suivants :

  * **Zone de texte à lignes multiples**

  * **Zone de texte à ligne unique**

  * **Valeur numérique**

  * **Date**

  * **Datetime**

  * **Choix multiple : une seule réponse**

  * **Choix multiple : plusieurs réponses possibles**

  * **Matrice**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les onglets <b>Réponses</b> et <b>Options</b> proposent des fonctionnalités différentes en fonction du <b>Type de question</b>. Toutefois, l’onglet <b>Description</b> reste inchangé, quelle que soit la question choisie.</p>
</div>

#### Créer des sections et des questions

Une fois un **Type de question** sélectionné, il existe trois onglets
permettant de personnaliser des informations relatives à la question. Il
s’agit des onglets **Réponses** (le cas échéant), **Description** et
**Options**.

Chaque onglet offre une variété de fonctionnalités différentes en fonction du
**type de question** choisi.

Par exemple, dans l’onglet **Options** , vous trouverez les options suivantes
:

  * **Réponse obligatoire** : la question est obligatoire.

  * **Type de matrice** : pour les questions de type matrice, sélectionnez si un choix ou des choix multiples peuvent être sélectionnés par ligne.

  * **Nombre de colonnes** : sélectionnez le nombre de colonnes qui seront affichées.

  * **Images sur les réponses** : permet d’afficher des images sur les options de réponse.

  * **Affichage conditionnel** : détermine si la question s’affiche en fonction de la réponse du participant à la question précédente.

  * **Afficher le champ Commentaires** : permet au participant de saisir un commentaire dans une zone de texte.

  * **Temps limite de la question** : pour les sondages en direct, définissez une limite de temps pour la question.

##### Affichage conditionnel

L”**Affichage conditionnel** signifie que la question ne s’affiche que si la
réponse conditionnelle définie a été sélectionnée dans une question
précédente.

Lorsque la case à côté d”**Affichage conditionnel** est cochée, le champ
**Question de déclenchement** apparaît. Sélectionnez une question du sondage.

Ensuite, un champ **Réponse de déclenchement** apparaît. Ici, sélectionnez la
réponse qui déclenchera la question d”**affichage conditionnel**.

## Onglet Options

De retour sur le formulaire principal du modèle de sondage, l’onglet
**Options** contient différentes sections de paramètres pouvant être modifiés.

Les sections sont les suivantes :

  * **Questions** : se concentre sur la présentation générale du sondage

  * **Notation** : détermine la manière dont le sondage est noté

  * **Participants** : gère l’accès au sondage

  * **Session en direct** : permet de transformer le sondage en une activité de groupe en temps réel

### Questions

Tout d’abord, déterminez l”**Agencement** du sondage. Les options suivantes
sont disponibles :

  * **Une page avec toutes les questions**

  * **Une page par section**

  * **Une page par question**

Si vous choisissez l’option **Une page par section** ou **Une page par
question** , l’option **Bouton de retour** apparaît. Si cette option est
sélectionnée, le **Bouton de retour** permet au participant de revenir à une
question précédente pendant le sondage.

Parmi les options d”**agencement** figure le paramètre **Mode de progression**
, qui indique comment s’affiche la progression du participant au cours du
sondage. Il s’agit d’un **Pourcentage** ou d’un **Nombre**.

Ensuite, une option permet d’ajouter une **Limite de temps du sondage**. Pour
mettre en œuvre cette option, il suffit de cocher la case et de saisir le
temps (en minutes) dont disposent les participants pour répondre au sondage.

Après l’option de **Limite de temps du sondage** , il y a une section
intitulée **Sélection**. Ici, les questions peuvent être **Aléatoires par
section**. En d’autres termes, le nombre de questions aléatoires peut être
configuré par section. Ce mode est ignoré lors d’une session en direct.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="time_random">Questions chronométrées et aléatoires</a></p>
</div>

### Notation

Les options suivantes sont disponibles lorsqu’il s’agit de déterminer une
méthode de **Notation** :

  * **Pas de notation**

  * **Notation avec réponses à la fin**

  * **Notation sans réponses à la fin**

Si vous sélectionnez **Notation avec réponses à la fin** ou **Notation sans
réponses à la fin** , le champ **% pour réussir** apparaît. Définissez le
pourcentage de réponses correctes nécessaires pour réussir le sondage.

Ensuite, vous avez la possibilité de transformer le sondage en certification.
Pour ce faire, cochez la case à côté de l’option intitulée **Est une
certification** et deux champs additionnels apparaissent. Sélectionnez un
thème de couleur dans le champ **Modèle de certification** et choisissez un
**Modèle d’email**. Lorsqu’un participant réussit la certification avec la
note requise, un email sera envoyé automatiquement depuis Konvergo ERP vers cette
personne en utilisant le modèle d’email sélectionné.

Si la fonctionnalité **Donner un badge** est activée et le **Badge de
certification** est défini, le participant au sondage reçoit également un
badge lorsqu’il réussit la certification.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="scoring">Noter les sondages</a></p>
</div>

### Participants

Pour déterminer l’accès au sondage, le **Mode d’accès** propose deux options :
**Toute personne disposant du lien** et **Seulement les personnes invitées**.

Sous la case à cocher **Responsables de l’évaluation uniquement** se trouve
l’option **Connexion requise** qui permet d’exiger que le participant se
connecte pour répondre au sondage. Si cette option est activée, un champ
**Limiter les tentatives** s’affiche également, dans lequel est défini le
nombre de tentatives dont le participant dispose.

### Session en direct

La section **Session en direct** est dédiée aux utilisateurs qui mènent des
sondages en temps réel, pendant lesquels ils communiquent avec un public en
direct et recueillent ses réponses.

Vous pouvez également pesonnaliser le **Code de session** ; ce code est
nécessaire pour que les participants puissent accéder à la session en direct.
Récompensez les participants pour leurs réponses rapides en cochant la case
intitulée **Récompenser les réponses rapides**. En sélectionnant cette option,
les participants obtiendront plus de points s’ils répondent rapidement.

## Onglet Description

De retour sur la page principale du modèle de sondage, vous avez l’onglet
**Description** , où il est possible d’ajouter une description personnalisée.
Celle-ci s’affiche sous le titre de la page d’accueil du sondage, qui se
trouve sur le frontend du site web créé à l’aide de l’application **Site
Web**.

## Tester et partager le sondage

Une fois le sondage créé et enregistré, lancez un test pour trouver les
éventuelles erreurs avant de l’envoyer aux participants en cliquant sur
**Test** dans le coin supérieur gauche de la page du modèle de sondage.

Ensuite, Konvergo ERP redirige la page vers une version test du sondage sur le
frontend du site web. Vous pouvez y voir le sondage comme un participant
normal. Parcourez le sondage à la recherche d’erreurs.

Pour retourner au formulaire du modèle de sondage dans le backend, cliquez
simplement sur le lien **Ceci est un sondage test. Modifier le sondage** dans
la bannière bleue en haut de la page. Konvergo ERP redirige ensuite vers le modèle de
sondage dans le backend, effectuez les changements nécessaires avant d’envoyer
officiellement le sondage aux participants.

Lorsque le sondage est prêt à être partagé avec le public, cliquez sur le
bouton **Démarrer le sondage** dans le coin supérieur gauche du formulaire du
modèle de sondage. Cliquez ensuite sur **Partager**.

Dans la fenêtre contextuelle, ajoutez les destinataires du sondage dans le
champ **Destinataires** (pour les contacts qui existent dans la base de
données Konvergo ERP) ou le champ **Emails supplémentaires** (pour les contacts qui ne
veulent pas être listés dans la base de données Konvergo ERP). Enfin, cliquez sur
**Envoyer**.

Au fur et à mesure que les réponses sont reçues, affichez-les en cliquant sur
le bouton intelligent **Réponses** sur le formulaire du modèle de sondage ou
sur le bouton **Voir les résultats** dans le coin supérieur gauche. Pour
terminer le sondage, cliquez sur le bouton **Fermer** sur le formulaire du
modèle de sondage.

