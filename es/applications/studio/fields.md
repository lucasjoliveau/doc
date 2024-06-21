# Campos y widgets

Los campos dan estructura a los modelos de una base de datos. Imagine que un
modelo es una tabla o una hoja de cálculo, los campos son las columnas donde
los datos se almacenan en los registros (por ejemplo, filas). Los campos
también definen el tipo de datos que se almacenan en ellos. Sus widgets son
los que definen cómo se presentan y se da formato a los datos en la interfaz
de usuario.

Desde un punto de vista técnico, hay 15 tipos de campos en Konvergo ERP. Sin embargo,
puede elegir entre 20 campos en Studio, pues algunos tipos de campos están
disponibles más de una vez con un widget predeterminado distinto.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Solo puede agregar <b>nuevos campos</b> en las vistas de <a href="views#studio-views-general-form"><span class="std std-ref">Formulario</span></a> y <a href="views#studio-views-multiple-records-list"><span class="std std-ref">Lista</span></a>. En otras vistas, solo puede agregar <b>campos existentes</b> <span class="dfn"><span>(campos que ya existen en el modelo)</span></span>.</p>
</div>

## Campos simples

Los campos simples contienen valores básicos, como texto, números, archivos,
etc.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>

### Texto (`char`)

El campo de **Texto** se utiliza para textos cortos que incluyen cualquier
carácter. Aparece una línea de texto cuando se completa el campo.

  * **Insignia** : muestra el valor dentro de una forma redonda, similar a una etiqueta. El valor no se puede editar en la interfaz de usuario, pero puede establecer un valor predeterminado.

  * **Copiar al portapapeles** : los usuarios pueden copiar el valor al hacer clic en un botón.

  * **Correo electrónico** : el valor se convierte en un enlace _mailto_ en el que se puede hacer clic.

  * **Imagen** : muestra una imagen que utiliza una URL. El valor no se puede editar de forma manual, pero se puede establecer un valor predeterminado.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>

  * **Teléfono** : el valor se convierte en un enlace _tel_ en el que se puede hacer clic.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>

  * **URL** : el valor se convierte en una URL en la que se puede hacer clic.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Ejemplos de campos de texto con diferentes widgets" class="align-center" src="../../_images/text-examples.png"/>
</div>

### Texto multilínea (`text`)

El campo de **Texto multilínea** se utiliza para textos más largos que
contienen cualquier tipo de carácter. Aparecen dos líneas de texto en la
interfaz de usuario cuando se completa el campo.

  * **Copiar al portapapeles** : los usuarios pueden copiar el valor al hacer clic en un botón.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Ejemplos de campos de texto multilínea con diferentes widgets" class="align-center" src="../../_images/multiline-text-examples.png"/>
</div>

### Entero (`integer`)

