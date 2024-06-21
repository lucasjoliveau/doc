# Propiedades

Las propiedades son campos que contienen datos y que cualquier usuario con
permiso de **edición** puede agregar a los artículos. Todos los subartículos y
elementos de artículo en el mismo artículo principal comparten estos campos.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo puede agregar propiedades a un artículo que sea un <b>subartículo</b> o un <b>elemento de artículo</b>.</p>
</div>

## Agregar campos de propiedad

Coloque el ratón sobre el encabezado de primer nivel para ver los botones.
Haga clic en ⚙ Agregar propiedades ‣ Tipo de campo, seleccione el tipo y
agregue un valor predeterminado si es necesario. Para que el campo aparezca en
las **vistas de kanban** seleccione la opción **ver en kanban**. Haga clic en
cualquier parte de la pantalla para validar y cerrar la ventana de creación de
propiedades.

![Lista desplegable con los tipos de campos de
propiedades](../../../_images/fields.png)

Los distintos tipos definen cuál puede ser el contenido del campo:

Tipos | Usos  
---|---  
**Texto** | Permite agregar cualquier contenido sin restricciones.  
**Casilla de verificación** | Agrega una casilla de verificación.  
**Entero** | Permite agregar números enteros.  
**Decimal** | Permite agregar cualquier número.  
**Fecha** | Permite seleccionar una fecha.  
**Fecha y hora** | Permite seleccionar una fecha y hora.  
  
Además, se deben configurar algunos **tipos de campo** :

![Formulario de configuración de propiedad](../../../_images/manyone.png) Tipos | Usos  
---|---  
**Selección** | Agrega un menú desplegable de selección con valores restringidos que se establecieron en la creación de la propiedad. Para configurarlo, haga clic en **agregar un valor** junto al campo **Valores**. Escriba los valores predeterminados y presione **enter** para validarlos, ingrese los que necesite. Haga clic en cualquier lado para cerrar la ventana de creación de propiedades.  
**Etiquetas** | Permite crear y aplicar tantas etiquetas como sea necesario. Para configurarlo, introduzca la `nueva_etiqueta` en el campo **etiquetas** y presione **enter** o haga clic en **crear «nueva_etiqueta»**. Haga clic en cualquier lado para cerrar la ventana. Luego agregue las etiquetas en el campo de propiedad, puede hacer clic en el campo correspondiente y elegir una de las etiquetas existentes, escribir el nombre de la etiqueta y presionar **enter** o escribir una nueva etiqueta y crearla en ese momento.  
**Many2one** | Permite elegir de una lista de registros que son el resultado del dominio de un modelo. Solo puede seleccionar un resultado. Para configurarlo, haga clic en **buscar un modelo** en el campo **modelo** y seleccione el modelo. Haga coincidir los registros al hacer clic en **## Registros** o filtre los resultados al hacer clic en **\+ Agregar filtro** y muestre los registros al hacer clic en **## Registros**.  
**Many2many** | Permite elegir de una lista de registros que son el resultado del dominio de un modelo. Puede seleccionar tantos como necesite. Para configurarlo, haga clic en **buscar un modelo** en el campo **modelo** y seleccione el modelo. Haga coincidir los registros al hacer clic en **## Registros** o filtre los resultados al hacer clic en **\+ Agregar filtro** y muestre los registros al hacer clic en **## Registros**.  
  
## Eliminar campos de propiedades

Para eliminar una propiedad, haga clic en el icono de **lápiz** que se
encuentra junto a la propiedad que desea eliminar y haga clic en Eliminar ‣
Eliminar.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>No puede recuperar un campo de propiedad eliminado.</p>
</div>

## Ocultar el panel de propiedad

Haga clic en el botón de engrane **(⚙)** para ocultar el panel lateral de
propiedades.

