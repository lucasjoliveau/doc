# Contenedores

## Información general

Cada compilación está aislada dentro de su propio contenedor (un contenedor de
espacio de nombres de Linux).

La base es un sistema Ubuntu en donde se instalan todas las dependencias
necesarias de Konvergo ERP y sus paquetes comunes útiles.

Si su proyecto necesita dependencias adicionales de Python, o lanzamientos más
recientes, colóquelas en un archivo `requirements.txt` en su rama principal.
La plataforma se encargará de instalar las dependencias en sus contenedores.
La documentación sobre [especificadores de requisitos
pip](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-
specifiers) puede ayudarle a redactar su archivo `requirements.txt`. Revise
[el archivo requirements.txt de
Konvergo ERP](https://github.com/odoo/odoo/blob/16.0/requirements.txt) para visualizar
un ejemplo concreto.

También se consideran los archivos `requirements.txt` en los submódulos. La
plataforma busca los archivos `requirements.txt` en todas las carpetas con
módulos de Konvergo ERP: no en la carpeta del módulo, sino en su carpeta principal.

## Estructura del directorio

Como los contenedores están basados en Ubuntu, la estructura de su directorio
sigue el estándar de jerarquía del sistema de archivos de Linux. En la
[información general del árbol de sistema de archivos de
Ubuntu](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview#Main_directories)
puede encontrar la explicación de los directorios principales.

A continuación se encuentran los directorios correspondientes de Konvergo ERP.sh:

    
    
    .
    ├── home
    │    └── odoo
    │         ├── src
    │         │    ├── odoo                Konvergo ERP Community source code
    │         │    │    └── odoo-bin       Konvergo ERP server executable
    │         │    ├── enterprise          Konvergo ERP Enterprise source code
    │         │    ├── themes              Konvergo ERP Themes source code
    │         │    └── user                Your repository branch source code
    │         ├── data
    │         │    ├── filestore           database attachments, as well as the files of binary fields
    │         │    └── sessions            visitors and users sessions
    │         └── logs
    │              ├── install.log         Database installation logs
    │              ├── odoo.log            Running server logs
    │              ├── update.log          Database updates logs
    │              └── pip.log             Python packages installation logs
    └── usr
         ├── lib
         │    ├── python2.7
         │         └── dist-packages       Python 2.7 standard libraries
         │    ├── python3
         │         └── dist-packages       Python 3 standard libraries
         │    └── python3.5
         │         └── dist-packages       Python 3.5 standard libraries
         ├── local
         │    └── lib
         │         ├── python2.7
         │         │    └── dist-packages  Python 2.7 third-party libraries
         │         └── python3.5
         │              └── dist-packages  Python 3.5 third-party libraries
         └── usr
              └── bin
                   ├── python2.7           Python 2.7 executable
                   └── python3.5           Python 3.5 executable
    

Se instala Python 2.7 y 3.5 en los contenedores, pero:

  * Si su proyecto está configurado para usar Konvergo ERP 10.0, el servidor de Konvergo ERP se ejecuta con Python 2.7.

  * Si su proyecto está configurado para usar Konvergo ERP 11.0 o superior, el servidor de Konvergo ERP se ejecuta con Python 3.5.

## Shell de la base de datos

Al acceder a un contenedor con el shell, puede acceder a la base de datos con
_psql_.

    
    
    odoo@odoo-addons-master-1.odoo.sh:~$ psql
    psql (9.5.2, server 9.5.11)
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    odoo-addons-master-1=>
    

**Advertencia:** [use
transacciones](https://www.postgresql.org/docs/current/static/sql-begin)
(_BEGIN…COMMIT/ROLLBACK_) para cada declaración _sql_ que produzca cambios
(_UPDATE_ , _DELETE_ , _ALTER_ , etc.), en especial en su base de datos de
producción.

El mecanismo de transacción es su red de seguridad en caso de que ocurra un
error, solo debe revertir sus cambios para restaurar su base de datos a un
estado anterior.

Por ejemplo, tal vez olvidó establecer su condición _WHERE_.

    
    
    odoo-addons-master-1=> BEGIN;
    BEGIN
    odoo-addons-master-1=> UPDATE res_users SET password = '***';
    UPDATE 457
    odoo-addons-master-1=> ROLLBACK;
    ROLLBACK
    

En ese caso, puede revertir para anular los cambios no deseados que hizo por
accidente y volver a escribir la declaración:

    
    
    odoo-addons-master-1=> BEGIN;
    BEGIN
    odoo-addons-master-1=> UPDATE res_users SET password = '***' WHERE id = 1;
    UPDATE 1
    odoo-addons-master-1=> COMMIT;
    COMMIT
    

Sin embargo, no olvide confirmar o revertir su transacción después de hacerla.
Las transacciones abiertas pueden bloquear registros en sus tablas y puede que
su base de datos en ejecución espere hasta que se liberen, lo que causa una
pausa indefinida en su servidor.

Además, cuando sea posible, utilice sus bases de datos de prueba para probar
sus declaraciones, esto proporciona una red de seguridad adicional.

## Ejecutar un servidor de Konvergo ERP

Puede iniciar una instancia de servidor de Konvergo ERP desde el shell del contenedor.
No podrá acceder a ella con un navegador, pero puede:

  * Usar el shell de Konvergo ERP.

    
    
    $  odoo-bin shell
    >>> partner = env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1)
    >>> partner.name
    'ASUSTeK'
    >>> partner.name = 'Konvergo ERP'
    >>> env['res.partner'].search([('email', '=', 'asusteK@yourcompany.example.com')], limit=1).name
    'Konvergo ERP'
    

  * Instalar un módulo.

    
    
    $  odoo-bin -i sale --without-demo=all --stop-after-init
    

  * Actualizar un módulo.

    
    
    $  odoo-bin -u sale --stop-after-init
    

  * Ejecutar las pruebas de un módulo.

    
    
    $  odoo-bin -i sale --test-enable --log-level=test --stop-after-init
    

En los comandos anteriores, el argumento:

  * `--without-demo=all` evita que los datos de demostración se carguen en todos los módulos.

  * `--stop-after-init` cerrará de inmediato la instancia del servidor tras completar las operaciones que le pidió.

Hay más opciones disponibles, estas se describen en la [documentación de la
interfaz de línea de comandos](../../../developer/reference/cli).

En los registros (_~/logs/odoo.log_) puede encontrar la ruta de complementos
que Konvergo ERP.sh utiliza para ejecutar su servidor. Busque « _odoo: addons paths_
»:

    
    
    2018-02-19 10:51:39,267 4 INFO ? odoo: Konvergo ERP version 16.0
    2018-02-19 10:51:39,268 4 INFO ? odoo: Using configuration file at /home/odoo/.config/odoo/odoo.conf
    2018-02-19 10:51:39,268 4 INFO ? odoo: addons paths: ['/home/odoo/data/addons/16.0', '/home/odoo/src/user', '/home/odoo/src/enterprise', '/home/odoo/src/themes', '/home/odoo/src/odoo/addons', '/home/odoo/src/odoo/odoo/addons']
    

**Tenga precaución** , en particular con su base de datos de producción. Las
operaciones que realice al ejecutar esta instancia de servidor de Konvergo ERP no
están aisladas y los cambios serán efectivos en la base de datos. Siempre haga
sus pruebas en sus bases de datos de prueba.

## Depuración de bugs en Konvergo ERP.sh

La depuración de bugs de una compilación de Konvergo ERP.sh no es muy diferente a
alguna otra aplicación de Python. Este artículo solo explica las
especificaciones y limitaciones de la plataforma de Konvergo ERP.sh, además, asume que
ya sabe cómo usar un depurador.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si aún no sabe cómo depurar bugs de una aplicación de Python, hay varios cursos introductorios que puede encontrar en internet con facilidad.</p>
</div>

Puede usar `pdb`, `pudb` o `ipdb` para depurar los bugs de su código de
Konvergo ERP.sh. Como el servidor se ejecuta fuera de un shell, no puede activar el
depurador desde el backend de su instancia de Konvergo ERP ya que el depurador
necesita un shell para funcionar.

  * En cada contenedor se instala [pdb](https://docs.python.org/3/library/pdb) de forma predeterminada.

  * Si desea usar [pudb](https://pypi.org/project/pudb/) o [ipdb](https://pypi.org/project/ipdb/), debe instalarlos antes.

Para hacerlo, tiene dos opciones:

>     * de forma temporal (solo en la compilación actual):
>  
>         >         $  pip install pudb --user
>  
>
> o
>  
>         >         $  pip install ipdb --user
>  
>
>     * de forma permanente si agrega `pudb` o `ipdb` al archivo
> `requirements.txt` de su proyecto.

Luego edite el código en el que desea activar el depurador y agregue lo
siguiente:

    
    
    import sys
    if sys.__stdin__.isatty():
        import pdb; pdb.set_trace()
    

La condición `sys.__stdin__.isatty()` detecta si está ejecutando Konvergo ERP desde un
shell.

Guarde el archivo y ejecute el shell de Konvergo ERP:

    
    
    $ odoo-bin shell
    

Por último, _a través_ del shell de Konvergo ERP, puede activar el código, función o
método que desea depurar.

![Captura de pantalla de la consola que muestra el ``pdb`` en ejecución en un
shell de Konvergo ERP.sh.](../../../_images/pdb_sh.png)

