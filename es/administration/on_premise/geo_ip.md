# IP de localización

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Esta documentación solo aplica a bases de datos con alojamiento local</p>
</div>

## Instalación

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Tenga en cuenta que la instalación depende del sistema operativo y la distribución de su computadora. Asumiremos que utiliza Linux.</p>
</div>

  1. Instale la biblioteca [geoip2](https://pypi.org/project/geoip2/) de Python
    
    
        pip install geoip2
    

  2. Descargue la [base de datos GeoLite2 City](https://dev.maxmind.com/geoip/geoip2/geolite2/), debe tener un archivo llamado `GeoLite2-City.mmdb`

  3. Mueva el archivo a la carpeta `/usr/share/GeoIP/`
    
    
        mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
    

  4. Reinicie el servidor

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no puede o no desea localizar la base de datos geoip en <code>/usr/share/GeoIP/</code>, puede utilizar la opción <code>-geoip-db`</code> de la interfaz de línea de comandos de Konvergo ERP. Esta opción toma la ruta absoluta al archivo de base de datos GeoIP y la usa como base de datos GeoIP. Por ejemplo:</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>./odoo-bin --geoip-db<span class="o">=</span> ~/Downloads/GeoLite2-City.mmdb
</pre></div>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><ul>
<li><p><a href="../../developer/reference/cli">Documentación de la CLI</a></p></li>
</ul>
</div>
</div> <div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>También se puede utilizar la biblioteca <code>GeoIP</code> de Python. Sin embargo, esta versión está obsoleta desde el 1 de enero.    Consulte <a href="https://support.maxmind.com/geolite-legacy-discontinuation-notice/">Las bases de datos GeoLite Legacy ya no están disponibles</a></p>
</div>

## Cómo probar la geolocalización GeoIP en su sitio web de Konvergo ERP

  1. Vaya a su sitio web y abra la página web en la que desea probar `GeoIP`.

  2. Seleccione Personalizar ‣ Editor HTML/CSS/JS.

  3. Agregue el siguiente fragmento de XML en la página:

    
    
    <h1 class="text-center" t-esc="request.session.get('geoip')"/>
    

Debe obtener como resultado un diccionario que indique la ubicación de la
dirección IP.

![../../_images/on-premise_geo-ip-installation01.png](../../_images/on-
premise_geo-ip-installation01.png) <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si las llaves están vacías <code>{}</code>, puede ser por cualquiera de los siguientes motivos:</p>
<ul>
<li><p>La dirección IP de navegación es el localhost (<code>127.0.0.1</code>) o una red de área local (<code>192.168.*.*</code>)</p></li>
<li><p>Si se utiliza un proxy inverso, asegúrese de configurarlo correctamente. Consulte <a href="../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode"><code>modo proxy</code></a></p></li>
<li><p><code>geoip2</code> no está instalada o no se encontró el archivo de base de datos GeoIP</p></li>
<li><p>La base de datos GeoIP no pudo determinar la dirección IP proporcionada</p></li>
</ul>
</div>

