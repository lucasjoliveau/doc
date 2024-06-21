# Neutralized database

A neutralized database is a non-production database on which several
parameters are deactivated. This enables one to carry out tests without the
risk of launching specific automated processes that could impact production
data (e.g., sending emails to customers). Live access is removed and turned
into a testing environment.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>Any testing database created is a neutralized database:</b></p>
<ul>
<li><p>testing backup databases</p></li>
<li><p>duplicate databases</p></li>
<li><p>for Konvergo ERP.sh: staging and development databases</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>A database can also be neutralized when upgrading, as it is vital to do some tests before
switching to a new version.</p>
</div>

## Deactivated features

Here is a non-exhaustive list of the deactivated parameters:

  * all planned actions (e.g., automatic invoicing of subscriptions, mass mailing, etc.)

  * outgoing emails

  * bank synchronization

  * payment providers

  * delivery methods

  * IAP tokens

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p><b>A red banner at the top of the screen is displayed on the neutralized database so that it can
be seen immediately.</b></p>
</div>

  *[IAP]: In-App Purchase

