# Configuration du système

This document describes basic steps to set up Konvergo ERP in production or on an
internet-facing server. It follows [installation](../on_premise), and is
not generally necessary for a development systems that is not exposed on the
internet.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous configurez un serveur public, assurez-vous de consulter nos recommandations de <span class="xref std std-ref">sécurité</span> !</p>
</div>

## dbfilter

Konvergo ERP est un système multi-tenant : un seul système Konvergo ERP peut fonctionner et
servir un certain nombre d’instances de base de données. Il est également
hautement personnalisable, les personnalisations (à partir des modules
chargés) dépendant de la « base de données actuelle ».

Ce n’est pas un problème lorsque vous travaillez avec le backend (client web)
en tant qu’utilisateur connecté de l’entreprise : la base de données peut être
sélectionnée lors de la connexion et les personnalisations chargées par la
suite.

Cependant, c’est un problème pour les utilisateurs non connectés (portail,
site web) qui ne sont pas liés à une base de données : Konvergo ERP a besoin de savoir
quelle base de données doit être utilisée pour charger la page du site web ou
effectuer l’opération. Si l’option multi-tenant n’est pas utilisée, ce n’est
pas un problème, car il n’y a qu’une seule base de données à utiliser.
Toutefois s’il y a plusieurs bases de données accessibles, Konvergo ERP a besoin d’une
règle pour savoir laquelle il doit utiliser.

C’est l’un des objectifs de [`--db-
filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter): il
précise comment la base de données doit être sélectionnée en fonction du nom
d’hôte (domaine) demandé. La valeur est une [expression
régulière](https://docs.python.org/3/library/re), incluant éventuellement
le nom d’hôte injecté dynamiquement (`%h`) ou le premier sous-domaine (`%d`)
par lequel le système est accessible.

Pour les serveurs hébergeant plusieurs bases de données en production, en
particulier si `website` est utilisé, dbfilter **doit** être défini, sinon un
certain nombre de fonctionnalités ne fonctionneront pas correctement.

### Exemples de configurations

  * Afficher uniquement les bases de données dont le nom commence par “mycompany”

dans [le fichier de
configuration](../../developer/reference/cli#reference-cmdline-config-
file) définissez :

    
    
    [options]
    dbfilter = ^mycompany.*$
    

  * Afficher uniquement les bases de données correspondant au premier sous-domaine après `www` : par exemple, la base de données « mycompany » sera affichée si la demande entrante a été envoyée à `www.mycompany.com` ou `mycompany.co.uk`, mais pas pour `www2.mycompany.com` ou `helpdesk.mycompany.com`.

dans [le fichier de
configuration](../../developer/reference/cli#reference-cmdline-config-
file) définissez :

    
    
    [options]
    dbfilter = ^%d$
    

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>

## PostgreSQL

Par défaut, PostgreSQL n’autorise que les connexions via les sockets UNIX et
les connexions loopback (à partir de « localhost », le même appareil sur
lequel le serveur PostgreSQL est installé).

Vous pouvez utiliser le socket UNIX si vous voulez qu’Konvergo ERP et PostgreSQL
s’exécutent sur le même appareil et c’est la valeur par défaut lorsqu’aucun
hôte n’est fourni, mais si vous voulez que Konvergo ERP et PostgreSQL s’exécutent sur
des appareils différents 1 il devra [écouter les interfaces
réseau](https://www.postgresql.org/docs/12/static/runtime-config-
connection) 2, soit :

  * N’accepter que les connexions loopback et [utiliser un tunnel SSH](https://www.postgresql.org/docs/12/static/ssh-tunnels) entre l’appareil sur lequel fonctionne Konvergo ERP et celui sur lequel fonctionne PostgreSQL, puis configurer Konvergo ERP pour qu’il se connecte à son extrémité du tunnel.

  * Accepter les connexions à l’appareil sur lequel Konvergo ERP est installé, éventuellement via SSL (voir [Paramètres de connexion PostgreSQL](https://www.postgresql.org/docs/12/static/runtime-config-connection) pour plus de détails), puis configurer Konvergo ERP pour qu’il se connecte via le réseau.

### Exemple de configuration

  * Autoriser la connexion TCP sur localhost

  * Autoriser la connexion TCP à partir du réseau 192.168.1.x

dans `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/pg_hba.conf` définissez :

    
    
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    host    all             all             192.168.1.0/24          md5
    

dans `/etc/postgresql/<YOUR POSTGRESQL VERSION>/main/postgresql.conf`
définissez :

    
    
    listen_addresses = 'localhost,192.168.1.2'
    port = 5432
    max_connections = 80
    

### Configurer Konvergo ERP

Par défaut, Konvergo ERP se connecte à un postgres local sur un socket UNIX via le
port 5432. Ceci peut être remplacé par [les options de base de
données](../../developer/reference/cli#reference-cmdline-server-database)
lorsque votre déploiement Postgres n’est pas local et/ou n’utilise pas les
valeurs par défaut de l’installation.

Les [programmes d’installation](packages) créeront automatiquement un
nouvel utilisateur (`odoo`) et le définiront comme utilisateur pour la base de
données.

  * Les pages d’administration des bases de données sont protégées par le paramètre `admin_passwd`. Ce paramètre peut uniquement être défini dans le fichier de configuration et est simplement vérifié avant de modifier la base de données. Il devrait être généré aléatoirement pour éviter que cette interface ne puisse être utilisée par des tiers non autorisés.

  * Toutes les opérations sur la base de données utilisent les [options de la base de données](../../developer/reference/cli#reference-cmdline-server-database), y compris la page d’administration de la base de données. Pour que cette dernière fonctionne, il est nécessaire que l’utilisateur PostgreSQL ait les droits `createdb`.

  * Les utilisateurs peuvent supprimer des bases de données qui leur appartiennent. Pour rendre non fonctionnelle la page d’administration des bases de données, l’utilisateur PostgreSQL doit être créé avec les droits `no-createdb` et le propriétaire de la base de données doit être un utilisateur PostgreSQL différent.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>L’utilisateur PostgreSQL <em>ne doit pas</em> être un superutilisateur</p>
</div>

#### Exemple de configuration

  * se connecter au serveur PostgreSQL à l’adresse 192.168.1.2

  * port 5432

  * en utilisant un compte utilisateur “odoo”,

  * avec “pwd” comme mot de passe

  * n’affichant que les bases de données dont le nom commence par “mycompany”

dans [le fichier de
configuration](../../developer/reference/cli#reference-cmdline-config-
file) définissez :

    
    
    [options]
    admin_passwd = mysupersecretpassword
    db_host = 192.168.1.2
    db_port = 5432
    db_user = odoo
    db_password = pwd
    dbfilter = ^mycompany.*$
    

### SSL entre Konvergo ERP et PostgreSQL

Depuis Konvergo ERP 11.0, vous pouvez forcer une connexion SSL entre Konvergo ERP et
PostgreSQL. Dans Konvergo ERP, le db_sslmode contrôle la sécurité SSL de la connexion
avec une valeur choisie parmi “disable”, “allow”, “prefer”, “require”,
“verify-ca” ou “verify-full”.

[Doc PostgreSQL](https://www.postgresql.org/docs/12/static/libpq-ssl)

## Serveur intégré

Konvergo ERP comprend des serveurs HTTP, cron et live chat intégrés, en utilisant le
multithreading ou le multiprocessing.

Le serveur **multithread** est un serveur plus simple, utilisé principalement
pour le développement, les démonstrations et sa compatibilité avec différents
systèmes d’exploitation (y compris Windows). Un nouveau thread est créé pour
chaque nouvelle requête HTTP, même pour les connexions de longue durée telles
que websocket. Les threads cron démon sont également créés. En raison d’une
limitation de Python (GIL), il n’utilise pas le matériel de manière optimale.

Le serveur multithread est le serveur par défaut, également pour les
conteneurs Docker. Il est sélectionné lorsque l’option
[`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-workers)
est omise ou lorsqu’elle est fixée à `0`.

