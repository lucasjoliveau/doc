# Submódulos

## Información general

Un [submódulo de Git](https://git-scm.com/book/es/v2/Herramientas-de-Git-
Subm%C3%B3dulos) le permite integrar otros proyectos de Git en su código sin
necesidad de copiar y pegar todo el código.

Sus módulos personalizados pueden depender de los módulos de otros
repositorios. En cuanto a Odoo, esta función le permite agregar módulos desde
otros repositorios de Git a las ramas de su repositorio. Agregar estas
dependencias a su rama mediante submódulos hace que el despliegue de su código
y su servidor sea más fácil, ya que puede clonar los repositorios que se
agregaron como submódulos mientras clona su propio repositorio.

Además, puede elegir la rama del repositorio que se agrega como submódulo y
tiene el control de la revisión que desea. Usted decide si quiere anclar el
submódulo a una revisión específica y cuándo quiere actualizarlo a una
revisión más reciente.

En Odoo.sh, los submódulos le dan la posibilidad de usar y depender de módulos
disponibles en otros repositorios. La plataforma detectará que agregó módulos
mediante submódulos en sus ramas y los agregará a su ruta de complementos de
forma automática para que pueda instalarlos en su base de datos.

Si agrega repositorios privados como submódulos a sus ramas, debe configurar
una clave de despliegue en los ajustes de su proyecto de Odoo.sh y en los de
su repositorio. De otra forma, Odoo.sh no podrá descargarlos. El proceso se
describe en el capítulo [Ajustes >
Submódulos](../getting_started/settings.html#odoosh-gettingstarted-settings-
submodules).

## Agregar un submódulo

### Con Odoo.sh (método simple)

Advertencia

Por ahora, no es posible agregar repositorios **privados** con este método
pero puede hacerlo con Git.

En Odoo.sh, en la vista de ramas de su proyecto, elija la rama en la que desea
agregar un submódulo.

En la esquina superior derecha, haga clic en el botón de _Submódulo_ y luego
en _Ejecutar_.

![../../../_images/advanced-submodules-button.png](../../../_images/advanced-
submodules-button.png)

Aparecerá un cuadro de diálogo con un formulario. Complete los campos como se
indica a continuación:

  * URL del repositorio: la URL SSH del repositorio.

  * Rama: la rama que desea utilizar.

  * Ruta: la carpeta en la que desea agregar este submódulo en su rama.

![../../../_images/advanced-submodules-dialog.png](../../../_images/advanced-
submodules-dialog.png)

En GitHub, puede obtener la URL del repositorio con el botón de _Clonar o
descargar_ del repositorio. Asegúrese de _usar SSH_.

![../../../_images/advanced-submodules-github-
sshurl.png](../../../_images/advanced-submodules-github-sshurl.png)

### Con Git (método avanzado)

En una terminal, en la carpeta donde se clonó su repositorio de Git, diríjase
a la rama en la que desea agregar un submódulo:

    
    
    $ git checkout <branch>
    

Luego, agregue el submódulo con el siguiente comando:

    
    
    $ git submodule add -b <branch> <git@yourprovider.com>:<username/repository.git> <path>
    

Reemplace

  * _< git@yourprovider.com>:<username/repository.git>_ con la URL SSH del repositorio que desea agregar como submódulo.

  * _< branch>_ con la rama que desea usar en el repositorio mencionado en el punto anterior.

  * _< path>_ con la carpeta en la que desea agregar este submódulo.

Confirme y suba sus cambios:

    
    
    $ git commit -a && git push -u <remote> <branch>
    

Reemplace

  * <remote> con el repositorio al que desea subir sus cambios. Para una configuración estándar de Git, este es el _origen_.

  * <branch> con la rama a la que desea subir sus cambios. Es muy probable que sea la rama en la que usó el comando `git checkout` en el primer paso.

Puede consultar la [documentación disponible en git-scm.com](https://git-
scm.com/book/en/v2/Git-Tools-Submodules) para obtener más detalles sobre los
submódulos de Git. Por ejemplo, si desea actualizar sus submódulos para que
tengan la revisión más reciente, puede consultar el capítulo [Llegada de los
cambios de Upstream](https://git-scm.com/book/es/v2/Herramientas-de-Git-
Subm%C3%B3dulos).

## Ignorar módulos

Si agrega un repositorio que contiene muchos módulos, es posible que quiera
ignorar algunos de ellos en caso de que se hayan instalado de forma
automática. Para hacerlo, puede agregar el prefijo `.` a la carpeta de su
submódulo. La plataforma ignorará esta carpeta y podrá elegir sus módulos
manualmente al crear enlaces simbólicos para ellos desde otra carpeta.

