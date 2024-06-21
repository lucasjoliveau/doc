# Utilize activities for sales teams

_Activities_ are follow-up tasks tied to a record in an _Konvergo ERP_ database.
Activities can be scheduled on any page of the database that contains a
chatter thread, Kanban view, list view, or activities view of an application.

![The summary view of activities for leads and opportunities in an Konvergo ERP
database.](../../../../_images/activities-view.png)

Planned Activities for Leads and Opportunities.

## Activity types

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

#### Activity settings

##### Action

The _Action_ field specifies the intent of the activity. Some actions trigger
specific behaviors after an activity is scheduled.

  * If **Upload Document** is selected, a link to upload a document is added directly to the planned activity in the chatter.

  * If either **Phonecall** or **Meeting** are selected, users have the option to open their calendar to schedule a time for this activity.

  * If **Request Signature** is selected, a link is added to the planned activity in the chatter that opens a signature request pop-up window.

![The Activity settings on a new activity type with emphasis on the Action
field.](../../../../_images/action-field.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The actions available to select on an activity type vary, depending on the applications currently
installed in the database.</p>
</div>

##### Default user

To automatically assign this activity to a specific user when this activity
type is scheduled, choose a name from the **Default User** drop-down menu. If
this field is left blank, the activity is assigned to the user who creates the
activity.

##### Default summary

To include notes whenever this activity type is created, enter them into the
**Default Summary** field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The information in the <b>Default User</b> and <b>Default Summary</b> fields are
included when an activity is created. However, they can be altered before the activity is
scheduled or saved.</p>
</div>

#### Next activity

To automatically suggest, or trigger, a new activity after an activity has
been marked complete, the **Chaining Type** must be set.

##### Suggest next activity

In the **Chaining Type** field, select **Suggest Next Activity**. Upon doing
so, the field underneath changes to: **Suggest**. Click the **Suggest** field
drop-down menu to select any activities to recommend as follow-up tasks to
this activity type.

![The Next Activity section on a new activity type
form.](../../../../_images/next-activity.png)

In the **Schedule** field, choose a default deadline for these activities. To
do so, configure a desired number of **Days** , **Weeks** , or **Months**.
Then, decide if it should occur **after completion date** or **after previous
activity deadline**.

This **Schedule** field information can be altered before the activity is
scheduled.

When all configurations are complete, click **Save**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If an activity has the <b>Chaining Type</b> set to <b>Suggest Next Activity</b>, and
has activities listed in the <b>Suggest</b> field, users are presented with recommendations
for activities as next steps.</p>
<img alt="A schedule activity pop-up with emphasis on the recommended activities." class="align-center" src="../../../../_images/suggest-next-activity.png"/>
</div>

##### Trigger next activity

Setting the **Chaining Type** to **Trigger Next Activity** immediately
launches the next activity once the previous one is completed.

If **Trigger Next Activity** is selected in the **Chaining Type** field, the
field beneath changes to: **Trigger**. From the **Trigger** field drop-down
menu, select the activity that should be launched once this activity is
completed.

In the **Schedule** field, choose a default deadline for these activities. To
do so, configure a desired number of **Days** , **Weeks** , or **Months**.
Then, decide if it should occur **after completion date** or **after previous
activity deadline**.

This **Schedule** field information can be altered before the activity is
scheduled.

When all configurations are complete, click **Save**.

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
See also</p><ul>
<li><p><a href="../../../essentials/activities">Activities</a></p></li>
</ul>
</div>

