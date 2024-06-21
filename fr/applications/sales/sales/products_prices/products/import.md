# Importer des produits

Konvergo ERP _Ventes_ fournit un modèle pour l’importation de produits avec catégories
et variantes, qui peut être ouvert et modifié avec n’importe quel logiciel de
feuille de calcul (Microsoft Excel, OpenOffice, Google Sheets, etc.).

Lorsque cette feuille de calcul est complétée correctement, elle peut être
rapidement chargée vers la base de données Konvergo ERP. Une fois chargés, ces
produits sont immédiatement ajoutés, accessibles et modifiables dans le
catalogue de produits.

## Modèle d’importation

Afin d’importer des produits avec catégories et variantes, le _Modèle
d’importation pour les produits_ **doit** être téléchargé. Une fois
téléchargé, le modèle peut être ajusté et personnalisé, puis de nouveau chargé
vers la base de données Konvergo ERP.

Pour télécharger le modèle d’importation nécessaire, allez à l’application
Ventes ‣ Produits ‣ Produits. Sur la page des **Produits** , cliquez sur
l’icône d’engrenage **⚙️** dans le coin supérieur gauche. Cette opération
ouvre un menu déroulant.

Dans ce menu déroulant, sélectionnez l’option **Importer des
enregistrements**.

![L'option Importer des enregistrements à sélectionner en cliquant sur l'icône
d'engrenage sur la page des produits dans Konvergo ERP
Ventes.](../../../../../_images/gear-import-records-option.png)

En cliquant sur **Importer des enregistrements** , une page séparée s’ouvre
contenant un lien qui permet de télécharger le **Modèle d’importation pour les
produits**. Cliquez sur ce lien pour télécharger le modèle.

![L'option Importer des enregistrements à sélectionner en cliquant sur l'icône
d'engrenage sur la page des produits dans Konvergo ERP
Ventes.](../../../../../_images/import-template-products.png)

Une fois que le modèle est téléchargé, ouvrez la feuille de calcul pour
personnaliser le fichier.

## Personnaliser le modèle d’importation des produits

Lorsque le modèle d’importation a été téléchargé et ouvert, vous devez à
présent modifier son contenu. Toutefois, avant d’apporter des changements,
gardez ces quelques éléments à l’esprit pendant le processus :

  * N’hésitez pas à supprimer des colonnes que vous n’estimez pas nécessaires. Toutefois, il est _fortement_ recommandé de conserver la colonne **Référence interne**.

Bien que ce ne soit pas obligatoire, le fait d’avoir un identifiant unique
(par ex. `FURN_001`) dans la colonne **Référence interne** pour chaque produit
peut être utile dans de nombreux cas. L’identifiant peut même être celui des
feuilles de calcul précédentes pour faciliter la transition dans Konvergo ERP.

Par exemple, lors de la mise à jour des produits importés, vous pouvez
importer le même fichier plusieurs fois sans devoir créer des doublons,
améliorant donc l’efficacité et la simplicité de la gestion des produits
importés.

  * Ne modifiez **pas** les libellés des colonnes qui doivent être importées. Sinon, Konvergo ERP ne les reconnaîtra pas et vous devrez les faire correspondre manuellement sur l’écran d’importation.

  * N’hésitez pas à ajouter de nouvelles colonnes au modèle de feuille de calcul si vous le souhaitez. Cependant, pour qu’ils soient ajoutés, ces champs **doivent** exister dans Konvergo ERP. Si Konvergo ERP ne peut pas faire correspondre le nom de la colonne à un champ, il peut être associé manuellement pendant le processus d’importation.

Pendant le processus d’importation du modèle complété, Konvergo ERP affiche une page
présentant tous les éléments du modèle de produit nouvellement configuré,
classés par **Colonne de fichier** , **Champ Konvergo ERP** , et **Commentaires**.

Pour manuellement faire correspondre un nom de colonne avec un champ dans
Konvergo ERP, cliquez sur le menu déroulant **Champ Konvergo ERP** à côté de la **Colonne de
fichier** qui doit être ajustée manuellement et sélectionnez le champ
approprié dans ce menu déroulant.

![Le menu déroulant du Champ Konvergo ERP à côté d'une Colonne de fichier qui doit
être ajustée manuellement.](../../../../../_images/odoo-field-dropdown-
menu.png)

## Importer la feuille de calcul du modèle de produit

Après avoir personnalisé la feuille de calcul du modèle de produit, retournez
à la page d’importation de produit d’Konvergo ERP, où vous trouvez le lien de
téléchargement du modèle et cliquez sur le bouton **Charger le fichier** dans
le coin supérieur gauche.

![Le bouton permettant de charger un fichier sur la page de téléchargement du
modèle de produit dans Konvergo ERP Ventes.](../../../../../_images/upload-file-
button.png)

