# Contabilidad y facturación

La aplicación **Facturación de Konvergo ERP** es una aplicación autónoma para crear
facturas, enviárselas a sus clientes y gestionar pagos.

**Contabilidad de Konvergo ERP** es una aplicación con funciones de contabilidad
completas. La productividad contable es el enfoque al desarrollar las
diferentes funciones, como facturas reconocidas por inteligencia artificial,
sincronización con sus cuentas bancarias, coincidencias inteligentemente
sugeridas, etc.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://www.odoo.com/slides/accounting-19">Tutoriales de Konvergo ERP: Contabilidad</a></p>
</div>

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting)

## Contabilidad de doble entrada

Konvergo ERP crea de manera automática todos los asientos de diarios de todas las
transacciones de contabilidad, como facturas, órdenes del punto de venta,
gastos, valoraciones del inventario, etc.

Konvergo ERP usa el sistema de partida doble, donde cada asiento requiere una
contraparte en una cuenta diferente, con una cuenta de débito y otra de
crédito. De esta manera nos aseguramos de que todas las transacciones se
registran debidamente y de que todas las cuentas siempre están balanceadas.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="accounting/get_started/cheat_sheet">Hoja de referencia de contabilidad</a></p>
</div>

## Base de devengo y efectivo

En Konvergo ERP es posible llevar la contabilidad con base de devengo y de efectivo.
De esta manera podrá reportar un ingreso y un gasto ya sea cuando ocurra una
transacción (base de devengo) o cuando se reciba un pago (base de efectivo).

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="accounting/taxes/cash_basis">Base de efectivo</a></p>
</div>

## Multiempresa

Es posible gestionar varias empresas dentro de una misma base de datos de
Konvergo ERP. Cada empresa tiene su propio [plan de
cuentas](accounting/get_started/chart_of_accounts), que también es útil
para generar reportes de consolidación. Los usuarios tienen acceso a varias
empresas, pero solo pueden trabajar en la contabilidad de una empresa a la
vez.

## Entorno multiempresa

En Konvergo ERP está disponible un entorno
[multiempresa](accounting/get_started/multi_currency) con una tasa de
cambio automática para facilitar transacciones internacionales. Cada
transacción se registra en automático en la divisa de la empresa, para
transacciones que se realizan en otra divisa, Konvergo ERP guardará el valor tanto en
la divisa que se usa en la empresa como la divisa de la transacción en sí.
Konvergo ERP genera las ganancias y pérdidas de la divisa después de conciliar los
apuntes de diario.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="accounting/bank/foreign_currency">Gestionar un banco en una divisa extranjera</a></p>
</div>

## Estándares internacionales

Es posible utilizar Contabilidad de Konvergo ERP en más de 70 países. La aplicación
contiene los mecanismos y estándares que son comunes en todas las naciones.
Además, gracias a que es posible instalar módulos específicos para cada país,
es fácil cumplir con todos los requisitos locales. Las posiciones fiscales
existen para poder gestionar cuestiones específicas de cada región, como lo es
el plan de cuentas, los impuestos y cualquier otro requerimiento.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="fiscal_localizations">Paquetes de localización fiscal</a></p>
</div>

## Cuentas por pagar y por cobrar

De forma predeterminada, hay una sola cuenta para los asientos de cuentas por
cobrar y otra para los asientos de cuentas por pagar. Como las transacciones
están vinculadas a sus **contactos** , puede realizar un reporte por cliente,
proveedor o distribuidor.

El reporte del **libro mayor de la empresa** muestra el balance de sus
clientes y proveedores. Lo puede encontrar en Contabilidad ‣ Reportes ‣ Libro
mayor de la empresa.

## Reportes

Estos [reportes financieros](accounting/reporting) están disponibles y se
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
<div class="alert alert-info">
<p class="alert-title">
Truco</p><p><a href="accounting/reporting/customize">Cree y personalice reportes</a> con el motor de reportes de Konvergo ERP.</p>
</div>

### Informe de impuestos

Konvergo ERP calcula todas las transacciones de contabilidad del periodo fiscal
específico y usa los totales para calcular las obligaciones relativas a los
impuestos.

<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Una vez que se crea el reporte de impuestos para un periodo, Konvergo ERP lo bloquea y evita que se creen nuevos asientos que incluyan IVA. Si necesita corregir cualquier factura, lo tendrá que hacer en el siguiente periodo.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Dependiendo de la localización del país, es posible generar una versión XML del reporte de impuestos para poder subirla a la plataforma de IVA de la autoridad fiscal correspondiente.</p>
</div>

## Sincronización bancaria

El sistema de sincronización bancaria se conecta directamente a su institución
bancaria, de esta forma puede importar todas las transacciones directamente a
su base de datos. Podrá obtener un resumen de su flujo de efectivo sin tener
que iniciar sesión en su sistema de banca en línea y sin tener que esperar a
que le entreguen sus estados de cuenta físicos.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="accounting/bank/bank_synchronization">Sincronización bancaria</a></p>
</div>

## Valoración del inventario

En Konvergo ERP se pueden realizar tanto valuaciones de inventario de forma periódica
(manuales) o permanente (automáticas). Los métodos disponibles son precio
estándar, precio promedio, UEPS y FIFO.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config">Configuración de la valoración de inventario</a></p>
</div>

## Ganancias retenidas

Las ganancias retenidas son la porción de los ingresos que un negocio retiene.
Konvergo ERP calcula las ganancias del año actual en tiempo real, así que no se
necesita un diario de final de año ni renovación. El estado de resultados se
reporta de manera automática en el reporte del balance general.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="accounting/get_started/cheat_sheet">Hoja de referencia de contabilidad</a></p>
</div>0

