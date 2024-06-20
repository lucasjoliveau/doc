# Forum

**Odoo Forum** est un forum de questions-réponses conçu pour aider les
clients. L’ajout d’un forum à un site web vous permet de construire une
communauté, d’encourager l’engagement et de partager des connaissances.

## Créer un forum

Pour créer ou éditer un forum, allez à Site Web ‣ Configuration ‣ Forum:
Forums. Cliquez sur Nouveau ou sélectionnez un forum existant et configurez
les éléments suivants.

Nom du forum : donnez un nom au forum.

Mode : sélectionnez Questions pour pouvoir marquer une réponse comme étant la
meilleure, ce qui signifie que les questions apparaissent comme _résolues_ ;
ou Discussions si cette fonctionnalité n’est pas nécessaire.

Note

Indépendamment du mode sélectionné, **une seule réponse** par utilisateur est
autorisée sur un seul post. Il est toutefois possible de commenter plusieurs
fois.

Tri par défaut : choisissez la manière dont les questions sont triées par
défaut.

>   * Le plus récent : selon la date de publication de la question la plus
> récente
>
>   * Dernière mise à jour : selon la dernière activité de publication
> (réponses et commentaires inclus)
>
>   * Le plus voté : selon le nombre de votes le plus élevé
>
>   * Pertinence : selon la pertinence du post (déterminée par une formule)
>
>   * Répondu : selon la probabilité de réponse (déterminée par une formule)
>
>

Note

Les utilisateurs disposent de plusieurs options de tri (nombre total de
réponses, nombre total de vues, dernière activité) sur la page d’accueil du
forum.

Confidentialité : sélectionnez Public pour que tout le monde puisse voir le
forum, Utilisateurs connectés pour le rendre visible uniquement pour les
utilisateurs connectés ou Certains utilisateurs pour le rendre visible
uniquement à un groupe d’accès d’utilisateurs spécifiques en sélectionnant un
Groupe autorisé.

Configurez ensuite les gains de karma et les droits liés au karma.

### Points de karma

Des points de karma peuvent être attribués aux utilisateurs en fonction de
leurs différentes interactions sur le forum. Ils peuvent être utilisés pour
déterminer les fonctionnalités du forum auxquelles les utilisateurs ont accès,
qu’il s’agisse de voter sur des posts ou d’avoir des droits de modérateur. Ils
sont également utilisés pour définir les rangs des utilisateurs.

