# Actions automatisées (automatisations)

Les actions automatisées sont utilisées pour déclencher des modifications
automatiques basées sur les actions de l’utilisateur (par ex. appliquer une
modification lorsqu’un champ est défini sur une valeur spécifique) ou sur des
conditions temporelles (par ex. archiver un enregistrement 7 jours après sa
dernière mise à jour).

Pour créer une action automatisée avec Studio, allez aux **Automatisations**
depuis n’importe quel endroit de Studio.

Pour chaque action automatisée que vous créez, il faut définir les éléments
suivants : le Modèle, le Déclencher, Appliquer sur et l”Action.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Exemple d'une action automatisée sur le modèle d'abonnement" class="align-center" src="../../_images/automated-action-example.png"/>
</div>

## Modèle

Sélectionnez le modèle sur lequel l’action automatisée doit être appliquée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le modèle sur lequel vous vous trouvez lorsque vous cliquez sur <b>Automatisations</b> est présélectionné par défaut.</p>
</div>

## Déclencher

Définissez le moment où l’action automatisée doit être appliquée. Six
déclencheurs sont à votre disposition.

### À la création

L’action est déclenchée lorsqu’un enregistrement est créé et enregistré.

### Lors d’une mise à jour

L’action est déclenchée lorsqu’un enregistrement précédemment enregistré est
édité et ensuite enregistré.

  * Utilisez des **champs de déclenchement** pour préciser quels champs - et uniquement ceux-là - déclenchent l’action lors de leur mise à jour.

  * Pour détecter le passage d’un enregistrement d’un état à un autre, définissez un filtre **Avant la mise à jour du domaine** , qui vérifie si la condition est remplie avant la mise à jour de l’enregistrement. Définissez ensuite un filtre Appliquer sur, qui vérifie si la condition est remplie après la mise à jour de l’enregistrement.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si vous souhaitez que l’action automatisée se déclenche lorsqu’une adresse email est définie sur un contact, définissez le filtre <b>Avant la mise à jour du domaine</b> sur <code>Email n'est pas défini</code> et le domaine <b>Appliquer sur</b> sur <code>Email est défini</code>.</p>
<img alt="Exemple d'un déclencheur lors d'une mise à jour" class="align-center" src="../../_images/on-update-trigger-example.png"/>
</div>

### À la création et en lors d’une mise à jour

L’action est déclenchée lorsqu’un enregistrement est créé et enregistré ou
édité ultérieurement et enregistré.

### Lors de la suppression

L’action est déclenchée lorsqu’un enregistrement est supprimé.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ce déclencheur est rarement utilisé, puisqu’il est généralement préférable d’archiver des enregistrements au lieu de les supprimer.</p>
</div>

### Basé sur une modification du formulaire

L’action est déclenchée lorsqu’une modification est apportée à la valeur d’un
champ de déclenchement dans la [vue Formulaire](views#studio-views-
general-form), même avant de sauvegarder l’enregistrement. Ce déclencheur
fonctionne uniquement sur l’interface utilisateur lorsqu’une modification est
effectuée par un utilisateur. Si le champ est modifié par une autre action et
non par l’utilisateur, l’action ne sera pas exécutée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Ce déclencheur ne peut être utilisé qu’avec l”<a href="#studio-automated-actions-action-python-code"><span class="std std-ref">action Exécuter un code Python</span></a>, un développement est donc nécessaire.</p>
</div>

### Basé sur une condition temporelle

L’action est déclenchée lorsqu’une date ou une valeur de date et d’heure d’un
champ de déclenchement est atteinte.

  * Pour déclencher l’action après la **Date de déclenchement** , ajoutez un nombre de minutes, d’heures, de jours ou de mois sous **Délai après la date de déclenchement**. Pour déclencher l’action avant, ajoutez plutôt un nombre négatif.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si vous voulez envoyer un email de rappel 30 minutes avant le début d’un événement de calendrier, sélectionnez le <b>Début (Événement Calendrier)</b> sous <b>Date de déclenchement</b> et définissez le <b>Délai après la date de déclenchement</b> à <b>-30</b> <b>Minutes</b>.</p>
<img alt="Exemple d'un déclencheur basé sur une condition temporelle" class="align-center" src="../../_images/timed-condition-trigger-example.png"/>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Par défaut, le planificateur vérifie les dates de déclenchement toutes les 4 heures.</p>
</div>

## Appliquer sur

