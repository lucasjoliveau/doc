# Aplicaciones y módulos

Puede instalar, actualizar y desinstalar todas las aplicaciones y módulos
desde el tablero de Aplicaciones.

El filtro de _aplicaciones_ se aplica de forma predeterminada. Si desea buscar
por _módulos_ , haga clic en _filtros_ y seleccione _extra_.

![Agregar un filtro "Adicional" en las aplicaciones de
Odoo.](../../_images/apps-search-filter.png)

Advertencia

Odoo _no es un celular_ y no puede instalar y desinstalar aplicaciones sin
pensarlo. Tenga cuidado al agregar o eliminar aplicaciones y módulos en su
base de datos, pues esto puede modificar los costos de su suscripción.

  * **Instalar o desinstalar aplicaciones y gestionar usuarios depende de usted.**

Como administrador de su base de datos, es responsable de su uso ya que usted
sabe mejor cómo funciona su empresa.

  * **Las aplicaciones de Odoo tienen dependencias**

Es probable que al instalar algunas aplicaciones y funciones con dependencias
también se instalen aplicaciones y módulos adicionales que, técnicamente, son
necesarios incluso si no los usará de forma activa.

  * **Pruebe instalar/eliminar la aplicación en un duplicado de su base de datos.**

De esta manera, puede saber qué dependencias de la aplicación se necesitan o

## Instale aplicaciones y módulos

Vaya a Aplicaciones, y haga clic en el botón de _instalar_ de la aplicación
que quiere instalar.

Nota

Si el módulo que está buscando no está listado, puede **actualizar la lista de
aplicaciones**.

Para hacerlo, active el [modo de desarrollador](developer_mode.html#developer-
mode), después vaya a Aplicaciones ‣ Actualizar lista de aplicaciones y haga
clic en _Actualizar_.

## Actualice aplicaciones y módulos

En algunas ocasiones, las mejoras o funciones nuevas de las aplicaciones se
agregan a [versiones funcionales de
Odoo](../../administration/supported_versions.html). Para poder usarlas, debe
**actualizar** su aplicación.

Vaya a Aplicaciones, haga clic en el _menú desplegable_ para la aplicación que
quiere actualizar y después haga clic en _Actualizar_.

## Desinstale aplicaciones y módulos

Vaya a Aplicaciones, haga clic en el _menú desplegable_ para la aplicación que
quiere desinstalar y después haga clic en _Desinstalar_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Algunas aplicaciones dependen una de la otra, por lo que si desinstala una de
las aplicaciones, es posible que se desinstalen varias aplicaciones y módulos.
Odoo le advertirá qué aplicaciones o módulos dependientes se verán afectados.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

Para completar la desinstalación haga clic en _Confirmar_.

Peligro

Al desinstalar una aplicación también se desinstalan todas sus dependencias y
borra datos permanentemente.

