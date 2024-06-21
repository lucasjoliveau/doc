# Les essentiels d’Événement

Konvergo ERP Événements fournit aux coordinateurs d’événements un arsenal d’outils de
planification, de communication et d’analyse pour créer des expériences
immersives et engageantes pour les clients. Le personnel peut notamment créer
et publier des événements sur leur site web, vendre des tickets en ligne,
scanner des tickets avec Konvergo ERP Code-barres, envoyer des emails automatisés et
générer des rapports riches en données une fois que l’événement accepte des
inscriptions.

## Concepts et organisation Kanban

Pour démarrer, cliquez sur l’application **Événements** sur le tableau de bord
d’accueil, ce qui mène ensuite à la vue kanban peuplée d’une variété d’étapes
du pipeline. Chaque carte reprend les informations principales d’un événement,
telles que la date/l’heure de l’événement, le nombre de participants attendus
(et confirmés)

Pour créer une nouvelle étape, cliquez sur **Ajouter une colonne** et donnez
un titre approprié pour illustrer l’objectif de cette étape.

Pour réorganiser les étapes, il suffit de les faire glisser jusqu’à ce
qu’elles se trouvent dans le bon ordre. Les étapes peuvent également être
“repliées” dans le kanban pour une présentation plus nette, via le menu
**Paramètres** à droite de chaque titre d’étape, représenté par une icône en
forme d’engrenage.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’icône d’engrenage est masquée par défaut et apparaît à côté de l’icône <b>+</b> lorsque vous passez la souris dessus.</p>
</div>

Lorsque vous cliquez dessus, un menu déroulant de paramètres apparaît.

![Aperçu des paramètres d'événement dans la vue kanban dans Konvergo ERP
Événements](../../../_images/events-dashboard.png)

## Créer un nouvel événement

Pour créer un événement, cliquez sur **Créer** depuis le tableau de bord
d’Événement. Konvergo ERP redirigera la page vers un formulaire de modèle d’événement
vierge.

Sur le formulaire de l’événement, complétez les champs nécessaires, soit en
choisissant parmi les données existantes dans la base de données Konvergo ERP ou en
créant et modifiant de nouvelles données de champ. Les informations clés à
saisir pour l’événement sont les suivantes :

  * **Nom de l’événement** : donnez un titre à l’événement.

  * **Date** : comprend les dates/heures de début et de fin de l’événement.

  * **Fuseau horaire** : couvre le fuseau horaire de l’événement.

  * **Modèle** : choisissez un modèle d’événement prédéfini ou créez un modèle personnalisé et sélectionnez-le ici.

  * **Étiquettes** : ajoutez des étiquettes pour indiquer brièvement la nature de l’événement (par ex. `salon professionnel`). Les étiquettes permettent de mieux organiser les cartes d’événement dans le kanban et sont utiles pour utiliser des filtres de recherche pendant les périodes d’analyse.

  * **Organisateur** : détail du ou des organisateurs de l’événement. Ce champ correspond généralement à la société qui possède la base de données Konvergo ERP ou à un fournisseur.

  * **Responsable** : la personne de contact responsable de l’organisation de l’événement.

  * **Site web** : indiquez sur quel(s) site(s) web d’Konvergo ERP l’événement doit être publié.

  * **Lieu** : indiquez les détails du lieu ici s’il s’agit d’un nouvel enregistrement, ou choisissez un lieu existant.

  * **Limiter les inscriptions** : si cette option est activée, les inscriptions sont limitées à un chiffre défini.

  * **Confirmation automatique** : si cette option est activée, l’email de confirmation envoyé aux personnes inscrites à l’événement est annulé et l’inscription est confirmée automatiquement.

Une fois les champs du formulaire de l’événement complétés, passez aux onglets
**Tickets** et **Communication** et, si nécessaire, l’onglet **Questions** si
les inscriptions nécessitent des informations supplémentaires.

### Ajouter et vendre des tickets d’événement