Une fenêtre contextuelle s’affiche alors, dans laquelle vous pouvez
sélectionner le fichier de feuille de calcul du modèle de produit complété et
le charger vers Konvergo ERP.

Ensuite, Konvergo ERP affiche une page qui présente tous les éléments du modèle de
produit nouvellement configuré, classés par **Colonne de fichier** , **Champ
Konvergo ERP** , et guilabel:`Commentaires`.

![La page Importer un fichier dans Konvergo ERP Ventes après avoir chargé un modèle de
produits.](../../../../../_images/import-a-file-page.png)

De là, vous pouvez manuellement assigner la **Colonne de fichier** à un
**Champ Konvergo ERP** , si nécessaire.

Pour s’assurer que tout est en ordre et que les colonnes et les champs sont
bien alignés, cliquez sur le bouton **Tester** dans le coin supérieur gauche.

Si tout est correctement aligné et appliqué, Konvergo ERP affiche une bannière bleue
en haut de la page, informant l’utilisateur que **Tout semble correct**.

![Le message Tout semble correct qui apparaît sir les colonnes de fichier sont
saisies correctement.](../../../../../_images/everything-seems-valid-
message.png)

S’il y a des erreurs, Konvergo ERP affiche une bannière rouge en haut de la page,
expliquant où se trouvent les problèmes spécifiques et comment y remédier.

![Le message d'erreur d'importation qui apparaît si les colonnes de fichier ne
correspondent pas à un champ Konvergo ERP.](../../../../../_images/import-error-
message.png)

Une fois que ces erreurs sont résolues, cliquez à nouveau sur **Tester** pour
vous assurer que tous les problèmes nécessaires ont été résolus.

Si vous devez charger d’autres modèles de produits, clique sur le bouton
**Charger un fichier** , sélectionnez la feuille de calcul souhaitée et
répétez le processus.

Une fois que vous avez terminé, cliquez sur le bouton **Importer**.

Konvergo ERP importe alors immédiatement ces produits et affiche la page principale
des **Produits** , avec un message contextuel dans le coin supérieur droit. Ce
message contextuel informe l’utilisateur sur le nombre de produits qui ont été
importés avec succès.

![La fenêtre contextuelle qui s'affiche après un processus d'importation de
produits réussi dans Konvergo ERP Ventes.](../../../../../_images/successful-import-
popup.png)

À ce stade, tous les produits nouvellement importés sont accessibles et
modifiables via la page des **Produits**.

## Importer des champs relationnels, des attributs et des variantes

Il convient de noter qu’un objet Konvergo ERP est toujours associé à de nombreux
autres objets. Par exemple, un produit est associé à des catégories de
produits, des attributs, des fournisseurs et bien d’autres choses encore. Ces
liens/connexions sont appelés des relations.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Afin d’importer les relations des produits, les enregistrements de l’objet lié <b>doivent</b> <em>d’abord</em> être importés de leur propre menu de liste.</p>
</div>

### Champs relationnels

Sur les formulaires de produit dans Konvergo ERP, un certain nombre de champs peut
être modifié et personnalisé à tout moment. Ces champs se trouvent dans chaque
onglet sur un formulaire. Tandis que ces champs peuvent facilement être
modifiés directement sur le formulaire de produit, ils peuvent également être
modifiés par le biais d’une importation de produits.

Comme il est indiqué ci-dessus, les champs relationnels de cette nature ne
peuvent être importés pour les produits **que** s’ils existent déjà dans la
base de données. Par exemple, si un utilisateur veut importer un produit avec
un _Type de produit_ , il peut uniquement s’agit des types de produit
préconfigurés qui existent déjà dans la base de données (par ex. _Produit
stockable_ , _Consommable_ , etc.).

Pour importer les informations d’un champ relationnel dans un modèle
d’importation de produit, ajoutez le nom du champ en tant que nom/titre de
colonne de la feuille de calcul. Ensuite, sur la ligne de produit appropriée,
ajoutez l’option de champ relationnel souhaitée.

Lorsque toutes les informations relatives aux champs relationnels ont été
saisies, enregistrez la feuille de calcul et importez-la dans la base de
données, conformément au processus mentionné ci-dessus (application Ventes ‣
Produits ‣ Produits ‣ icône d’engrenage ⚙️ ‣ Importer des enregistrements ‣
Télécharger le fichier).

Une fois que la feuille de calcul avec les informations relatives au champ
relationnel nouvellement configuré a été chargée, cliquez sur **Importer** ,
et Konvergo ERP retourne à la page des **Produits**.

Lorsque les produits nouvellement modifiés, avec les nouvelles informations
sur les champs relationnels, ont été importés et chargés, ces nouvelles
informations peuvent être trouvées sur la page des **Produits**.

### Attributs et valeurs

Konvergo ERP permet aussi aux utilisateurs d’importer des attributs et des valeurs qui
peuvent être utilisés pour des produits qui existent dans la base de données
et/ou avec des produits importés.