Le serveur **multiprocessing** est un serveur à part entière, utilisé
principalement pour la production. Il n’est pas soumis à la même limitation de
Python (GIL) sur l’utilisation des ressources et utilise donc le matériel de
manière optimale. Un pool de workers est créé lors du démarrage du serveur.
Les nouvelles requêtes HTTP sont mises en attente par le système
d’exploitation jusqu’à ce qu’il y ait des workers prêts à les traiter. Un
worker HTTP événementiel supplémentaire pour le live chat est créé sur un
autre port. Des workers cron supplémentaires sont également créés. Un reaper
de processus configurable surveille l’utilisation des ressources et peut
arrêter/relancer des workers défaillants.

Le serveur multiprocessing est optionnel. Il est sélectionné lorsque l’option
[`--workers`](../../developer/reference/cli#cmdoption-odoo-bin-workers)
est fixée sur un entier non nul.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le serveur multiprocessing n’est pas disponible sur Windows, car il est fortement personnalisé pour les serveurs Linux.</p>
</div>

### Calcul du nombre de workers

  * Règle de base : (#CPU * 2) + 1

  * Workers cron nécessitent un CPU

  * 1 worker ~= 6 utilisateurs simultanés

### Calcul de la taille de la mémoire

  * Nous considérons que 20% des requêtes sont des requêtes lourdes, tandis que 80% sont des requêtes plus simples

  * Un gros worker, lorsque tous les champs calculés sont bien conçus, les requêtes SQL sont bien conçues,… est estimé consommer environ 1 Go de RAM

  * Un worker plus léger, dans le même scénario, est estimé consommer environ 150 Mo de RAM

RAM nécessaire = #worker * ( (light_worker_ratio *
light_worker_ram_estimation) + (heavy_worker_ratio *
heavy_worker_ram_estimation) )

### LiveChat