El campo **entero** se utiliza para todos los números enteros (positivos,
negativos o cero, sin decimales).

  * **Círculo de porcentaje** : muestra el valor en un círculo de porcentaje, por lo general para valores calculados. El valor no se puede editar en la interfaz de usuario, pero puede establecer un valor predeterminado.

  * **Barra de progreso** : muestra el valor junto a una barra de porcentaje, por lo general para valores calculados. El campo no se puede editar de forma manual, pero puede establecer un valor predeterminado.

  * **Manija** : muestra un icono de manija para ordenar registros de forma manual en la [vista de lista](views#studio-views-multiple-records-list).

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Ejemplos de campos entero con diferentes widgets" class="align-center" src="../../_images/integer-examples.png"/>
</div>

### Decimal (`float`)

El campo de **decimal** se utiliza para números decimales (positivos,
negativos o cero, con decimales).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los números decimales se muestran en la interfaz de usuario con dos decimales después del punto, pero se almacenan en la base de datos con mayor precisión.</p>
</div>

  * **Monetario** : es similar a usar el campo monetario. Le recomendamos utilizar este último, ya que ofrece más funciones.

  * **Porcentaje** : muestra un carácter de porcentaje `%` después del porcentaje.

  * **Porcentaje circular** : muestra el valor dentro de un porcentaje circular, por lo general para valores calculados. El campo no se puede editar de forma manual, pero puede establecer un valor predeterminado.

  * **Barra de progreso** : muestra el valor junto a una barra de porcentaje, por lo general para valores calculados. El campo no se puede editar de forma manual, pero puede establecer un valor predeterminado.

  * **Tiempo** : el valor debe seguir el formato _hh:mm_ con un máximo de 59 minutos.

<div class="alert alert-success">
<p class="alert-title">
Example</p><img alt="Ejemplos de campos decimales con diferentes widgets" class="align-center" src="../../_images/decimal-examples.png"/>
</div>

### Monetario (`monetary`)

El campo **Monetario** se utiliza para todos los valores monetarios.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Cuando agrega por primera vez un campo <b>Monetario</b>, se le invita a agregar un campo de <b>Divisa</b> si no existe ninguno en el modelo. Konvergo ERP le ofrece agregar el campo de <b>Divisa</b> por usted. Una vez agregado, agregue el campo <b>Monetario</b> otra vez.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>0

### Html (`html`)

El campo **Html** se utiliza para agregar texto que se puede editar mediante
el editor HTML de Konvergo ERP.

  * **Texto multilínea** : deshabilita el editor HTML de Konvergo ERP para permitir editar el HTML sin procesar.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>1

### Fecha (`date`)

El campo **Fecha** se usa para seleccionar una fecha en el calendario.

  * **Días restantes** : el número de días que faltan para que se muestre la fecha seleccionada (por ejemplo, _en 5 días_), según la fecha actual.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>2

### Fecha y hora (`datetime`)

El campo **Fecha y hora** se utiliza para seleccionar una fecha en el
calendario y una hora en un reloj. Si no se establece ninguna hora, se
utilizará la hora actual del usuario.

  * **Fecha** : se utiliza para registrar la hora sin mostrarla en la interfaz de usuario.

  * **Días restantes** : muestra el número de días que faltan para que se muestre la fecha seleccionada (por ejemplo, _en 5 días_), según la fecha y hora actual.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>3

### Casilla de verificación (`boolean`)

El campo **Casilla de verificación** se utiliza cuando un valor solo puede ser
verdadero o falso, y se indica al marcar o desmarcar una casilla de
verificación.

  * **Botón** : muestra un botón de opción. El widget funciona sin tener que cambiar al modo de edición.

  * **Activar** : muestra un botón de activación. El widget funciona sin tener que cambiar al modo de edición.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>4

### Seleccionar (`selection`)

El campo **Selección** se utiliza cuando los usuarios deben seleccionar un
valor único de un grupo de valores predefinidos.

  * **Insignia** : muestra el valor dentro de una forma redonda, similar a una etiqueta. El valor no se puede editar en la interfaz de usuario, pero puede establecer un valor predeterminado.

  * **Insignias** : muestra todos los valores seleccionables dentro de formas rectangulares, organizadas de manera horizontal.

  * **Prioridad** : muestra símbolos de estrellas en lugar de valores y se utilizan para indicar un nivel de importancia o de satisfacción. Tiene el mismo efecto que seleccionar el Campo de prioridad, aunque, para este último, ya hay cuatro valores de prioridad predefinidos.

  * **Radio** : muestra todos los valores seleccionables como los botones de opción.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>5

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>6

### Prioridad (`selection`)

El campo **Prioridad** se utiliza para mostrar un sistema de clasificación de
tres estrellas, que se puede utilizar para indicar la importancia o el nivel
de satisfacción. Este tipo de campo es un Campo de selección con el widget
**Prioridad** seleccionado de forma predeterminada y cuatro valores de
prioridad predefinidos. Por lo tanto, los widgets **Insignia** , **Insignias**
, **Radio** y **Selección** tienen los mismos propósitos que los descritos en
Selección.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>8

### Archivo (`binary`)

El campo **Archivo** se utiliza para subir cualquier tipo de archivo, o para
firmar un formulario (widget **Firmar**).

  * **Imagen** : los usuarios pueden subir un archivo de imagen que se mostrará en la vista de [Formulario](views#studio-views-general-form). Esto tiene el mismo propósito que usar el campo Imagen`.

  * **Lector de PDF** : los usuarios pueden subir un archivo PDF, que puede ver desde la [Vista de formulario](views#studio-views-general-form).

  * **Firmar** : los usuarios pueden firmar el formulario de forma electrónica. Esto tiene el mismo resultado que si se selecciona el campo Firmar.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Algunas veces puede seleccionar widgets no predeterminados, estos aparecen como viñetas a continuación.</p>
</div>9

### Imagen (`binary`)

El campo **Imagen** se utiliza para subir una imagen y mostrarla en la [Vista
de formulario](views#studio-views-general-form). Este tipo de campo es un
Campo de archivo que cuenta con el widget **Imagen** seleccionado de forma
predeterminada. Por lo tanto, los widgets **Archivo** , **Lector PDF** y
**Firma** tienen los mismos propósitos que los descritos en Archivo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>0

### Firmar (`binary`)

El campo **Firmar** se utiliza para firmar el formulario de forma electrónica.
Este tipo de campo es un Campo de archivo con el widget **Firma** seleccionado
de forma predeterminada. Por lo tanto, los widgets **Archivo** , **Imagen** y
**Lector PDF** tienen los mismos propósitos que los descritos en Archivo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>1

## Campos de relación

Los campos de relación se utilizan para vincular y mostrar los datos de los
registros de otro modelo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>2

### Many2One (`many2one`)

El campo **Many2One** se utiliza para vincular otro registro (de otro modelo)
al registro que se está editando. Por lo tanto, se mostrará el nombre del
registro del otro modelo en el registro que se está editando.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>3 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>4

  * **Insignia** : muestra el valor dentro de una forma redonda, similar a una etiqueta, y no se puede editar en la interfaz del usuario.

  * **Radio** : muestra todos los valores seleccionables como los botones de opción.

### One2Many (`one2many`)

El campo **One2Many** se usa para mostrar las relaciones existentes entre un
registro del modelo actual y varios registros de otro modelo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>6

### Líneas (`one2many`)

El campo **Líneas** se utiliza para crear una tabla con filas y columnas (por
ejemplo, las líneas de productos de una orden de venta).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>7 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>8

### Many2Many (`many2many`)

El campo **Many2Many** se utiliza para vincular varios registros de otro
modelo con varios registros del modelo actual. Los campos Many2Many pueden
utilizar **Desactivar creación** , **Desactivar apertura** , **Dominio** , al
igual que los campos Many2One.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esto funciona de forma diferente a seleccionar el <a href="#studio-fields-simple-fields-image"><span class="std std-ref">campo de Imagen</span></a> directamente, ya que la imagen no se almacena en Konvergo ERP cuando se utiliza un campo de <b>Texto</b> con el widget de <b>Imagen</b>. Por ejemplo, puede ser útil si desea ahorrar espacio de memoria.</p>
</div>9

  * **Casillas de verificación** : los usuarios pueden seleccionar varios valores utilizando las casillas de verificación.

  * **Etiquetas** : los usuarios pueden seleccionar varios valores en forma circular, también conocidos como _etiquetas_. Esto tiene el mismo resultado que si se selecciona el Campo de etiquetas.

### Etiquetas (`many2many`)

El campo **Etiquetas** se utiliza para mostrar varios valores de otro modelo,
también conocidas como _etiquetas_. Este tipo de campo es un campo Many2Many
que cuenta con el widget **Etiquetas** seleccionado de forma predeterminada.
Por lo tanto, los widgets **Casillas de verificación** y **Many2Many** tienen
los mismos propósitos que los descritos en Many2Many.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>0 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>1

### Campo de relación (`related`)

Un **Campo de relación** no es un campo de relación por sí mismo, ya que no se
crea ninguna relación entre modelos. En su lugar, utiliza una relación
existente para obtener y mostrar información de otro registro.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>2

## Propiedades

  * **Invisible** : Cuando no es necesario que los usuarios vean un campo en la interfaz del usuario, marque **Invisible**. Esta opción permite despejar la interfaz, de manera que solo se muestren los campos necesarios según la situación.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>3 <div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>4

  * **Obligatorio** : Si es necesario que el usuario complete un campo antes de poder continuar, seleccione **Obligatorio**.

  * **Solo lectura** : Si los usuarios no deberán ser capaces de modificar un campo, seleccione **Solo lectura**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>5

  * **Etiqueta** : **Etiqueta** es el nombre del campo en la interfaz del usuario.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Seleccione <b>Habilitar SMS</b> para agregar la opción de enviar un SMS desde Konvergo ERP junto al campo.</p>
</div>6

  * **Información de ayuda** : Si desea describir la función de un campo, escriba una descripción en **Información de ayuda**. Se mostrará dentro de un cuadro de información sobre herramientas al pasar el ratón por encima de la etiqueta del campo.

  * **Marcador de posición** : Si desea mostrar un ejemplo de cómo debe completarse un campo, escríbalo en **Marcador de posición**. Se mostrará en color gris claro en lugar del valor del campo.

  * **Widget** : Si desea cambiar la apariencia o función predeterminada de un campo, seleccione uno de los widgets disponibles.

  * **Valor predeterminado** : Si desea añadir un valor predeterminado a un campo al crear un registro, utilice **Valor predeterminado**.

  * **Limitar la visibilidad a grupos** : Si desea limitar los usuarios que pueden ver el campo, seleccione un grupo de acceso de usuarios.

