# Modo de desarrollador (modo de depuración)

El modo de desarrollador, también conocido como el modo de solución de
errores, desbloquea acceso a herramientas y ajustes avanzados en Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Haga esto con precaución puesto que algunas herramientas y ajustes técnicos del modo de desarrollador pueden tener riesgos asociados. Solo úselos si entiende las implicaciones y sabe lo que está haciendo.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El modo de desarrollador también está disponible con <a href="../../developer/reference/frontend/framework_overview#frontend-framework-assets-debug-mode"><span class="std std-ref">activos</span></a>, que se usan para resolver errores del código de JavaScript y con <a href="../../developer/reference/frontend/framework_overview#frontend-framework-tests-debug-mode"><span class="std std-ref">activos de prueba</span></a>, que se usan cuando se realizan pruebas.</p>
</div>

## Activación

Para activar este modo, abra los **Ajustes** , baje a la sección
**Herramientas de desarrollador** y haga clic en **Activar modo de
desarrollador**.

Una vez que lo active, la opción **Desactivar el modo desarrollador** se
vuelve disponible.

![Activación del modo de desarrollador en la aplicación
Ajustes](../../_images/settings.png)

Para activar el modo de desarrollador **desde cualquier parte de la base de
datos** agregue `?debug=1` a la URL después de `/web` (por ejemplo,
`https://example.odoo.com/web?debug=1#action=menu&cids=1`). Para desactivarlo,
use `?debug=0`.

Use `?debug=assets` el modo de desarrollador con activos y `?debug=tests` para
activarlo con activos de prueba.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Abra la <b>paleta de comandos</b> con las teclas <code>CTRL+K</code> o <code>Cmd ⌘ + K</code> y después escriba <code>debug</code> para activar o desactivar el modo de desarrollador con activos.</p>
</div> <div class="admonition-browser-extension alert">
<p class="alert-title">
Extensión del navegador web</p><p>La extensión de navegador de <a href="https://github.com/Droggol/Konvergo ERPDebug">Konvergo ERP Debug</a> agrega un icono para activar o desactivar el modo de desarrollador desde la barra de herramientas del navegador. Está disponible en <a href="https://chromewebstore.google.com/detail/odoo-debug/hmdmhilocobgohohpdpolmibjklfgkbi">Chrome Web Store</a> y en <a href="https://addons.mozilla.org/firefox/addon/odoo-debug/">Firefox Add-ons</a>.</p>
</div>

## Herramientas de desarrollador y menú técnico

Ya que este activado el modo de desarrollador podrá acceder a las herramientas
de desarrollador haciendo clic en el icono __**(bug)**. El menú contiene
herramientas que son útiles para entender o editar información técnica, como
el campo de una vista, los filtros o las acciones. Las opciones disponibles
dependen de el lugar desde el que accede al menú.

![Acceder a las herramientas de desarrollador](../../_images/tools.png)

Los administradores de una base de datos pueden ingresar el menú técnico desde
los **Ajustes**. Este menú contiene ajustes avanzados para la base de datos,
especialmente aquellos relacionados a la estructura de la base de datos, la
seguridad, las acciones, etc.

![Acceder al menú técnico](../../_images/technical.png)

