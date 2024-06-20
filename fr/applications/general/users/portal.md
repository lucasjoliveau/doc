# Accès au portail

L’accès au portail est accordé aux utilisateurs qui ont besoin de visualiser
certains documents ou informations dans une base de données Odoo.

Parmi les cas d’utilisation courants de l’accès au portail, on peut citer le
fait de permettre aux clients de lire/visualiser l’un ou l’autre ou l’ensemble
des éléments suivants dans Odoo :

  * pistes/opportunités

  * devis/commandes clients

  * bons de commande

  * factures clients & factures fournisseurs

  * projets

  * tâches

  * feuilles de temps

  * tickets

  * signatures

  * abonnements

Note

Les utilisateurs du portail disposent d’un accès en lecture/visualisation et
ne peuvent pas modifier les documents de la base de données.

## Donner un accès au portail aux clients

À partir du tableau de bord d’Odoo, sélectionnez l’application Contacts. Si le
contact n’est pas encore créé dans la base de données, cliquez sur le bouton
Créer, saisissez les détails du contact et cliquez sur Enregistrer. Sinon,
choisissez un contact existant et cliquez sur le menu déroulant Action situé
en haut au centre de l’interface.

![Utiliser l'application Contacts pour donner accès au portail aux
utilisateurs.](../../../_images/grant-portal-access.png)

Sélectionnez ensuite Donner accès au portail. Une fenêtre contextuelle
apparaît et affiche trois champs :

  * Contact : le nom du contact enregistré dans la base de données d’Odoo

  * Email : l’adresse email du contact utilisée pour se connecter au portail

  * Au portail : si l’utilisateur a accès au portail ou pas

Pour accorder accès au portail, saisissez d’abord l”Email que le contact
utilisera pour se connecter au portail. Cochez ensuite la cause dans la
colonne Au portail. Vous pouvez optionnellement ajouter le texte du message
d’invitation que le contact recevra. Cliquez ensuite sur Appliquer pour
terminer.

![Une adresse email et la case à cocher correspondante pour le contact doivent
être complétées avant d'envoyer une invitation au
portail.](../../../_images/add-contact-to-portal.png)

Un email sera envoyé à l’adresse email précisé, indiquant que le contact est à
présent un utilisateur du portail pour cette base de données Odoo.

Astuce

Pour accorder l’accès au portail à plusieurs utilisateurs en une fois, allez à
la fiche contact d’une entreprise, cliquez ensuite sur:menuselection:`Action
--> Donner accès au portail` pour afficher la liste de tous les contacts liés
à cette entreprise. Cochez la case dans la colonne Au portail pour tous les
contacts qui doivent accéder au portail et cliquez sur Appliquer.

Note

L’accès au portail peut être révoqué à tout moment en allant au contact, en
cliquant sur Action ‣ Donner accès au portail, et en décochant ensuite la case
à cocher dans la colonne Au portail et en cliquant sur Appliquer.

## Changer le nom d’utilisateur du portail

Il se peut qu’un utilisateur du portail souhaite modifier son nom
d’utilisateur. Cette opération peut être effectuée par n’importe quel
utilisateur de la base de données ayant des droits d’accès d’administrateur.
La procédure suivante décrit les étapes nécessaires pour modifier le nom
d’utilisateur du portail.

Pour plus d'infos

[Consultez la documentation relative à la configuration des droits
d’accès](access_rights.html).

Allez d’abord à l’application Paramètres ‣ utilisateurs. Ensuite, dans le menu
Filtres, sélectionnez Utilisateur du portail, ou sélectionnez Ajouter un
filtre personnalisé et définissez la configuration suivante : Groupes >
contient > `portail`. Après avoir effectué cette sélection, recherchez (et
ouvrez) l’utilisateur du portail qui doit être modifié.

Ensuite, cliquez sur Modifier (le cas échéant), cliquez sur le champ Adresse
email et effectuez les modifications nécessaires à ce champ. Le champ Adresse
email est utilisé pour se connecter au portail Odoo.

