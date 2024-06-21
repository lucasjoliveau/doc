# Certificat HTTPS (IoT)

## Qu’est-ce que HTTPS ?

Le protocole _Hypertext Transfer Protocol Secure_ (HTTPS ou, littéralement,
protocole de transfert hypertextuel sécurisé) est la version sécurisée de
_Hypertext Transfer Protocol_ (HTTP ou, littéralement, protocole de transfert
hypertextuel), qui est le protocole principal utilisé pour échanger des
données entre un navigateur web et un site web. HTTPS est chiffré afin
d’accroître la sécurité du transfert de données.

Le protocole HTTPS utilise un protocole de chiffrement permettant de chiffrer
les communications. Ce protocole s’appelle _Transport Layer Security_ (TLS),
connu auparavant sous le nom de _Secure Sockets Layer_ (SSL).

Le protocole HTTPS repose sur la transmission de certificats TLS/SSL, qui
permettent de vérifier qu’un fournisseur donné est bien celui qu’il prétend
être.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans cette documentation et dans tout Konvergo ERP, le terme « certificat HTTPS » sera utilisé pour définir le fait que le certificat <abbr title="Secure Sockets Layer">SSL</abbr> est valide et permet une connexion <abbr title="Hypertext Transfer Protocol Secure">HTTPS</abbr>.</p>
</div>

### Pourquoi est-ce nécessaire ?

Afin de communiquer avec certains périphériques réseau (plus particulièrement
pour les terminaux de paiement), l’utilisation de HTTPS est obligatoire. Si le
certificat HTTPS n’est pas valide, certains périphériques ne pourront pas
interagir avec l”IoT Box.

## Comment obtenir un certificat Hypertext Transfer Protocol Secure (HTTPS)

La génération du certificat HTTPS est automatique.

L”IoT Box enverra une requête spécifique à <https://www.odoo.com> qui renverra
le certificat HTTPS si l”IoT box et la base de données sont éligibles.

### Éligibilité à l’Internet des objets (IoT)

>   1. La base de données doit être une instance de **production**. L’instance
> de la base de données ne doit pas être une copie, un doublon, un
> environnement de simulation ou de développement.
>
>   2. L’abonnement Konvergo ERP doit :
>

>>      * Avoir une ligne **Abonnement IoT Box**.

>>

>>      * Le **Statut** doit être **En cours**.

>
> Si l’abonnement est lié à un utilisateur du portail <https://www.odoo.com>,
> vérifiez les informations sur la page d’abonnement du portail.
>
> ![Les abonnements dans le portail Konvergo ERP.com filtrés par "en
> cours".](../../../../_images/sub-example-in-progress.png)
>
> Dans ce cas, les deux abonnements sont considérés comme étant « en cours »,
> car le filtre **Filtrer par: En cours** a été utilisé.
>
> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si l’abonnement est en question, contactez le gestionnaire de compte ou le partenaire de la base de données à ce sujet.</p>
</div>
>

## Dépannage des erreurs de certificat Hypertext Transfer Protocol Secure
(HTTPS)

Si un problème survient au cours du processus de génération ou de réception du
« certificat HTTPS », un code d’erreur spécifique est indiqué sur la page
d’accueil de l”IoT box.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>L’accès à la page d’accueil de l”<abbr title="Internet of Things">IoT</abbr> box permet de vérifier la présence du « certificat HTTPS » et de tenter de le générer s’il est manquant. Par conséquent, en cas d’erreur sur la page d’accueil de l”<abbr title="Internet of Things">IoT</abbr>, actualisez la page d’accueil de l”<abbr title="Internet of Things">IoT</abbr> pour voir si l’erreur disparaît.</p>
</div>

### `ERR_IOT_HTTPS_CHECK_NO_SERVER`

Motif :

    

La configuration concernant le serveur est manquante. En d’autres termes,
l’instance Konvergo ERP n’est pas connectée à l’IoT Box.

Solution :

    

Assurez-vous que le serveur est configuré.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="connect">Connecter une IoT box à Konvergo ERP</a></p>
</div>

### `ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`

Motif :

    

Une erreur non gérée s’est produite lors de la lecture du certificat HTTPS.

Solution :

    

Assurez-vous que le fichier de certificat HTTPS est lisible.

### `ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`

Motif :

    

L”UUID du contrat et/ou de la base de données est manquant.

Solution :

    

Assurez-vous que les deux valeurs sont configurées comme prévu. Pour les
modifier, allez à la page d’accueil de l”IoT box et naviguez jusqu’à
**Credential**.

### `ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`

Motif :

    

Une erreur inattendue s’est produite lorsque l”IoT box a essayé d’atteindre
<https://www.odoo.com>. Les causes sont probablement dues à
l’infrastructure/configuration du réseau :

>   * L”IoT box n’a pas accès à Internet.
>
>   * Le réseau ne permet pas à l”IoT box de communiquer avec
> <https://www.odoo.com>. Cela peut être dû à des périphériques réseau
> empêchant la communication (pare-feu, etc.) ou à la configuration du réseau
> (VPN, etc.).
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>De plus amples informations concernant l’erreur qui s’est produite peuvent être trouvées dans les détails complets de l’exception de la requête, qui se trouvent dans les journaux de l”<abbr title="Internet of Things">IoT</abbr> box.</p>
</div>

Solution :

    <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Consultez votre administrateur système ou réseau si ce problème survient. Ce code d’erreur dépend de l’infrastructure du réseau et dépasse la portée du service d’assistance d’Konvergo ERP.</p>
</div> 

### `ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`

Motif :

    

L’IoT Box a pu atteindre <https://www.odoo.com> mais a reçu une [réponse HTTP
inhabituelle (codes de statut)](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Status).

