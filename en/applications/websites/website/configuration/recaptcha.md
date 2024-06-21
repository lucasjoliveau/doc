# reCAPTCHA v3 on forms

Google’s reCAPTCHA protects website forms against spam and abuse. It attempts
to distinguish between human and bot submissions.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>reCAPTCHA v3 may not be compliant with local data protection regulations.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>reCAPTCHA v3 works in the background and does not interrupt visitors. However, if the check
fails, visitors cannot submit the form.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><p><a href="https://developers.google.com/recaptcha/docs/v3">Google’s reCAPTCHA v3 guide</a></p>
</div>

## Configuration

### On Google

Open [the reCAPTCHA website registration
page](https://www.google.com/recaptcha/admin/create). Log in or create a
Google account if necessary.

On the website registration page:

  * Give the website a **Label**.

  * Leave the **reCAPTCHA type** on **Score based (v3)**.

  * Enter one or more **Domains** (e.g., _example.com_ or _subdomain.example.com_).

  * Under **Google Cloud Platform** , a project is automatically selected if one was already created with the logged-in Google account. If not, one is automatically created. Click **Google Cloud Platform** to select a project yourself or rename the automatically created project.

  * Agree to the terms of service.

  * Click **Submit**.

![reCAPTCHA website registration example](../../../../_images/recaptcha-
google-configuration.png)

A new page with the generated keys is then displayed. Leave it open for
convenience, as copying the keys to Konvergo ERP is required next.

### On Konvergo ERP

  * From the database dashboard, click **Settings**. Under **Integrations** , enable **reCAPTCHA** if needed.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Do not disable the <b>reCAPTCHA</b> feature or uninstall the <b>Google reCAPTCHA
integration</b> module, as many other modules would also be removed.</p>
</div>

  * Open the Google reCAPTCHA page, copy the **Site key** , and paste it into the **Site Key** field in Konvergo ERP.

  * Open the Google reCAPTCHA page, copy the **Secret key** , and paste it into the **Secret Key** field in Konvergo ERP.

  * Change the default **Minimum score** (`0.5`) if necessary, using a value between `1.0` and `0.0`. The higher the threshold is, the more difficult it is to pass the reCAPTCHA, and vice versa.

  * Click **Save**.

All pages using the **Form** , **Newsletter Block** , **Newsletter Popup**
snippets, and the eCommerce **Extra Step During Checkout** form are now
protected by reCAPTCHA.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>If the reCAPTCHA check fails, the following error message is displayed:</p>
<img alt="Google reCAPTCHA verification error message" src="../../../../_images/recaptcha-error.png"/>
</li>
<li><p>reCAPTCHA v3 is free for up to <a href="https://developers.google.com/recaptcha/docs/faq#are-there-any-qps-or-daily-limits-on-my-use-of-recaptcha">1 million assessments per month</a>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Tip</p><ul>
<li><p>Analytics and additional settings are available on <a href="https://www.google.com/recaptcha/admin/">Google’s reCAPTCHA administration page</a>. For example, you can receive email alerts if
Google detects suspicious traffic on your website or view the percentage of suspicious
requests, which could help you determine the right minimum score.</p></li>
<li><p>You can notify visitors that reCAPTCHA protects a form. To do so, open the website editor
and navigate to the form. Then, click somewhere on the form, and on the right sidebar’s
<b>Customize</b> tab, toggle <b>Show reCAPTCHA Policy</b> found under the
<b>Form</b> section.</p></li>
</ul>
<img alt="reCAPTCHA policy message displayed on a form" src="../../../../_images/recaptcha-policy.png"/>
</div>

