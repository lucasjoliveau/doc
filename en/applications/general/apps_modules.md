# Apps and modules

You can install, upgrade and uninstall all apps and modules from the Apps
dashboard.

By default, an _Apps_ filter is applied. If you want to search for modules,
click on _Filters_ and select _Extra_.

![Add "Extra" filter in Konvergo ERP Apps](../../_images/apps-search-filter.png)
<div class="alert alert-warning">
<p class="alert-title">
Warning</p><p>Konvergo ERP is <em>not a smartphone</em>, and its apps shouldn’t be installed or uninstalled carelessly. Apply
caution when adding or removing apps and modules on your database since this may impact your
subscription costs.</p>
<ul>
<li><div class="line-block">
<div class="line"><b>Installing or uninstalling apps and managing users is up to you.</b></div>
<div class="line">As the administrator of your database, you are responsible for its usage, as you know best
how your organization works.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>Konvergo ERP apps have dependencies.</b></div>
<div class="line">Installing some apps and features with dependencies may also install additional apps and
modules that are technically required, even if you won’t actively use them.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>Test app installation/removal on a duplicate of your database.</b></div>
<div class="line">This way, you can know what app dependencies may be required or what data may be erased.</div>
</div>
</li>
</ul>
</div>

## Install apps and modules

Go to Apps, and click on the _Install_ button of the app you want to install.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If the module you are looking for is not listed, you can <b>update the app list</b>.</p>
<p>To do so, activate the <a href="developer_mode#developer-mode"><span class="std std-ref">developer mode</span></a>, then go to Apps
‣ Update Apps List and click on <em>Update</em>.</p>
</div>

## Upgrade apps and modules

On some occasions, new improvements or app features are added to [supported
versions of Konvergo ERP](../../administration/supported_versions). To be able to
use them, you must **upgrade** your app.

Go to Apps, click on the _dropdown menu_ of the app you want to upgrade, then
on _Upgrade_.

## Uninstall apps and modules

Go to Apps, click on the _dropdown menu_ of the app you want to uninstall,
then on _Uninstall_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Some apps have dependencies, meaning that one app requires another. Therefore,
uninstalling one app may uninstall multiple apps and modules. Konvergo ERP warns you
which dependent apps and modules are affected by it.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

To complete the uninstallation, click on _Confirm_.

<div class="alert alert-danger">
<p class="alert-title">
Danger</p><p>Uninstalling an app also uninstalls all its dependencies and permanently erases their data.</p>
</div>

