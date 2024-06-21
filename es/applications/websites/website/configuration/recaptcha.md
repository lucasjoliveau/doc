# reCAPTCHA v3 en los formularios

reCAPTCHA de Google protege el sitio web contra el spam y ataques. Intenta
distinguir entre solicitudes de humanos y bots.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Es posible que reCAPTCHA v3 no cumpla con las regulaciones locales de protección de datos.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>reCAPTCHA v3 trabaja en segundo plano y no interrumpe a los visitantes del sitio web. Sin embargo, si el reconocimiento falla, los visitantes no podrán completar el formulario.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://developers.google.com/recaptcha/docs/v3">Guía para reCAPTCHA v3 de Google</a></p>
</div>

## Configuración

### En Google

Ingrese a la [página web de registro de
reCAPTCHA](https://www.google.com/recaptcha/admin/create). Inicie sesión o
cree una cuenta de Google si es necesario.

En la página web de registro:

  * Póngale una **Etiqueta** al sitio web.

  * Deje el **tipo de reCAPTCHA** en **Score based (v3)**.

  * Introduzca uno o mas **Dominios** (por ejemplo, _example.com_ or _subdomain.example.com_).

  * En **Plataforma Google Cloud** , se seleccionará automáticamente un proyecto si ya se creó uno con la cuenta con la que inició sesión en Google. Si no es así, se creará uno automáticamente. Haga clic en **Plataforma Google Cloud** para que usted mismo pueda seleccionar un proyecto o para cambiar el nombre del poryecto que se creó de manera automática.

  * Acepte los términos y condiciones de servicio.

  * Haga clic en **Enviar**.

![Ejemplo del sitio web de registro de reCAPTCHA.
](../../../../_images/recaptcha-google-configuration.png)

Aparecerá una nueva página con las claves generadas. Déjela abierta para más
tarde, pues necesitará copiar las claves en Konvergo ERP después.

### En Konvergo ERP

  * Desde el tablero de la base de datos, haga clic en **Ajustes**. Si es necesario, active la opción **reCAPTCHA** en la sección de **Integraciones**.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>No desactive la función <b>reCAPTCHA</b> ni desinstale el módulo <b>integración de Google reCAPTCHA</b>, pues es posible que se eliminen otros módulos.</p>
</div>

  * Abra la página de Google reCAPTCHA, copie la **Clave del sitio** y péguela en el campo **Clave del sitio** en Konvergo ERP.

  * Abra la página de Google reCAPTCHA, copie la **Clave secreta** y péguela en el campo **Clave secreta** en Konvergo ERP.

  * Cambie el **Puntaje mínimo requerido** (`0.5`) predeterminado si es necesario, usando un valor entre `1.0` y `0.0`. Entre más alto sea el umbral, más difícil será aprobar el reCAPTCHA y viceversa.

  * Haga clic en **Guardar**.

Todas las páginas que utilicen los snippets **Formulario** , **Bloque de
boletín** , **Ventana emergente del boletín** y el formulario **Pasos
adicionales durante la finalización de la compra** en el comercio electrónico,
estarán protegidos con reCAPTCHA.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>Si el reconocimiento falla, aparecerá el siguiente mensaje de error:</p>
<img alt="Mensaje de error en la verificación de Google reCAPTCHA. " src="../../../../_images/recaptcha-error.png"/>
</li>
<li><p>reCAPTCHA v3 es gratuito hasta <a href="https://developers.google.com/recaptcha/docs/faq#are-there-any-qps-or-daily-limits-on-my-use-of-recaptcha">1 millón de valoraciones al mes</a>.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Truco</p><ul>
<li><p>La analítica y otros ajustes adicionales están disponibles en la <a href="https://www.google.com/recaptcha/admin/">página de administración de Google reCAPTCHA</a>. Por ejemplo, puede recibir alertas por correo electrónico si Google detecta tráfico sospechoso en su sitio web o puede ver el porcentaje de solicitudes sospechosas, lo que puede ayudarle a determinar el puntaje mínimo adecuado.</p></li>
<li><p>Puede notificar a los visitantes que reCAPTCHA  proteje un formulario. Para hacerlo, abra el editor del sitio web y vaya al formulario. Luego, haga clic en cualquier parte del formulario y en la pestaña <b>Personalizar</b> que se encuentra del lado derecho de la barra, conmute <b>Mostrar política de reCAPTCHA</b> que está en la sección de <b>Formulario</b>.</p></li>
</ul>
<img alt="Mensaje de política de reCAPTCHA que aparece en el formulario" src="../../../../_images/recaptcha-policy.png"/>
</div>

