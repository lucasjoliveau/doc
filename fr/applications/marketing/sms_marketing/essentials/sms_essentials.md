# Les essentiels de SMS

L’utilisation de SMS dans les stratégies de communication peut aider les
entreprises à étendre leur marché, en particulier dans certains pays où les
emails ne sont pas très courants ou ne sont pas utilisés.

L’application _SMS Marketing_ d’Konvergo ERP peut également aider à augmenter les taux
de conversion autour d’actions de valeur, telles que les inscriptions à des
événements, les essais gratuits, les achats, etc., puisque les canaux de
marketing basés sur le texte et le mobile génèrent généralement des résultats
plus élevés en termes de CTOR et CTR.

## Tableau de bord du SMS Marketing

Lorsque l’application est ouverte, Konvergo ERP affiche le tableau de bord principal
du **SMS Marketing** , qui présente les différents mailings SMS qui ont été
créés, ainsi que les informations et données pertinentes liées à ce message
spécifique.

La vue **Kanban** est la vue par défaut utilisée par Konvergo ERP lorsque
l’application est ouverte et fournit un affichage organisé des mailings SMS
qui ont été créés, ainsi que de leur statut actuel.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Un mailing de <abbr title="Short Message Service">SMS</abbr> peut avoir le statut suivant : <b>Brouillon</b>, <b>Dans la file d’attente</b>, <b>En cours d’envoi</b> ou <b>Envoyé</b>.</p>
</div>

Dans le coin supérieur droit du tableau de bord principal du **SMS Marketing**
, vous avez le choix entre différentes options d’affichage. Chacune d’entre
elles offre un point de vue unique sur les mêmes informations relatives au
SMS.

La vue **Liste** fournit les mêmes données utiles relatives aux mailings SMS,
mais dans une présentation de liste plus traditionnelle.

La vue **Caldendrier** propose un simple calendrier, qui permet de voir quand
les mailings SMS seront envoyés (ou ont été envoyés). Si une date future est
sélectionnée, Konvergo ERP ouvre un modèle de SMS vierge qui, une fois complété, sera
programmé pour être envoyé à cette date spécifique.

Enfin, la vue **Graphique** permet de visualiser les mêmes données relatives
aux SMS sous forme de graphiques et diagrammes. Konvergo ERP propose également
plusieurs façons de trier et de regrouper les données permettant une analyse
plus détaillée.

## Créer des SMS

Pour commencer, cliquez sur **Créer** sur le tableau de bord principal du
**SMS Marketing** et Konvergo ERP ouvre un modèle de formulaire de SMS vierge, qui
peut être configuré de différentes manières.

![Créer un modèle de SMS Marketing.](../../../../_images/sms-create.png)

Tout d’abord, donnez un **Sujet** au mailing, qui décrit le sujet du mailing.

