# VoIP services in Konvergo ERP with Axivox

## Introduction

Konvergo ERP VoIP (Voice over Internet Protocol) can be set up to work together with
[Axivox](https://www.axivox.com/). In that case, an Asterisk server is **not**
necessary, as the infrastructure is hosted and managed by Axivox.

To use this service, [contact Axivox](https://www.axivox.com/contact/) to open
an account. Before doing so, verify that Axivox covers the company’s area,
along with the areas the company’s users wish to call.

## Configuration

To configure Axivox in Konvergo ERP, go to the Apps application, and search for
`VoIP`. Then, install the **VoIP** module.

Next, go to Settings app ‣ General Settings ‣ Integrations section, and fill
out the **Asterisk (VoIP)** field:

  * **OnSIP Domain** : set the domain created by Axivox for the account (e.g., `yourcompany.axivox.com`)

  * **WebSocket** : type in `wss://pabx.axivox.com:3443`

  * **VoIP Environment** : set as **Production**

![Integration of Axivox as VoIP provider in an Konvergo ERP
database.](../../../../_images/voip-configuration.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Access the domain on the Axivox administrative panel by navigating to <a href="https://manage.axivox.com/">https://manage.axivox.com/</a>. After logging into the portal, go to Users ‣
Edit (next to any user) ‣ SIP Identifiers tab ‣ Domain.</p>
</div>

### Configure VoIP user in Konvergo ERP

Next, the user is configured in Konvergo ERP, which **must** take place for every
Axivox/Konvergo ERP user using VoIP.

In Konvergo ERP, go to Settings app ‣ Users & Companies ‣ Users, then open the desired
user’s form to configure VoIP. Under the **Preferences** tab, fill out the
**VOIP Configuration** section:

  * **VoIP username** / **Browser’s Extension** : (Axivox) **SIP username**

  * **VoIP Secret** : (Axivox) **SIP Password**

  * **External device number** : SIP external phone extension

  * **How to place calls on mobile** : method to make calls on a mobile device

  * **OnSIP Auth User** : (Axivox) **SIP username**

  * **Call from another device** : option to always transfer phone calls to handset

  * **Reject All Incoming Calls** : option to reject all incoming calls

![Integration of Axivox user in the Konvergo ERP user
preference.](../../../../_images/odoo-user.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>Access the domain on the Axivox administrative panel by navigating to <a href="https://manage.axivox.com/">https://manage.axivox.com/</a>. After logging into the portal, go to Users ‣
Edit (next to the user) ‣ SIP Identifiers tab ‣ SIP username / SIP password.</p>
<img alt="SIP credentials in the Axivox manager." class="align-center" src="../../../../_images/manager-sip.png"/>
</div>
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>When entering the <b>SIP Password</b> into the user’s <b>Preferences</b> tab, this
value <b>must</b> be typed out manually and <b>not</b> pasted in. Pasting in causes a <code>401 server
rejection error</code>.</p>
</div>

  *[VoIP]: Voice over Internet Protocol

