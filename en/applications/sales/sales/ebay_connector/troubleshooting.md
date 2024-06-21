# Troubleshooting eBay connector

<div class="alert alert-secondary">
<p class="alert-title">
See also</p><p>To learn more about the eBay connector visit these pages as well:</p>
<ul>
<li><p><a href="setup">eBay connector setup</a></p></li>
<li><p><a href="manage">How to list a product?</a></p></li>
<li><p><a href="linking_listings">Linking existing listings</a></p></li>
</ul>
</div>

## Accept account deletion notifications

Since September 2021, **eBay requires supporting customer account
deletion/closure notifications**. As such, when eBay receives an account
request for deletion, all eBay partners must confirm the reception of the
request and take further action if necessary.

Konvergo ERP has a notification endpoint to receive those notifications, confirm the
reception of the request, and handle the first set of actions to anonymize the
account details in _Contacts_ and remove the customer’s access to the portal.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Make sure to correctly <a href="#ebay-subscribe-account-deletion-notifications"><span class="std std-ref">set up the subscription to the marketplace account deletion
notifications</span></a> as eBay may temporarily disable
the related eBay account until the subscription is completed.</p>
</div>

### Verify the installation of Konvergo ERP is up to date

In order to activate the endpoint, the module _eBay Connector - Account
Deletion_ must be installed. If the Konvergo ERP database was first created after
September 2021, the module is installed automatically and the administrator
can proceed to the next step.

#### Update Konvergo ERP to the latest release

The notification endpoint is made available through a new Konvergo ERP module; to be
able to install it, the administrator must make sure that the Konvergo ERP source code
is up-to-date.

  * If the company uses Konvergo ERP on Konvergo ERP.com or Konvergo ERP.sh platform, the code is already up-to-date, so proceed to the next step.

  * If the company uses Konvergo ERP with an on-premise setup or through a partner, then the administrator must update the installation as detailed in [this documentation page](../../../../administration/on_premise/update) or by contacting an integrating partner.

#### Update the list of available modules

New modules must be _discovered_ by the Konvergo ERP instance to be available in the
Apps menu.

To do so, activate the [developer
mode](../../../general/developer_mode#developer-mode), and go to Apps ->
Update Apps List. A wizard will ask for confirmation.

#### Install the eBay Connector - Account Deletion update

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p><b>Never</b> install new modules in the production database without testing them in a duplicate or
staging environment. For Konvergo ERP.com customers, a duplicate database can be created from the
database management page. For Konvergo ERP.sh users, the administrator should use a staging or duplicate
database. For on-premise users, the administrator should use a staging environment - contact the
integrating partner for more information regarding how to test a new module in a particular
setup.</p>
</div>

To install the module, go to the Apps menu, remove the `Apps` search facet and
search for `eBay`. If the module _eBay Connector - Account Deletion_ is
present and marked as installed, the Konvergo ERP database is already up-to-date and
the administrator can proceed with the next step. If it is not yet installed,
install it now.

### Retrieve endpoint details from Konvergo ERP

The endpoint details can be found in Sales ‣ Configuration ‣ Settings ‣ eBay.
First, input random text values for the **Production App Key** and for the
**Production Cert Key**. Click on **Generate Token** to retrieve the
**Verification Token**.

![Generate a verification token in Konvergo ERP.](../../../../_images/generate-
token1.png)

### Subscribe to account deletion notifications

Navigate to the [eBay developer portal](https://go.developer.ebay.com/).
Configure the account deletion/notification settings in eBay by navigating to
the `Hi [username]` at the top right of screen, then go to **Alerts &
Notifications**.

![Overview of the Alerts & Notifications dashboard of
eBay](../../../../_images/ebay-your-account.png)

To subscribe to deletion/closure notifications, eBay needs a few details:

  * An _email address_ to send notifications to if the endpoint is unreachable.

  * The _endpoint details_ :

    * The URL to Konvergo ERP’s account deletion notification endpoint

    * A verification token

![Dedicated fields to enter the endpoint details](../../../../_images/ebay-
notification-endpoint.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>The administrator can edit the last two fields once the email address field is filled out.</p>
</div>

### Verify the connectivity with the endpoint

After setting the retrieved endpoint details in eBay’s dashboard, consider
testing the connectivity with the **Send Test Notification** button.

> The following confirmation message should be received: “A test notification
> was sent successfully!”

![Button to send test notification](../../../../_images/test-notification.png)
<div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="manage">How to list a product?</a></p></li>
<li><p><a href="linking_listings">Linking existing listings</a></p></li>
<li><p><a href="setup">eBay connector setup</a></p></li>
</ul>
</div>

