# Email Marketing

Les emails sont une forme de communication efficace et entièrement
personnalisable qui permet d’atteindre n’importe quel public cible, qu’il soit
grand ou petit. Le succès d’un email est facilement mesurable, en particulier
lorsqu’un appel à l’action créatif est impliqué.

Odoo _Email Marketing_ fournit des outils de conception d’emails, de modèles
et de fonctionnalités de qualité professionnelle, conçus pour simplifier le
processus autrement complexe nécessaire à la création d’emails attrayants, à
l’élaboration de campagnes réussies et au suivi de leur efficacité globale
dans une seule et même application.

Pour plus d'infos

  * [Listes de diffusion](email_marketing/mailing_lists.html)

  * [Gérer les désabonnements (liste noire)](email_marketing/unsubscriptions.html)

## Tableau de bord d’Email Marketing

Pour commencer, cliquez sur l’icône de l’application Email Marketing, située
dans le tableau de bord principal d’Odoo. Cela vous mène au tableau de bord
principal d”Email Marketing (dans la vue kanban par défaut).

Pour voir tous les mailings dans la base de données, supprimez le filtre Mes
mailings de la barre de recherche.

![Vue du tableau de bord principal de l'application Email Marketing
d'Odoo.](../../_images/dashboard1.png)

Note

Le filtre Mes mailings est présent par défaut dans la barre de recherche. Cela
signifie que les seules informations visibles (à ce moment-là) sur le tableau
de bord d”Email Marketing sont les emails que l’utilisateur actuel a créés,
envoyés ou dont il est responsable.

Vous pouvez supprimer ce filtre en cliquant sur le X à côté de Mes mailings
dans la barre de recherche. Ceci permet d’afficher toutes les informations
relatives à chaque email de la base de données.

### Vue et étapes kanban par défaut

Les quatre colonnes kanban représentent les différentes étapes des emails qui
ont été créés ou envoyés avec l’application _Email Marketing_.

Les étapes sont : Brouillon, Dans la file d’attente, En cours d’envoi et
Envoyé.

  * Brouillon : signifie que l’email est encore en cours de rédaction/création.

  * Dans la file d’attente : signifie que l’email est planifié et envoyé à une date ultérieure.

  * En cours d’envoi : signifie que l’email est en cours d’envoi à ses destinataires.

  * Envoyé : signifie que l’email a déjà été envoyé à ses destinataires.

À chaque étape, les cartes à glisser-déposer représentent les campagnes
d’email qui ont été créées, et l’étape à laquelle elles se trouvent représente
le statut actuel de l’envoi.

Chaque bloc de mailing sur le tableau de bord de l”Email Marketing fournit des
informations essentielles relatives à cet email spécifique.

Lorsque le curseur survole le coin supérieur droit d’une carte de campagne
d’email, trois points verticaux (⋮) apparaissent. Lorsque vous cliquez dessus,
un mini menu déroulant propose de donner un code couleur à l’email, de
Supprimer l’email ou d”Archiver l’email pour éventuellement l’utiliser plus
tard.

![Vue du menu déroulant à trois points sur le tableau de bord d'Email
Marketing d'Odoo.](../../_images/three-dot-dropdown.png)

Dans le coin supérieur droit du tableau de bord principal d”Email Marketing,
d’autres options d’affichage sont disponibles : Liste et Graphique.

### Vue liste

La vue Liste (représentée par l’icône ☰ (trois lignes verticales)) fournit les
mêmes informations essentielles, mais dans un format de liste classique.

![Comment la vue Liste apparaît dans l'application Email Marketing
d'Odoo.](../../_images/list-view1.png)

### Vue graphique

La vue Graphique (représentée par l’icône 📊 (graphique à barres)) fournit les
mêmes informations essentielles, mais dans une variété de mises en page de
graphiques (et diagrammes) personnalisables.

![Comment la vue Graphique apparaît dans l'application Email Marketing
d'Odoo.](../../_images/graph-view.png)

Dans le coin supérieur gauche, il y a un menu Mesures, qui offre encore plus
d’options de filtrage pour personnaliser davantage les vues graphiques.

Ces options de Mesure sont : Pourcentage du test A/B, Couleur, et Comptage
(option sélectionnée par défaut).

### Options de recherche Filtres, Regrouper par et Favoris

Indépendamment de la vue choisie pour le tableau de bord Email Marketing, les
options Filtres, Regrouper par et Favoris sont toujours disponibles.

Ces options permettent de détailler et d’organiser les informations visibles
sur le tableau de bord Email Marketing de plusieurs façons.

FiltersGroup ByFavorites

Ce menu déroulant propose différentes façons de filtrer les campagnes d’email
sur le tableau de bord. Les options sont : Mes mailings, Date d’envoi, Archivé
et Ajouter un filtre personnalisé. Si vous sélectionnez l’option Ajouter un
filtre personnalisé, Odoo affiche un menu déroulant supplémentaire, avec trois
champs personnalisables à remplir, afin d’obtenir des résultats qui
correspondent à des critères plus spécifiques.

![Vue des options du menu déroulant des filtres du tableau de bord Email
Marketing d'Odoo.](../../_images/filters-dropdown.png)

Ce menu déroulant propose différentes façons d’organiser les données du
tableau de bord en les regroupant de manière spécifique. Il permet de
regrouper les données en fonction du Statut des messages ou de leur
Expéditeur.

Vous pouvez également regrouper les données par Période d’envoi, qui dispose
de son propre sous-menu d’options. Les options de Période d’envoi sont Année,
Trimestre, Mois, Semaine, et Jour.

Si aucune des options de Regrouper par ne permet d’obtenir les résultats
souhaités, cliquez sur Ajouter un groupe personnalisé en bas du menu
déroulant. Cette opération fait apparaître un nouveau champ dans lequel des
critères personnalisés peuvent être sélectionnés et appliqués, ce qui permet
de regrouper les données souhaitées.

![Vue du menu déroulant Regrouper par de l'application Email Marketing
d'Odoo.](../../_images/group-by-dropdown.png)

Ce menu déroulant propose différentes façons d’incorporer les filtres de
recherche antérieurs et d’autres options liées aux enregistrements pour
personnaliser le tableau de bord. Les options sont les suivantes : Enregistrer
la recherche actuelle, Importer des enregistrements, Ajouter à mon tableau de
bord, et Ajouter à Google Feuilles de calcul.

![Vue du menu déroulant Favoris de l'application Email Marketing
d'Odoo.](../../_images/favorites-dropdown.png)

## Paramètres

Pour afficher (et modifier) les paramètres d” _Email Marketing_ , allez à
l’application Email Marketing ‣ Configuration ‣ Paramètres.

![Vue de la page des paramètres de l'application Email Marketing
d'Odoo.](../../_images/settings-page.png)

Trois fonctionnalités sont disponibles dans les Paramètres : Campagnes
d’emails, Option de liste noire lors du désabonnement, et Serveur dédié.

  * Campagnes d’emails : permet de gérer des campagnes d’email marketing.

  * Option de liste noire lors du désabonnement : permet aux destinataires de s’inscrire sur une liste noire pour ne plus recevoir d’envois lors de la procédure de désabonnement.

  * Serveur dédié : permet d’utiliser un serveur séparé et dédié pour les mailings. Si cette option est activée, Odoo affiche un nouveau champ (et lien), dans lequel les configurations spécifiques du serveur doivent être saisies, afin qu’il se connecte correctement à Odoo.

## Créer un email

Pour créer un email, ouvrez l’application Email Marketing et cliquez sur le
bouton Créer dans le coin supérieur gauche.

En cliquant sur Créer, un formulaire détaillé d’email vierge s’affiche.

![Vue d'un formulaire détaillé d'email vierge dans l'application Email
Marketing d'Odoo.](../../_images/blank-email-detail-form.png)

Précisez d’abord le Sujet de l’email. Le Sujet est visible dans la boîte de
réception du destinataire, ce qui lui permet de voir rapidement de quoi il
s’agit.

Note

Le champ Sujet est obligatoire. Vous ne pouvez pas envoyer un email sans avoir
rempli le Sujet.

Astuce

L’icône ☺ (smiley) au bout du champ Sujet (et du champ Texte de
prévisualisation) représente les émojis. Cliquez sur cette icône ☺ (smiley)
pour afficher un menu d’émojis qui peuvent être utilisés dans l’un ou l’autre
champ.

Ensuite, vous avez la possibilité de saisir un Texte de prévisualisation. Ce
texte est une phrase de prévisualisation accrocheuse qui encourage les
destinataires à ouvrir le message. Dans la plupart des boîtes de réception, il
s’affiche à côté du sujet.

Astuce

Laissez le Texte de prévisualisation vide pour plutôt afficher les premiers
caractères du contenu de l’email.

### Destinataires

Vous devez ensuite choisir les destinataires de l’email, que vous pouvez
compléter dans le champ Destinataires.

![Vue du menu déroulant des destinataires dans l'application Email Marketing
d'Odoo.](../../_images/recipients-dropdown.png)

L’option par défaut est Liste de diffusion. Si l’option Liste de diffusion est
sélectionné, vous devez choisir une Liste de diffusion spécifique dans le menu
déroulant Sélectionner une liste de diffusion qui se trouve à côté.

Odoo n’enverra alors cet email qu’aux contacts de cette liste de diffusion
spécifique.

Pour plus d'infos

[Listes de diffusion](email_marketing/mailing_lists.html)

En cliquant sur le champ Destinataires, un menu déroulant proposant d’autres
options s’affiche. Chaque option propose différentes façons pour Odoo de créer
une audience cible pour l’email.

Ces options (à l’exception de l’option par défaut Liste de diffusion)
permettent de créer un filtre de destinataires plus spécifique, sous la forme
d’une équation.

Les options du champ Destinataires sont les suivantes :

  * Candidat : filtre ciblant des candidats spécifiques de la base de données.

  * Contact : filtre ciblant des contacts spécifiques de la base de données.

  * Inscription à l’événement : filtre ciblant les personnes de la base de données qui se sont inscrites à un événement.

  * Session d’événement : filtre ciblant les personnes de la base de données qui ont donné une présentation spécifique (session) lors d’un événement.

  * Piste/Opportunité : filtre ciblant les pistes ou les opportunités de la base de données.

  * Contact de la liste de diffusion : filtre ciblant des contacts spécifiques d’une liste de diffusion de la base de données.

  * Bon de commande : filtre ciblant un bon de commande spécifique de la base de données.

Si les champs de destinataires spécifiques ne s’affichent pas automatiquement,
cliquez simplement sur le bouton Ajouter un filtre en-dessous du champ
Destinataires et Odoo affiche les champs d’équation nécessaires pour affiner
les destinataires cibles de ce mailing.

### Ajouter un filtre de destinataires

Pour ajouter un filtre de destinataires plus spécifiques, sélectionnez
n’importe quelle option de destinataire (sauf Liste de diffusion) et cliquez
sur Ajouter un filtre, le cas échéant, pour afficher trois champs formatés
comme une équation.

Pour faire apparaître les options de sous-menu, cliquez sur chaque champ et
effectuez les sélections souhaitées, jusqu’à ce que vous ayez obtenu la
configuration souhaitée. Le nombre d”Enregistrements correspondant aux règles
est indiqué en vert à droite du champ Destinataires.

![Vue de la façon dont les filtres de destinataires peuvent être personnalisés
dans Odoo Email Marketing.](../../_images/add-filter-button.png)

Note

Certaines options de sous-menu dans le premier champ de règle permettent un
deuxième choix pour fournir encore plus de spécificité.

À droite de chaque règle se trouvent les icônes × (Supprimer le nœud), ＋
(Ajouter un nœud), et ⋯ (Ajouter une branche).

L’icône × (Supprimer le nœud) permet de supprimer un nœud (ligne) spécifique
de la règle. L’icône ＋ (Ajouter un nœud) permet d’ajouter un nœud (ligne) à la
règle et l’icône ⋯ (Ajouter une branche) permet d’ajouter une branche au nœud.
Une branche signifie que deux sous-nœuds supplémentaires, en retrait, sont
ajoutés à la règle, permettant de préciser davantage la ligne qui la précède.

### Onglet Corps de l’email

Au bas du formulaire d’email se trouvent deux onglets : Corps de l’email et
Paramètres. Concentrons-nous d’abord sur l’onglet Corps de l’email.

Dans l’onglet Corps de l’email, vous pouvez choisir parmi un certain nombre
d’emails préconfigurés. Sélectionnez le modèle souhaité et modifiez chaque
élément de son design avec les blocs de construction d’Odoo, situés dans la
barre latérale droite. Chaque bloc de construction offre des caractéristiques
uniques et des éléments de design professionnels.

![Vue des blocs de construction utilisés pour créer des emails dans
l'application Email Marketing d'Odoo.](../../_images/mail-blocks.png)

Astuce

Pour créer un email à partir de zéro, sélectionnez le modèle Texte simple et
Odoo fournit un canevas vierge qui vous pouvez personnaliser de plusieurs
façons - soit en utilisant l’éditeur de texte enrichi qui accepte les
commandes slash (/), soit en utilisant l’éditeur de code XML lorsque le [Mode
développeur (mode débug)](../general/developer_mode.html#developer-mode) est
activé et que l’on clique sur l’icône </>.

### Onglet Paramètres

L’onglet Paramètres se trouve à droite de l’onglet Corps de l’email.

Note

Les options disponibles dans l’onglet Paramètres, selon que la fonctionnalité
Campagnes d’emails est activée sur la page des Paramètres de l’application
Email Marketing (Email Marketing ‣ Configuration ‣ Paramètres).

Si la fonctionnalité Campagnes d’emails n’est pas activée, l’onglet Paramètres
du formulaire détaillé de l’email ressemble à ceci :

![Vue de l'onglet des paramètres de l’application Email Marketing sans les
paramètres activés.](../../_images/settings-without-features.png)

  * Responsable : choisissez un employé (dans la base de données) qui sera responsable pour ce mailing en particulier.

  * Adresse d’envoi : désigne un alias d’email qui s’affichera en tant qu’expéditeur de ce mailing en particulier.

  * Adresse de réponse : désigne un alias d’email auquel seront envoyées toutes les réponses à ce mailing en particulier.

  * Pièces jointes : si des documents spécifiques sont nécessaire (ou utiles) pour cette invitation, ils peuvent être envoyés avec ce mailing, en cliquant sur JOINDRE UN FICHIER et en ajoutant le(s) document(s) approprié(s).

Lorsque la fonctionnalité Campagnes d’emails _est_ activée, d’autres options
Marketing s’affichent dans l’onglet Paramètres, qui ressemble à ceci :

![Vue de l'onglet paramètres dans Odoo Email Marketing lorsque les paramètres
sont activés.](../../_images/settings-tab-with-settings.png)

Les fonctionnalités supplémentaires sont les suivantes : Campagne d’email,
Autoriser les tests A/B et Pourcentage de test A/B.

## Campagnes d’emails

Le champ Campagne d’email permet d’ajouter cet email en particulier à une
campagne d’email déjà réalisée dans la base de données. Cliquez sur le champ
vide pour afficher un menu déroulant contenant toutes les campagnes d’emails
créées précédemment dans la base de données.

![Vue d'un menu déroulant de campagne d'email dans l'application Email
Marketing d'Odoo.](../../_images/mailing-campaign-dropdown.png)

Si la campagne souhaitée ne figure pas dans le menu déroulant initial, cliquez
sur Recherche avancée pour afficher la liste exhaustive de toutes les
campagnes d’emails de la base de données. Vous pouvez également saisir le nom
de la campagne d’email souhaitée dans le champ Campagne d’email jusqu’à ce
qu’Odoo affiche la campagne souhaitée dans le menu déroulant. Sélectionnez
ensuite la campagne souhaitée.

### Créer une nouvelle campagne d’email (à partir de l’onglet Paramètres)

Pour créer une nouvelle campagne à partir de ce champ Campagne d’email,
commencez par taper le nom de cette nouvelle campagne et sélectionnez Créer
[Nom de la campagne] ou Créer et Modifier….

Cliquez sur Créer pour ajouter cette nouvelle campagne d’email à la base de
données et modifier ses paramètres ultérieurement. Et cliquez sur Créer et
Modifier… pour ajouter cette nouvelle campagne d’email à la base de données et
Odoo affiche une fenêtre contextuelle.

![Vue de la fenêtre contextuelle d'une campagne d'email dans l'application
Email Marketing d'Odoo.](../../_images/mailing-campaign-popup.png)

Vous pouvez personnaliser davantage la nouvelle campagne d’email. Modifiez le
Nom de la campagne, assignez un Responsable et ajoutez des Étiquettes.

La ligne supérieure de la fenêtre contextuelle Créer : Campagne d’email est
remplie de boutons intelligents analytiques. Chacun d’entre eux affiche
diverses mesures liées à la campagne. Lorsque l’on clique dessus, Odoo affiche
une page séparée, plus détaillée, avec des statistiques encore plus
approfondies.

L’option permettant d’envoyer immédiatement une nouvelle communication à
partir de cette fenêtre contextuelle est disponible dans le coin supérieur
gauche. La barre de statut ajustable se situe dans le coin supérieur droit.

Lorsque vous avez terminé toutes les modifications, cliquez sur Enregistrer.
Pour supprimer l’ensemble de la campagne, cliquez sur Ignorer.

### Créer une nouvelle campagne d’email (à partir de la page Campagnes)

Lorsque la fonctionnalité Campagnes d’emails est activée, une nouvelle option
Campagnes apparaît dans l’en-tête de l’application _Email Marketing_. Les
campagnes peuvent également être créées sur cette page Campagnes de
l’application _Email Marketing_.

Pour ce faire, allez à l’application Email Marketing ‣ Campagnes ‣ Créer. Une
fenêtre contextuelle s’affiche alors, dans laquelle vous pouvez directement
ajouter le Nom de la campagne, le Responsable et les Étiquettes sur le tableau
de bord des Campagnes.

![Vue de la fenêtre contextuelle de campagne dans Odoo Email
Marketing.](../../_images/campaigns-page-popup.png)

Cliquez sur Ajouter pour ajouter la campagne à la base de données et la
modifier ultérieurement. Ou bien, cliquez sur Modifier et Odoo ouvre le
formulaire du modèle de campagne dans une page séparée, offrant la possibilité
de modifier la campagne, d’envoyer des communications liées à la campagne et
d’analyser diverses mesures liées à la campagne, via les boutons intelligents
situés en haut du formulaire.

## Tests A/B

Dans l’onglet Paramètres du mailing, si la case Autoriser les tests A/B est
cochée, les destinataires ne reçoivent qu’un seul email. Cela permet d’envoyer
plusieurs emails à des destinataires sélectionnés de manière aléatoire, de
tester l’efficacité globale du mailing et d’éliminer la nécessité d’envoyer
des emails en double.

Le champ Pourcentage de test A/B représente le pourcentage de contacts de la
base de données auxquels cet email sera envoyé, dans le cadre du Test A/B.
Saisissez un nombre entre `1-100`. Les destinataires sont choisis au hasard.

## Envoyer, planifier ou tester

Après avoir finalisé le mailing, Odoo propose les options suivantes dans le
coin supérieur gauche du modèle d’email. Ces options sont les suivantes :
Envoyer, Planifier, et Tester.

En mode Édition, vous avez également des boutons permettant également
d”Enregistrer ou d”Ignorer le mailing.

  * Envoyer \- Cliquez sur ce bouton pour qu’Odoo envoie l’email aux destinataires souhaités. Lorsqu’Odoo a envoyé le mailing, le statut devient _Envoyé_.

  * Planifier \- Cliquez sur ce bouton pour faire apparaître une fenêtre contextuelle dans laquelle vous pouvez choisir la date et l’heure. Odoo envoie l’email aux destinataires choisis à cette date et heure. Lorsqu’une date et une heure sont choisies, le statut du mailing devient _Dans la file d’attente_.

  * Tester \- Cliquez sur ce bouton pour faire apparaître une fenêtre contextuelle dans laquelle Odoo vous permet d’envoyer un exemple d’email à des fins de test. Saisissez l’adresse email du destinataire souhaité dans le champ Destinataires et cliquez sur Envoyer un exemple d’email.

  * Enregistrer \- Cliquez sur ce bouton pour enregistrer le mailing en tant que brouillon, qui peut être modifié (et envoyé) à une date ultérieure. En cliquant sur ce bouton, le statut du mailing reste Brouillon.

  * Ignorer \- Cliquez sur ce bouton pour ignorer toute modification effectuée depuis le dernier enregistrement.

Astuce

Lorsque vous cliquez sur Enregistrer ou Ignorer (en mode Édition), ces options
sont remplacées par un bouton Modifier et un bouton Créer. Cliquez sur
Modifier pour revenir au mode Édition. Cliquez sur Créer pour commencer à
créer un nouveau mailing.

Note

Par défaut, une limite journalière est appliquée à **tous les emails** envoyés
dans _toutes_ les applications. Par conséquent, s’il reste des emails à
envoyer après avoir atteint la limite, ces emails _ne seront pas_ envoyés
automatiquement le jour suivant. Il faut forcer l’envoi en ouvrant l’email et
en cliquant sur Réessayer.

  * [Listes de diffusion](email_marketing/mailing_lists.html)
  * [Gérer les désabonnements (liste noire)](email_marketing/unsubscriptions.html)

