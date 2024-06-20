# Modo de desarrollador (modo de depuración)

El modo de desarrollador, también conocido como el modo de solución de
errores, desbloquea acceso a herramientas y ajustes avanzados en Odoo.

Advertencia

Haga esto con precaución puesto que algunas herramientas y ajustes técnicos
del modo de desarrollador pueden tener riesgos asociados. Solo úselos si
entiende las implicaciones y sabe lo que está haciendo.

Nota

El modo de desarrollador también está disponible con
[activos](../../developer/reference/frontend/framework_overview.html#frontend-
framework-assets-debug-mode), que se usan para resolver errores del código de
JavaScript y con [activos de
prueba](../../developer/reference/frontend/framework_overview.html#frontend-
framework-tests-debug-mode), que se usan cuando se realizan pruebas.

## Activación

Para activar este modo, abra los Ajustes, baje a la sección Herramientas de
desarrollador y haga clic en Activar modo de desarrollador.

Una vez que lo active, la opción Desactivar el modo desarrollador se vuelve
disponible.

![Activación del modo de desarrollador en la aplicación
Ajustes](../../_images/settings.png)

Para activar el modo de desarrollador **desde cualquier parte de la base de
datos** agregue `?debug=1` a la URL después de `/web` (por ejemplo,
`https://example.odoo.com/web?debug=1#action=menu&cids=1`). Para desactivarlo,
use `?debug=0`.

Use `?debug=assets` el modo de desarrollador con activos y `?debug=tests` para
activarlo con activos de prueba.

Truco

Abra la **paleta de comandos** con las teclas `CTRL+K` o `Cmd ⌘ + K` y después
escriba `debug` para activar o desactivar el modo de desarrollador con
activos.

Extensión del navegador web

La extensión de navegador de [Odoo
Debug](https://github.com/Droggol/OdooDebug) agrega un icono para activar o
desactivar el modo de desarrollador desde la barra de herramientas del
navegador. Está disponible en [Chrome Web
Store](https://chromewebstore.google.com/detail/odoo-
debug/hmdmhilocobgohohpdpolmibjklfgkbi) y en [Firefox Add-
ons](https://addons.mozilla.org/firefox/addon/odoo-debug/).

## Herramientas de desarrollador y menú técnico

Ya que este activado el modo de desarrollador podrá acceder a las herramientas
de desarrollador haciendo clic en el icono __(bug). El menú contiene
herramientas que son útiles para entender o editar información técnica, como
el campo de una vista, los filtros o las acciones. Las opciones disponibles
dependen de el lugar desde el que accede al menú.

![Acceder a las herramientas de desarrollador](../../_images/tools.png)

Los administradores de una base de datos pueden ingresar el menú técnico desde
los Ajustes. Este menú contiene ajustes avanzados para la base de datos,
especialmente aquellos relacionados a la estructura de la base de datos, la
seguridad, las acciones, etc.

![Acceder al menú técnico](../../_images/technical.png)

