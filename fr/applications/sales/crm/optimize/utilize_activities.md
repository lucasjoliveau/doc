# Utilize activities for sales teams

_Activities_ are follow-up tasks tied to a record in an _Konvergo ERP_ database.
Activities can be scheduled on any page of the database that contains a
chatter thread, Kanban view, list view, or activities view of an application.

![The summary view of activities for leads and opportunities in an Konvergo ERP
database.](../../../../_images/activities-view.png)

Planned Activities for Leads and Opportunities.

## Types d’activité

A set of preconfigured activity types is available in the _CRM_ app. To view
the list of available activity types, navigate to the CRM app ‣ Configuration
‣ Activity Types.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Additional activity types are available within the database, and can be utilized through
different applications. To access the complete list of activity types, go to the
Settings app, then scroll to the <b>Discuss</b> section, and click
<b>Activity Types</b>.</p>
</div>

The preconfigured activity types for the _CRM_ app are as follows:

>   * **Email** : adds a reminder to the chatter that prompts the salesperson
> to send an email.
>
>   * **Call** : opens a calendar link where the salesperson can schedule time
> to call the contact.
>
>   * **Meeting** : opens a calendar link where the salesperson can schedule
> time to have a meeting with the contact.
>
>   * **To Do** : adds a general reminder task to the chatter.
>
>   * **Upload Document** : adds a link on the activity where an external
> document can be uploaded. Note that the _Documents_ app is **not** required
> to utilize this activity type.
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If other applications are installed, such as <em>Sales</em> or <em>Accounting</em>, other activity types are
made available in the <em>CRM</em> app.</p>
</div>

### Create a new activity type

To create a new activity type, click **New** at the top-left of the page to
open a blank form.

At the top of the form, start by choosing a **Name** for the new activity
type.

#### Paramètres des activités

##### Action

Le champ _Action_ précise l’intention de l’activité. Certaines actions
déclenchent des comportements spécifiques après avoir planifié une activité.

  * Si vous sélectionnez **Charger un document** , un lien pour charger un document s’ajoute directement à l’activité planifiée dans le chatter.

  * Si vous sélectionnez **Appel téléphonique** ou **Réunion** , les utilisateurs ont l’option d’ouvrir leur calendrier pour programmer une heure pour cette activité.

  * Si vous sélectionnez **Demander une signature** , un lien est ajouté à l’activité planifiée dans le chatter permettant d’ouvrir une fenêtre contextuelle de demande de signature.

