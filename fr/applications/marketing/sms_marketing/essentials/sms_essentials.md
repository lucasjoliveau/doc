# Les essentiels de SMS

L’utilisation de SMS dans les stratégies de communication peut aider les
entreprises à étendre leur marché, en particulier dans certains pays où les
emails ne sont pas très courants ou ne sont pas utilisés.

L’application _SMS Marketing_ d’Odoo peut également aider à augmenter les taux
de conversion autour d’actions de valeur, telles que les inscriptions à des
événements, les essais gratuits, les achats, etc., puisque les canaux de
marketing basés sur le texte et le mobile génèrent généralement des résultats
plus élevés en termes de CTOR et CTR.

## Tableau de bord du SMS Marketing

Lorsque l’application est ouverte, Odoo affiche le tableau de bord principal
du SMS Marketing, qui présente les différents mailings SMS qui ont été créés,
ainsi que les informations et données pertinentes liées à ce message
spécifique.

La vue Kanban est la vue par défaut utilisée par Odoo lorsque l’application
est ouverte et fournit un affichage organisé des mailings SMS qui ont été
créés, ainsi que de leur statut actuel.

Note

Un mailing de SMS peut avoir le statut suivant : Brouillon, Dans la file
d’attente, En cours d’envoi ou Envoyé.

Dans le coin supérieur droit du tableau de bord principal du SMS Marketing,
vous avez le choix entre différentes options d’affichage. Chacune d’entre
elles offre un point de vue unique sur les mêmes informations relatives au
SMS.

La vue Liste fournit les mêmes données utiles relatives aux mailings SMS, mais
dans une présentation de liste plus traditionnelle.

La vue Caldendrier propose un simple calendrier, qui permet de voir quand les
mailings SMS seront envoyés (ou ont été envoyés). Si une date future est
sélectionnée, Odoo ouvre un modèle de SMS vierge qui, une fois complété, sera
programmé pour être envoyé à cette date spécifique.

Enfin, la vue Graphique permet de visualiser les mêmes données relatives aux
SMS sous forme de graphiques et diagrammes. Odoo propose également plusieurs
façons de trier et de regrouper les données permettant une analyse plus
détaillée.

## Créer des SMS

Pour commencer, cliquez sur Créer sur le tableau de bord principal du SMS
Marketing et Odoo ouvre un modèle de formulaire de SMS vierge, qui peut être
configuré de différentes manières.

![Créer un modèle de SMS Marketing.](../../../../_images/sms-create.png)

Tout d’abord, donnez un Sujet au mailing, qui décrit le sujet du mailing.

Ensuite, dans le champ Destinataires, choisissez à qui ce SMS sera envoyé. Par
défaut, Odoo sélectionne une Lste de diffusion. Si c’est l’option souhaitée
dans le champ Destinataires, précisez quelle liste de diffusion à laquelle
Odoo doit envoyer ce SMS dans le champ Sélectionner une liste de diffusion.

Note

Pour créer (ou modifier) une liste de diffusion, allez à Listes de diffusion ‣
Listes de diffusion. Odoo y affiche toutes les listes de diffusion
précédemment créées, ainsi que divers types de données liées à cette liste
spécifique (par ex. nombre de contacts, d’envois, de destinataires, etc.).

To learn more about mailing lists and contacts, check out [Listes de diffusion
et listes noires](mailing_lists_blacklists.html).

![Vue de la page des listes de diffusion dans l'application SMS
Marketing.](../../../../_images/sms-mailing-list1.png)

Pour révéler toutes les options possibles dans le champ Destinataires, cliquez
sur le champ pour voir tous les choix que Odoo met à disposition.

Lorsqu’un champ différent (autre que Liste de diffusion) est sélectionné,
l’option de préciser davantage le champ choisi devient disponible — soit avec
une équation de filtre de destinataire par défaut qui apparaît automatiquement
(qui peut être personnalisée pour s’adapter à tout besoin d’entreprise) ou,
s’il n’y a aucune équation de filtre de destinataire par défaut, un bouton
Ajouter un filtre apparaîtra.

En cliquant sur le bouton Ajouter un filtre, vous accédez à des champs de
règles de domaine entièrement personnalisables, qui peuvent être configurés de
la même manière qu’une équation. Vous pouvez créer plusieurs règles de
destinataire, le cas échéant.

Par conséquent, Odoo enverra uniquement le SMS aux destinataires qui
correspondent aux critères configurés dans ces champs. Il est possible
d’ajouter plusieurs règles.

Example

Si vous choisissez Contact, tous les enregistrements dans _Contacts_ dans la
base de données Odoo (fournisseurs, clients, etc.) recevront le SMS par défaut
— sauf si des règles de destinataire plus précises sont ajoutées.

Par exemple, le message suivant sera uniquement envoyé aux contacts dans la
base de données qui sont situés aux États-Unis (par ex. `Pays` > `Nom du pays`
est égal à `États-Unis`) et qui ne se sont mis sur liste noire (par ex. `Liste
noire` > `est` > `non défini`).

![Destinataires dans SMS Marketing.](../../../../_images/contact-
recipient.png)

### Écrire des SMS

