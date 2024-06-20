# Redondeo de efectivo

El **redondeo de efectivo** es necesario cuando la denominación física más
baja de la divisa, o la moneda más pequeña, es superior a la unidad mínima de
cuenta.

Por ejemplo, algunos países exigen a sus empresas que redondeen el importe
total de una factura a los cinco centavos más cercanos, siempre que el pago
sea en efectivo.

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Ajustes y habilite _Redondeo de
efectivo_ , luego haga clic en _Guardar_.

![../../../../_images/cash_rounding01.png](../../../../_images/cash_rounding01.png)

Vaya a Contabilidad ‣ Configuración ‣ Redondeos de efectivo, y haga clic en
_Crear_.

Defina aquí su _Precisión de redondeo_ , _Estrategia de redondeo_ y _Método de
redondeo_.

Odoo acepta dos **estrategias de redondeo** :

  1. **Añadir línea de redondeo** : se añade una línea de _redondeo_ en la factura. Hay que definir en qué cuenta se registran los redondeos de efectivo.

  2. **Modificar el importe del impuesto** : el redondeo se aplica en la sección de impuestos.

## Aplicar redondeos

Cuando edite un borrador de factura, abra la pestaña _Más información_ , vaya
a la sección _Información contable_ y seleccione el _Método de redondeo de
efectivo_ correspondiente.

