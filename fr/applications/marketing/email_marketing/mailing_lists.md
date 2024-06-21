# Listes de diffusion

Les listes de diffusion sont importantes pour un certain nombre de raisons.
Elles peuvent fournir des pistes précieuses aux équipes commerciales,
communiquer avec les participants aux groupes de discussion, contacter
directement les consommateurs pour obtenir un feedback utile, et bien plus
encore.

## Créer des listes de diffusion

Pour créer une liste de diffusion dans l’application _Email Marketing_ , allez
à Listes de diffusion ‣ Listes de diffusion ‣ Créer. En cliquant sur **Créer**
, une fenêtre contextuelle s’affiche.

![Vue de la fenêtre contextuelle de la liste de diffusion dans l'application
Email Marketing d'Konvergo ERP.](../../../_images/new-mailing-list-popup.png)

Dans la fenêtre contextuelle, donnez un nom à la liste de diffusion et
indiquez si la liste de diffusion doit être publique en cochant la case **Est
publique**.

L’option **Est publique** permet aux destinataires d’accéder à la liste de
diffusion dans la page de désabonnement, ce qui leur permet de mettre à jour
leurs préférences d’abonnement.

Après avoir configuré ces options, cliquez sur **Créer** pour créer la liste
de diffusion, qu’Konvergo ERP ajoute automatiquement à la page des **Listes de
diffusion**.

## Ajouter des contacts à une liste de diffusion

Avoir avoir créé une liste de diffusion (et l’avoir ajoutée au tableau de bord
des **Listes de diffusion**), cliquez sur la liste de diffusion souhaitée pour
ajouter des contacts à la liste.

En cliquant sur la liste de diffusion souhaitée, une page **Contacts de la
liste de diffusion** s’affiche, dans laquelle vous pouvez ajouter des contacts
à cette liste spécifique en cliquant sur **Créer** et en ajoutant des
informations de contact directement sur un formulaire détaillé de contact
distinct.

Ou bien, dans l’application Email Marketing, allez à Listes de diffusion ‣
Contacts de la liste de diffusion. Cette opération fait apparaître une page
distincte contenant tous les contacts de la liste de diffusion.

Cliquez alors sur **Créer** et ajoutez un contact en suivant les mêmes étapes
que précédemment. Vous pouvez également cliquer sur l’icône **Importer** (à
droite du bouton **Créer**) pour importer des contacts dans la base de
données.

Une fois que les contacts sont dans la base de données, cliquez sur le
formulaire détaillé du contact souhaité et ajoutez la liste de diffusion
préférée dans l’onglet **Liste de diffusion** (au bas du formulaire détaillé
du contact), en cliquant sur **Ajouter une ligne** et en sélectionnant la
liste de diffusion souhaitée. Plusieurs listes de diffusion peuvent être
ajoutées au formulaire d’un même contact.

![Vue d'un formulaire détaillé d'un contact avec l'onglet liste de diffusion
dans Konvergo ERP Email Marketing.](../../../_images/contact-form-mailing-list-
tab.png)

### Créer une nouvelle liste de diffusion à partir du formulaire de contact

Pour créer une liste de diffusion à partir du formulaire d’un contact, cliquez
sur **Ajouter une ligne** et saisissez le nom d’une nouvelle liste de
diffusion dans le champ vide qui apparaît. Sélectionnez ensuite soit **Créer**
, soit **Créer et Modifier…**.

![Vue du menu déroulant de la nouvelle liste de diffusion sur le formulaire du
contact dans Konvergo ERP Email Marketing.](../../../_images/new-list-dropdown-create-
options.png)

L’option **Créer** permet de rapidement créer la liste de diffusion sur le
formulaire du contact et de configurer la liste ultérieurement. L’option
**Créer et Modifier…** permet de créer la liste de diffusion et d’afficher une
fenêtre contextuelle dans laquelle il possible de configurer la nouvelle liste
de diffusion.

![Vue de la fenêtre contextuelle de la liste de diffusion après avoir cliqué
sur Créer et Modifier dans Konvergo ERP Email Marketing.](../../../_images/create-and-
edit-mailing-list-popup.png)

## Lier une liste de diffusion à un site web (blocs de newsletter)

Lorsqu’une liste de diffusion est créée dans la base de données, Konvergo ERP propose
de lier la liste de diffusion directement au site web construit par Konvergo ERP (créé
via l’application **Site Web** d’Konvergo ERP).

Pour lier une liste de diffusion à un site web, allez au frontend du site web
et activez le mode **Édition** en cliquant sur **Modifier** dans le coin
supérieur droit. En cliquant dessus, Konvergo ERP affiche une barre latérale droite,
remplie de _blocs de construction_ à glisser-déposer qui sont remplis de
fonctionnalités, d’options et d’éléments de design variés.

Ensuite, pour ajouter un _champ d’abonnement_ à une liste de diffusion
spécifique sur un site web, glissez et déposez l’une des options
**Newsletter** (**Bloc de newsletter** , **Fenêtre contextuelle newsletter**
ou **Newsletter**).

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour localiser rapidement les blocs de construction <b>Newsletter</b> (en mode <b>Édition</b> sur le frontend du site web), saisissez <code>Newsletter</code> dans la barre de recherche, située dans la barre latérale droite, dans l’onglet <b>Blocs</b> et Konvergo ERP affiche les trois différentes options de <b>Newsletter</b>.</p>
<img alt="Vue de la façon de rechercher rapidement les blocs de newsletter dans l'application Site Web d'Konvergo ERP." class="align-center" src="../../../_images/newsletter-block-search.png"/>
</div>

Lorsque vous glissez un bloc **Newsletter** dans le corps du site web, Konvergo ERP
fait apparaître une fenêtre contextuelle, dans laquelle la liste de diffusion
souhaitée est sélectionnée dans un menu déroulant (et liée à ce bloc sur le
site web).

![Vue de la fenêtre contextuelle d'ajout d'une liste de diffusion sur un site
web d'Konvergo ERP.](../../../_images/add-mailing-list-popup-website.png)

  * **Bloc de newsletter** \- Ajoute un bloc sur la page web, offrant aux visiteurs la possibilité d’ajouter leur adresse email à cette liste de diffusion et de s’abonner aux communications futures.

Voici un exemple d’un **Bloc de newsletter**.

![Vue d'un exemple de bloc de newsletter dans l'application Site Web
d'Konvergo ERP.](../../../_images/newsletter-block-sample.png)

  * **Fenêtre contextuelle Newsletter** \- Indique à Konvergo ERP de faire apparaître une fenêtre contextuelle d’abonnement à un certain endroit de la page web. Lorsque le visiteur fait défiler la page jusqu’à ce point prédéterminé, une fenêtre contextuelle d’abonnement apparaît, lui demandant son adresse email pour s’abonner à la liste de diffusion. La fenêtre contextuelle peut être modifiée pour mieux s’adapter aux besoins de l’entreprise.

Voici un exemple d’une **Fenêtre contextuelle Newsletter**.

![Vue d'un exemple de fenêtre contextuelle newsletter sur un site web
Konvergo ERP.](../../../_images/newsletter-popup-sample.png)

  * **Newsletter** \- Fournit aux visiteurs un champ simple pour ajouter leur adresse email à la liste de diffusion et s’abonner aux futurs mailings dans le pied de page (ou à un autre endroit sur la page).

Voici un exemple d’un bloc dynamique **Newsletter**.

![Vue d'un bloc dynamique Newsletter sur un site web
Konvergo ERP.](../../../_images/newsletter-footer-block-sample.png)

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../email_marketing">Email Marketing</a></p></li>
<li><p><a href="unsubscriptions">Gérer les désabonnements (liste noire)</a></p></li>
</ul>
</div>

