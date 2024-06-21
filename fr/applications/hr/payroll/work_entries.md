# Prestations

Le tableau de bord des _Prestations_ , accessible via Paie ‣ Prestations ‣
Prestations, fournit un aperçu visuel des feuilles de temps individuelles de
chaque employé, chaque jour étant divisé en un poste du matin et un poste de
l’après-midi.

![Le tableau de bord des prestations affichant les prestations de tous les
employés.](../../../_images/work-entries-overview.png)

Pour modifier la vue de manière à n’afficher que les prestations d’un seul
jour, d’une seule semaine ou d’un seul mois, cliquez sur l’un des liens
correspondants pour le **Jour** , la **Semaine** , ou le **Mois** , situés en
haut du tableau de bord.

Utilisez les icônes **⬅️ (flèche gauche)** et **➡️ (flèche droite)** situées à
gauche et à droite du bouton **Aujourd’hui** pour ajuster les dates affichées.
Les flèches ajustent la date en fonction de la plage de temps sélectionnée.
Par exemple, si le mois est sélectionné, les flèches se déplacent d’un mois à
chaque clic. Si la semaine ou le jour est sélectionné, les flèches se
déplacent d’une semaine ou d’un jour à chaque clic, respectivement.

## Ajouter une nouvelle prestation

Si une prestation manque et doit être ajoutée, comme les congés maladie ou les
congés payés, cliquez sur **Ajouter** pour créer une nouvelle prestation. Une
fenêtre contextuelle s’affiche, avec plusieurs champs à remplir.

Saisissez le **Nom de la prestation** , comme `Congé maladie` ou toute autre
description courte. Sélectionnez l”**Employé** et le **Type de prestation**
dans les listes déroulantes respectives.

![Remplissez le formulaire de création d'une prestation dans
Konvergo ERP.](../../../_images/create.png)

Ensuite, saisissez la date et l’heure de la prestation dans les menus
déroulants **Du** et **Au**. Sélectionnez d’abord la date en allant au bon
mois et à la bonne année à l’aide des icônes **⬅️ (flèche gauche)** et **➡️
(flèche droite)** , puis cliquez sur le jour spécifique.

Ensuite, sélectionnez l’heure en cliquant sur l’icône **⏰ (horloge)** et en
utilisant les icônes **⬆️ (flèche vers le haut)** et **⬇️ (flèche vers le
bas)** pour chaque section pour entrer l’heure, la minute et la seconde de la
période.

La **Période** affichera les heures en fonction des entrées **Au** et **Du**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Avant de cliquer sur <b>Enregistrer &amp; Fermer</b> ou <b>Enregistrer &amp; Nouveau</b>, il est conseillé de revérifier la <b>Période</b> pour s’assurer que l’heure indiquée correspond aux champs <b>Au</b> et <b>Du</b>.</p>
<img alt="Heures saisies dans le champ Période." class="align-center" src="../../../_images/period.png"/>
</div>

Une fois les informations saisies, cliquez sur **Enregistrer & Fermer** pour
enregistrer l’entrée et fermer la fenêtre contextuelle, ou sur **Enregistrer &
Nouveau** pour enregistrer l’entrée et créer un autre **Type de prestation**.

## Regénérer les prestations

Après l’ajout ou la modification d’une prestation, les prestations doivent
être regénérées pour le(s) employé(s) concerné(s). Cliquez sur le bouton
**Regénérer les prestations** en haut du tableau de bord principal et une
fenêtre contextuelle s’ouvre.

Sélectionnez l”**Employé** pour lequel vous devez regénérer les prestations
dans le **menu déroulant** , et ajustez les champs **Du** et **Au** pour
afficher la bonne plage de dates. Cliquez sur le bouton **Regénérer les
prestations** et les prestations seront recréées. Une fois l’opération
terminée, la fenêtre contextuelle se ferme.

![Regénérez une prestation pour un employé en
particulier.](../../../_images/regenerate-details.png)

## Conflits

Un conflit apparaît pour toute demande qui n’a pas été approuvée, comme les
congés maladie ou des vacances, ou s’il y a des erreurs dans les prestations,
comme des champs obligatoires laissés vides. Les conflits doivent être résolus
avant que les fiches de paie puissent être générées.

Toute prestation qui présente un conflit à résoudre est indiquée dans le
tableau de bord principal de la **Prestation** , accessible via Paie ‣
Prestations ‣ Conflits, où seuls les conflits devant être résolus sont
affichés.

![Le tableau de bord des conflits affichant les prestations en conflit des
employés.](../../../_images/conflicts.png)