Pour importer des attributs et des valeurs, une feuille de temps séparée ou un
fichier CSV dédié aux attributs et valeurs **doivent** être importés et
chargés avant qu’ils puissent être utilisés pour d’autres produits.

Les noms/titres de colonne des attributs et des valeurs de la feuille de
calcul doivent être les suivants : **Attribut** , **Type d’affichage** ,
**Mode de création des variantes** , et **Valeurs / Valeur**.

![Un modèle de feuille de calcul d'attributs et de valeurs pour les
importations.](../../../../../_images/attributes-and-values-spreadsheet.png)

  * **Attribut** : le nom de l’attribut (par ex. `Taille`).

  * **Type d’affichage** : affiche le type utilisé dans le configurateur de produits. Il y a trois options de types d’affichage :

    * **Radio** : valeurs affichées sous forme de boutons radio

    * **Sélection** : valeurs affichées sous forme de liste de sélection

    * **Couleur** : valeurs affichées sous forme d’une sélection de couleurs

  * **Mode de création des variantes** : la façon dont les variantes sont créées lorsqu’elles sont appliquées à un produit. Il y a trois options de mode de création des variantes :

    * **Instantanément** : toutes les variantes possibles sont créées dès que l’attribut et ses valeurs sont ajoutés à un produit

    * **Dynamique** : chaque variante est créée **uniquement** lorsque ses attributs et valeurs correspondants sont ajoutés à une commande

    * **Jamais** : les variantes ne sont **jamais** créées pour l’attribut

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le <b>Mode de création des variantes</b> <b>ne peut pas</b> être modifié une fois que l’attribut est utilisé sur au moins un produit.</p>
</div>

  * **Valeurs/Valeur** : les valeurs relatives à l’attribut correspondant. Il y a plusieurs valeurs pour le même attribut, les valeurs doivent se trouver dans des lignes individuelles sur la feuille de calcul.

Une fois que les attributs et les valeurs souhaités ont été saisis et
enregistrés dans la feuille de calcul, vous devez l’importer et la charger
dans Konvergo ERP. Pour ce faire, allez à l’application Ventes ‣ Configuration ‣
Attributs ‣ icône d’engrenage ⚙️ ‣ Importer des enregistrements ‣ Charger un
fichier.

Une fois que la feuille de calcul avec les attributs et valeurs nouvellement
configurés a été chargée, cliquez sur **Importer** , et Konvergo ERP retourne à la
page **Attributs**. Vous pourrez y trouver ces attributs et les valeurs
nouvellement ajoutés et les modifier le cas échéant.

Comme il est mentionné ci-dessus, lorsque les attributs et les valeurs ont été
ajoutés à la base de données Konvergo ERP, ils peuvent être utilisés pour des produits
existants ou importés.

### Variantes de produit

Lorsque les attributs et les valeurs de produit sont configurés dans la base
de données, ils peuvent être utilisés dans les feuilles de calcul
d’importation des produits pour ajouter plus d’informations et de détails aux
produits importés.

Pour importer des produits avec des attributs et des valeurs de produits, la
feuille de calcul du modèle d’importation des produits avec des colonnes
spécifiques : **Attributs de produit / Attribut** , **Attributs de produit /
Valeurs** , et **Nom**.

Il peut y avoir d’autres colonnes, mais ces colonnes sont **nécessaires** pour
importer correctement des produits avec des variantes spécifiques.

![Feuille de calcul des variantes de produits contenant les attributs et les
variantes des produits à des fins
d'importation.](../../../../../_images/product-attribute-spreadsheet-
import.png)

  * **Nom** : nom du produit

  * **Attributs de produits / Attribut** : nom de l’attribut

  * **Attributs de produits / Valeurs** : valeurs relatives à l’attribut correspondant

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour importer plusieurs valeurs, séparez-les par <em>une virgule</em>, et <b>non</b> par une virgule d’une espace, dans la feuille de calcul du modèle d’importation de produits (par ex. <code>furniture,couch,home</code>).</p>
</div>

Lorsque les produits et les variantes souhaités ont été saisis et enregistrés
dans la feuille de calcul, vous devez les importer et les charger vers Konvergo ERP.
Pour ce faire, allez à l’application Ventes ‣ Produits ‣ Produits ‣ Icône
d’engrenage ⚙️ ‣ Importer des enregistrements ‣ Charger un fichier.

Une fois que la feuille de calcul avec les produits et les variantes
nouvellement configurés a été chargée, cliquez sur **Importer** , et Konvergo ERP
retourne à la page des **Produits**. Vous y trouverez les produits
nouvellement ajoutés.

Pour visualiser et modifier les attributs et les variantes de n’importe quel
produit, sélectionnez le produit souhaité sur la page des **Produits** et
cliquez sur l’onglet **Attributs & Variantes**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="variants">Variantes de produit</a></p>
</div>

