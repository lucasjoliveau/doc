# SMS Pricing and FAQ

## What do I need to send SMSs?

SMS Text Messaging is an In-App Purchase (IAP) service that _requires prepaid
credits_ to work.

## How many types of SMSs are there?

There are 2 types: GSM7 and UNICODE.

**GSM7** is the standard format, with a limit of 160 characters per message,
that includes the following characters:

![GSM7 characters available in Konvergo ERP SMS
Marketing.](../../../../_images/faq1.png)

**UNICODE** is the format applied if a special character, that _is not_ in the
GSM7 list, is used. Limit per SMS: 70 characters.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>For GSM7 SMS the size limit is 160 characters, and for Unicode is 70. <em>Above these limits, the
content is divided into a multi-part message</em> and the limit of characters is lowered to 153 for
GSM7 and to 67 for Unicode. Then, in real-time, the system displays the number of SMS mailings
the message represents.</p>
</div>

## How much does it cost to send an SMS?

The price of an SMS depends on the destination and the length (number of
characters) of the message. To see the **price per country, please consult** :
[Konvergo ERP SMS - FAQ](https://iap-services.odoo.com/iap/sms/pricing#sms_faq_01).

The number of SMSs a message represents will always be available in the
database.

![Number of GSM7 characters that fit in an SMS message in Konvergo ERP SMS
Marketing.](../../../../_images/faq2.png)

## How to buy credits

Go to Settings ‣ Buy Credits.

![Buying credits for SMS Marketing in Konvergo ERP
settings.](../../../../_images/faq3.png)

Or go to Settings ‣ View my Services.

![Using Konvergo ERP IAP to recharge credits for SMS Marketing in Konvergo ERP
settings.](../../../../_images/faq4.png) <div class="alert alert-info">
<p class="alert-title">
Tip</p><p>If Konvergo ERP Online (Saas) is being used, along with the Enterprise version, free trial credits are
available to test the feature.</p>
</div>

## More common questions

  1. **Is there an expiration time for my credits?**

No, credits do not expire.

  2. **Can I send an SMS to a phone number (which is not a mobile phone) because I see the icon in front of the field “phone”?**

Only if that phone number supports SMS (e.g. SIP phones).

  3. **Do I receive an invoice to buy my credits?**

Yes.

  4. **Can the recipient answer me?**

No, it is not possible to reply to the SMS.

  5. **What happens if I send multiple SMSs at once, but I don’t have enough credits to send them all?**

Multiple SMS communications at once at are counted as a single transaction, so
no SMSs will be sent until there are enough credits to send them all.

  6. **Do I have a history of the sent SMSs?**

A history of sent SMSs, along with all pertinent information related to its
sent contacts (and the message itself), can be found in the **Sent** column of
the main **SMS Marketing** dashboard (while in **Kanban** view).

> For more detailed information, select a desired SMS from the main dashboard
> (in **Kanban** view), and click on either link in the blue banner above the
> SMS detail form to learn more.

  7. **Can I send as many SMSs I want at once?**

Yes, if you have enough credits.

  8. **If an SMS is sent to a number that doesn’t exist in the list of recipients, will credits be lost?**

No, not if the phone number is incorrectly formatted (e.g. too many digits).
However, if the SMS is sent to the wrong person (or to a fake number), the
credit for that SMS will be lost.

  9. **What happens if I send my SMS to a paying number (e.g.: a contest to win a ticket for a festival)?**

The SMS will not be delivered to that kind of number, so no charges will be
made.

  10. **Can I identify the numbers that do not exist when I send several SMSs?**

Only the ones that have an invalid format.

  11. **How does the GDPR regulation affect this service?**

Please find our [Privacy Policy here](https://iap.odoo.com/privacy#sms).

  12. **Can I use my own SMS provider?**

Yes, but it is not possible out-of-the-box. Konvergo ERP experts can help customize a
database to allow for the use of a personal SMS provider. Please check our
success packs [here](https://www.odoo.com/pricing-packs).

