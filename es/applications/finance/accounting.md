# Contabilidad y facturación

La aplicación **Facturación de Odoo** es una aplicación autónoma para crear
facturas, enviárselas a sus clientes y gestionar pagos.

**Contabilidad de Odoo** es una aplicación con funciones de contabilidad
completas. La productividad contable es el enfoque al desarrollar las
diferentes funciones, como facturas reconocidas por inteligencia artificial,
sincronización con sus cuentas bancarias, coincidencias inteligentemente
sugeridas, etc.

Ver también

[Tutoriales de Odoo: Contabilidad](https://www.odoo.com/slides/accounting-19)

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started.html)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes.html)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices.html)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills.html)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments.html)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank.html)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting.html)

## Contabilidad de doble entrada

Odoo crea de manera automática todos los asientos de diarios de todas las
transacciones de contabilidad, como facturas, órdenes del punto de venta,
gastos, valoraciones del inventario, etc.

Odoo usa el sistema de partida doble, donde cada asiento requiere una
contraparte en una cuenta diferente, con una cuenta de débito y otra de
crédito. De esta manera nos aseguramos de que todas las transacciones se
registran debidamente y de que todas las cuentas siempre están balanceadas.

Ver también

[Hoja de referencia de contabilidad](accounting/get_started/cheat_sheet.html)

## Base de devengo y efectivo

En Odoo es posible llevar la contabilidad con base de devengo y de efectivo.
De esta manera podrá reportar un ingreso y un gasto ya sea cuando ocurra una
transacción (base de devengo) o cuando se reciba un pago (base de efectivo).

Ver también

[Base de efectivo](accounting/taxes/cash_basis.html)

## Multiempresa

Es posible gestionar varias empresas dentro de una misma base de datos de
Odoo. Cada empresa tiene su propio [plan de
cuentas](accounting/get_started/chart_of_accounts.html), que también es útil
para generar reportes de consolidación. Los usuarios tienen acceso a varias
empresas, pero solo pueden trabajar en la contabilidad de una empresa a la
vez.

## Entorno multiempresa

En Odoo está disponible un entorno
[multiempresa](accounting/get_started/multi_currency.html) con una tasa de
cambio automática para facilitar transacciones internacionales. Cada
transacción se registra en automático en la divisa de la empresa, para
transacciones que se realizan en otra divisa, Odoo guardará el valor tanto en
la divisa que se usa en la empresa como la divisa de la transacción en sí.
Odoo genera las ganancias y pérdidas de la divisa después de conciliar los
apuntes de diario.

Ver también

[Gestionar un banco en una divisa
extranjera](accounting/bank/foreign_currency.html)

## Estándares internacionales

Es posible utilizar Contabilidad de Odoo en más de 70 países. La aplicación
contiene los mecanismos y estándares que son comunes en todas las naciones.
Además, gracias a que es posible instalar módulos específicos para cada país,
es fácil cumplir con todos los requisitos locales. Las posiciones fiscales
existen para poder gestionar cuestiones específicas de cada región, como lo es
el plan de cuentas, los impuestos y cualquier otro requerimiento.

Ver también

[Paquetes de localización fiscal](fiscal_localizations.html)

## Cuentas por pagar y por cobrar

De forma predeterminada, hay una sola cuenta para los asientos de cuentas por
cobrar y otra para los asientos de cuentas por pagar. Como las transacciones
están vinculadas a sus **contactos** , puede realizar un reporte por cliente,
proveedor o distribuidor.

El reporte del **libro mayor de la empresa** muestra el balance de sus
clientes y proveedores. Lo puede encontrar en Contabilidad ‣ Reportes ‣ Libro
mayor de la empresa.

## Reportes

Estos [reportes financieros](accounting/reporting.html) están disponibles y se
actualizan en tiempo real:

