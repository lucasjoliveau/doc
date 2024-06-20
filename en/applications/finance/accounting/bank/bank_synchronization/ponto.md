# Ponto

**Ponto** is a service that allows companies and professionals to aggregate
their accounts in one place and directly see all their transactions within one
app. It is a third-party solution that is continuously expanding the number of
bank institutions that can be synchronized with Odoo.

![Logo of the Ponto brand](../../../../../_images/ponto-logo.png)

**Odoo** can synchronize directly with your bank to get all bank statements
imported automatically into your database.

Ponto is a paid third-party provider that can handle the synchronization
between your bank accounts and Odoo. [Its pricing is 4€/month per
account/integration](https://myponto.com/en#pricing).

See also

  * [Bank synchronization](../bank_synchronization.html)

  * [Transactions](../transactions.html)

## Configuration

### Link your bank accounts with Ponto

  1. Go to [Ponto’s website (https://myponto.com)](https://myponto.com).

  2. Create an account if you don’t have one yet.

  3. Once you are logged in, create an _organization_.

![Fill out the form to add an organization in
Ponto.](../../../../../_images/ponto-organization.png)

  4. Go to Accounts ‣ Live, and click on _Add account_.

You might have to add your **Billing Information** first.

  5. Select your country, your bank institutions, give your consent to Ponto, and follow the steps on-screen to link your bank account with your Ponto account.

![Add bank accounts to your Ponto account.](../../../../../_images/ponto-add-
account.png)

  6. Make sure to add all bank accounts you want to synchronize with your Odoo database before moving on to the next steps.

### Link your Ponto account with your Odoo database

  1. Go to Accounting ‣ Configuration ‣ Add a Bank Account.

  2. Search your institution, make sure to select the right institution. By selecting the institution, you can verify that the third party provider is Ponto.

  3. Click on _Connect_ and follow the steps.

  4. At some point, you will have to authorize the accounts you want to access in Odoo. Please select **all the accounts** you want to synchronize. Even the ones coming from other banking institutions.

![Selection of the accounts you wish to synchronize with
Odoo.](../../../../../_images/ponto-select-accounts.png)

  5. Finish the flow.

Note

You have to authorize all the accounts you want to access in Odoo, but Odoo
will filter the accounts based on the institution you selected in the second
step.

### Update your synchronization credentials

You might have to update your Ponto credentials or modify the synchronization
settings.

To do so, go to Accounting ‣ Configuration ‣ Online Synchronization and select
the institution you want to fetch the other accounts. Click on _Fetch
Accounts_ button to start the flow.

During the update, select **all the accounts** you want to synchronize, even
the ones coming from other banking institutions.

### Fetch new accounts

You might want to add new online accounts to your connection.

To do so, go to Accounting ‣ Configuration ‣ Online Synchronization and select
the institution you want to fetch the other accounts. Click on _Fetch
Accounts_ button to start the flow.

Don’t forget to keep authorization for existing accounts (for all institutions
that you have synchronized with Ponto).

## FAQ

### After my synchronization, no account appears

You selected an institution from the list and did not authorize any accounts
from this institution.

### I have an error about that my authorization has expired

Every **3 months** (90 days) you must re-authorize the connection between your
bank account and Ponto. This must be done from the [Ponto
website](https://myponto.com). If you do not do this, the synchronization will
stop for these accounts.

### I have some errors with my beta institution

Ponto provides institutions in _beta_ , these institutions are not directly
supported by Odoo and we advise you to contact Ponto directly.

Important

Using an institution in beta is beneficial for Ponto, it allows them to have
real feedback on the connection with the institution.

