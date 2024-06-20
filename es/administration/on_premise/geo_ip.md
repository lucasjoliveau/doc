# IP de localización

Nota

Esta documentación solo aplica a bases de datos con alojamiento local

## Instalación

Advertencia

Tenga en cuenta que la instalación depende del sistema operativo y la
distribución de su computadora. Asumiremos que utiliza Linux.

  1. Instale la biblioteca [geoip2](https://pypi.org/project/geoip2/) de Python
    
    
        pip install geoip2
    

  2. Descargue la [base de datos GeoLite2 City](https://dev.maxmind.com/geoip/geoip2/geolite2/), debe tener un archivo llamado `GeoLite2-City.mmdb`

  3. Mueva el archivo a la carpeta `/usr/share/GeoIP/`
    
    
        mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
    

  4. Reinicie el servidor

Nota

Si no puede o no desea localizar la base de datos geoip en
`/usr/share/GeoIP/`, puede utilizar la opción `-geoip-db`` de la interfaz de
línea de comandos de Odoo. Esta opción toma la ruta absoluta al archivo de
base de datos GeoIP y la usa como base de datos GeoIP. Por ejemplo:

    
    
    ./odoo-bin --geoip-db= ~/Downloads/GeoLite2-City.mmdb
    

Ver también

  * [Documentación de la CLI](../../developer/reference/cli.html)

Advertencia

También se puede utilizar la biblioteca `GeoIP` de Python. Sin embargo, esta
versión está obsoleta desde el 1 de enero. Consulte [Las bases de datos
GeoLite Legacy ya no están disponibles](https://support.maxmind.com/geolite-
legacy-discontinuation-notice/)

## Cómo probar la geolocalización GeoIP en su sitio web de Odoo

  1. Vaya a su sitio web y abra la página web en la que desea probar `GeoIP`.

  2. Seleccione Personalizar ‣ Editor HTML/CSS/JS.

  3. Agregue el siguiente fragmento de XML en la página:

    
    
    <h1 class="text-center" t-esc="request.session.get('geoip')"/>
    

Debe obtener como resultado un diccionario que indique la ubicación de la
dirección IP.

![../../_images/on-premise_geo-ip-installation01.png](../../_images/on-
premise_geo-ip-installation01.png)

Nota

Si las llaves están vacías `{}`, puede ser por cualquiera de los siguientes
motivos:

  * La dirección IP de navegación es el localhost (`127.0.0.1`) o una red de área local (`192.168.*.*`)

  * Si se utiliza un proxy inverso, asegúrese de configurarlo correctamente. Consulte [`modo proxy`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode)

  * `geoip2` no está instalada o no se encontró el archivo de base de datos GeoIP

  * La base de datos GeoIP no pudo determinar la dirección IP proporcionada

