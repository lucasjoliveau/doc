# Imágenes para productos con Google Imágenes

Que los productos en Konvergo ERP cuenten con las imágenes apropiadas es útil por
varios motivos. Sin embargo, asignar imágenes a varios productos puede tomar
mucho tiempo.

Afortunadamente, si configura la API de _Google Custom Search_ dentro de una
base de datos de Konvergo ERP podrá encontrar imágenes para los productos con mucha
facilidad gracias a sus códigos de barras.

## Configuración

Para poder usar _Google Custom Search_ en una base de datos deberá configurar
de forma adecuada su base y la API de Google.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las cuentas gratuitas de Google permiten que los usuarios seleccionen hasta 100 imágenes gratuitas al día. En caso de que necesiten más, entonces deben usar la versión de pago.</p>
</div>

### Tablero de la API de Google

  1. Vaya a la página [APIs y servicios de Google Cloud Platform](https://console.developers.google.com/) para generar las credenciales API de Google Custom Search. Inicie sesión con una cuenta de Google y acepte los **Términos del Servicio** , para esto seleccione la casilla y haga clic en **Aceptar y continuar**.

  2. Una vez aquí, seleccione o cree un proyecto de API para almacenar las credenciales. Primero proporcione un **nombre de proyecto** fácil de recordar, seleccione una **ubicación** (si la hay) y luego haga clic en **Crear**.

  3. Una vez que la opción **Credenciales** en la barra lateral izquierda esté seleccionada haga clic en **Crear credenciales** y elija **Clave API** en el menú desplegable.

![Página de APIs y servicios en Google Cloud
Platform.](../../../../../_images/credentials-api-key.png)

  4. Aparecerá una ventana emergente con el mensaje **Clave API creada** con una **clave API** personalizada. Copie y guarde **su clave API** , la utilizará después. Una vez que haya copiado la clave (y la haya almacenado para su uso posterior), haga clic en el botón **Cerrar** de la ventana emergente.

![Visualización de la ventana emergente con la clave API recién
creada.](../../../../../_images/api-key-pop-up.png)

  5. En esta página, busque `Custom Search API` y selecciónela.

![Barra de búsqueda con la "Custom Search API" en Google Cloud
Platform.](../../../../../_images/custom-search-api-search-bar.png)

  6. Una vez que se encuentre en la página de **Custom Search API** haga clic en **Habilitar**.

![La página de "Custom Search API" con el botón Habilitar resaltado en Google
Cloud Platform.](../../../../../_images/gcp-custom-search-api-page.png)

### Tablero de Google Programmable Search

  1. A continuación, vaya al [Motor de Búsqueda Programable de Google](https://programmablesearchengine.google.com/) (no está disponible en español) y haga clic en alguno de los botones **Get started** (es decir, comenzar). Si aún no ha iniciado sesión, entonces inicie sesión con una cuenta de Google.

![Página del motor de búsqueda programable de Google con los botones "Get
started" \(Comenzar\).](../../../../../_images/google-pse-get-started.png)

  2. En el formulario **Create a new search engine (Crear un nuevo motor de búsqueda)** , complete el nombre del motor de búsqueda junto con lo que debería buscar. Asegúrese de habilitar **Image Search** y **SafeSearch**.

![El formulario para crear un nuevo motor de búsqueda que aparece al
configurar el motor de búsqueda.](../../../../../_images/create-new-
search.png)

  3. Haga clic en **Crear** para validar el formulario.

  4. Después de esto aparecerá una nueva página con el texto «**Your new search engine has been created** » (Su nuevo motor de búsqueda ha sido creado).

![La página con el mensaje "Su nuevo motor de búsqueda ha sido creado" con el
código a copiar.](../../../../../_images/new-search-engine-has-been-
created.png)

  5. Desde esta página, haga clic en **Personalizar** para abrir la página Información general ‣ Básico. Luego copie el ID del campo **ID del motor de búsqueda** , es necesario para realizar la configuración en Konvergo ERP.

![Página de información general con el campo ID del motor de
búsqueda.](../../../../../_images/basic-overview-search-engine-id.png)

### Konvergo ERP

  1. En la base de datos de Konvergo ERP, vaya a la aplicación Ajustes y diríjase a la sección **Integraciones**. Una vez allí, seleccione la casilla junto a **Google Imágenes** y después haga clic en **Guardar**.

![La función Google Imágenes en la página de la aplicación Ajustes de
Konvergo ERP.](../../../../../_images/google-images-setting.png)

  2. Regrese a la aplicación Ajustes y, de nuevo, diríjase a la sección **Integraciones**. En la sección **Google Imágenes** deberá completar los campos **Clave API** así como también **ID de motor de búsqueda**.

  3. Haga clic en **Guardar**.

## Imágenes de producto en Konvergo ERP con la API de Google Custom Search

Puede agregar imágenes a los productos en Konvergo ERP en cualquier producto o sus
variantes. Este proceso se puede realizar en cualquier aplicación de Konvergo ERP que
proporcione acceso a las páginas de productos, por ejemplo, _Ventas_ ,
_Inventario_ , entre otras.

A continuación encontrará una guía con todas las instrucciones sobre el uso de
la _API de Google Custom Search_ para asignar imágenes a productos desde la
aplicación _Ventas_ de Konvergo ERP:

  1. Desde la aplicación _Ventas_ vaya a la página **Productos** (aplicación Ventas ‣ Productos ‣ Productos) o a la página **Variantes de producto** (aplicación Ventas ‣ Productos ‣ Variantes de producto).

  2. Seleccione el producto que necesita una imagen.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo se procesarán los productos (o las variantes) que tienen un código de barras, pero <b>no</b> tienen una imagen asignada.</p>
<p>Si selecciona un producto con una o más variantes, se procesa cada variante que coincida con los criterios correspondientes.</p>
</div>

  3. Haga clic en el icono **Acción ⚙️ (engranaje)** ubicado en la página del producto y, en el menú que aparece, seleccione **Obtener imágenes de Google Imágenes**.

![La opción "Obtener imágenes de Google Imágenes" del menú desplegable de
acción en Konvergo ERP.](../../../../../_images/get-pictures-from-google-action.png)

  4. Aparecerá una ventana emergente, allí haga clic en **Obtener imágenes**.

![La ventana emergente en la aplicación Ventas de Konvergo ERP que aparece en la que
el usuario deberá hacer clic en "Obtener
imágenes".](../../../../../_images/click-get-picture-from-pop-up.png)

  5. Una vez que haga clic, las imágenes irán apareciendo.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Solo las primeras diez imágenes se obtienen de inmediato. Si seleccionó más, se irán obteniendo en segundo plano.</p>
<p>El trabajo en segundo plano procesa alrededor de 100 imágenes por minuto. Si alcanza la cuota autorizada por Google (ya sea con un plan gratuito o de pago), el trabajo en segundo plano se pausará durante 24 horas y después continuará donde se detuvo el día anterior.</p>
</div>

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p><a href="https://cloud.google.com/billing/docs/how-to/manage-billing-account">Cree, modifique o cierre su cuenta de facturación de Google Cloud</a></p>
</div>

