# Modèles de devis

Dans Konvergo ERP _Ventes_ , les vendeurs ont la possibilité de créer des modèles de
devis réutilisables pour des produits ou des services courants proposés par
l’entreprise.

Grâce à ces devis, les devis peuvent être personnalisés et envoyés aux clients
bien plus rapidement, sans avoir à créer de nouveaux devis à partir de zéro
chaque fois qu’une négociation a lieu.

## Configuration

Commencez par activer le paramètre dans l’application Ventes ‣ Configuration ‣
Paramètres, et faites défiler jusqu’à la section **Devis & Commandes**.

Dans cette section, cochez la case à côté de l’option **Modèles de devis**.
Cette option fait apparaître un nouveau champ **Modèle par défaut** dans
lequel un modèle de devis par défaut peut être sélectionné dans un menu
déroulant.

![Comment activer les modèles de devis dans Konvergo ERP
Ventes.](../../../../_images/quotations-templates-setting.png)

En outre, lors de l’activation de la fonctionnalité **Modèle de devis** , un
lien interne **➡️ Modèles de devis** apparaît sous le champ **Modèle par
défaut**.

Le fait de cliquer sur ce lien ouvre la page **Modèles de devis** où vous
pouvez créer, afficher et modifier des modèles.

Avant de quitter la page des **Paramètres** , n’oubliez pas de cliquer sur le
bouton **Enregistrer** pour enregistrer tous les changements effectués pendant
al session.

## Créer des modèles de devis

Cliquez sur le lien **Modèles de devis** sur la page des **Paramètres** ou
allez à l’application Ventes ‣ Configuration ‣ Modèles de devis. Les deux
options permettent d’afficher la page des **Modèles de devis** sur laquelle
vous pouvez créer, visualiser et modifier des modèles de devis.

![Page des modèles de devis dans l'application Konvergo ERP
Ventes.](../../../../_images/quotation-templates-page.png)

Pour créer un nouveau modèle de devis, cliquez sur le bouton **Nouveau** dans
le coin supérieur gauche. Cette opération fait apparaître un formulaire de
modèle de devis vierge qui peut être personnalisé de plusieurs façons.

![Créez un nouveau modèle de devis dans Konvergo ERP
Ventes.](../../../../_images/blank-quotation-form.png)

Commencez par donner un nom au modèle dans le champ **Modèle de devis**.

Then, in the **Quotation expires after** field, designate how many days the
quotation template will remain valid for, or leave the field on the default
`0` to keep the template valid indefinitely.

If the **Online Signature** and/or **Online Payment** features are activated
in the **Settings** (Sales app ‣ Configuration ‣ Settings), those options are
available in the **Online confirmation** field.

In the **Online confirmation** field, check the box beside **Signature** to
request an online signature from the customer to confirm an order. Check the
box beside **Payment** to request an online payment from the customer to
confirm an order.

Both options can be enabled simultaneously, in which case the customer must
provide **both** a signature **and** a payment to confirm an order.

Ensuite, dans le champ **Email de confirmation** , cliquez sur le champ vierge
pour afficher un menu déroulant. Dans ce menu, sélectionnez un modèle d’email
préconfiguré qui sera envoyé aux clients lors de la confirmation d’une
commande.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour créer un nouveau modèle d’email directement dans le champ <b>Email de confirmation</b>, commencez par écrire le nom du nouveau modèle d’email dans le champ et sélectionnez <b>Créer</b> ou <b>Créer et modifier…</b> dans le menu déroulant qui s’affiche.</p>
<p>Selecting <b>Create</b> creates the email template, which can be edited later. Selecting
<b>Create and edit…</b> creates the email template, and a <b>Create Confirmation
Mail</b> pop-up window appears, in which the email template can be customized and configured right
away.</p>
<img alt="Fenêtre contextuelle permettant de créer un email de confirmation à partir du formulaire de modèle de devis dans Konvergo ERP Ventes." class="align-center" src="../../../../_images/create-confirmation-mail-popup.png"/>
<p>Lorsque toutes les modifications ont été effectuées, cliquez sur <b>Enregistrer &amp; Fermer</b> pour enregistrer le modèle d’email et retourner au formulaire de devis.</p>
</div>

Si vous travaillez dans un environnement de plusieurs sociétés, utilisez le
champ **Société** pour indiquer à quelle société ce modèle de devis
s’applique.

