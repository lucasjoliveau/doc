# Help center

Konvergo ERP _Helpdesk_ integrates with the _Forum_ , _eLearning_ , and _Knowledge_
apps to create the _help center_.

![Overview of the settings page of a team emphasizing the help center
features.](../../../../_images/help-center-enable-features.png)

The _help center_ is a centralized location where teams and customers can
search for and share detailed information about products and services.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In order to activate any of these features on a <em>Helpdesk</em> team, (<em>Forums</em>, <em>eLearning</em>, or
<em>Knowledge</em>), the <b>Visibility</b> of the team has to be set to <b>Invited portal
users and all internal users</b>. See <a href="getting_started">Getting Started</a> for more information on <em>Helpdesk</em>
team settings and configuration.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Since all of the <em>help center</em> features require integration with other applications, enabling any
of them may result in the installation of additional modules or applications.</p>
<p>Installing a new application on a <em>One-App-Free</em> database will trigger a 15-day trial. At the end
of the trial, if a paid subscription has not been added to the database, it will no longer be
active or accessible.</p>
</div>

## Knowledge

Konvergo ERP’s _Knowledge_ application is a collaborative library where users can
store, edit, and share information. The _Knowledge_ app is represented
throughout the database by a _book_ icon.

![View of a message in Helpdesk focusing on the Knowledge book
icon.](../../../../_images/help-center-knowledge-book-icon.png)

### Enable Knowledge on a Helpdesk team

To enable the _Knowledge_ feature on a _Helpdesk_ team, go to Helpdesk ‣
Configuration ‣ Teams and select a team, or create a [new
one](getting_started).

When a team has been selected or created, Konvergo ERP displays that team’s detail
form.

On the team’s detail form, scroll down to the **Self-Service** section. Click
the box next to **Knowledge** to activate the _Knowledge_ feature. When
clicked, a new field labeled **Article** appears.

Clicking the **Article** field reveals a drop-down menu. At first, there is
only one option in the drop-down menu titled **Help** , which Konvergo ERP provides by
default. Select **Help** from the drop-down menu to choose this article.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To create a new article, go to the Knowledge app, then hover the cursor next to
the <b>Workspace</b> section heading, located in the left sidebar. Moving the cursor there
reveals a hidden <b>➕ (plus sign)</b> icon.</p>
<p>Click the <b>➕ (plus sign)</b> to create a new article in the <b>Workspace</b>. In the
upper right corner of the page, click the <b>Share</b> button, and slide the
<b>Share to Web</b> toggle switch until it reads <b>Article Published</b>. It can then
be added to a <em>Helpdesk</em> team.</p>
</div>

Once an article has been created and assigned to a _Helpdesk_ team, content
can be added and organized through the _Knowledge_ app.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="../../../productivity/knowledge/articles_editing">Editing Knowledge articles</a></p>
</div>

### Search articles from a Helpdesk ticket

When members of a _Helpdesk_ team are trying to solve a ticket, they can
search through the content in the _Knowledge_ app for more information on the
issue.

To search _Knowledge_ articles, open a ticket — either from the _Helpdesk_ app
dashboard, or by going to Helpdesk app ‣ Tickets ‣ All Tickets, and selecting
a **Ticket** from the list.

When a **Ticket** is selected, Konvergo ERP reveals that ticket’s detail form.

Click the **Knowledge (book)** icon, located above the chatter to open a
search window.

![View of knowledge search window from a helpdesk
ticket.](../../../../_images/help-center-knowledge-search.png)
<div class="alert alert-info">
<p class="alert-title">
Tip</p><p><em>Knowledge</em> articles can also be searched by pressing <b class="command o_code">Ctrl + K</b> to open the command
palette, then typing <b class="command o_code">?</b>, followed by the name of the desired article.</p>
</div>

When Konvergo ERP reveals the desired article, click it, or highlight the **Article**
title, and press **Enter**. This will open the article in the **Knowledge**
application.

To open the article in a new tab, press **Ctrl + Enter**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If a more in-depth search is required, press <b class="command o_code">Alt + B</b>. That will reveal a separate
page, in which a more detailed search can occur.</p>
</div>

#### Share articles to the help center

