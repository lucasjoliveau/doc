# Tester/lancer des campagnes

L’application Konvergo ERP _Marketing Automation_ permet aux utilisateurs de tester
les campagnes de marketing (et les mailings) avant de les lancer
officiellement afin de vérifier et corriger toutes les erreurs avant qu’elles
n’atteignent leur public cible.

## Tester des campagnes

Pour tester une campagne de marketing, ouvrez l’application Marketing
Automation, et sélectionnez la campagne que vous voulez tester. Le formulaire
de la campagne s’ouvre alors.

Sur le formulaire de la campagne, assurez-vous que la campagne a déjà des
activités configurées dans le flux de travail (ou créez une campagne en
suivant les étapes de [cette documentation](workflow_activities)).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les tests des campagnes de marketing automation doivent être effectués dans la version de production de la base de données. Les bases de données dupliquées (ou d’essai) ont des capacités d’envoi d’emails limitées.</p>
</div>

Pour lancer un test, cliquez sur le bouton **Lancer un test** en haut du
formulaire de la campagne, à droit du bouton **Lancer**.

![Bouton Lancer un test sur un formulaire de campagne dans Konvergo ERP Marketing
Automation.](../../../../_images/launch-test.png)

Lorsque vous cliquez sur ce bouton, une fenêtre contextuelle **Lancer un
test** s’ouvre.

![Fenêtre contextuelle permettant de lancer un test dans Konvergo ERP Marketing
Automation.](../../../../_images/launch-test-popup-window.png)

Dans la fenêtre contextuelle **Lancer un test** , cliquez sur le champ
**Choisissez ou créez un contact pour générer un participant test** pour faire
apparaître un menu déroulant de contacts. Dans ce menu déroulant, sélectionnez
un contact existant (ou créez un nouveau contact) sur lequel vous voulez
effectuer le test.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous ne pouvez sélectionner qu’un seul contact dans la fenêtre contextuelle <b>Lancer un test</b>.</p>
</div>

Pour créer un nouveau contact directement dans la fenêtre contextuelle
**Lancer un test** , commencez par taper le nom du nouveau contact dans le
champ vierge et cliquez sur **Créer et modifier…**.

![Tapez un nouveau contact directement dans la fenêtre contextuelle permettant
de lancer un test dans Konvergo ERP.](../../../../_images/new-contact-from-launch-
test-popup.png)

Cette opération fait apparaître un formulaire contextuel vierge **Créer
Enregistrement** dans lequel vous _devez_ compléter les coordonnées
nécessaires (**Email** , **Mobile** , etc.) pour que le test fonctionne.
Lorsque vous avez saisi toutes les informations nécessaires, cliquez sur
**Enregistrer & Fermer**.

![Un formulaire de contact vierge à partir d'une fenêtre contextuelle
permettant de lancer un test dans Konvergo ERP Marketing
Automation.](../../../../_images/blank-contact-form.png)

Lorsque tous les champs nécessaires ont été saisis, cliquez sur **Enregistrer
& Fermer** pour revenir à la fenêtre contextuelle **Lancer un test**.

Une fois que vous avez sélectionné un contact, cliquez sur **Lancer** pour
afficher la page de test de la campagne.

![Écran de test dans Konvergo ERP Marketing Automation.](../../../../_images/test-
screen.png)

Sur la page de test de la campagne, le nom de l”**Enregistrement** en cours de
test est visible, tout comme l’heure précise à laquelle ce flux de test a été
lancé dans le champ **Flux de travail commencé le**. En dessous, dans la
section **Flux de travail** , se trouve la première activité (ou activités) du
flux de travail qui est testée.

Pour lancer un test, cliquez sur le bouton **Exécuter** , représenté par une
icône **▶️ (bouton de lecture)** à côté de la première activité du flux de
travail. Lorsque vous cliquez sur le bouton, la page recharge et Konvergo ERP montre
les différents résultats (et analyses) liés à cette activité spécifique au fur
et à mesure qu’ils se produisent, en temps réel.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si une activité enfant est planifiée sous une activité parent, cette activité enfant sera révélée légèrement en retrait dans le flux de travail, une fois que l’activité parent aura été exécutée, via l’icône <b>▶️ (bouton de lecture)</b>.</p>
</div> ![Progression du flux de test dans Konvergo ERP Marketing
Automation.](../../../../_images/workflow-test-progress.png)

