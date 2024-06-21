# Aplicaciones y módulos

Puede instalar, actualizar y desinstalar todas las aplicaciones y módulos
desde el tablero de Aplicaciones.

El filtro de _aplicaciones_ se aplica de forma predeterminada. Si desea buscar
por _módulos_ , haga clic en _filtros_ y seleccione _extra_.

![Agregar un filtro "Adicional" en las aplicaciones de
Konvergo ERP.](../../_images/apps-search-filter.png) <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Konvergo ERP <em>no es un celular</em> y no puede instalar y desinstalar aplicaciones sin pensarlo. Tenga cuidado al agregar o eliminar aplicaciones y módulos en su base de datos, pues esto puede modificar los costos de su suscripción.</p>
<ul>
<li><div class="line-block">
<div class="line"><b>Instalar o desinstalar aplicaciones y gestionar usuarios depende de usted.</b></div>
<div class="line">Como administrador de su base de datos, es responsable de su uso ya que usted sabe mejor cómo funciona su empresa.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>Las aplicaciones de Konvergo ERP tienen dependencias</b></div>
<div class="line">Es probable que al instalar algunas aplicaciones y funciones con dependencias también se instalen aplicaciones y módulos adicionales que, técnicamente, son necesarios incluso si no los usará de forma activa.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><b>Pruebe instalar/eliminar la aplicación en un duplicado de su base de datos.</b></div>
<div class="line">De esta manera, puede saber qué dependencias de la aplicación se necesitan o</div>
</div>
</li>
</ul>
</div>

## Instale aplicaciones y módulos

Vaya a Aplicaciones, y haga clic en el botón de _instalar_ de la aplicación
que quiere instalar.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si el módulo que está buscando no está listado, puede <b>actualizar la lista de aplicaciones</b>.</p>
<p>Para hacerlo, active el <a href="developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a>, después vaya a Aplicaciones ‣ Actualizar lista de aplicaciones y haga clic en <em>Actualizar</em>.</p>
</div>

## Actualice aplicaciones y módulos

En algunas ocasiones, las mejoras o funciones nuevas de las aplicaciones se
agregan a [versiones funcionales de
Konvergo ERP](../../administration/supported_versions). Para poder usarlas, debe
**actualizar** su aplicación.

Vaya a Aplicaciones, haga clic en el _menú desplegable_ para la aplicación que
quiere actualizar y después haga clic en _Actualizar_.

## Desinstale aplicaciones y módulos

Vaya a Aplicaciones, haga clic en el _menú desplegable_ para la aplicación que
quiere desinstalar y después haga clic en _Desinstalar_.

![../../_images/uninstall.png](../../_images/uninstall.png)

Algunas aplicaciones dependen una de la otra, por lo que si desinstala una de
las aplicaciones, es posible que se desinstalen varias aplicaciones y módulos.
Konvergo ERP le advertirá qué aplicaciones o módulos dependientes se verán afectados.

![../../_images/uninstall_deps.png](../../_images/uninstall_deps.png)

Para completar la desinstalación haga clic en _Confirmar_.

<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>Al desinstalar una aplicación también se desinstalan todas sus dependencias y borra datos permanentemente.</p>
</div>