En multiprocessing, un worker live chat dédié est automatiquement lancé et
écoute le [`--gevent-port`](../../developer/reference/cli#cmdoption-odoo-
bin-gevent-port). Par défaut, les requêtes HTTP continuent d’accéder aux
workers HTTP normaux au lieu du worker live chat. Vous devez déployer un proxy
devant Konvergo ERP et rediriger les requêtes entrantes dont le chemin commence par
`/websocket/` vers le worker live chat. Vous devez également lancer Konvergo ERP en
[`--proxy-mode`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-
mode) pour qu’il utilise les vrais en-têtes clients (tels que le nom d’hôte,
le schéma et l’IP) au lieu des en-têtes du proxy.

### Exemple de configuration

  * Serveur avec 4 CPU, 8 threads

  * 60 utilisateurs simultanés

  * 60 utilisateurs / 6 = 10 <\- nombre théorique de workers nécessaires

  * (4 * 2) + 1 = 9 <\- nombre maximal théorique de workers

  * Nous utiliserons 8 workers + 1 pour le cron. Nous utiliserons également un système de surveillance pour mesurer la charge du CPU et vérifier si elle se situe entre 7 et 7,5.

  * RAM = 9 * ((0.8*150) + (0.2*1024)) ~= 3 Go de RAM pour Konvergo ERP

dans [le fichier de
configuration](../../developer/reference/cli#reference-cmdline-config-
file) :

    
    
    [options]
    limit_memory_hard = 1677721600
    limit_memory_soft = 629145600
    limit_request = 8192
    limit_time_cpu = 600
    limit_time_real = 1200
    max_cron_threads = 1
    workers = 8
    

## HTTPS