In order for a _Knowledge_ article to be available to customers and website
visitors, it has to be published.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Even though the <em>Help</em> article has been enabled on a team, Konvergo ERP will not share all the nested
articles to the web. Individual articles intended for customers <b>must</b> be published for them to
be viewable on the website.</p>
</div>

To publish an article, navigate to the desired article, by following the above
steps, and click the **Share** icon in the upper-right corner. This will
reveal a menu. Slide the toggle button labeled **Share to Web** to read
**Article Published**.

![View of a knowledge article focused on sharing and publishing
options.](../../../../_images/help-center-knowledge-sharing.png)

### Solve tickets with templates

_Template_ boxes can be added to _Knowledge_ articles to allow content to be
reused, copied, sent as messages, or added to the description on a ticket.
This allows teams to maintain consistency when answering customer tickets, and
minimize the amount of time spent on responding to repeat questions.

#### Add templates to articles

To create a template, go to Knowledge ‣ Help. Click on an existing nested
article or create a new one by clicking the **➕ (plus sign)** icon next to
_Help_.

Type `/` to open the **Powerbox** and view a list of
[commands](../../../productivity/knowledge/articles_editing). Select or
type `template`. A gray template block will be added to the page. Add any
necessary content to this block.

![View of a template in knowledge with focus on send and copy
options.](../../../../_images/help-center-knowledge-template-options.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Templates will only display the <b>Use as description</b> or <b>Send as Message</b>
options if they are accessed directly from <em>Helpdesk</em>.</p>
</div>

#### Use templates in tickets

Templates can be used to respond directly to a _Helpdesk_ ticket as a message,
or to add information to the ticket’s description.

To use templates in a _Helpdesk_ ticket, first, open a ticket, either from the
**Helpdesk** dashboard or by going to Helpdesk ‣ Tickets ‣ All Tickets and
selecting a **Ticket** from the list.

Click on the **Knowledge (book)** icon above the chatter for the ticket. This
opens a search window. In this search window, select, or search for the
desired article. Doing so reveals that article page in the Konvergo ERP _Knowledge_
application.

To use a template to respond to a ticket, click **Send as message** in the
upper right corner of the template box, located in the body of the article.

Doing so opens a **Compose email** pop-up window. In this window, select the
recipients, make any necessary additions or edits to the template, then click
**Send**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>To use a template to add information to a ticket’s description, click <b>Use as
description</b> in the upper right corner of the template box, located in the body of the article.
Doing so will not replace the existing text in a ticket’s description. The template will be added
as additional text.</p>
</div>

## Community Forum

A _Community Forum_ provides a space for customers to answer each other’s
questions and share information. By integrating a forum with a _Helpdesk_
team, tickets submitted by customers can be converted to posts and shared.

### Enable forums on a Helpdesk team

To enable **Community Forums** on a _Helpdesk_ team, start by navigating to
Helpdesk app ‣ Configuration ‣ Teams and select a team, or create a [new
one](getting_started).

Selecting or creating a team reveals that team’s detail form. Scroll down to
the **Self-Service** section of features, and enable **Community Forum** , by
checking the box beside it.

When activated, a new field labeled **Forums** appears beneath.

Click the empty **Forums** field to reveal a drop-down menu. By default, there
is only one option to begin with, labeled **Help**. That is the option Konvergo ERP
automatically created when the **Community Forums** feature was enabled.
Select **Help** from the drop-down menu to enable that forum.

To create a new forum, type a name into the blank **Forums** field, then click
the **Create and Edit** option. Multiple forums can be selected in this field.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>Check out the <a href="../../../websites/forum">Forum documentation</a> to learn how to configure,
use, and moderate a forum.</p>
</div>

### Create a forum post from a Helpdesk ticket

When a _Helpdesk_ team has a _Forum_ enabled, tickets submitted to that team
can be converted to forum posts.

To do that, select a ticket, either from a team’s pipeline or from Tickets ‣
All Tickets in the **Helpdesk** application.

At the top of the ticket detail form, click the **Share on Forum** button.

![Overview of the Forums page of a website to show the available ones in Konvergo ERP
Helpdesk.](../../../../_images/help-center-share-on-forum.png)

When clicked, a pop-up appears. Here, the post and title can be edited to
correct any typos, or modified to remove any proprietary or client
information. **Tags** can also be added to help organize the post in the
forum, making it easier for users to locate during a search. When all
adjustments have been made, click **Create and View Post**.

## eLearning

Konvergo ERP _eLearning_ courses offer customers additional training and content in
the form of videos, presentations, and certifications/quizzes. Providing
additional training enables customers to work through issues and find
solutions on their own. They can also develop a deeper understanding of the
services and products they are using.

### Enable eLearning courses on a Helpdesk team

To enable _eLearning_ courses on a _Helpdesk_ team, go to Helpdesk ‣
Configuration ‣ Teams and select a team, or create a [new
one](getting_started).

On the team’s settings page, scroll to the **Self-Service** section, and check
the box next to **eLearning**. A new field will appear below, labeled
**Courses**.

Click the empty field next to **Courses** beneath the **eLearning** feature to
reveal a drop-down menu. Select an available course from the drop-down menu,
or type a title into the field, and click **Create and edit** to create a new
course from this page. Multiple courses can be assigned to a single team.

### Create an eLearning course

A new _eLearning_ course can be created from the **Helpdesk** team’s settings
page, as in the step above, or from the _eLearning_ app.

To create a course directly through the _eLearning_ application, navigate to
eLearning ‣ New. This reveals a blank course template that can be customized
and modified as needed.

On the course template page, add a **Course Title** , and below that,
**Tags**.

Click on the **Options** tab. Under **Access Rights** , choose the **Enroll
Policy**. This determines which users will be allowed to take the course.
Under **Display** , choose the course **Type** and **Visibility**. The
**Visibility** setting determines whether the course will be available to
public site visitors or members.

#### Add content to an eLearning course

To add content to a course, click the **Content** tab and select **Add
Content**. Choose the **Content Type** from the drop-down menu and upload the
file, or paste the link, where instructed. Click **Save** when finished. Click
**Add Section** to organize the course in sections.

![View of a course being published for Konvergo ERP
Helpdesk.](../../../../_images/help-center-elearning-course-contents-page.png)
<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Since all of the <em>help center</em> features require integration with other applications, enabling any
of them may result in the installation of additional modules or applications.</p>
<p>Installing a new application on a <em>One-App-Free</em> database will trigger a 15-day trial. At the end
of the trial, if a paid subscription has not been added to the database, it will no longer be
active or accessible.</p>
</div>0 <div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Since all of the <em>help center</em> features require integration with other applications, enabling any
of them may result in the installation of additional modules or applications.</p>
<p>Installing a new application on a <em>One-App-Free</em> database will trigger a 15-day trial. At the end
of the trial, if a paid subscription has not been added to the database, it will no longer be
active or accessible.</p>
</div>1

### Publish an eLearning course

To allow customers to enroll in a course, both the course and the contents
need to be published.

If the course is published, but the contents of the course are not published,
customers can enroll in the course on the website, but they won’t be able to
view any of the course content. Knowing this, it may be beneficial to publish
the course first if the course contents are intended to be released over time,
such as classes with a weekly schedule.

To make the entire course available at once, each piece of course content must
be published first, then the course can be published.

To publish a course, choose a course from the _eLearning_ dashboard. On the
course template page, click the **Go to Website** smart button.

This will reveal the front end of the course’s web page. At the top of the
course web page, move the **Unpublished** toggle switch to **Published**.

#### Publish eLearning course contents from the back-end

To publish _eLearning_ course content from the back-end, choose a course from
the _eLearning_ dashboard. On the course template page, click the **Published
Contents** smart button.

Doing so reveals a separate page displaying all the published content related
to that course. Remove the default **Published** filter from the search bar in
the upper-right corner, to reveal all the content related to the course - even
the non-published content.

Click the **≣ (List View)** icon in the upper-right corner, directly beneath
the search bar to switch to list view.

While in **List View** , there is a checkbox on the far left of the screen,
above the listed courses, to the left of the **Title** column. When that
checkbox is clicked, all the course contents are selected at once.

With all the course content selected, double click any of the boxes in the
**Is Published** column. This reveals a pop-up window, asking for confirmation
that all selected records are intended to be published. Click **OK** to
automatically publish all course content.

![View of a course contents being published in Konvergo ERP Helpdesk back-
end.](../../../../_images/help-center-elearning-publish-back-end.png)

