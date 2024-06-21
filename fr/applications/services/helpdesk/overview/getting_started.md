# Démarrer avec Assistance

Konvergo ERP **Assistance** est une application d’assistance aux clients basée sur les
tickets. Les équipes peuvent suivre, prioriser et résoudre les problèmes
depuis leur pipeline, qui est organisé en étapes personnalisables. Plusieurs
équipes peuvent être configurées et gérées dans un seul tableau de bord.

## Créer des équipes d’assistance

La configuration de plusieurs équipes permet de regrouper les tickets par lieu
ou par type d’assistance.

Pour afficher ou modifier les équipes d” _Assistance_ , allez à Assistance ‣
Configuration ‣ Équipes. Pour créer une nouvelle équipe, cliquez sur le bouton
**Nouveau** dans le coin supérieur gauche du tableau de bord. Saisissez-y le
nom de la nouvelle équipe et complétez les champs restants tels que définis
dans les sections suivantes du formulaire.

![Vue de la page des équipes d'assistance dans Konvergo ERP
Assistance](../../../../_images/helpdesk-teams-list.png)

### Assignation & Visibilité

#### Décider à qui l’équipe sera visible

Dans la section **Visibilité** , décidez qui peut voir cette équipe et ses
tickets.

  * Les **Utilisateurs internes invités** ont accès à l’équipe et aux tickets auxquels ils sont abonnés. Cette option peut être modifiée sur chaque ticket individuel.

  * **Tous les utilisateurs internes** ont accès à l’équipe et tous ses tickets sans y être abonnés.

  * **Tous les utilisateurs internes et les utilisateurs portail invités** ont accès à l’équipe sans y être abonnés. Les utilisateurs portail pourront uniquement accéder aux tickets auxquels ils sont abonnés.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Une équipe <code>Service clientèle</code> est chargée de traiter les problèmes généraux liés à l’expédition et aux produits et aura le paramètre de visibilité <b>Tous les utilisateurs internes et les utilisateurs portail invités</b>. Toutefois, une équipe <code>Services financiers</code> est chargée des tickets liés à la comptabilité ou aux taxes et devra uniquement être visible par les <b>Utilisateurs internes invités</b>.</p>
</div>

#### Assigner automatiquement les nouveaux tickets

À la réception des tickets, ils doivent être assignés à un membre de l’équipe
d’assistance. Cela peut être fait manuellement sur chaque ticket
individuellement ou par **Assignation automatique**. Cochez la case à côté
d”**Assignation automatique** pour activer la fonctionnalité pour cette
équipe.

![Vue de la page des paramètres d'une équipe d'assistance mettant en évidence
les fonctionnalités d'assignation et de visibilité dans Konvergo ERP
Assistance](../../../../_images/assignment-visibility.png)

Sélectionnez l’une des méthodes d’assignation suivantes, en fonction de la
manière dont la charge de travail doit être répartie au sein de l’équipe :

  * **Chaque utilisateur se voit attribuer un nombre égal de tickets** assigne des tickets aux membres de l’équipe
    

en fonction du nombre total de tickets, quel que soit le nombre de tickets
ouverts ou clôturés qui leur sont actuellement assignés.

  * **Chaque utilisateur a un nombre égal de tickets ouverts** assigne des tickets aux membres de l’équipe
    

en fonction du nombre de tickets ouverts qui sont actuellement assignés. Cette
option est utile pour déléguer automatiquement une charge de travail plus
importante aux personnes les plus performantes qui ont tendance à clôturer les
tickets rapidement.

Enfin, ajoutez les **membres de l’équipe** qui se verront assigner des tickets
pour cette équipe. Laissez le champ vide pour inclure tous les employés qui
ont les assignations et les droits d’accès appropriés configurés dans les
paramètres de leur compte utilisateur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si un employé a des congés planifiés dans l’application <b>Congés</b>, il ne se verra pas assigner de tickets pendant cette période. Si aucun employé n’est disponible, le système continuera à chercher jusqu’à ce qu’il y ait une correspondance.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../general/users#users-add-individual"><span class="std std-ref">Gérer des utilisateurs</span></a></p></li>
<li><p><a href="../../../general/users/access_rights">Droits d’accès</a></p></li>
</ul>
</div>

