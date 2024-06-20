# Conexión segura (HTTPS)

HTTP se convierte en el protocolo predeterminado si la opción **Dispositivos
directos** está habilitada en los ajustes de Punto de venta (por ejemplo, si
usa una [impresora ePos](epos_printers.html)).

## Fuerce su Punto de venta a usar una conexión segura (HTTPS)

Agregue una nueva **clave** en los **Parámetros del sistema** para forzar a
que su Punto de venta use una conexión segura con el protocolo HTTPS.

Active el [modo de
desarrollador](../../../general/developer_mode.html#developer-mode), vaya a
Ajustes ‣ Técnico ‣ Parámetros ‣ Parámetros del sistema, después cree un nuevo
parámetro, agregue los siguientes valores y haga clic en _Guardar_.

  * **Clave** : `point_of_sale.enforce_https`

  * **Valor** : `True`

Ver también

  * [Certificado autofirmado para impresoras electrónicas del PdV](epos_ssc.html)

