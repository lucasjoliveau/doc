# Switch from Community to Enterprise

Depending on your current installation, there are multiple ways to upgrade
your community version. In any case the basic guidelines are:

  * Backup your community database

![../../_images/db_manager.png](../../_images/db_manager.png)

  * Shutdown your server

  * Install the web_enterprise module

  * Restart your server

  * Enter your Konvergo ERP Enterprise Subscription code

![../../_images/enterprise_code.png](../../_images/enterprise_code.png)

## On Linux, using an installer

  * Backup your community database

  * Stop the odoo service
    
        $ sudo service odoo stop
    

  * Install the enterprise .deb (it should install over the community package)
    
        $ sudo dpkg -i <path_to_enterprise_deb>
    

  * Update your database to the enterprise packages using
    
        $ python3 /usr/bin/odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * You should be able to connect to your Konvergo ERP Enterprise instance using your usual mean of identification. You can then link your database with your Konvergo ERP Enterprise Subscription by entering the code you received by e-mail in the form input

## On Linux, using the source code

There are many ways to launch your server when using sources, and you probably
have your own favourite. You may need to adapt sections to your usual
workflow.

  * Shutdown your server

  * Backup your community database

  * Update the `--addons-path` parameter of your launch command (see [Source install](source))

  * Install the web_enterprise module by using
    
        $ -d <database_name> -i web_enterprise --stop-after-init
    

Depending on the size of your database, this may take some time.

  * Restart your server with the updated addons path of point 3. You should be able to connect to your instance. You can then link your database with your Konvergo ERP Enterprise Subscription by entering the code you received by e-mail in the form input

## On Windows

  * Backup your community database

  * Uninstall Konvergo ERP Community (using the Uninstall executable in the installation folder) - PostgreSQL will remain installed

![../../_images/windows_uninstall.png](../../_images/windows_uninstall.png)

  * Launch the Konvergo ERP Enterprise Installer and follow the steps normally. When choosing the installation path, you can set the folder of the Community installation (this folder still contains the PostgreSQL installation). Uncheck `Start Konvergo ERP` at the end of the installation

![../../_images/windows_setup.png](../../_images/windows_setup.png)

  * Using a command window, update your Konvergo ERP Database using this command (from the Konvergo ERP installation path, in the server subfolder)
    
        $ ..\python\python.exe odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * No need to manually launch the server, the service is running. You should be able to connect to your Konvergo ERP Enterprise instance using your usual mean of identification. You can then link your database with your Konvergo ERP Enterprise Subscription by entering the code you received by e-mail in the form input