Une fois que toutes les activités du flux de travail sont exécutées, le test
prend fin et la barre de statut (dans le coin supérieur droit) passe à l’étape
**Terminé**.

Pour arrêter un test avant que toutes les activités du flux de travail ne
soient terminées, cliquez sur le bouton **Arrêter** dans le coin supérieur
gauche de la page de test de la campagne.

## Exécuter des campagnes

Pour exécuter une campagne, allez à l’application Marketing Automation, et
sélectionnez la campagne que vous voulez exécuter.

Sur le formulaire de la campagne, avec toutes les activités souhaitées prête
dans la section **Flux de travail** , cliquez sur **Lancer** dans le coin
supérieur gauche pour officiellement lancer la campagne auprès de l’audience
cible configurée sur le formulaire de la campagne.

Le fait de cliquer sur **Lancer** lance la campagne et la barre de statut de
la campagne passe à **En cours** , qui se situe dans le coin supérieur droit
du formulaire de campagne.

![Le statut d'une campagne de marketing passant à en cours dans le coin
supérieur droit.](../../../../_images/campaign-running-status.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si certains participants sont déjà en cours d’exécution dans le cadre d’une campagne et que celle-ci a été arrêtée pour une raison quelconque, le fait de cliquez à nouveau sur le bouton <b>Lancer</b> entraîne l’affichage d’une fenêtre d’avertissement. Cet avertissement conseille à l’utilisateur de cliquez sur le bouton <b>Mettre à jour</b> pour appliquer les modifications apportées à la campagne.</p>
<img alt="Fenêtre d'avertissement signalant que le flux de travail d'une campagne de marketing a été modifié." class="align-center" src="../../../../_images/workflow-modification-warning.png"/>
<p>Sachez que les participants qui ont déjà participé à l’ensemble de la campagne dans son état d’origine <b>peuvent</b> être réintroduits dans la campagne modifiée et que de nouvelles traces peuvent être créées pour eux.</p>
</div>

Ensuite, lorsque les mailings et les actions sont déclenchés dans le **Flux de
travail** , les diverses statistiques et données liées à chaque activité
apparaissent dans chaque bloc d’activité. Une série de boutons intelligents
liés aux statistiques apparaît également en haut du formulaire de la campagne.

Ces boutons intelligents analytiques s’enrichissent _également_ de données en
temps réel au fur et à mesure que la campagne progresse : **Modèles** ,
**Clics** , **Tests** , **Participants**.

![La rangée de boutons intelligents qui apparaissent dans un campagne
marketing en cours dans Konvergo ERP.](../../../../_images/campaign-smart-buttons.png)

## Arrêter des campagnes

Pour arrêter une campagne en cours, allez à l’application Marketing
Automation, et sélectionnez la campagne que vous voulez arrêter. Sur le
formulaire de la campagne, cliquez sur le bouton **Arrêter** dans le coin
supérieur gauche.

![Le bouton arrêter sur un formulaire de campagne typique dans l'application
Konvergo ERP Marketing Automation.](../../../../_images/stop-button-campaign-form.png)

Lorsque vous cliquez dessus, le campagne est officiellement arrêtée et le
statut passe à **Arrêté** dans le coin supérieur droit du formulaire de la
campagne.

![Statut arrêté de la campagne sur son formulaire dans Konvergo ERP Marketing
Automation.](../../../../_images/campaign-stopped-status-bar.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="first_campaign">Campagnes de marketing automation</a></p></li>
<li><p><a href="target_audience">Cibler un public</a></p></li>
<li><p><a href="workflow_activities">Activités du flux de travail de la campagne</a></p></li>
</ul>
</div>