In the **Recurrence** field, choose from a variety of pre-configured amounts
of time (e.g. **Monthly** , **Quarterly**) to designate how often this
quotation template should occur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Recurrence</b> field <b>only</b> applies to subscription plans. For more information,
check out the documentation on <a href="../../subscriptions/plans">Plans d’abonnement</a>.</p>
</div>

### Onglet Lignes

Dans l’onglet **Lignes** , vous pouvez ajouter des produits au modèle de devis
en cliquant sur **Ajouter un produit** , vous pouvez l’organiser en cliquant
sur **Ajouter une section** (et en glissant/déposant des en-têtes de section)
et vous pouvez ajouter des informations discrétionnaires (telles que les
détails de garantie, les conditions, etc.) en cliquant sur **Ajouter une
note**.

![Populated lines tab on a quotation template form in Konvergo ERP
Sales.](../../../../_images/lines-tab-quotation-template.png)

Pour ajouter un produit à un modèle de devis, cliquez sur **Ajouter un
produit** dans l’onglet **Lignes** d’un formulaire de modèle de devis. cette
opération fait apparaître un champ vierge dans la colonne **Produit**.

Lorsque vous cliquez dessus, un menu déroulant contenant des produits
existants de la base de données s’ouvre. Sélectionnez le produit souhaité dans
le menu déroulant pour l’ajouter au modèle de devis.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le produit souhaité n’est pas encore visible, saisissez le nom du produit souhaité dans le champ <b>Produit</b> et l’option apparaît dans le menu déroulant. Vous pouvez également trouver des produits en cliquant sur <b>Recherche avancée</b> dans le menu déroulant.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Lorsqu’un produit est ajouté à un modèle de devis, la <b>Quantité</b> par défaut est <code>1</code>, mais cette valeur peut être modifiée à tout moment.</p>
</div>

Ensuite, glissez et déposez le produit à l’endroit souhaité, en utilisant
l’icône des **six carrés** à gauche de chaque ligne.

Pour ajouter une _section_ , qui sert d’en-tête pour organiser les lignes
d’une commande, cliquez sur **Ajouter une section** dans l’onglet **Lignes**.
Lorsque vous cliquez sur cette option, un champ vierge s’ouvre dans lequel
vous pouvez donner un nom à la section. Une fois le nom saisi, cliquez à côté
pour sécuriser le nom de la section.

Ensuite, glissez-déposez le nom de la section à l’endroit souhaité en
utilisant l’icône des **six carrés** située à gauche de chaque ligne
d’article.

Pour ajouter une note, qui apparaîtra sous la forme d’un texte destiné au
client sur le devis, cliquez sur **Ajouter une note** dans l’onglet
**Lignes**. Lorsque vous cliquez sur cette option, un champ vierge s’affiche
dans lequel vous pouvez saisir la note souhaitée. Une fois la note saisie,
cliquez à côté pour enregistrer la note.

Ensuite, glissez-déposez la note à l’endroit souhaité en utilisant l’icône des
**six carrés**.

Pour supprimer un article de l’onglet **Lignes** (produit, section et/ou
note), cliquez sur l’icône de la corbeille **🗑️** à l’extrême droite de la
ligne.

### Onglet Produits optionnels

L’utilisation des _produits optionnels_ est une stratégie de marketing qui
implique la vente croisée de produits avec un produit principal. L’objectif
est d’offrir aux clients des produits utiles et pertinents, ce qui peut se
traduire par une augmentation des ventes.

Par exemple, si un client souhaite acheter une voiture, il a le choix de
commander des sièges massants ou d’ignorer l’offre et d’acheter simplement la
voiture. Le fait de proposer au client d’acheter des produits optionnels
améliorer son expérience.

Les produits optionnels apparaissent dans une section au bas des commandes et
des pages d’eCommerce. Les clients peuvent les ajouter immédiatement à leurs
commandes en ligne eux-mêmes, s’ils le souhaitent.

![Les produits optionnels sur une commande typique avec Konvergo ERP
Ventes.](../../../../_images/optional-products-on-sales-order.png)

