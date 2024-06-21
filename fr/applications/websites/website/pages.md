# Pages

Konvergo ERP vous permet de créer des pages pour votre site web et de personnaliser
leur contenu et leur apparence selon vos besoins.

**Static** pages have stable content, such as the homepage. You can manually
create new ones, define their URLs, adapt their properties, etc. **Dynamic**
pages, on the other hand, are generated dynamically. All pages generated
automatically by Konvergo ERP, for example, when you install an app or module (e.g.,
`/shop` or `/blog`) or publish a new product or blog post, are dynamic pages
and are therefore managed differently.

## Création de pages

Les pages du site web peuvent être créées à partir du **frontend** et du
**backend**. Pour créer une nouvelle page du site web, suivez les étapes
suivantes :

>   1.      * Ouvez l’application **Site Web** , cliquez sur **\+ Nouveau**
> dans le coin supérieur droit, puis sélectionnez **Page** ;
>
>      * Ou allez à Site Web ‣ Site ‣ Pages et cliquez sur **Nouveau**.
>
>   2. Enter a **Page Title** ; this title is used in the menu and the page’s
> URL.
>
>   3. Cliquez sur **Créer**.
>
>   4. Personnalisez le contenu et l’apparence de la page en utilisant le
> constructeur de site web, puis cliquez sur **Enregistrer**.
>
>   5. Publiez la page.
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Désactivez l’option <b>Ajouter au menu</b> si la page ne doit pas figurer dans le menu.</p>
</div>

## Gestion des pages

### Publication/dépublication de pages

Pages need to be published to make them accessible to website visitors. To
publish or unpublish a page, access it and toggle the switch in the upper-
right corner from **Unpublished** to **Published** , or vice versa.

