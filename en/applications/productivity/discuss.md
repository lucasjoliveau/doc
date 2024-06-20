# Discuss

Odoo _Discuss_ is an internal communication app that allows users to connect
through messages, notes, and file sharing, either through a persistent chat
window that works across applications, or through the dedicated _Discuss_
dashboard.

## Choose notifications preference

Access user-specific preferences for the _Discuss_ app by navigating to
Settings app ‣ Users ‣ User ‣ Preferences tab.

![View of the Preferences tab for Odoo Discuss.](../../_images/preferences-
user.png)

By default, the Notification field is set as Handle by Emails. With this
setting enabled, a notification email will be sent by Odoo every time a
message is sent from the chatter, a note is sent with an `@` mention (from
chatter), or a notification is sent for a record that the user follows.
Something that triggers a notification is changing of the stage (if an emailis
configured to be sent, for example if the task is set to Done).

By choosing Handle in Odoo, the above notifications are shown in the _Discuss_
app’s _inbox_. Messages can have the following actions taken on them: respond
with an emoji by clicking Add a Reaction, or reply to the message by clicking
on Reply. Additional actions may include starring the message by clicking
Marked as Todo, or pinning the message by selecting Pin or even mark the
message as unread by selecting Marked as unread.

![View of an inbox message and its action options in Odoo
Discuss.](../../_images/reactions-discuss.png)

Clicking Mark as Todo on a message causes it to appear on the Starred page,
while clicking Mark as Read moves the message to History.

![View of messages marked as todo in Odoo Discuss.](../../_images/starred-
messages.png)

## Start chatting

The first time a user logs in to their account, OdooBot sends a message asking
for permission to send desktop notifications for chats. If accepted, the user
will receive push notifications on their desktop for the messages they
receive, regardless of where the user is in Odoo.

![View of the messages under the messaging menu emphasizing the request for
push notifications for Odoo Discuss.](../../_images/odoobot-push.png)

Tip

To stop receiving desktop notifications, reset the notifications settings of
the browser.

To start a chat, go to the Discuss app and click on the \+ (plus) icon next to
Direct Messages or Channels in the left menu of the dashboard.

![View of Discuss's panel emphasizing the titles channels and direct messages
in Odoo Discuss.](../../_images/channels-direct-messages.png)

A company can also easily create [public and private
channels](discuss/team_communication.html).

### Mentions in the chat and on the chatter

To mention a user within a chat or the chatter, type `@user-name`; to refer to
a channel, type `#channel-name`. The user mentioned will be notified in their
_inbox_ or through an email, depending on their communication settings.

![View of a couple of chat window messages for Odoo
Discuss.](../../_images/chat-windows.png)

Tip

When a user is mentioned, the search list (list of names) suggests values
first based on the task’s followers, and secondly on employees. If the record
being searched does not match with either a follower or employee, the scope of
the search becomes all partners.

### User status

It is helpful to see what colleagues are up to and how quickly they can
respond to messages by checking their _status_. The status is shown on the
left side of a contact’s name on the Discuss sidebar, on the _messaging menu_
and when listed in the _chatter_.

  * Green = online

  * Orange = away

  * White = offline

  * Airplane = out of the office

![View of the contacts' status for Odoo Discuss.](../../_images/status.png)

See also

  * [Use channels for team communication](discuss/team_communication.html)

  * [Activities](../essentials/activities.html)

  * [Use channels for team communication](discuss/team_communication.html)
  * [Configure ICE servers with Twilio](discuss/ice_servers.html)

