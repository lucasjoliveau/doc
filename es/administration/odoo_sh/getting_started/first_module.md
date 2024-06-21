# Su primer módulo

## Información general

Este capítulo le ayudará a crear su primer módulo de Konvergo ERP y desplegarlo en su
proyecto de Konvergo ERP.sh.

Este tutorial requiere [que haya creado un proyecto en
Konvergo ERP.sh](create#odoosh-gettingstarted-create) y conozca la URL de su
repositorio en GitHub.

Se explica el uso básico de Git y GitHub.

Se hacen las siguientes suposiciones:

  * _~/src_ es la carpeta en donde se ubican los repositorios de Git relacionados a sus proyectos de Konvergo ERP.

  * _odoo_ es el usuario de GitHub,

  * _odoo-addons_ es el repositorio de GitHub,

  * _feature-1_ es el nombre de la rama de desarrollo,

  * _master_ es el nombre de la rama de producción,

  * _my_module_ es el nombre del módulo.

Reemplácelos con los valores de su elección.

## Cree la rama de desarrollo

### Desde Konvergo ERP.sh

En la vista de ramas:

  * haga clic en el botón `+` junto a la etapa de desarrollo,

  * seleccione la rama _master_ en la selección _bifurcación_ ,

  * escriba _feature-1_ en la entrada _To_.

![pic1](../../../_images/firstmodule-development-+.png)
![pic2](../../../_images/firstmodule-development-fork.png)

Una vez que haya creado la compilación puede acceder al editor y buscar en la
carpeta _~/src/user_ el código de su rama de desarrollo.

![../../../_images/firstmodule-development-
editor.png](../../../_images/firstmodule-development-editor.png)
![../../../_images/firstmodule-development-editor-
interface.png](../../../_images/firstmodule-development-editor-interface.png)

### Desde su computadora

Clone su repositorio de GitHub en su computadora:

    
    
    $ mkdir ~/src
    $ cd ~/src
    $ git clone https://github.com/odoo/odoo-addons.git
    $ cd ~/src/odoo-addons
    

Cree una nueva rama:

    
    
    $ git checkout -b feature-1 master
    

## Cree una estructura de modelo

### Andamiaje del módulo

Aunque no es necesario, el andamiaje evita la tarea de establecer la
estructura básica de los módulos de Konvergo ERP. Puede usar el andamiaje para crear
un nuevo módulo utilizando _odoo-bin_.

Desde el editor de Konvergo ERP.sh, en una terminal:

    
    
    $ odoo-bin scaffold my_module ~/src/user/
    

O desde su computadora si tiene una [instalación de
Konvergo ERP](../../on_premise/source):

    
    
    $ ./odoo-bin scaffold my_module ~/src/odoo-addons/
    

Si no desea instalar Konvergo ERP en su computadora puede [`descargar esta plantilla
de estructura de
módulo`](../../../_downloads/b7f3a4243ae7f3166cd5c4d23a256739/my_module.zip)
en la cual deberá remplazar cada ocurrencia de _my_module_ con el nombre de su
preferencia.

Se generará la siguiente estructura:

    
    
    my_module
    ├── __init__.py
    ├── __manifest__.py
    ├── controllers
    │   ├── __init__.py
    │   └── controllers.py
    ├── demo
    │   └── demo.xml
    ├── models
    │   ├── __init__.py
    │   └── models.py
    ├── security
    │   └── ir.model.access.csv
    └── views
        ├── templates.xml
        └── views.xml
    

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>No utilice caracteres especiales que no sean el guion bajo ( _ ) para el nombre de su módulo, tampoco puede utilizar guiones ( - ). Este nombre se utiliza para las clases de Python de su módulo y en este lenguaje no es válido tener nombres de clases con caracteres especiales que no sean el guion bajo.</p>
</div>

Descomente el contenido de los archivos:

  * _models/models.py_ , un ejemplo de modelo con sus campos,

  * _views/views.xml_ , un árbol y una vista de formulario, con los menús que los abren,

  * _demo/demo.xml_ , registros de demostración para el modelo del ejemplo anterior,

  * _controllers/controllers.py_ , un ejemplo de controlador que implementa algunas rutas,

  * _views/templates.xml_ , dos ejemplos de vistas qweb utilizadas en las rutas de los controladores anteriores,

  * ___manifest__.py_ , el archivo manifest de su módulo, puede incluir su título, descripción y archivos de datos a cargar. Solo debe descomentar el archivo de datos de la lista de control de acceso:
    
        # 'security/ir.model.access.csv',
    

### Manualmente

Si desea crear la estructura de su módulo de forma manual, siga el tutorial
[Getting started](../../../developer/tutorials/getting_started) para
entender la estructura de un módulo y el contenido de cada archivo.

## Suba la rama de desarrollo

Indique los cambios que se van a realizar.

    
    
    $ git add my_module
    

Confirme los cambios.

    
    
    $ git commit -m "My first module"
    

Envíe los cambios a su repositorio remoto.

Desde una terminal del editor de Konvergo ERP.sh, utilice el siguiente comando:

    
    
    $ git push https HEAD:feature-1
    

El comando anterior se explica en la sección [Confirmar y enviar
cambios](online-editor#odoosh-gettingstarted-online-editor-push) del
capítulo [Editor en línea](online-editor#odoosh-gettingstarted-online-
editor). Incluye la explicación sobre por qué se le pedirá que escriba su
usuario y contraseña, y qué hacer si utiliza la autenticación de dos factores.

O, desde la terminal de la computadora:

    
    
    $ git push -u origin feature-1
    

Es necesario especificar _-u origin feature-1_ solo en el primer push.
Después, para enviar los futuros cambios desde su computadora, puede utilizar
el siguiente comando:

    
    
    $ git push
    

## Pruebe su módulo

Su rama debería aparecer en las ramas de desarrollo de su proyecto.

![../../../_images/firstmodule-test-branch.png](../../../_images/firstmodule-
test-branch.png)

Desde la vista de ramas de su proyecto, puede hacer clic en el nombre de su
rama en el panel de navegación izquierdo para acceder a su historial.

![../../../_images/firstmodule-test-branch-
history.png](../../../_images/firstmodule-test-branch-history.png)

Ahí podrá ver los nuevos cambios, incluido el comentario que escribió. Una vez
que la base de datos esté lista, puede acceder a ella haciendo clic en el
botón _Conectar_.

![../../../_images/firstmodule-test-
database.png](../../../_images/firstmodule-test-database.png)

Si su proyecto de Konvergo ERP.sh está configurado para instalar su módulo de forma
automática, lo verá directamente entre las aplicaciones de la base de datos.
De lo contrario, estará disponible en las aplicaciones a instalar.

A continuación, puede explorar su módulo, crear nuevos registros y probar sus
funciones y botones.

## Probar con los datos de producción

Para este paso necesita tener una base de datos de producción. Puede crearla
si aún no la tiene.

Una vez que haya probado su módulo en una compilación de desarrollo con los
datos de demostración y considere que está listo, puede probarlo con los datos
de producción utilizando una rama de prueba.

Puede:

  * Convertir su rama de desarrollo en una rama de prueba, arrastrándola y soltándola en el título de la sección _de prueba_.

![../../../_images/firstmodule-test-
devtostaging.png](../../../_images/firstmodule-test-devtostaging.png)

  * Fusionarla en una rama de prueba que ya existe, arrastrándola y soltándola en la rama de prueba deseada.

![../../../_images/firstmodule-test-
devinstaging.png](../../../_images/firstmodule-test-devinstaging.png)

También puede utilizar el comando `git merge` para fusionar sus ramas.

Esto creará una nueva compilación de prueba que duplicará la base de datos de
producción y hará que se ejecute utilizando un servidor actualizado con los
últimos cambios de su rama.

![../../../_images/firstmodule-test-
mergedinstaging.png](../../../_images/firstmodule-test-mergedinstaging.png)

Una vez que la base de datos esté lista, puede acceder a ella utilizando el
botón _Conectar_.

### Instale su módulo

Su módulo no se instalará de manera automática, debe instalarlo desde el menú
de aplicaciones. El propósito de la compilación de prueba es probar el
comportamiento de sus cambios para saber cómo funcionarían en producción, y el
resultado esperado no es que su módulo se instale automáticamente en
producción, sino cuando se requiera.

Es posible que su módulo no aparezca directamente en sus aplicaciones a
instalar, primero necesita actualizar su lista de aplicaciones:

  * Active el [modo de desarrollador](../../../applications/general/developer_mode#developer-mode)

  * en el menú de aplicaciones, haga clic en el botón _Actualizar lista de aplicaciones_ ,

  * en el cuadro de diálogo que aparece, haga clic en el botón _Actualizar_.

![../../../_images/firstmodule-test-
updateappslist.png](../../../_images/firstmodule-test-updateappslist.png)

Su módulo aparecerá en la lista de aplicaciones disponibles.

![../../../_images/firstmodule-test-
mymoduleinapps.png](../../../_images/firstmodule-test-mymoduleinapps.png)

## Despliegue en producción

Una vez que haya probado su módulo en una rama de prueba con sus datos de
producción y crea que está listo para enviar a producción, puede fusionar su
rama en la rama de producción.

Arrastre y suelte su rama de prueba en la rama de producción.

![../../../_images/firstmodule-test-
mergeinproduction.png](../../../_images/firstmodule-test-
mergeinproduction.png)

También puede utilizar el comando `git merge` para fusionar sus ramas.

Esto fusionará los últimos cambios de su rama de prueba en la rama de
producción y actualizará su servidor de producción con estos últimos cambios.

![../../../_images/firstmodule-test-
mergedinproduction.png](../../../_images/firstmodule-test-
mergedinproduction.png)

Una vez que la base de datos esté lista, puede acceder a ella utilizando el
botón _Conectar_.

### Instale su módulo

Su módulo no se instalará de manera automática, debe instalarlo por su cuenta
como se explica en la sección anterior sobre la instalación de su módulo en
bases de datos de prueba.

## Agregar un cambio

Esta sección explica cómo agregar un cambio a su módulo añadiendo un nuevo
campo en un modelo y desplegando.

Desde el editor de Konvergo ERP.sh,

    

  * vaya a la carpeta del módulo _~/src/user/my_module_ ,

  * después abra el archivo _models/models.py_.

O desde su computadora,

    

  * utilice su explorador de archivos favorito para ir a la carpeta del módulo _~/src/odoo-addons/my_module_ ,

  * después abra el archivo _models/models.py_ con el editor de su preferencia, puede ser _Atom_ , _Sublime Text_ , _PyCharm_ , _vim_ , …

Luego, después del campo de descripción

    
    
    description = fields.Text()
    

Agregue un campo de fecha y hora

    
    
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    

Luego, abra el archivo _views/views.xml_.

Después de

    
    
    <field name="value2"/>
    

Agregue

    
    
    <field name="start_datetime"/>
    

Estos cambios alteran la estructura de la base de datos al agregar una columna
en una tabla y modficando una vista almacenada en la base de datos.

Para que aplique en bases de datos ya existentes, como en su base de datos de
producción, estos cambios requieren que se actualice el módulo.

Si desea que la actualización se realice de forma automática por la plataforma
de Konvergo ERP.sh cuando aplique sus cambios, mejore la versión de su módulo en su
manifiesto.

Abra el módulo manifiesto ___manifest__.py_.

Reemplace

    
    
    'version': '0.1',
    

con

    
    
    'version': '0.2',
    

La plataforma detectará el cambio de versión y activará la actualización del
módulo después del despliegue de la nueva revisión.

Vaya a su folder Git.

Luego, desde una terminal de Konvergo ERP.sh:

    
    
    $ cd ~/src/user/
    

O, desde la terminal de la computadora:

    
    
    $ cd ~/src/odoo-addons/
    

Luego, indique sus cambios para que se confirmen

    
    
    $ git add my_module
    

Confirme los cambios.

    
    
    $ git commit -m "[ADD] my_module: add the start_datetime field to the model my_module.my_module"
    

Suba sus cambios:

Desde una terminal de Konvergo ERP.sh:

    
    
    $ git push https HEAD:feature-1
    

O, desde la terminal de la computadora:

    
    
    $ git push
    

La plataforma creará una nueva compilación para la rama _feature-1_.

![../../../_images/firstmodule-test-addachange-
build.png](../../../_images/firstmodule-test-addachange-build.png)

Una vez que haya probado sus cambios, puede fusionarlos con la rama de
producción, por ejemplo, arrastre y suelte la rama en la rama de producción en
la interfaz de Konvergo ERP.sh. Cuando actualiza la versión del módulo en el
manifiesto, la plataforma actualizará el módulo automáticamente y su nuevo
campo estará disponible directamente.También puede actualizar el módulo
manualmente dentro de la lista de aplicaciones.

## Usar una biblioteca externa de Python

Si desea usar una biblioteca externa de Python que no está instalada de manera
predeterminada, puede definir un archivo _requirements.txt_ con una lista de
las bibliotecas externas de las que dependa su módulo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>No es posible instalar o actualizar los paquetes del sistema en una base de datos de Konvergo ERP.sh (por ejemplo, herramientas avanzadas de empaquetado). Sin embargo, bajo condiciones específicas, se puede considerar instalar paquetes. Esto también aplica para los <b>módulos de Python</b> que requieren paquetes de sistema para su compilación, y <b>módulos externos de Konvergo ERP</b>.</p></li>
<li><p>Konvergo ERP.sh no admite las <b>extensiones PostgreSQL</b>.</p></li>
<li><p>Para obtener más información, consulte nuestras <a href="https://www.odoo.sh/faq#install_dependencies">preguntas frecuentes</a>.</p></li>
</ul>
</div>

La plataforma usará este archivo automáticamente para instalar las bibliotecas
de Pyhton que su proyecto necesita.

Está función se explica en esta sección usando la [Biblioteca
Unidecode](https://pypi.python.org/pypi/Unidecode) en su módulo.

Cree un archivo _requirements.txt_ en la carpeta principal de su repositorio.

Desde el editor de Konvergo ERP.sh, cree y abra el archivo
~/src/user/requirements.txt.

O, desde su computadora, cree y abra el archivo ~/src/odoo-
addons/requirements.txt.

Agregue

    
    
    unidecode
    

Luego, use la biblioteca en su módulo para quitar acentos de caracteres en el
nombre del campo de su modelo.

Abra el módulo _models/models.py_.

Antes

    
    
    from odoo import models, fields, api
    

Agregue

    
    
    from unidecode import unidecode
    

Después de

    
    
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    

Agregue

    
    
    @api.model
    def create(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).create(values)
    
    def write(self, values):
        if 'name' in values:
            values['name'] = unidecode(values['name'])
        return super(my_module, self).write(values)
    

Agregar una dependencia de Python requiere una actualización de la versión del
módulo para que la plataforma lo instale.

Edite el módulo manifiesto ___manifest__.py_

Reemplace

    
    
    'version': '0.2',
    

con

    
    
    'version': '0.3',
    

Prepare y confirme sus cambios:

    
    
    $ git add requirements.txt
    $ git add my_module
    $ git commit -m "[IMP] my_module: automatically remove special chars in my_module.my_module name field"
    

Luego, suba sus cambios:

En una terminal de Konvergo ERP.sh:

    
    
    $ git push https HEAD:feature-1
    

En la terminal de su computadora:

    
    
    $ git push
    

