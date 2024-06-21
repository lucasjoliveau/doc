# Suivre et gérer des présentations

Dans Konvergo ERP Événements, les participants ont la possibilité de proposer des
intervenants pour faire une présentation lors d’événements.

## Configuration

Allez tout d’abord à Événements ‣ Configuration ‣ Paramètres et activez
**Programme & Sessions**.

Lorsque cette fonctionnalité est activée, deux autres options deviennent
disponibles : _Diffusion en direct_ et _Ludification d’événement_.

**Diffusion en direct** vous permet de diffuser vos sessions en ligne grâce à
l’intégration de YouTube.

**Ludification d’événement** vous permet de partager un quiz avec vos
participants, une fois qu’une session (présentation) est terminée.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>La <b>ludification d’événement</b> n’est pas nécessaire pour que les sessions apparaissent sur la page de l’événement sur le site web, mais elle peut améliorer l’engagement et la satisfaction globale des participants à l’événement.</p>
</div>

## Présentations, propositions de présentations et programme

Une fois ces deux fonctionnalités activées, les liens suivants sont ajoutés
automatiquement au menu des sous-titres, situé sur la page de l’événement sur
le site web : **Présentations** , **Propositions de présentations** , et
**Programme**. Chaque participant peut accéder librement à ces éléments de
menu et à leur contenu correspondant.

Le lien **Présentations** permet aux participants d’accéder à la liste des
présentations de cet événement.

Le lien **Propositions de présentations** permet aux participants d’accéder à
une page de formulaire, où ils peuvent proposer des présentations pour
l’événement.

Le lien **Programme** permet aux participants d’accéder à la liste de toutes
les présentations de l’événement, mais sous forme de calendrier/créneaux
horaires.

![Vue du site web publié et les présentations, propositions de présentations
et programme dans Konvergo ERP Événements](../../../_images/events-talk-proposal-
header.png)

## Gérer les propositions de présentations

Lorsque les participants complètent et soumettent un formulaire de proposition
de présentation sur le site web, une nouvelle **Proposition** est
immédiatement créée dans le backend de l’événement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Toutes les présentations (propositions, confirmées, annoncées, etc.) sont accessibles via le bouton intelligent <b>Sessions</b> sur le formulaire de l’événement.</p>
</div> ![Vue de la page des propositions de présentations mettant
en évidence la colonne des propositions dans Konvergo ERP
Événements.](../../../_images/events-tracks-kanban.png)

Si une proposition est acceptée, faites glisser la **Session d’événement** à
l’étape appropriée dans la vue Kanban (par ex. `Confirmé`, etc.). Ensuite,
allez à ce formulaire de modèle d’événement en particulier et cliquez sur le
bouton intelligent **Allez au Site Web** pour accéder à la page de la
présentation en question sur le site web.

Dans le coin supérieur droit, cliquez sur le bouton de commutation pour passer
de **Non publié** à **Publié** et la présentation est immédiatement accessible
sur le site web.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si la présentation n’est pas publiée, les participants ne pourront jamais y accéder.</p>
</div> ![Vue de la page du site web permettant de publier une
présentation proposée dans Konvergo ERP Événements.](../../../_images/events-tracks-
publish.png)

### Liste des participants et présences

Une fois les participants se sont inscrits à un événement spécifique, ils sont
ajoutés à la **Liste des participants** de cet événement, qui est accessible
depuis le bouton intelligent **Participants** sur le formulaire du modèle
d’événement ou via Analyse ‣ Participants en les triant par événement.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsqu’un participant arrive à l’événement, il sera marqué comme présent (<b>Présence confirmée</b>) et le statut de ce participant passera à <b>Présent.</b></p>
</div> ![Aperçu des événements dans la vue kanban dans Konvergo ERP
Événements.](../../../_images/events-attendees-smartbutton.png)

Lors de l’analyse d’une **liste de participants** , Konvergo ERP propose différentes
façons d’afficher les informations. Chaque option d’affichage présente les
mêmes informations, mais dans une disposition légèrement différente. Pour
changer la vue, cliquez sur le icônes dans le coin supérieur droit de l’écran.

![Différentes options d'affichage sur la page de la liste de
participants.](../../../_images/events-attendees-view-options.png)

La vue **Kanban** permet de confirmer si les participants ont déjà payé ou
non.

La vue **Liste** fournit les informations sous la forme d’une liste plus
traditionnelle.

La vue **Calendrier** permet d’afficher clairement à quelle date de
l’événement les participants arrivent.

La vue **Graphique** fournit des représentations graphiques des participants à
l’événement, ainsi que de nombreux filtres et mesures personnalisables
permettant une analyse plus approfondie.

La vue **Cohorte** présente les données relatives aux participants afin de
mieux analyser le nombre de dates d’inscription.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les tickets vendus par le biais de bons de commande confirment les participants dès que le devis est confirmé.</p>
</div>

### Gérer les inscriptions

En sélectionnant un participant, Konvergo ERP montre la fiche détaillée de ce
participant.

À partir de là, les badges de l’événement peuvent être envoyés manuellement,
en cliquant sur **Envoyer par email**. Le **participant** peut également être
marqué comme **Présent** ou l’inscription peut être annulée via le bouton
**Annuler l’inscription**.

![Vue d'un formulaire de participant mettant en évidence l'envoi par email et
l'annulation de l'inscription dans Konvergo ERP Événements.](../../../_images/events-
send-email-button.png)

### Règles de génération de pistes

Avec Konvergo ERP, il est possible de générer des pistes à partir d’événements.

Pour créer et configurer une **Règle de génération de pistes** associée aux
événements, allez à l’application Événements ‣ Configuration ‣ Génération de
pistes.

Sur la page **Règle de génération de pistes** , vous y trouvez chaque **règle
de génération de pistes** , ainsi que les données pertinentes relatives à ces
règles.

![Comment se présente la page des Règles de génération de pistes dans Konvergo ERP
Événements.](../../../_images/events-lead-generation-rule-page.png)

Pour créer une nouvelle **règle de génération de pistes** , cliquez sur
**Créer** et complétez le formulaire de **Règle de génération de pistes**.

![Comment se présente le modèle de Règle de génération de pistes dans Konvergo ERP
Événements.](../../../_images/events-lead-generation-rule-template.png)

Après avoir donné un nom à la règle, configurez _comment_ les pistes doivent
être créées (soit **Par participant** ou **Par commande**), et _quand_ elles
doivent être créées (lorsque les **Participants sont créés** , lorsque les
**Participants sont confirmés** , ou lorsque les **Participants ont
participé** à l’événement).

Dans la section **Pour n’importe lequel de ces événements** , des champs
permettent d’associer cette règle à des catégories d’événements, à des
entreprises et/ou à des événements spécifiques. Pour ajouter encore plus de
spécificité à une règle, vous pouvez configurer un filtre pour s’assurer que
la règle s’applique uniquement à un public cible spécifique de participants
(dans la section **Si les participants respectent ces conditions**).

Enfin, dans la section **Valeurs par défaut de piste** , désignez un **Type de
piste** , puis assignez-la à une **Équipe commerciale** (et/ou un **Vendeur**)
spécifique et associez des étiquettes à la règle si nécessaire.

