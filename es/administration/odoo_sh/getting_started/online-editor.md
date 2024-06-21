# Editor en línea

## Información general

El editor en línea le permite editar el código fuente de sus compilaciones
desde el navegador web. También le da la posibilidad de abrir terminales,
consolas de Pyhton y Shell de Konvergo ERP y
[Notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook).

![../../../_images/interface-editor.png](../../../_images/interface-
editor.png)

Puede acceder al editor de una compilación a través de [las pestañas de las
ramas](branches#odoosh-gettingstarted-branches-tabs), [el menú
desplegable de las compilaciones](builds#odoosh-gettingstarted-builds-
dropdown-menu) o agregando _/odoo-sh/editor_ al nombre del dominio de su
compilación (por ejemplo, _https://odoo-addons-master-1.dev.odoo.com/odoo-
sh/editor_).

## Editar el código fuente

El directorio de trabajo está compuesto por las siguientes carpetas:

    
    
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
    

Puede editar el código fuente (archivos en _/src_) en las compilaciones de
desarrollo y de prueba.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Sus cambios no se propagarán a la nueva compilación, debe confirmarlas en su código fuente si quiere conservarlos.</p>
</div>

Para compilaciones de producción, el código fuente deber ser de solo lectura
porque aplicar cambios locales a un servidor de producción no es una buena
práctica.

  * El código fuente de su repositorio Github está ubicado en _/src/user_ ,

  * El código fuente de Konvergo ERP está ubicado en

    * _/src/odoo_ ([odoo/odoo](https://github.com/odoo/odoo)),

    * _/src/enterprise_ ([odoo/enterprise](https://github.com/odoo/enterprise)),

    * _/src/themes_ ([odoo/design-themes](https://github.com/odoo/design-themes)).

Para abrir un archivo en el editor, solo haga doble clic en panel de
navegación de archivos ubicado a la izquierda.

![../../../_images/interface-editor-open-file.png](../../../_images/interface-
editor-open-file.png)

Puede comenzar a hacer los cambios que desee. Puede guardarlos en el menú
Archivo ‣ Guardar .. Archivo o presionando las teclas ``Ctrl`+`S`` para el
atajo.

![../../../_images/interface-editor-save-file.png](../../../_images/interface-
editor-save-file.png)

Si guarda un archivo Python que está en la ruta de complementos de su servidor
de Konvergo ERP, este lo detectará y lo volverá a cargar en automático para que sus
cambios se apliquen en seguida sin tener que reiniciar el servidor de forma
manual.

![../../../_images/interface-editor-
automaticreload.gif](../../../_images/interface-editor-automaticreload.gif)

Sin embargo, si el cambio es un dato almacenado en la base de datos, como la
etiqueta de un campo o una vista, debe actualizar el módulo correspondiente
para aplicar los cambios. Puede actualizar el módulo del archivo abierto en
ese momento desde el menú Konvergo ERP ‣ Actualizar módulo actual. Tenga en cuenta que
el archivo que se considera abierto en ese momento es el archivo resaltado en
el editor de texto, no el archivo resaltado en el explorador de archivos.

![../../../_images/interface-editor-update-current-
module.png](../../../_images/interface-editor-update-current-module.png)

También puede abrir una terminal y ejecutar el comando:

    
    
    $ odoo-bin -u <comma-separated module names> --stop-after-init
    

## Confirmar y enviar cambios

Tiene la posibilidad de confirmar y subir sus cambios en su repositorio de
Github.

  * Abra una terminal (Archivo ‣ Nuevo ‣ Terminal),

  * Cambie el directorio a _~/src/user_ usando `cd ~/src/user`,

  * Indique sus cambios usando `git add`,

  * Haga commit a sus cambios usando `git commit`,

  * Haga push a sus cambios usando `git push https HEAD:<branch>`.

En este último comando,

  * _https_ es el nombre de su repositorio remoto Github _HTTPS_ (por ejemplo, <https://github.com/username/repository.git>),

  * HEAD es la referencia de la última revisión que realizó,

  * <branch>debe reemplazarse por el nombre de la rama a la cuál quiera subir los cambios, probablemente sea la rama actual si trabaja en una compilación de desarrollo.

![../../../_images/interface-editor-commit-
push.png](../../../_images/interface-editor-commit-push.png)
<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El SSH remoto de GitHub no se usa ya que su clave SSH privada no está alojada en sus contenedores de compilación (por obvios motivos de seguridad) ni se reenvía a través de un agente SSH (al acceder al editor mediante el navegador web) y, por lo tanto, no puede autenticarse en GitHub con SSH. Debe usar el HTTPS remoto de su repositorio de GitHub para poder subir sus cambios, que se agregan en automático con el nombre de <em>https</em> en los Git remotos. Se le pedirá que introduzca su nombre de usuario de GitHub y su contraseña. Si activó la autenticación de dos factores en GitHub, puede crear un <a href="https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens">token de acceso personal</a> que podrá usar como contraseña. Conceder el permiso <code>repo</code> es suficiente.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>La carpeta fuente de Git <em>~/src/user</em> no se comprueba en una rama sino en una revisión separada: esto es porque las compilaciones trabajan en revisiones específicas y no sobre ramas. En otras palabras, esto significa que puede tener varias compilaciones en la misma rama, pero en diferentes revisiones.</p>
</div>

Una vez que los cambios se aplican, de acuerdo a su [comportamiento push de la
rama](branches#odoosh-gettingstarted-branches-tabs-settings), es posible
que se cree una nueva compilación. Puede continuar trabajando en el editor
desde donde los aplico, pues tendrá la misma revisión que la nueva compilación
que se creo. Siempre asegúrese de estar en el editor de una compilación usando
la última revisión de su rama.

## Consolas

Puede abrir las consolas de Python, que son [shells IPython
interactivas](https://ipython.readthedocs.io/en/stable/interactive/tutorial).
Una de las adiciones más interesantes para usar una consola de Python en lugar
de un shell IPhython dentro de una terminal son las capacidades [display
rich](https://ipython.readthedocs.io/en/stable/config/integrating#rich-
display). Gracias a esto, será capaz de mostrar objetos en HTML.

Por ejemplo, puede mostrar celdas de un archivo CSV usando
[pandas](https://pandas.pydata.org/pandas-docs/stable/tutorials).

![../../../_images/interface-editor-console-python-read-
csv.png](../../../_images/interface-editor-console-python-read-csv.png)

También puede abrir la consola de Konvergo ERP Shell para jugar con el registro de
Konvergo ERP y con los métodos del modelo de su base de datos. También puede leer o
escribir directamente en sus registros.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>En una consola de Konvergo ERP, las transacciones se confirman automáticamente. Esto significa, por ejemplo, que los cambios en los registros se aplican efectivamente a las bases de datos. Si cambia el nombre de un usuario, el nombre de ese usuario también cambia en la base de datos. Por lo tanto, debe usar las consolas de Konvergo ERP con cuidado en las bases de datos de producción.</p>
</div>

Puede usar _env_ para invocar modelos del registro de su base de datos, por
ejemplo `env['res.users']`.

    
    
    env['res.users'].search_read([], ['name', 'email', 'login'])
    [{'id': 2,
    'login': 'admin',
    'name': 'Administrator',
    'email': 'admin@example.com'}]
    

La clase `Pretty` le da la posibilidad de mostrar fácilmente listas y dicts de
una manera bonita, usando el [rich
display](https://ipython.readthedocs.io/en/stable/config/integrating#rich-
display) mencionado anteriormente.

![../../../_images/interface-editor-console-odoo-
pretty.png](../../../_images/interface-editor-console-odoo-pretty.png)

También puede usar [pandas](https://pandas.pydata.org/pandas-
docs/stable/tutorials) para mostrar gráficos.

![../../../_images/interface-editor-console-odoo-
graph.png](../../../_images/interface-editor-console-odoo-graph.png)

