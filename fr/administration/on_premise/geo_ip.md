# GeoIP

Note

Cette documentation s’applique uniquement aux bases de données on-premise.

## Installation

Avertissement

Veuillez noter que l’installation dépend du système d’exploitation et de la
distribution de votre ordinateur. Nous supposons que vous utilisez un système
d’exploitation Linux.

  1. Installer la bibliothèque Python de [geoip2](https://pypi.org/project/geoip2/)
    
    
        pip install geoip2
    

  2. Télécharger la [base de données GeoLite2 City](https://dev.maxmind.com/geoip/geoip2/geolite2/). Vous devriez obtenir un fichier appelé « GeoLite2-City.mmdb ».

  3. Déplacer le fichier vers le dossier `/usr/share/GeoIP/`
    
    
        mv ~/Downloads/GeoLite2-City.mmdb /usr/share/GeoIP/
    

  4. Redémarrer le serveur

Note

Si vous ne pouvez/voulez pas localiser la base de données GeoIP dans
`/usr/share/GeoIP/`, vous pouvez utiliser l’option `--geoip-db` de l’interface
de ligne de commande de Odoo. Cette option prend le chemin absolu vers le
fichier de la base de données GeoIP et l’utilise comme base de données GeoIP.
Par exemple :

    
    
    ./odoo-bin --geoip-db= ~/Downloads/GeoLite2-City.mmdb
    

Pour plus d'infos

  * [documentation CLI](../../developer/reference/cli.html).

Avertissement

La bibliothèque Python `GeoIP` peut également être utilisée. Cependant cette
version est abandonnée depuis le 1er janvier. Voir [Les bases de données
GeoLite Legacy sont désormais
abandonnées.](https://support.maxmind.com/geolite-legacy-discontinuation-
notice/)

## Comment tester la géolocalisation GeoIP dans votre site web Odoo

  1. Allez à votre site web. Ouvrez la page web sur laquelle vous voulez tester `GeoIP`.

  2. Choisissez Personnaliser ‣ HTML/CSS/JS Editor.

  3. Ajoutez l’élément XML suivant dans la page :

    
    
    <h1 class="text-center" t-esc="request.session.get('geoip')"/>
    

Vous devriez vous retrouver avec un dictionnaire indiquant l’emplacement de
l’adresse IP.

![../../_images/on-premise_geo-ip-installation01.png](../../_images/on-
premise_geo-ip-installation01.png)

Note

Si les accolades sont vides `{}`, cela peut être pour l’une des raisons
suivantes :

  * L’adresse IP de navigation est le localhost (127.0.0.1) ou un réseau local (192.168.*.*).

  * Si un proxy inversé est utilisé, assurez-vous de le configurer correctement. Voir [`mode proxy`](../../developer/reference/cli.html#cmdoption-odoo-bin-proxy-mode).

  * `geoip2` n’est pas installé ou le fichier de la base de données GeoIP n’a pas été trouvé

  * La base de données GeoIP n’a pas pu résoudre l’adresse IP donnée.

