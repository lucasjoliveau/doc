# Paramètres de la campagne SMS

L’utilisation de campagnes SMS avec Konvergo ERP _SMS Marketing_ n’est pas une simple
stratégie publicitaire efficace, mais un excellent moyen de rappeler aux gens
les événements à venir, les factures émises, et bien plus encore.

Mais avant de pouvoir créer (et envoyer) des campagnes SMS, il faut d’abord
activer quelques paramètres et fonctionnalités spécifiques.

## Paramètre de la campagne SMS

Pour activer les campagnes SMS dans Konvergo ERP, assurez-vous que la fonctionnalité
_Campagnes d’emails_ est activée en allant à Email Marketing ‣ Configuration ‣
Paramètres, activez **Campagnes d’emails** et **enregistrez** les changements.

![Vue du paramètre des campagnes d'emails dans Konvergo ERP.](../../../../_images/sms-
mailing-campaigns.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’activation de la fonctionnalité <em>Campagnes d’emails</em> dans les <em>Paramètres généraux</em> active également la fonctionnalité <em>Test A/B</em>.</p>
</div>

Une fois le paramètre activé, retournez à l’application SMS Marketing et notez
que le menu d’en-tête **Campagnes** est désormais disponible. De même,
l’onglet **Test A/B** est désormais disponible sur chaque formulaire du modèle
de SMS.

## Tests A/B

Les **Tests A/B** permettent de tester n’importe quel envoi de SMS à d’autres
versions de la même campagne, afin de comparer la version la plus performante
en termes d’engagement et/ou de conversion.

Sur un formulaire du modèle de SMS, sous l’onglet **Tests A/B** , il n’y a
initialement qu’une seule case à cocher intitulée **Autoriser les tests A/B**.

Lorsqu’on clique dessus, une série d’autres options apparaît.

![L'onglet Test A/B se situe sur un formulaire de campagne dans l'application
Konvergo ERP SMS Marketing.](../../../../_images/ab-tests-sms.png)

Dans le premier champ, saisissez un pourcentage souhaité de destinataires qui
fera l’objet du Test A/B.

Sous le champ de pourcentage, se trouve le champ **Sélection du gagnant**.
C’est ce que Konvergo ERP utilisera pour décider de la réussite d’un test A/B. En
d’autres termes, il indique à Konvergo ERP comment choisir un test A/B gagnant.

Les sections suivantes sont disponibles : **Manuelle** , **Taux de clic le
plus élevé** , **Pistes** , **Devis** ou **Revenus**.

Enfin, le champ **Envoyer le définitif le** s’affiche. Il représente la date
et l’heure que Konvergo ERP utilise comme date limite pour déterminer l’envoi gagnant.
Ensuite, Konvergo ERP envoie ce mailing gagnant aux destinataires restants qui n’ont
pas été impliqués dans le test, à cette date et heure antérieures.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Créez rapidement différentes versions du mailing à ajouter au Test A/B en cliquant sur le bouton <b>Créer une version alternative</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>N’oubliez pas que le mailing gagnant est basé sur les critères sélectionnés dans le champ <b>Sélection du gagnant</b>.</p>
</div>

## Page des campagnes

Pour créer, modifier ou analyser une campagne, cliquez sur Campagnes dans le
menu d’en-tête de l’application **SMS Marketing**. Sur la page des
**Campagnes** , chaque campagne affiche plusieurs informations liées aux
envois associées à cette campagne (par ex. le nombre d’emails, de publications
sociales, de SMS et de notifications push).

![Vue du tableau de bord de différentes campagnes dans l'application Konvergo ERP SMS
Marketing, séparées par étape.](../../../../_images/campaigns-page.png)

## Modèles de campagne

Cliquez sur **Créer** pour créer une nouvelle campagne et Konvergo ERP affiche un
formulaire de campagne vierge à remplir. Vous pouvez également sélectionner
une campagne déjà créée afin de dupliquer, réviser ou modifier le formulaire
du modèle.

![Vue d'un modèle de campagne SMS dans Konvergo ERP SMS
Marketing.](../../../../_images/sms-campaign-template.png)

Pour chaque campagne, les options **Envoyer un nouvel email** , **Envoyer un
SMS** , **Envoyer un post social** et **Notifications push** sont disponibles
en haut du formulaire du modèle.

Chaque fois qu’une de ces options de communication est ajoutée à la campagne,
Konvergo ERP crée un nouvel onglet correspondant sur le formulaire du modèle, où ces
types de messages peuvent être revus ou édités, ainsi que divers ensembles de
données liés à chaque envoi spécifique.

En haut du modèle, vous trouverez plusieurs boutons intelligents analytiques.
Lorsqu’on clique dessus, Konvergo ERP affiche des mesures détaillées liées à ce sujet
spécifique (par ex. **Engagement** , **Opportunités** , etc.) sur une page
séparée.

Sous les boutons intelligents, on trouve les champs **Nom de la campagne** et
**Responsable**. Konvergo ERP permet également d’ajouter diverses **Étiquettes** (si
nécessaire).

## Envoyer des SMS via l’application Contacts

L’envoi de SMS directement via la fiche d’un contact est disponible par
défaut.

Afin d’envoyer un SMS de cette manière, allez à l’application Contacts,
sélectionnez le contact souhaité dans la base de données et cliquez sur
l’icône de **SMS** sur la fiche du contact (à côté du champ **Numéro de
téléphone**).

![L'icône de SMS est située sur la fiche de contact d'une personne dans Konvergo ERP
Contacts.](../../../../_images/sms-contact-form.png)

Pour envoyer un message à plusieurs contacts en même temps, allez au tableau
de bord principal de l’application Contacts, choisissez la **vue Liste** et
sélectionnez tous les contacts souhaités auxquels le message doit être envoyé.
Ensuite, sous **Action** , sélectionnez **Envoyer un SMS**.

![Sélectionnez un certain nombre de contacts, cliquez sur Action et
sélectionnez Envoyer plusieurs SMS.](../../../../_images/sms-contacts-action-
send-message.png)

## Configurer des modèles de SMS pour une utilisation future

Afin de configurer des **Modèles de SMS** pour une utilisation future, activez
le [mode développeur](../../../general/developer_mode#developer-mode) en
allant au tableau de bord principal de Konvergo ERP contenant toutes les applications
et cliquez sur l’application Paramètres. Ensuite, descendez jusqu’à la section
**Outils développeur** et cliquez sur **Activer le mode développeur**.

Une fois le _mode développeur_ activé, le tableau de bord principal de Konvergo ERP
apparaît à nouveau, affichant désormais une icône de bug, qui se situe dans le
coin supérieur droit du tableau de bord ; cette icône indique que le mode
développeur est actuellement actif.

Retournez ensuite à l’application Paramètres et dans les menus d’en-tête
désormais visibles, choisissez Technique ‣ Modèles de SMS pour commencer à
configurer des modèles de SMS pour les futures campagnes de marketing.

![Sélectionnez l'option Modèles de SMS dans le menu déroulant Technique de la
page des Paramètres.](../../../../_images/sms-template-setting.png)

Dans le tableau de bord des **Modèles de SMS** , Konvergo ERP affiche une page entière
de modèles de SMS. La vue **Liste** par défaut énumère le nom de chaque modèle
et les destinataires auxquels il s’applique.

Sur cette page, les modèles de SMS peuvent être édités ou créés à partir de
zéro.

![La page des Modèles de SMS dans Konvergo ERP est disponible après avoir activé le
mode développeur dans les Paramètres généraux](../../../../_images/sms-
template.png)

  *[SMS]: Short Message Service

