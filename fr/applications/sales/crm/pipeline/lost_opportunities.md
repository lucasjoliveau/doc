# Gérer des opportunités perdues

Toutes les opportunités ne débouchent pas sur des ventes. Pour maintenir le
pipeline à jour, les opportunités perdues doivent être identifiées. Préciser
la raison pour laquelle une opportunité a été perdue permet d’obtenir des
informations supplémentaires qui peuvent s’avérer utiles pour les opportunités
futures.

## Marquer une piste comme perdue

Pour marquer une piste comme perdue, ouvrez l’application CRM et sélectionnez
une piste dans le pipeline en cliquant sur sa carte kanban correspondante. La
fiche détaillée de cette piste s’affiche alors.

Cliquez ensuite sur Perdu, situé en haut de la fiche détaillée de la piste.

![Boutons situés en haut d'un enregistrement d'opportunité avec le bouton
perdu mis en évidence.](../../../../_images/lost-opps-lost-button.png)

Cela ouvre la fenêtre contextuelle Motif de perte. Dans le menu déroulant,
choisissez un motif de perte existant. Si aucun motif applicable n’est
disponible, créez-en un nouveau en saisissant le champ Motif de la perte et en
cliquant sur Créer.

Vous pouvez ajouter des notes additionnelles et des commentaires sous le motif
de la perte dans le champ Motif de la perte.

Lorsque toutes les informations souhaitées ont été saisies dans la fenêtre
contextuelle Motif de la perte, cliquez sur Soumettre.

![Fenêtre contextuelle des motifs de perte avec des
exemples.](../../../../_images/lost-opps-lost-reason.png)

Lorsque vous cliquez sur Soumettre, la fenêtre contextuelle se ferme et Odoo
revient au formulaire détaillé de la piste, où figure à présent une nouvelle
bannière rouge Perdu dans le coin supérieur droit de la piste.

## Créer/modifier des motifs de perte

Pour créer un nouveau motif de perte ou modifier un motif existant, allez à
l’application CRM ‣ Configuration ‣ Motifs de perte.

Pour modifier un motif existant, cliquez sur le motif qui doit être modifié.
Une fois cliqué, le motif est mis en surbrillance. Une fois en surbrillance,
modifiez la description du motif de perte sélectionné en modifiant le champ
Description. Lorsque vous avez terminé, cliquez sur Enregistrer dans le coin
supérieur gauche.

Pour créer un nouveau motif de perte, cliquez sur Créer dans le coin supérieur
gauche de la page Motifs de perte. Cette opération fait apparaître une
nouvelle ligne vierge dans le champ Description. Saisissez ensuite le nouveau
motif de perte dans cette nouvelle ligne. Une fois que vous avez terminé,
cliquez sur Enregistrer.

## Récupérer des opportunités perdues

Pour récupérer les opportunités perdues dans Odoo _CRM_ , ouvrez l’application
CRM et le tableau de bord principal du Pipeline. Cliquez ensuite sur le menu
déroulant Filtres, situé en-dessous de la barre de recherche.

![Barre de recherche avec le filtre de perte mis en
évidence.](../../../../_images/lost-opps-lost-filter.png)

Dans le menu déroulant Filtres, sélectionnez l’option Perdu. Lorsque vous
sélectionnez l’option Perdu, seules les pistes qui ont été marquées comme
`Perdues` apparaissent sur la page Pipeline.

Pour filtrer les pistes par motif de perte spécifique, sélectionnez Filtres ‣
Ajouter un filtre personnalisé. Cette opération fait apparaître un autre menu
déroulant avec trois champs.

Dans le menu déroulant du champ supérieur, sélectionnez Motif de perte. Dans
le menu déroulant du deuxième champ, sélectionnez Contient. Puis, dans le
troisième champ du sous-menu Ajouter un champ personnalisé, saisissez le ou
les mots-clés spécifiques. Enfin, cliquez sur Appliquer. Lorsque vous cliquez
sur Appliquer, Odoo montre toutes les pistes perdues avec un motif qui
contient ce ou ces mots-clés.

![Barre de recherche avec filtre personnalisé ajouté pour le motif de
perte.](../../../../_images/lost-opps-lost-custom-filter.png)

## Restaurer des opportunités perdues

Pour restaurer une opportunité perdue, allez au tableau de bord principal
Pipeline de l’application _CRM_ , ouvrez le menu déroulant Filtres et
sélectionnez l’option Perdu. Cette opération fait apparaître toutes les
opportunités perdues sur la page Pipeline.

Cliquez ensuite sur la carte kanban de l’opportunité perdue souhaitée à
restaurer, ce qui ouvre le formulaire détaillé de cette piste.

Sur le formulaire détaillé de la piste perdue, cliquez sur Restaurer dans le
coin supérieur gauche. Ceci supprime la bannière rouge Perdu du formulaire de
piste, ce qui signifie que la piste a été restaurée.

![Opportunité perdue avec le bouton Restaurer mis en
évidence.](../../../../_images/lost-opps-restore.png)

### Restaurer plusieurs opportunités simultanément

Pour restaurer plusieurs opportunités en même temps, allez au tableau de bord
principal Pipeline de l’application _CRM_ , ouvrez le menu déroulant Filtres
et sélectionnez l’option Perdu.

Sélectionnez ensuite l’option vue de liste, représentée par l’icône de trois
lignes ☰ (liste) dans le coin supérieur droit.. Toutes les pistes de la page
Pipeline s’affichent alors dans un formulaire de liste. Une fois le formulaire
de liste sélectionné, cochez la case à gauche de chaque opportunité/piste
sélectionnée à restaurer.

Une fois que les opportunités/pistes souhaitées ont été sélectionnées, cliquez
sur le menu déroulant ⚙️ Action (engrenage) en haut de la page Pipeline. Dans
le menu déroulant ⚙️ Action (engrenage), sélectionnez Désarchiver.

Vous supprimez ainsi les opportunités perdues ainsi sélectionnées de la page
du Pipeline, car elles ne correspondent plus aux critères de filtre `Perdu`.
Pour révéler ces pistes nouvellement restaurées, supprimez le filtre `Perdu`
de la barre de recherche.

![Bouton d'action de la vue de liste avec l'option Désarchiver mise en
évidence.](../../../../_images/lost-opps-unarchive.png)

Pour plus d'infos

[Contrôler votre ratio gain/perte](../performance/win_loss.html)

