# Devices and integrations

VoIP can be used on many different devices, such as a computer, tablet, mobile
phone, and many more. This is helpful in that it reduces costs, and employees
can work from anywhere in the world, so long as they have a broadband internet
connection.

Odoo _VoIP_ is SIP (Session Initiation Protocol) compatible, which means it
can be used with _any_ SIP compatible application.

This document covers the process of setting up Odoo _VoIP_ across different
devices and integrations.

Odoo is fully-integrated with all Odoo apps, allowing users to click into any
app, and schedule a call as an activity in the chatter.

Example

For example, in the _CRM_ app, a user can click into an opportunity, and click
on Activities in the chatter.

Next, they can choose Call, and under Due Date, they can select a date.

Once they click Save, an activity shows up in the chatter.

Should the Due Date be for today’s date, the activity shows up in the VoIP
widget.

![View of CRM leads and the option to schedule an activity for Odoo
Discuss.](../../../_images/crm-voip-widget.png)

## Odoo VoIP (laptop/desktop computer)

The Odoo _VoIP_ (Voice over Internet Protocol) module and widget can be used
from any browser on a laptop or desktop device. Simply click on the ☎️ (phone)
icon in the upper-right corner, while in the Odoo database, and the widget
appears.

See also

To see how to use the VoIP widget on a desktop/laptop computer, check out this
documentation: [VoIP widget](voip_widget.html).

## Odoo VoIP (tablet/mobile device)

The Odoo _VoIP_ app can be used on tablets and mobile phones, through the Odoo
Android or Apple IOS applications. Additionally, a mobile web browser can be
used to access the database.

Warning

Odoo Android and Apple IOS applications are no longer being maintained by Odoo
on the Android and Apple portals. This means Odoo support only handles limited
scopes of Odoo Android or Apple IOS support tickets.

Important

While outgoing calls can be placed using Odoo on a mobile device, be aware
that Odoo is **not** a full VoIP application, and does **not** ring on
incoming calls. If the user needs to be reachable on a mobile device at all
times, an app, like Zoiper, should be used. Apps like that stay connected in
the background at all times.

For more information, see this documentation: Zoiper Lite.

While in the mobile application on a mobile device/tablet, access the Odoo
_VoIP_ widget, by tapping on the ☎️ (phone) icon in the upper-right corner.
The widget appears in the lower-left corner.

When first making a call from the tablet using the mobile application, the
user is prompted to Allow the database to use the microphone. Click Allow when
prompted to continue with the call using the microphone.

This step is **necessary** , whether using the mobile Odoo application or web
browser.

![Allow the database to access the microphone.](../../../_images/allow-
mic.png)

Odoo then asks how to make the call. The two options are : VOIP or Phone
(should the tablet be enabled for calling). Click the box next to Remember ?
should this decision be the default moving forward.

![Window prompt to choose whether to use VOIP or the devices phone to make the
call.](../../../_images/voip-phone.png)

Here is the layout of what the Odoo _VoIP_ app looks like on a mobile device:

![Layout of what the VoIP app looks like on the a mobile
device.](../../../_images/voip-odoo-dashboard.png)

## Zoiper Lite

_Zoiper Lite_ is a free VoIP SIP dialer with voice and video.

To start using the _Zoiper_ app, download it to the device, via the [Zoiper
download page](https://www.zoiper.com/en/voip-softphone/download/current).

A mobile device is the most common installation, and this document covers how
to set up on the _Zoiper_ IOS application. Screenshots and steps may differ
depending on the set up conditions.

After installing the _Zoiper_ application on the mobile phone, open the
application, and tap on Settings. Navigate to Accounts, and tap on the \+
(plus) icon to add an account.

If the VoIP account is already set up, then click Yes. This means an account
username and password has already been produced.

![Zoiper account setup, shown in the view from a mobile
device.](../../../_images/account-settings-zoiper-group.png)

Next, tap on Select a provider. On the screen that populates, tap Country, in
the upper-right corner, to narrow the providers down to a specific country.
Choose the country for the provider that is being configured, then find the
Provider, and select it.

Example

If the provider being configured is _Axivox_ , then select Belgium. Then,
choose Axivox as the provider.

![Zoiper account setup, choosing the provider.](../../../_images/provider-
zoiper-odoo.png)

Under SIP options, enter the Account name, Domain, Username, and Password. All
this information varies, based on the account.

Tip

To access this information, via the _Axivox_ portal, navigate to Users ‣
Choose user ‣ Edit ‣ SIP Identifiers tab. The SIP username, Domain, SIP
password, and Address of the proxy server are all present in this tab.

Zoiper Field | Axivox Field  
---|---  
Account name | _Can be anything_  
Domain | Domain  
Username | SIP username  
Password | SIP password  
  
Once this account information is entered, click the green Register button at
the top of the screen. Once the registration information is checked, _Zoiper_
populates a message, stating Registration Status: OK.

At this point, _Zoiper_ is now set up to make phone calls using the VoIP
service.

![Zoiper account setup, registration successful.](../../../_images/sip-
options-zoiper.png)

## Linphone

_Linphone_ is an open-source VoIP SIP softphone, used for voice, video,
messaging (group and individual), as well as conference calls.

To start using the _Linphone_ app, download it to the device, via the
[Linphone download page](https://new.linphone.org/technical-
corner/linphone?qt-technical_corner=2#qt-technical_corner).

A mobile device is the most common installation, and this document covers how
to set up the _Linphone_ IOS application. Screenshots and steps may differ
depending on the circumstances.

To begin configuring _Linphone_ for use with a SIP provider, first open
_Linphone_ , and an assistant screen appears.

From this screen, select Use SIP Account. Then, on the following screen, enter
the Username, Password, Domain, and Display Name. Once complete, press Login.

At this point, _Linphone_ is ready to start making calls, once there is a
green button at the top of the application screen that reads, Connected.

![Linphone account setup, registration successful.](../../../_images/linphone-
odoo-setup.png)

Tip

 _Linphone_ makes a variety of applications for mobile and desktop devices in
operating systems, such as Windows, Linux, Apple, and Android. Because
_Linphone_ is an open-source project, many new updates are released on a
regular basis.

See [Linphone’s wiki-documentation
page](https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/).

  *[VoIP]: Voice over Internet Protocol
  *[SIP]: Session Initiation Protocol