Définissez les enregistrements du modèle sur lesquels l’action automatisée
doit être appliquée. Cela fonctionne de la même manière lorsque vous appliquez
des filtres sur un modèle.

## Action

Déterminez ce que l’action automatisée doit faire (action du serveur). Vous
avez le choix entre huit types d’actions.

### Exécuter le code Python

L’action est utilisée pour exécuter du code Python. Les variables disponible
sont décrites dans l’onglet **code Python** , qui est également utilisé pour
écrire votre code, ou dans l’onglet **Aide**.

  * Pour permettre l’exécution de l’action via le site web, cochez **Disponible sur le site web** et ajoutez un **Chemin du site web**.

### Créez un nouvel enregistrement

L’action est utilisée pour créer un nouvel enregistrement sur n’importe quel
modèle.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La sélection d’un <b>Modèle cible</b> est uniquement requise si vous souhaitez cibler un autre modèle que celui sur lequel vous vous trouvez.</p>
</div>

  * Pour lier l’enregistrement qui a déclenché la création d’un nouvel enregistrement, sélectionnez un champ sous **Champ de lien**. Par exemple, vous pouvez créer un contact automatiquement lorsqu’une piste est convertie en opportunité.

  * L’onglet **Données à saisir** : l’onglet est utilisé pour préciser les valeurs du nouvel enregistrement. Après avoir sélectionné un **Champ** , sélectionnez son **type d’évaluation** :

    * **Valeur** : permet d’indiquer directement la valeur brute du champ dans la colonne **Valeur**.

    * **Référence** : permet de sélectionner l’enregistrement sous la colonne **Enregistrement** et de laisser Studio ajouter l’ID interne dans la colonne **Valeur**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si une action automatisée crée une nouvelle tâche dans un projet, vous pouvez l’assigner à un utilisateur spécifique en définissant le <b>Champ</b> sur <b>Utilisateur responsable (Projet)</b>, le <b>Type d’évaluation</b> sur <b>Référence</b> et l”<b>Enregistrement</b> sur un utilisateur spécifique.</p>
<img alt="Exemple de l'action Créer un nouvel enregistrement" class="align-center" src="../../_images/new-record-example.png"/>
</div>

    * **Expression Python** : permet de définir de manière dynamique la valeur du nouvel enregistrement pour un champ utilisant du code Python dans la colonne **Valeur**.

### Mettre à jour l’enregistrement

L’action est utilisée pour définir une ou plusieurs valeurs pour un ou
plusieurs champs de n’importe quel enregistrement sur le modèle actuel.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La procédure à suivre pour compléter l’onglet <b>Données à saisir</b> est la même que celle décrite sous <a href="#studio-automated-actions-action-new-record"><span class="std std-ref">Créez un nouvel enregistrement</span></a>.</p>
</div>

### Exécuter plusieurs actions

L’action permet de déclencher plusieurs actions en même temps. Pour ce faire,
cliquez sur **Ajouter une ligne** sous l’onglet **Actions**. Dans la fenêtre
contextuelle **Actions enfants** , cliquez sur **Créer** et configurez
l’action.

### Envoyer un email

L’action permet d’envoyer un email à un contact lié à un enregistrement
spécifique. Pour ce faire, sélectionnez ou créez un **Modèle d’email**.

### Ajouter des abonnés

L’action permet d’abonner des contacts existants à l’enregistrement.

### Créer l’activité suivante

L’action permet de programmer une activité suivante liée à l’enregistrement.
Utilisez l’onglet **Activité** pour la configurer comme d’habitude, mais au
lieu du champ **Assigné à** , sélectionnez un **Type d’utilisateur de
l’activité**. Sélectionnez l”**Utilisateur spécifique** et ajoutez
l’utilisateur sous **Responsable** si l’activité doit toujours être assignée
au même utilisateur. Pour cibler de manière dynamique un utilisateur lié à
l’enregistrement, sélectionnez plutôt **Utilisateur générique de
l’enregistrement** et modifiez le **Nom du champ utilisateur** le cas échéant.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le modèle sur lequel vous vous trouvez lorsque vous cliquez sur <b>Automatisations</b> est présélectionné par défaut.</p>
</div>0

### Envoyer un SMS

L’action permet d’envoyer un SMS à un contact lié à l’enregistrement. Pour ce
faire, sélectionnez ou créez un **Modèle de SMS**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le modèle sur lequel vous vous trouvez lorsque vous cliquez sur <b>Automatisations</b> est présélectionné par défaut.</p>
</div>1