![The Activity settings on a new activity type with emphasis on the Action
field.](../../../../_images/action-field.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les actions disponibles pour sélectionner un type d’activité varient en fonction des applications actuellement installées dans la base de données.</p>
</div>

##### Utilisateur par défaut

Pour assigner cette activité automatiquement à un utilisateur spécifique
lorsque ce type d’activité est planifié, choisissez un nom dans le menu
déroulant **Utilisateur par défaut**. Si ce champ est laissé vierge,
l’activité est assignée à l’utilisateur qui a créé l’activité.

##### Résumé par défaut

Pour inclure des notes chaque fois que ce type d’activité est créé, saisissez-
les dans le champ **Résumé par défaut**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les informations dans les champs <b>Utilisateur par défaut</b> et <b>Résumé par défaut</b> sont incluses lors de la création d’une activité. Toutefois, elles peuvent être modifiées avant que l’activité ne soit planifiée ou enregistrée.</p>
</div>

#### Activité suivante

Pour suggérer ou déclencher automatiquement une nouvelle activité après qu’une
activité a été marquée comme faite, vous devez définir le **Type de
chaînage**.

##### Suggérer l’activité suivante

Dans le champ **Type de chaînage** , sélectionnez **Suggérer l’activité
suivante**. Le champ situé en dessous devient alors **Suggérer**. Cliquez sur
le menu déroulant **Suggérer** pour sélectionner les activités à recommander
comme tâches de suivi pour ce type d’activité.

![The Next Activity section on a new activity type
form.](../../../../_images/next-activity.png)

Dans le champ **Planifier** , choisissez un délai par défaut pour ces
activités. Pour ce faire, configurez un nombre souhaité de **Jours** ,
**Semaines** , ou **Mois**. Puis décidez si elle doit avoir lieu **après la
date d’achèvement** ou **après la date de fin de l’activité précédente**.

Vous pouvez modifier ce champ **Planifier** avant que l’activité ne soit
planifiée.

Lorsque toutes les configurations sont terminées, cliquez sur **Enregistrer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le <b>Type de chaînage</b> de l’activité est défini sur <b>Suggérer l’activité suivante</b> et des activités sont répertoriées dans le champ <b>Suggérer</b>, les utilisateurs reçoivent des recommandations d’activités pour les étapes suivantes.</p>
<img alt="A schedule activity pop-up with emphasis on the recommended activities." class="align-center" src="../../../../_images/suggest-next-activity.png"/>
</div>

##### Déclencher l’activité suivante

Le fait de définir le **Type de chaînage** sur **Déclencher l’activité
suivante** permet de lancer immédiatement l’activité suivante une fois que la
précédente est terminée.

Si vous sélectionnez **Déclencher l’activité suivante** dans le champ **Type
de chaînage** , le champ situé en dessous devient **Déclencher**. Dans le menu
déroulant du champ **Déclencher** , sélectionnez l’activité qui doit être
lancée une fois que cette activité est terminée.

Dans le champ **Planifier** , choisissez un délai par défaut pour ces
activités. Pour ce faire, configurez un nombre souhaité de **Jours** ,
**Semaines** , ou **Mois**. Puis décidez si elle doit avoir lieu **après la
date d’achèvement** ou **après la date de fin de l’activité précédente**.

Vous pouvez modifier ce champ **Planifier** avant que l’activité ne soit
planifiée.

Lorsque toutes les configurations sont terminées, cliquez sur **Enregistrer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>When an activity has the <b>Chaining Type</b> set to <b>Trigger Next Activity</b>,
marking the activity as <em>Done</em> immediately launches the next activity listed in the
<b>Trigger</b> field.</p>
</div>

## Activity tracking

To keep the pipeline up to date with the most accurate view of the status of
activities, as soon as a lead is interacted with, the associated activity
should be marked as _Done_. This ensures the next activity can be scheduled as
needed. It also prevents the pipeline from becoming cluttered with past due
activities.

The pipeline is most effective when it is kept up-to-date and accurate to the
interactions it is tracking.

## Activity plans

Activity types with the _Chaining Type_ set to _Trigger New Activity_ provide
the opportunity to preplan a sequence of customized activities. Once an
activity is marked as _Done_ , the next activity is automatically scheduled.

The _Chaining Type_ setting on an activity type provides the opportunity to
preplan a sequence of events, that can aide in the sales process.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>A salesperson adds a new lead to their pipeline, and schedules an <em>Email</em> activity for the
following day. The email activity type is configured with the following settings:</p>
<ul>
<li><p><b>Chaining Type</b>: <code>Suggest Next Activity</code></p></li>
<li><p><b>Suggest</b>: <code>Call</code>, <code>Meeting</code></p></li>
<li><p><b>Schedule</b>: <code>2 days after previous activity deadline</code></p></li>
</ul>
<p>After sending an email to the lead, the salesperson clicks <b>DONE &amp; SCHEDULE NEXT</b> on
the <b>Schedule Activity</b> pop-up window. This opens a new pop-up window, where the
suggested next activities are listed as recommendations for next steps.</p>
<img alt="Schedule an activity pop-up window with recommended activities." class="align-center" src="../../../../_images/recommended-activities.png"/>
</div>

The _suggested_ or _triggered_ activities may vary, depending on a variety of
factors. See below for some suggested sequences:

Sample #1Sample #2Sample #3

  * A salesperson adds a lead to the pipeline and schedules an _email_ activity.

  * The _email_ activity suggests scheduling a _call_ or a _meeting_ within two days of the previous deadline.

  * Both the _call_ and the _meeting_ activities trigger a _create quote_ activity.

  * After the quote is sent, a _follow-up on quote_ activity is scheduled within five days.

  * A lead is [added to the pipeline](../acquire_leads/generate_leads) through the website’s contact form. The salesmanager assigns a salesperson and schedules an activity for a _call_.

  * The _call_ activity triggers an _upload document_ activity, so the salesperson can send over a proposal after a successful phone call.

  * The _upload document_ activity suggests scheduling a _request signature_ activity or a _meeting_. The salesperson chooses to schedule a meeting.

  * A salesmanager notices several of their salespeople are neglecting to follow-up on their leads in a timely manner. As a result, high-value targets are not receiving adequate attention.

  * The salesmanager creates a new activity type, titled _follow-up_ , which is configured with the **Action** set to **Reminder**.

  * The salesmanager adds _follow-up_ as the next activity triggered or suggested to all of their teams activities.

  * After a salesperson schedules an _email_ activity, a _follow-up_ activity is scheduled for the next day. After they schedule a _meeting_ activity, a _follow-up_ activity is scheduled two days later.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../essentials/activities">Activities</a></p></li>
</ul>
</div>

