# Configurer un réseau de diffusion de contenu (CDN)

## Déployer avec KeyCDN

Un CDN ou _réseau de diffusion de contenu_ est un réseau de serveurs
distribués géographiquement qui fournit du contenu interne à haut débit. Le
CDN fournit un contenu rapide et de haute qualité pour les sites web à fort
contenu.

Ce document vous guidera dans la configuration d’un compte
[KeyCDN](https://www.keycdn.com) avec un site web généré par Konvergo ERP.

### Créer une pull zone dans le tableau de bord KeyCDN

Sur le tableau de bord KeyCDN, commencez par naviguer vers l’élément de menu
Zones sur la gauche. Sur le formulaire, complétez le champ **Zone Name** , qui
apparaîtra dans l”URL du CDN. Ensuite, définissez le **Zone Status** sur
**active** pour activer la zone. En ce qui concerne le **Zone Type** ,
définissez la valeur sur **Pull** , et, enfin, sous les **Pull Settings** ,
saisissez **Origin URL** — cette adresse doit être l”URL complète de la base
de données Konvergo ERP.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Utilisez <code>https://yourdatabase.odoo.com</code> et remplacez le préfixe du sous-domaine <em>yourdatabase</em> par le nom de la base de données. Il est également possible d’utiliser une <abbr title="Uniform Resource Locator">URL</abbr> personnalisée, au lieu du sous-domaine Konvergo ERP qui est donné à la base de données.</p>
</div> ![Page de configuration de la Zone de
KeyCDN.](../../../../_images/keycdn-zone.png)

Dans la rubrique **Paramètres généraux** sous le formulaire de zone, cliquez
sur le bouton **Show all settings** pour développer les options de la zone. Il
doit s’agir de la dernière option de la page. Après avoir développé les
**Paramètres généraux** , assurez-vous que l’option **CORS** est **activée**.

Ensuite, descendez au bas de la page de configuration de la zone et
**enregistrez** les changements. KeyCDN indiquera que la nouvelle zone sera
déployée. Cela peut prendre environ 10 minutes.

![KeyCDN en train de déployer la nouvelle Zone.](../../../../_images/zone-
url.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une nouvelle <b>Zone URL</b> a été générée pour votre Zone. Dans cet exemple, il s’agit de <code>pulltest-xxxxx.kxcdn.com</code>. Cette valeur sera différente pour chaque base de données.</p>
</div>

Copiez cette **Zone URL** dans un éditeur de texte pour plus tard, car vous
devrez l’utiliser dans les étapes suivantes.

### Configurer l’instance Konvergo ERP avec la nouvelle zone

In the Konvergo ERP **Website** app, go to the Settings and then activate the
**Content Delivery Network (CDN)** setting and copy/paste the **Zone URL**
value from the earlier step into the **CDN Base URL** field. This field is
only visible and configurable when the [developer
mode](../../../general/developer_mode#developer-mode) is activated.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Veillez à ce qu’il y ait deux <em>barres obliques</em> (<code>//</code>) avant la valeur <b>CDN Base URL</b> et une barre oblique (<code>/</code>) après la valeur <b>CDN Base URL</b>.</p>
</div>

**Enregistrez** les paramètres une fois qu’ils sont complétés.

![Activation du paramètre CDN dans Konvergo ERP.](../../../../_images/cdn-base-
url.png)

Le site web utilise désormais le CDN pour les ressources correspondant aux
expressions régulières des **filtres CDN**.

Dans le HTML du site web Konvergo ERP, l’intégration du CDN est prouvée comme
fonctionnant correctement en vérifiant l”URL des images. La valeur _CDN Base
URL_ peut être consultée en utilisant la fonctionnalité **Inspecter** de votre
navigateur web sur le site web d’Konvergo ERP. Recherchez son enregistrement dans
l’onglet **Network** à l’intérieur de devtools.

![La valeur CDN Base URL peut être consultée à l'aide de la fonction Inspecter
du site web d'Konvergo ERP.](../../../../_images/test-pull.png)

### Prévenir les problèmes de sécurité en activant le partage des ressources
entre origines multiples (CORS)

Une restriction de sécurité dans certains navigateurs (tels que Mozilla
Firefox et Google Chrome) empêche un fichier CSS lié à distance d’aller
récupérer des ressources relatives sur ce même serveur externe.

Si l’option CORS n’est pas activée dans la **Zone CDN** , le problème le plus
évident sur un site web Konvergo ERP standard sera l’absence d’icônes _Font Awesome_
parce que le fichier de police déclaré dans le CSS _Font Awesome_ ne sera pas
chargé à partir du serveur distant.

Lorsque ces problèmes de ressources entre origines multiples se produisent, un
message d’erreur de sécurité similaire à l’exemple ci-dessous apparaîtra dans
la console de développement du navigateur web :

`Font from origin 'http://pulltest-xxxxx.kxcdn.com' has been blocked from
loading /shop:1 by Cross-Origin Resource Sharing policy: No 'Access-Control-
Allow-Origin' header is present on the requested resource. Origin
'http://yourdatabase.odoo.com' is therefore not allowed access.`

![Message d'erreur affiché dans la console du
navigateur.](../../../../_images/odoo-security-message.png)

L’activation de l’option CORS dans les paramètres de CDN règle ce problème.

  *[CDN]: Content Delivery Network
  *[URL]: Uniform Resource Locators
  *[CORS]: Cross-Origin Resource Sharing