## Créer ou modifier les étapes du kanban

Les **Étapes** sont utilisées pour organiser le pipeline d” _Assistance_ et
suivre la progression des tickets. Les étapes sont personnalisables et peuvent
être renommées pour répondre aux besoins de chaque équipe.

Pour afficher ou modifier les étapes d” _Assistance_ , allez à Assistance ‣
Configuration ‣ Étapes.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Le <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">mode développeur</span></a> doit être activé pour pouvoir accéder au menu des étapes. Pour activer le mode développeur, allez aux Paramètres ‣ Paramètres généraux ‣ outils développeur et cliquez sur <b>Activer le mode développeur</b>.</p>
</div>

La vue de liste affiche une vue d’ensemble de toutes les étapes actuellement
disponibles dans Assistance. Elles sont listées dans l’ordre dans lequel elles
apparaissent dans le pipeline. Pour modifier l’ordre des étapes, utilisez les
boutons de flèche situés à gauche de la liste.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Modifiez l’ordre des étapes dans la vue kanban en déplaçant les colonnes individuelles.</p>
</div> ![Vue de la liste des étapes mettant en évidence l'option
de créer une nouvelle étape](../../../../_images/stages-create-new.png)

Pour créer une nouvelle étape, cliquez sur le bouton **Nouveau** dans le coin
supérieur gauche du tableau de bord. Ensuite, donnez un nom à la nouvelle
étape et ajoutez une description (même si ce n’est pas requis). Complétez les
champs restants en suivant les étapes suivantes.

![Vue de la page des paramètres d'une étape dans Konvergo ERP
Assistance](../../../../_images/stage-settings.png)

### Ajouter des modèles d’email et de SMS aux étapes

Lorsqu’un **Modèle d’email** est ajouté à une étape, un email est
automatiquement envoyé au client lorsqu’un ticket atteint cette étape
spécifique dans le pipeline d’Assistance. De la même manière, l’ajout d’un
**Modèle de SMS** entraînera l’envoi d’un SMS au client.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>L’envoi de SMS est un service d’Achats In-App (IAP) qui requiert des crédits prépayés pour fonctionner. Consultez la <a href="https://iap-services.odoo.com/iap/sms/pricing">FAQ sur la tarification des SMS</a> pour plus d’informations.</p>
</div>

Pour sélectionner un modèle d’email existant, sélectionnez-le dans le champ
**Modèle d’email**. Cliquez sur la flèche à droite du champ pour modifier le
modèle.

Pour créer un nouveau modèle, cliquez sur le champ et commencez à écrire un
nouveau titre de modèle. Sélectionnez ensuite **Créer et modifier** et
complétez les détails du formulaire.

Suivez les mêmes étapes pour sélectionner, modifier ou créer un **Modèle de
SMS**.

![Vue de la page de configuration d'un modèle de SMS dans Konvergo ERP
Assistance](../../../../_images/sms-template1.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../general/companies/email_template">Modèles d’email</a></p>
</div>

### Assigner des étapes à une équipe

Faites une sélection dans le champ **Équipes** dans le formulaire des
**Étapes**. Il est possible de sélectionner plus d’une équipe, puisque la ou
les mêmes étapes peuvent être assignées à plusieurs équipes.

> ![Vue de la configuration d'une étape mettant en évidence le champ des
> équipes](../../../../_images/stages-settings-sharing.png)

### Replier une étape

Cochez la case à côté de **Repliée dans la vue Kanban** dans le formulaire des
**Étapes** pour afficher cette étape comme _repliée_ par défaut dans la vue
kanban de cette équipe.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les tickets qui atteignent une étape <em>repliée</em> sont considérés comme clôturés. Clôturer un ticket avant que le travail ne soit terminé peut entraîner des problèmes d’analyse et de communication. Ce paramètre ne doit être activé que pour les étapes qui sont considérées comme des étapes de <em>clôture</em>.</p>
</div>

Alternativement, les étapes peuvent être repliées temporairement dans la vue
kanban, en cliquant sur l’icône des paramètres et en sélectionnant
**Replier**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Replier manuellement une étape dans la vue kanban ne clôturera pas les tickets de l’étape.</p>
</div>

