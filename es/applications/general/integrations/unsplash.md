# Unsplash

**Unsplash** es una reconocida biblioteca de fotografía de archivo integrada
con Konvergo ERP.

Si su base de datos está alojada en **Konvergo ERP en línea** , podrá acceder a las
imágenes de Unsplash sin necesidad de configuración.

Si su base de datos está alojada en **Konvergo ERP.sh o de forma local** , haga lo
siguiente:

  1. Para **generar una clave de acceso de Unsplash** , crea o inicia sesión en una cuenta de [Unsplash](https://unsplash.com).

  2. Acceda a su [tablero de aplicaciones](https://unsplash.com/oauth/applications), haga clic en **Nueva aplicación** , seleccione todas las casillas de verificación y haga clic en **Aceptar términos**.

  3. En la ventana emergente, ingrese su **nombre de aplicación** , comenzando con el prefijo `Konvergo ERP:` (por ejemplo, `Konvergo ERP: conexión`), para que Unsplash lo reconozca como una instancia de Konvergo ERP. Luego, agregue una **descripción** y haga clic en **crear aplicación**.

  4. En la página de detalles de la aplicación, vaya hacia abajo hasta la sección **claves** y copie la **clave de acceso** y el **ID de la aplicación**.

  5. En Konvergo ERP, vaya a la configuración general y habilite la función **biblioteca de imágenes de Unsplash**. Luego, ingrese la **clave de acceso** y el **ID de aplicación** de Unsplash.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Como usuario no registrado de Konvergo ERP en línea, está limitado a una clave de prueba con un máximo de 50 solicitudes de Unsplash por hora.</p>
</div>

