# Suiza

## ISR (recibo de pago con número de referencia)

Los ISR son recibos de pago que se utilizan en Suiza. Puede imprimirlos
directamente desde Konvergo ERP. En las facturas de cliente hay un botón nuevo que se
llama _Imprimir ISR_.

![../../../_images/switzerland00.png](../../../_images/switzerland00.png)
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>El botón <em>Imprimir ISR</em> solo aparece cuando hay una cuenta bancaria definida en la factura. Puede usar CH6309000000250097798 como número de cuenta bancario y 010391391 como referencia ISR en CHF.</p>
</div>
![../../../_images/switzerland01.png](../../../_images/switzerland01.png)

Luego abra un PDF con el ISR.

![../../../_images/switzerland02.png](../../../_images/switzerland02.png)

Hay dos diseños para el ISR: uno con las coordenadas bancarias y uno sin
ellas. Para elegir cuál usar, hay una opción para imprimir la información
bancaria en el ISR. Para activarlo, vaya a Contabilidad ‣ Configuración ‣
Ajustes ‣ Facturas de clientes y habilite la función **Imprimir banco en el
ISR** :

![../../../_images/switzerland03.png](../../../_images/switzerland03.png)

### Referencia ISR en las facturas

Para facilitar el proceso de conciliación, puede agregar su referencia ISR
como **referencia de pago** en sus facturas.

Para hacerlo, debe configurar el diario que usualmente usa para emitir
facturas. Vaya a Contabilidad ‣ Configuración ‣ Diarios, abra el diario que
desea modificar (De forma predeterminada, el nombre del diario es _Facturas de
clientes_), haga clic en _Editar_ , y abra la pestaña de _Ajustes avanzados_.
En el campo de **comunicación estándar** , seleccione _Suiza_ , y haga clic en
_Guardar_.

![Configuración de diario para mostrar el ISR como referencia de pago en las
facturas en Konvergo ERP](../../../_images/switzerland-isr-reference.png)

## Actualización en vivo de la tasa de cambio

Puede actualizar automáticamente sus tasas de cambio de divisas con base en la
Administración Federal de Impuestos de Suiza. Para esto, vaya a Contabilidad ‣
Ajustes, active los ajustes multidivisa y elija el servicio que desea.

![../../../_images/switzerland04.png](../../../_images/switzerland04.png)

## IVA actualizado para enero 2018

A partir del 1° de enero de 2018, se aplicarán nuevas tasas de IVA reducidas
en Suiza. La tasa normal de 8.0% cambiará a 7.7% y la tasa específica para el
sector hotelero cambiará de 3.8% a 3.7%.

### ¿Cómo actualizar sus impuestos en Konvergo ERP Enterprise (Konvergo ERP en línea o con
alojamiento local)?

Si tiene la versión V11.1, ya está todo el trabajo hecho, no tiene que hacer
nada.

Si empezó en una versión anterior, primero tiene que actualizar el módulo
«Suiza - Reportes contables». Para esto, vaya a Aplicaciones ‣ elimine el
filtro «Aplicaciones» ‣ busque «Suiza - Reportes contables» ‣ abra el módulo ‣
haga clic en «actualizar».

![../../../_images/switzerland05.png](../../../_images/switzerland05.png)

Una vez hecho esto, puede trabajar en crear nuevos impuestos para las tasas
actualizadas.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p><b>No elimine o modifique los impuestos existentes</b> (8.0% y 3.8%). Manténgalos ya que tal vez use ambas tasas por un periodo corto de tiempo. En lugar de esto, recuerde archivarlos una vez que haya codificado todas sus transacciones del 2017.</p>
</div>

La creación de tales impuestos debe hacerse de la siguiente forma:

  * **Impuestos de compra** : copie los impuestos de origen, cambie su nombre, etiqueta en factura, tasa y grupo de impuestos (efectivo desde la versión v10 solamente)

  * **Impuestos de venta** : copie los impuestos de origen, cambie su nombre, etiqueta en factura, tasa y grupo de impuestos (efectivo desde la versión v10 solamente). Ya que el reporte de IVA ahora muestra los detalles de las tasas antiguas y nuevas, debe establecer las etiquetas en conformidad

    * Para los impuestos del 7.7%: Formulario IVA de Suiza: tabla base 302, formulario IVA de Suiza: tabla de impuesto 302

    * Para los impuestos del 3.7%: formulario IVA de Suiza: tabla base 342, formulario IVA de Suiza: tabla de impuesto 342

Encontrará a continuación ejemplos de configuración correcta para todos los
impuestos incluidos en Konvergo ERP de forma predeterminada

**Nombre del impuesto** | **Tasa** | **Etiqueta en factura** | **Grupo de impuestos (efectivo desde la versión V10)** | **Alcance del impuesto** | **Etiqueta**  
---|---|---|---|---|---  
TVA 7.7% sur achat B&S (TN) | 7.7% | 7.7% achat | TVA 7.7% | Compras | Formulario IVA de Suiza: tabla 400  
TVA 7.7% sur achat B&S (Incl. TN) | 7.7% | 7.7% achat Incl. | TVA 7.7% | Compras | Formulario IVA de Suiza: tabla 400  
TVA 7.7% sur invest. et autres ch. (TN) | 7.7% | 7.7% invest. | TVA 7.7% | Compras | Formulario IVA de Suiza: tabla 405  
TVA 7.7% sur invest. et autres ch. (Incl. TN) | 7.7% | 7.7% invest. Incl. | TVA 7.7% | Compras | Formulario IVA de Suiza: tabla 405  
TVA 3.7% sur achat B&S (TS) | 3.7% | 3.7% achat | TVA 3.7% | Compras | Formulario IVA de Suiza: tabla 400  
TVA 3.7% sur achat B&S (Incl. TS) | 3.7% | 3.7% achat Incl. | TVA 3.7% | Compras | Formulario IVA de Suiza: tabla 400  
TVA 3.7% sur invest. et autres ch. (TS) | 3.7% | 3.7% invest | TVA 3.7% | Compras | Formulario IVA de Suiza: tabla 405  
TVA 3.7% sur invest. et autres ch. (Incl. TS) | 3.7% | 3.7% invest Incl. | TVA 3.7% | Compras | Formulario IVA de Suiza: tabla 405  
TVA due a 7.7% (TN) | 7.7% | 7.7% | TVA 7.7% | Ventas | Formulario IVA de Suiza: tabla base 302, formulario IVA de Suiza: tabla de impuestos 302  
TVA due à 7.7% (Incl. TN) | 7.7% | 7.7% Incl. | TVA 7.7% | Ventas | Formulario IVA de Suiza: tabla base 302, formulario IVA de Suiza: tabla de impuestos 302  
TVA due à 3.7% (TS) | 3.7% | 3.7% | TVA 3.7% | Ventas | Formulario IVA de Suiza: tabla base 342, formulario IVA de Suiza: tabla de impuestos 342  
TVA due a 3.7% (Incl. TS) | 3.7% | 3.7% Incl. | TVA 3.7% | Ventas | Formulario IVA de Suiza: tabla base 342, formulario IVA de Suiza: tabla de impuestos 342  
  
Si tiene preguntas o comentarios, contacte a nuestro equipo de soporte a
través de odoo.com/help.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>No olvide actualizar sus posiciones fiscales. Si tiene la versión 11.1 (o superior), no hay nada que hacer. De otra forma, también tendrá que actualizar sus posiciones fiscales en conformidad.</p>
</div>

