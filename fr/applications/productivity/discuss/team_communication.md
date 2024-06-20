# Utiliser les canaux pour la communication d’équipe

Utilisez les canaux dans l’application _Discussion_ d’Odoo pour organiser des
discussions entre équipes individuelles, départements, projets ou tout autre
groupe qui nécessite une communication régulière. Grâce aux canaux, les
employés peuvent communiquer dans des espaces dédiés dans la base de données
Odoo à propos de sujets spécifiques, de mises à jour et des derniers
développements en rapport avec l’organisation.

## Canaux publics et privés

Un canal _public_ est visible par tout le monde, tandis qu’un canal _privé_
n’est visible que par les utilisateurs qui y sont invités. Pour créer un
nouveau canal, allez à l’application Discussion et cliquez sur l’icône ➕
(plus) à côté de l’en-tête Canaux dans le menu de gauche. Après avoir saisi le
nom du canal, deux options apparaissent : la première est un canal avec un
hashtag (`#`) pour indiquer qu’il s’agit d’un canal public ; la deuxième est
un canal avec une icône de verrouillage (`🔒`) pour indiquer qu’il s’agit d’un
canal privé. Sélectionnez le type de canal qui correspond le mieux à vos
besoins de communication.

![Vue de la barre latérale de discussion et d'un canal en cours de création
dans Odoo Discussion.](../../../_images/public-private-channel.png)

Astuce

Il est préférable d’utiliser un canal public lorsque de nombreux employés ont
besoin d’accéder à des informations (telles que les annonces de l’entreprise),
alors qu’un canal privé peut être utilisé chaque fois que les informations
doivent être limitées à des groupes spécifiques (comme un département
spécifique).

### Options de configuration

Le Nom du groupe, la Description, et les paramètres de Confidentialité du
canal peuvent être modifiés en cliquant sur les paramètres du canal,
représentés par une icône ⚙️ (engrenage) dans le menu latéral de gauche, à
côté du nom du canal.

![Vue des paramètres d'un canal dans Odoo
Discussion.](../../../_images/channel-settings.png)

#### Onglets Confidentialité et Membres

L’option Qui peut suivre les activités du groupe ? permet de contrôler quels
groupes ont accès au canal.

Note

Autoriser Tout le monde à suivre un canal privé permet aux autres utilisateurs
de le voir et de le rejoindre, comme ils le feraient pour un canal public.

Lorsque vous choisissez Personnes invitées uniquement, indiquez dans l’onglet
Membres les membres qui doivent être invités. Vous pouvez également inviter
des membres à partir du tableau de bord principal de l’application
_Discussion_ , en sélectionnant le canal, en cliquant sur l’icône _ajouter un
utilisateur_ dans le coin supérieur droit du tableau de bord et en cliquant
sur Inviter au canal une fois que tous les utilisateurs ont été ajoutés.

![Vue de l'option de Discussion d'inviter des membres dans Odoo
Discussion.](../../../_images/invite-channel.png)

Lorsque vous sélectionnez l’option Groupe d’utilisateurs sélectionné, vous
avez la possibilité d’ajouter un Groupe autorisé, ainsi que la possibilité
d”Abonner automatiquement les groupes et d”Abonner automatiquement des
départements.

L’option d”Abonner automatiquement des groupes ajoute automatiquement des
utilisateurs de ce groupe d’utilisateurs particulier en tant qu’abonnés. En
d’autres termes, tandis que l’option Groupes autorisés limite le nombre
d’utilisateurs qui peuvent accéder au canal, l’option Abonner automatiquement
des groupes ajoute automatiquement des utilisateurs en tant que membres tant
qu’ils font partie d’un groupe d’utilisateurs spécifique. Il en va de même
pour l’option Abonner automatiquement des départements.

## Barre de recherche rapide

Une fois qu’au moins 20 canaux, messages directes ou conversations de live
chat (si le module _Live Chat_ est installé sur la base de données) sont
épinglés dans la barre latérale, une barre de Recherche rapide… s’affiche.
C’est un moyen pratique de filtrer des conversations et de trouver rapidement
celle dont vous avez besoin.

![Vue de la barre latérale de Discussion mettant en évidence la barre de
recherche rapide dans Odoo Discussion.](../../../_images/quick-search.png)

### Trouver des canaux

Cliquez sur l’icône des paramètres ⚙️ (engrenage), située dans la barre
latérale de gauche, à droite de l’élément de menu rétractable CANAUX. Cette
opération permet d’afficher une mosaïque contenant tous les canaux publics
disponibles. Les utilisateurs peuvent rejoindre ou quitter les canaux sur cet
écran en cliquant sur les boutons REJOINDRE ou QUITTER qui apparaissent dans
les cases des canaux.

Il est également possible d’appliquer des critères de filtrage et de les
enregistrer pour plus tard. La fonction Rechercher… accepte les caractères
génériques en utilisant le caractère de soulignement [ `_` ], et des
recherches spécifiques peuvent être enregistrées en utilisant le menu
déroulant Favoris ‣ Enregistrer la recherche actuelle.

![Vue d'un canal recherché à travers des filtres dans Odoo
Discussion](../../../_images/filter.png)

## Lier un canal dans le chatter

Les canaux peuvent être liés dans le chatter (enregistrer une note) d’un
enregistrement dans Odoo. Pour ce faire, tapez simplement : `#` et le nom du
canal. Cliquez ou appuyez sur enter sur le nom du _canal_. Lors de
l’enregistrement de la note, un lien vers le canal apparaîtra. En cliquant sur
le lien, une fenêtre de discussion avec la conversation du canal s’affiche
dans le coin inférieur droit de l’écran.

Les utilisateurs peuvent contribuer à ce canal de groupe (soit public, soit
accessible aux membres) en écrivant des messages dans la fenêtre et appuyant
sur _enter_.

![Canal lié dans le chatter avec le canal ouvert dans le quadrant inférieur
droit.](../../../_images/chatter-channel.png)

Pour plus d'infos

  * [Discussion](../discuss.html)

  * [Activités](../../essentials/activities.html)