Reportes financieros  
---  
Estado de cuenta | Balance general  
Estado de resultados  
Estado de flujo de efectivo  
Informe de impuestos  
Declaración recapitulativa de operaciones intracomunitarias  
Auditar | Libro mayor  
Balanza de comprobación  
Reporte de diario  
Reporte Intrastat  
Registro de caja  
Contacto | Libro mayor de la empresa  
Cuenta antigua por cobrar  
Cuenta antigua por pagar  
Administración | Análisis de factura  
Ganancias/pérdidas de divisa no realizadas  
Programa de depreciación  
Gastos rechazados  
Análisis de presupuesto  
Márgenes de producto  
Reporte 1099  
  
Truco

[Cree y personalice reportes](accounting/reporting/customize.html) con el
motor de reportes de Odoo.

### Informe de impuestos

Odoo calcula todas las transacciones de contabilidad del periodo fiscal
específico y usa los totales para calcular las obligaciones relativas a los
impuestos.

Importante

Una vez que se crea el reporte de impuestos para un periodo, Odoo lo bloquea y
evita que se creen nuevos asientos que incluyan IVA. Si necesita corregir
cualquier factura, lo tendrá que hacer en el siguiente periodo.

Nota

Dependiendo de la localización del país, es posible generar una versión XML
del reporte de impuestos para poder subirla a la plataforma de IVA de la
autoridad fiscal correspondiente.

## Sincronización bancaria

El sistema de sincronización bancaria se conecta directamente a su institución
bancaria, de esta forma puede importar todas las transacciones directamente a
su base de datos. Podrá obtener un resumen de su flujo de efectivo sin tener
que iniciar sesión en su sistema de banca en línea y sin tener que esperar a
que le entreguen sus estados de cuenta físicos.

Ver también

[Sincronización bancaria](accounting/bank/bank_synchronization.html)

## Valoración del inventario

En Odoo se pueden realizar tanto valuaciones de inventario de forma periódica
(manuales) o permanente (automáticas). Los métodos disponibles son precio
estándar, precio promedio, UEPS y FIFO.

Ver también

[Configuración de la valoración de
inventario](../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config.html)

## Ganancias retenidas

Las ganancias retenidas son la porción de los ingresos que un negocio retiene.
Odoo calcula las ganancias del año actual en tiempo real, así que no se
necesita un diario de final de año ni renovación. El estado de resultados se
reporta de manera automática en el reporte del balance general.

Ver también

[Hoja de referencia de contabilidad](accounting/get_started/cheat_sheet.html)

## Fiduciarias

