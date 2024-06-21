# Unsplash

**Unsplash** is a recognized stock photography library integrated with Konvergo ERP.

If your database is hosted on **Konvergo ERP Online** , you can access Unsplash
pictures without configuration.

If your database is hosted on **Konvergo ERP.sh or on-premise** , proceed as follows:

  1. To **generate an Unsplash access key** , create or sign in to an [Unsplash account](https://unsplash.com).

  2. Access your [applications dashboard](https://unsplash.com/oauth/applications), click **New Application** , select all checkboxes, and click **Accept terms**.

  3. In the pop-up window, enter your **Application Name** , starting with the prefix `Konvergo ERP:` (e.g., `Konvergo ERP: connection`), so Unsplash recognizes it as an Konvergo ERP instance. Then, add a **Description** and click **Create application**.

  4. On the application details page, scroll down to the **Keys** section and copy the **Access Key** and **Application ID**.

  5. In Konvergo ERP, go to General Settings and enable the **Unsplash Image Library** feature. Then, enter the Unsplash **Access Key** and **Application ID**.

<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>As a non-Konvergo ERP Online user, you are limited to a test key with a maximum of 50 Unsplash requests
per hour.</p>
</div>