Dans l’onglet **Produits optionnels** , cliquez sur **Ajouter une ligne** pour
chaque produit de vente croisée lié aux articles originaux dans l’onglet
**Lignes** , le cas échéant. Les produits ajoutés ici complètent l’offre
originale en tant que valeur ajoutée pour l’acheteur potentiel.

![Populated optional products tab on a quotation template in Konvergo ERP
Sales.](../../../../_images/optional-products-tab-quotation-template1.png)

Le fait de cliquer sur **Ajouter une ligne** fait apparaître un champ vierge
dans la colonne **Produit**.

Lorsque vous cliquez dessus, un menu déroulant contenant des produits de la
base de données s’affiche. Sélectionnez le produit souhaité dans le menu
déroulant pour l’ajouter en tant que produit optionnel au modèle de devis.

Pour supprimer un article de l’onglet **Produits optionnels** , cliquez sur
l’icône de corbeille **🗑️**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les produits optionnels ne sont <b>pas</b> obligatoires pour créer un modèle de devis.</p>
</div>

### Onglet Conditions générales

L’onglet **Conditions générales** vous permet d’ajouter des conditions
générales au modèle de devis. Pour ajouter des conditions générales, tapez
simplement (ou copiez/collez) les conditions générales souhaitées dans cet
onglet.

![Terms and conditions tab in a quotation template form in Konvergo ERP
Sales.](../../../../_images/terms-and-conditions-tab.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../finance/accounting/customer_invoices/terms_conditions">Conditions générales par défaut (CG)</a></p>
</div>
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les conditions générales ne sont <b>pas</b> obligatoires pour créer un modèle de devis.</p>
</div>

## Concevoir des modèles de devis

In the upper-left corner of the quotation template form, there’s a **Design
Template** button.

![Design template button in the upper-left corner of quotation template
form.](../../../../_images/design-template-button.png)

When clicked, Konvergo ERP reveals a preview of the quotation template, through the
Konvergo ERP _Website_ application, as it will appear on the front-end of the website
to the customer.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>This feature is <b>only</b> available if the <em>Website</em> application is installed.</p>
</div>

Konvergo ERP uses numerous blue placeholder blocks to signify where certain elements
appear, and what they contain (e.g. **Template Header** , **Product**).

To edit the content, appearance, and overall design of the quotation template
via the _Website_ application, click the **Edit** button in the upper-right
corner.

![Design template edit button in the upper-right corner of quotation template
design.](../../../../_images/design-template-edit-button.png)

When **Edit** is clicked, Konvergo ERP reveals a sidebar filled with a variety of
design elements and feature-rich building blocks. These building blocks can be
dragged-and-dropped anywhere on the quotation template design.

![Design quotation template building blocks sidebar in Konvergo ERP
Website.](../../../../_images/design-quotation-building-blocks.png)

After a block has been dropped in the desired position, it can be customized
and configured to fit any unique need, look, or style.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>La conception du modèle de devis utilise la même méthodologie et fonctionnalité avec des blocs de construction qu’une conception de page web typique avec Konvergo ERP <em>Site Web</em>. N’hésitez pas de consulter la documentation relative au <a href="../../../websites/website">Site Web</a> pour en savoir plus.</p>
</div>

Lorsque toutes les configurations souhaitées sont terminées, cliquez sur le
bouton **Enregistrer**.

There is also a blue banner at the top of the quotation template design with a
link to quickly return **Back to edit mode**. When clicked, Konvergo ERP returns to
the quotation template form in the back-end of the _Sales_ application.

## Utiliser les modèles de devis

Lors de la création d’un devis (application Ventes ‣ Nouveau), choisissez un
modèle préconfiguré dans le champ **Modèle de devis**.

![Le champ Modèles de devis sur un formulaire de devis standard dans Konvergo ERP
VenteS.](../../../../_images/quotation-templates-field.png)

Pour visualiser ce que le client verra, cliquez sur le bouton **Aperçu** en
haut de la page pour voir à quoi ressemblera le modèle de devis dans le
frontend du site web par le biais du portail client d’Konvergo ERP.

![Aperçu client d'un modèle de devis dans Konvergo ERP
Ventes.](../../../../_images/quotations-templates-preview.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="get_signature_to_validate">Signatures en ligne pour les confirmations de commande</a></p></li>
<li><p><a href="get_paid_to_validate">Paiement en ligne pour confirmer la commande</a></p></li>
</ul>
</div>

