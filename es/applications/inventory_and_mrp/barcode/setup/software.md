# Activar los códigos de barras en Odoo

Los códigos de barra pueden ahorrarle tiempo que generalmente pierde cambiando
entre el teclado, el ratón y el escáner. El uso correcto del código de barras
en productos, ubicaciones de recolección, etc. le ayudará a controlar todo el
software desde el lector de código de barras, lo que le permitirá trabajar de
forma más eficiente.

## Configuración

Para usar esta función, primero debe activar el uso de _Código de barras_ en
:menuselection: `Inventario -> Configuración -> Código de Barras`. Una vez que
haya activado la función, puede presionar guardar.

![../../../../_images/software_01.png](../../../../_images/software_01.png)

## Establecer códigos de barras de productos

Puede asignar fácilmente códigos de barras a sus diferentes productos a través
de la aplicación *Inventario *. Para hacerlo, vaya a Configuración ‣
Configurar códigos de barras de productos.

![../../../../_images/software_02.png](../../../../_images/software_02.png)

Ya que haga esto podrá asignar códigos de barra a sus productos al crear el
formulario del producto.

![../../../../_images/software_03.png](../../../../_images/software_03.png)
![../../../../_images/software_04.png](../../../../_images/software_04.png)

Nota

Tenga cuidado, agregue códigos de barras directamente en las variantes del
producto y no en la plantilla del producto, de lo contrario, no podrá
diferenciarlos.

## Establecer códigos de barras de ubicaciones

Si administra varias ubicaciones puede designar un código de barras para cada
una de ellas. Puede configurar los códigos de barras de ubicaciones en
Inventario ‣ Configuración ‣ Ubicaciones.

![../../../../_images/software_05.png](../../../../_images/software_05.png)
![../../../../_images/software_06.png](../../../../_images/software_06.png)

Nota

En el menú _imprimir_ puede imprimir el código de barras que le asigne a cada
ubicación.

## Formatos de código de barras

La mayoría de los productos de venta al por menos usan los códigos de barra
EAN-13, también conocido como Número Global de Artículo Comercial (GTIN, por
sus siglas en inglés). Las empresas usan los GTIN para identificar sus
productos y servicios. A veces es posible encontrar GTIN y UPC como sinónimos,
pero mientras que el GTIN se refiere al número que representa un código de
barras, el UPC se refiere al código de barras en sí. Para más información
sobre el GTIN visite el sitio web del GS1.

Para poder crear GTIN para artículos, una empresa debe tener una clave de la
empresa GS1. Esta clave será el número que aparecerá al inicio de cada GTIN e
identificará la empresa a la cual pertenecen los productos que tienen este
código de barras. Para obtener más información sobre la clave de la empresa
GS1, o para comprar una licencia para una clave, vaya a la página de clave de
la empresa GS1.

Los usuarios de Odoo pueden usar códigos de barra GTIN para identificar sus
productos. Sin embargo, ya que Odoo acepta cualquier string numérica como
código de barras, también es posible definir un código de barras personalizado
para uso interno.

