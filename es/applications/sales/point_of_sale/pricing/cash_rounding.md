# Redondeo de efectivo

El **redondeo de efectivo** es necesario cuando la denominación física más
baja de la divisa, o la moneda más pequeña, es superior a la unidad mínima de
cuenta.

Por ejemplo, algunos países exigen a sus empresas que redondeen el importe
total de una factura a los cinco centavos más cercanos, siempre que el pago
sea en efectivo.

Cada punto de venta en Odoo se puede configurar para aplicar redondeo de
efectivo en los totales de sus cuentas o recibos.

## Configuración

Vaya a Punto de venta ‣ Configuración ‣ Ajustes y habilite la función de
_Redondeo de efectivo_ , luego haga clic en _Guardar_.

![../../../../_images/cash_rounding011.png](../../../../_images/cash_rounding011.png)

Vaya a Punto de venta ‣ Configuración ‣ Punto de venta, abra el punto de venta
que desea configurar y habilite la opción de _Redondeo de efectivo_.

Para definir el **Método de redondeo** , abra la lista desplegable y haga clic
en _Crear y editar…_.

Defina su _Precisión de redondeo_ , _Cuenta de ganancias_ y _Cuenta de
pérdidas_. Posteriormente, guarde tanto su método de redondeo como los ajustes
de su Punto de venta.

![../../../../_images/cash_rounding02.png](../../../../_images/cash_rounding02.png)

Ahora todos los importes totales de este punto de venta agregan una línea para
aplicar el redondeo según sus ajustes.

![../../../../_images/cash_rounding03.png](../../../../_images/cash_rounding03.png)

Nota

La aplicación Punto de venta de Odoo solo es compatible con la estrategia de
redondeo agregar una línea de redondeo.

