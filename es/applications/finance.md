# Finanzas

  * [Contabilidad y facturación](finance/accounting)
    * [Contabilidad de doble entrada](finance/accounting#double-entry-bookkeeping)
    * [Base de devengo y efectivo](finance/accounting#accrual-and-cash-basis)
    * [Multiempresa](finance/accounting#multi-company)
    * [Entorno multiempresa](finance/accounting#multi-currency-environment)
    * [Estándares internacionales](finance/accounting#international-standards)
    * [Cuentas por pagar y por cobrar](finance/accounting#accounts-receivable-and-payable)
    * Reportes
      * [Informe de impuestos](finance/accounting#tax-report)
    * [Sincronización bancaria](finance/accounting#bank-synchronization)
    * [Valoración del inventario](finance/accounting#inventory-valuation)
    * [Ganancias retenidas](finance/accounting#retained-earnings)
    * Fiduciarias
      * [Información básica](finance/accounting/get_started)
        * Panel de integración de Contabilidad
          * [Datos de la empresa](finance/accounting/get_started#company-data)
          * [Cuenta bancaria](finance/accounting/get_started#bank-account)
          * [Periodos contables](finance/accounting/get_started#accounting-periods)
          * [Plan de cuentas](finance/accounting/get_started#chart-of-accounts)
        * Panel de integración de Facturación
          * [Datos de la empresa](finance/accounting/get_started#invoicing-setup-company)
          * [Diseño de factura](finance/accounting/get_started#invoice-layout)
          * [Método de pago](finance/accounting/get_started#payment-method)
          * Factura de muestra
            * Hoja de referencia de Contabilidad
              * Plan de cuentas
                * [Ejemplo](finance/accounting/get_started/cheat_sheet#example)
              * [Asientos contables](finance/accounting/get_started/cheat_sheet#journal-entries)
              * [Conciliación](finance/accounting/get_started/cheat_sheet#reconciliation)
              * [Conciliación bancaria](finance/accounting/get_started/cheat_sheet#bank-reconciliation)
              * [Gestión de cheques](finance/accounting/get_started/cheat_sheet#checks-handling)
            * Plan de cuentas
              * Configuración de una cuenta
                * [Código y nombre](finance/accounting/get_started/chart_of_accounts#code-and-name)
                * Tipo
                  * [Automatización de activos y gastos e ingresos diferidos](finance/accounting/get_started/chart_of_accounts#assets-deferred-expenses-and-deferred-revenues-automation)
                * [Impuestos predeterminados](finance/accounting/get_started/chart_of_accounts#default-taxes)
                * [Etiquetas](finance/accounting/get_started/chart_of_accounts#tags)
                * Grupos de cuentas
                  * [Crear grupos de cuentas de forma manual](finance/accounting/get_started/chart_of_accounts#create-account-groups-manually)
                * [Permitir conciliaciones](finance/accounting/get_started/chart_of_accounts#allow-reconciliation)
                * [Obsoleta](finance/accounting/get_started/chart_of_accounts#deprecated)
            * Sistema multidivisa
              * Configuración
                * [Divisa principal](finance/accounting/get_started/multi_currency#main-currency)
                * [Habilitar divisas extranjeras](finance/accounting/get_started/multi_currency#enable-foreign-currencies)
                * Tasas de cambio
                  * [Actualización manual](finance/accounting/get_started/multi_currency#manual-update)
                  * [Actualización automática](finance/accounting/get_started/multi_currency#automatic-update)
                * [Asientos de diferencia de cambio](finance/accounting/get_started/multi_currency#exchange-difference-entries)
                * [Plan de cuentas](finance/accounting/get_started/multi_currency#chart-of-accounts)
                * [Diarios contables](finance/accounting/get_started/multi_currency#journals)
              * Contabilidad multidivisa
                * [Facturas de cliente, de proveedor y otros documentos](finance/accounting/get_started/multi_currency#invoices-bills-and-other-documents)
                * [Registro de pagos](finance/accounting/get_started/multi_currency#payment-registration)
                * [Transacciones bancarias](finance/accounting/get_started/multi_currency#bank-transactions)
                * [Asientos contables de tipo de cambio](finance/accounting/get_started/multi_currency#exchange-rate-journal-entries)
            * Costo promedio en bienes devueltos
              * [Configuración](finance/accounting/get_started/avg_price_valuation#configuration)
              * Uso de la valuación del costo promedio
                * [Fórmula](finance/accounting/get_started/avg_price_valuation#formula)
                * Cálculo del costo promedio
                  * [Envío de productos (caso de uso)](finance/accounting/get_started/avg_price_valuation#product-delivery-use-case)
              * Devolver artículos al proveedor (caso de uso)
                * [Eliminar errores de valuación de existencias en productos salientes](finance/accounting/get_started/avg_price_valuation#eliminate-stock-valuation-errors-in-outgoing-products)
              * Contabilidad anglosajona
                * Recepción de productos
                  * [Resumen](finance/accounting/get_started/avg_price_valuation#summary)
                  * Conciliación de cuentas al recibir productos
                    * [En Konvergo ERP](finance/accounting/get_started/avg_price_valuation#in-odoo)
                  * Conciliación de cuentas al recibir la factura del proveedor
                    * [En Konvergo ERP](finance/accounting/get_started/avg_price_valuation#id1)
                * [Al recibir un producto](finance/accounting/get_started/avg_price_valuation#on-product-delivery)
                * [Al devolver un producto](finance/accounting/get_started/avg_price_valuation#on-product-return)
            * Unidades de IVA
              * Configuración
                * [Posición fiscal](finance/accounting/get_started/vat_units#fiscal-position)
              * [Informe de impuestos](finance/accounting/get_started/vat_units#tax-report)
      * [Impuestos](finance/accounting/taxes)
        * [Impuestos predeterminados](finance/accounting/taxes#default-taxes)
        * [Activar los impuestos sobre la venta desde la vista de lista](finance/accounting/taxes#activate-sales-taxes-from-the-list-view)
        * Configuración
          * Opciones principales
            * [Nombre del impuesto](finance/accounting/taxes#tax-name)
            * [Cálculo de impuestos](finance/accounting/taxes#tax-computation)
            * [Activo](finance/accounting/taxes#active)
            * [Ámbito del impuesto](finance/accounting/taxes#tax-scope)
          * [Pestaña de definición](finance/accounting/taxes#definition-tab)
          * Pestaña de opciones avanzadas
            * [Etiqueta en facturas](finance/accounting/taxes#label-on-invoices)
            * [Grupo de impuestos](finance/accounting/taxes#tax-group)
            * [Incluir en el costo analítico](finance/accounting/taxes#include-in-analytic-cost)
            * [Incluido en el precio](finance/accounting/taxes#included-in-price)
            * Afectación a la base de los impuestos subsecuentes
              * Impuestos de base de efectivo
                * [Configuración](finance/accounting/taxes/cash_basis#configuration)
                * [Impacto de los impuestos de base de efectivo en la contabilidad](finance/accounting/taxes/cash_basis#impact-of-cash-basis-taxes-on-accounting)
              * Retención fiscal
                * [Configuración](finance/accounting/taxes/retention#configuration)
                * [Aplicación de las retenciones en las facturas](finance/accounting/taxes/retention#applying-retention-taxes-on-invoices)
              * Comprobar un número de IVA (sistema VIES)
                * [Configuración](finance/accounting/taxes/vat_verification#configuration)
                * [Comprobar número de IVA](finance/accounting/taxes/vat_verification#vat-number-validation)
              * Posiciones fiscales (mapeo de impuestos y cuentas)
                * Configuración
                  * [Mapeo de impuestos y cuentas](finance/accounting/taxes/fiscal_positions#tax-and-account-mapping)
                * Uso
                  * [Uso automático](finance/accounting/taxes/fiscal_positions#automatic-application)
                  * [Uso manual](finance/accounting/taxes/fiscal_positions#manual-application)
                  * [Asignar a un contacto](finance/accounting/taxes/fiscal_positions#assign-to-a-partner)
              * [Integración con AvaTax](finance/accounting/taxes/avatax)
                * Configuración en AvaTax
                  * [Crear un perfil básico de la empresa](finance/accounting/taxes/avatax#create-basic-company-profile)
                  * [Conexión con AvaTax](finance/accounting/taxes/avatax#connect-to-avatax)
                * Configuración en Konvergo ERP
                  * [País fiscal](finance/accounting/taxes/avatax#fiscal-country)
                  * [Ajustes de la empresa](finance/accounting/taxes/avatax#company-settings)
                  * [Instalación del módulo](finance/accounting/taxes/avatax#module-installation)
                  * Ajustes de AvaTax en Konvergo ERP
                    * [Prerrequisitos](finance/accounting/taxes/avatax#prerequisites)
                    * [Credenciales](finance/accounting/taxes/avatax#credentials)
                    * [Opciones transaccionales](finance/accounting/taxes/avatax#transaction-options)
                    * [Validación de dirección](finance/accounting/taxes/avatax#address-validation)
                    * [Probar conexión](finance/accounting/taxes/avatax#test-connection)
                    * [Sincronizar parámetros](finance/accounting/taxes/avatax#sync-parameters)
                  * Posición fiscal
                    * [Cuentas de AvaTax](finance/accounting/taxes/avatax#avatax-accounts)
                  * Mapeo de impuestos
                    * [Mapeo de categorías de producto](finance/accounting/taxes/avatax#product-category-mapping)
                    * Mapeo de productos
                      * Uso de AvaTax
                        * Cálculo de impuestos
                          * [Activaciones automáticas](finance/accounting/taxes/avatax/avatax_use#automatic-triggers)
                          * [Activaciones manuales](finance/accounting/taxes/avatax/avatax_use#manual-triggers)
                        * [Sincronización con AvaTax](finance/accounting/taxes/avatax/avatax_use#avatax-synchronization)
                        * [Descuentos sobre el precio establecido](finance/accounting/taxes/avatax/avatax_use#fixed-price-discounts)
                        * [Registro](finance/accounting/taxes/avatax/avatax_use#logging)
                      * Portal de Avalara (AvaTax)
                        * Transacciones
                          * [Editar transacciones](finance/accounting/taxes/avatax/avalara_portal#edit-transaction)
                          * [Filtro](finance/accounting/taxes/avatax/avalara_portal#filter)
                          * Ordenar por
                            * [Personalizar columnas](finance/accounting/taxes/avatax/avalara_portal#customize-columns)
                          * [Importar y exportar](finance/accounting/taxes/avatax/avalara_portal#import-export)
                          * [Reportes](finance/accounting/taxes/avatax/avalara_portal#reports)
                        * [Agregar más jurisdicciones](finance/accounting/taxes/avatax/avalara_portal#add-more-jurisdictions)
                        * [Certificado de exención de impuestos](finance/accounting/taxes/avatax/avalara_portal#tax-exemption-certificate)
                        * [Operaciones de fin de año](finance/accounting/taxes/avatax/avalara_portal#end-of-year-operations)
              * Integración con TaxCloud
                * [Registro en TaxCloud](finance/accounting/taxes/taxcloud#taxcloud-registration)
                * [Habilitar TaxCloud](finance/accounting/taxes/taxcloud#enable-taxcloud)
                * [Establecer categorías de TaxCloud en productos](finance/accounting/taxes/taxcloud#set-taxcloud-categories-on-products)
                * [Registrar de forma automática los impuestos en la cuenta de impuestos por pagar correcta](finance/accounting/taxes/taxcloud#automatically-post-taxes-in-the-correct-tax-payable-account)
                * [Detectar la posición fiscal de forma automática](finance/accounting/taxes/taxcloud#automatically-detect-the-fiscal-position)
                * [Interacción con cupones y promociones](finance/accounting/taxes/taxcloud#interaction-with-coupons-and-promotions)
              * Ventas a distancia intracomunitarias en la UE
                * [Configuración](finance/accounting/taxes/eu_distance_selling#configuration)
                * Ventanilla única
                  * [Reportes](finance/accounting/taxes/eu_distance_selling#reports)
              * Precios B2B (impuestos no incluidos) y B2C (impuestos incluidos)
                * Configuración
                  * [Introducción](finance/accounting/taxes/B2B_B2C#introduction)
                  * [Comercio electrónico](finance/accounting/taxes/B2B_B2C#ecommerce)
                  * [Gestionar productos](finance/accounting/taxes/B2B_B2C#setting-your-products)
                  * [Fijar la posición fiscal del B2C](finance/accounting/taxes/B2B_B2C#setting-the-b2c-fiscal-position)
                * [Realizar una cotización de prueba](finance/accounting/taxes/B2B_B2C#test-by-creating-a-quotation)
                * [Evite cambiar cada orden de ventas](finance/accounting/taxes/B2B_B2C#avoid-changing-every-sale-order)
      * [Facturas de cliente](finance/accounting/customer_invoices)
        * Desde la factura de cliente a la cobranza
          * [Desde el Borrador de factura a las Ganancias y pérdidas](finance/accounting/customer_invoices#from-draft-invoice-to-profit-and-loss)
          * [Creación de facturas](finance/accounting/customer_invoices#invoice-creation)
          * [Borradores de factura](finance/accounting/customer_invoices#draft-invoices)
          * [Facturas proforma o abiertas](finance/accounting/customer_invoices#open-or-pro-forma-invoices)
          * [Enviar la factura al cliente](finance/accounting/customer_invoices#send-the-invoice-to-customer)
          * [Pagos](finance/accounting/customer_invoices#payment)
          * [Recibir un pago parcial a través del estado de cuenta bancario](finance/accounting/customer_invoices#receive-a-partial-payment-through-the-bank-statement)
          * [Conciliar](finance/accounting/customer_invoices#reconcile)
          * Seguimiento de pagos
            * [Reporte de antigüedad del cliente:](finance/accounting/customer_invoices#customer-aging-report)
          * [Estado de resultados](finance/accounting/customer_invoices#profit-and-loss)
          * Balance general
            * Procesos de facturación
              * Ventas
                * [Órdenes de venta ‣ Factura](finance/accounting/customer_invoices/overview#sales-order-invoice)
                * [Orden de venta ‣ Orden de entrega ‣ Factura](finance/accounting/customer_invoices/overview#sales-order-delivery-order-invoice)
                * [Orden de comercio electrónico ‣ factura](finance/accounting/customer_invoices/overview#ecommerce-order-invoice)
              * Contratos
                * [Contratos ordinarios ‣ facturas](finance/accounting/customer_invoices/overview#regular-contracts-invoices)
                * [Contratos recurrentes ‣ facturas](finance/accounting/customer_invoices/overview#recurring-contracts-invoices)
              * Otros
                * [Crear una factura de manera manual](finance/accounting/customer_invoices/overview#creating-an-invoice-manually)
                * [Módulos específicos](finance/accounting/customer_invoices/overview#specific-modules)
                * [Cambiar la secuencia de las facturas](finance/accounting/customer_invoices/overview#resequencing-of-the-invoices)
                * [Digitalización de facturas con reconocimiento óptico de caracteres (OCR)](finance/accounting/customer_invoices/overview#invoice-digitization-with-optical-character-recognition-ocr)
            * Direcciones de entrega y de facturación
              * [Configuración](finance/accounting/customer_invoices/customer_addresses#configuration)
              * [Facturación y entrega en direcciones diferentes](finance/accounting/customer_invoices/customer_addresses#invoice-and-deliver-to-different-addresses)
            * Términos de pago y planes de pago a plazos
              * [Configuración](finance/accounting/customer_invoices/payment_terms#configuration)
              * [Usar términos de pago](finance/accounting/customer_invoices/payment_terms#using-payment-terms)
              * [Asientos contables](finance/accounting/customer_invoices/payment_terms#journal-entries)
            * Términos y condiciones predeterminados
              * [Configuración](finance/accounting/customer_invoices/terms_conditions#configuration)
            * Descuentos por pronto pago y reducción de impuestos
              * Configuración
                * [Reducciones de impuestos](finance/accounting/customer_invoices/cash_discounts#tax-reductions)
                * [Cuentas de ganancias o pérdidas por descuentos pronto pago](finance/accounting/customer_invoices/cash_discounts#cash-discount-gain-loss-accounts)
                * [Términos de pago](finance/accounting/customer_invoices/cash_discounts#payment-terms)
              * Aplicar un descuento por pronto pago a una factura
                * [Conciliación de pagos](finance/accounting/customer_invoices/cash_discounts#payment-reconciliation)
            * Notas de crédito y reembolsos
              * Emitir nota de crédito
                * [Reembolso parcial](finance/accounting/customer_invoices/credit_notes#partial-refund)
                * [Reembolso completo](finance/accounting/customer_invoices/credit_notes#full-refund)
                * [Reembolso completo y nuevo borrador de factura](finance/accounting/customer_invoices/credit_notes#full-refund-and-new-draft-invoice)
              * [Emitir nota de débito](finance/accounting/customer_invoices/credit_notes#issue-a-debit-note)
              * [Registrar un reembolso de proveedor](finance/accounting/customer_invoices/credit_notes#record-a-vendor-refund)
              * [Registrar una nota de débito](finance/accounting/customer_invoices/credit_notes#record-a-debit-note)
              * [Asientos contables](finance/accounting/customer_invoices/credit_notes#journal-entries)
            * Redondeo de efectivo
              * [Configuración](finance/accounting/customer_invoices/cash_rounding#configuration)
              * [Aplicar redondeos](finance/accounting/customer_invoices/cash_rounding#apply-roundings)
            * Ingresos diferidos
              * Prerrequisitos
                * [Configurar una cuenta de ingresos diferidos](finance/accounting/customer_invoices/deferred_revenues#configure-a-deferred-revenue-account)
                * Contabilizar un ingreso en la cuenta correcta
                  * [Seleccionar la cuenta en un borrador de factura](finance/accounting/customer_invoices/deferred_revenues#select-the-account-on-a-draft-invoice)
                  * [Elija una cuenta de ingresos diferente para productos específicos](finance/accounting/customer_invoices/deferred_revenues#choose-a-different-income-account-for-specific-products)
                  * [Modificar la cuenta de un apunte contable registrado](finance/accounting/customer_invoices/deferred_revenues#change-the-account-of-a-posted-journal-item)
              * Apuntes de ingresos diferidos
                * Crear un nuevo asiento
                  * [¿Qué significa «Prorata Temporis»?](finance/accounting/customer_invoices/deferred_revenues#what-does-prorata-temporis-mean)
                * [Asiento diferido del diario de ventas](finance/accounting/customer_invoices/deferred_revenues#deferred-entry-from-the-sales-journal)
              * Modelos de ingresos diferidos
                * [Aplicar un modelo de ingresos diferidos a un nuevo asiento](finance/accounting/customer_invoices/deferred_revenues#apply-a-deferred-revenue-model-to-a-new-entry)
              * [Automatizar los ingresos diferidos](finance/accounting/customer_invoices/deferred_revenues#automate-the-deferred-revenues)
            * Facturación electrónica (EDI)
              * [Configuración](finance/accounting/customer_invoices/electronic_invoicing#configuration)
            * Correo postal
              * [Configuración](finance/accounting/customer_invoices/snailmail#configuration)
              * [Enviar facturas por correo](finance/accounting/customer_invoices/snailmail#send-invoices-by-post)
              * [Precios](finance/accounting/customer_invoices/snailmail#pricing)
            * Códigos EPC QR
              * Configuración
                * [Configure su diario de cuenta bancaria](finance/accounting/customer_invoices/epc_qr_code#configure-your-bank-account-s-journal)
              * [Emitir facturas con códigos EPC QR](finance/accounting/customer_invoices/epc_qr_code#issue-invoices-with-epc-qr-codes)
            * Incoterms
              * [Definir un incoterm](finance/accounting/customer_invoices/incoterms#define-an-incoterm)
              * [Configuración predeterminada de Incoterms](finance/accounting/customer_invoices/incoterms#default-incoterm-configuration)
      * [Facturas de proveedor](finance/accounting/vendor_bills)
        * Creación de factura
          * [Manualmente](finance/accounting/vendor_bills#manually)
          * [Automáticamente](finance/accounting/vendor_bills#automatically)
        * [Finalización de la factura](finance/accounting/vendor_bills#bill-completion)
        * [Confirmación de la factura](finance/accounting/vendor_bills#bill-confirmation)
        * [Pago de la factura](finance/accounting/vendor_bills#bill-payment)
        * Reporte de cuentas antiguas por pagar
          * Digitalización de documentos con IA
            * [Configuración](finance/accounting/vendor_bills/invoice_digitization#configuration)
            * Cargar facturas
              * [Cargar facturas de forma manual](finance/accounting/vendor_bills/invoice_digitization#upload-invoices-manually)
              * [Cargar facturas usando un seudónimo de correo electrónico](finance/accounting/vendor_bills/invoice_digitization#upload-invoices-using-an-email-alias)
            * [Digitalización de facturas](finance/accounting/vendor_bills/invoice_digitization#invoice-digitization)
            * [Reconocimiento de datos por IA](finance/accounting/vendor_bills/invoice_digitization#data-recognition-with-ai)
            * [Precios](finance/accounting/vendor_bills/invoice_digitization#pricing)
          * Activos no circulantes y fijos
            * Prerrequisitos
              * [Configurar una cuenta de activos](finance/accounting/vendor_bills/assets#configure-an-assets-account)
              * Contabilizar un gasto en la cuenta correcta
                * [Seleccionar la cuenta en un borrador de factura](finance/accounting/vendor_bills/assets#select-the-account-on-a-draft-bill)
                * [Elija una cuenta de gastos diferente para productos específicos](finance/accounting/vendor_bills/assets#choose-a-different-expense-account-for-specific-products)
                * [Modificar la cuenta de un apunte contable registrado](finance/accounting/vendor_bills/assets#change-the-account-of-a-posted-journal-item)
            * Asientos contables de activos
              * Crear un nuevo asiento
                * [¿Qué significa «Prorata Temporis»?](finance/accounting/vendor_bills/assets#what-does-prorata-temporis-mean)
                * [¿Cuáles son los diferentes métodos de depreciación?](finance/accounting/vendor_bills/assets#what-are-the-different-depreciation-methods)
              * [Activos del diario de compras](finance/accounting/vendor_bills/assets#assets-from-the-purchases-journal)
            * [Modificación de un activo](finance/accounting/vendor_bills/assets#modification-of-an-asset)
            * [Eliminar activos fijos](finance/accounting/vendor_bills/assets#disposal-of-fixed-assets)
            * Modelos de activos
              * [Aplicar un modelo de activos a un nuevo asiento](finance/accounting/vendor_bills/assets#apply-an-asset-model-to-a-new-entry)
            * [Automatizar activos](finance/accounting/vendor_bills/assets#automate-the-assets)
          * Gastos diferidos y prepagos
            * Prerrequisitos
              * [Configurar una cuenta de gastos diferidos](finance/accounting/vendor_bills/deferred_expenses#configure-a-deferred-expense-account)
              * Contabilizar un gasto en la cuenta correcta
                * [Seleccionar la cuenta en un borrador de factura](finance/accounting/vendor_bills/deferred_expenses#select-the-account-on-a-draft-bill)
                * [Elija una cuenta de gastos diferente para productos específicos](finance/accounting/vendor_bills/deferred_expenses#choose-a-different-expense-account-for-specific-products)
                * [Modificar la cuenta de un apunte contable registrado](finance/accounting/vendor_bills/deferred_expenses#change-the-account-of-a-posted-journal-item)
            * Asientos de gastos diferidos
              * Crear un nuevo asiento
                * [¿Qué significa «Prorata Temporis»?](finance/accounting/vendor_bills/deferred_expenses#what-does-prorata-temporis-mean)
              * [Asiento diferido del diario de compras](finance/accounting/vendor_bills/deferred_expenses#deferred-entry-from-the-purchases-journal)
            * Modelos de gastos diferidos
              * [Aplicar un modelo de gasto diferido a un nuevo asiento](finance/accounting/vendor_bills/deferred_expenses#apply-a-deferred-expense-model-to-a-new-entry)
            * [Automatizar los gastos diferidos](finance/accounting/vendor_bills/deferred_expenses#automate-the-deferred-expenses)
      * [Pagos](finance/accounting/payments)
        * [Registrar un pago para una factura](finance/accounting/payments#registering-payment-from-an-invoice-or-bill)
        * Registrar pagos que no están ligados a una factura
          * [Vincular facturas con pagos](finance/accounting/payments#matching-invoices-and-bills-with-payments)
          * [Pago en lote](finance/accounting/payments#batch-payment)
          * [Emparejamiento de pagos](finance/accounting/payments#payments-matching)
          * [Conciliación de pagos por lote](finance/accounting/payments#batch-payments-matching)
        * [Registrar un pago parcial](finance/accounting/payments#registering-a-partial-payment)
        * Conciliar pagos con estados de cuenta bancarios
          * [Pagos en línea](finance/accounting/payments/online)
            * Instale el parche para desactivar el pago de factura en línea
              * [Actualizar Konvergo ERP a la versión más reciente](finance/accounting/payments/online/install_portal_patch#update-odoo-to-the-latest-release)
              * [Actualizar la lista de módulos disponibles](finance/accounting/payments/online/install_portal_patch#update-the-list-of-available-modules)
              * [Instalación del módulo Parche de pago de factura en línea](finance/accounting/payments/online/install_portal_patch#install-the-module-invoice-online-payment-patch)
            * [Configuración](finance/accounting/payments/online#configuration)
            * [Portal del cliente](finance/accounting/payments/online#customer-portal)
          * Cheques
            * [Método 1: cuentas pendientes](finance/accounting/payments/checks#method-1-outstanding-account)
            * [Método 2: ignorar la conciliación](finance/accounting/payments/checks#method-2-reconciliation-bypass)
            * [Registro de pagos](finance/accounting/payments/checks#payment-registration)
            * Asientos contables
              * [Cuentas pendientes](finance/accounting/payments/checks#outstanding-account)
              * [Ignorar el paso de conciliación](finance/accounting/payments/checks#reconciliation-bypass)
          * Pagos por lote para depósitos bancarios
            * [Configuración](finance/accounting/payments/batch#configuration)
            * Depositar varios pagos en lote
              * [Registrar pagos](finance/accounting/payments/batch#register-payments)
              * [Agregar pagos a un depósito por lote](finance/accounting/payments/batch#add-payments-to-a-batch-deposit)
              * [Conciliación bancaria](finance/accounting/payments/batch#bank-reconciliation)
          * Pagos por lotes: domiciliación bancaria SEPA (SDD)
            * [Configuración](finance/accounting/payments/batch_sdd#configuration)
            * Mandatos de adeudos directos SEPA
              * [Crear un mandato](finance/accounting/payments/batch_sdd#create-a-mandate)
              * [Domiciliación bancaria SEPA como método de pago](finance/accounting/payments/batch_sdd#sepa-direct-debit-as-a-payment-method)
              * [Cerrar o revocar un mandato.](finance/accounting/payments/batch_sdd#close-or-revoke-a-mandate)
            * Reciba pagos por lote mediante la domiciliación bancaria SEPA
              * [Facturas de cliente](finance/accounting/payments/batch_sdd#customer-invoices)
              * [Generar archivos `.XML` de domiciliación bancaria SEPA para adjuntar pagos](finance/accounting/payments/batch_sdd#generate-sepa-direct-debit-xml-files-to-submit-payments)
          * Seguimiento en las facturas
            * [Configuración](finance/accounting/payments/follow_up#configuration)
            * Reportes de seguimiento
              * [Nivel de confianza del deudor](finance/accounting/payments/follow_up#debtor-s-trust-level)
              * [Enviar recordatorios por lotes](finance/accounting/payments/follow_up#send-reminders-in-batches)
          * Transferencias internas
            * [Configuración](finance/accounting/payments/internal_transfers#configuration)
            * Registrar una transferencia interna de un banco a otro
              * Iniciar una transferencia interna
                * [Diario bancario (Banco A)](finance/accounting/payments/internal_transfers#bank-journal-bank-a)
                * [Asiento automatizado: Diario bancario (BANCO B)](finance/accounting/payments/internal_transfers#automated-booking-bank-journal-bank-b)
              * Gestione y concilie los extractos bancarios
                * [Entrada de diario bancario](finance/accounting/payments/internal_transfers#bank-journal-entry)
                * [Entrada de diario bancario](finance/accounting/payments/internal_transfers#id1)
          * Pagos con SEPA
            * Configuración
              * [Activar la transferencia de crédito SEPA (SCT)](finance/accounting/payments/pay_sepa#activate-sepa-credit-transfer-sct)
              * [Activar métodos de pago SEPA en bancos](finance/accounting/payments/pay_sepa#activate-sepa-payment-methods-on-banks)
              * [Registro de pagos](finance/accounting/payments/pay_sepa#registering-payments)
          * Pagar con cheques
            * Configuración
              * [Activar métodos de pago con cheque](finance/accounting/payments/pay_checks#activate-checks-payment-methods)
            * Material compatible para la impresión de cheques
              * [Estados Unidos](finance/accounting/payments/pay_checks#united-states)
            * Pagar una factura de proveedor con un cheque
              * [Registrar un pago con cheque](finance/accounting/payments/pay_checks#register-a-payment-by-check)
              * [Imprimir cheques](finance/accounting/payments/pay_checks#print-checks)
          * Pronóstico de futuras facturas por pagar
            * [Configuración: términos de pago](finance/accounting/payments/forecast#configuration-payment-terms)
            * [Pronóstico de las facturas a pagar con el reporte de cuentas antiguas por pagar](finance/accounting/payments/forecast#forecast-bills-to-pay-with-the-aged-payable-report)
            * [Seleccionar facturas por pagar](finance/accounting/payments/forecast#select-bills-to-pay)
      * [Cuentas bancarias y de efectivo](finance/accounting/bank)
        * Administre sus cuentas bancarias y de efectivo.
          * [Conecte su banco para la sincronización automática.](finance/accounting/bank#connect-your-bank-for-automatic-synchronization)
          * [Crear una cuenta bancaria](finance/accounting/bank#create-a-bank-account)
          * [Crear un diario de efectivo](finance/accounting/bank#create-a-cash-journal)
          * [Editar un diario bancario o de efectivo existente](finance/accounting/bank#edit-an-existing-bank-or-cash-journal)
        * Configuración
          * [Cuenta transitoria](finance/accounting/bank#suspense-account)
          * [Cuentas del estado de resultados](finance/accounting/bank#profit-and-loss-accounts)
          * [Moneda](finance/accounting/bank#currency)
          * [Número de cuenta](finance/accounting/bank#account-number)
          * [Conexiones bancarias](finance/accounting/bank#bank-feeds)
        * Cuentas pendientes
          * [Configuración predeterminada de cuentas](finance/accounting/bank#default-accounts-configuration)
          * Configuración de diarios bancarios y en efectivo
            * [Sincronización bancaria](finance/accounting/bank/bank_synchronization)
              * Configuración
                * [Usuarios locales](finance/accounting/bank/bank_synchronization#on-premise-users)
                * [Primera sincronización](finance/accounting/bank/bank_synchronization#first-synchronization)
                * [Sincronizar manualmente](finance/accounting/bank/bank_synchronization#synchronize-manually)
              * Problemas
                * [Error de sincronización](finance/accounting/bank/bank_synchronization#synchronization-in-error)
                * [Desconexión de la sincronización](finance/accounting/bank/bank_synchronization#synchronization-disconnected)
              * [Proceso de migración para usuarios que hayan instalado Konvergo ERP antes de diciembre de 2020](finance/accounting/bank/bank_synchronization#migration-process-for-users-having-installed-odoo-before-december-2020)
              * Preguntas frecuentes
                * [La sincronización no está funcionando en tiempo real, ¿es normal?](finance/accounting/bank/bank_synchronization#the-synchronization-is-not-working-in-real-time-is-that-normal)
                * [¿La función de sincronización bancaria en línea está incluida en mi contrato?](finance/accounting/bank/bank_synchronization#is-the-online-bank-synchronization-feature-included-in-my-contract)
                * [Algunos bancos tienen un estado «Beta», ¿qué significa?](finance/accounting/bank/bank_synchronization#some-banks-have-a-status-beta-what-does-this-mean)
                * [¿Por qué mis transacciones solo se sincronizan cuando las actualizo manualmente?](finance/accounting/bank/bank_synchronization#why-do-my-transactions-only-synchronize-when-i-refresh-manually)
                * [No todas mis transacciones pasadas están en Konvergo ERP, ¿por qué?](finance/accounting/bank/bank_synchronization#not-all-of-my-past-transactions-are-in-odoo-why)
                * [¿Por qué no veo ninguna transacción?](finance/accounting/bank/bank_synchronization#why-don-t-i-see-any-transactions)
                * ¿Cómo puedo actualizar mis credenciales bancarias?
                  * Salt Edge
                    * Configuración
                      * [Vincule sus cuentas bancarias con Konvergo ERP](finance/accounting/bank/bank_synchronization/saltedge#link-your-bank-accounts-with-odoo)
                      * [Actualice sus credenciales](finance/accounting/bank/bank_synchronization/saltedge#update-your-credentials)
                      * [Obtener cuentas nuevas](finance/accounting/bank/bank_synchronization/saltedge#fetch-new-accounts)
                    * Preguntas frecuentes
                      * [Aparece un error cuando intento de borrar la sincronización dentro de Konvergo ERP](finance/accounting/bank/bank_synchronization/saltedge#i-have-an-error-when-i-try-to-delete-my-synchronization-within-odoo)
                      * [Aparece un error en el que dice que ya sincronicé esta cuenta](finance/accounting/bank/bank_synchronization/saltedge#i-have-an-error-saying-that-i-have-already-synchronized-this-account)
                  * Ponto
                    * Configuración
                      * [Vincule sus cuentas bancarias con Ponto](finance/accounting/bank/bank_synchronization/ponto#link-your-bank-accounts-with-ponto)
                      * [Vincule su cuenta Ponto con su base de datos Konvergo ERP](finance/accounting/bank/bank_synchronization/ponto#link-your-ponto-account-with-your-odoo-database)
                      * [Actualice sus credenciales de sincronización](finance/accounting/bank/bank_synchronization/ponto#update-your-synchronization-credentials)
                      * [Obtener cuentas nuevas](finance/accounting/bank/bank_synchronization/ponto#fetch-new-accounts)
                    * Preguntas frecuentes
                      * [Después de mi sincronización, no aparece ninguna cuenta.](finance/accounting/bank/bank_synchronization/ponto#after-my-synchronization-no-account-appears)
                      * [Tengo un error en el que dice que mi autorización ha caducado.](finance/accounting/bank/bank_synchronization/ponto#i-have-an-error-about-that-my-authorization-has-expired)
                      * [Tengo algunos errores con mi institución en estado beta](finance/accounting/bank/bank_synchronization/ponto#i-have-some-errors-with-my-beta-institution)
                  * Enable Banking
                    * Configuración
                      * [Vincular cuentas bancarias con Konvergo ERP](finance/accounting/bank/bank_synchronization/enablebanking#link-bank-accounts-with-odoo)
            * Transacciones
              * [Importar transacciones](finance/accounting/bank/transactions#import-transactions)
              * [Registrar transacciones bancarias manualmente](finance/accounting/bank/transactions#register-bank-transactions-manually)
              * Extractos
                * [Creación de estados de cuenta desde la vista de kanban](finance/accounting/bank/transactions#statement-creation-from-the-kanban-view)
                * [Creación de estado de cuenta desde la vista de lista](finance/accounting/bank/transactions#statement-creation-from-the-list-view)
            * Conciliación bancaria
              * [Vista de conciliación bancaria](finance/accounting/bank/reconciliation#bank-reconciliation-view)
              * Conciliar transacciones
                * [Emparejar asientos existentes](finance/accounting/bank/reconciliation#match-existing-entries)
                * [Pagos por lotes](finance/accounting/bank/reconciliation#batch-payments)
                * [Operaciones manuales](finance/accounting/bank/reconciliation#manual-operations)
                * [Botones del modelo de conciliación](finance/accounting/bank/reconciliation#reconciliation-model-buttons)
            * Modelos de conciliación
              * [Tipos de modelos de conciliación](finance/accounting/bank/reconciliation_models#reconciliation-model-types)
              * Modelos de conciliación predeterminados
                * [Coincidencia perfecta de facturas](finance/accounting/bank/reconciliation_models#invoices-bills-perfect-match)
                * [Conciliación parcial de las facturas si no se han pagado](finance/accounting/bank/reconciliation_models#invoices-bills-partial-match-if-underpaid)
                * [Línea con comisiones bancarias](finance/accounting/bank/reconciliation_models#line-with-bank-fees)
              * [Mapeo de contactos](finance/accounting/bank/reconciliation_models#partner-mapping)
            * Gestione una cuenta bancaria en una moneda extranjera
              * Configuración
                * [Activar multidivisas](finance/accounting/bank/foreign_currency#activate-multi-currencies)
                * [Configurar divisas](finance/accounting/bank/foreign_currency#configure-currencies)
                * [Crear una nueva cuenta bancaria](finance/accounting/bank/foreign_currency#create-a-new-bank-account)
              * [Factura de proveedor en divisa extranjera](finance/accounting/bank/foreign_currency#vendor-bill-in-a-foreign-currency)
              * [Reporte de ganancias/pérdidas de divisas no realizadas](finance/accounting/bank/foreign_currency#unrealized-currency-gains-losses-report)
            * Caja registradora
              * [Configuración](finance/accounting/bank/cash_register#configuration)
              * Uso
                * [¿Cómo registrar pagos en efectivo?](finance/accounting/bank/cash_register#how-to-register-cash-payments)
                * [Ingresar dinero](finance/accounting/bank/cash_register#put-money-in)
                * [Sacar dinero](finance/accounting/bank/cash_register#take-money-out)
      * [Reportes](finance/accounting/reporting)
        * Principales reportes disponibles
          * [Balance general](finance/accounting/reporting#balance-sheet)
          * [Estado de resultados](finance/accounting/reporting#profit-and-loss)
          * [Resumen ejecutivo](finance/accounting/reporting#executive-summary)
          * [Libro mayor](finance/accounting/reporting#general-ledger)
          * [Cuenta antigua por pagar](finance/accounting/reporting#aged-payable)
          * [Cuentas por cobrar antiguas](finance/accounting/reporting#aged-receivable)
          * [Estado de flujos de efectivo](finance/accounting/reporting#cash-flow-statement)
          * Reporte de impuestos
            * Declaración de impuestos
              * Prerrequisitos
                * [Periodicidad de la declaración de impuestos](finance/accounting/reporting/tax_returns#tax-return-periodicity)
                * [Tablas de impuestos](finance/accounting/reporting/tax_returns#tax-grids)
              * Cerrar un periodo de impuestos
                * [Fecha de bloqueo de impuestos](finance/accounting/reporting/tax_returns#tax-lock-date)
                * [Reporte de impuestos](finance/accounting/reporting/tax_returns#tax-report)
            * [Traspaso de impuestos](finance/accounting/reporting/tax_carryover)
            * Contabilidad analítica
              * [Configuración](finance/accounting/reporting/analytic_accounting#configuration)
              * [Cuentas analíticas](finance/accounting/reporting/analytic_accounting#analytic-accounts)
              * [Planes analíticos](finance/accounting/reporting/analytic_accounting#analytic-plans)
              * Distribución analítica
                * [Modelos de distribución analítica](finance/accounting/reporting/analytic_accounting#analytic-distribution-models)
            * Presupuesto financiero
              * Configuración
                * [Posiciones presupuestarias](finance/accounting/reporting/budget#budgetary-positions)
              * Caso de uso
                * [Cuentas analíticas](finance/accounting/reporting/budget#analytical-accounts)
                * [Definir presupuesto](finance/accounting/reporting/budget#define-the-budget)
                * [Ver presupuesto](finance/accounting/reporting/budget#check-your-budget)
            * Intrastat
              * Configuración general
                * [Códigos predeterminados de transacción: facturación y reembolsos](finance/accounting/reporting/intrastat#default-transaction-codes-invoice-and-refund)
                * [Código regional](finance/accounting/reporting/intrastat#region-code)
              * Configuración de productos
                * [Código de mercancía](finance/accounting/reporting/intrastat#commodity-code)
                * [Cantidad: peso y unidades suplementarias](finance/accounting/reporting/intrastat#quantity-weight-and-supplementary-unit)
                * [País de origen](finance/accounting/reporting/intrastat#country-of-origin)
              * Configuración de las facturas
                * [Código de transacción](finance/accounting/reporting/intrastat#transaction-code)
                * [País del contacto](finance/accounting/reporting/intrastat#partner-country)
                * [Código de transporte](finance/accounting/reporting/intrastat#transport-code)
                * [Valor de los bienes](finance/accounting/reporting/intrastat#value-of-the-goods)
              * [Configuración de contacto](finance/accounting/reporting/intrastat#partner-configuration)
              * [Generar el reporte intrastat](finance/accounting/reporting/intrastat#generate-the-intrastat-report)
            * Reporte de comprobación de inalterabilidad de datos
              * [Bloquear asientos registrados con hash](finance/accounting/reporting/data_inalterability#lock-posted-entries-with-hash)
              * [Descargar reporte](finance/accounting/reporting/data_inalterability#report-download)
            * Integración con Silverfin
              * Configuración
                * Clave API de Konvergo ERP
                  * [Para una sola base de datos](finance/accounting/reporting/silverfin#per-database)
                  * [Para todas las bases de datos (fiduciarias)](finance/accounting/reporting/silverfin#for-all-databases-fiduciaries)
            * Reportes personalizados
              * [Reporte raíz](finance/accounting/reporting/customize#root-reports)
              * [Variantes](finance/accounting/reporting/customize#variants)
              * [Líneas](finance/accounting/reporting/customize#lines)
              * Expresiones
                * [Motor del dominio de Konvergo ERP](finance/accounting/reporting/customize#odoo-domain-engine)
                * [Etiquetas de impuestos](finance/accounting/reporting/customize#tax-tags-engine)
                * [Agregar otras fórmulas](finance/accounting/reporting/customize#aggregate-other-formulas-engine)
                * [Prefijo de los códigos de cuenta](finance/accounting/reporting/customize#prefix-of-account-codes-engine)
                * [Valor externo](finance/accounting/reporting/customize#external-value-engine)
                * [Función python personalizada](finance/accounting/reporting/customize#custom-python-function-engine)
              * [Columnas](finance/accounting/reporting/customize#columns)
            * Cierre del ejercicio
              * [Años fiscales](finance/accounting/reporting/year_end#fiscal-years)
              * Tareas a realizar antes de terminar el año fiscal
                * [Antes del cierre](finance/accounting/reporting/year_end#before-closure)
                * Cierre de año fiscal
                  * [Ganancias del año en curso](finance/accounting/reporting/year_end#current-year-s-earnings)
  * [Gastos](finance/expenses)
    * [Establecer categorías de gastos](finance/expenses#set-expense-categories)
    * Registrar gastos
      * Crear un nuevo gasto de manera manual
        * [Adjuntar un recibo](finance/expenses#attach-a-receipt)
      * [Crear nuevos gastos a partir de un recibo escaneado](finance/expenses#create-new-expenses-from-a-scanned-receipt)
      * [Crear nuevos gastos de forma automática desde un correo electrónico](finance/expenses#automatically-create-new-expenses-from-an-email)
    * Crear un reporte de gastos
      * [Presentar un reporte de gastos](finance/expenses#submit-an-expense-report)
    * [Aprobar gastos](finance/expenses#approve-expenses)
    * [Registrar gastos en Contabilidad](finance/expenses#post-expenses-in-accounting)
    * [Reembolsar a los empleados](finance/expenses#reimburse-employees)
    * Volver a facturar los gastos a los clientes.
      * [Configurar](finance/expenses#setup)
      * [Crear un gasto](finance/expenses#create-an-expense)
      * [Validar y publicar gastos](finance/expenses#validate-and-post-expenses)
      * [Gastos de factura](finance/expenses#invoice-expenses)
  * [Pagos en línea](finance/payment_providers)
    * Transferencias bancarias
      * [Configuración](finance/payment_providers/wire_transfer#configuration)
    * Adyen
      * Configuración
        * Pestaña de credenciales
          * [Clave API y clave de cliente](finance/payment_providers/adyen#api-key-and-client-key)
          * [Clave HMAC](finance/payment_providers/adyen#hmac-key)
          * [URLs de las API](finance/payment_providers/adyen#api-urls)
        * Cuenta de Adyen
          * [Permitir pagos de un origen específico](finance/payment_providers/adyen#allow-payments-from-a-specific-origin)
        * [Hacer una retención de tarjeta de crédito](finance/payment_providers/adyen#place-a-hold-on-a-card)
    * Alipay
      * Configuración
        * [Pestaña de credenciales](finance/payment_providers/alipay#credentials-tab)
    * Servicios de pago de Amazon
      * [Configuración en el tablero de APS](finance/payment_providers/amazon_payment_services#configuration-on-aps-dashboard)
      * [Configuración en Konvergo ERP](finance/payment_providers/amazon_payment_services#configuration-on-odoo)
    * AsiaPay
      * [Configuración en el tablero de AsiaPay](finance/payment_providers/asiapay#configuration-on-asiapay-dashboard)
      * [Configuración en Konvergo ERP](finance/payment_providers/asiapay#configuration-on-odoo)
    * Authorize.Net
      * Configuración
        * [Pestaña de credenciales](finance/payment_providers/authorize#credentials-tab)
        * Pestaña de configuración
          * [Hacer una retención de tarjeta de crédito](finance/payment_providers/authorize#place-a-hold-on-a-card)
      * Pagos ACH (solo para Estados Unidos)
        * [Configuración](finance/payment_providers/authorize#id2)
      * Importar un estado de cuenta de Authorize.Net
        * [Exportar desde Authorize.Net](finance/payment_providers/authorize#export-from-authorize-net)
        * [Importar a Konvergo ERP](finance/payment_providers/authorize#import-into-odoo)
    * Buckaroo
      * [Configuración en Buckaroo Plaza](finance/payment_providers/buckaroo#configuration-on-buckaroo-plaza)
      * [Configuración en Konvergo ERP](finance/payment_providers/buckaroo#configuration-on-odoo)
    * Demostración
      * [Configuración](finance/payment_providers/demo#configuration)
      * [Resultado del pago](finance/payment_providers/demo#payment-outcome)
      * [Estado de la transacción](finance/payment_providers/demo#transaction-state)
    * Flutterwave
      * [Configuración en el tablero de Flutterwave](finance/payment_providers/flutterwave#configuration-on-flutterwave-dashboard)
      * [Configuración en Konvergo ERP](finance/payment_providers/flutterwave#configuration-on-odoo)
    * Mercado Pago
      * [Configuración en el tablero de Mercado Pago](finance/payment_providers/mercado_pago#configuration-on-mercado-pago-dashboard)
      * [Configuración en Konvergo ERP](finance/payment_providers/mercado_pago#configuration-on-odoo)
    * Mollie
      * Configuración
        * [Pestaña de credenciales](finance/payment_providers/mollie#credentials-tab)
    * Ogone
      * Coonfiguración en Ogone
        * [Cree un usuario API](finance/payment_providers/ogone#create-an-api-user)
        * [Configure Ogone para Konvergo ERP](finance/payment_providers/ogone#set-up-ogone-for-odoo)
      * [Ajustes en Konvergo ERP](finance/payment_providers/ogone#settings-in-odoo)
    * PayPal
      * Configuración en PayPal
        * [Retorno automático](finance/payment_providers/paypal#auto-return)
        * [Transferencia de datos de pago (PDT)](finance/payment_providers/paypal#payment-data-transfer-pdt)
        * [Notificación de pago instantáneo (IPN)](finance/payment_providers/paypal#instant-payment-notification-ipn)
        * [Cuenta opcional PayPal](finance/payment_providers/paypal#paypal-account-optional)
        * [Formato de mensajes de pago](finance/payment_providers/paypal#payment-messages-format)
      * Ajustes en Konvergo ERP
        * [Credenciales](finance/payment_providers/paypal#credentials)
        * [Tarifas adicionales](finance/payment_providers/paypal#extra-fees)
      * Entorno de prueba
        * [Configuración](finance/payment_providers/paypal#configuration)
    * Razorpay
      * [Configuración en el tablero de RazorPay](finance/payment_providers/razorpay#configuration-on-razorpay-dashboard)
      * [Configuración en Konvergo ERP](finance/payment_providers/razorpay#configuration-on-odoo)
    * SIPS
      * Configuración
        * [Pestaña de credenciales](finance/payment_providers/sips#credentials-tab)
    * Stripe
      * Cree su cuenta de Stripe con Konvergo ERP
        * [Complete sus credenciales](finance/payment_providers/stripe#fill-in-your-credentials)
        * [Genere un webhook](finance/payment_providers/stripe#generate-a-webhook)
      * [Activar métodos de pago locales](finance/payment_providers/stripe#enable-local-payment-methods)
      * [Activar Apple Pay](finance/payment_providers/stripe#enable-apple-pay)
    * Proveedores de pago admitidos
      * [Proveedores de pago en línea](finance/payment_providers#online-payment-providers)
      * [Pagos bancarios](finance/payment_providers#bank-payments)
    * Activar un proveedor de pago
      * [Modo de prueba](finance/payment_providers#test-mode)
    * [Formulario de pago](finance/payment_providers#payment-form)
    * [Tokenización](finance/payment_providers#tokenization)
    * [Captura manual](finance/payment_providers#manual-capture)
    * [Reembolsos](finance/payment_providers#refunds)
    * [Finalización de compra exprés](finance/payment_providers#express-checkout)
    * [Cuotas adicionales](finance/payment_providers#extra-fees)
    * Disponibilidad
      * [Divisas y países](finance/payment_providers#currencies-and-countries)
      * [Cantidad máxima](finance/payment_providers#maximum-amount)
    * Diario de pagos
      * [Perspectiva contable](finance/payment_providers#accounting-perspective)
  * [Localizaciones fiscales](finance/fiscal_localizations)
    * Paquetes de localización fiscal
      * [Configuración](finance/fiscal_localizations#configuration)
      * [Uso](finance/fiscal_localizations#use)
    * Lista de países compatibles
      * Argentina
        * [Webinarios](finance/fiscal_localizations/argentina#webinars)
        * Configuración
          * [Instalación de módulos](finance/fiscal_localizations/argentina#modules-installation)
          * [Configure su empresa](finance/fiscal_localizations/argentina#configure-your-company)
          * [Plan de cuentas](finance/fiscal_localizations/argentina#chart-of-account)
          * Configurar los datos maestros
            * Credenciales de factura electrónica
              * [Entorno](finance/fiscal_localizations/argentina#environment)
              * [Certificados AFIP](finance/fiscal_localizations/argentina#afip-certificates)
            * Contacto
              * [Tipo de identificación e IVA](finance/fiscal_localizations/argentina#identification-type-and-vat)
              * [Tipo de responsabilidad AFIP](finance/fiscal_localizations/argentina#afip-responsibility-type)
            * Impuestos
              * [Tipos de impuestos](finance/fiscal_localizations/argentina#taxes-types)
              * [Impuestos especiales](finance/fiscal_localizations/argentina#special-taxes)
            * Tipos de documentos
              * [Letras](finance/fiscal_localizations/argentina#letters)
              * [Uso en facturas](finance/fiscal_localizations/argentina#use-on-invoices)
          * Diarios contables
            * Información AFIP (también conocida como Punto de venta AFIP)
              * [Servicios web](finance/fiscal_localizations/argentina#web-services)
            * [Secuencias](finance/fiscal_localizations/argentina#sequences)
        * Uso y prueba
          * Facturas
            * [Asignación de tipo de documento](finance/fiscal_localizations/argentina#document-type-assignation)
            * [Elementos de facturas electrónicas](finance/fiscal_localizations/argentina#electronic-invoice-elements)
            * [Impuestos en facturas](finance/fiscal_localizations/argentina#invoice-taxes)
            * Casos de uso especiales
              * [Facturas de servicios](finance/fiscal_localizations/argentina#invoices-for-services)
              * [Facturas de exportación](finance/fiscal_localizations/argentina#exportation-invoices)
              * [Bono fiscal](finance/fiscal_localizations/argentina#fiscal-bond)
              * [Factura de crédito electrónica MiPyme (FCE)](finance/fiscal_localizations/argentina#electronic-credit-invoice-mipyme-fce)
            * [Reporte impreso de factura](finance/fiscal_localizations/argentina#invoice-printed-report)
            * [Solución de problemas y auditorías](finance/fiscal_localizations/argentina#troubleshooting-and-auditing)
          * Facturas de proveedor
            * Validar el número de factura de proveedor en la AFIP
              * [Validar facturas de proveedor en Konvergo ERP](finance/fiscal_localizations/argentina#validate-vendor-bills-in-odoo)
            * Casos de uso especiales
              * [Conceptos sin impuestos](finance/fiscal_localizations/argentina#untaxed-concepts)
              * [Impuestos de percepción](finance/fiscal_localizations/argentina#perception-taxes)
          * Gestión de cheques
            * Cheques propios
              * [Gestión de cheques propios](finance/fiscal_localizations/argentina#management-of-own-checks)
              * [Cancelar un cheque propio](finance/fiscal_localizations/argentina#cancel-an-own-check)
            * Cheques de terceros
              * [Nuevos cheques de terceros](finance/fiscal_localizations/argentina#new-third-party-checks)
              * [Cheques existentes de terceros](finance/fiscal_localizations/argentina#existing-third-party-checks)
        * Reportes
          * Reportes de IVA
            * [Libro IVA de ventas](finance/fiscal_localizations/argentina#sales-vat-book)
            * [Libro IVA de compras](finance/fiscal_localizations/argentina#purchases-vat-book)
            * [Resumen de IVA](finance/fiscal_localizations/argentina#vat-summary)
          * IIBB - Reportes
            * [IIBB - Ventas por jurisdicción](finance/fiscal_localizations/argentina#iibb-sales-by-jurisdiction)
            * [IIBB - Compras por jurisdicción](finance/fiscal_localizations/argentina#iibb-purchases-by-jurisdiction)
      * Australia
        * Héroe de empleo de la nómina australiana
          * [Configuración](finance/fiscal_localizations/australia#configuration)
          * [¿Cómo funciona la API?](finance/fiscal_localizations/australia#how-does-the-api-work)
      * Bélgica
        * [Configuración](finance/fiscal_localizations/belgium#configuration)
        * [Plan de cuentas](finance/fiscal_localizations/belgium#chart-of-accounts)
        * Impuestos
          * [Impuestos no deducibles](finance/fiscal_localizations/belgium#non-deductible-taxes)
        * Reportes
          * Reporte de gastos rechazados
            * [Gastos de restaurante](finance/fiscal_localizations/belgium#restaurant-expenses)
            * [Gastos de automóviles: separación de vehículos](finance/fiscal_localizations/belgium#car-expenses-vehicle-split)
        * Formulario de impuestos 281.50 y formulario 325
          * [Formulario de impuestos 281.50](finance/fiscal_localizations/belgium#fee-form-281-50)
          * [Formulario 325](finance/fiscal_localizations/belgium#form-325)
        * Estados de cuenta CODA y SODA
          * [CODA](finance/fiscal_localizations/belgium#coda)
          * [SODA](finance/fiscal_localizations/belgium#soda)
        * [Facturación electrónica](finance/fiscal_localizations/belgium#electronic-invoicing)
        * [Descuento por pronto pago](finance/fiscal_localizations/belgium#cash-discount)
        * Certificación fiscal: restaurante en PdV
          * [Sistema PdV certificado](finance/fiscal_localizations/belgium#certified-pos-system)
          * Módulo de datos fiscales (FDM, por sus siglas en inglés)
            * Configuración
              * [Módulo de caja negra](finance/fiscal_localizations/belgium#black-box-module)
              * [Caja IoT](finance/fiscal_localizations/belgium#iot-box)
          * [Tarjeta de firma de IVA](finance/fiscal_localizations/belgium#vat-signing-card)
      * Brasil
        * [Introducción](finance/fiscal_localizations/brazil#introduction)
        * Configuración
          * [Instalación de módulos](finance/fiscal_localizations/brazil#modules-installation)
          * [Configure su empresa](finance/fiscal_localizations/brazil#configure-your-company)
          * Configurar la integración con AvaTax
            * [Configuración con credenciales](finance/fiscal_localizations/brazil#credential-configuration)
          * Configurar los datos maestros
            * [Plan de cuentas](finance/fiscal_localizations/brazil#chart-of-accounts)
            * [Impuestos](finance/fiscal_localizations/brazil#taxes)
            * [Productos](finance/fiscal_localizations/brazil#products)
            * [Contactos](finance/fiscal_localizations/brazil#contacts)
            * [Posiciones fiscales](finance/fiscal_localizations/brazil#fiscal-positions)
        * Flujos de trabajo
          * [Cálculo de impuestos en cotizaciones y órdenes de venta](finance/fiscal_localizations/brazil#tax-calculations-on-quotation-sales-orders)
          * [Cálculo de impuestos en facturas](finance/fiscal_localizations/brazil#tax-calculations-on-invoices)
      * Chile
        * [Módulos](finance/fiscal_localizations/chile#modules)
        * [Información de la empresa](finance/fiscal_localizations/chile#company-information)
        * Ajustes de contabilidad
          * [Información fiscal](finance/fiscal_localizations/chile#fiscal-information)
          * [Datos de facturación electrónica](finance/fiscal_localizations/chile#electronic-invoice-data)
        * Servidor de correo entrante para DTE
          * [Certificado](finance/fiscal_localizations/chile#certificate)
        * [Multidivisa](finance/fiscal_localizations/chile#multicurrency)
        * [Información del contacto](finance/fiscal_localizations/chile#partner-information)
        * Tipos de documentos
          * [Uso en facturas](finance/fiscal_localizations/chile#use-on-invoices)
        * Diarios contables
          * [Crear un diario de ventas](finance/fiscal_localizations/chile#create-a-sales-journal)
        * CAF
          * [Subir archivos CAF](finance/fiscal_localizations/chile#upload-caf-files)
        * [Plan de cuentas](finance/fiscal_localizations/chile#chart-of-accounts)
        * [Impuestos](finance/fiscal_localizations/chile#taxes)
        * Uso y prueba
          * [Flujo de trabajo de la factura electrónica](finance/fiscal_localizations/chile#electronic-invoice-workflow)
          * Emisión de factura para el cliente
            * [Validación y estado del DTE](finance/fiscal_localizations/chile#validation-and-dte-status)
            * [Referencias cruzadas](finance/fiscal_localizations/chile#crossed-references)
            * [Reporte la de factura en PDF](finance/fiscal_localizations/chile#invoice-pdf-report)
            * [Validación comercial](finance/fiscal_localizations/chile#commercial-validation)
            * [Proceso para facturas con reclamo](finance/fiscal_localizations/chile#processed-for-claimed-invoices)
            * [Errores comunes](finance/fiscal_localizations/chile#common-errors)
          * Notas de crédito
            * Casos de uso
              * [Cancelar el documento de referencia](finance/fiscal_localizations/chile#cancel-referenced-document)
              * [Corregir el documento de referencia](finance/fiscal_localizations/chile#correct-referenced-document)
              * [Corregir el monto del documento de referencia](finance/fiscal_localizations/chile#corrects-referenced-document-amount)
          * Notas de débito
            * Casos de uso
              * [Agrega un cargo adicional a las facturas](finance/fiscal_localizations/chile#add-debt-on-invoices)
              * [Cancelar notas de crédito](finance/fiscal_localizations/chile#cancel-credit-notes)
          * Facturas de proveedor
            * [Recepción](finance/fiscal_localizations/chile#reception)
            * [Aceptación](finance/fiscal_localizations/chile#acceptation)
            * [Reclamación](finance/fiscal_localizations/chile#claim)
          * Boletas electrónicas de compra
            * [Configuración](finance/fiscal_localizations/chile#configuration)
            * [Generar una boleta electrónica de compra](finance/fiscal_localizations/chile#generate-an-electronic-purchase-invoice)
          * Guía de entrega
            * [Guía de entrega a partir de un proceso de venta](finance/fiscal_localizations/chile#delivery-guide-from-a-sales-process)
          * Boletas electrónicas
            * [Validación y estado del DTE](finance/fiscal_localizations/chile#id2)
          * Exportaciones electrónicas de bienes
            * [Configuraciones de contacto](finance/fiscal_localizations/chile#contact-configurations)
            * [Aduanas de Chile](finance/fiscal_localizations/chile#chilean-customs)
            * [Reporte en PDF](finance/fiscal_localizations/chile#pdf-report)
        * Reportes financieros
          * [Balance tributario de 8 columnas](finance/fiscal_localizations/chile#balance-tributario-de-8-columnas)
          * [Propuesta F29](finance/fiscal_localizations/chile#propuesta-f29)
      * Colombia
        * Configuración
          * [Instalación de módulos](finance/fiscal_localizations/colombia#modules-installation)
          * [Configuración de la empresa](finance/fiscal_localizations/colombia#company-configuration)
          * [Configuración de las credenciales de Carvajal](finance/fiscal_localizations/colombia#carjaval-credentials-configuration)
          * [Configuración de los datos del reporte](finance/fiscal_localizations/colombia#report-data-configuration)
          * Configuración de los datos maestros
            * Contacto
              * [Información de identificación](finance/fiscal_localizations/colombia#identification-information)
              * [Información fiscal](finance/fiscal_localizations/colombia#fiscal-information)
            * [Productos](finance/fiscal_localizations/colombia#products)
            * [Impuestos](finance/fiscal_localizations/colombia#taxes)
            * Diarios de ventas
              * [Secuencia de facturación](finance/fiscal_localizations/colombia#invoice-sequence)
              * [Diarios de compra](finance/fiscal_localizations/colombia#purchase-journals)
              * [Plan de cuentas](finance/fiscal_localizations/colombia#chart-of-accounts)
        * Flujos de trabajo principales
          * Facturas electrónicas
            * [Creación de facturas](finance/fiscal_localizations/colombia#invoice-creation)
            * [Validación de la factura](finance/fiscal_localizations/colombia#invoice-validation)
            * [Recepción de XML legal y PDF](finance/fiscal_localizations/colombia#reception-of-legal-xml-and-pdf)
          * [Notas de crédito](finance/fiscal_localizations/colombia#credit-notes)
          * [Notas de débito](finance/fiscal_localizations/colombia#debit-notes)
          * [Documento soporte para las facturas de proveedor](finance/fiscal_localizations/colombia#support-document-for-vendor-bills)
          * [Errores comunes](finance/fiscal_localizations/colombia#common-errors)
        * Reportes financieros
          * [Certificado de retención en ICA](finance/fiscal_localizations/colombia#certificado-de-retencion-en-ica)
          * [Certificado de retención en IVA](finance/fiscal_localizations/colombia#certificado-de-retencion-en-iva)
          * [Certificado de retención en la fuente](finance/fiscal_localizations/colombia#certificado-de-retencion-en-la-fuente)
      * Ecuador
        * Introducción
          * [Glosario](finance/fiscal_localizations/ecuador#glossary)
        * Configuración
          * [Instalación de módulos](finance/fiscal_localizations/ecuador#modules-installation)
          * [Configure su empresa](finance/fiscal_localizations/ecuador#configure-your-company)
          * [Documentos electrónicos](finance/fiscal_localizations/ecuador#electronic-documents)
          * [Retención de IVA](finance/fiscal_localizations/ecuador#vat-withholding)
          * [Puntos de impresión](finance/fiscal_localizations/ecuador#printer-points)
          * [Retenciones](finance/fiscal_localizations/ecuador#withholding)
          * [Liquidaciones de compra](finance/fiscal_localizations/ecuador#purchase-liquidations)
          * Configurar los datos maestros
            * [Plan de cuentas](finance/fiscal_localizations/ecuador#chart-of-accounts)
            * [Productos](finance/fiscal_localizations/ecuador#products)
            * [Contactos](finance/fiscal_localizations/ecuador#contacts)
            * [Revisar sus impuestos](finance/fiscal_localizations/ecuador#review-your-taxes)
            * [Revisar sus tipos de documento](finance/fiscal_localizations/ecuador#review-your-document-types)
        * Flujos de trabajo
          * Documentos de ventas
            * [Facturas de cliente](finance/fiscal_localizations/ecuador#customer-invoices)
            * [Nota de crédito del cliente](finance/fiscal_localizations/ecuador#customer-credit-note)
            * [Notas de débito del cliente](finance/fiscal_localizations/ecuador#customer-debit-note)
            * [Retención de cliente](finance/fiscal_localizations/ecuador#customer-withholding)
          * Documentos de compra
            * [Factura de proveedor](finance/fiscal_localizations/ecuador#vendor-bill)
            * [Liquidación de compra](finance/fiscal_localizations/ecuador#purchase-liquidation)
            * [Retención de compra](finance/fiscal_localizations/ecuador#purchase-withholding)
        * Reportes financieros
          * [Reporte 103](finance/fiscal_localizations/ecuador#report-103)
          * [Reporte 104](finance/fiscal_localizations/ecuador#report-104)
          * Reporte ATS
            * Configuración
              * [Facturas de proveedor](finance/fiscal_localizations/ecuador#vendor-bills)
              * [Notas de crédito y débito](finance/fiscal_localizations/ecuador#credit-and-debit-notes)
            * [Generar archivos XML](finance/fiscal_localizations/ecuador#xml-generation)
      * Egipto
        * [Instalación](finance/fiscal_localizations/egypt#installation)
        * Facturación electrónica para Egipto
          * [Registre Konvergo ERP en su portal ETA](finance/fiscal_localizations/egypt#register-odoo-on-your-eta-portal)
          * Configuración en Konvergo ERP
            * [Códigos de la ETA](finance/fiscal_localizations/egypt#eta-codes)
            * [Sucursales](finance/fiscal_localizations/egypt#branches)
            * [Clientes](finance/fiscal_localizations/egypt#customers)
            * [Productos](finance/fiscal_localizations/egypt#products)
          * Autenticación por USB
            * [Instalar Konvergo ERP como proxy local en su computadora](finance/fiscal_localizations/egypt#install-odoo-as-a-local-proxy-on-your-computer)
            * [Configurar la clave USB](finance/fiscal_localizations/egypt#configure-the-usb-key)
      * Francia
        * FEC - Fichier des Écritures Comptables
          * Importar FEC
            * [Formatos de archivo](finance/fiscal_localizations/france#file-formats)
            * [Descripción y uso de los campos](finance/fiscal_localizations/france#fields-description-and-use)
            * Detalles de implementación
              * [Cuentas](finance/fiscal_localizations/france#accounts)
              * [Emparejamiento de código](finance/fiscal_localizations/france#code-matching)
              * [Marcado como conciliado](finance/fiscal_localizations/france#reconcilable-flag)
              * [Tipo de cuenta y emparejamiento de plantillas](finance/fiscal_localizations/france#account-type-and-templates-matching)
              * [Diarios contables](finance/fiscal_localizations/france#journals)
              * [Determinación del tipo de diario](finance/fiscal_localizations/france#journal-type-determination)
              * [Contactos](finance/fiscal_localizations/france#partners)
              * [Movimientos](finance/fiscal_localizations/france#moves)
              * [Problemas de redondeamiento](finance/fiscal_localizations/france#rounding-issues)
              * [Nombre de movimiento faltante](finance/fiscal_localizations/france#missing-move-name)
              * [Información del contacto](finance/fiscal_localizations/france#partner-information)
          * [Exportar](finance/fiscal_localizations/france#export)
        * [Reportes contables franceses](finance/fiscal_localizations/france#french-accounting-reports)
        * Obtener la certificación antifraude del IVA con Konvergo ERP
          * [¿Mi empresa necesita usar un software antifraude?](finance/fiscal_localizations/france#is-my-company-required-to-use-anti-fraud-software)
          * [Obtenga la certificación con Konvergo ERP](finance/fiscal_localizations/france#get-certified-with-odoo)
          * Funciones antifraude
            * [Inalterabilidad](finance/fiscal_localizations/france#inalterability)
            * [Seguridad](finance/fiscal_localizations/france#security)
            * [Almacenamiento](finance/fiscal_localizations/france#storage)
          * [Responsabilidades](finance/fiscal_localizations/france#responsibilities)
          * [Más información](finance/fiscal_localizations/france#more-information)
      * Alemania
        * [Plan de cuentas de Alemania](finance/fiscal_localizations/germany#german-chart-of-accounts)
        * [Reportes contables alemanes](finance/fiscal_localizations/germany#german-accounting-reports)
        * [Exportación de Konvergo ERP a Datev](finance/fiscal_localizations/germany#export-from-odoo-to-datev)
        * Punto de venta en Alemania: sistema de seguridad técnica
          * Configuración
            * [Instalación de módulos](finance/fiscal_localizations/germany#modules-installation)
            * [Registre su empresa ante la autoridad fiscal](finance/fiscal_localizations/germany#register-your-company-at-the-financial-authority)
            * [Cree y vincule un sistema de seguridad técnica a su PdV](finance/fiscal_localizations/germany#create-and-link-a-technical-security-system-to-your-pos)
          * [DSFinV-K](finance/fiscal_localizations/germany#dsfinv-k)
        * Estándares para la contabilidad tributaria alemana: la guía de Konvergo ERP para la conformidad con las normas GoBD
          * [¿Qué necesita saber sobre GoBD al confiar en un software de contabilidad?](finance/fiscal_localizations/germany#what-do-you-need-to-know-about-gobd-when-relying-on-accounting-software)
          * [¿Qué hay de la seguridad de los datos?](finance/fiscal_localizations/germany#what-about-data-security)
          * [Responsabilidad del editor del software](finance/fiscal_localizations/germany#responsibility-of-the-software-editor)
          * [¿Cómo puede ir en conformidad con las normas con la ayuda de Konvergo ERP?](finance/fiscal_localizations/germany#how-can-odoo-help-you-achieve-compliance)
          * [¿Necesita un archivo de exportación GoBD?](finance/fiscal_localizations/germany#do-you-need-a-gobd-export)
          * [¿Cuál es la función y el significado del certificado de conformidad?](finance/fiscal_localizations/germany#what-is-the-role-and-meaning-of-the-compliance-certification)
          * [¿Qué pasa si no cumple con las normas adecuadas?](finance/fiscal_localizations/germany#what-happens-if-you-are-not-compliant)
      * India
        * [Instalación](finance/fiscal_localizations/india#installation)
        * Sistema de facturación electrónica
          * Configurar
            * [Registro de facturación electrónica NIC](finance/fiscal_localizations/india#nic-e-invoice-registration)
            * Configuración en Konvergo ERP
              * [Diarios contables](finance/fiscal_localizations/india#journals)
          * Flujo de trabajo
            * [Validación de la factura](finance/fiscal_localizations/india#invoice-validation)
            * [Reporte la de factura en PDF](finance/fiscal_localizations/india#invoice-pdf-report)
            * [Cancelar una factura electrónica](finance/fiscal_localizations/india#e-invoice-cancellation)
            * [Verificación de facturación electrónica GST](finance/fiscal_localizations/india#gst-e-invoice-verification)
        * Guía de embarque electrónica
          * Configurar
            * [Registro de la API en la guía de embarque electrónica NIC](finance/fiscal_localizations/india#api-registration-on-nic-e-way-bill)
            * [Configuración en Konvergo ERP](finance/fiscal_localizations/india#india-e-waybill-configuration)
          * Flujo de trabajo
            * [Enviar una guía de embarque electrónica](finance/fiscal_localizations/india#send-an-e-way-bill)
            * [Validación de la factura](finance/fiscal_localizations/india#india-invoice-validation-e-way)
            * [Reporte la de factura en PDF](finance/fiscal_localizations/india#id6)
            * [Cancelar una guía de embarque electrónica](finance/fiscal_localizations/india#e-way-bill-cancellation)
        * Declaración de impuestos GST en la India
          * [Habilitar acceso a la API](finance/fiscal_localizations/india#enable-api-access)
          * [Servicio GST de la India en Konvergo ERP](finance/fiscal_localizations/india#indian-gst-service-in-odoo)
          * Presentar declaraciones GST
            * [Enviar el GSTR-1](finance/fiscal_localizations/india#send-gstr-1)
            * [Recibir el GSTR-2B](finance/fiscal_localizations/india#receive-gstr-2b)
            * [Reporte GSTR-3](finance/fiscal_localizations/india#gstr-3-report)
        * Reportes de impuestos
          * [Reporte GSTR-1](finance/fiscal_localizations/india#gstr-1-report)
          * [Reporte GSTR-3](finance/fiscal_localizations/india#india-gstr-3-report)
      * Indonesia
        * Módulo de E-Faktur
          * [Ajustes de NPWP y NIK](finance/fiscal_localizations/indonesia#npwp-nik-settings)
          * Uso
            * [Generar un número de serie para una factura impositiva](finance/fiscal_localizations/indonesia#generate-tax-invoice-serial-number)
            * [Generar el archivo CSV de e-faktur desde una factura o un lote de facturas](finance/fiscal_localizations/indonesia#generate-e-faktur-csv-for-a-single-invoice-or-a-batch-invoices)
            * [Kode Transaksi FP (Código de transacción)](finance/fiscal_localizations/indonesia#kode-transaksi-fp-transaction-code)
            * [Corregir una factura que se publicó y se descargó: función para reemplazar la factura](finance/fiscal_localizations/indonesia#correct-an-invoice-that-has-been-posted-and-downloaded-replace-invoice-feature)
            * [Corregir una factura que se publicó pero no se ha descargado: restablecer e-Faktur](finance/fiscal_localizations/indonesia#correct-an-invoice-that-has-been-posted-but-not-downloaded-yet-reset-e-faktur)
      * Italia
        * Configuración
          * [Información de la empresa](finance/fiscal_localizations/italy#company-information)
          * Facturación electrónica
            * [Intercambio electrónico de datos (EDI)](finance/fiscal_localizations/italy#electronic-data-interchange-edi)
          * [Autorización para el procesamiento de archivos (Konvergo ERP)](finance/fiscal_localizations/italy#file-processing-authorization-odoo)
        * Configuración de impuestos
          * Cobro revertido externo
            * [Facturas](finance/fiscal_localizations/italy#invoices)
            * [Facturas de proveedor](finance/fiscal_localizations/italy#vendor-bills)
          * [Cobro revertido interno](finance/fiscal_localizations/italy#internal-reverse-charge)
          * [Tablas de impuestos de “cobro revertido”](finance/fiscal_localizations/italy#reverse-charge-tax-grids)
        * San Marino
          * [Facturas](finance/fiscal_localizations/italy#id1)
          * [Facturas](finance/fiscal_localizations/italy#bills)
        * Pubblica amministrazione (B2G)
          * [Firma digital calificada](finance/fiscal_localizations/italy#digital-qualified-signature)
          * [CIG, CUP, DatiOrdineAcquisto](finance/fiscal_localizations/italy#cig-cup-datiordineacquisto)
      * Kenia
        * [Configuración](finance/fiscal_localizations/kenya#configuration)
        * Integración con el TIMS de Kenia
          * [Instalar el servidor proxy en un dispositivo Windows](finance/fiscal_localizations/kenya#installing-the-proxy-server-on-a-windows-device)
          * [Envío de los datos a la KRA mediante la unidad de control Tremol G03](finance/fiscal_localizations/kenya#sending-the-data-to-kra-using-the-tremol-g03-control-unit)
      * Luxemburgo
        * [Configuración](finance/fiscal_localizations/luxembourg#configuration)
        * [Plan de cuentas estándar - PCN 2020](finance/fiscal_localizations/luxembourg#standard-chart-of-accounts-pcn-2020)
        * [Declaración fiscal eCDF](finance/fiscal_localizations/luxembourg#ecdf-tax-return)
        * [Declaración fiscal anual](finance/fiscal_localizations/luxembourg#annual-tax-report)
        * FAIA (SAF-T)
          * [Exportar el archivo FAIA](finance/fiscal_localizations/luxembourg#export-faia-file)
      * México
        * [Webinarios](finance/fiscal_localizations/mexico#webinars)
        * [Introducción](finance/fiscal_localizations/mexico#introduction)
        * Configuración
          * [Requisitos](finance/fiscal_localizations/mexico#requirements)
          * [Instalación de los módulos](finance/fiscal_localizations/mexico#installing-modules)
          * [Configure su empresa](finance/fiscal_localizations/mexico#configure-your-company)
          * [Contactos](finance/fiscal_localizations/mexico#contacts)
          * Impuestos
            * [Tipo factor](finance/fiscal_localizations/mexico#factor-type)
            * [Objeto de impuestos](finance/fiscal_localizations/mexico#tax-object)
            * [Otras configuraciones fiscales](finance/fiscal_localizations/mexico#other-tax-configurations)
          * [Productos](finance/fiscal_localizations/mexico#products)
          * Facturación electrónica
            * [Credenciales del proveedor autorizado de certificación](finance/fiscal_localizations/mexico#pac-credentials)
            * [Certificados .cer y .key](finance/fiscal_localizations/mexico#cer-and-key-certificates)
        * Flujos de trabajo
          * Facturación electrónica
            * [Facturas de cliente](finance/fiscal_localizations/mexico#customer-invoices)
            * [Notas de crédito](finance/fiscal_localizations/mexico#credit-notes)
            * Complementos de pago
              * [Política de pago](finance/fiscal_localizations/mexico#payment-policy)
              * [Flujo de pago](finance/fiscal_localizations/mexico#payment-flow)
            * Cancelar facturas
              * [01 - Comprobante emitido con errores con relación](finance/fiscal_localizations/mexico#invoices-sent-with-errors-with-a-relation)
              * [02 - Comprobante emitido con errores sin relación](finance/fiscal_localizations/mexico#invoices-sent-with-errors-without-a-relation)
              * [Cancelaciones de pago](finance/fiscal_localizations/mexico#payment-cancellations)
            * Facturación de casos de uso especial
              * [CFDI al público](finance/fiscal_localizations/mexico#cfdi-to-public)
              * [Multidivisa](finance/fiscal_localizations/mexico#multicurrency)
              * [Anticipos](finance/fiscal_localizations/mexico#down-payments)
          * Comercio exterior
            * Configuración
              * [Contactos](finance/fiscal_localizations/mexico#id3)
              * [Productos](finance/fiscal_localizations/mexico#id4)
            * [Flujo de facturación](finance/fiscal_localizations/mexico#invoicing-flow)
          * Guía de entrega
            * Configuración
              * [Contactos y vehículos](finance/fiscal_localizations/mexico#contacts-and-vehicles)
              * [Productos](finance/fiscal_localizations/mexico#id6)
            * Flujo de ventas e inventario
              * [Materiales peligrosos](finance/fiscal_localizations/mexico#dangerous-hazards)
          * Números de pedimento
            * [Configuración](finance/fiscal_localizations/mexico#id8)
            * [Flujo de compra y ventas](finance/fiscal_localizations/mexico#purchase-and-sales-flow)
          * Contabilidad electrónica
            * [Plan de cuentas](finance/fiscal_localizations/mexico#chart-of-accounts)
            * [Balanza de comprobación](finance/fiscal_localizations/mexico#trial-balance)
            * [Libro mayor](finance/fiscal_localizations/mexico#general-ledger)
            * [Reporte DIOT](finance/fiscal_localizations/mexico#diot-report)
      * Países Bajos
        * [Exportar en XAF](finance/fiscal_localizations/netherlands#xaf-export)
        * [Reportes de contabilidad holandesa](finance/fiscal_localizations/netherlands#dutch-accounting-reports)
      * Rumania
        * [Configuración](finance/fiscal_localizations/romania#configuration)
        * Declaración D.406
          * Configuración
            * [Empresa](finance/fiscal_localizations/romania#company)
            * [Plan de cuentas](finance/fiscal_localizations/romania#chart-of-accounts)
            * [Cliente y proveedor](finance/fiscal_localizations/romania#customer-and-supplier)
            * [Impuesto](finance/fiscal_localizations/romania#tax)
            * [Producto](finance/fiscal_localizations/romania#product)
            * [Factura de proveedor](finance/fiscal_localizations/romania#vendor-bill)
          * Generar la declaración
            * [Exportar sus datos](finance/fiscal_localizations/romania#exporting-your-data)
            * [Firma del reporte](finance/fiscal_localizations/romania#signing-the-report)
      * Perú
        * [Introducción](finance/fiscal_localizations/peru#introduction)
        * Configuración
          * Instale los módulos de localización peruana
            * [Configure su empresa](finance/fiscal_localizations/peru#configure-your-company)
            * [Plan de cuentas](finance/fiscal_localizations/peru#chart-of-account)
          * Opciones de Contabilidad
            * [Conceptos básicos](finance/fiscal_localizations/peru#basic-concepts)
            * Proveedor de firma digital
              * IAP (Compras dentro de la aplicación de Konvergo ERP)
                * [¿Qué significa IAP?](finance/fiscal_localizations/peru#what-is-the-iap)
                * [¿Cómo funciona?](finance/fiscal_localizations/peru#how-does-it-work)
                * [¿Qué debe hacer?](finance/fiscal_localizations/peru#what-do-you-need-to-do)
              * [Digiflow](finance/fiscal_localizations/peru#digiflow)
              * [SUNAT](finance/fiscal_localizations/peru#sunat)
            * [Entorno de prueba](finance/fiscal_localizations/peru#testing-environment)
            * [Certificado](finance/fiscal_localizations/peru#certificate)
            * [Multidivisa](finance/fiscal_localizations/peru#multicurrency)
          * Configurar datos maestros
            * Impuestos
              * [Configuración EDI](finance/fiscal_localizations/peru#edi-configuration)
            * [Posiciones fiscales](finance/fiscal_localizations/peru#fiscal-positions)
            * [Tipos de documentos](finance/fiscal_localizations/peru#document-types)
            * Diarios contables
              * [Uso de documentos](finance/fiscal_localizations/peru#use-documents)
              * [Intercambio electrónico de datos](finance/fiscal_localizations/peru#electronic-data-interchange)
            * Contacto
              * [Tipo de identificación e IVA](finance/fiscal_localizations/peru#identification-type-and-vat)
            * [Producto](finance/fiscal_localizations/peru#product)
        * Uso y prueba
          * Factura de cliente
            * [Elementos EDI](finance/fiscal_localizations/peru#edi-elements)
            * Validación de la factura
              * [Estado de factura electrónica](finance/fiscal_localizations/peru#electronic-invoice-status)
            * [Errores comunes](finance/fiscal_localizations/peru#common-errors)
            * [Reporte de facturas en PDF](finance/fiscal_localizations/peru#invoice-pdf-report)
            * [Créditos IAP](finance/fiscal_localizations/peru#iap-credits)
            * Casos de uso especiales
              * Proceso de cancelación
                * [Estado de factura electrónica](finance/fiscal_localizations/peru#id3)
              * [Proceso de cancelación](finance/fiscal_localizations/peru#id4)
              * [Anticipos](finance/fiscal_localizations/peru#advance-payments)
              * [Facturas sujetas a detracción](finance/fiscal_localizations/peru#detraction-invoices)
          * [Notas de crédito](finance/fiscal_localizations/peru#credit-notes)
          * [Notas de débito](finance/fiscal_localizations/peru#debit-notes)
          * Guía de entrega electrónica 2.0
            * Tipos de guía de remisión
              * [Remitente](finance/fiscal_localizations/peru#sender)
              * [Transportista](finance/fiscal_localizations/peru#carrier)
            * Tipos de traslado
              * [Privado](finance/fiscal_localizations/peru#private)
              * [Público](finance/fiscal_localizations/peru#public)
            * [Envío directo a la SUNAT](finance/fiscal_localizations/peru#direct-submission-to-sunat)
            * [Información requerida](finance/fiscal_localizations/peru#required-information)
            * [Dar de baja](finance/fiscal_localizations/peru#cancellations)
            * [Prueba](finance/fiscal_localizations/peru#testing)
            * Configuración
              * [Operador](finance/fiscal_localizations/peru#operator)
              * [Transportista](finance/fiscal_localizations/peru#id6)
              * [Vehículos](finance/fiscal_localizations/peru#vehicles)
              * [Productos](finance/fiscal_localizations/peru#products)
            * [Generar una GRE](finance/fiscal_localizations/peru#generating-a-gre)
            * [Errores comunes](finance/fiscal_localizations/peru#id7)
      * Filipinas
        * Configuración
          * [Plan de cuentas e impuestos](finance/fiscal_localizations/philippines#chart-of-accounts-and-taxes)
          * [Contactos](finance/fiscal_localizations/philippines#contacts)
        * [Reporte BIR 2307](finance/fiscal_localizations/philippines#bir-2307-report)
      * Arabia Saudita
        * [Configuración](finance/fiscal_localizations/saudi_arabia#configuration)
        * Facturas electrónicas ZATCA
          * [Información de la empresa](finance/fiscal_localizations/saudi_arabia#company-information)
          * Modo de prueba
            * [Portal de simulación de Fatoora](finance/fiscal_localizations/saudi_arabia#fatoora-simulation-portal)
            * [Integración API con ZATCA](finance/fiscal_localizations/saudi_arabia#zatca-api-integration)
            * [Diarios de ventas](finance/fiscal_localizations/saudi_arabia#sales-journals)
            * [Prueba](finance/fiscal_localizations/saudi_arabia#testing)
            * [Impuestos](finance/fiscal_localizations/saudi_arabia#taxes)
          * [Modo de producción](finance/fiscal_localizations/saudi_arabia#production-mode)
      * España
        * [Plan de cuentas para España](finance/fiscal_localizations/spain#spanish-chart-of-accounts)
        * [Informes contables para España](finance/fiscal_localizations/spain#spanish-accounting-reports)
      * Suiza
        * ISR (recibo de pago con número de referencia)
          * [Referencia ISR en las facturas](finance/fiscal_localizations/switzerland#isr-reference-on-invoices)
        * [Actualización en vivo de la tasa de cambio](finance/fiscal_localizations/switzerland#currency-rate-live-update)
        * IVA actualizado para enero 2018
          * [¿Cómo actualizar sus impuestos en Konvergo ERP Enterprise (Konvergo ERP en línea o con alojamiento local)?](finance/fiscal_localizations/switzerland#how-to-update-your-taxes-in-odoo-enterprise-odoo-online-or-on-premise)
      * Tailandia
        * [Configuración](finance/fiscal_localizations/thailand#configuration)
        * [Plan de cuentas e impuestos](finance/fiscal_localizations/thailand#chart-of-accounts-and-taxes)
        * Informe de impuestos
          * [Reporte de impuestos de ventas y compra](finance/fiscal_localizations/thailand#sales-and-purchase-tax-report)
          * [Reporte de retención de impuestos PND](finance/fiscal_localizations/thailand#withholding-pnd-tax-report)
        * Factura impositiva
          * [Ajustes de la sede/número de filial](finance/fiscal_localizations/thailand#headquarter-branch-number-settings)
      * Emiratos Árabes Unidos
        * [Instalación](finance/fiscal_localizations/united_arab_emirates#installation)
        * [Plan de cuentas](finance/fiscal_localizations/united_arab_emirates#chart-of-accounts)
        * [Impuestos](finance/fiscal_localizations/united_arab_emirates#taxes)
        * [Tipos de cambio](finance/fiscal_localizations/united_arab_emirates#currency-exchange-rates)
        * Nómina
          * [Reglas salariales](finance/fiscal_localizations/united_arab_emirates#salary-rules)
          * [Provisión por terminación laboral](finance/fiscal_localizations/united_arab_emirates#end-of-service-provision)
          * [Facturas](finance/fiscal_localizations/united_arab_emirates#invoices)
      * Reino Unido
        * [Configuración](finance/fiscal_localizations/united_kingdom#configuration)
        * [Plan de cuentas](finance/fiscal_localizations/united_kingdom#chart-of-accounts)
        * Impuestos
          * Making Tax Digital (MTD)
            * [Registre su empresa ante Hacienda del Reino Unido antes de hacer su primer envío de documentos.](finance/fiscal_localizations/united_kingdom#register-your-company-to-hmrc-before-the-first-submission)
            * [Envío periodico a HMRC](finance/fiscal_localizations/united_kingdom#periodic-submission-to-hmrc)
            * [Envío periodico a HMRC para multi-empresas](finance/fiscal_localizations/united_kingdom#periodic-submission-to-hmrc-for-multi-company)

  *[EDI]: intercambio electrónico de datos