Qu’il soit accessible via un site web/un client web ou un service web, Konvergo ERP
transmet les informations d’authentification en texte clair. Cela signifie
qu’un déploiement sécurisé d’Konvergo ERP doit utiliser HTTPS3. La terminaison SSL
peut être implémentée via à peu près n’importe quel proxy de terminaison SSL,
mais nécessite la configuration suivante :

  * Activer le [`mode proxy`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode) dans Konvergo ERP. À activer uniquement quand Konvergo ERP est derrière un reverse proxy.

  * Configurer le proxy de terminaison SSL ([Exemple de terminaison Nginx](https://nginx.com/resources/admin-guide/nginx-ssl-termination/))

  * Configurer le proxy lui-même ([Exemple de proxy Nginx](https://nginx.com/resources/admin-guide/reverse-proxy/))

  * Votre proxy de terminaison SSL doit également rediriger automatiquement les connexions non sécurisées vers le port sécurisé

### Exemple de configuration

  * Rediriger les requêtes http vers https

  * Demandes de proxy à Konvergo ERP

dans [le fichier de
configuration](../../developer/reference/cli#reference-cmdline-config-
file) définissez :

    
    
    proxy_mode = True
    

dans `/etc/nginx/sites-enabled/odoo.conf` définissez :

    
    
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
    

### Durcissement HTTPS

Ajoutez l’en-tête `Strict-Transport-Security` à toutes les requêtes, pour
empêcher les navigateurs d’envoyer une requête HTTP simple à ce domaine. Vous
devrez maintenir en permanence un service HTTPS fonctionnel avec un certificat
valide sur ce domaine, faute de quoi vos utilisateurs recevront des alertes de
sécurité ou seront dans l’incapacité totale d’y accéder.

Forcez les connexions HTTPS pendant un an pour chaque visiteur dans NGINX avec
la ligne :

    
    
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
    

Une configuration supplémentaire peut être définie pour le cookie
`session_id`. Le drapeau `Secure` peut être ajouté pour s’assurer qu’il n’est
jamais transmis par HTTP et `SameSite=Lax` pour empêcher le
[CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) authentifié.

    
    
    # requires nginx 1.19.8
    proxy_cookie_flags session_id samesite=lax secure;
    

## Konvergo ERP en tant qu’application WSGI

Il est également possible de monter Konvergo ERP comme une application
[WSGI](https://wsgi.readthedocs.org/) standard. Konvergo ERP fournit la base d’un
script de lancement WSGI sous la forme de `odoo-wsgi.example.py`. Ce script
doit être personnalisé (éventuellement après l’avoir copié depuis le
répertoire de configuration) pour définir correctement la configuration
directement dans `odoo.tools.config` plutôt que par ligne de commande ou un
fichier de configuration.

Cependant, le serveur WSGI n’exposera que le point de terminaison HTTP
principal pour le client web, le site web et l’API du service web. Comme Konvergo ERP
ne contrôle plus la création de workers, il ne peut pas configurer de workers
cron ou livechat.

### Workers cron

Le démarrage d’un des serveurs Konvergo ERP intégrés à côté du serveur WSGI est requis
pour traiter les tâches cron. Ce serveur doit être configuré pour ne traiter
que les crons et pas les requêtes HTTP en utilisant l’option [`--no-
http`](../../developer/reference/cli#cmdoption-odoo-bin-no-http) cli ou
le paramètre `http_enable = False` du fichier de configuration.

Sur les systèmes de type Linux, il est recommandé d’utiliser le serveur
multiprocessing au lieu du serveur multithreading pour bénéficier d’une
meilleure utilisation du matériel et d’une stabilité accrue, c’est-à-dire en
utilisant les options
[`--workers=-1`](../../developer/reference/cli#cmdoption-odoo-bin-
workers) et [`--max-cron-
threads=n`](../../developer/reference/cli#cmdoption-odoo-bin-max-cron-
threads) cli.

### LiveChat

L’utilisation d’un serveur WSGI compatible avec gevent est requise au bon
fonctionnement de la fonction de live chat. Ce serveur doit être capable de
gérer de nombreuses connexions de longue durée simultanées, mais n’a pas
besoin d’une grande puissance de traitement. Toutes les requêtes dont le
chemin commence par `/websocket/` doivent être redirigées vers ce serveur. Un
serveur WSGI normal (basé sur un thread/processus) doit être utilisé pour
toutes les autres requêtes.

Le serveur cron d’Konvergo ERP peut également être utilisé pour répondre aux requêtes
de live chat. Il suffit de supprimer l’option [`--no-
http`](../../developer/reference/cli#cmdoption-odoo-bin-no-http) cli du
serveur cron et de s’assurer que les requêtes dont le chemin commence par
`/websocket/` sont redirigées vers ce serveur, sur le [`--http-
port`](../../developer/reference/cli#cmdoption-odoo-bin-http-port)
(serveur multithreading) ou sur le [`--gevent-
port`](../../developer/reference/cli#cmdoption-odoo-bin-gevent-port)
(serveur multiprocessing).

## Servir des fichiers statiques et des pièces jointes

Pour des raisons de commodité de développement, Konvergo ERP sert directement tous les
fichiers statiques et les pièces jointes dans ses modules. Ce n’est peut-être
pas idéal en termes de performances et les fichiers statiques doivent
généralement être servis par un serveur HTTP statique.

### Servir des fichiers statiques

Les fichiers statiques Konvergo ERP se situent dans le fichier `static/` de chaque
module, dont les fichiers statiques peuvent être servis en interceptant toutes
les requêtes vers `/_MODULE_ /static/_FILE_`, et en recherchant le bon module
(et le bon fichier) dans les différents chemins d’accès aux modules
complémentaires.

Il est recommandé de définir l’en-tête `Content-Security-Policy: default-src
'none'` sur toutes les limages délivrées par le serveur web. Il n’est pas
strictement nécessaire, car les utilisateurs ne peuvent pas modifier/injecter
du contenu dans le dossier `static/` des modules et les images existantes sont
définitives (elles ne récupèrent pas de nouvelles ressources par elles-mêmes).
Il s’agit toutefois d’une bonne pratique.

En utilisant la configuration NGINX (https) susmentionnée, les blocs `map` et
`location` suivants doivent être ajoutés pour servir les fichiers statiques
via NGINX.

    
    
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
    

Les directives `root` et `try_files` dépendent de votre installation, en
particulier de votre [`--addons-
path`](../../developer/reference/cli#cmdoption-odoo-bin-addons-path).

<div class="alert alert-success">
<p class="alert-title">
Example</p><div class="sphinx-tabs docutils container">
<div aria-label="Tabbed content" role="tablist"><button aria-controls="panel-0-RGViaWFuIHBhY2thZ2U=" aria-selected="true" class="sphinx-tabs-tab group-tab" id="tab-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tab" tabindex="0">Debian package</button><button aria-controls="panel-0-R2l0IHNvdXJjZXM=" aria-selected="false" class="sphinx-tabs-tab group-tab" id="tab-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tab" tabindex="-1">Git sources</button></div><div aria-labelledby="tab-0-RGViaWFuIHBhY2thZ2U=" class="sphinx-tabs-panel group-tab" id="panel-0-RGViaWFuIHBhY2thZ2U=" name="RGViaWFuIHBhY2thZ2U=" role="tabpanel" tabindex="0"><p>Disons qu’Konvergo ERP a été installé via les <b>packages debian</b> pour les éditions Community et Enterprise et que le <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> est <code>'/usr/lib/python3/dist-packages/odoo/addons'</code>.</p>
<p>Les <code>root</code> et <code>try_files</code> doivent être :</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/usr/lib/python3/dist-packages/odoo/addons</span><span class="p">;</span>
<span class="k">try_files</span> <span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div><div aria-labelledby="tab-0-R2l0IHNvdXJjZXM=" class="sphinx-tabs-panel group-tab" hidden="true" id="panel-0-R2l0IHNvdXJjZXM=" name="R2l0IHNvdXJjZXM=" role="tabpanel" tabindex="0"><p>Disons qu’Konvergo ERP a été installé via les <b>sources</b>, que les dépôts git Community et Enterprise ont été clonés dans <code>/opt/odoo/community</code> et <code>/opt/odoo/enterprise</code> respectively, et que le <a href="../../developer/reference/cli#cmdoption-odoo-bin-addons-path"><code>--addons-path</code></a> est <code>'/opt/odoo/community/odoo/addons,/opt/odoo/community/addons,/opt/odoo/enterprise'</code>.</p>
<p>Les <code>root</code> et <code>try_files</code> doivent être :</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">root</span> <span class="s">/opt/odoo</span><span class="p">;</span>
<span class="k">try_files</span> <span class="s">/community/odoo/addons</span><span class="nv">$uri</span> <span class="s">/community/addons</span><span class="nv">$uri</span> <span class="s">/enterprise</span><span class="nv">$uri</span> <span class="s">@odoo</span><span class="p">;</span>
</pre></div>
</div>
</div></div>
</div>

### Servir des pièces jointes

Les pièces jointes sont les fichiers stockés dans le filestore dont l’accès
est réglementé par Konvergo ERP. Il n’est pas possible d’y accéder directement via un
serveur web statique, car l’accès à ces fichiers nécessite de multiples
recherches dans la base de données pour déterminer où les fichiers sont
stockés et si l’utilisateur actuel peut y accéder ou non.

Néanmoins, une fois que le fichier a été localisé et que les droits d’accès
ont été vérifiés par Konvergo ERP, c’est une bonne idée de servir le fichier en
utilisant le serveur web statique au lieu d’Konvergo ERP. Pour que Konvergo ERP délègue le
service des fichiers au serveur web statique, les extensions
[X-Sendfile](https://tn123.org/mod_xsendfile/) (apache) ou
[X-Accel](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/)
(nginx) doivent être activées et configurées sur le serveur web statique. Une
fois qu’elles sont configurées, démarrez Konvergo ERP avec l’indicateur CLI
[`--x-sendfile`](../../developer/reference/cli#cmdoption-odoo-bin-x-
sendfile) (cet indicateur unique est utilisé à la fois pour X-Sendfiele et
X-Accel).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>L’extension X-Sendfile pour apache (et les serveurs web compatibles) ne nécessite aucune configuration supplémentaire.</p></li>
<li><p>L’extension X-Accel pour NGINX <b>nécessite</b> la configuration supplémentaire suivante :</p>
<div class="highlight-nginx notranslate"><div class="highlight"><pre><span></span><span class="k">location</span> <span class="s">/web/filestore</span> <span class="p">{</span>
    <span class="kn">internal</span><span class="p">;</span>
    <span class="kn">alias</span> <span class="s">/path/to/odoo/data-dir/filestore</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
</div>
<p>Dans le cas où vous ne savez pas quel est le chemin d’accès à votre filestore, démarrez Konvergo ERP avec l’option <a href="../../developer/reference/cli#cmdoption-odoo-bin-x-sendfile"><code>--x-sendfile</code></a> et naviguez vers l’URL <code>/web/filestore</code> directement via Konvergo ERP (ne naviguez pas vers l’URL via NGINX). Ceci enregistre un avertissement, le message contient la configuration dont vous avez besoin.</p>
</li>
</ul>
</div>

## Sécurité

Pour commencer, gardez à l’esprit que la sécurisation d’un système
d’information est un processus continu, et non une opération ponctuelle. À
tout moment, votre sécurité ne sera que celle du maillon le plus faible de
votre environnement.

Ne considérez donc pas cette section comme une liste exhaustive des mesures
qui permettront d’éviter tous les problèmes de sécurité. Il s’agit uniquement
d’un récapitulatif des premiers éléments importants que vous devez inclure
dans votre plan d’action en matière de sécurité. Le reste viendra des
meilleures pratiques de sécurité pour votre système d’exploitation et votre
distribution, des meilleures pratiques en termes d’utilisateurs, de mots de
passe et de gestion du contrôle d’accès, etc.

Lors du déploiement d’un serveur exposé sur internet, veillez à prendre en
compte les sujets suivants liés à la sécurité :

  * Définissez toujours un mot de passe administrateur super-admin fort et limitez l’accès aux pages d’administration de la base de données dès que le système est configuré. Consultez Sécurité du gestionnaire de bases de données.

  * Choisissez des identifiants uniques et des mots de passe forts pour tous les comptes administrateurs de toutes les bases de données. N’utilisez pas « admin » comme identifiant. N’utilisez pas ces identifiants pour les opérations quotidiennes, mais uniquement pour contrôler/gérer l’installation. N’utilisez _jamais_ de mots de passe par défaut comme admin/admin, même pour les bases de données de test/simulation.

  * N’installez **pas** de données de démonstration sur des serveurs exposés sur internet. Les bases de données contenant des données de démonstration contiennent des identifiants et des mots de passe par défaut qui peuvent être utilisés pour s’introduire dans vos systèmes et causer des problèmes importants, même sur les systèmes de simulation/développement.

  * Utilisez les filtres de base de données appropriés ([`--db-filter`](../../developer/reference/cli#cmdoption-odoo-bin-db-filter)) pour limiter la visibilité de vos bases de données en fonction du nom d’hôte. Consultez dbfilter. Vous pouvez également utiliser [`-d`](../../developer/reference/cli#cmdoption-odoo-bin-d) pour fournir votre propre liste (séparée par des virgules) de bases de données disponibles à filtrer, au lieu de laisser le système les récupérer toutes depuis le backend de la base de données.

  * Une fois que vos `db_name` et `db_filter` sont configurés et ne correspondent qu’à une seule base de données par nom d’hôte, vous devez définir l’option de configuration `list_db` sur `False`, pour empêcher de lister entièrement des bases de données, et pour bloquer l’accès aux pages d’administration des bases de données (ceci est aussi exposé comme l’option de ligne de commande [`--no-database-list`](../../developer/reference/cli#cmdoption-odoo-bin-no-database-list))

  * Assurez-vous que l’utilisateur PostgreSQL ([`--db_user`](../../developer/reference/cli#cmdoption-odoo-bin-r)) n’est _pas_ un super-utilisateur, et que vos bases de données appartiennent à un autre utilisateur. Par exemple, elles pourraient appartenir au super-utilisateur `postgres` si vous utilisez un `db_user` dédié et non privilégié. Consultez aussi Configurer Konvergo ERP.

  * Maintenez vos installations à jour en installant régulièrement les dernières versions, soit via GitHub, soit en téléchargeant la dernière version sur <https://www.odoo.com/page/download> ou <http://nightly.odoo.com>.

  * Configurez votre serveur en mode multi-process avec des limites appropriées correspondant à votre utilisation typique (mémoire/CPU/délais d’attente). Consultez aussi Serveur intégré.

  * Exécutez Konvergo ERP derrière un serveur web fournissant une terminaison HTTPS avec un certificat SSL valide, afin d’empêcher l’écoute des communications en texte clair. Les certificats SSL sont bon marché et il existe de nombreuses options gratuites. Configurez le proxy web pour limiter la taille des requêtes, définissez des délais d’attente appropriés, puis activez l’option [`mode proxy`](../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode). Consultez aussi HTTPS.

  * Si vous devez autoriser un accès SSH distant à vos serveurs, assurez-vous de définir un mot de passe fort pour **tous** les comptes, et pas seulement pour `root`. Il est fortement recommandé de désactiver complètement l’authentification par mot de passe et de n’autoriser que l’authentification par clé publique. Pensez également à restreindre l’accès via un VPN, à n’autoriser que les IP de confiance dans le pare-feu, et/ou à utiliser un système de détection par force brute tel que `fail2ban` ou équivalent.

  * Pensez à installer une limitation de débit appropriée sur votre proxy ou votre pare-feu, afin d’empêcher les attaques par force brute et les attaques par déni de service. Consultez aussi Bloquer des attaques par force brute pour des mesures spécifiques.

De nombreux fournisseurs de réseaux proposent une atténuation automatique des
attaques par déni de service distribué (DDOS), mais il s’agit souvent d’un
service facultatif, que vous devez donc consulter.

  * Dans la mesure du possible, hébergez vos instances de démonstration/test/simulation destinées au public sur des appareils différents de ceux de production. Et appliquez les mêmes précautions de sécurité que pour la production.

  * Si votre serveur Konvergo ERP destiné au public a accès à des ressources ou des services réseau internes sensibles (par ex. via un VLAN privé), mettez en place des règles de pare-feu appropriées pour protéger ces ressources internes. Cela garantira que le serveur Konvergo ERP ne peut pas être utilisé accidentellement (ou à la suite d’actions malveillantes d’utilisateurs) pour accéder à ces ressources internes ou les perturber. Typiquement, cela peut être fait en appliquant une règle DENY par défaut sur le pare-feu, puis en autorisant explicitement l’accès aux ressources internes auxquelles le serveur Konvergo ERP doit accéder. Il est également possible d’utiliser [Systemd IP traffic access control](http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd) pour mettre en place un contrôle d’accès réseau par processus.

  * Si votre serveur Konvergo ERP destiné au public se trouve derrière un pare-feu d’application web, un équilibreur de charge, un service de protection DDoS transparent (comme CloudFlare) ou un dispositif similaire au niveau du réseau, vous souhaiteriez peut-être éviter l’accès direct au système Konvergo ERP. Il est généralement difficile de garder secrètes les adresses IP des points de terminaison de vos serveurs Konvergo ERP. Par exemple, elles peuvent apparaître dans les journaux des serveurs web lors de l’interrogation de systèmes publics ou dans les en-têtes des emails envoyés depuis Konvergo ERP. Dans une telle situation, vous pouvez configurer votre pare-feu de sorte que les points de terminaison ne soient pas accessibles publiquement, sauf à partir des adresses IP spécifiques de votre WAF, de votre équilibreur de charge ou de votre service de proxy. Les fournisseurs de services comme CloudFlare conservent généralement une liste publique de leurs plages d’adresses IP à cette fin.

  * Si vous hébergez plusieurs clients, isolez les données et les fichiers des clients les uns des autres en utilisant des conteneurs ou des techniques de « prison » appropriées.

  * Configurez des sauvegardes quotidiennes de vos bases de données et des données de votre filestore et copiez-les sur un serveur d’archivage distant qui n’est pas accessible depuis le serveur lui-même.

  * Il est fortement recommandé de déployer Konvergo ERP sur Linux au lieu de Windows. Si vous choisissez toutefois de déployer Konvergo ERP sur une plateforme Windows, un examen détaillé du renforcement de la sécurité du serveur doit être effectué et n’entre pas dans le cadre de ce guide.

### Bloquer des attaques par force brute

Pour les déploiements exposés sur internet, les attaques par force brute sur
les mots de passe des utilisateurs sont très fréquentes et cette menace ne
doit pas être négligée pour les serveurs Konvergo ERP. Konvergo ERP émet une entrée de journal
chaque fois qu’une tentative de connexion est effectuée et rapporte le
résultat : réussite ou échec, ainsi que le login cible et l’IP source.

Les entrées du journal auront la forme suivante.

Connexion échouée :

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1
    

Connexion réussie :

    
    
    2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login successful for db:db_name login:admin from 127.0.0.1
    

Ces journaux peuvent être facilement analysés par un système de prévention des
intrusions tel que `fail2ban`.

Par exemple, la définition suivante du filtre fail2ban devrait correspondre à
une connexion échouée :

    
    
    [Definition]
    failregex = ^ \d+ INFO \S+ \S+ Login failed for db:\S+ login:\S+ from <HOST>
    ignoreregex =
    

Ceci pourrait être utilisé avec une définition de prison pour bloquer l’IP
attaquant sur HTTP(S).

Voici à quoi cela pourrait ressembler pour bloquer l’IP pendant 15 minutes
lorsque 10 tentatives de connexion échouées sont détectées à partir de la même
adresse IP en 1 minute :

    
    
    [odoo-login]
    enabled = true
    port = http,https
    bantime = 900  ; 15 min ban
    maxretry = 10  ; if 10 attempts
    findtime = 60  ; within 1 min  /!\ Should be adjusted with the TZ offset
    logpath = /var/log/odoo.log  ;  set the actual odoo log path here
    

### Sécurité du gestionnaire de bases de données

Configurer Konvergo ERP a mentionné en passant `admin_passwd`.

Ce paramètre est utilisé sur toutes les pages d’administration de la base de
données (pour créer, supprimer, vider ou restaurer des bases de données).

Si les pages d’administration ne doivent pas être accessibles du tout, vous
devez définir l’option de configuration `list_db` sur `False` pour bloquer
l’accès à toutes les pages d’administration et de sélection des bases de
données.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Il est fortement recommandé de désactiver le Gestionnaire de bases de données pour tout système exposé sur internet ! Il est conçu comme un outil de développement/démonstration, pour faciliter la création et la gestion rapides de bases de données. Il n’est pas conçu pour être utilisé en production et peut même exposer des fonctionnalités dangereuses aux attaquants. Il n’est pas non plus conçu pour gérer des bases de données volumineuses et peut déclencher des limites de mémoire.</p>
<p>Sur les systèmes de production, les opérations de gestion des bases de données doivent toujours être effectuées par l’administrateur système, y compris l’approvisionnement de nouvelles bases de données et les sauvegardes automatiques.</p>
</div>

Assurez-vous de configurer un paramètre `db_name` approprié (et
optionnellement `db_filter` aussi) afin que le système puisse déterminer la
base de données cible pour chaque requête, sinon les utilisateurs seront
bloqués, car ils ne seront pas autorisés à choisir la base de données eux-
mêmes.

Si les pages d’administration ne doivent être accessibles qu’à partir d’un
ensemble d’appareils sélectionnés, utilisez les fonctionnalités du serveur
proxy pour bloquer l’accès à toutes les routes commençant par `/web/database`
sauf (peut-être) `/web/database/selector` qui affiche la page de sélection de
la base de données.

Si la page d’administration de la base de données doit rester accessible, le
paramètre `admin_passwd` doit être modifié par rapport à sa valeur par défaut
`admin` : ce mot de passe est vérifié avant d’autoriser les opérations de
modification de la base de données.

Il doit être stocké en toute sécurité et doit être généré de manière
aléatoire, par ex.

    
    
    $ python3 -c 'import base64, os; print(base64.b64encode(os.urandom(24)))'
    

which generates a 32-character pseudorandom printable string.

### Reset the master password

There may be instances where the master password is misplaced, or compromised,
and needs to be reset. The following process is for system administrators of
an Konvergo ERP on-premise database detailing how to manually reset and re-encrypt the
master password.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p>For more information about changing an Konvergo ERP.com account password, see this documentation:
<a href="../odoo_accounts#odoocom-change-password"><span class="std std-ref">Changer le mot de passe du compte Konvergo ERP.com</span></a>.</p>
</div>

When creating a new on-premise database, a random master password is
generated. Konvergo ERP recommends using this password to secure the database. This
password is implemented by default, so there is a secure master password for
any Konvergo ERP on-premise deployment.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>When creating an Konvergo ERP on-premise database the installation is accessible to anyone on the
internet, until this password is set to secure the database.</p>
</div>

The master password is specified in the Konvergo ERP configuration file (`odoo.conf`
or `odoorc` (hidden file)). The Konvergo ERP master password is needed to modify,
create, or delete a database through the graphical user interface (GUI).

#### Locate configuration file

First, open the Konvergo ERP configuration file (`odoo.conf` or `odoorc` (hidden
file)).

WindowsLinux

The configuration file is located at:
`c:\ProgramFiles\Konvergo ERP{VERSION}\server\odoo.conf`

Depending on how Konvergo ERP is installed on the Linux machine, the configuration
file is located in one of two different places:

  * Package installation: `/etc/odoo.conf`

  * Source installation: `~/.odoorc`

#### Change old password

Once the appropriate file has been opened, proceed to modify the old password
in the configuration file to a temporary password.

Graphical user interfaceCommand-line interface

After locating the configuration file, open it using a (GUI). This can be
achieved by simply double clicking on the file. Then, the device should have a
default GUI to open the file with.

Next, modify the master password line `admin_passwd = $pbkdf2-sha…` to
`admin_passwd = newpassword1234`, for example. This password can be anything,
as long as it is saved temporarily. Make sure to modify all characters after
the `=`.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>The line appears like this:
<code>admin_passwd =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m</code></p>
<p>The modified line appears like this: <code>admin_passwd = newpassword1234</code></p>
</div>

Modify the master password line using the following Unix command detailed
below.

Connect to the Konvergo ERP server’s terminal via Secure Shell (SSH) protocol, and
edit the configuration file. To modify the configuration file, enter the
following command: **sudo nano /etc/odoo.conf**

After opening the configuration file, modify the master password line
`admin_passwd = $pbkdf2-sha…` to `admin_passwd = newpassword1234`. This
password can be anything, as long as it is saved temporarily. Make sure to
modify all characters after the `=`.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>0

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>1

#### Restart Konvergo ERP server

After setting the temporary password, a restart of the Konvergo ERP server is
**required**.

Graphical user interfaceCommand-line interface

To restart the Konvergo ERP server, first, type `services` into the Windows **Search**
bar. Then, select the **Services** application, and scroll down to the
**Konvergo ERP** service.

Next, right click on **Konvergo ERP** , and select **Start** or **Restart**. This
action manually restarts the Konvergo ERP server.

Restart the Konvergo ERP server by typing the command: **sudo service odoo15 restart**

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>2

#### Use web interface to re-encrypt password

First, navigate to `/web/database/manager` or
`http://server_ip:port/web/database/manager` in a browser.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>3

Next, click **Set Master Password** , and type in the previously-selected
temporary password into the **Master Password** field. Following this step,
type in a **New Master Password**. The **New Master Password** is hashed (or
encrypted), once the **Continue** button is clicked.

At this point, the password has been successfully reset, and a hashed version
of the new password now appears in the configuration file.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>4

## Navigateurs pris en charge

Konvergo ERP prend en charge tous les principaux navigateurs d’ordinateur de bureau et
portable disponibles sur le marché, pour autant qu’ils soient pris en charge
par leurs éditeurs.

Voici les navigateurs pris en charge :

  * Google Chrome

  * Mozilla Firefox

  * Microsoft Edge

  * Apple Safari

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>5 <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La configuration d’un <a href="../../developer/reference/cli#cmdoption-odoo-bin-db-filter"><code>--db-filter</code></a> approprié est une partie importante de la sécurisation de votre déploiement. Une fois qu’il fonctionne correctement et qu’il ne correspond qu’à une seule base de données par nom d’hôte, il est fortement recommandé de bloquer l’accès aux pages d’administration des bases de données et d’utiliser le paramètre de démarrage <code>--no-database-list</code> pour empêcher l’énumération de vos bases de données et bloquer l’accès aux pages d’administration de la base de données. Consultez également <a href="#id9">sécurité</a>.</p>
</div>6

1

    

pour que plusieurs installations Konvergo ERP utilisent la même base de données
PostgreSQL ou pour fournir plus de ressources informatiques aux deux
logiciels.

2

    

techniquement, un outil tel que [socat](http://www.dest-unreach.org/socat/)
peut être utilisé pour transmettre les sockets UNIX à travers les réseaux,
mais il s’agit principalement de logiciels qui ne peuvent être utilisés que
sur des sockets UNIX.

3

    

ou n’être accessible que sur un réseau interne à commutation de paquets, mais
cela nécessite des commutateurs sécurisés, des protections contre le [ARP
spoofing](https://en.wikipedia.org/wiki/ARP_spoofing) et exclut l’utilisation
du WiFi. Même sur des réseaux à commutation de paquets sécurisés, le
déploiement sur HTTPS est recommandé et les coûts éventuels sont réduits, car
les certificats « auto-signés » sont plus faciles à déployer dans un
environnement contrôlé que sur internet.

  *[GUI]: graphical user interface

