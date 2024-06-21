# Address autocomplete

You can use the Google Places API on your website to ensure that your users’
delivery addresses exist and are understood by the carrier. The Google Places
API allows developers to access detailed information about places using HTTP
requests. The autocompletion predicts a list of places when the user starts
typing the address.

![Address autocomplete example](../../../../_images/address-autocomplete-
example.png) <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="https://mapsplatform.google.com/maps-products">Google Maps Platform</a></p></li>
<li><p><a href="https://developers.google.com/maps/documentation/places/web-service/autocomplete">Google Developers Documentation: Google Places API</a></p></li>
</ul>
</div>

To do so, go to Website ‣ Configuration ‣ Settings and enable **Address
Autocomplete** in the **SEO** section.

![Enable address autocomplete](../../../../_images/enable-address-
autocomplete.png)

Insert your **Google Places API key** in the **API Key** field. If you don’t
have one, create yours on the [Google Cloud
Console](https://console.cloud.google.com/getting-started) and follow these
steps.

## Step 1: Enable the Google Places API

**Create a New Project:** To enable the **Google Places API** , you first need
to create a project. To do so, click **Select a project** in the top left
corner, **New Project** , and follow the prompts to set up your project.

**Enable the Google Places API:** Go to the **Enabled APIs & Services** and
click **\+ ENABLE APIS AND SERVICES.** Search for **“Places API”** and select
it. Click on the **“Enable”** button.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Google’s pricing depends on the number of requests and their complexity.</p>
</div>

## Step 2: Create API Credentials

Go to [APIs & Services –>
Credentials](https://console.cloud.google.com/apis/credentials).

**Create credentials:** To create your credentials, go to **Credentials** ,
click **Create Credentials** , and select **API key**.

<div class="admonition-restrict-the-api-key-optional alert">
<p class="alert-title">
Restrict the API Key (Optional)</p><p>For security purposes, you can restrict the usage of your API key. You can go to the
<b>API restrictions</b> section to specify which APIs your key can access. For the Google
Places API, you can restrict it to only allow requests from specific websites or apps.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><ul>
<li><p>Save Your API Key: copy your API key and securely store it.</p></li>
<li><p>Do not share it publicly or expose it in client-side code.</p></li>
</ul>
</div>