Sous l’onglet **Tickets** , ajoutez des lignes pour chaque type de ticket que
l’événement prévoit d’offrir. Déterminez ici le prix du ticket, les dates de
début et de fin des inscriptions et le nombre maximum de tickets pouvant être
vendus.

Si la vente de tickets n’est pas nécessaire pour l’événement, un simple bouton
**Inscription** sera affiché par défaut sur la page de l’événement.

![Vue de l'onglet Tickets dans Konvergo ERP Événements.](../../../_images/events-
tickets-tab.png)

### Envoyer des emails, SMS et publications automatisés aux participants de
l’événement

Sous l’onglet **Communication** , configurez un email, SMS ou publication
automatisés pour rester en contact avec les participants à l’événement. Pour
chaque communication, cliquez sur **Ajouter une ligne** dans le formulaire de
l’onglet **Communication** et choisissez ensuite parmi des modèles de
communication (ou créez-en un) en utilisant le menu déroulant dans la colonne
**Modèle**.

Ensuite, définissez l”**Intervalle** et l”**Unité** de temps pour la fréquence
d’envoi de la communication; utilisez ces champs temporels pour préciser la
fréquence d’envoi des communications en **Heures** , **Jours** , **Semaines**
, ou **Mois**. Il est également possible d’envoyer des communications
`Immédiatement` après l’activation d’un **Déclencheur** donné.

Dans la dernière colonne, déterminez le **Déclencheur** qui contrôle comment
et quand la communication est envoyée. Pour cette action, choisissez entre :
**Avant l’événement** , **Après chaque inscription** , ou **Après
l’événement**.

![Vue de l'onglet Communication dans Konvergo ERP
Événements.](../../../_images/events-communication-tab.png)

### Joindre un questionnaire aux inscriptions à l’événement

La mise en place d’un questionnaire lors de l’inscription à un événement est
un moyen efficace d’évaluer à l’avance les souhaits, les besoins et les
intérêts des participants à l’événement. Les questionnaires constituent
également des outils d’analyse informatifs pour les périodes d’analyse avant
(ou après) la tenue d’un événement.

Pour créer un questionnaire, dans l’application **Événements** , allez à
Configuration ‣ Paramètres et activez ensuite le paramètre **Questions**.

Une fois le paramètre activé, des questions et des réponses peuvent être
ajoutées (et enregistrées) sous l’onglet **Questions** du formulaire
d’événement. Pour chaque question, indiquez si elle ne doit être posée qu’une
seule fois en cochant la case **Demander une fois par commande** ou si la
question nécessite une **Réponse obligatoire** , ce qui rendra la question
obligatoire pour l’inscription.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si la case <b>Une fois par commande</b> est activée, le questionnaire ne sera affiché qu’une seule fois lors de l’inscription de 3 participants à l’événement.</p>
</div>

Vous avez le choix entre deux **Types de question** : **Sélection** et
**Saisie de texte**. Le type **Sélection** permet aux participants de
sélectionner une réponse parmi des options préconfigurées, qui sont saisies
dans l’onglet **Réponses** ci-dessous. Le type **Saisie de texte** permet aux
participants de donner leur propre réponse à la question dans une zone de
texte.

![Vue d'un formulaire d'événement, ouvrez l'onglet Questions et ajoutez une
question.](../../../_images/events-questions-tab.png)

### Enregistrer des notes internes ou ajouter des instructions sur le ticket

Dans l’onglet **Notes** , vous avez la possibilité d’ajouter une **Note**
et/ou des **Instructions sur le ticket**.

Dans le champ **Note** , vous pouvez laisser des notes internes (telles que
listes de tâches, coordonnées, etc.) pour que le personnel de l’événement
puisse s’y référer. Dans le champ **Instructions sur le ticket** , vous pouvez
partager des informations utiles pour le personnel et les participants (telles
que l’itinéraire pour se rendre sur le lieux de l’événement, les heures
d’ouverture/de fermeture, etc.).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Tapez <code>/</code> dans la zone de texte (<b>Note</b> ou <b>Instructions sur le ticket</b>) pour faire apparaître un sous-menu d’options de <b>Structure</b>. Ces options fournissent diverses options de formatage afin de garantir que les informations internes essentielles soient organisées pour que le personnel de l’événement puisse en prendre connaissance.</p>
</div> ![Vue de l'onglet Notes dans Konvergo ERP
Événements.](../../../_images/events-notes-tab.png)