Ce code d’erreur indique également des codes de statut de la réponse HTTP. Par
exemple, si l’erreur indique `ERR_IOT_HTTPS_LOAD_REQUEST_STATUS 404`, cela
signifie que la page a renvoyé une erreur 404, c’est-à-dire le code « Page
introuvable ».

Solution :

    

Vérifiez si <https://www.odoo.com> est hors service à l’aide d’un navigateur
web, car il est possible qu’il soit hors service pour cause de maintenance.

>   * Si <https://www.odoo.com> est hors service pour cause de maintenance, il
> n’y a malheureusement rien à faire. Il faut attendre qu’il se rétablisse.
>
>   * Si <https://www.odoo.com> n’est pas hors service pour cause de
> maintenance, ouvrez un [ticket d’assistance](https://www.odoo.com/help) à ce
> sujet. Assurez-vous que le code de statut à 3 chiffres à côté du code
> d’erreur figure dans le ticket d’assistance.
>
>

### `ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`

Motif :

    

L”IoT box a pu atteindre <https://www.odoo.com> mais a refusé de délivrer le
certificat HTTPS.

Solution :

    

Assurez-vous que l”IoT box et la base de données sont éligibles pour un
certificat : Éligibilité à l’Internet des objets (IoT).

## Comment s’assurer que le certificat HTTPS est correct

Si le certificat a été appliqué avec succès, une nouvelle URL HTTPS pour l”IoT
box se terminant par `.odoo-iot.com` apparaîtra dans la base de données Konvergo ERP,
à l’intérieur de l’application IoT sur le formulaire de ce périphérique
spécifique.

![IoT Box sur l'application IoT Konvergo ERP avec le domaine .odoo-
iot.com.](../../../../_images/odoo-new-domain.png)

Lors de la navigation vers l”URL dans un navigateur, une connexion sécurisée
HTTPS sera établie.

![Exemple de détails d'un certificat SSL valide sur le
navigateur.](../../../../_images/secured-connection.png)

Cadenas dans Chrome dans Windows 10 attestant que la connexion est sécurisée
dans HTTPS.

La page d’accueil de l’IoT Box affiche désormais un statut `OK` à côté du
`certificat HTTPS`. En cliquant sur l’icône du menu déroulant, vous obtiendrez
des informations sur le certificat.

![Page d'accueil de l'IoT Box avec le statut OK du certificat
HTTPS.](../../../../_images/status-ok.png)

## Problème de Domain Name System (DNS)

Si l”IoT box est accessible à partir de son adresse IP, mais pas à partir du
domaine attribué par Konvergo ERP : `.odoo-iot.com` ; ensuite, il est probable que
l”IoT box rencontre un problème de DNS (système de nom de domaine). Sur
certains navigateurs, un code d’erreur mentionnant DNS (like
`DNS_PROBE_FINISHED_NXDOMAIN`) sera affiché.

Ces problèmes de DNS peuvent apparaître comme suit dans différents navigateurs
:

ChromeFirefoxEdge

![Problème DNS dans le navigateur Chrome sous Windows
10.](../../../../_images/dns-chrome.png)

Problème DNS dans le navigateur Chrome sous Windows 10.

![Problème DNS dans le navigateur Firefox sous Windows
10.](../../../../_images/dns-firefox.png)

Problème DNS dans le navigateur Firefox sous Windows 10.

![Problème DNS dans la navigateur Edge sous Windows
10.](../../../../_images/dns-edge.png)

Problème DNS dans la navigateur Edge sous Windows 10.

### Solution au problème de Domain Name System (DNS)

  1. Si le routeur permet de modifier manuellement le DNS, changez le DNS pour utiliser [Google DNS](https://developers.google.com/speed/public-dns).

  2. Si votre routeur ne le permet pas, il faudra modifier les paramètres DNS de chaque périphérique utilisant [Google DNS](https://developers.google.com/speed/public-dns). Cette opération doit être effectuée sur **chaque** périphérique qui prévoit d’interagir avec l”IoT box (par ex. ordinateur, tablette ou téléphone). Les processus de configuration de chaque périphérique figurent sur le site web du fabricant du périphérique.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il ne sera probablement pas nécessaire de modifier les paramètres <abbr title="Domain Name System">DNS</abbr> d’autres périphériques <abbr title="Internet of Things">IoT</abbr>, tels que les terminaux de paiement, car ils sont déjà configurés avec un <abbr title="Domain Name System">DNS</abbr> personnalisé.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Consultez votre administrateur système ou réseau si ce problème survient. Ce code d’erreur dépend de l’infrastructure du réseau et dépasse la portée du service d’assistance d’Konvergo ERP.</p>
</div>

  *[HTTPS]: Hypertext Transfer Protocol Secure
  *[TLS]: Transport Layer Security
  *[SSL]: Secure Sockets Layer
  *[IoT]: Internet of Things
  *[UUID]: Universal Unique Identifier
  *[VPN]: Virtual Private Network
  *[URL]: Uniform Resource Locator
  *[IP]: Internet Protocol
  *[DNS]: Domain Name System

