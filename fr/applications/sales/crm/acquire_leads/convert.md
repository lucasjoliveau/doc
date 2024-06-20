# Convertir des pistes en opportunités

Les _pistes_ constituent des étapes de qualification avant la création d’une
opportunité. Cela permet de gagner du temps avant qu’une opportunité
potentielle ne soit attribué à un vendeur.

## Configuration

Pour activer le paramètre des _pistes_ , allez à l’application CRM ‣
Configuration ‣ Paramètres et cochez la case à côté de Pistes. Cliquez ensuite
sur Enregistrer.

![Paramètre des pistes sur la page de configuration
CRM.](../../../../_images/convert-leads-leads-setting.png)

L’activation de cette fonctionnalité ajoute un nouveau menu, Pistes, à la
barre de menu en haut de l’écran.

![Le menu des pistes dans l'application CRM.](../../../../_images/convert-
leads-leads-menu.png)

Une fois que le paramètre des _Pistes_ a été activé, il s’applique à toutes
les équipes commerciales par défaut. Pour désactiver les pistes pour une
équipe spécifique, allez à l’application CRM ‣ Configuration ‣ Équipes
commerciales. Puis, sélectionnez une équipe dans la liste pour ouvrir
l’enregistrement et décochez la case Pistes. Une fois que vous avez terminé,
cliquez sur Enregistrer.

![Le menu des pistes dans l'application CRM.](../../../../_images/convert-
leads-leads-button.png)

## Convertir une piste en opportunité

Pour convertir une piste en _opportunité_ , allez à CRM ‣ Pistes, et cliquez
sur une Piste dans la liste pour l’ouvrir.

Dans le coin supérieur gauche de l’écran, cliquez sur le bouton Convertir en
opportunité, ce qui ouvre une fenêtre contextuelle Convertir en opportunité.

![Le bouton Créer une opportunité sur l'enregistrement d'une
piste.](../../../../_images/convert-leads-convert-opp-button.png)

Dans la fenêtre contextuelle Convertir en opportunité, dans le champ Action de
conversion, sélectionnez l’option Convertir en opportunité.

Note

Si une poste ou une opportunité existe déjà dans la base de données pour ce
client, Odoo suggère automatiquement de fusionner les deux
pistes/opportunités. Pour plus d’informations sur la fusion des pistes et des
opportunités, consultez la section sur la façon de fusionner les pistes ci-
dessous.

Sélectionnez ensuite un Vendeur et une Équipe commerciale auxquels
l’opportunité doit être assignée.

Si la piste est déjà assignée à un vendeur ou à une équipe, ces champs sont
remplis automatiquement avec ces informations.

![Fenêtre contextuelle permettant de créer une
opportunité.](../../../../_images/convert-leads-conversion-action.png)

Dans la section Client, vous pouvez choisir entre les options suivantes :

  * Créer un nouveau client : Choisissez cette option pour utiliser les informations de la piste pour créer une nouveau client.

  * Lier à un client existant : Choisissez cette option, puis sélectionnez un client dans le menu déroulant afin de lier cette opportunité à l’enregistrement d’un client existant.

  * Ne pas lier à un client : Choisissez cette option pour convertir la piste, mais ne pas la lier à un nouveau client ou à un client existant.

Enfin, lorsque toutes les configurations sont terminées, cliquez sur Créer une
opportunité.

## Fusionner des pistes et des opportunités

Odoo détecte automatiquement les pistes et opportunités similaires en
comparant les adresses email des contacts associés. Si une piste/opportunité
similaire est trouvée, un bouton intelligent Piste similaire s’affiche en haut
de l’enregistrement de la piste/de l’opportunité.

![Bouton intelligent des pistes similaires.](../../../../_images/convert-
leads-similar-leads.png)

Pour comparer les détails des pistes/opportunités similaires, cliquez sur le
bouton Pistes similaires. Cette action fait apparaître une vue kanban
contenant seulement les pistes/opportunités similaires. Cliquez sur chaque
carte pour afficher les détails de chaque piste/opportunité, et confirmez si
elles doivent être fusionnées.

Important

Lors de la fusion, Odoo privilégie la piste/l’opportunité qui a été créée en
premier lieur dans le système, fusionnant les informations dans la
piste/l’opportunité créée en premier. Cependant, si une piste et une
opportunité sont fusionnées, l’enregistrement résultant est intitulé
opportunité, quel que soit l’enregistrement créé en premier.

Après avoir confirmé que les pistes/opportunités doivent être fusionnées,
revenez à la vue kanban à l’aide du fil d’Ariane ou en cliquant sur le bouton
intelligent Piste similaire. Cliquez sur l’icône ☰ (trois lignes verticales)
pour passer à la vue de liste.

Cochez la case à gauche de la page pour les pistes/opportunités à fusionner.
Cliquez ensuite sur l’icône d’engrenage Action ⚙️ en haut de la page pour
afficher un menu déroulant. Dans ce menu déroulant, sélectionnez l’option
Fusionner pour fusionner les opportunités (ou pistes) sélectionnées.

Lorsque vous sélectionnez Fusionner dans le menu déroulant Action ⚙️
(engrenage), une fenêtre contextuelle Fusionner. Dans cette fenêtre
contextuelle, décidez d”Assigner des opportunités à un Vendeur et/ou à une
Équipe commerciale.

Sous ces champs, les pistes/opportunités à fusionner sont répertoriées, ainsi
que les informations y relatives. Pour fusionner ces pistes/opportunités,
cliquez sur Fusionner.

Note

Lors de la fusion d’opportunités, aucune information n’est perdue. Les données
de l’autre opportunité sont enregistrées dans le chatter et les champs
d’informations pour référence.

![Option Fusionner dans le menu d'action de la vue de
liste.](../../../../_images/convert-leads-merge.png)

