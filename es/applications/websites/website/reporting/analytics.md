# Analítica

La analítica del sitio web le ayuda a los propietarios a monitorear de qué
forma los visitantes usan su sitio. También proporciona datos acerca del
sector demográfico, comportamiento e interacciones de los visitantes, lo que
ayuda a mejorar los sitios web y las estrategias de marketing.

Puede monitorear el tráfico de su sitio web de Konvergo ERP con Plausible.io o
analytics/GA. Le recomendamos que use Plausible.io, pues es fácil de usar,
protege su privacidad y es ligero.

El tablero analítico de Plausible también está integrado con Konvergo ERP y puede
acceder a él desde Sitio web ‣ Reportes ‣ Analítica.

## Plausible.io

Konvergo ERP aloja su propio servidor de Plausible.io y proporciona una solución
gratuita lista para funcionar en las bases de datos de **Konvergo ERP en línea**. De
manera automática, Konvergo ERP crea y configura su cuenta. Para comenzar a usarlo,
vaya a Sitio web ‣ Reportes ‣ Analítica.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p><b>Si ya tiene una cuenta de Plausible.io</b> y desea conectarla a su base de datos de Konvergo ERP en línea, debe crear dos <code>ir.config.parameters</code> para usar los servidores de Plausible.io. Para hacerlo, active el <a href="../../../general/developer_mode#developer-mode"><span class="std std-ref">modo de desarrollador</span></a> y vaya a Ajustes generales ‣ Ajustes técnicos – Parámetros del sistema. Haga clic en <b>Nuevo</b> y complete los campos <b>Clave</b> y <b>Valor</b>:</p>
<table class="table docutils">
<colgroup>
<col style="width: 50%"/>
<col style="width: 50%"/>
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Clave</p></th>
<th class="head"><p>Valor</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code>website.plausible_script</code></p></td>
<td><p><code>https://plausible.io/js/plausible.js</code></p></td>
</tr>
<tr class="row-odd"><td><p><code>website.plausible_server</code></p></td>
<td><p><code>https://plausible.io</code></p></td>
</tr>
</tbody>
</table>
<p>Luego, siga los pasos de a continuación para conectar su cuenta existente con los servidores de Plausible.io.</p>
</div>

