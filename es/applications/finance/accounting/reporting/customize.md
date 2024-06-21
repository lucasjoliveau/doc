# Reportes personalizados

Konvergo ERP dispone de un marco de reportes avanzado y fácil de usar. Esta
herramienta le permite crear nuevos reportes como **reportes fiscales** ,
**balances generales** y **estados de resultados** con **grupos** y
**diseños** específicos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Active el <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> para acceder a la interfaz de creación de reportes contables.</p>
</div>

Para crear un nuevo reporte vaya a Contabilidad ‣ configuración ‣ gestión:
reportes contables. Aquí, puede crear un reporte raíz o una variante.

![herramienta de reportes contables.](../../../../_images/engine-accounting-
reports.png)

## Reporte raíz

Los reportes raíz se pueden considerar como reportes contables generales;
sirven como modelos sobre los que se construyen las versiones de contabilidad
locales. Si se crea un reporte y no se le asigna un reporte raíz, se considera
que dicho reporte es un reporte raíz.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>

Si desea crear un reporte raíz nuevo, deberá crearle un **elemento de menú**
primero. Para hacer esto debe abrir el reporte y, en el mismo reporte, hacer
clic en acción ‣ crear elemento de menú. Vuelva a cargar la página y verá el
reporte en Contabilidad ‣ reportes.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>No es normal encontrarse casos que requieran crear un nuevo reporte raíz, un ejemplo de casos que lo necesitan son los reportes específicos que exigen algunas autoridades fiscales.</p>
</div> ![Botón de crear elemento de
menú.](../../../../_images/engine-create-menu-item.png)

## Variantes

Las variantes son versiones específicas de los reportes raíz, por lo que
siempre van a referirse a un reporte raíz. Para crear una variante, selecciona
un reporte raíz general en **reporte raíz** al crear un nuevo reporte.

Cuando se abre un reporte raíz desde uno de los menús principales de la
aplicación Contabilidad, aparecerán todas sus variantes en el selector de
variantes situado en la esquina superior derecha de la vista.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La siguiente imagen, <b>reporte de IVA (BE)</b> es una variante del reporte raíz <b>reporte general de impuestos</b>.</p>
<img alt="Selección de variante de reportes." class="align-center" src="../../../../_images/engine-variant.png"/>
</div>

## Líneas

Después de haber creado un reporte (raíz o variante), necesita agregar las
líneas necesarias; las puede crear haciendo clic en **agregar línea** o
modifique una línea existente al hacer clic sobre ella. Todas las líneas
_necesitan_ un **nombre** , y pueden llegar a tener una opción adicional de
**Código** (de su elección) por si desea usar su valor en formulas.

![opciones de la herramienta de líneas](../../../../_images/engine-lines-
options.png)

## Expresiones

Cada línea puede contener una o varias **expresiones**. Las expresiones pueden
actuar como **subvariables** que se necesitan en una línea de reporte. Si
desea crear una expresión, haga clic en **Agregar línea** _dentro_ de una
línea de reporte.

Si desea crear una expresión debe atribuirle una **etiqueta** que se utilizará
como referencia a dicha expresión. Por lo tanto, cada expresión debe ser
**única** entre todas las líneas. Se deben indicar tanto **motor de cálculo**
y la **Formula**. El **motor** define la manera en que se interpretan las
**fórmulas** y **subfórmulas**. Si es necesario, se pueden incluir distintas
expresiones que utilicen diferentes motores de cálculo en la misma línea.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>En algunos casos también va a ser necesario definir <b>subfórmulas</b>.</p>
</div>

### Motor del dominio de Konvergo ERP

