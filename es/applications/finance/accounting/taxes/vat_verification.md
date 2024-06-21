# Comprobar un número de IVA (sistema VIES)

**Sistema de intercambio de información sobre el IVA** (**VIES** , por sus
siglas en inglés): es una herramienta facilitada por la Comisión Europea que
le permite comprobar la validez de los números de IVA de las empresas
registradas en la Unión Europea.

Konvergo ERP cuenta con una función para **comprobar números de IVA** cada vez que se
guarda un contacto. Esto le ayuda a asegurarse de que sus contactos le
proporcionaron un número de IVA válido sin salir de la interfaz de Konvergo ERP.

## Configuración

Para activar esta función, vaya a Contabilidad ‣ Configuración ‣ Ajustes ‣
Impuestos, active la función **comprobar números de IVA** y haga clic en
_guardar_.

![Habilitar *verificar números de IVA" en la aplicación Contabilidad de
Konvergo ERP](../../../../_images/vat-validation-configuration.png)

## Comprobar número de IVA

Cada vez que cree o modifique un contacto, asegúrese de completar los campos
**país** e **IVA**.

![Complete el formulario de contacto con el país y el número de IVA antes de
hacer clic en *guardar*.](../../../../_images/vat-validation-contact-form.png)

Al hacer clic en _guardar_ , Konvergo ERP confirma el número de IVA por VIES, y
muestra un mensaje de error si el número de IVA no es válido.

![Cuando el número de IVA no es válido, Konvergo ERP muestra un mensaje de error en
lugar de guardar](../../../../_images/vat-validation-error.png)
<div class="alert alert-warning">
<p class="alert-title">
Importante</p><p>Esta herramienta verifica la validez del número de IVA pero no comprueba la validez de los demás campos.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="https://ec.europa.eu/taxation_customs/vies/vatRequest">Comisión Europea: sistema de búsqueda VIES</a></p></li>
</ul>
</div>

