# Listes de diffusion et listes noires

La création ou l’importation des listes de diffusion dans Konvergo ERP est très utile
pour diffuser du contenu à des groupes spécifiques de personnes qui partagent
déjà des données démographiques ou des intérêts similaires. Les listes de
diffusion sont également un excellent moyen de démarrer si une entreprise
migre d’un autre système et dispose déjà d’une audience établie.

De plus, le fait de permettre à un public de se « désabonner » des listes de
diffusion aide les entreprises à entretenir de bonnes relations avec leurs
clients, en donnant aux destinataires le pouvoir de contrôler ce qu’on leur
envoie (et ce qu’on ne leur envoie pas).

## Listes de diffusion

Dans l’application **SMS Marketing** , il existe une option dans le menu de
l’en-tête intitulée **Listes de diffusion**. Lorsqu’on clique dessus, un sous-
menu s’affiche avec des options pour les **Listes de diffusion** et les
**Contacts de la liste de diffusion**.

Cliquez sur Listes de diffusion ‣ Listes de diffusion pour obtenir une vue
d’ensemble de toutes les listes de diffusion de la base de données.

![Vue de la page principale des listes de diffusion par SMS dans l'application
Konvergo ERP SMS Marketing.](../../../../_images/mailing-list-main-page.png)

Pour modifier une liste existante, sélectionnez la liste souhaitée sur la page
des **listes de diffusion** et effectuez vos modifications.

Pour créer une nouvelle liste de diffusion, cliquez sur **Créer** dans le coin
supérieur gauche de la page des **Listes de diffusion**. Un modèle de liste de
diffusion vierge s’affichera.

![Vue de la fenêtre contextuelle de la liste de diffusion dans Konvergo ERP SMS
Marketing.](../../../../_images/sms-mailing-list-popup.png)

Donnez d’abord un nom à la **Liste de diffusion** et activez l’option **Est
public** pour rendre la liste de diffusion accessible aux destinataires sur la
**Page de gestion des abonnements**. Les utilisateurs pourront ainsi mettre à
jour leurs préférences d’abonnement à tout moment.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il n’est pas obligatoire de cocher la case <b>Est public</b>, mais c’est recommandé pour entretenir de bonnes relations avec vos clients.</p>
</div>

Une fois ces champs activés, cliquez sur **Créer** pour finaliser le
formulaire. Ensuite, la toute nouvelle liste de diffusion sera accessible dans
le tableau de bord principal des **Listes de diffusion**.

Pour continuer à modifier ou personnaliser la liste de diffusion, sélectionnez
le formulaire de liste de diffusion sur la page principale des **Listes de
diffusion** pour faire apparaître le formulaire détaillé de la liste.

En haut du formulaire détaillé de la liste de diffusion, plusieurs boutons
intelligents analytiques affichent des statistiques pour différentes mesures
liées à la liste de diffusion (par ex. **Destinataires** , **Mailings** ,
etc.).

Pour consulter ou modifier l’un de ces éléments, cliquez sur le bouton
intelligent souhaité pour afficher une page séparée contenant plus de données
liées à la liste de diffusion.

Pour modifier la liste de diffusion elle-même, cliquez sur le bouton
**Modifier** dans le coin supérieur gauche du formulaire détaillé de la liste
de diffusion.

![Vue du formulaire de modèle de la liste de diffusion dans Konvergo ERP SMS
Marketing.](../../../../_images/sms-mailing-list.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>N’oubliez pas de cliquer sur <b>Enregistrer</b> une fois tous les changements effectués.</p>
</div>

## Contacts de la liste de diffusion

Vous pouvez accéder aux informations de contact d’une ou plusieurs listes de
diffusion en allant à Listes de diffusion ‣ Contacts de la liste de diffusion
pour afficher un tableau de bord contenant tous les contacts liés à une ou
plusieurs des listes de diffusion configurées dans la base de données.

![Vue de la page des contacts de la liste de diffusion dans l'application Konvergo ERP
SMS Marketing.](../../../../_images/mailing-list-contacts-page.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Par défaut, Konvergo ERP affiche la page des <b>Contacts de la liste de diffusion</b> avec le filtre <b>Exclure les téléphones mis sur liste noire</b> activé dans la barre de recherche. Par conséquent, il n’affiche que les informations de contact des destinataires qui souhaitent toujours recevoir des communications et des mailings.</p>
</div>

### Historique des communications dans le chatter

Un enregistrement accessible de chaque mailing envoyé est conservé dans le
_chatter_ de chaque destinataire, situé sous le formulaire de contact du
destinataire (dans l’application _Contacts_).

Les utilisateurs de la base de données peuvent consulter le chatter pour
garder facilement une trace des communications ou voir l’historique des
interactions avec les contacts et les prospects.

Par exemple, les représentants commerciaux peuvent utiliser le chatter pour
savoir rapidement quelles promotions par SMS un client donné a reçues (ou
non).

![Vue du chatter dans l'application Konvergo ERP Contacts.](../../../../_images/sms-
marketing-chatter.png)

## Liste noire

Konvergo ERP _SMS Marketing_ dispose d’une fonctionnalité de **Liste noire** qui
permet aux destinataires d’ajouter leur numéro de téléphone à une liste de
personnes qui ne souhaitent plus recevoir de communications ou de mailings.

Cette fonctionnalité est également connue comme le processus de désabonnement
: les clients seront automatiquement ajoutés à une _liste noire_ s’ils
cliquent sur **Se désabonner** sur leur page de **Gestion des abonnements**.
Les clients peuvent également être ajoutés manuellement à la liste noire si
nécessaire.

Pour voir l’ensemble des numéros sur liste noire, allez à l’application SMS
Marketing ‣ Configuration ‣ Numéros de téléphone sur liste noire pour afficher
un tableau de bord contenant chaque numéro de téléphone sur liste noire dans
la base de données.

![Menu de la liste noir de SMS dans l'application.](../../../../_images/sms-
blacklist-menu.png)

Pour ajouter manuellement un numéro à la liste noire, cliquez sur le bouton
**Créer** dans le coin supérieur gauche de ce tableau de bord et saisissez le
numéro de téléphone sur le formulaire de la page suivante. Il y a également
une case à cocher pour indiquer si ce numéro de téléphone est **actif** (ou
non).

![Menu de la liste noir de SMS dans l'application.](../../../../_images/sms-
blacklist-create.png)

Une fois le formulaire complété, cliquez sur **Enregistrer** pour l’ajouter à
la liste des **Numéros de téléphone sur liste noire**. Pour supprimer un
numéro de la liste noire, sélectionnez le numéro souhaité dans le tableau de
bord et cliquez sur **Supprimer de la liste noire** sur le formulaire du
numéro de téléphone.

### Importer des listes noires

Lors d’une migration de logiciel/plateforme, il est possible d’importer une
liste noire de contacts déjà existante. Il s’agit des clients qui ont déjà
demandé à figurer sur la liste noire des envois de SMS.

Pour ce faire, allez à l’application SMS Marketing ‣ Configuration ‣ Numéros
de téléphone sur liste noire, sélectionnez le menu déroulant **Favoris** (sous
la barre de recherche) et cliquez sur **Importer des enregistrements**.

![Vue de comment importer une liste noire dans Konvergo ERP SMS
Marketing.](../../../../_images/import-blacklist.png)

  *[SMS]: Short Message Service

