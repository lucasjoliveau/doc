# Configuración del sistema

Este documento describe los pasos básicos para configurar Odoo en producción o
en un servidor de internet, sigue la [instalación](../on_premise.html) y por
lo general no es necesario para un sistema de desarrollo que no está expuesto
a internet.

Advertencia

Si está configurando un servidor público, asegúrese de consultar nuestras
recomendaciones de Seguridad.

## dbfilter

Odoo es un sistema de tenencia múltiple. Es posible que un solo sistema de
Odoo ejecute y preste servicios a varias instancias de la base de datos,
también puede tener varias personalizaciones (por ejemplo, cómo se cargan los
módulos) dependiendo de la base de datos actual.

Esto no representa un problema al trabajar en el backend (cliente web) como un
usuario de la empresa que inició sesión: puede seleccionar la base de datos al
iniciar sesión y las personalizaciones se cargan después.

Sin embargo, esto sí es un problema para los usuarios que no iniciaron sesión
(portal, sitio web) y no están vinculados a la base de datos. Odoo necesita
saber qué base de datos se debería usar para cargar la página de sitio web o
realizar la operación. No habrá ningún problema si no usa la tenencia
múltiple, pues solo hay una base de datos para usar, pero si hay varias bases
de datos a las que se pueden acceder, Odoo necesita una regla para saber cuál
debe usar.

Ese es uno de los propósitos de [`--db-
filter`](../../developer/reference/cli.html#cmdoption-odoo-bin-db-filter),
especificar cuál es la base de datos que se debe seleccionar según el nombre
de host (dominio) que se solicita. El valor es una [expresión
regular](https://docs.python.org/3/library/re.html) que tal vez puede incluir
el nombre de host con inyección dinámica (`%h`) o el primer subdominio (`%d`)
mediante el cual se accede al sistema.

Para servidores que alojan varias bases de datos en producción, sobre todo si
usan `sitio web`, el dbfilter **debe** estar configurado. De lo contrario,
varias funciones no trabajarán de forma adecuada.

### Ejemplos de configuración

  * Para mostrar solo las bases de datos con nombres que empiecen con “mycompany”

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli.html#reference-cmdline-config-
file):

    
    
    [options]
    dbfilter = ^mycompany.*$
    

  * Para mostrar solo las bases de datos que coinciden con el primer subdominio después de `www`. Por ejemplo, la base de datos «mycompany» aparecerá si la solicitud entrante se envió a `www.mycompany.com` o a `mycompany.co.uk`, pero no para `www2.mycompany.com` o `helpdesk.mycompany.com`.

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli.html#reference-cmdline-config-
file):

    
    
    [options]
    dbfilter = ^%d$
    

Nota

Configurar un [`--db-filter`](../../developer/reference/cli.html#cmdoption-
odoo-bin-db-filter) es una parte importante para asegurar el despliegue. Una
vez que funciona de forma correcta y coincida solo con una base de datos por
nombre de host, le recomendamos bloquear el acceso a las pantallas de gestión
de la base de datos. Use el parámetro de inicio `--no-database-list` para
evitar que sus bases de datos aparezcan en una lista y para bloquear el acceso
a las pantallas antes mencionadas. También consulte security.

## PostgreSQL

De forma predeterminada, PostgreSQL solo permite conexiones mediante sockets
UNIX y bucles de retorno (también conocidas como loopback) que ocurren desde
«localhost», en la misma máquina en la que está instalada el servidor
PostgreSQL.

