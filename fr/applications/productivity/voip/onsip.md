# Utiliser les services VoIP dans Konvergo ERP avec OnSIP

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>OnSIP <abbr title="voice over internet protocol">VoIP</abbr> services are only available in the <b>United
States</b> (US). OnSIP <abbr title="voice over internet protocol">VoIP</abbr> services are widely available in
the lower-48, contiguous United States. In Alaska or Hawaii, charges for service can be higher.</p>
<p>Additionally, a <abbr title="United States">US</abbr> billing address, and <abbr title="United States">US</abbr> credit
card are required to use the service.</p>
<p>Before setting up an account with OnSIP, the business will need to make sure the business
telephone numbers are portable to OnSIP.</p>
<p>OnSIP makes every attempt to work with all telephone service providers. However, certain local or
regional guidelines may preclude the company’s current provider from releasing the number.</p>
</div>

## Introduction

Konvergo ERP _VoIP_ can be set up to work together with [OnSIP (Konvergo ERP Landing
Page)](https://info.onsip.com/odoo/). OnSIP is a VoIP provider. An account is
needed with OnSIP in order to use this service.

Before setting up an account with OnSIP, make sure the company’s home area,
and the areas that will be called, are covered by OnSIP services.

After opening an OnSIP account, follow the configuration procedure below to
configure it on an Konvergo ERP database.

## Configuration

To configure the Konvergo ERP database to connect to OnSIP services, first navigate to
the Apps application from the main Konvergo ERP dashboard. Then, remove the default
`Apps` filter from the **Search…** bar, and search for `VoIP OnSIP`.

Next, install the **VOIP OnSIP** module.

![View of OnSIP app in the app search results.](../../../_images/install-
onsip.png)

### Konvergo ERP VoIP setting

After installing the _VOIP OnSIP_ module, go to the Settings app, scroll down
to the **Integrations** section, and locate the **Asterisk (VoIP)** fields.
Then, proceed to fill in those three fields with the following information:

  * **OnSIP Domain** : the domain that was assigned when creating an account on [OnSIP](https://www.onsip.com/).

  * **WebSocket** : `wss://edge.sip.onsip.com`

  * **VoIP Environment** : **Production**

![VoIP configuration settings in Konvergo ERP Settings
app.](../../../_images/asterisk-setting.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>To access the OnSIP domain, navigate to <a href="https://www.onsip.com/">OnSIP</a> and log in. Then, click
the <b>Administrators</b> link in the top-right of the page.</p>
<p>Next, in the left menu, click <b>Users</b>, and then select any user. By default, the
selected user opens on the <b>User Info</b> tab.</p>
<p>Click on the <b>Phone Settings</b> tab to reveal OnSIP configuration credentials (first
column).</p>
<img alt="Domain setting revealed (highlighted) on administrative panel of OnSIP management console." class="align-center" src="../../../_images/domain-setting.png"/>
</div>

### Konvergo ERP user setting

Next, the user needs to be set up in Konvergo ERP. Every user associated with an OnSIP
user **must** also be configured in the Konvergo ERP user’s settings/preferences.

To do that, navigate to Settings app ‣ Manage Users ‣ Select the User.

On the user form, click **Edit** to configure the user’s OnSIP account. Then,
click the **Preferences** tab, and scroll to the **VoIP** section.

In this section, fill in the fields with OnSIP credentials.

Fill in the following fields with the associated credentials listed below:

  * **VoIP Username** / **Extension Number** = OnSIP **Username**

  * **OnSIP Auth Username** = OnSIP **Auth Username**

  * **VoIP secret** = OnSIP **SIP Password**

  * **External device number** = OnSIP **Ext.** (extension without the `x`)

![OnSIP user credentials with username, auth username, SIP password, and
extension highlighted.](../../../_images/onsip-creds.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>The OnSIP extension can be found in the <em>User</em> banner line above the tabs.</p>
</div>

When these steps are complete, navigate away from the user form in Konvergo ERP to
save the configurations.

Once saved, Konvergo ERP users can make phone calls by clicking the **☎️ (phone)**
icon in the top-right corner of Konvergo ERP.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>Additional setup and troubleshooting steps can be found on <a href="https://support.onsip.com/hc/en-us">OnSIP’s knowledge base</a>.</p>
</div>

### Incoming calls

The Konvergo ERP database also receives incoming calls that produce pop-up windows in
Konvergo ERP. When those call pop-up windows appear, click the green **📞 (phone)**
icon to answer the call.

To ignore the call, click the red **📞 (phone)** icon.

![Incoming call shown in the Konvergo ERP VoIP widget.](../../../_images/incoming-
call.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="voip_widget">VoIP widget</a></p>
</div>

### Aide au dépannage

#### Missing parameters

If a _Missing Parameters_ message appears in the Konvergo ERP widget, make sure to
refresh the Konvergo ERP browser window (or tab), and try again.

![Missing parameter message in the Konvergo ERP VoIP
widget.](../../../_images/onsip04.png)

#### Incorrect number

If an _Incorrect Number_ message appears in the Konvergo ERP widget, make sure to use
the international format for the number. This means leading with the
international country code.

A country code is a locator code that allows access to the desired country’s
phone system. The country code is dialed first, prior to the target number.
Each country in the world has its own specific country code.

For example, `16505555555` (where `1` is the international prefix for the
United States).

![Incorrect number message populated in the Konvergo ERP VoIP
widget.](../../../_images/onsip05.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>For a list of comprehensive country codes, visit: <a href="https://countrycode.org">https://countrycode.org</a>.</p>
</div>

## OnSIP on mobile phone

In order to make and receive phone calls when the user is not in front of Konvergo ERP
on their computer, a softphone app on a mobile phone can be used in parallel
with Konvergo ERP _VoIP_.

This is useful for convenient, on-the-go calls, and to make sure incoming
calls are heard. Any SIP softphone will work.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="devices_integrations">Devices and integrations</a></p></li>
<li><p><a href="https://www.onsip.com/app/download">OnSIP App Download</a></p></li>
</ul>
</div>

