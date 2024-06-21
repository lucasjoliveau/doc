# SMS essentials

Utilizing SMS outreach in communication strategies can help companies expand
their market reach, especially in some countries, where emails might not be
very common, or even used at all.

Konvergo ERP’s _SMS Marketing_ application can also help boost conversion rates around
valuable actions, such as event registrations, free trials, purchases, etc.,
since text and mobile-based marketing channels typically yield higher CTOR and
CTR outcomes.

## SMS marketing dashboard

When the application is opened, Konvergo ERP displays the main **SMS Marketing**
dashboard, which showcases the various SMS mailings that have been created,
along with pertinent information and data related to that specific message.

The **Kanban** view is the default Konvergo ERP uses when the application is opened,
which provides an organized display of the SMS mailings that have been
created, and what their current status is at the moment.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>An <abbr title="Short Message Service">SMS</abbr> mailing can have one of the following statuses:
<b>Draft</b>, <b>In Queue</b>, <b>Sending</b>, or <b>Sent</b>.</p>
</div>

In the upper right corner of the main **SMS Marketing** dashboard, there are a
few different view options to choose from. Each one provides a unique take on
the same SMS information.

The **List** view provides the same useful data related to SMS mailings, but
in a more traditional list layout.

The **Calendar** view provides a simple calendar, making it easy to see when
SMS mailings are going to be sent (or have been sent). If a future date is
clicked, Konvergo ERP reveals a blank SMS template that, when completed, will be
scheduled to be sent on that specific future date.

Lastly, the **Graph** view visualizes that same SMS-related data in series of
graphs and charts. Konvergo ERP also provides various ways to sort and group the data
for more detailed analysis.

## Create SMS messages

To start, click **Create** on the main **SMS Marketing** dashboard, and Konvergo ERP
reveals a blank SMS template form, which can be configured in a number of
different ways.

![Creating an SMS marketing template.](../../../../_images/sms-create.png)

First, give the mailing a **Subject** , which describes what the mailing is
about.

Next, in the **Recipients** field, choose to whom this SMS will be sent. By
default, Konvergo ERP has **Mailing List** selected. If this is the desired
**Recipients** field option, specify which mailing list Konvergo ERP should send this
SMS to in the **Select Mailing List** field.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>To create (or edit) a mailing list, go to Mailing Lists ‣ Mailing List. There,
Konvergo ERP displays all previously created mailing lists, along with various types of data related to
that specific list (e.g. number of contacts, mailings, recipients, etc.).</p>
<p>To learn more about mailing lists and contacts, check out <a href="mailing_lists_blacklists">Mailing lists and blacklists</a>.</p>
</div> ![View of the mailing list page in the SMS marketing
application.](../../../../_images/sms-mailing-list1.png)

To reveal all the possible options in the **Recipients** field, click the
field to see all the choices Konvergo ERP makes available.

When another field (other than **Mailing List**) is selected, the option to
specify that chosen field even further becomes available — either with a
default recipient filter equation that appears automatically (which can be
customized to fit any business need), or, if no default recipient filter
equation is present, an **Add Filter** button will appear.

Clicking the **Add Filter** button, reveals fully customizable domain rule
fields, which can be configured similar to an equation. You can create
multiple recipient rules, if necessary.

Then, Konvergo ERP will only send the SMS to recipients who fit into whatever criteria
is configured in those fields. Multiple rules can be added.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>If <b>Contact</b> is chosen, all of the <em>Contacts</em> records in the Konvergo ERP database (vendors,
customers, etc.) will receive the <abbr title="Short Message Service">SMS</abbr>, by default — unless more
specific recipient rules are entered.</p>
<p>For instance, the message below will only be sent to contacts in the database that are located in
the United States (e.g. <code>Country</code> &gt; <code>Country Name</code> equals <code>United States</code>), and they haven’t
blacklisted themselves from any mailings (e.g. <code>Blacklist</code> &gt; <code>is</code> &gt; <code>not set</code>).</p>
<img alt="Contact recipients on SMS marketing." class="align-center" src="../../../../_images/contact-recipient.png"/>
</div>

### Writing SMS messages

Enter the content of the SMS in the text field, found in the **SMS Content**
tab. Links and emojis can also be included. Beneath the text field, Konvergo ERP
displays how many characters are used in the message, along with how many SMS
mailings it will take to deliver the complete message.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To check the price of sending an <abbr title="Short Message Service">SMS</abbr> for a country, click on the
<b>Information</b> icon.</p>
</div> ![SMS price check icon.](../../../../_images/sms-price-
check.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Credits must be purchased from Konvergo ERP in order to take advantage of the <em>SMS Marketing</em> app;
<abbr title="Short Message Service">SMS</abbr> messages will not be sent without credits.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://iap-services.odoo.com/iap/sms/pricing">Konvergo ERP SMS - FAQ</a></p>
</div>

### Track links used in SMS messages

When links are used in SMS messages, Konvergo ERP automatically generates link
trackers to gather analytical data and metrics related to those specific
links, which can be found by going to Configuration ‣ Link Tracker.

![SMS Link Tracker page.](../../../../_images/sms-link-tracker.png)

## Adjust SMS settings

Under the **Settings** tab of the SMS template, there is an option to
**Include opt-out link**. If activated, the recipient is able to unsubscribe
from the mailing list, thus avoiding all future mailings.

An employee can be designated as the **Responsible** in the **Tracking**
section of the **Settings** tab, as well.

![SMS Settings tab.](../../../../_images/sms-settings-tab.png)

## Send SMS messages

Once a mailing is created, choose when Konvergo ERP should deliver the message from
the following options:

  * **Send** : sends the message immediately. Consider using this option if the recipient list is highly refined, or in cases that involve fast approaching deadlines, such as a “flash sale.”

  * **Schedule** : choose a day (and time) for Konvergo ERP to send the mailing. This is typically the best option for mailings related to a specific event. Such a method can also be used to promote a limited-time offer, or to help plan a company’s content strategy in advance.

  * **Test** : allows for an SMS to be sent to one or multiple numbers for test purposes. Remember to use a comma between phone numbers if multiple numbers are used as recipients.

## Visualize reports

On the **Reporting** page (accessible via the Reporting option in the header
menu), there are options to apply different combinations of **Filters** and
**Measures** to view metrics in a number of different layouts (e.g. **Graph**
, **List** , and **Cohort** views.)

Each **Reporting** metric view option allows for more extensive performance
analysis of SMS mailings.

For example, while in the default **Graph** view, SMS data is visualized as
different graphs and charts, which can be sorted and grouped in various ways
(e.g. **Measures** drop down menu).

![Reporting page in SMS Marketing.](../../../../_images/sms-reporting-
page.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>SMS messages can be sent using automated actions in Konvergo ERP. Konvergo ERP <em>Studio</em> is required to use
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
See also</p><ul>
<li><p><a href="sms_campaign_settings">SMS campaign settings</a></p></li>
<li><p><a href="mailing_lists_blacklists">Mailing lists and blacklists</a></p></li>
<li><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
</ul>
</div>

  *[SMS]: Short Message Service
  *[CTOR]: click-to-open rate
  *[CTR]: click-through rate