Les conflits sont signalés par un triangle orange dans le coin supérieur
gauche de chaque prestation individuelle. Cliquez sur une prestation
individuelle pour voir les détails du conflit dans une fenêtre contextuelle.

Le conflit est brièvement expliqué dans une zone de texte orange.

![Les détails d'un conflit apparaissent dans la fenêtre
contextuelle.](../../../_images/conflict-detail.png)

Le **Nom de la prestation** , l”**Employé** , et le **Type de prestation**
sont répertoriés dans la partie gauche de la fenêtre contextuelle. La plage de
dates **Du** et **Au** , ainsi que le temps total demandé (en heures)
apparaissent dans le champ **Période** , du côté droit.

S’il y a un conflit parce qu’une demande de congé pour la même période existe
déjà dans le système, le congé sera saisi dans le champ **Congé**. Le fait de
cliquer sur le bouton **Lien externe** à côté de l’entrée **Congé** fera
apparaître la demande de congé en double.

Les détails de la demande de congé s’affichent dans la fenêtre contextuelle.
La demande peut être modifiée au besoin. Cliquez sur le bouton **Valider** ou
**Refuser** pour approuver ou rejeter la demande, puis cliquez sur le bouton
**Enregistrer** pour enregistrer les modifications.

![Modifiez et/ou validez une demande de congé en
double.](../../../_images/validate.png)

Une fois que la demande de congé en double a été approuvée et enregistrée,
vous êtes redirigé vers le conflit. Cliquez sur **Refuser le congé** ou
**Approuver le congé** à l’aide des boutons en haut à droite pour soit
approuver, soit refuser la demande. Répétez pour tous les conflits jusqu’à ce
qu’il n’y en ait plus.

Après que les conflits ont été résolus, les prestations doivent être
regénérées pour chaque employé en cliquant sur le bouton **Regénérer les
prestations** et en saisissant les informations correspondantes de chaque
employé.

![Le bouton Regénérer les prestations sur le formulaire de regénération des
prestations.](../../../_images/regenerate-employee.png)

## Générer des fiches de paie

Pour générer les fiches de paie, allez à la période pour laquelle les fiches
de paie doivent être générées, soit le jour, la semaine ou le mois. Lorsque la
période de paie souhaitée est affichée, cliquez sur le bouton **Générer les
fiches de paie**.

![Le bouton Générer les fiches de paie dans le tableau de bord des
prestations.](../../../_images/generate-payslips1.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le bouton <b>Générer les fiches de paie</b> n’est pas actif (il apparaît en turquoise clair au lieu de turquoise foncé), cela indique qu’il y a des conflits. <em>Résolvez d’abord les conflits</em> apparaîtra comme un avertissement lorsque vous passez la souris sur <b>Générer les fiches de paie</b>. Résolvez tous les conflits avant de générer les fiches de paie.</p>
</div>

Une entrée de lot apparaît pour la période sélectionnée. Le nom du lot
apparaît en haut dans le champ **Nom** , avec généralement le mois et l’année
pour le lot en question.

La plage de dates à laquelle les fiches de paie s’appliquent apparaît dans le
champ **Période**. La société apparaît dans le champ **Société** , ainsi
qu’une option permettant de marques les fiches de paie comme avoir. Pour
apporter des modifications, cliquez sur le bouton **Modifier** en haut à
gauche, apportez vos changements, puis cliquez sur **Enregistrer** pour
accepter les changements ou sur **Ignorer** pour revenir aux données
d’origine.

![Informations sur le lot qui apparaissent lors de la création d'un
lot.](../../../_images/batch.png)

Cliquez sur le bouton **Créer une entrée brouillon** pour créer les fiches de
paie du lot.

Cliquez sur le bouton **Fiches de paie** en haut à droite pour afficher toutes
les fiches de paie du lot.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les fiches de paie auront un statut <em>En attente</em> jusqu’à ce que le bouton <b>Créer une entrée brouillon</b> ait été cliqué. Ensuite, le statut de la fiche de paie passera à <em>Fait</em>.</p>
</div>

Les fiches de paie peuvent être imprimées en cochant la case à côté de chaque
fiche de paie à imprimer ou en cochant la case située à côté de **Référence**
pour sélectionner toutes les fiches de paie en une seule fois. Cliquez sur le
bouton **Imprimer** et un fichier PDF sera créé avec toutes les fiches de paie
spécifiées.

![Le bouton Imprimer permettant d'imprimer les fiches de
paie.](../../../_images/print-payslips.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../payroll#payroll-work-entries-config"><span class="std std-ref">Configurer les prestations</span></a></p>
</div>

