# Commands and canned responses

In the Konvergo ERP _Live Chat_ application, _commands_ allow the user to perform
specific actions both inside the chat window, and through other Konvergo ERP
applications. The _Live Chat_ app also includes _canned responses_. These are
customized, pre-configured substitutions that allow users to replace shortcut
entries in place of longer, well-thought out responses to some of the most
common questions and comments.

Both commands and canned responses save time, and allow users to maintain a
level of consistency throughout their conversations.

## Execute a command

Live chat _commands_ are keywords that trigger pre-configured actions. When a
live chat _operator_ is participating in a conversation with a customer or
website visitor, they can execute a command by typing `/`, followed by the
command.

Commands, and the resulting actions, are only visible in the conversation
window for the live chat operator. A customer will not see any commands that
an operator uses in a conversation from their view of the chat.

![View of the chat window with a helpdesk ticket created in Konvergo ERP Live
Chat.](../../../_images/responses-ticket-link.png)

More information about each available command can be found below.

### Help

If an operator types `/help` in the chat window, an informative message that
includes the potential entry types an operator can make is displayed.

  * Type `@username` to mention a user in the conversation. A notification will be sent to that user’s inbox or email, depending on their notification settings.

  * Type `#channel` to mention a _Discuss_ channel.

  * Type `/command` to execute a command.

  * Type `:shortcut` to insert a canned response.

![View of the message generated from using the /help command in Konvergo ERP Live
Chat.](../../../_images/responses-help.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../productivity/discuss">Discuss</a></p></li>
<li><p><a href="../../productivity/discuss/team_communication">Use channels for team communication</a></p></li>
</ul>
</div>

### Helpdesk & Helpdesk search

The `/helpdesk` and `/helpdesk_search` commands allow operators to both create
helpdesk tickets directly from a conversation, and search through existing
tickets by keyword or ticket number.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <code>/helpdesk</code> and <code>/helpdesk_search</code> commands can only be used if the <em>Helpdesk</em> app has been
installed, and <em>Live Chat</em> has been activated on a <em>Helpdesk</em> team. To activate <b>Live
Chat</b>, go to Helpdesk application ‣ Configuration ‣ Teams, and select a
team. Scroll to the <b>Channels</b> section and check the box labeled <b>Live Chat</b>.</p>
</div>

#### Create a ticket from a live chat

If an operator types `/helpdesk` in the chat window, the conversation is used
to create a _Helpdesk_ ticket.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In version 16.3, the command to create a new ticket is <code>/ticket</code>. This only applies to databases
running version 16.3.</p>
</div>

After entering the `/helpdesk` command, type a title for the ticket into the
chat window, then press `Enter`.

![View of the results from a helpdesk search in a Live Chat
conversation.](../../../_images/helpdesk.png)

The newly created ticket will be added to the _Helpdesk_ team that has live
chat enabled. If more than one team has live chat enabled, the ticket will
automatically be assigned based on the team’s priority.

The transcript from the conversation will be added to the new ticket, under
the **Description** tab.

To access the new ticket, click on the link in the chat window, or go to the
Helpdesk app and click the **Tickets** button on the kanban card for the
appropriate team.

#### Search for a ticket from a live chat

If an operator types `/helpdesk_search` in the chat window, they can search
through _Helpdesk_ tickets by ticket number or keyword.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>In version 16.3, the command to search through <em>Helpdesk</em> tickets is <code>/search_tickets</code>. This only
applies to databases running version 16.3.</p>
</div>

After entering the `/helpdesk_search` command, type a keyword or ticket
number, then press `Enter`. If one or more related tickets are found, a list
of links will be generated in the conversation window.

![View of the results from a helpdesk search in a Live Chat
conversation.](../../../_images/helpdesk-search.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Results from the search command will only be seen by the operator, not the customer.</p>
</div>

### History

If an operator types `/history` in the chat window, it will generate a list of
the most recent pages the visitor has viewed on the website (up to 15).

![View of the results from a /history command in a Live Chat
conversation.](../../../_images/responses-history.png)

### Lead

By typing `/lead` in the chat window, an operator can create a _lead_ in the
_CRM_ application.

![View of the results from a /lead command in a Live Chat
conversation.](../../../_images/responses-lead.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <code>/lead</code> command can only be used if the <em>CRM</em> app has been installed.</p>
</div>

After typing `/lead`, create a title for this new lead, then press `Enter`. A
link with the lead title appears. Click the link, or navigate to the CRM app
to view the **Pipeline**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The link to the new lead can only be seen and accessed by the operator, not the customer.</p>
</div>

The transcript of that specific live chat conversation (where the lead was
created) is added to the **Internal Notes** tab of the lead form.

On the **Extra Information** tab of the lead form, the **Source** will be
listed as **Livechat**.

### Leave

If an operator types `/leave` in the chat window, they can automatically exit
the conversation. This command does not cause the customer to be removed from
the conversation, nor does it automatically end the conversation.

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../../sales/crm/acquire_leads">Acquire leads</a></p></li>
<li><p><a href="../../services/helpdesk/overview/getting_started">Getting started with Helpdesk</a></p></li>
</ul>
</div>

## Canned responses

_Canned responses_ are customizable inputs where a _shortcut_ stands in for a
longer response. An operator will enter the shortcut, and it will
automatically be replaced by the expanded _substitution_ response in the
conversation.

### Create canned responses

To create a new canned response, go to Live Chat app ‣ Configuration ‣ Canned
Responses ‣ New.

From here, type the shortcut command into the **Shortcut** field.

Then, click into the **Substitution** field, and enter the custom message that
will be sent to visitors in place of the shortcut. Click **Save**.

<div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Try to connect the shortcut to the topic of the substitution. The easier it is for the operators
to remember, the easier it will be to use the canned responses in conversations.</p>
</div>

### Use canned responses in a live chat conversation

To use a canned response during a live chat conversation, type a colon (`:`)
into the chat window, followed by the shortcut.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>An operator is chatting with a visitor. As soon as they type <code>:</code> they would see a list of
available responses. They can manually select one from the list, or continue to type. If they
want to use the canned response <code>'I am sorry to hear that.'</code>, they would type <code>:sorry</code>.</p>
</div> ![View of a chat window and the use of a canned response
in Konvergo ERP Live Chat.](../../../_images/canned-responses.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>The <code>/helpdesk</code> and <code>/helpdesk_search</code> commands can only be used if the <em>Helpdesk</em> app has been
installed, and <em>Live Chat</em> has been activated on a <em>Helpdesk</em> team. To activate <b>Live
Chat</b>, go to Helpdesk application ‣ Configuration ‣ Teams, and select a
team. Scroll to the <b>Channels</b> section and check the box labeled <b>Live Chat</b>.</p>
</div>0