## Inviter des participants à l’événement

Pour inviter des personnes à un événement, cliquez sur le bouton **Inviter**
situé dans le coin supérieur gauche du formulaire de l’événement.

Dans le formulaire d’invitation, vous avez la possibilité d’envoyer des
invitations par email ou par SMS. Chaque message peut être entièrement
personnalisé et des destinataires peuvent être ajoutés.

L’ajout d’une ligne de **Sujet** est obligatoire pour le message d’invitation,
mais le champ **Aperçu du texte** est optionnel. L”**Aperçu du texte** est une
phrase accrocheuse destinée à encourager les destinataires à ouvrir l’email.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans la plupart des cas, l”<b>Aperçu du texte</b> est affiché à côté du sujet. Laissez ce champ vide pour que les premiers caractères du contenu de l’email s’affichent à la place.</p>
</div>

### Sélectionner les invités et configurer les filtres de destinataires

Au milieu du formulaire d’invitation, trouvez et cliquez le champ
**Destinataires** pour faire apparaître un menu déroulant des options de
destinataires. Ces choix représentent l’endroit où Konvergo ERP trouvera les
informations souhaitées sur les destinataires.

Une fois qu’une option de ce menu est sélectionnée (par ex. **Candidat** ,
**Contact** , **Inscription à l’événement** , **Piste/Opportunité** , etc.),
Konvergo ERP enverra l’invitation à tous les destinataires qui correspondent à cette
règle initiale. Des règles additionnelles peuvent être ajoutées pour réduire
le nombre de destinataires ciblés, en cliquant sur **Ajouter un filtre**.

![Vue du bouton Ajouter un filtre en-dessous du champ des destinataires dans
Konvergo ERP Événements.](../../../_images/add-filter-button1.png)

Le fait que cliquer sur **Ajouter un filtre** fait apparaître trois champs,
formatés comme une équation. Pour faire apparaître les options du sous-menu,
cliquez sur chaque champ et faites les choix souhaités jusqu’à ce que la
configuration préférée soit atteinte. Le nombre d”:`Enregistrements` qui
correspondent aux règles est indiqué en vert à droite du champ
**Destinataires**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Certaines options de sous-menu dans le premier champ de règle permettent un deuxième choix pour fournir encore plus de spécificité.</p>
</div>

À droite de chaque règle se trouvent les icônes **x** , **+** , et **…**.
L’icône **x** supprime un nœud (ligne) spécifique de la règle. L’icône **+**
ajoute un nœud (ligne) à la règle. Et l’icône **…** ajoute une branche au
nœud. Une branche signifie que deux sous-nœuds sont ajoutés à la règle,
donnant encore plus de spécificité à la ligne qui la précède.

### Créer une invitation personnalisée à un événement

Dans l’onglet **Corps de l’email** , vous pouvez choisir parmi un certain
nombre de modèles de message préconfigurés. Sélectionnez le modèle souhaité et
modifiez chaque élément de son design avec la fonctionnalité glisser-déposer
du constructeur web d’Konvergo ERP, situé dans la barre latérale droite.

![Vue de la fonctionnalité de glisser-déposer des blocs de construction
utilisés pour personnaliser les emails d'invitation à un
événement.](../../../_images/event-email-builder-block.gif)
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour créer un email d’invitation à un événement à partir de zéro, sélectionnez le modèle <b>Texte simple</b> et Konvergo ERP fournira un canevas d’email vierge, à personnaliser soit en utilisant l’éditeur de texte enrichi en frontend qui accepte les commandes slash (<code>/</code>), soit en utilisant l’éditeur de code XML lorsque le <a href="../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a> est activé et l’icône <b>&lt;/&gt;</b> est pressée.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’onglet <b>Corps de l’email</b> (et les options du modèle) sont uniquement disponibles si le <b>Type d’envoi</b> de l’email d’invitation est <b>Email</b>. Si le <b>Type d’envoi</b> est <b>SMS</b>, un onglet <b>Contenu du SMS</b> (étant un espace de texte vide) apparaît à la place.</p>
</div>

