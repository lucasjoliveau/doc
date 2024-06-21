# GeoIP

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Cette documentation s’applique uniquement aux bases de données on-premise.</p>
</div>

## Installation

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Veuillez noter que l’installation dépend du système d’exploitation et de la distribution de votre ordinateur. Nous supposons que vous utilisez un système d’exploitation Linux.</p>
</div>

  1. Installer la bibliothèque Python de [geoip2](https://pypi.org/project/geoip2/)
    
    
        pip install geoip2
    

  2. Télécharger la [base de données GeoLite2 City](https://dev.maxmind.com/geoip/geoip2/geolite2/). Vous devriez obtenir un fichier appelé « GeoLite2-City.mmdb ».

  3. Déplacer le fichier vers le dossier `/usr/share/GeoIP/`
    
    
        mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
    

  4. Redémarrer le serveur

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous ne pouvez/voulez pas localiser la base de données GeoIP dans <code>/usr/share/GeoIP/</code>, vous pouvez utiliser l’option <code>--geoip-db</code> de l’interface de ligne de commande de Konvergo ERP. Cette option prend le chemin absolu vers le fichier de la base de données GeoIP et l’utilise comme base de données GeoIP. Par exemple :</p>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>./odoo-bin --geoip-db<span class="o">=</span> ~/Downloads/GeoLite2-City.mmdb
</pre></div>
</div>
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../developer/reference/cli">documentation CLI</a>.</p></li>
</ul>
</div>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>La bibliothèque Python <code>GeoIP</code> peut également être utilisée. Cependant cette version est abandonnée depuis le 1er janvier. Voir <a href="https://support.maxmind.com/geolite-legacy-discontinuation-notice/">Les bases de données GeoLite Legacy sont désormais abandonnées.</a></p>
</div>

## Comment tester la géolocalisation GeoIP dans votre site web Konvergo ERP

  1. Allez à votre site web. Ouvrez la page web sur laquelle vous voulez tester `GeoIP`.

  2. Choisissez Personnaliser ‣ HTML/CSS/JS Editor.

  3. Ajoutez l’élément XML suivant dans la page :

    
    
    <h1 class="text-center" t-esc="request.session.get('geoip')"/>
    

Vous devriez vous retrouver avec un dictionnaire indiquant l’emplacement de
l’adresse IP.

![../../_images/on-premise_geo-ip-installation01.png](../../_images/on-
premise_geo-ip-installation01.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si les accolades sont vides <code>{}</code>, cela peut être pour l’une des raisons suivantes :</p>
<ul>
<li><p>L’adresse IP de navigation est le localhost (127.0.0.1) ou un réseau local (192.168.*.*).</p></li>
<li><p>Si un proxy inversé est utilisé, assurez-vous de le configurer correctement. Voir <a href="../../developer/reference/cli#cmdoption-odoo-bin-proxy-mode"><code>mode proxy</code></a>.</p></li>
<li><p><code>geoip2</code> n’est pas installé ou le fichier de la base de données GeoIP n’a pas été trouvé</p></li>
<li><p>La base de données GeoIP n’a pas pu résoudre l’adresse IP donnée.</p></li>
</ul>
</div>

