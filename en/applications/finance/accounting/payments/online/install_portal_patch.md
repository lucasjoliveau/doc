# Install the patch to disable online invoice payment

Following recent changes in Odoo 16, you might be warned that disabling the
Invoice Online Payment setting will uninstall modules. If you want to disable
the feature without uninstalling modules, follow the steps below to install
the module **Payment - Account / Invoice Online Payment Patch**.

Note

If your Odoo database is created after the module **Payment - Account /
Invoice Online Payment Patch** was released, you don’t have anything to do.

To check if the module is already installed, go to Apps, remove the `Apps`
filter, and search for `account_payment`. If the module **Payment - Account /
Invoice Online Payment Patch** is present and marked as installed, your Odoo
database is already up-to-date and you are able to disable the feature without
side-effect.

## Update Odoo to the latest release

The possibility to disable the Invoice Online Payment setting without side-
effect is made available through a new Odoo module; to be able to install it,
you must make sure that your Odoo source code is up-to-date.

If you use Odoo on Odoo.com or Odoo.sh platform, your code is already up-to-
date and you can proceed to the next step.

If you use Odoo with an on-premise setup or through a partner, you must update
your installation as detailed in [this documentation
page](../../../../../administration/on_premise/update.html), or by contacting
your integrating partner.

## Update the list of available modules

New modules must be _discovered_ by your Odoo instance to be available in the
**Apps** menu.

To do so, activate the [developer
mode](../../../../general/developer_mode.html#developer-mode), and go to Apps
‣ Update Apps List. A wizard will ask for confirmation.

## Install the module Invoice Online Payment Patch

Warning

You should never install new modules in your production database without first
testing them in a duplicate or staging environment. For Odoo.com customers, a
duplicate database can be created from the database management page. For
Odoo.sh users, you should use a staging or duplicate database. For on-premise
users, you should use a staging environment—contact your integrating partner
for more information regarding how to test a new module in your particular
setup.

The module should now be available in your Apps menu. Remove the `Apps` filter
and search for `account_payment`; the module Payment - Account / Invoice
Online Payment Patch should be available for installation. If you cannot find
the module after having updated the list of available modules, it means your
Odoo source code is not up-to-date; refer to step one of this page.

Once the module is installed, disabling the feature will work as intended and
will not ask you to uninstall installed applications or modules.

