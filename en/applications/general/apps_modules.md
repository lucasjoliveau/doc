# Apps and modules

You can install, upgrade and uninstall all apps and modules from the Apps
dashboard.

By default, an _Apps_ filter is applied. If you want to search for modules,
click on _Filters_ and select _Extra_.

![Add "Extra" filter in Odoo Apps](../../_images/apps-search-filter.png)

Warning

Odoo is _not a smartphone_ , and its apps shouldn’t be installed or
uninstalled carelessly. Apply caution when adding or removing apps and modules
on your database since this may impact your subscription costs.

  * **Installing or uninstalling apps and managing users is up to you.**

As the administrator of your database, you are responsible for its usage, as
you know best how your organization works.

  * **Odoo apps have dependencies.**

Installing some apps and features with dependencies may also install
additional apps and modules that are technically required, even if you won’t
actively use them.

  * **Test app installation/removal on a duplicate of your database.**

This way, you can know what app dependencies may be required or what data may
be erased.

## Install apps and modules

Go to Apps, and click on the _Install_ button of the app you want to install.

Note

If the module you are looking for is not listed, you can **update the app
list**.

To do so, activate the [developer mode](developer_mode.html#developer-mode),
then go to Apps ‣ Update Apps List and click on _Update_.

## Upgrade apps and modules

On some occasions, new improvements or app features are added to [supported
versions of Odoo](../../administration/supported_versions.html). To be able to
use them, you must **upgrade** your app.

Go to Apps, click on the _dropdown menu_ of the app you want to upgrade, then
on _Upgrade_.

## Uninstall apps and modules

Go to Apps, click on the _dropdown menu_ of the app you want to uninstall,
then on _Uninstall_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Some apps have dependencies, meaning that one app requires another. Therefore,
uninstalling one app may uninstall multiple apps and modules. Odoo warns you
which dependent apps and modules are affected by it.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

To complete the uninstallation, click on _Confirm_.

Danger

Uninstalling an app also uninstalls all its dependencies and permanently
erases their data.

