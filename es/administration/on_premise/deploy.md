# Configuración del sistema

Este documento describe los pasos básicos para configurar Konvergo ERP en producción o
en un servidor de internet, sigue la [instalación](../on_premise) y por
lo general no es necesario para un sistema de desarrollo que no está expuesto
a internet.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Si está configurando un servidor público, asegúrese de consultar nuestras recomendaciones de <a href="#security"><span class="std std-ref">Seguridad</span></a>.</p>
</div>

## dbfilter

Konvergo ERP es un sistema de tenencia múltiple. Es posible que un solo sistema de
Konvergo ERP ejecute y preste servicios a varias instancias de la base de datos,
también puede tener varias personalizaciones (por ejemplo, cómo se cargan los
módulos) dependiendo de la base de datos actual.

Esto no representa un problema al trabajar en el backend (cliente web) como un
usuario de la empresa que inició sesión: puede seleccionar la base de datos al
iniciar sesión y las personalizaciones se cargan después.

Sin embargo, esto sí es un problema para los usuarios que no iniciaron sesión
(portal, sitio web) y no están vinculados a la base de datos. Konvergo ERP necesita
saber qué base de datos se debería usar para cargar la página de sitio web o
realizar la operación. No habrá ningún problema si no usa la tenencia
múltiple, pues solo hay una base de datos para usar, pero si hay varias bases
de datos a las que se pueden acceder, Konvergo ERP necesita una regla para saber cuál
debe usar.

Ese es uno de los propósitos de [`--db-
filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter),
especificar cuál es la base de datos que se debe seleccionar según el nombre
de host (dominio) que se solicita. El valor es una [expresión
regular](https://docs.python.org/3/library/re) que tal vez puede incluir
el nombre de host con inyección dinámica (`%h`) o el primer subdominio (`%d`)
mediante el cual se accede al sistema.

Para servidores que alojan varias bases de datos en producción, sobre todo si
usan `sitio web`, el dbfilter **debe** estar configurado. De lo contrario,
varias funciones no trabajarán de forma adecuada.

### Ejemplos de configuración

  * Para mostrar solo las bases de datos con nombres que empiecen con “mycompany”

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli#reference-cmdline-config-
file):

    
    
    [options]
    dbfilter = ^mycompany.*$
    

  * Para mostrar solo las bases de datos que coinciden con el primer subdominio después de `www`. Por ejemplo, la base de datos «mycompany» aparecerá si la solicitud entrante se envió a `www.mycompany.com` o a `mycompany.co.uk`, pero no para `www2.mycompany.com` o `helpdesk.mycompany.com`.

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli#reference-cmdline-config-
file):

    
    
    [options]
    dbfilter = ^%d$
    

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>

## PostgreSQL

De forma predeterminada, PostgreSQL solo permite conexiones mediante sockets
UNIX y bucles de retorno (también conocidas como loopback) que ocurren desde
«localhost», en la misma máquina en la que está instalada el servidor
PostgreSQL.

El socket UNIX es suficiente si desea que Konvergo ERP y PostgreSQL se ejecuten en la
misma máquina y es la opción predeterminada cuando no se proporciona
alojamiento, pero si desea que Konvergo ERP y PostgreSQL se ejecuten en distintas
máquinas 1 necesitará [escuchar las interfaces de
red](https://www.postgresql.org/docs/12/static/runtime-config-connection)
2. Para esto:

  * Solo acepte conexiones de bucle de retorno y [use un túnel SSH](https://www.postgresql.org/docs/12/static/ssh-tunnels) entre la máquina en la que se ejecuta Konvergo ERP se ejecutar y en la que se ejecuta PostgreSQL. Después configure Konvergo ERP para que se vincule a su extremo del túnel.

  * Acepte conexiones a la máquina en la que Konvergo ERP está instalado, es probable que sea mediante SSL (consulte los [ajustes de conexión con PostgreSQL](https://www.postgresql.org/docs/12/static/runtime-config-connection) para obtener más detalles), luego configure Konvergo ERP para conectarse a través de la red.

### Ejemplo de configuración

  * Permita la conexión tcp en localhost.

  * Permita la conexión tcp desde la red 192.168.1.x.

En `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/pg_hba.conf` establezca:

    
    
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    host    all             all             192.168.1.0/24          md5
    

En `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/postgresql.conf`
establezca:

    
    
    listen_addresses = 'localhost,192.168.1.2'
    port = 5432
    max_connections = 80
    

### Configurar Konvergo ERP

Konvergo ERP se conecta a un servidor PostgreSQL local mediante un socket UNIX a
través del puerto 5432 de forma predeterminada. Puede anular esto si usa [las
opciones de la base de datos](../../developer/reference/cli#reference-
cmdline-server-database) cuando el despliegue de PostgreSQL no es local o no
usa la configuración de instalación predeterminada.

Los [paquetes de instalación](packages) crearán un nuevo usuario (`odoo`)
de manera automática y se establecerá como el usuario de la base de datos.

  * Las pantallas de gestión de las bases de datos están protegidas por la configuración `admin_passwd`. Esta configuración solo se puede establecer mediante archivos de configuración y solo se revisa antes de realizar alteraciones a la base de datos. Debe estar configurado en un valor generado de forma aleatoria para garantizar que cualquier fuente externa no pueda utilizar esta interfaz.

  * Todas las operaciones de la base de datos usan las [opciones de base de datos](../../developer/reference/cli#reference-cmdline-server-database), entre ellas, la pantalla de gestión de las bases de datos. Para que esta pantalla funcione, el usuario de PostgreSQL necesita tener el permiso `createdb`.

  * Los usuarios siempre pueden abandonar las bases de datos que les pertenecen. Para que la pantalla de gestión de la base de datos deje de ser funcional, el usuario de PostgreSQL debe crearse con `no-createdb` y otro de los usuarios debe ser propietario de la base de datos.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>El usuario de PostgreSQL <b>no debe</b> ser un superusuario.</p>
</div>

#### Ejemplo de configuración

  * Conéctese a un servidor PostgreSQL en 192.168.1.2.

  * Puerto 5432.

  * Use la cuenta con el usuario «odoo».

  * Use «pwd» como contraseña.

  * Filtre solo las bases de datos con nombres que empiecen con «mycompany».

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli#reference-cmdline-config-
file):

    
    
    [options]
    admin_passwd = mysupersecretpassword
    db_host = 192.168.1.2
    db_port = 5432
    db_user = odoo
    db_password = pwd
    dbfilter = ^mycompany.*$
    

### SSL entre Konvergo ERP y PostgreSQL

Desde Konvergo ERP 11.0 puede hacer uso de la conexión SSL entre Konvergo ERP y PostgreSQL. En
Konvergo ERP, `db_sslmode` controla la seguridad SSL de la conexión con un valor que
puede ser “disable”, “allow”, “prefer”, “require”, “verify-ca” o “verify-
full”.

[Documentación de PostgreSQL](https://www.postgresql.org/docs/12/static/libpq-
ssl)

## Servidor incorporado

Konvergo ERP incluye servidores integrados HTTP, cron y de chat en vivo. Estos usan
multiprocesos o multihilos.

El servidor **multihilos** es un servidor más simple que por lo general se usa
para desarrollos y demostraciones, además de que se usa debido a su
compatibilidad con varios sistemas operativos (como Windows). Por cada nueva
solicitud HTTP se genera un nuevo hilo, incluso para las conexiones
persistentes como websocket, también se generan hilos de cron daemonic
adicionales. Sin embargo, por su limitación con Python (GIL), no aprovecha muy
bien el hardware.

El servidor predeterminado es el multihilos, también en los contenedores de
docker. Se selecciona al no elegir la opción
[`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-workers) o
estableciéndola en `0`.

