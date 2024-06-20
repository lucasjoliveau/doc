# Cambiar de Community a Enterprise

Según la instalación actual, hay varias maneras de actualizar la versión
Community. En cualquier caso, las reglas básicas son:

  * Respalde su base de datos de Community

![../../_images/db_manager.png](../../_images/db_manager.png)

  * Cierre su servidor

  * Instale el módulo web_enterprise

  * Reinicie su servidor

  * Ingrese su código de suscripción para Odoo Enterprise

![../../_images/enterprise_code.png](../../_images/enterprise_code.png)

## En Linux, mediante un instalador

  * Respalde su base de datos de Community

  * Parar el servicio odoo
    
        $ sudo service odoo stop
    

  * Instale el .deb de Enterprise (debería volver a instalar el paquete de community)
    
        $ sudo dpkg -i <path_to_enterprise_deb>
    

  * Actualice su base de datos a los paquetes de enterprise usando
    
        $ python3 /usr/bin/odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * Debería poder conectar su instancia de Odoo Enterprise usando sus medios de identificación usuales. Después puede vincular su base de datos con su suscripción de Odoo Enterprise ingresando el código que recibió en su correo electrónico cuando completó el formulario

## En Linux, usando el código fuente

Hay muchas maneras de lanzar su servidor cuando se utilizan fuentes, y
probablemente tenga su propia favorita. Puede que tenga que adaptar las
secciones a su flujo de trabajo habitual.

  * Cierre su servidor

  * Respalde su base de datos de Community

  * Actualice el parámetro `--addons-path` de su comando de inicio (consulte [Instalación desde la fuente](source.html)).

  * Instale el módulo de web_enterprise con
    
        $ -d <database_name> -i web_enterprise --stop-after-init
    

Dependiendo el tamaño de su base de datos, puede que tarde un poco.

  * Reinicie su servidor con los complementos de ruta del punto 3 actualizados. Debería poder conectarse a su instancia. Después puede vincular su base de datos con su suscripción a Odoo Enterprise, para esto solo debe ingresar el código que recibió por correo electrónico al llenar el formulario

## En Windows

  * Respalde su base de datos de Community

  * Desinstale Odoo Community (mediante el archivo «Uninstall» que se encuentra en la carpeta de instalación) - PostgreSQL debe seguir instalado

![../../_images/windows_uninstall.png](../../_images/windows_uninstall.png)

  * Ejecute el instalador de Odoo Enterprise y siga los pasos como siempre. Al elegir la ruta de instalación puede configurar la carpeta de instalación de Community (esta carpeta aún tendrá la instalación de PostgreSQL). Desmarque `Ejecutar Odoo` al final de la instalación

![../../_images/windows_setup.png](../../_images/windows_setup.png)

  * Con ayuda de la ventana de comando, actualice su base de datos de Odoo con este comando (desde la ruta de instalación de Odoo, en la subcarpeta del servidor)
    
        $ ..\python\python.exe odoo-bin -d <database_name> -i web_enterprise --stop-after-init
    

  * No es necesario lanzar manualmente el servidor, el servicio está funcionando. Debería poder conectarse a su instancia de Odoo Enterprise usando su medio habitual de identificación. A continuación, puede vincular su base de datos con su suscripción a Odoo Enterprise introduciendo el código que recibió por correo electrónico en la entrada del formulario