Este motor identifica una fórmula como un [dominio de
Konvergo ERP](../../../../developer/reference/backend/orm#reference-orm-domains)
cuyo destino son los objetos account.move.line.

La subformula le permite definir el uso de las líneas de movimiento que
coinciden con el dominio para calcular el valor de la expresión:

`sum`

    

El resultado es la suma de todos los balances de las líneas de movimiento
coincidentes.

`sum_if_pos`

    

El resultado es la suma de todos los balances de las líneas de movimiento
coincidentes si el importe es positivo; de lo contrario, es `0`.

`sum_if_neg`

    

El resultado es la suma de todos los balances de las líneas de movimiento
coincidentes si el importe es negativo; de lo contrario, es `0`.

`count_rows`

    

El resultado es el número de sublíneas de esta expresión. Si la línea
principal tiene un valor «agrupar por», corresponderá al número de claves de
agrupación distintas en las líneas de movimiento coincidentes. De lo
contrario, corresponderá al número de líneas de movimiento coincidentes.

Si coloca el signo `-` al principio de la subfórmula, el resultado tendrá un
signo **invertido**.

![Línea de expresión dentro de una línea de
reporte](../../../../_images/engine-expressions.png)

### Etiquetas de impuestos

Cualquier fórmula creada mediante este motor tendrá un nombre que permita que
coincidan con las etiquetas de impuestos. Si dichas etiquetas no existen al
crear la expresión, se crearán.

Cuando se evalúa la expresión, su cálculo puede expresarse de la siguiente
manera: **(cantidad de líneas de movimiento con** `+` **etiqueta)** `-`
**(cantidad de líneas de movimiento con** `-` **etiqueta)**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si la fórmula es <code>nombre_etiqueta</code>, el motor compara las etiquetas de impuestos <code>+nombre_etiqueta</code> y <code>-nombre_etiqueta</code>, y las crea si es necesario. Para ejemplificar, la fórmula coincide con dos etiquetas; si la fórmula es <code>A</code>, necesitará (y creará, si es necesario) las etiquetas <code>+A</code> y <code>-A</code>.</p>
</div>

### Agregar otras fórmulas

Utilice este motor cuando necesite realizar operaciones aritméticas con las
cantidades obtenidas para otras expresiones. Las fórmulas se componen de
referencias a expresiones separadas por uno de los cuatro operadores
aritméticos básicos (suma `+`, resta `-`, división `/` y multiplicación `*`).
Si desea hacer referencia a una expresión, escriba el **código** de la línea
principal seguido de un punto `.` y la **etiqueta** de la expresión (por
ejemplo, **código.etiqueta**).

Las **subfórmulas** pueden ser las siguientes:

`if_above(CUR(amount))`

    

Se devolverá el valor de la expresión aritmética solo si es mayor que el
límite proporcionado. De lo contrario, el resultado será `0`.

`if_below(CUR(amount))`

    

Se devolverá el valor de la expresión aritmética solo si es menor que el
límite proporcionado. De lo contrario, el resultado será `0`.

`if_between(CUR1(amount1), CUR2(amount2))`

    

Se devolverá el valor de la expresión aritmética solo si se encuentra entre
los límites proporcionados. De lo contrario, se devolverá al límite más
cercano.

`if_other_expr_above(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`

    

Se devolverá el valor de la expresión aritmética solo si el valor indicado por
el código de línea y la etiqueta de expresión es mayor que el límite
establecido. De lo contrario, el resultado será `0`.

`if_other_expr_below(LINE_CODE.EXPRESSION_LABEL, CUR(amount))`

    

Se devolverá el valor de la expresión aritmética solo si el valor indicado por
el código de línea y la etiqueta de expresión es inferior al límite
establecido. De lo contrario, el resultado será `0`.

`CUR` es el código de la divisa en mayúsculas, e `importe` es el importe del
límite expresado en esa divisa.

También puede utilizar la subfórmula `cross_report` para que coincida con una
expresión encontrada en otro reporte.

### Prefijo de los códigos de cuenta

Este motor se utiliza para hacer coincidir los importes realizados en las
cuentas mediante los prefijos de los códigos de estas cuentas como variables
de una expresión aritmética.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><code>21</code></div>
<div class="line">Las expresiones aritméticas también pueden tener solo un prefijo, como aquí.</div>
</div>
</div> <div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><code>21 + 10 - 5</code></div>
<div class="line">Esta fórmula suma los balances de las líneas de movimiento realizadas en cuentas cuyos códigos empiezan por <code>21</code> y <code>10</code>, y resta el balance de las realizadas en cuentas con el prefijo <code>5</code>.</div>
</div>
</div>

También es posible ignorar una selección de subprefijos.

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="line-block">
<div class="line"><code>21 + 10\(101, 102) - 5\(57)</code></div>
<div class="line">Esta fórmula funciona igual que en el ejemplo anterior, solo que en este caso no se tienen en cuenta los prefijos <code>101</code>, <code>102</code> y <code>57</code>.</div>
</div>
</div>

También puede aplicar un «subfiltrado» en los **créditos y débitos**
utilizando los sufijos `C` y `D`. En este caso, solo se tendrá en cuenta una
cuenta si su prefijo coincide, _y_ si el balance total de las líneas de
movimiento realizadas en esta cuenta es de **crédito/débito**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La cuenta <code>210001</code> tiene un balance de -42 y la cuenta <code>210002</code> tiene un balance de 25. La fórmula <code>21D</code> solo coincide con la cuenta <code>210002</code>, por lo que devuelve 25. La cuenta <code>210001</code> no coincide, ya que su saldo es de <em>crédito</em>.</p>
</div>

Se pueden mezclar las exclusiones de los prefijos con los sufijos `C` y `D`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>0

Si desea que la letra `C` o `D` coincida con un prefijo y no se utilice como
sufijo, utilice una exclusión vacía `()`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>1

Además de utilizar prefijos de código para incluir cuentas, también puede
hacer que coincidan con las **etiquetas de cuentas**. Esto es muy útil, por
ejemplo, si su país no tiene un plan de cuentas estandarizado, donde es
posible que se use el mismo prefijo para diferentes propósitos de una empresa
a otra.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>2

Si la etiqueta a la que hace referencia está definida en un archivo de datos,
puede usar XMLID en lugar del ID.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>3

También puede usar expresiones aritméticas con etiquetas y tiene la
posibilidad de combinarlas con selecciones de prefijo.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>4

Los sufijos `C` y `D` se pueden utilizar de la misma forma con las etiquetas.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>5

La exclusión de prefijos también funciona con las etiquetas.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>6

### Valor externo

La herramienta “valor externo” se utiliza para referirse a los valores
**manuales** y **traspasados**. Estos valores no se almacenan con
`account.move.line`, sino con `account.report.external.value`. Cada uno de
estos objetos dirige directamente a la expresión sobre la que actúa, por lo
que no hace falta hacer mucho para seleccionarlos.

Las **fórmulas** pueden ser las siguientes:

`sum`

    

Si el resultado debe ser la suma de todos los valores externos del periodo.

`most_recent`

    

Si el resultado debe ser el valor del último valor externo del periodo.

Además, puede usar las **subfórmulas** de dos formas:

`rounding=X`

    

Se sustituye `X` por un número para redondear la cantidad a X decimales.

`editable`

    

Indica que esta expresión se puede editar de forma manual, lo que provoca la
aparición de un icono en el reporte que permite que el usuario realice esta
acción.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>7

Ambas fórmulas se pueden usar al mismo tiempo, solo se deben separar por `;`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un reporte fiscal para Bélgica y Estados Unidos usará la misma versión general como base y se adaptará según sus normativas nacionales.</p>
</div>8

### Función python personalizada

Esta herramienta permite que los desarrolladores introduzcan cálculos
personalizados de expresiones caso por caso. La fórmula es el nombre de una
**función de python** a llamar, y la subfórmula es una **clave** a buscar en
el **diccionario** devuelto por esta función. Utilícela solo si está creando
su propio módulo personalizado.

## Columnas

Los reportes pueden tener un **número indefinido** de columnas. Cada columna
obtiene sus valores de las **expresiones** indicadas en las **líneas**. El
campo **expression_label** de la columna proporciona la etiqueta de las
expresiones cuyo valor se muestra. Si una línea no tiene ninguna **expresión**
en ese campo, no se mostrará nada para ella en esta columna. Si se necesitan
varias columnas, debe utilizar diferentes etiquetas de **expresión**

![Columnas en el reporte](../../../../_images/engine-columns.png)

Si utiliza la función **comparación de periodos** en la pestaña **Opciones**
de un reporte contable, todas las columnas se repiten en y para cada periodo.