### Modifier les paramètres d’invitation à un événement

Les options sous l’onglet **Paramètres** varient en fonction du **Type
d’envoi** choisi.

Si le **Type d’envoi** est **Email** , un employé peut être désigné comme
**Responsable** , ce que signifie que cette personne est responsable de ce
message d’invitation spécifique. Des alias de messagerie d”**Envoi** et de
**Réponse** peuvent également être définis ici.

De plus, si des documents spécifiques sont requis (ou utiles) pour cette
invitation, ils peuvent être envoyés avec cet email, en cliquant sur **JOINDRE
UN FICHIER** et en ajoutant le ou les documents en question.

Si le **Type d’envoi** est **SMS** , un **Reponsable** peut être désigné et
l’option **Inclure un lien de désinscription** est disponible.

### Envoyer des invitations aux destinataires

Si le **Type d’envoi** est **Email** , vous avez trois options pour envoyer
l’invitation : **Envoyer** , **Planifier** , et **Tester**.

L’option **Envoyer** permet d’envoyer l’invitation immédiatement. L’option
**Planifier** fait apparaître une fenêtre contextuelle dans laquelle il est
possible de sélectionner une date/heure d’envoi de l’email. L’option
**Tester** fait apparaître une fenêtre contextuelle, dans laquelle des
adresses d’email de destinataires spécifiques peuvent être saisies pour que
Konvergo ERP leur envoie la version actuelle du mailing pour révision avant de
l’envoyer officiellement aux participants potentiels de l’événement.

Si le **Type d’envoi** est **SMS** , il y a quatre options pour envoyer
l’invitation : **Mettre dans la file d’attente** , **Envoyer maintenant** ,
**Planifier** et **Tester**.

L’option **Mettre dans la file d’attente** permet de planifier l’envoi d’un
SMS à tous les destinataires (qui correspondent aux règles désignées, le cas
échéant) dans un avenir proche. Le fait de cliquer sur **Mettre dans la file
d’attente** fait apparaître une fenêtre contextuelle qui demande une
confirmation. Une fois confirmé, une bannière bleue apparaît sur le formulaire
d’invitation, indiquant que le SMS sera envoyé plus tard dans la journée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les options <b>Envoyer maintenant</b>, <b>Planifier</b> et <b>Tester</b> fonctionnent de la même manière pour les deux options <b>Type d’envoi</b>.</p>
</div>

## Publier des événements

Tant qu’un événement n’est pas publié, il reste masqué pour le public du site
web, qui ne pourra pas s’inscrire. Pour publier un événement, naviguez jusqu’à
l’événement depuis le backend d’Konvergo ERP via l’application **Événements** ou
accédez à la page masquée de l’événement depuis le frontend en tant
qu’utilisateur privilégié ou administrateur.

Si naviguez depuis le backend, allez au formulaire de l’événement et cliquez
sur le bouton intelligent **Visiter le site web** pour accéder à la page de
l’événement sur le site web (sur le frontend). Si vous commencez à partir du
frontend, allez simplement à la page de l’événement qui doit être publié.

Quel que soit le chemin emprunté, une page d’événement peut uniquement être
publiée depuis le frontend. Dans le coin supérieur droit de la page de
l’événement sur le site web, activez le commutateur pour changer le statut
rouge **Non publié** en statut vert **Publié**. La page de l’événement sera
ainsi immédiatement accessible au public depuis le site web.

![Vue d'une page du site web et l'option de publier le site web dans Konvergo ERP
Événements.](../../../_images/events-frontend-publish.png)