El servidor **multiprocesos** es un servidor avanzado que se usa para
producción. No esta sujeto a la misma limitación de Python (GIL) en cuanto al
uso de recursos, así que aprovecha mucho mejor el hardware. Al momento de
poner en marcha un servidor se crea un conjunto de workers y el sistema
operativo pone en cola las nuevas solicitudes HTTP hasta que haya workers
listos para procesarlas. Los eventos del chat en vivo generan otro worker HTTP
en un puerto alternativo. También se generan workers cron adicionales. Un
proceso reaper configurable monitorea el uso y puede detener o reiniciar
workers con errores.

El servidor multiprocesos es opcional. Lo puede seleccionar al establecer la
opción [`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-
workers) como non-null integer.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>El servidor multiprocesos está personalizado para servidores de Linux, así que no está disponible para Windows.</p>
</div>

### Cálculo del número de workers

  * Regla general: (#CPU * 2) + 1

  * Los workers del cron necesitan CPU.

  * 1 worker ~= 6 usuarios concurrentes.

### Cálculo del tamaño de la memoria

  * Consideramos que el 20% de las solicitudes son serias, mientras que el 80% son más simples.

  * Se estima que un worker pesado consume alrededor de 1 GB de RAM una vez que todos los campos calculados y las peticiones SQL están bien diseñadas, etc.

  * Se estima que un worker ligero en el mismo escenario consume alrededor de 150 MB de RAM.

RAM necesaria = #worker * ( (light_worker_ratio * light_worker_ram_estimation)
+ (heavy_worker_ratio * heavy_worker_ram_estimation) )

### Chat en vivo

En el multiprocesos, se inicia automáticamente un worker específico para
LiveChat y escucha en [`--gevent-
port`](../../developer/reference/cli#cmdoption-odoo-bin-gevent-port). De
manera predeterminada, las solicitudes HTTP podrán seguir accediendo a los
workers HTTP normales en lugar de al de LiveChat. Debe desplegar un proxy en
Konvergo ERP y redirigir las solicitudes entrantes que empiecen con `/websocket/` al
worker de LiveChat. También debe establecer Konvergo ERP en [`--proxy-
mode`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode) para
que use los encabezados reales de los clientes (como el nombre del
alojamiento, shceme, IP) en lugar de los de proxy.

### Ejemplo de configuración

  * Servidor con 4 CPU, 8 hilos.

  * 60 usuarios concurrentes.

  * 60 usuarios / 6 = 10 <\- Número teórico de workers necesarios.

  * (4 * 2) + 1 = 9 <\- Número teórico máximo de workers.

  * Usaremos 8 workers + 1 para el cron. También usaremos un sistema de monitoreo para medir la carga del CPU y verificar que se encuentre entre 7 y 7.5.

  * RAM = 9 * ((0.8*150) + (0.2*1024)) ~= 3Go RAM para Konvergo ERP.

En [el archivo de configuración](../../developer/reference/cli#reference-
cmdline-config-file):

    
    
    [options]
    limit_memory_hard = 1677721600
    limit_memory_soft = 629145600
    limit_request = 8192
    limit_time_cpu = 600
    limit_time_real = 1200
    max_cron_threads = 1
    workers = 8
    

## HTTPS

No importa si el acceso es mediante un sitio web, cliente web o servicio web,
Konvergo ERP transmite información de autenticación mediante texto sin cifrar. Esto
significa que un despliegue seguro de Konvergo ERP debe usar HTTPS3. La terminación
SSL se puede implementar con cualquier proxy de terminación SSL, pero requiere
la siguiente configuración:

  * Habilite el [`modo proxy`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode) de Konvergo ERP. Solo debería estar habilitado cuando Konvergo ERP se encuentre detrás de un proxy inverso.

  * Configure la terminación SSL del proxy ([ejemplo de terminación Nginx](https://nginx.com/resources/admin-guide/nginx-ssl-termination/)).

  * Configure el proxy ([ejemplo de Nginx del proxy](https://nginx.com/resources/admin-guide/reverse-proxy/)).

  * Su proxy de terminación SSL también debería redirigir conexiones no seguras de forma automática al puerto seguro.

### Ejemplo de configuración

  * Redirigir solicitudes HTTP a HTTPS.

  * Solicitudes proxy a Konvergo ERP.

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli#reference-cmdline-config-
file):

    
    
    proxy_mode = True
    

En `/etc/nginx/sites-enabled/odoo.conf` configure:

    
    
    #odoo server
    upstream odoo {
      server 127.0.0.1:8069;
    }
    upstream odoochat {
      server 127.0.0.1:8072;
    }
    map $http_upgrade $connection_upgrade {
      default upgrade;
      ''      close;
    }
    
    # http -> https
    server {
      listen 80;
      server_name odoo.mycompany.com;
      rewrite ^(.*) https://$host$1 permanent;
    }
    
    server {
      listen 443 ssl;
      server_name odoo.mycompany.com;
      proxy_read_timeout 720s;
      proxy_connect_timeout 720s;
      proxy_send_timeout 720s;
    
      # SSL parameters
      ssl_certificate /etc/ssl/nginx/server.crt;
      ssl_certificate_key /etc/ssl/nginx/server.key;
      ssl_session_timeout 30m;
      ssl_protocols TLSv1.2;
      ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
      ssl_prefer_server_ciphers off;
    
      # log
      access_log /var/log/nginx/odoo.access.log;
      error_log /var/log/nginx/odoo.error.log;
    
      # Redirect websocket requests to odoo gevent port
      location /websocket {
        proxy_pass http://odoochat;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
    
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
        proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
      }
    
      # Redirect requests to odoo backend server
      location / {
        # Add Headers for odoo proxy mode
        proxy_set_header X-Forwarded-Host $http_host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
        proxy_pass http://odoo;
    
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
        proxy_cookie_flags session_id samesite=lax secure;  # requires nginx 1.19.8
      }
    
      # common gzip
      gzip_types text/css text/scss text/plain text/xml application/xml application/json application/javascript;
      gzip on;
    }
    

### Reforzamiento de HTTPS

Agregue el encabezado `Strict-Transport-Security` a todas las peticiones para
evitar que los navegadores envíen una solicitud HTTP simple a este dominio.
Necesitará mantener un servicio HTTPS con un certificado válido en operación
para este dominio todo el tiempo. De lo contrario, sus usuarios visualizarán
las alertas de seguridad o no podrán acceder.

Debe forzar las conexiones HTTPS durante un año para cada visitante en NGINX
con la línea:

    
    
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    

Es posible definir una configuración adicional para la cookie `session_id`,
puede agregar el marcador `secure` para asegurarse de que nunca se transmita
por HTTP y `samesite=lax` para prevenir un
[CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) autenticado.

    
    
    # requires nginx 1.19.8
    proxy_cookie_flags session_id samesite=lax secure;
    

## Konvergo ERP como una aplicación WSGI

También es posible montar Konvergo ERP como una aplicación
[WSGI](https://wsgi.readthedocs.org/) estándar. Konvergo ERP proporciona la base para
un script de lanzamiento WSGI como `odoo-wsgi.example.py`. Debe personalizar
el script (luego de copiarlo desde la carpeta de configuración) para realizar
la configuración de forma correcta en `odoo.tools.config` y no en la línea de
comandos o el archivo de configuración.

Sin embargo, el servidor WSGI solo mostrará el punto de conexión HTTP
principal para el cliente web, sitio web y servicio web API. Konvergo ERP ya no
controla la creación de workers, así que ya no puede configurar el cron o los
workers del chat en vivo.

### Workers de cron

Es necesario que inicie uno de los servidores incluidos en Konvergo ERP junto al
servidor WSGI para procesar trabajos cron. Ese servidor debe estar configurado
para que solo procese crons y no solicitudes HTTPS. Use la opción [`--no-
http`](../../developer/reference/cli#cmdoption-odoo-bin-no-http) en la
línea de comandos o ajuste el archivo de configuración con `http_enable =
False`.

En sistemas de tipo Linux es recomendable utilizar el servidor multiprocesos
en lugar del multihilos para aprovechar mejor el hardware e incrementar la
estabilidad, por ejemplo, use las opciones
[`--workers=-1`](../../developer/reference/cli#cmdoption-odoo-bin-
workers) y [`--max-cron-
threads=n`](../../developer/reference/cli#cmdoption-odoo-bin-max-cron-
threads) de la línea de comandos.

### Chat en vivo

Es necesario usar un servidor WSGI compatible con gevent para que la función
de chat en vivo trabaje de forma correcta. Ese servidor debe poder gestionar
varias conexiones persistentes de manera simultánea, pero no necesita mucha
potencia de procesamiento. Redirija todas las solicitudes que comienzan con
`/websocket/` a ese servidor y usar un servidor normal WSGI (de hilos o
procesos) para el resto de las solicitudes.

El servidor cron de Konvergo ERP también es útil para las solicitudes de chat en vivo.
Solo tiene que soltar la opción [`--no-
http`](../../developer/reference/cli#cmdoption-odoo-bin-no-http) de la
interfaz de línea de comandos desde el servidor cron y asegurarse de que las
solicitudes que comienzan con `/websocket/` estén dirigidas a este servidor,
ya sea en [`--http-port`](../../developer/reference/cli#cmdoption-odoo-
bin-http-port) (servidor multihilos) o en [`--gevent-
port`](../../developer/reference/cli#cmdoption-odoo-bin-gevent-port)
(servidor multiprocesos).

## Gestión de archivos y archivos adjuntos estáticos

Con fines de mejorar el proceso de desarrollo, Konvergo ERP gestiona todos los
archivos estáticos y adjuntos en sus módulos de forma directa. Sin embargo,
puede que esto no sea lo mejor en cuestión de rendimiento, además solo debería
utilizar un servidor HTTP estático para gestionar sus archivos estáticos.

### Gestión de archivos estáticos

Los archivos estáticos de Konvergo ERP se encuentran en la carpeta `static/` de cada
módulo. Por lo tanto, los archivos estáticos se pueden gestionar al
interceptar todas las solicitudes a `/_MÓDULO_ /static/_ARCHIVO_` y buscar el
módulo (y el archivo) correcto en las distintas rutas de los complementos.

Es recomendable que establezca el encabezado `Content-Security-Policy:
default-src 'none'` en todas las imágenes proporcionadas por el servidor web.
No es indispensable, ya que los usuarios no pueden modificar o inyectar
contenido a la carpeta `static/` de los módulos y las imágenes existentes son
finales (no obtienen nuevos recursos por su cuenta). Sin embargo, es una buena
práctica.

Con la configuración NGINX (https) anterior, agregue los siguientes bloques
`map` y `location` para gestionar archivos estáticos a través de NGINX.

    
    
    map $sent_http_content_type $content_type_csp {
        default "";
        ~image/ "default-src 'none'";
    }
    
    server {
        # the rest of the configuration
    
        location @odoo {
            # copy-paste the content of the / location block
        }
    
        # Serve static files right away
        location ~ ^/[^/]+/static/.+$ {
            # root and try_files both depend on your addons paths
            root ...;
            try_files ... @odoo;
            expires 24h;
            add_header Content-Security-Policy $content_type_csp;
        }
    }
    

Las directivas `root` y `try_files` reales dependen de su instalación, sobre
todo de [`--addons-path`](../../developer/reference/cli#cmdoption-odoo-
bin-addons-path).

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-RGViaWFuIHBhY2thZ2U=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tab" tabindex="0">Debian package</button><button aria-controls="panel-0-R2l0IHNvdXJjZXM=" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tab" tabindex="-1">Git sources</button></div><div aria-labelledby="tab-0-RGViaWFuIHBhY2thZ2U=" class="sphinx-tabs-panel group-tab" id="panel-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tabpanel" tabindex="0"><p>Digamos que Konvergo ERP se instaló a través de los <b>paquetes de Debian</b> para Community y Enterprise. Además, la ruta de <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> es <code>'/usr/lib/python3/dist-packages/odoo/addons'</code>.</p>
<p><code>root</code> y <code>try_files</code> deberían ser:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/usr/lib/python3/dist-packages/odoo/addons</span><span class="p">;</span>
<span class="k">try_files</span> <span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-0-R2l0IHNvdXJjZXM=" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tabpanel" tabindex="0"><p>Digamos que Konvergo ERP se instaló a través del código <b>fuente</b>, que tanto el repositorio de Git de Community como el de Enterprise se clonaron en <code>/opt/odoo/community</code> y <code>/opt/odoo/enterprise</code> respectivamente y que la ruta de <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> es <code>'/opt/odoo/community/odoo/addons,/opt/odoo/community/addons,/opt/odoo/enterprise'</code>.</p>
<p><code>root</code> y <code>try_files</code> deberían ser:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/opt/odoo</span><span class="p">;</span>
<span class="k">try_files</span> <span class="s">/community/odoo/addons</span><span class="nv">$uri</span> <span class="s">/community/addons</span><span class="nv">$uri</span> <span class="s">/enterprise</span><span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div></div>
</div>

### Alojamiento de adjuntos

Los adjuntos son archivos que se guardan en un filestore y Konvergo ERP regula el
acceso al mismo. No se puede acceder a estos adjuntos mediante un servidor web
estático ya que se requieren diversas consultas en la base de datos para
determinar si los archivos están almacenados y si el usuario actual tiene
acceso a los mismos.

De igual manera, ya que se localizó el archivo y Konvergo ERP verificó los derechos de
acceso, es una buena idea almacenar el archivo en el servidor web estático en
lugar de Konvergo ERP. Para que Konvergo ERP pueda delegar el alojamiento del archivo al
servidor web estático las extensiones
[X-Sendfile](https://tn123.org/mod_xsendfile/) (apache) or
[X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/)
(nginx) deben estar activadas y configuradas en el servidor web estático. Ya
que esté configurada, inicie Konvergo ERP con la marca
[`--x-sendfile`](../../developer/reference/cli#cmdoption-odoo-bin-x-
sendfile) en la interfaz de línea de comandos (esta marca única se usa tanto
para X-Sendfile como para X-Accel).

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><ul>
<li><p>La extensión X-Sendfile para Apache (y servidores web comptaibles) no necesita configuración adicional.</p></li>
<li><p>La extensión X-Accel para NGINX <b>sí</b> necesita la configuración que mostramos a continuación:</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">location</span> <span class="s">/web/filestore</span> <span class="p">{</span>
    <span class="kn">internal</span><span class="p">;</span>
    <span class="kn">alias</span> <span class="s">/path/to/odoo/data-dir/filestore</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Si no sabe cuál es la ruta a su filestore, inicie Konvergo ERP con la opción <a href="../../developer/reference/cli#cmdoption-odoo-bin-x-sendfile"><code>--x-sendfile</code></a> y navegue al <code>/web/filestore</code> URL directamente desde Konvergo ERP (no vaya al URL mediante NGINX). Esto registrará una advertencia, el mensaje contiene la configuración que necesita.</p>
</li>
</ul>
</div>

## Seguridad

Para empezar, tome en cuenta que asegurar un sistema de información es un
proceso continuo, no una operación de una sola vez. En cualquier momento, su
entorno solo será tan seguro como el vínculo más débil.

No crea que esta sección es la única lista de medidas para prevenir todos los
problemas de seguridad. Esta lista solo es un resumen de las cosas más
importantes que debe incluir en su plan de acción de seguridad. Lo demás
vendrá de las mejores prácticas de seguridad para su sistema operativo y
distribución. Las mejores prácticas en cuanto a usuarios, contraseñas y la
gestión del control de acceso, etc.

Al desplegar un servidor con acceso a internet, asegúrese de considerar los
siguientes temas relacionados a la seguridad:

  * Siempre configure una contraseña de administrador del super-admin que sea fuerte y también restrinja el acceso a las páginas de gestión de la base de datos tan pronto como configure el sistema. Consulte Seguridad del gestor de la base de datos.

  * Elija inicios de sesión únicos y contraseñas fuertes para todas las cuentas de administrador en todas las bases de datos. No use «admin» como inicio de sesión. No use los mismos inicios de sesión para operaciones del día a día, solo para controlar o gestionar la instalación. _Nunca_ use contraseñas automáticas, como admin/admin, ni si quiera para bases de dato de prueba o de secuenciamiento.

  * **No** instale los datos demo en servidores con acceso a internet. Las bases de datos con información de demo tienen inicios de sesión predeterminados y contraseñas que se podrían usar para ingresar a sus sistemas y puede ser un gran problema, incluso en sistemas de desarrollo o secuenciamiento.

  * Use filtros apropiados para la base de datos ( [`--db-filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter)) para restringir la visibilidad de sus bases de datos según al nombre de host. Vea dbfilter. También puede usar [`-d`](../../developer/reference/cli#cmdoption-odoo-bin-d) para obtener su propia lista (separada por comas) de bases de datos que puede filtrar, en lugar de dejar que el sistema obtenga todo desde el backend de la base de datos.

  * Una vez que su `db_name` y `db_filter` están configurados y solo emparejan las bases de datos por nombre de host. Debe poner la opción de configuración a `Falso`, para prevenir que se enlisten las bases de datos por completo y para bloquear el acceso a la pantalla de gestión de la base de datos (esto también se muestra como [`--no-database-list`](../../developer/reference/cli#cmdoption-odoo-bin-no-database-list) en la opción de la línea de comando).

  * Asegúrese de que el usuario de PostgreSQL ([`--db_user`](../../developer/reference/cli#cmdoption-odoo-bin-r)) _no_ sea un super usuario y que sus bases de datos le pertenezcan a un usuario diferente. Por ejemplo, puede que los super usuarios de `postgres` sean los dueños si usa un `db_user` especializado y no privilegiado. También vea Configurar Konvergo ERP.

  * Mantenga las instalaciones actualizadas e instale con regularidad las versiones más recientes, ya sea a través de GitHub o descárguelas de <https://www.odoo.com/page/download> o <http://nightly.odoo.com>.

  * Configure su servidor en un modo multiproceso con límites adecuados que sean igual a su uso habitual (memoria/CPU/tiempos de espera). También vea Servidor incorporado.

  * Ejecute Konvergo ERP con un servicio web que proporcione una terminación HTTPS con un certificado SSL válido para evitar interceptación en las comunicaciones de texto sin cifrar. Los certificados de SSL son baratos y existen muchas opciones gratuitas. Configure el proxy web para limitar el tamaño de las solicitudes, establezca tiempos de espera apropiados y después active la opción de [`modo proxy`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode). Consulte HTTPS.

  * Si necesita permitir el acceso remoto SSH a sus servidores, asegúrese de configurar una contraseña fuerte para **todas** las cuentas, no solo para `root`. Le recomendamos deshabilitar por completo la autenticación por contraseña y solo permita la autenticación con clave pública. También considere restringir el acceso a través de VPN para permitir el acceso solo a las IP de confianza en el firewall o ejecute un sistema de detección de fuerza bruta como `fail2ban` o algún equivalente.

  * Considere instalar un límite en su proxy o firewall para evitar ataques de fuerza bruta y negar ataques al servicio. También consulte Bloquear ataques de fuerza bruta para obtener más información sobre medidas específicas.

Muchos proveedores de red ofrecen mitigación automática para ataques de
denegación de servicio distribuido (DDoS), pero suele ser un servicio
opcional. Le recomendamos que lo consulte con ellos.

  * Siempre que sea posible, aloje sus instancias de demostración, prueba o preproducción en máquinas distintas a las de producción y aplique las mismas precauciones de seguridad que usa para producción.

  * Si su servidor público de Konvergo ERP tiene acceso a recursos o servicios confidenciales de la red interna (por ejemplo, a través de una VLAN privada), implemente reglas de firewall apropiadas para proteger esos recursos internos. Esto asegurará que el servidor de Konvergo ERP no se pueda usar sin querer (o como resultado de acciones maliciosas de algún usuario) para acceder o alterar los recursos internos. Por lo general, esto se puede hacer con una regla de denegación predeterminada de salida en el firewall, después autorice de forma explícita el acceso solo a los recursos internos que el servidor de Konvergo ERP necesita. [El control de acceso al tráfico IP de Systemd](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd) también puede ser útil para implementar el control de acceso a la red por procesos.

  * Si su servidor público de Konvergo ERP está detrás de un firewall de aplicaciones web, un equilibrador de carga, un servicio transparente de protección contra DDoS (como CloudFare) o un dispositivo similar a nivel de red, querrá evitar tener acceso directo al sistema de Konvergo ERP. Por lo general es difícil mantener el punto de conexión de las direcciones IP de sus servidores de Konvergo ERP en secreto. Por ejemplo, pueden aparecer en registros del servidor web al consultar sistemas públicos o en los encabezados de los correos que envía Konvergo ERP. En este caso, es posible que quiera configurar su firewall para que no se pueda ingresar a las terminales de forma pública, excepto por las direcciones IP de su firewall de aplicaciones web, equilibrador de carga o servicio proxy. Los proveedores de servicios como CloudFlare casi siempre mantienen una lista pública de sus rangos de direcciones IP para este propósito.

  * Si está alojando a varios clientes, aísle datos de clientes y archivos el uno de otro usando contenedores o técnicas de «jail».

  * Configure respaldos diarios para sus bases de datos y los datos de los archivos guardados, cópielos a un servidor de almacenamiento remoto que no sea accesible desde el servidor en sí.

  * Le recomendamos que despliegue Konvergo ERP en Linux y no en Windows. Pero si decide hacerlo en una plataforma de Windows de todas maneras, debe realizar una minuciosa revisión de seguridad del servidor, proceso que no cubre esta guía.

### Bloquear ataques de fuerza bruta

Para despliegues en internet, los ataques a fuerza bruta en las contraseñas de
los usuarios son muy comunes. Esta amenaza no se pueda pasar por alto para los
servidores de Konvergo ERP. Konvergo ERP registra una entrada cada que se realiza un intento
de inicio de sesión y reporta los resultados: éxito o fallo, así como el
objetivo de inicio de sesión e IP fuente.

Los registros de entradas tendrán el siguiente formato.

Inicio de sesión fallido:

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1
    

Inicio de sesión exitoso:

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login successful for db:db_name login:admin from 127.0.0.1
    

Estos registros se pueden analizar fácilmente con un sistema de prevención de
intrusos como `fail2ban`.

Por ejemplo, la siguiente definición del filtro fail2ban debe emparejarse con
un inicio de sesión fallido:

    
    
    [Definition]
    failregex = ^ \d+ INFO \S+ \S+ Login failed for db:\S+ login:\S+ from <HOST>
    ignoreregex =
    

Esto se podía usar con una definición de jail para bloquear los ataques IP en
HTTP.

Así es como se podría ver por bloquear la IP por 15 minutos cuando se detectan
10 intentos fallidos de inicio de sesión desde la misma IP en 1 minuto:

    
    
    [odoo-login]
    enabled = true
    port = http,https
    bantime = 900  ; 15 min ban
    maxretry = 10  ; if 10 attempts
    findtime = 60  ; within 1 min  /!\ Should be adjusted with the TZ offset
    logpath = /var/log/odoo.log  ;  set the actual odoo log path here
    

### Seguridad del gestor de la base de datos

Configurar Konvergo ERP menciona `admin_passwd` de paso.

Esta configuración se usa en todas las pantallas de gestión de la base de
datos (para crear, borrar, descartar o restablecer bases de datos).

Si no se debería acceder a las pantallas de gestión de ninguna manera, debe
establecer la opción de configuración `list_db` a `Falso`, para bloquear el
acceso a todas las pantallas de gestión o selección de bases de datos.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>¡Le recomendamos deshabilitar el gestor de la base de datos para un sistema en internet! Está hecha como una herramienta de desarrollo/demo, para facilitar la creación y gestión rápida de las bases de datos. No está diseñada para usarse en producción, además de que puede exponer funciones peligrosas para los atacantes. Tampoco está diseñado para ejecutar bases de datos grandes y puede que active límites de memoria.</p>
<p>En sistemas en producción, las operaciones de gestión en la base de datos siempre las debe realizar el administrador del sistema, incluyendo el suministro de bases de datos nuevas y respaldos automáticos.</p>
</div>

Asegúrese de configurar un parámetro `db_name` apropiado (y también
`db_filter`, opcionalmente) para que el sistema pueda determinar la base de
datos objetivo para cada petición, de lo contrario, se bloqueará a los
usuarios ya que no se permitirá que ellos mismos elijan la base de datos.

Si solo se puede acceder a las pantallas de gestión desde un grupo de máquinas
específicas, use las funciones de proxy del servidor para bloquear el acceso a
todas las rutas que empiecen con `/web/database`, excepto (quizá)
`/web/database/selector` que muestra la pantalla de selección de base de
datos.

Si se debe de mantener el acceso a la pantalla de gestión de la base de datos,
la configuración de `admin_passwd` se debe de cambiar de la predeterminada que
es `admin`: esta contraseña se debe de revisar antes de permitir operaciones
que alteren la base de datos.

Se debe guardar en un lugar seguro y se debe de generar aleatoriamente, p. ej.

    
    
    $ python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)))'
    

que genera una cadena imprimible pseudoaleatoria de 32 caracteres.

### Restablecer la contraseña maestra

Pueden haber casos en los que la contraseña principal se pierde o ya no es
segura y necesita cambiarse. El siguiente proceso es para administradores del
sistema de una base de datos de Konvergo ERP local y se muestra cómo cambiar y volver
a encriptar la contraseña principal de nuevo de forma manual.

<div class="alert alert-secondary">
<p class="alert-title">
Ver también</p><p>Consulte esta documentación para obtener más información sobre cómo cambiar la contraseña de una cuenta de Konvergo ERP.com: <a href="../odoo_accounts#odoocom-change-password"><span class="std std-ref">Cambiar la contraseña de una cuenta de Konvergo ERP.com</span></a>.</p>
</div>

Al crear una base de datos local se generará una contraseña principal
aleatoria, la cual Konvergo ERP recomienda usar para asegurar la base de datos. Esta
contraseña se implementa de forma automática, así que hay una contraseña
maestra segura para cada entorno de Konvergo ERP local.

<div class="alert alert-warning">
<p class="alert-title">
Advertencia</p><p>Al crear una base de datos de Konvergo ERP local cualquiera dentro de internet podrá entrar a la instalación hasta que use la contraseña para asegurar la base de datos.</p>
</div>

La contraseña maestra se especifica en el archivo de configuración de Konvergo ERP
(`odoo.conf` u `odoorc` (archivo oculto)). Necesita la contraseña maestra de
Konvergo ERP para modificar, crear o borrar una base de datos a través de la interfaz
gráfica de usuario (GUI, por sus siglas en inglés).

#### Ubicar el archivo de configuración

Primero abra el archivo de configuración de Konvergo ERP (`odoo.conf` o `odoorc`
(archivo oculto)).

WindowsLinux

El archivo de configuración está en
`c:\ProgramFiles\Konvergo ERP{VERSION}\server\odoo.conf`.

Según cómo se instale Konvergo ERP en la máquina Linux, es posible que el archivo de
configuración se encuentre en uno de dos lugares diferentes:

  * Instalación del paquete: `/etc/odoo.conf`

  * Instalación de la fuente: `~/.odoorc`

#### Cambiar la contraseña anterior

Una vez que haya abierto el archivo adecuado, modifique la contraseña anterior
en el archivo de configuración a una contraseña temporal.

Graphical user interfaceCommand-line interface

Después de ubicar el archivo de configuración, ábralo con una (GUI), para esto
solo debe hacer doble clic al archivo. El dispositivo debería tener una GUI
predeterminada con la cual abrir el archivo.

Después modifique la línea de la contraseña maestra `admin_passwd =
$pbkdf2-sha…` a `admin_passwd = newpassword1234`, por ejemplo. Elija la
contraseña que desee, siempre y cuando la almacene de forma temporal.
Asegúrese de modificar todos los caracteres después del `=`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>La línea aparece de la siguiente forma: <code>admin_passwd = $pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m</code></p>
<p>La línea modificada aparece de la siguiente manera: <code>admin_passwd = newpassword1234</code></p>
</div>

Modifique la línea de la contraseña maestra con el comando de Unix que aparece
a continuación.

Conéctese a la terminal del servidor de Konvergo ERP a través del protocolo Secure
Shell (SSH) y edite el archivo de configuración. Para modificar el archivo de
configuración use el comando **sudo nano /etc/odoo.conf**.

Luego de abrir el archivo de configuración, modifique la línea de la
contraseña maestra `admin_passwd = $pbkdf2-sha…` a `admin_passwd =
newpassword1234`. Elija la contraseña que desee, siempre y cuando la almacene
de forma temporal. Asegúrese de modificar todos los caracteres después del
`=`.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>0

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>1

#### Reiniciar el servidor de Konvergo ERP

Después de configurar una contraseña temporal **debe** reiniciar el servidor
de Konvergo ERP.

Graphical user interfaceCommand-line interface

Para reiniciar el servidor de Konvergo ERP, primero escriba `servicios` en la **barra
de búsqueda** de Windows. Después, seleccione la aplicación **Servicios** y
vaya al servicio **Konvergo ERP**.

Haga clic derecho en **Konvergo ERP** y seleccione **Iniciar** o **Reiniciar**. Esta
acción reiniciará el servidor de Konvergo ERP de forma manual.

Reinicie el servidor de Konvergo ERP con el comando **sudo service odoo15 restart**.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>2

#### Usar la interfaz web para volver a encriptar la contraseña

Primero, vaya a `/web/database/manager` o a
`http://server_ip:port/web/database/manager` desde un navegador.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>3

Después haga clic en **Establecer contraseña maestra** y escriba la contraseña
temporal seleccionada con anterioridad en el campo **Contraseña maestra**.
Después de este paso, escriba una **nueva contraseña maestra**. La **nueva
contraseña maestra** se cifrará (o encriptará) después de que haga clic en el
botón **Continuar**.

En este punto ya restableció la contraseña con éxito, así que en el archivo de
configuración aparecerá una versión encriptada de la nueva contraseña.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>4

## Navegadores compatibles

Konvergo ERP es compatible con todos los navegadores web principales, siempre y cuando
sigan siendo compatibles con sus creadores.

Los navegadores compatibles son los siguientes:

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge

  * Apple Safari

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Configurar un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> es una parte importante para asegurar el despliegue. Una vez que funciona de forma correcta y coincida solo con una base de datos por nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión de la base de datos. Use el parámetro de inicio <code>--no-database-list</code> para evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso a las pantallas antes mencionadas. También consulte <a href="#security">security</a>.</p>
</div>6

1

    

para que varias instalaciones de Konvergo ERP usen la misma base de datos PostgreSQL,
o brindar más recursos de cálculo para el software.

2

    

técnicamente una herramienta como [socat](http://www.dest-unreach.org/socat/)
puede utilizarse para proxy UNIX sockets a través de redes, pero eso es sobre
todo para el software que sólo se puede utilizar a través de UNIX sockets

3

    

o puede ser accesible solo a través de una red interna de comunicación de
paquetes, pero para esto se necesitan paquetes seguros, protección contra
[suplantación de ARP](https://en.wikipedia.org/wiki/ARP_spoofing) y excluir el
uso de WiFi. Incluso en redes seguras de comunicación de paquetes, se
recomienda el despliegue en HTTPS y los costos posibles se reducen, ya que los
certificados «autofirmados» son más fáciles de desplegar en un entorno
controlado que en Internet.

  *[GUI]: Interfaz gráfica del usuario

