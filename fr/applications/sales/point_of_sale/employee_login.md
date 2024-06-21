# Gestion de plusieurs employés

Konvergo ERP Point de Vente vous permet de gérer l’accès à un PdV spécifique en
activant la fonctionnalité **Plusieurs employés par session**. Une fois
activée, vous pouvez sélectionner les utilisateurs qui peuvent se connecter au
PdV et garder une trace des employés impliqués dans chaque commande.

## Configuration

[Accédez aux paramètres du PdV](configuration#configuration-settings) et
sélectionnez votre PdV, ou cliquez sur le bouton d’ellipse vertical (**⋮**)
sur une carte PdV et cliquez sur **Modifier**. Ensuite, activez la
fonctionnalité **Plusieurs employés par session** et ajoutez les employés
autorisés dans le champ **Employés autorisés**.

![Paramètre pour activer plusieurs caissiers dans le
PdV](../../../_images/setting.png)

## Application dans la pratique

Une fois la fonctionnalité activée, les caissiers peuvent se connecter en
scannant leur badge ou en sélectionnant leur nom dans la liste des employés
autorisés pour [ouvrir la session](../point_of_sale#pos-session-start).

![Fenêtre pour ouvrir une session avec la fonctionnalité des plusieurs
caissiers activée](../../../_images/open-session.png)

Pour passer à un autre utilisateur [dans une session
ouverte](../point_of_sale#pos-session-start), cliquez sur le nom de
l’employé dans le coin supérieur droit de l’écran et sélectionnez l’employé
auquel vous voulez passer dans la liste.

![Bouton pour passer d'un caissier à un autre.](../../../_images/switch-
user.png)

Vous pouvez également demander à vos employés de saisir un code pin chaque
fois qu’ils se connectent à un PdV pour les empêcher de se connecter en tant
que quelqu’un d’autre. Pour définir le code, allez à l’application
**Employés** , ouvrez la fiche de l’employé et cliquez sur l’onglet
**Paramètres RH**. Ensuite, saisissez le code pin de votre choix dans le champ
**Code PIN** de la catégorie **Présence/Point de Vente**.

![Paramètre sur la fiche de l'employé pour assigner l'ID du badge et le code
PIN.](../../../_images/pin-and-badgeid.png)

### Se connecter à l’aide de badges

Pour que vos employés puissent se connecter en scannant leur badge, il faut
leur assigner un ID de badge. Pour ce faire, allez à l’application
**Employés** , ouvrez la fiche de l’employé et cliquez sur l’onglet
**Paramètres RH**. Ensuite, saisissez l’ID de badge de votre choix dans le
champ **ID bu badget** de la catégorie **Présence/Point de Vente** ou cliquez
sur **Générer**.

Pour passer à un autre utilisateur, verrouillez la session en cliquant sur
l’icône en forme de cadenas (**🔓**) dans le coin supérieur droit de l’écran et
scannez votre badge.

## Rapports analytiques

Une fois que vous avez fermé et enregistré la session du PdV, accédez au
rapport détaillée pour passer en revue toutes les activités de la session, y
compris le nom de la personne qui a lancé la session et celui de la personne
qui a géré des commandes spécifiques. Pour accéder au rapport de la session,
cliquez sur le bouton d’ellipse vertical (**⋮**) sur la carte PdV et
sélectionnez **Sessions** dans la section **Vue**. Ensuite, sélectionnez une
session spécifique pour obtenir des informations plus détaillées et cliquez
sur le bouton **Commandes** pour voir la liste de toutes les commandes passées
au cours de cette session.

Pour obtenir une vue d’ensemble de toutes les commandes, quelle que soit la
session, cliquez sur le bouton d’ellipse vertical (**⋮**) de la carte PdV et
sélectionnez **Commandes** dans la section **Vue**.