Ensuite, dans le champ **Destinataires** , choisissez à qui ce SMS sera
envoyé. Par défaut, Konvergo ERP sélectionne une **Lste de diffusion**. Si c’est
l’option souhaitée dans le champ **Destinataires** , précisez quelle liste de
diffusion à laquelle Konvergo ERP doit envoyer ce SMS dans le champ **Sélectionner une
liste de diffusion**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour créer (ou modifier) une liste de diffusion, allez à Listes de diffusion ‣ Listes de diffusion. Konvergo ERP y affiche toutes les listes de diffusion précédemment créées, ainsi que divers types de données liées à cette liste spécifique (par ex. nombre de contacts, d’envois, de destinataires, etc.).</p>
<p>To learn more about mailing lists and contacts, check out <a href="mailing_lists_blacklists">Listes de diffusion et listes noires</a>.</p>
</div> ![Vue de la page des listes de diffusion dans
l'application SMS Marketing.](../../../../_images/sms-mailing-list1.png)

Pour révéler toutes les options possibles dans le champ **Destinataires** ,
cliquez sur le champ pour voir tous les choix que Konvergo ERP met à disposition.

Lorsqu’un champ différent (autre que **Liste de diffusion**) est sélectionné,
l’option de préciser davantage le champ choisi devient disponible — soit avec
une équation de filtre de destinataire par défaut qui apparaît automatiquement
(qui peut être personnalisée pour s’adapter à tout besoin d’entreprise) ou,
s’il n’y a aucune équation de filtre de destinataire par défaut, un bouton
**Ajouter un filtre** apparaîtra.

En cliquant sur le bouton **Ajouter un filtre** , vous accédez à des champs de
règles de domaine entièrement personnalisables, qui peuvent être configurés de
la même manière qu’une équation. Vous pouvez créer plusieurs règles de
destinataire, le cas échéant.

Par conséquent, Konvergo ERP enverra uniquement le SMS aux destinataires qui
correspondent aux critères configurés dans ces champs. Il est possible
d’ajouter plusieurs règles.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si vous choisissez <b>Contact</b>, tous les enregistrements dans <em>Contacts</em> dans la base de données Konvergo ERP (fournisseurs, clients, etc.) recevront le <abbr title="Short Message Service">SMS</abbr> par défaut — sauf si des règles de destinataire plus précises sont ajoutées.</p>
<p>Par exemple, le message suivant sera uniquement envoyé aux contacts dans la base de données qui sont situés aux États-Unis (par ex. <code>Pays</code> &gt; <code>Nom du pays</code> est égal à <code>États-Unis</code>) et qui ne se sont mis sur liste noire (par ex. <code>Liste noire</code> &gt; <code>est</code> &gt; <code>non défini</code>).</p>
<img alt="Destinataires dans SMS Marketing." class="align-center" src="../../../../_images/contact-recipient.png"/>
</div>

### Écrire des SMS

Saisissez le contenu du SMS dans le champ de texte dans l’onglet **Contenu du
SMS**. Il est également possible d’inclure des liens et des émojis. Sous le
champ de texte, Konvergo ERP affiche le nombre de caractères utilisés dans le message,
ainsi que le nombre de SMS nécessaires pour délivrer le message complet.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour vérifier le prix de l’envoi d’un <abbr title="Short Message Service">SMS</abbr> pour un pays, cliquez sur l’icône <b>Informations</b>.</p>
</div> ![Icône de vérification du prix du
SMS.](../../../../_images/sms-price-check.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est nécessaire d’acheter des crédits dans Konvergo ERP pour pouvoir utiliser l’application <em>SMS Marketing</em> ; les <abbr title="Short Message Service">SMS</abbr> ne seront pas envoyés sans crédits.</p>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://iap-services.odoo.com/iap/sms/pricing">Konvergo ERP SMS - FAQ</a></p>
</div>

### Liens trackés dans les SMS

Lorsque des liens sont utilisés dans les SMS, Konvergo ERP génère automatiquement des
trackers de liens pour collecter des données analytiques et des mesures
relatives à ces liens, alors disponibles via Configuration ‣ Tracker de liens.

![Page du tracker de liens de SMS.](../../../../_images/sms-link-tracker.png)

## Modifier les paramètres du SMS

Dans l’onglet **Paramètres** d’un modèle de SMS, une option permet d”**Inclure
un lien de désinscription**. Si elle est activée, le destinataire est en
mesure de se désabonner de la liste de diffusion pour ainsi éviter tout
mailing ultérieur.

Un employé peut être désigné comme **Responsable** dans la section **Suivi**
de l’onglet **Paramètres**.

![L'onglet Paramètres du SMS.](../../../../_images/sms-settings-tab.png)

## Envoyer des SMS

Une fois qu’un mailing est créé, choisissez quand Konvergo ERP doit envoyer le message
parmi les options suivantes :

  * **Envoyer** : envoie le message immédiatement. Envisagez d’utiliser cette option si la liste des destinataires est très limitée ou dans les cas qui impliquent des délais très rapprochés, comme une « vente flash ».

  * **Planifier** : choisissez un jour (et une heure) pour que Konvergo ERP envoie le mailing. C’est généralement la meilleure option pour les mailings liés à un événement spécifique. Une telle méthode peut être utilisée pour promouvoir une offre limitée dans le temps ou pour aider à planifier à l’avance la stratégie de contenu d’une entreprise.

  * **Tester** : permet d’envoyer un SMS à un ou plusieurs numéros à des fins de test. N’oubliez pas d’utiliser une virgule entre les numéros de téléphone si plusieurs numéros sont utilisés comme destinataires.

## Visualiser vos rapports

Sur la page d”**Analyse** (accessible via l’option Analyse dans le menu d’en-
tête), il est possible d’appliquer différentes combinaisons de **Filtres** et
de **Mesures** pour afficher des métriques dans un certain nombre de
représentations différentes (par ex. les vues **Graphique** , **Liste** et
**Cohorte**).

Chaque option d’affichage des mesures d”**Analyse** permet d’analyser en
détail les performances des SMS.

Par exemple, dans la vue **Graphique** par défaut, les données des SMS sont
affichées sous forme de graphiques et diagrammes, qui peuvent être triés et
regroupés de différentes manières (par ex. dans le menu déroulant
**Mesures**).

![Page d'analyse dans SMS Marketing.](../../../../_images/sms-reporting-
page.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>SMS messages can be sent using automated actions in Konvergo ERP. Konvergo ERP <em>Studio</em> is required to use
automated actions.</p>
<p>To install Konvergo ERP <em>Studio</em>, go to Apps application. Then, using the
<b>Search…</b> bar, and search for <code>studio</code>.</p>
<p>If it is not already installed, click <b>Install</b>.</p>
<p>Adding the <em>Studio</em> application upgrades the subscription status to <em>Custom</em>, which increases the
cost. Consult <a href="https://www.odoo.com/contactus">support</a>, or reach out to the database’s
customer success manager, with any questions on upgrading.</p>
<p>To use automated actions, navigate in <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, to
Settings app ‣ Technical menu ‣ Automation section ‣ Automated Actions.
Then, click <b>New</b> to create a new action.</p>
<p>Enter an <b>Action Name</b>, and select a <b>Model</b> to implement this action on.</p>
<p>Ensure the <b>Active</b> toggle is set to <em>on</em>, represented by a full-green switch, in order
for the automated action to run.</p>
<p>Set the <b>Trigger</b> to either <b>On Creation</b>, <b>On Update</b>,
<b>On Creation &amp; Update</b>, <b>On Deletion</b>, <b>Based on Form
Modification</b>, or <b>Based on Timed Condition</b>.</p>
<p>Based on the selection for the <b>Trigger</b>, additional fields may populate.</p>
<p>Under the <b>Apply on</b> field, a record filter using a domain can be created. Ensure a
model has been selected before setting any domains on the <b>Apply on</b> field. Click
<b>Edit Domain</b> to set record parameters.</p>
<p>Under <b>Action To Do</b> drop-down field, select <b>Send SMS Text Message</b>. Next,
set the <b>SMS Template</b>, and choose whether the SMS message should be logged as a note,
by ticking the checkbox next to <b>Log as Note</b>.</p>
<img alt="Automated action template with action to do, SMS template and log as note highlighted." class="align-center" src="../../../../_images/automated-action-sms.png"/>
<p>To implement the automated action, save it; either by navigating away, or manually saving it
(using the <b>☁️ (cloud)</b> icon).</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="sms_campaign_settings">Paramètres de la campagne SMS</a></p></li>
<li><p><a href="mailing_lists_blacklists">Listes de diffusion et listes noires</a></p></li>
<li><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
</ul>
</div>

  *[SMS]: Short Message Service
  *[CTOR]: click-to-open rate ou taux de réactivité
  *[CTR]: click-through rate ou taux de clics

