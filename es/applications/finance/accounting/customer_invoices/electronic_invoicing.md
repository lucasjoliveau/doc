# Facturación electrónica (EDI)

EDI, o intercambio electrónico de datos, es la comunicación entre empresas de
documentos empresariales, como órdenes de compra y facturas, en formato
estándar. Si envía documentos que cumplen con el estándar EDI se podrá
asegurar de que la máquina que reciba el mensaje podrá interpretar la
información de manera correcta. Hay muchos formatos EDI que están disponibles
dependiendo del país de su empresa.

La función EDI permite automatizar la administración entre empresas, además de
que es posible que algunos gobiernos lo pidan para facilitar el control fiscal
y la administración

Uno de los usos de EDI es que podrá crear facturas y notas de crédito en
formato electrónico.

Los siguientes formatos, entre otros, son compatibles con Konvergo ERP.

Nombre de Formato | Aplicación  
---|---  
Factur-X (PDF/A-3) | Para las empresas de Francia y Alemania  
Peppol BIS Billing 3.0 (UBL) | Para empresas que están en países que están dentro de [la lista EAS](https://docs.peppol.eu/poacc/billing/3.0/codelist/eas/)  
E-FFF | Para empresas de Bélgica  
XRechnung (UBL) | Para las empresas de Alemania  
Fattura PA (IT) | Para las empresas de Italia  
CFDI (4.0) | Para las empresas de México  
Perú UBL 2.1 | Para las empresas de Perú  
SII IVA Llevanza de libros registro (ES) | Para las empresas de España  
UBL 2.1 (Colombia) | Para las empresas de Colombia  
Autoridad fiscal de Egipto | Para empresas egipcias  
E-Invoice (IN) | Para las empresas de India  
NLCIUS (Países Bajos) | Para empresas neerlandesas  
EHF 3.0 | Para empresas noruegas  
Facturación SG BIS 3.0 | Para empresas singapurenses  
A-NZ BIS Billing 3.0 | Para empresas australianas o neozelandesas  
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Paquetes de localización fiscal</span></a></p>
</div>

## Configuración

Vaya a Contabilidad ‣ Configuración ‣ Diarios ‣ Facturas del cliente ‣ Ajustes
avanzados ‣ Facturación electrónica y active los formatos que necesita para
este diario.

![Seleccione el formato EDI que necesita](../../../../_images/formats.png)

Después de que active el formato de facturación electrónica, se generarán los
documentos XML cuando haga clic en el botón **Confirmar** que está en los
documentos como facturas, notas de crédito, etc. Podrá encontrar estos
documentos en la sección de archivos adjuntos o incrustados en el PDF.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Para el formato E-FFF, el archivo xml aparece solo después de generar el PDF (con el botón <b>Imprimir</b> o <b>Enviar e imprimir</b>), ya que el PDF necesita estar insertado en el xml.</p></li>
<li><p>Todo PDF generado desde Konvergo ERP contiene un archivo XML <b>Factur-X</b> (por motivos de interoperabilidad). Para empresas alemanas y francesas, la opción <b>Factur-X (PDF/A-3)</b> también activa las revisiones de validación en la factura y genera un archivo PDF/A-3. Este archivo es necesario para plataformas como Chorus Pro.</p></li>
<li><p>Los formatos disponibles dependen del país que está registrado en la <b>Información general</b> de la empresa.</p></li>
<li><p>Konvergo ERP es compatible con el formato <b>Peppol BIS Billing 3.0</b>  que se puede usar a través de puntos de acceso existentes.</p></li>
</ul>
</div>

  *[EDI]: intercambio electrónico de datos

