# Devices and integrations

VoIP can be used on many different devices, such as a computer, tablet, mobile
phone, and many more. This is helpful in that it reduces costs, and employees
can work from anywhere in the world, so long as they have a broadband internet
connection.

Konvergo ERP _VoIP_ is SIP (Session Initiation Protocol) compatible, which means it
can be used with _any_ SIP compatible application.

This document covers the process of setting up Konvergo ERP _VoIP_ across different
devices and integrations.

Konvergo ERP is fully-integrated with all Konvergo ERP apps, allowing users to click into any
app, and schedule a call as an activity in the chatter.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>For example, in the <em>CRM</em> app, a user can click into an opportunity, and click on
<b>Activities</b> in the chatter.</p>
<p>Next, they can choose <b>Call</b>, and under <b>Due Date</b>, they can select a date.</p>
<p>Once they click <b>Save</b>, an activity shows up in the chatter.</p>
<p>Should the <b>Due Date</b> be for today’s date, the activity shows up in the <abbr title="Voice over Internet Protocol">VoIP</abbr> widget.</p>
<img alt="View of CRM leads and the option to schedule an activity for Konvergo ERP Discuss." class="align-center" src="../../../_images/crm-voip-widget.png"/>
</div>

## Konvergo ERP VoIP (laptop/desktop computer)

The Konvergo ERP _VoIP_ (Voice over Internet Protocol) module and widget can be used
from any browser on a laptop or desktop device. Simply click on the **☎️
(phone)** icon in the upper-right corner, while in the Konvergo ERP database, and the
widget appears.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>To see how to use the <abbr title="Voice over Internet Protocol">VoIP</abbr> widget on a desktop/laptop
computer, check out this documentation: <a href="voip_widget">VoIP widget</a>.</p>
</div>

## Konvergo ERP VoIP (tablet/mobile device)

The Konvergo ERP _VoIP_ app can be used on tablets and mobile phones, through the Konvergo ERP
Android or Apple IOS applications. Additionally, a mobile web browser can be
used to access the database.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Konvergo ERP Android and Apple IOS applications are no longer being maintained by Konvergo ERP on the Android and
Apple portals. This means Konvergo ERP support only handles limited scopes of Konvergo ERP Android or Apple IOS
support tickets.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>While outgoing calls can be placed using Konvergo ERP on a mobile device, be aware that Konvergo ERP is <b>not</b> a
full <abbr title="Voice over Internet Protocol">VoIP</abbr> application, and does <b>not</b> ring on incoming
calls. If the user needs to be reachable on a mobile device at all times, an app, like Zoiper,
should be used. Apps like that stay connected in the background at all times.</p>
<p>For more information, see this documentation: <a href="#voip-zoiper"><span class="std std-ref">Zoiper Lite</span></a>.</p>
</div>

While in the mobile application on a mobile device/tablet, access the Konvergo ERP
_VoIP_ widget, by tapping on the **☎️ (phone)** icon in the upper-right
corner. The widget appears in the lower-left corner.

When first making a call from the tablet using the mobile application, the
user is prompted to **Allow** the database to use the microphone. Click
**Allow** when prompted to continue with the call using the microphone.

This step is **necessary** , whether using the mobile Konvergo ERP application or web
browser.

![Allow the database to access the microphone.](../../../_images/allow-
mic.png)

Konvergo ERP then asks how to make the call. The two options are : **VOIP** or
**Phone** (should the tablet be enabled for calling). Click the box next to
**Remember ?** should this decision be the default moving forward.

![Window prompt to choose whether to use VOIP or the devices phone to make the
call.](../../../_images/voip-phone.png)

Here is the layout of what the Konvergo ERP _VoIP_ app looks like on a mobile device:

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
application, and tap on **Settings**. Navigate to Accounts, and tap on the
**\+ (plus)** icon to add an account.

If the VoIP account is already set up, then click **Yes**. This means an
account username and password has already been produced.

![Zoiper account setup, shown in the view from a mobile
device.](../../../_images/account-settings-zoiper-group.png)

Next, tap on **Select a provider**. On the screen that populates, tap
**Country** , in the upper-right corner, to narrow the providers down to a
specific country. Choose the country for the provider that is being
configured, then find the **Provider** , and select it.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>If the provider being configured is <em>Axivox</em>, then select <b>Belgium</b>. Then, choose
<b>Axivox</b> as the provider.</p>
</div> ![Zoiper account setup, choosing the
provider.](../../../_images/provider-zoiper-odoo.png)

Under SIP options, enter the **Account name** , **Domain** , **Username** ,
and **Password**. All this information varies, based on the account.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>To access this information, via the <em>Axivox</em> portal, navigate to Users ‣ Choose
user ‣ Edit ‣ SIP Identifiers tab. The <b>SIP username</b>, <b>Domain</b>,
<b>SIP password</b>, and <b>Address of the proxy server</b> are all present in this
tab.</p>
</div>  Zoiper Field | Axivox Field  
---|---  
Nom du compte | _Can be anything_  
Domaine | Domaine  
Nom d’utilisateur | SIP username  
Mot de passe | SIP password  
  
Once this account information is entered, click the green **Register** button
at the top of the screen. Once the registration information is checked,
_Zoiper_ populates a message, stating **Registration Status: OK**.

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

From this screen, select **Use SIP Account**. Then, on the following screen,
enter the **Username** , **Password** , **Domain** , and **Display Name**.
Once complete, press **Login**.

At this point, _Linphone_ is ready to start making calls, once there is a
green button at the top of the application screen that reads, **Connected**.

![Linphone account setup, registration successful.](../../../_images/linphone-
odoo-setup.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p><em>Linphone</em> makes a variety of applications for mobile and desktop devices in operating systems,
such as Windows, Linux, Apple, and Android. Because <em>Linphone</em> is an open-source project, many
new updates are released on a regular basis.</p>
<p>See <a href="https://wiki.linphone.org/xwiki/wiki/public/view/Linphone/">Linphone’s wiki-documentation page</a>.</p>
</div>

  *[VoIP]: Voice over Internet Protocol
  *[SIP]: Session Initiation Protocol

