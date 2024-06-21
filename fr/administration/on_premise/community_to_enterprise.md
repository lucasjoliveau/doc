# Basculer de Community à Enterprise

En fonction de votre installation actuelle, il existe plusieurs façons de
mettre à niveau votre version Community. Dans tous les cas, les directives de
base sont les suivantes :

  * Sauvegarder votre base de données Community

![../../_images/db_manager.png](../../_images/db_manager.png)

  * Arrêter votre serveur

  * Installer le module web_enterprise

  * Redémarrer votre serveur

  * Saisir votre code d’abonnement Konvergo ERP Enterprise

![../../_images/enterprise_code.png](../../_images/enterprise_code.png)

## Sur Linux, avec un programme d’installation

  * Sauvegarder votre base de données Community

  * Arrêter le service Konvergo ERP
    
        $ sudo service odoo stop
    

  * Installer le .deb enterprise (il devrait s’installer par-dessus le paquet Community)
    
        $ sudo dpkg -i <path_to_enterprise_deb>
    

  * Mettre à niveau votre base de données vers les paquets Enterprise en utilisant
    
        $ python3 /usr/bin/odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * Vous devrez être en mesure de connecter votre instance Konvergo ERP Enterprise en utilisant vos identifiants habituels. Vous pouvez ensuite lier votre base de données à votre abonnement Konvergo ERP Enterprise en saisissant le code que vous avez reçu par email dans le formulaire de saisie

## Sur Linux, avec le code source

Il existe de nombreuses façons de lancer votre serveur lorsque vous utilisez
les sources et vous avez probablement votre source préférée. Il se peut que
vous deviez adapter certaines sections à votre flux de travail habituel.

  * Arrêter votre serveur

  * Sauvegarder votre base de données Community

  * Update the `--addons-path` parameter of your launch command (see [Installation par la source](source))

  * Installer le module web_enterprise en utilisant
    
        $ -d <database_name> -i web_enterprise --stop-after-init
    

En fonction de la taille de votre base de données, cette opération peut
prendre un certain temps.

  * Redémarrer votre serveur avec le chemin d’accès aux modules complémentaires mis à jour au point 3. Vous devez être en mesure de vous connecter à votre instance. Vous pouvez ensuite lier votre base de données à votre abonnement Konvergo ERP Enterprise en saisissant le code que vous avez reçu par email dans le formulaire de saisie

## Sur Windows

  * Sauvegarder votre base de données Community

  * Désinstaller Konvergo ERP Community (en utilisant le fichier Uninstall exécutable dans le dossier d’installation) - PostgreSQL restera installé

![../../_images/windows_uninstall.png](../../_images/windows_uninstall.png)

  * Lancer le programme d’installation Konvergo ERP Enterprise et suivre les étapes normalement. Lorsque vous choisissez le chemin d’installation, vous pouvez définir le dossier de l’installation Community (ce dossier contient toujours l’installation PostgreSQL). Décocher `Lancer Konvergo ERP` à la fin de l’installation.

![../../_images/windows_setup.png](../../_images/windows_setup.png)

  * Dans une fenêtre de commande, mettre à jour votre base de données Konvergo ERP en utilisant cette commande (depuis le chemin d’installation Konvergo ERP, dans le sous-dossier serveur)
    
        $ ..\python\python.exe odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * Il n’est pas nécessaire de lancer le serveur, le service est en cours d’exécution. Vous devrez être en mesure de vous connecter à votre instance Konvergo ERP Enterprise en utilisant vos identifiants habituels. Vous pouvez ensuite lier votre base de données à votre abonnement Konvergo ERP Enterprise en saisissant le code que vous avez reçu par email dans le formulaire de saisie