Si su base de datos está alojada en **Konvergo ERP.sh** o de manera **local** , o si
desea usar su propia cuenta de Plausible.io, siga los pasos a continuación:

  1. Cree o inicie sesión en una cuenta de Plausible usando el siguiente enlace: <https://plausible.io/register>.

  2. Si va a crear una nueva cuenta, siga los pasos de registro y activación de su cuenta. Cuando le pida los detalles de su sitio web, agregue su **Dominio** sin incluir `www` (por ejemplo, `ejemplo.odoo.com`) y, si es necesario, cambie la **Zona horaria del reporte**. Haga clic en **Agregar snippet** para seguir con el siguiente paso. Haga caso omiso de las instrucciones de the **Agregar snippet de JavaScript** y haga clic en **Empezar a recolectar datos**.

  3. Haga clic en el logotipo de Plausible ubicado en la parte superior izquierda de la página para acceder a su [lista de sitios web](https://plausible.io/sites) y luego haga clic en el icono de engranaje que está junto al sitio web.

![Haga clic en el icono de engranaje en la lista de sitios web.
](../../../../_images/plausible-gear-icon.png)

  4. En la barra lateral, seleccione **Visibilidad** , y luego haga clic en **\+ Nuevo enlace**.

  5. Escriba un **Nombre** , deje el campo de **Contraseña** vacío, pues no es compatible con la integración del tablero de la analítica de Plausible con Konvergo ERP. Luego haga clic en **Crear enlace compartido**.

![Creación de credenciales para el nuevo enlace
compartido](../../../../_images/plausible-create-sharedlink.png)

  6. Copie el enlace compartido.

![Copiar el URL del enlace compartido de
Plausible.io](../../../../_images/plausible-copy-sharedlink.png)

  7. En Konvergo ERP, vaya a Sitio web ‣ Configuración ‣ Ajustes.

  8. En la sección **SEO** , active **Plausible Analytics** , y luego pegue el **Enlace compartido** y haga clic en **Guardar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si tiene <a href="../configuration/multi_website">varios sitios web</a>, agregue sus sitios web a su cuenta de Plausible.io en <a href="https://plausible.io/sites">https://plausible.io/sites</a> y haciendo clic en <b>+ Agregar sitio web</b>. En Konvergo ERP, en los <b>ajustes de Sitio web</b>, asegúrese de seleccionar el sitio web en el campo <b>Ajustes del sitio web</b> antes de pegar el <b>Enlace compartido</b>.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Konvergo ERP dará prioridad automáticamente a dos objetivos personalizados:  <code>Generar Leads</code> y <code>Tienda</code>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://plausible.io/docs">Documentación de Plausible Analytics</a></p>
</div>

## Google Analytics

Para llevar el seguimiento del tráfico del sitio web de Konvergo ERP con Google
Analytics:

  1. Cree o inicie sesión en su cuenta de Google usando el siguiente enlace: <https://analytics.google.com>.

  2.      * Si está configurando Google Analytics por primera vez, haga clic en **Empezar a medir** y siga los pasos para crear la cuenta.

     * Si ya tiene una cuenta de Google Analytics, inicie sesión y haga clic en el icono de engranaje en la esquina inferior izquiera de la página para acceder a la página de **Admin**. Luego, haga clic en **\+ Crear propiedad**.

![Medición del ID en Google Analytics.](../../../../_images/GA-add-
property.png)

  3. Siga los siguientes pasos: [creación de propiedad](https://support.google.com/analytics/answer/9304153?hl=en/&visit_id=638278591144564289-3612494643&rd=2#property), detalles del negocio y objetivos.

  4. Cuando llegue al paso de **Recolección de datos** , elija la plataforma **Web**.

![Elija una plataforma para la propiedad de su Google
Analytics.](../../../../_images/GA-platform.png)

  5. Configure el flujo de sus datos: Especifique la **URL del sitio web** y un **Nombre del flujo**. Luego haga clic en **Crear flujo**.

  6. Copie el **ID de medición**.

![Medición del ID en Google Analytics.](../../../../_images/GA-measurement-
id.png)

  7. En Konvergo ERP, vaya a Sitio web ‣ Configuración ‣ Ajustes.

  8. En la sección **SEO** , active **Google Analytics** , luego pegue el **ID de medición** y haga clic en **Guardar**.

<div class="alert alert-info">
<p class="alert-title">
Truco</p><p>Si cuenta con  <a href="../configuration/multi_website">varios sitios web</a> con dominios separados, se le recomienda crear  <a href="https://support.google.com/analytics/answer/9304153?hl=en/&amp;visit_id=638278591144564289-3612494643&amp;rd=2#property">una propiedad</a> por dominio. En Konvergo ERP, en los <b>ajustes de Sitio web</b>, asegúrese de seleccionar el sitio web en el campo <b>Ajustes del sitio web</b> antes de pegar el <b>ID de medición</b>.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://support.google.com/analytics/answer/1008015?hl=en/">Documentación de Google para configurar Analytics para un sitio web</a></p>
</div>

## Google Tag Manager

GTM es un sistema de gestión de etiquetas que le permite actualizar con
facilidad códigos de medición y fragmentos de código relacionados (a los que
se les conoce de forma colectiva como etiquetas) en su sitio web o aplicación
móvil mediante el inyector de código.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Es posible que Google Tag Manager no cumpla con las regulaciones locales de protección de datos.</p>
</div>

Consulte los siguientes pasos para usar GTM:

  1. Vaya a <https://tagmanager.google.com/> para crear o iniciar sesión en una cuenta de Google.

  2. En la pestaña **Cuentas** , haga clic en **Crear cuenta**.

  3. Escriba el **nombre de cuenta** y seleccione el **país** correspondiente.

  4. Escriba la URL de su sitio web en el campo **Nombre de contenedor** y seleccione la **plataforma objetivo**.

  5. Haga clic en **Crear** y acepte las condiciones del servicio.

  6. Copie los códigos `<head>` y `<body>` de la ventana emergente. Después, vaya a su sitio web, haga clic en **Editar** y diríjase a la pestaña **Temas** , busque la sección **Ajustes del sitio web** y haga clic en **< head>** and **< /body>** para pegarlos según corresponda.

![Instalar Google Tag Manager](../../../../_images/gtm-codes.png)

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Los datos se recopilan de las herramientas de marketing utilizadas para monitorear el sitio web (por ejemplo, Google Analytics, Plausible, Facebook Pixel), no de Konvergo ERP.</p>
</div>

  *[GTM]: Google Tag Manager