![Commutateur Non publié/Publié](../../../_images/un-published_toggle.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il est également possible de :</p>
<blockquote>
<div><ul>
<li><p>publier/dépublier une page à partir des <a href="#website-page-properties"><span class="std std-ref">propriétés de la page</span></a>, où vous pouvez définir une date de publication et/ou restreindre la visibilité de la page si nécessaire ;</p></li>
<li><p>publish/unpublish several pages at once: go to Website ‣ Site ‣ Pages,
select the pages, then click <b>Action</b> and select <b>Publish</b> or
<b>Unpublish</b>.</p></li>
</ul>
</div></blockquote>
</div>

### Page d’accueil

When you create a website, Konvergo ERP creates a dedicated **Home** page by default,
but you can define any website page as your homepage. To do so, go to Website
‣ Configuration ‣ Settings, then, in the **Website info** section, define the
URL of the desired page in the field **Homepage URL** (e.g., `/shop`).

Alternatively, you can define any static page as your homepage by going to
Website ‣ Site ‣ Properties. Select the **Publish** tab and enable **Use as
Homepage**.

### Propriétés de la page

To modify a static page’s properties, access the page you wish to modify, then
go to Site ‣ Properties.

L’onglet **Nom** vous permet de :

  * renommer la page dans le champ **Nom de la page** ;

  * modifier l”**URL de la page**. Dans ce cas, vous pouvez rediriger l’ancienne URL vers la nouvelle le cas échéant. Pour ce faire, activez l’option **Rediriger l’ancienne URL** , puis sélectionnez le **Type** de redirection :

    * **301 Changement d’adresse définitif** : pour rediriger la page de manière permanente ;

    * **302 Changement d’adresse temporaire** : pour rediriger la page de manière temporaire.

![Rediriger une ancienne URL](../../../_images/page-redirection.png)

Vous pouvez davantage adapter les propriétés de la page dans l’onglet
**Publier** :

  * **Afficher dans le menu supérieur** : Désactivez cette option si vous ne voulez pas que la page apparaisse dans le menu ;

  * **Définir comme page d’accueil** : Activez cette option si vous voulez que cette page soit la page d’accueil de votre site web ;

  * **Indexé** : Désactivez cette option si vous ne voulez pas que la page s’affiche dans les résultats des moteurs de recherche ;

  * **Publié** : Activez cette option pour publier la page ;

  * **Date de publication** : Pour publier la page à un moment spécifique, sélectionnez la date, cliquez sur l’icône d’horloge pour définir l’heure, puis cliquez sur la coche verte pour valider votre sélection.

  * **Visibilité** : Sélectionnez qui peut accéder à la page :

    * **Tout le monde**

    * **Personnes connectées**

    * **Groupe restreint** : Sélectionnez le(s) [groupe(s) d’accès](../../general/users/access_rights) dans le champ **Groupe autorisé**.

    * **Avec mot de passe** : Saisissez le mot de passe dans le champ **Mot de passe**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p><em>Certaines</em> de ces propriétés peuvent également être modifiées à partir de Site Web ‣ Site ‣ Pages.</p>
</div>

#### Duplication de pages

Pour dupliquer une page, accédez à la page, puis allez à Site ‣ Propriétés et
cliquez sur **Dupliquer la page**. Saisissez un **Nom de page** , puis cliquez
sur **OK**. Par défaut, la nouvelle page est ajoutée après la page dupliquée
dans le menu, mais vous pouvez la retirer du menu ou modifier sa position à
l’aide de l”[éditeur de menu](pages/menus).

#### Suppression de pages

Pour supprimer une page, suivez les étapes suivantes :

  1. Accédez à la page, puis allez à Site ‣ Propriétés et cliquez sur **Supprimer la page**.

  2. Une fenêtre contextuelle s’affiche avec tous les liens se rapportant à la page que vous voulez supprimer, organisés par catégorie. Pour éviter que les visiteurs du site web n’atterrissent sur une page d’erreur 404, vous devez mettre à jour tous les liens de votre site web qui renvoient à cette page. Pour ce faire, développez une catégorie, puis cliquez sur un lien pour l’ouvrir dans une nouvelle fenêtre. Vous pouvez également mettre en place une redirection pour la page supprimée.

  3. Une fois les liens mis à jour (ou la redirection mise en place), cochez la case **Je confirme cette décision** , puis cliquez sur **OK**.

### URL redirect mapping

URL redirect mapping consists in sending visitors and search engines to a URL
different from the one they initially requested. This technique is used, for
example, to prevent broken links when you delete a page, modify its URL, or
migrate your site from another platform to an Konvergo ERP
[domain](configuration/domain_names). It can also be used to improve
[Search Engine Optimization (SEO)](pages/seo).

Pour accéder aux redirections d’URL existantes et en créer de nouvelles,
[activez le mode développeur](../../general/developer_mode) et allez à
Site Web ‣ Configuration ‣ Redirections.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>A redirect record is added automatically every time you <a href="#website-page-properties"><span class="std std-ref">modify a page’s URL</span></a> and enable <b>Redirect Old URL</b>.</p></li>
<li><p>You can set up redirections for <a href="#website-page-type"><span class="std std-ref">static and dynamic pages</span></a>.</p></li>
</ul>
</div>

Pour créer une nouvelle redirection, cliquez sur le bouton **Nouveau** , puis
complétez les champs :

  * **Nom** : Saisissez un nom permettant d’identifier la redirection.

  * **Action** : Sélectionnez le type de redirection :

>     * **404 Not found** : visitors are redirected to a 404 error page when
> they try to access an unpublished or deleted page.
>
>     * **301 Moved Permanently** : for permanent redirections of unpublished
> or deleted static pages. The new URL is shown in search engine results, and
> the redirect is cached by browsers.
>
>     * **302 Moved Temporarily** : for short-term redirections, for example,
> if you are redesigning or updating a page. The new URL is neither cached by
> browsers nor shown in search engine results.
>
>     * **308 Redirect/Rewrite** : for permanent redirections of existing
> dynamic pages. The URL is renamed; the new name is shown in search engine
> results and is cached by browsers. Use this redirect type to rename a
> dynamic page, for example, if you wish to rename `/shop` into `/market`.

  * **URL from** : Enter the URL to be redirected (e.g., `/about-the-company`) or search for the desired dynamic page and select it from the list.

  * **URL to** : For 301, 302, and 308 redirects, enter the URL to be redirected to. If you want to redirect to an external URL, include the protocol (e.g., `https://`).

  * **Site Web** : Sélectionnez un site web spécifique.

  * **Sequence** : To define the order in which redirections are performed, e.g., in the case of redirect chains (i.e., a series of redirects where one URL is redirected to another one, which is itself further redirected to another URL).

Basculez le commutateur **Actif** pour désactiver la redirection.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>404, 301, and 302 redirections are meant to migrate traffic from
<a href="#website-un-publish-page"><span class="std std-ref">unpublished</span></a> or <a href="#website-delete-page"><span class="std std-ref">deleted</span></a> pages
to <em>new</em> pages, while the 308 redirect is used for <em>permanent</em> redirections of <em>existing</em> pages.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://developers.google.com/search/docs/crawling-indexing/301-redirects">Documentation de Google sur les redirections et la recherche</a></p></li>
<li><p><a href="pages/seo">Search Engine Optimization (SEO)</a></p></li>
</ul>
</div>

  * [Menus](pages/menus)
  * [Search Engine Optimization (SEO)](pages/seo)