Saisissez le contenu du SMS dans le champ de texte dans l’onglet Contenu du
SMS. Il est également possible d’inclure des liens et des émojis. Sous le
champ de texte, Odoo affiche le nombre de caractères utilisés dans le message,
ainsi que le nombre de SMS nécessaires pour délivrer le message complet.

Astuce

Pour vérifier le prix de l’envoi d’un SMS pour un pays, cliquez sur l’icône
Informations.

![Icône de vérification du prix du SMS.](../../../../_images/sms-price-
check.png)

Note

Il est nécessaire d’acheter des crédits dans Odoo pour pouvoir utiliser
l’application _SMS Marketing_ ; les SMS ne seront pas envoyés sans crédits.

Pour plus d'infos

[Odoo SMS - FAQ](https://iap-services.odoo.com/iap/sms/pricing)

### Liens trackés dans les SMS

Lorsque des liens sont utilisés dans les SMS, Odoo génère automatiquement des
trackers de liens pour collecter des données analytiques et des mesures
relatives à ces liens, alors disponibles via Configuration ‣ Tracker de liens.

![Page du tracker de liens de SMS.](../../../../_images/sms-link-tracker.png)

## Modifier les paramètres du SMS

Dans l’onglet Paramètres d’un modèle de SMS, une option permet d”Inclure un
lien de désinscription. Si elle est activée, le destinataire est en mesure de
se désabonner de la liste de diffusion pour ainsi éviter tout mailing
ultérieur.

Un employé peut être désigné comme Responsable dans la section Suivi de
l’onglet Paramètres.

![L'onglet Paramètres du SMS.](../../../../_images/sms-settings-tab.png)

## Envoyer des SMS

Une fois qu’un mailing est créé, choisissez quand Odoo doit envoyer le message
parmi les options suivantes :

  * Envoyer : envoie le message immédiatement. Envisagez d’utiliser cette option si la liste des destinataires est très limitée ou dans les cas qui impliquent des délais très rapprochés, comme une « vente flash ».

  * Planifier : choisissez un jour (et une heure) pour que Odoo envoie le mailing. C’est généralement la meilleure option pour les mailings liés à un événement spécifique. Une telle méthode peut être utilisée pour promouvoir une offre limitée dans le temps ou pour aider à planifier à l’avance la stratégie de contenu d’une entreprise.

  * Tester : permet d’envoyer un SMS à un ou plusieurs numéros à des fins de test. N’oubliez pas d’utiliser une virgule entre les numéros de téléphone si plusieurs numéros sont utilisés comme destinataires.

## Visualiser vos rapports

Sur la page d”Analyse (accessible via l’option Analyse dans le menu d’en-
tête), il est possible d’appliquer différentes combinaisons de Filtres et de
Mesures pour afficher des métriques dans un certain nombre de représentations
différentes (par ex. les vues Graphique, Liste et Cohorte).

Chaque option d’affichage des mesures d”Analyse permet d’analyser en détail
les performances des SMS.

Par exemple, dans la vue Graphique par défaut, les données des SMS sont
affichées sous forme de graphiques et diagrammes, qui peuvent être triés et
regroupés de différentes manières (par ex. dans le menu déroulant Mesures).

![Page d'analyse dans SMS Marketing.](../../../../_images/sms-reporting-
page.png)

Astuce

SMS messages can be sent using automated actions in Odoo. Odoo _Studio_ is
required to use automated actions.

To install Odoo _Studio_ , go to Apps application. Then, using the Search…
bar, and search for `studio`.

If it is not already installed, click Install.

Adding the _Studio_ application upgrades the subscription status to _Custom_ ,
which increases the cost. Consult [support](https://www.odoo.com/contactus),
or reach out to the database’s customer success manager, with any questions on
upgrading.

To use automated actions, navigate in [developer
mode](../../../general/developer_mode.html#developer-mode), to Settings app ‣
Technical menu ‣ Automation section ‣ Automated Actions. Then, click New to
create a new action.

Enter an Action Name, and select a Model to implement this action on.

Ensure the Active toggle is set to _on_ , represented by a full-green switch,
in order for the automated action to run.

Set the Trigger to either On Creation, On Update, On Creation & Update, On
Deletion, Based on Form Modification, or Based on Timed Condition.

Based on the selection for the Trigger, additional fields may populate.

Under the Apply on field, a record filter using a domain can be created.
Ensure a model has been selected before setting any domains on the Apply on
field. Click Edit Domain to set record parameters.

Under Action To Do drop-down field, select Send SMS Text Message. Next, set
the SMS Template, and choose whether the SMS message should be logged as a
note, by ticking the checkbox next to Log as Note.

![Automated action template with action to do, SMS template and log as note
highlighted.](../../../../_images/automated-action-sms.png)

To implement the automated action, save it; either by navigating away, or
manually saving it (using the ☁️ (cloud) icon).

Pour plus d'infos

  * [Paramètres de la campagne SMS](sms_campaign_settings.html)

  * [Listes de diffusion et listes noires](mailing_lists_blacklists.html)

  * [In-app purchases (IAP)](../../../essentials/in_app_purchase.html)

  *[SMS]: Short Message Service
  *[CTOR]: click-to-open rate ou taux de réactivité
  *[CTR]: click-through rate ou taux de clics