Note

Changer l”Adresse email (ou login) modifie uniquement le _nom d’utilisateur_
sur le login du portail du client.

Pour changer l’email du contact, ce changement doit être effectué sur le
modèle du contact dans l’application _Contacts_. Le client peut également
modifier son adresse email directement à partir du portail, mais le login ne
peut **pas** être modifié. Consultez Modifier les données du client.

## Changements du portail client

Il se peut que le client souhaite modifier ses coordonnées, son mot de
passe/sécurité ou les informations de paiement liées à son compte de portail.
Le client peut effectuer ses modifications à partir de son portail. La
procédure suivante montre comment un client peut modifier ses coordonnées.

### Changer les coordonnées du client

Saisissez d’abord le nom d’utilisateur et le mot de passe (login) sur la page
de connexion à la base de données pour accéder au compte utilisateur du
portail. Un tableau de bord du portail s’ouvre après avoir réussi à se
connecter. Les documents du portail provenant des différentes applications
Odoo installées apparaîtront avec le nombre de documents pour chacune d’entre
elles.

Pour plus d'infos

Documentation relative à l’accès au portail.

Ensuite, allez au coin supérieur droit du portail et cliquez sur le bouton
Modifier, à côté de la section Détails. Modifiez ensuite les informations
pertinentes et cliquez sur Confirmer.

### Changer le mot de passe

Saisissez d’abord le nom d’utilisateur et le mot de passe (login) sur la page
de connexion à la base de données pour accéder au compte utilisateur du
portail. Un tableau de bord du portail s’ouvre après avoir réussi à se
connecter.

Si le client souhaite modifier son mot de passe pour accéder au portail,
cliquez sur le lien Modifier les paramètres de sécurité, dans la section
Sécurité du compte. Ensuite, effectuez les changements nécessaires en tapant
le Mot de passe actuel, le Nouveau mot de passe, et vérifiez le nouveau mot de
passe. Cliquez enfin sur Modifier le mot de passe pour terminer la
modification du mot de passe.

Note

Si un client souhaite modifier le login, comme il est indiqué ci-dessus,
contactez le point de contact de votre base de données Odoo. Consultez la
documentation susmentionnée relative au changement du nom d’utilisateur du
portail.

Note

Les mots de passe des utilisateurs du portail et des utilisateurs Odoo.com
restent distincts, même si la même adresse email est utilisée.

### Ajouter l’authentification à deux facteurs

Saisissez d’abord le nom d’utilisateur et le mot de passe (login) sur la page
de connexion à la base de données pour accéder au compte utilisateur du
portail. Un tableau de bord du portail s’ouvre après avoir réussi à se
connecter.

Si le client souhaite activer l’authentification à deux facteurs (2FA) pour
accéder au portail, cliquez sur le lien Modifier les paramètres de sécurité
dans la section Sécurité du compte.

Cliquez sur Activer l’authentification à deux facteurs pour activer la 2FA.
Confirmez ensuite le mot de passe actuel du portail dans le champ Mot de passe
et cliquez sur Confirmer le mot de passe. Activez ensuite 2FA dans une
application 2FA app (Google Authenticator, Authy, etc.), en scannant le code
QR ou en saisissant un Code de vérification.

Enfin, cliquez sur Activer l’authentification à deux facteurs pour finaliser
la configuration.

### Changer les informations de paiement

Saisissez d’abord le nom d’utilisateur et le mot de passe (login) sur la page
de connexion à la base de données pour accéder au compte utilisateur du
portail. Un tableau de bord du portail s’ouvre après avoir réussi à se
connecter.

Si le client souhaite gérer les options de paiement, allez à Gérer les modes
de paiement dans le menu sur la droite. Ajoutez ensuite les nouvelles
informations de paiement et sélectionnez Ajouter une nouvelle carte.

  *[2FA]: authentification à deux facteurs