El modo de empresas de contabilidad se puede activar desde Contabilidad ‣
Configuración ‣ Ajustes ‣ Modo de empresas de contabilidad. Cuando lo active:

  * Es posible editar la secuencia del documento en cada uno de ellos.

  * Aparecerá un nuevo campo llamado Total (impuestos incluidos) con el que será posible acelerar y controlar la codificación, ya que las líneas se crearán de inmediato con la cuenta y el impuesto correctos;

  * Al codificar una transacción, el campo Fecha de la factura se llena de manera predeterminada.

  * La opción de Codificación rápida está disponible en sus facturas.

  * [Información básica](accounting/get_started.html)
    * [Hoja de referencia de Contabilidad](accounting/get_started/cheat_sheet.html)
    * [Plan de cuentas](accounting/get_started/chart_of_accounts.html)
    * [Sistema multidivisa](accounting/get_started/multi_currency.html)
    * [Costo promedio en bienes devueltos](accounting/get_started/avg_price_valuation.html)
    * [Unidades de IVA](accounting/get_started/vat_units.html)
  * [Impuestos](accounting/taxes.html)
    * [Impuestos de base de efectivo](accounting/taxes/cash_basis.html)
    * [Retención fiscal](accounting/taxes/retention.html)
    * [Comprobar un número de IVA (sistema VIES)](accounting/taxes/vat_verification.html)
    * [Posiciones fiscales (mapeo de impuestos y cuentas)](accounting/taxes/fiscal_positions.html)
    * [Integración con AvaTax](accounting/taxes/avatax.html)
      * [Uso de AvaTax](accounting/taxes/avatax/avatax_use.html)
      * [Portal de Avalara (AvaTax)](accounting/taxes/avatax/avalara_portal.html)
    * [Integración con TaxCloud](accounting/taxes/taxcloud.html)
    * [Ventas a distancia intracomunitarias en la UE](accounting/taxes/eu_distance_selling.html)
    * [Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)](accounting/taxes/B2B_B2C.html)
  * [Facturas de cliente](accounting/customer_invoices.html)
    * [Procesos de facturación](accounting/customer_invoices/overview.html)
    * [Direcciones de entrega y de facturación](accounting/customer_invoices/customer_addresses.html)
    * [Términos de pago y planes de pago a plazos](accounting/customer_invoices/payment_terms.html)
    * [Términos y condiciones predeterminados](accounting/customer_invoices/terms_conditions.html)
    * [Descuentos por pronto pago y reducción de impuestos](accounting/customer_invoices/cash_discounts.html)
    * [Notas de crédito y reembolsos](accounting/customer_invoices/credit_notes.html)
    * [Redondeo de efectivo](accounting/customer_invoices/cash_rounding.html)
    * [Ingresos diferidos](accounting/customer_invoices/deferred_revenues.html)
    * [Facturación electrónica (EDI)](accounting/customer_invoices/electronic_invoicing.html)
    * [Correo postal](accounting/customer_invoices/snailmail.html)
    * [Códigos EPC QR](accounting/customer_invoices/epc_qr_code.html)
    * [Incoterms](accounting/customer_invoices/incoterms.html)
  * [Facturas de proveedor](accounting/vendor_bills.html)
    * [Digitalización de documentos con IA](accounting/vendor_bills/invoice_digitization.html)
    * [Activos no circulantes y fijos](accounting/vendor_bills/assets.html)
    * [Gastos diferidos y prepagos](accounting/vendor_bills/deferred_expenses.html)
  * [Pagos](accounting/payments.html)
    * [Pagos en línea](accounting/payments/online.html)
      * [Instale el parche para desactivar el pago de factura en línea](accounting/payments/online/install_portal_patch.html)
    * [Cheques](accounting/payments/checks.html)
    * [Pagos por lote para depósitos bancarios](accounting/payments/batch.html)
    * [Pagos por lotes: domiciliación bancaria SEPA (SDD)](accounting/payments/batch_sdd.html)
    * [Seguimiento en las facturas](accounting/payments/follow_up.html)
    * [Transferencias internas](accounting/payments/internal_transfers.html)
    * [Pagos con SEPA](accounting/payments/pay_sepa.html)
    * [Pagar con cheques](accounting/payments/pay_checks.html)
    * [Pronóstico de futuras facturas por pagar](accounting/payments/forecast.html)
  * [Cuentas bancarias y de efectivo](accounting/bank.html)
    * [Sincronización bancaria](accounting/bank/bank_synchronization.html)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge.html)
      * [Ponto](accounting/bank/bank_synchronization/ponto.html)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking.html)
    * [Transacciones](accounting/bank/transactions.html)
    * [Conciliación bancaria](accounting/bank/reconciliation.html)
    * [Modelos de conciliación](accounting/bank/reconciliation_models.html)
    * [Gestione una cuenta bancaria en una moneda extranjera](accounting/bank/foreign_currency.html)
    * [Caja registradora](accounting/bank/cash_register.html)
  * [Reportes](accounting/reporting.html)
    * [Declaración de impuestos](accounting/reporting/tax_returns.html)
    * [Traspaso de impuestos](accounting/reporting/tax_carryover.html)
    * [Contabilidad analítica](accounting/reporting/analytic_accounting.html)
    * [Presupuesto financiero](accounting/reporting/budget.html)
    * [Intrastat](accounting/reporting/intrastat.html)
    * [Reporte de comprobación de inalterabilidad de datos](accounting/reporting/data_inalterability.html)
    * [Integración con Silverfin](accounting/reporting/silverfin.html)
    * [Reportes personalizados](accounting/reporting/customize.html)
    * [Cierre del ejercicio](accounting/reporting/year_end.html)

  *[UEPS]: Últimas entradas, primeras salidas
  *[FIFO]: Primeras entradas, primeras salidas
  *[EDI]: intercambio electrónico de datos