Important

  * Les points de karma d’un utilisateur sont partagés entre tous les forums, cours, etc. d’un même site web d’Odoo.

  * Les utilisateurs d’eLearning peuvent gagner des points de karma en [interagissant avec différents cours](elearning.html#elearning-karma) et en [complétant des quiz](elearning.html#elearning-quiz).

#### Gains de karma

Plusieurs interactions sur le forum peuvent attribuer ou retirer des points de
karma.

Interaction | Description | Gain de karma par défaut  
---|---|---  
Poser une question | Vous publiez une question. | 2  
Question votée positivement | Un autre utilisateur vote pour une question que vous avez publiée. | 5  
Question votée négativement | Un autre utilisateur vote contre une question que vous avez publiée. | -2  
Réponse approuvée | Un autre utilisateur vote pour une réponse que vous avez publiée. | 10  
Réponse rejetée | Un autre utilisateur vote contre une réponse que vous avez publiée. | -2  
Valider une réponse | Vous marquez une réponse publiée par un autre utilisateur comme la meilleure. | 2  
Réponse validée | Un autre utilisateur marque une réponse que vous avez publiée comme la meilleure. | 15  
Réponse signalée | Une question ou une réponse que vous avez publiée est marquée comme insultante. | -100  
  
Note

Les nouveaux utilisateurs reçoivent **trois points** lors de la validation de
leur adresse email.

Pour modifier les valeurs par défaut, allez à Site Web ‣ Configuration ‣ Forum
: Forums, sélectionnez le forum et allez à l’onglet Gains de karma.
Sélectionnez une valeur pour la modifier.

Si la valeur est positive (par ex. `5`), le nombre de points sera ajouté au
score de l’utilisateur chaque fois que l’interaction a lieu sur le forum
sélectionné. Inversement, si la valeur est négative (par ex. `-5`), le nombre
de points sera déduit. Utilisez `0` si une interaction ne doit pas avoir
d’impact sur le score d’un utilisateur.

#### Droits liés au karma

Pour configurer le nombre de points requis pour accéder aux différentes
fonctionnalités du forum, allez à Site Web ‣ Configuration ‣ Forum : Forums,
sélectionnez le forum et allez à l’onglet Droits liés au karma. Sélectionnez
une valeur pour la modifier.

Avertissement

Certaines fonctionnalités, comme Modifier tous les posts, Fermer tous les
posts, Supprimer tous les posts, Modérer les posts, et Délier tous les
commentaires, sont assez sensibles. Assurez-vous de bien comprendre les
conséquences de donner accès à ces fonctionnalités à _tout_ utilisateur
atteignant le niveau de karma requis.

Fonctionnalité | Description | Karma requis par défaut  
---|---|---  
Poser des questions | Publier des questions. | 3  
Répondre aux questions | Publier des réponses aux questions. | 3  
Voter positivement | Voter pour des questions ou des réponses. | 5  
Voter négativement | Voter contre des questions ou des réponses. | 50  
Modifier ses propres posts | Modifier les questions ou les réponses que vous avez publiées. | 1  
Modifier tous les posts | Modifier n’importe quelle question ou réponse. | 300  
Fermer ses propres posts | Fermer les questions ou les réponses que vous avez publiées. | 100  
Fermer tous les posts | Fermer n’importe quelle question ou réponse. | 500  
Supprimer ses propres posts | Supprimer les questions ou les réponses que vous avez publiées. | 500  
Supprimer tous les posts | Supprimer n’importe quelle question ou réponse. | 1.000  
Liens nofollow | Si vous êtes en dessous du seuil de karma, un attribut _nofollow_ indique aux moteurs de recherche d’ignorer les liens que vous publiez. | 500  
Valider une réponse à ses propres questions | Marquer une réponse comme étant la meilleure sur les questions que vous avez publiées. | 20  
Valider une réponse à toutes les questions | Marquer une réponse comme étant la meilleure sur n’importe quelle question. | 500  
Fonctionnalités de l’éditeur : image et liens | Ajouter des liens et des images à vos posts. | 30  
Commenter vos propres posts | Publier des commentaires sur les questions ou les réponses que vous avez créées. | 1  
Commenter tous les posts | Publier des commentaires sous n’importe quelle question ou réponse. | 1  
Convertir vos propres réponses en commentaires et vice versa | Convertir les commentaires que vous avez publiés en réponses. | 50  
Convertir toutes les réponses en commentaires et vice versa | Convertir n’importe quel commentaire en réponse. | 500  
Délier vos propres commentaires | Supprimer les commentaires que vous avez publiés. | 50  
Délier tous les commentaires | Supprimer n’importe quel commentaire. | 500  
Poser des questions sans validation | Les questions que vous publiez ne doivent pas être validées avant. | 100  
Signaler un post comme insultant | Signaler une question ou une réponse comme insultante. | 500  
Modérer les posts | Accéder à tous les outils de modération. | 1.000  
Changer les étiquettes des questions | Changer les étiquettes des questions publiées (si vous avez le droit de les modifier). | 75  
Créer de nouvelles étiquettes | Créer de nouvelles étiquettes lors de la publication des questions. | 30  
Afficher la biographie détaillée de l’utilisateur | Lorsqu’un utilisateur survole votre avatar ou nom d’utilisateur, une fenêtre contextuelle affiche vos points de karma, votre biographie et le nombre de badges per niveau. | 750  
  
Astuce

Suivez toutes les activités liées au karma et ajoutez ou supprimez des points
de karma manuellement en [activant le mode
développeur](../general/developer_mode.html#developer-mode) et en allant aux
Paramètres ‣ Outils de ludification ‣ Suivi de karma.

### Ludification

Les rangs et les badges peuvent être utilisés pour encourager les visiteurs à
participer. Les rangs sont basés sur le nombre total de points de karma,
tandis que les badges peuvent être attribués manuellement ou automatiquement
en relevant des défis.

#### Rangs

Pour créer de nouveau rangs ou modifier les rangs par défaut, allez à Site Web
‣ Configuration ‣ Forum : Rangs et cliquez sur Nouveau ou sélectionnez un rang
existant.

Ajoutez le Nom du rang, les points de karma nécessaires pour l’atteindre, sa
Description, un message de Motivation pour encourager les utilisateurs à
l’atteindre et une image.

![Rangs par défaut du forum](../../_images/ranks.png)

#### Badges

Pour créer de nouveaux badges ou modifier les badges par défaut, allez à Site
Web ‣ Configuration ‣ Forum : Badges et cliquez sur Nouveau ou sélectionnez un
badge existant.

Saisissez le nom et la description du badge, ajoutez une image et configurez-
le.

##### Attribution manuelle

Si le badge doit être accordé manuellement, sélectionnez quels utilisateurs
peuvent les accorder en sélectionnant l’une des options d”Autorisation
d’attribution suivantes :

  * Tout le monde : tous les utilisateurs non portail (puisque les badges sont accordés depuis le backend).

  * Une sélection d’utilisateurs : les utilisateurs répertoriés sous Utilisateurs autorisés.

  * Personnes possédant certains badges : les utilisateurs ayant reçu les badges sélectionnés sous Badges requis.

Il est possible de limiter le nombre de fois par mois que chaque utilisateur
peut accorder le badge en activant la Limite mensuelle d’envoi et en
saisissant un Nombre limité.

##### Attribution automatique

Si le badge doit être accordé **automatiquement** lorsque certaines conditions
sont remplies, sélectionnez Personne, attribué par les défis sous Autorisation
d’attribution.

Ensuite, déterminez comment le badge doit être attribué en cliquant sur
Ajouter dans la section Récompenser les défis. Sélectionnez un défi à ajouter
ou créez-en un en cliquant sur Nouveau.

Astuce

Il est possible d’attribuer au badge un Niveau de votre badge forum (Bronze,
Argent, Or) pour lui donner plus ou moins d’importance.

![Badges par défaut du forum](../../_images/badges1.png)

### Étiquettes

Les utilisateurs peuvent utiliser des étiquettes pour filtrer les posts du
forum.

Pour gérer des étiquettes, allez à Site Web ‣ Configuration ‣ Forum :
Étiquettes. Cliquez sur Nouveau pour créer une étiquette et sélectionner le
Forum associé.

Astuce

  * Utilisez la section Étiquettes dans la barre latérale du forum pour filtrer toutes les questions attribuées à l’étiquette sélectionnée. Cliquez sur Tout afficher pour afficher toutes les étiquettes.

  * De nouvelles étiquettes peuvent être créées lors de la publication d’un nouveau message, à condition que l’utilisateur ait suffisamment de points de karma.

## Utiliser un forum

Note

L’accès à de nombreuses fonctionnalités dépend des points de karma d’un
utilisateur.

### Publier des questions

Pour créer un nouveau post, accéder à la page d’accueil du forum, cliquez sur
Nouveau post et complétez les éléments suivants :

  * Titre : ajoutez la question ou le sujet du post.

  * Description : ajoutez une description à la question.

  * Étiquettes : ajoutez jusqu’à cinq étiquettes.

Cliquez sur Poser votre question.

### Interagir avec les posts

Différentes actions sont possibles sur un post.

  * Marquer une question comme **favorite** en cliquant sur le bouton d’étoile (☆).

  * Suivre un post et obtenir des **notifications** (par email ou dans Odoo) lorsqu’il y est répondu en cliquant sur le bouton de cloche (🔔).

  * **Voter** _pour_ (flèche vers le haut ▲) ou _contre_ (flèche vers le bas ▼) une question ou une réponse.

  * Marquer une réponse comme étant la **meilleure** en cliquant sur la coche (✔). Cette option n’est disponible que si le Mode du forum est défini sur Questions.

  * Répondre à une question.

  * **Commenter** une question ou une réponse en cliquant sur le bouton de bulle (💬).

  * **Partager** une question sur Facebook, Twitter, ou LinkedIn en cliquant sur le bouton des _nœuds de partage_.

Cliquez sur le bouton d’ellipse (…) pour :

>   * Modifier une question ou une réponse.
>
>   * Fermer une question.
>
>   * Supprimer, répondre ou commenter une question. Il est possible d”Annuler
> la suppression des questions par la suite.
>
>   * Signaler une question ou une réponse comme insultante.
>
>   * Convertir un commentaire en réponse.
>
>   * Afficher le [ticket
> d’assistance](../services/helpdesk/overview/help_center.html#helpdesk-forum)
> associé, le cas échéant.
>
>

![Actions sur les posts](../../_images/post-actions.png)

Note

Par défaut, 150 points de karma sont nécessaires pour afficher le profil d’un
autre utilisateur. Cette valeur peut être configurée lors de la création d’un
nouveau site web.

## Modérer un forum

Sur la page d’accueil du forum, la barre latérale de la section Outils de
modération regroupe les fonctionnalités essentielles du modérateur.

![Barre latérale des outils de modération du forum](../../_images/moderation-
tools.png)

À valider : accéder à toutes les questions et réponses en attente de
validation avant d’être affichées aux utilisateurs non modérateurs.

![Question à valider](../../_images/to-validate.png)

Note

Une question est en attente si un utilisateur n’a pas le karma requis.
L’utilisateur n’est pas en mesure de publier des questions ou des réponses en
attendant la validation. Une seule question en attente par utilisateur est
autorisée par forum.

Signalé : accéder à toutes les questions et réponses qui ont été marquées
comme insultantes. Cliquez sur Accepter pour supprimer le drapeau insultant ou
sur Insultant pour le confirmer, puis sélectionnez une raison et cliquez sur
Marquer comme insultant. Le post est ensuite masqué aux utilisateurs sans
droits de modération et 100 points de karma sont déduits du score de
l’utilisateur fautif.

![Sélection du motif d'insulte](../../_images/offensive-reason.png)

Fermé : accéder à toutes les questions qui ont été fermées. Il est possible de
les Supprimer ou de les Rouvrir. Pour fermer une question, ouvrez-la, cliquez
sur le bouton d’ellipse (…), puis sur Fermer. Sélectionnez un Motif de
fermeture, et cliquez sur Fermer le post. Le post est ensuite masqué aux
utilisateurs sans droits de modération.

Note

Lorsque vous sélectionnez Spam ou publicité ou Contient des remarques
insultantes ou malveillantes comme motif, 100 points de karma sont déduits du
score de l’auteur du post.

Astuce

  * Créez et modifiez des motifs de fermeture en allant à Site Web ‣ Configuration ‣ Forum : Motifs de fermeture. Sélectionnez Basique comme Type de motif si le motif doit être utilisé lors de la fermeture d’une question et Insultant si elle doit être utilisée pour les posts signalés.

  * Gérez tous les posts en allant à Site Web ‣ Configuration ‣ Forum : Forums, en sélectionnant le forum et en cliquant sur le bouton intelligent Posts. En cliquant sur le bouton Actions, vous pouvez Exporter, Archiver, Désarchiver, ou Supprimer un ou plusieurs posts.