El socket UNIX es suficiente si desea que Odoo y PostgreSQL se ejecuten en la
misma máquina y es la opción predeterminada cuando no se proporciona
alojamiento, pero si desea que Odoo y PostgreSQL se ejecuten en distintas
máquinas 1 necesitará [escuchar las interfaces de
red](https://www.postgresql.org/docs/12/static/runtime-config-connection.html)
2. Para esto:

  * Solo acepte conexiones de bucle de retorno y [use un túnel SSH](https://www.postgresql.org/docs/12/static/ssh-tunnels.html) entre la máquina en la que se ejecuta Odoo se ejecutar y en la que se ejecuta PostgreSQL. Después configure Odoo para que se vincule a su extremo del túnel.

  * Acepte conexiones a la máquina en la que Odoo está instalado, es probable que sea mediante SSL (consulte los [ajustes de conexión con PostgreSQL](https://www.postgresql.org/docs/12/static/runtime-config-connection.html) para obtener más detalles), luego configure Odoo para conectarse a través de la red.

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
    

### Configurar Odoo

Odoo se conecta a un servidor PostgreSQL local mediante un socket UNIX a
través del puerto 5432 de forma predeterminada. Puede anular esto si usa [las
opciones de la base de datos](../../developer/reference/cli.html#reference-
cmdline-server-database) cuando el despliegue de PostgreSQL no es local o no
usa la configuración de instalación predeterminada.

Los [paquetes de instalación](packages.html) crearán un nuevo usuario (`odoo`)
de manera automática y se establecerá como el usuario de la base de datos.

  * Las pantallas de gestión de las bases de datos están protegidas por la configuración `admin_passwd`. Esta configuración solo se puede establecer mediante archivos de configuración y solo se revisa antes de realizar alteraciones a la base de datos. Debe estar configurado en un valor generado de forma aleatoria para garantizar que cualquier fuente externa no pueda utilizar esta interfaz.

  * Todas las operaciones de la base de datos usan las [opciones de base de datos](../../developer/reference/cli.html#reference-cmdline-server-database), entre ellas, la pantalla de gestión de las bases de datos. Para que esta pantalla funcione, el usuario de PostgreSQL necesita tener el permiso `createdb`.

  * Los usuarios siempre pueden abandonar las bases de datos que les pertenecen. Para que la pantalla de gestión de la base de datos deje de ser funcional, el usuario de PostgreSQL debe crearse con `no-createdb` y otro de los usuarios debe ser propietario de la base de datos.

Advertencia

El usuario de PostgreSQL **no debe** ser un superusuario.

#### Ejemplo de configuración

  * Conéctese a un servidor PostgreSQL en 192.168.1.2.

  * Puerto 5432.

  * Use la cuenta con el usuario «odoo».

  * Use «pwd» como contraseña.

  * Filtre solo las bases de datos con nombres que empiecen con «mycompany».

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli.html#reference-cmdline-config-
file):

    
    
    [options]
    admin_passwd = mysupersecretpassword
    db_host = 192.168.1.2
    db_port = 5432
    db_user = odoo
    db_password = pwd
    dbfilter = ^mycompany.*$
    

### SSL entre Odoo y PostgreSQL

Desde Odoo 11.0 puede hacer uso de la conexión SSL entre Odoo y PostgreSQL. En
Odoo, `db_sslmode` controla la seguridad SSL de la conexión con un valor que
puede ser “disable”, “allow”, “prefer”, “require”, “verify-ca” o “verify-
full”.

[Documentación de PostgreSQL](https://www.postgresql.org/docs/12/static/libpq-
ssl.html)

## Servidor incorporado

Odoo incluye servidores integrados HTTP, cron y de chat en vivo. Estos usan
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
[`--workers`](../../developer/reference/cli.html#cmdoption-odoo-bin-workers) o
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
opción [`--workers`](../../developer/reference/cli.html#cmdoption-odoo-bin-
workers) como non-null integer.

Nota

El servidor multiprocesos está personalizado para servidores de Linux, así que
no está disponible para Windows.

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
port`](../../developer/reference/cli.html#cmdoption-odoo-bin-gevent-port). De
manera predeterminada, las solicitudes HTTP podrán seguir accediendo a los
workers HTTP normales en lugar de al de LiveChat. Debe desplegar un proxy en
Odoo y redirigir las solicitudes entrantes que empiecen con `/websocket/` al
worker de LiveChat. También debe establecer Odoo en [`--proxy-
mode`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode) para
que use los encabezados reales de los clientes (como el nombre del
alojamiento, shceme, IP) en lugar de los de proxy.

### Ejemplo de configuración

  * Servidor con 4 CPU, 8 hilos.

  * 60 usuarios concurrentes.

  * 60 usuarios / 6 = 10 <\- Número teórico de workers necesarios.

  * (4 * 2) + 1 = 9 <\- Número teórico máximo de workers.

  * Usaremos 8 workers + 1 para el cron. También usaremos un sistema de monitoreo para medir la carga del CPU y verificar que se encuentre entre 7 y 7.5.

  * RAM = 9 * ((0.8*150) + (0.2*1024)) ~= 3Go RAM para Odoo.

En [el archivo de configuración](../../developer/reference/cli.html#reference-
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
Odoo transmite información de autenticación mediante texto sin cifrar. Esto
significa que un despliegue seguro de Odoo debe usar HTTPS3. La terminación
SSL se puede implementar con cualquier proxy de terminación SSL, pero requiere
la siguiente configuración:

  * Habilite el [`modo proxy`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode) de Odoo. Solo debería estar habilitado cuando Odoo se encuentre detrás de un proxy inverso.

  * Configure la terminación SSL del proxy ([ejemplo de terminación Nginx](https://nginx.com/resources/admin-guide/nginx-ssl-termination/)).

  * Configure el proxy ([ejemplo de Nginx del proxy](https://nginx.com/resources/admin-guide/reverse-proxy/)).

  * Su proxy de terminación SSL también debería redirigir conexiones no seguras de forma automática al puerto seguro.

### Ejemplo de configuración

  * Redirigir solicitudes HTTP a HTTPS.

  * Solicitudes proxy a Odoo.

establezca lo siguiente en el [el archivo de
configuración](../../developer/reference/cli.html#reference-cmdline-config-
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
    

## Odoo como una aplicación WSGI

También es posible montar Odoo como una aplicación
[WSGI](https://wsgi.readthedocs.org/) estándar. Odoo proporciona la base para
un script de lanzamiento WSGI como `odoo-wsgi.example.py`. Debe personalizar
el script (luego de copiarlo desde la carpeta de configuración) para realizar
la configuración de forma correcta en `odoo.tools.config` y no en la línea de
comandos o el archivo de configuración.

Sin embargo, el servidor WSGI solo mostrará el punto de conexión HTTP
principal para el cliente web, sitio web y servicio web API. Odoo ya no
controla la creación de workers, así que ya no puede configurar el cron o los
workers del chat en vivo.

### Workers de cron

Es necesario que inicie uno de los servidores incluidos en Odoo junto al
servidor WSGI para procesar trabajos cron. Ese servidor debe estar configurado
para que solo procese crons y no solicitudes HTTPS. Use la opción [`--no-
http`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-http) en la
línea de comandos o ajuste el archivo de configuración con `http_enable =
False`.

En sistemas de tipo Linux es recomendable utilizar el servidor multiprocesos
en lugar del multihilos para aprovechar mejor el hardware e incrementar la
estabilidad, por ejemplo, use las opciones
[`--workers=-1`](../../developer/reference/cli.html#cmdoption-odoo-bin-
workers) y [`--max-cron-
threads=n`](../../developer/reference/cli.html#cmdoption-odoo-bin-max-cron-
threads) de la línea de comandos.

### Chat en vivo

Es necesario usar un servidor WSGI compatible con gevent para que la función
de chat en vivo trabaje de forma correcta. Ese servidor debe poder gestionar
varias conexiones persistentes de manera simultánea, pero no necesita mucha
potencia de procesamiento. Redirija todas las solicitudes que comienzan con
`/websocket/` a ese servidor y usar un servidor normal WSGI (de hilos o
procesos) para el resto de las solicitudes.

El servidor cron de Odoo también es útil para las solicitudes de chat en vivo.
Solo tiene que soltar la opción [`--no-
http`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-http) de la
interfaz de línea de comandos desde el servidor cron y asegurarse de que las
solicitudes que comienzan con `/websocket/` estén dirigidas a este servidor,
ya sea en [`--http-port`](../../developer/reference/cli.html#cmdoption-odoo-
bin-http-port) (servidor multihilos) o en [`--gevent-
port`](../../developer/reference/cli.html#cmdoption-odoo-bin-gevent-port)
(servidor multiprocesos).

## Gestión de archivos y archivos adjuntos estáticos

Con fines de mejorar el proceso de desarrollo, Odoo gestiona todos los
archivos estáticos y adjuntos en sus módulos de forma directa. Sin embargo,
puede que esto no sea lo mejor en cuestión de rendimiento, además solo debería
utilizar un servidor HTTP estático para gestionar sus archivos estáticos.

### Gestión de archivos estáticos

Los archivos estáticos de Odoo se encuentran en la carpeta `static/` de cada
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
todo de [`--addons-path`](../../developer/reference/cli.html#cmdoption-odoo-
bin-addons-path).

Example

Debian packageGit sources

Digamos que Odoo se instaló a través de los **paquetes de Debian** para
Community y Enterprise. Además, la ruta de [`--addons-
path`](../../developer/reference/cli.html#cmdoption-odoo-bin-addons-path) es
`'/usr/lib/python3/dist-packages/odoo/addons'`.

`root` y `try_files` deberían ser:

    
    
    root /usr/lib/python3/dist-packages/odoo/addons;
    try_files $uri @odoo;
    

Digamos que Odoo se instaló a través del código **fuente** , que tanto el
repositorio de Git de Community como el de Enterprise se clonaron en
`/opt/odoo/community` y `/opt/odoo/enterprise` respectivamente y que la ruta
de [`--addons-path`](../../developer/reference/cli.html#cmdoption-odoo-bin-
addons-path) es
`'/opt/odoo/community/odoo/addons,/opt/odoo/community/addons,/opt/odoo/enterprise'`.

`root` y `try_files` deberían ser:

    
    
    root /opt/odoo;
    try_files /community/odoo/addons$uri /community/addons$uri /enterprise$uri @odoo;
    

### Alojamiento de adjuntos

Los adjuntos son archivos que se guardan en un filestore y Odoo regula el
acceso al mismo. No se puede acceder a estos adjuntos mediante un servidor web
estático ya que se requieren diversas consultas en la base de datos para
determinar si los archivos están almacenados y si el usuario actual tiene
acceso a los mismos.

De igual manera, ya que se localizó el archivo y Odoo verificó los derechos de
acceso, es una buena idea almacenar el archivo en el servidor web estático en
lugar de Odoo. Para que Odoo pueda delegar el alojamiento del archivo al
servidor web estático las extensiones
[X-Sendfile](https://tn123.org/mod_xsendfile/) (apache) or
[X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/)
(nginx) deben estar activadas y configuradas en el servidor web estático. Ya
que esté configurada, inicie Odoo con la marca
[`--x-sendfile`](../../developer/reference/cli.html#cmdoption-odoo-bin-x-
sendfile) en la interfaz de línea de comandos (esta marca única se usa tanto
para X-Sendfile como para X-Accel).

Nota

  * La extensión X-Sendfile para Apache (y servidores web comptaibles) no necesita configuración adicional.

  * La extensión X-Accel para NGINX **sí** necesita la configuración que mostramos a continuación:
    
        location /web/filestore {
        internal;
        alias /path/to/odoo/data-dir/filestore;
    }
    

Si no sabe cuál es la ruta a su filestore, inicie Odoo con la opción
[`--x-sendfile`](../../developer/reference/cli.html#cmdoption-odoo-bin-x-
sendfile) y navegue al `/web/filestore` URL directamente desde Odoo (no vaya
al URL mediante NGINX). Esto registrará una advertencia, el mensaje contiene
la configuración que necesita.

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

  * Use filtros apropiados para la base de datos ( [`--db-filter`](../../developer/reference/cli.html#cmdoption-odoo-bin-db-filter)) para restringir la visibilidad de sus bases de datos según al nombre de host. Vea dbfilter. También puede usar [`-d`](../../developer/reference/cli.html#cmdoption-odoo-bin-d) para obtener su propia lista (separada por comas) de bases de datos que puede filtrar, en lugar de dejar que el sistema obtenga todo desde el backend de la base de datos.

  * Una vez que su `db_name` y `db_filter` están configurados y solo emparejan las bases de datos por nombre de host. Debe poner la opción de configuración a `Falso`, para prevenir que se enlisten las bases de datos por completo y para bloquear el acceso a la pantalla de gestión de la base de datos (esto también se muestra como [`--no-database-list`](../../developer/reference/cli.html#cmdoption-odoo-bin-no-database-list) en la opción de la línea de comando).

  * Asegúrese de que el usuario de PostgreSQL ([`--db_user`](../../developer/reference/cli.html#cmdoption-odoo-bin-r)) _no_ sea un super usuario y que sus bases de datos le pertenezcan a un usuario diferente. Por ejemplo, puede que los super usuarios de `postgres` sean los dueños si usa un `db_user` especializado y no privilegiado. También vea Configurar Odoo.

  * Mantenga las instalaciones actualizadas e instale con regularidad las versiones más recientes, ya sea a través de GitHub o descárguelas de <https://www.odoo.com/page/download> o <http://nightly.odoo.com>.

  * Configure su servidor en un modo multiproceso con límites adecuados que sean igual a su uso habitual (memoria/CPU/tiempos de espera). También vea Servidor incorporado.

  * Ejecute Odoo con un servicio web que proporcione una terminación HTTPS con un certificado SSL válido para evitar interceptación en las comunicaciones de texto sin cifrar. Los certificados de SSL son baratos y existen muchas opciones gratuitas. Configure el proxy web para limitar el tamaño de las solicitudes, establezca tiempos de espera apropiados y después active la opción de [`modo proxy`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode). Consulte HTTPS.

  * Si necesita permitir el acceso remoto SSH a sus servidores, asegúrese de configurar una contraseña fuerte para **todas** las cuentas, no solo para `root`. Le recomendamos deshabilitar por completo la autenticación por contraseña y solo permita la autenticación con clave pública. También considere restringir el acceso a través de VPN para permitir el acceso solo a las IP de confianza en el firewall o ejecute un sistema de detección de fuerza bruta como `fail2ban` o algún equivalente.

  * Considere instalar un límite en su proxy o firewall para evitar ataques de fuerza bruta y negar ataques al servicio. También consulte Bloquear ataques de fuerza bruta para obtener más información sobre medidas específicas.

Muchos proveedores de red ofrecen mitigación automática para ataques de
denegación de servicio distribuido (DDoS), pero suele ser un servicio
opcional. Le recomendamos que lo consulte con ellos.

  * Siempre que sea posible, aloje sus instancias de demostración, prueba o preproducción en máquinas distintas a las de producción y aplique las mismas precauciones de seguridad que usa para producción.

  * Si su servidor público de Odoo tiene acceso a recursos o servicios confidenciales de la red interna (por ejemplo, a través de una VLAN privada), implemente reglas de firewall apropiadas para proteger esos recursos internos. Esto asegurará que el servidor de Odoo no se pueda usar sin querer (o como resultado de acciones maliciosas de algún usuario) para acceder o alterar los recursos internos. Por lo general, esto se puede hacer con una regla de denegación predeterminada de salida en el firewall, después autorice de forma explícita el acceso solo a los recursos internos que el servidor de Odoo necesita. [El control de acceso al tráfico IP de Systemd](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd.html) también puede ser útil para implementar el control de acceso a la red por procesos.

  * Si su servidor público de Odoo está detrás de un firewall de aplicaciones web, un equilibrador de carga, un servicio transparente de protección contra DDoS (como CloudFare) o un dispositivo similar a nivel de red, querrá evitar tener acceso directo al sistema de Odoo. Por lo general es difícil mantener el punto de conexión de las direcciones IP de sus servidores de Odoo en secreto. Por ejemplo, pueden aparecer en registros del servidor web al consultar sistemas públicos o en los encabezados de los correos que envía Odoo. En este caso, es posible que quiera configurar su firewall para que no se pueda ingresar a las terminales de forma pública, excepto por las direcciones IP de su firewall de aplicaciones web, equilibrador de carga o servicio proxy. Los proveedores de servicios como CloudFlare casi siempre mantienen una lista pública de sus rangos de direcciones IP para este propósito.

  * Si está alojando a varios clientes, aísle datos de clientes y archivos el uno de otro usando contenedores o técnicas de «jail».

  * Configure respaldos diarios para sus bases de datos y los datos de los archivos guardados, cópielos a un servidor de almacenamiento remoto que no sea accesible desde el servidor en sí.

  * Le recomendamos que despliegue Odoo en Linux y no en Windows. Pero si decide hacerlo en una plataforma de Windows de todas maneras, debe realizar una minuciosa revisión de seguridad del servidor, proceso que no cubre esta guía.

### Bloquear ataques de fuerza bruta

Para despliegues en internet, los ataques a fuerza bruta en las contraseñas de
los usuarios son muy comunes. Esta amenaza no se pueda pasar por alto para los
servidores de Odoo. Odoo registra una entrada cada que se realiza un intento
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

Configurar Odoo menciona `admin_passwd` de paso.

Esta configuración se usa en todas las pantallas de gestión de la base de
datos (para crear, borrar, descartar o restablecer bases de datos).

Si no se debería acceder a las pantallas de gestión de ninguna manera, debe
establecer la opción de configuración `list_db` a `Falso`, para bloquear el
acceso a todas las pantallas de gestión o selección de bases de datos.

Advertencia

¡Le recomendamos deshabilitar el gestor de la base de datos para un sistema en
internet! Está hecha como una herramienta de desarrollo/demo, para facilitar
la creación y gestión rápida de las bases de datos. No está diseñada para
usarse en producción, además de que puede exponer funciones peligrosas para
los atacantes. Tampoco está diseñado para ejecutar bases de datos grandes y
puede que active límites de memoria.

En sistemas en producción, las operaciones de gestión en la base de datos
siempre las debe realizar el administrador del sistema, incluyendo el
suministro de bases de datos nuevas y respaldos automáticos.

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
sistema de una base de datos de Odoo local y se muestra cómo cambiar y volver
a encriptar la contraseña principal de nuevo de forma manual.

Ver también

Consulte esta documentación para obtener más información sobre cómo cambiar la
contraseña de una cuenta de Odoo.com: [Cambiar la contraseña de una cuenta de
Odoo.com](../odoo_accounts.html#odoocom-change-password).

Al crear una base de datos local se generará una contraseña principal
aleatoria, la cual Odoo recomienda usar para asegurar la base de datos. Esta
contraseña se implementa de forma automática, así que hay una contraseña
maestra segura para cada entorno de Odoo local.

Advertencia

Al crear una base de datos de Odoo local cualquiera dentro de internet podrá
entrar a la instalación hasta que use la contraseña para asegurar la base de
datos.

La contraseña maestra se especifica en el archivo de configuración de Odoo
(`odoo.conf` u `odoorc` (archivo oculto)). Necesita la contraseña maestra de
Odoo para modificar, crear o borrar una base de datos a través de la interfaz
gráfica de usuario (GUI, por sus siglas en inglés).

#### Ubicar el archivo de configuración

Primero abra el archivo de configuración de Odoo (`odoo.conf` o `odoorc`
(archivo oculto)).

WindowsLinux

El archivo de configuración está en
`c:\ProgramFiles\Odoo{VERSION}\server\odoo.conf`.

Según cómo se instale Odoo en la máquina Linux, es posible que el archivo de
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

Example

La línea aparece de la siguiente forma: `admin_passwd =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`

La línea modificada aparece de la siguiente manera: `admin_passwd =
newpassword1234`

Modifique la línea de la contraseña maestra con el comando de Unix que aparece
a continuación.

Conéctese a la terminal del servidor de Odoo a través del protocolo Secure
Shell (SSH) y edite el archivo de configuración. Para modificar el archivo de
configuración use el comando **sudo nano /etc/odoo.conf**.

Luego de abrir el archivo de configuración, modifique la línea de la
contraseña maestra `admin_passwd = $pbkdf2-sha…` a `admin_passwd =
newpassword1234`. Elija la contraseña que desee, siempre y cuando la almacene
de forma temporal. Asegúrese de modificar todos los caracteres después del
`=`.

Example

La línea aparece de la siguiente forma: `admin_passwd =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`

La línea modificada aparece de la siguiente manera: `admin_passwd =
newpassword1234`

Importante

Es indispensable que cambie la contraseña a otra cosa en lugar de activar un
nuevo restablecimiento de contraseña al agregar un punto y coma `;` al inicio
de la línea. Esto asegurará que la base de datos esté segura durante todo el
proceso de restablecimiento de contraseña.

#### Reiniciar el servidor de Odoo

Después de configurar una contraseña temporal **debe** reiniciar el servidor
de Odoo.

Graphical user interfaceCommand-line interface

Para reiniciar el servidor de Odoo, primero escriba `servicios` en la barra de
búsqueda de Windows. Después, seleccione la aplicación Servicios y vaya al
servicio Odoo.

Haga clic derecho en Odoo y seleccione Iniciar o Reiniciar. Esta acción
reiniciará el servidor de Odoo de forma manual.

Reinicie el servidor de Odoo con el comando **sudo service odoo15 restart**.

Nota

Cambie el número después de `odoo` para que coincida con la versión específica
en la que está ejecutando el servidor.

#### Usar la interfaz web para volver a encriptar la contraseña

Primero, vaya a `/web/database/manager` o a
`http://server_ip:port/web/database/manager` desde un navegador.

Nota

Reemplace `server_ip` con la dirección IP de la base de datos y reemplace
`port` con el número de puerto desde el cual es posible acceder a la base de
datos.

Después haga clic en Establecer contraseña maestra y escriba la contraseña
temporal seleccionada con anterioridad en el campo Contraseña maestra. Después
de este paso, escriba una nueva contraseña maestra. La nueva contraseña
maestra se cifrará (o encriptará) después de que haga clic en el botón
Continuar.

En este punto ya restableció la contraseña con éxito, así que en el archivo de
configuración aparecerá una versión encriptada de la nueva contraseña.

Ver también

Consulte la siguiente documentación para obtener más información sobre la
seguridad de la base de datos de Odoo: Seguridad del gestor de la base de
datos.

## Navegadores compatibles

Odoo es compatible con todos los navegadores web principales, siempre y cuando
sigan siendo compatibles con sus creadores.

Los navegadores compatibles son los siguientes:

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge

  * Apple Safari

Advertencia

Asegúrese de que su navegador esté actualizado y que el creador le siga dando
soporte antes de llenar un reporte de bug.

Nota

Desde Odoo 13.0, ES6 es compatible. Por lo tanto, ya no se da asistencia a IE.

1

    

para que varias instalaciones de Odoo usen la misma base de datos PostgreSQL,
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