## Fiduciarias

El modo de **empresas de contabilidad** se puede activar desde Contabilidad ‣
Configuración ‣ Ajustes ‣ Modo de empresas de contabilidad. Cuando lo active:

  * Es posible editar la secuencia del documento en cada uno de ellos.

  * Aparecerá un nuevo campo llamado **Total (impuestos incluidos)** con el que será posible acelerar y controlar la codificación, ya que las líneas se crearán de inmediato con la cuenta y el impuesto correctos;

  * Al codificar una transacción, el campo **Fecha de la factura** se llena de manera predeterminada.

  * La opción de **Codificación rápida** está disponible en sus facturas.

  * [Información básica](accounting/get_started)
    * [Hoja de referencia de Contabilidad](accounting/get_started/cheat_sheet)
    * [Plan de cuentas](accounting/get_started/chart_of_accounts)
    * [Sistema multidivisa](accounting/get_started/multi_currency)
    * [Costo promedio en bienes devueltos](accounting/get_started/avg_price_valuation)
    * [Unidades de IVA](accounting/get_started/vat_units)
  * [Impuestos](accounting/taxes)
    * [Impuestos de base de efectivo](accounting/taxes/cash_basis)
    * [Retención fiscal](accounting/taxes/retention)
    * [Comprobar un número de IVA (sistema VIES)](accounting/taxes/vat_verification)
    * [Posiciones fiscales (mapeo de impuestos y cuentas)](accounting/taxes/fiscal_positions)
    * [Integración con AvaTax](accounting/taxes/avatax)
      * [Uso de AvaTax](accounting/taxes/avatax/avatax_use)
      * [Portal de Avalara (AvaTax)](accounting/taxes/avatax/avalara_portal)
    * [Integración con TaxCloud](accounting/taxes/taxcloud)
    * [Ventas a distancia intracomunitarias en la UE](accounting/taxes/eu_distance_selling)
    * [Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)](accounting/taxes/B2B_B2C)
  * [Facturas de cliente](accounting/customer_invoices)
    * [Procesos de facturación](accounting/customer_invoices/overview)
    * [Direcciones de entrega y de facturación](accounting/customer_invoices/customer_addresses)
    * [Términos de pago y planes de pago a plazos](accounting/customer_invoices/payment_terms)
    * [Términos y condiciones predeterminados](accounting/customer_invoices/terms_conditions)
    * [Descuentos por pronto pago y reducción de impuestos](accounting/customer_invoices/cash_discounts)
    * [Notas de crédito y reembolsos](accounting/customer_invoices/credit_notes)
    * [Redondeo de efectivo](accounting/customer_invoices/cash_rounding)
    * [Ingresos diferidos](accounting/customer_invoices/deferred_revenues)
    * [Facturación electrónica (EDI)](accounting/customer_invoices/electronic_invoicing)
    * [Correo postal](accounting/customer_invoices/snailmail)
    * [Códigos EPC QR](accounting/customer_invoices/epc_qr_code)
    * [Incoterms](accounting/customer_invoices/incoterms)
  * [Facturas de proveedor](accounting/vendor_bills)
    * [Digitalización de documentos con IA](accounting/vendor_bills/invoice_digitization)
    * [Activos no circulantes y fijos](accounting/vendor_bills/assets)
    * [Gastos diferidos y prepagos](accounting/vendor_bills/deferred_expenses)
  * [Pagos](accounting/payments)
    * [Pagos en línea](accounting/payments/online)
      * [Instale el parche para desactivar el pago de factura en línea](accounting/payments/online/install_portal_patch)
    * [Cheques](accounting/payments/checks)
    * [Pagos por lote para depósitos bancarios](accounting/payments/batch)
    * [Pagos por lotes: domiciliación bancaria SEPA (SDD)](accounting/payments/batch_sdd)
    * [Seguimiento en las facturas](accounting/payments/follow_up)
    * [Transferencias internas](accounting/payments/internal_transfers)
    * [Pagos con SEPA](accounting/payments/pay_sepa)
    * [Pagar con cheques](accounting/payments/pay_checks)
    * [Pronóstico de futuras facturas por pagar](accounting/payments/forecast)
  * [Cuentas bancarias y de efectivo](accounting/bank)
    * [Sincronización bancaria](accounting/bank/bank_synchronization)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge)
      * [Ponto](accounting/bank/bank_synchronization/ponto)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking)
    * [Transacciones](accounting/bank/transactions)
    * [Conciliación bancaria](accounting/bank/reconciliation)
    * [Modelos de conciliación](accounting/bank/reconciliation_models)
    * [Gestione una cuenta bancaria en una moneda extranjera](accounting/bank/foreign_currency)
    * [Caja registradora](accounting/bank/cash_register)
  * [Reportes](accounting/reporting)
    * [Declaración de impuestos](accounting/reporting/tax_returns)
    * [Traspaso de impuestos](accounting/reporting/tax_carryover)
    * [Contabilidad analítica](accounting/reporting/analytic_accounting)
    * [Presupuesto financiero](accounting/reporting/budget)
    * [Intrastat](accounting/reporting/intrastat)
    * [Reporte de comprobación de inalterabilidad de datos](accounting/reporting/data_inalterability)
    * [Integración con Silverfin](accounting/reporting/silverfin)
    * [Reportes personalizados](accounting/reporting/customize)
    * [Cierre del ejercicio](accounting/reporting/year_end)

  *[UEPS]: Últimas entradas, primeras salidas
  *[FIFO]: Primeras entradas, primeras salidas
  *[EDI]: intercambio electrónico de datos

