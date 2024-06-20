# Devises étrangères

Avec Odoo, vous pouvez utiliser des listes de prix pour gérer les prix dans un
certain nombre de devises étrangères. Plus précisément, Odoo a la capacité de
travailler avec 167 devises.

Note

Pour pouvoir utiliser plusieurs devises dans Odoo _Ventes_ , l’application
_Comptabilité_ **doit** être installée.

## Paramètres

Une fois que l’application _Comptabilité_ a été mise à jour, les devises
étrangères peuvent être ajoutées à la base de données, Allez à l’application
Comptabilité ‣ Configuration ‣ Paramètres, faites défiler jusqu’à la section
Devises et trouvez le paramètre Devise principale.

![La présentation de la fonctionnalité de devise principale sur la page des
paramètres dans Odoo Comptabilité.](../../../../../_images/main-currency-
setting-page.png)

Odoo définit automatiquement la devise principale comme la devise du pays dans
lequel l’entreprise est basée.

Pour changer la devise principale de l’entreprise, cliquez sur le menu
déroulant dans le champ Devise, sélectionnez la devise souhaitée et assurez-
vous d”Enregistrer les changements.

Astuce

Pour s’assurer que les taux de change sont automatiquement mis à jour, activez
la fonctionnalité _Taux de change automatiques_ sur la page des paramètres de
_Comptabilité_ (Comptabilité ‣ Configuration ‣ Paramètres ‣ section Devises).

![La présentation de la fonctionnalité de devise principale sur la page des
paramètres dans Odoo Comptabilité.](../../../../../_images/automatic-currency-
rates.png)

Cochez la case à côté de la fonctionnalité ;guilabel:`Taux de change
automatiques`, choisissez une banque désignée pour obtenir les taux de change
ans le menu déroulant Service et sélectionnez un Intervalle de temps pour que
les mises à jour aient lieu. Déterminez ensuite la date de la Prochaine
exécution.

Pour mettre à jour instantanément les taux de change, cliquez sur l’icône 🔁
(flèches circulaires), située à droite du champ Prochaine exécution.

Lorsque toutes les configurations sont terminées, assurez-vous d”enregistrer
tous les changements.

Note

Tous les modes de paiement **doivent** être libellés dans la même devise que
le journal des ventes ou dans la devise de l’entreprise, si celle-ci n’est pas
définie. Si ce n’est pas le cas, un message d”Erreur de validation s’affiche.

## Afficher, modifier et ajouter des devises

Pour afficher, modifier et ajouter des devises à la base de données et les
rendre disponibles dans les listes de prix et dans le menu déroulant Devise
principale, cliquez sur le lien Devises, situé sous le champ Devise de la page
app Comptabilité ‣ Paramètres.

Lorsque vous cliquez sur le lien Devises, une page séparée Devises s’affiche.

![La présentation de la page des devises principales dans Odoo
Comptabilité.](../../../../../_images/main-currencies-page.png)

Sur cette page, Odoo fournit une liste principale de 167 devises. Chaque ligne
indique la Devise, le Symbole, le Nom, la date de la Dernière mise à jour et
le Taux actuel (par rapport à la devise par défaut du pays dans lequel
l’entreprise est basée).

À l’extrême droite, il y a deux colonnes qui peuvent être activées ou
désactivées :

  * Utiliser sur eBay : cette devise peut être utilisée avec le compte eBay connecté (si applicable).

  * Actif : cette devise est activée, ce qui signifie qu’elle peut être ajoutée à une liste de prix ou utilisée en tant que devise principale de l’entreprise, si vous le souhaitez (via l’application Comptabilité ‣ Configuration ‣ Paramètres ‣ section Devises).

Note

Par défaut, toutes les options de devises actives se trouvent en haut de la
liste.

Astuce

Il est recommandé de créer _au moins_ une liste de prix par devise active.
Consultez la page [Listes de prix, remises et formules](pricing.html) pour en
savoir plus sur la configuration des listes de prix.

Pour activer ou désactiver les options, cliquez sur le bouton à bascule dans
la ligne de la colonne correspondante. Lorsque l’option est _activée_ , le
bouton est vert ; lorsqu’elle est _désactivée_ , le bouton est gris.

### Formulaire détaillé de la devise

Pour modifier une devise sur la page Devises, cliquez sur la devise souhaitée
pour afficher le formulaire détaillé de cette devise en particulier et faites
les changements nécessaires.

![La présentation d'un formulaire détaillé de la devise dans Odoo
Comptabilité.](../../../../../_images/currency-detail-form.png)

Sur le formulaire détaillé de la devise, le code de la devise pertinente
apparaît dans le champ Devise. En dessous, le nom de la devise se trouve dans
le champ Nom.

Ensuite, vous pouvez basculer la disponibilité de la devise avec le bouton
Actif : le bouton vert indique que la devise est _activée_ et le bouton gris
indique qu’elle est _désactivée_.

Sur la droite du formulaire détaillé de la devise, vous trouverez l”Unité
monétaire (par ex. `Dollars`) et la Sous-unité montaire (par ex. `Cents`).

Si la devise est destinée à être utilisée sur eBay, activez l’option Utiliser
sur eBay.

Ensuite, dans l’onglet Taux, vous pouvez visualiser, ajouter ou supprimer les
différents taux de conversion. Chaque ligne affiche la Date de ce taux
spécifique, la Société à laquelle il est lié, suivie de l”Unité par… et …par
Unité.

Note

Le _…_ dans les deux dernières colonnes

Pour ajouter un nouveau taux, cliquez sur Ajouter une ligne dans l’onglet Taux
et complétez les informations nécessaires dans les colonnes susmentionnées.

### Formulaire détaillé de la devise principale

Si la devise sélectionnée est la devise principale de l’entreprise, une
bannière bleue apparaît en haut du formulaire détaillé de la devise avec le
message : Il s’agit de la devise de votre entreprise..

![La présentation d'un formulaire détaillé de la devise principale dans Odoo
Comptabilité.](../../../../../_images/main-currency-detail-form.png)

Tous les champs sont les mêmes qu’un formulaire détaillé d’une devise typique,
mais il n’y aura **pas** d’onglet Taux parce que tous les autres taux de
change sont basés sur la devise principale de l’entreprise.

## Créer une nouvelle devise

Si une devise souhaitée ne figure pas sur la page Devises, cliquez sur le
bouton Nouveau pour ouvrir un formulaire de modèle de devis vierge.

Astuce

Le même bouton Nouveau se situe dans le coin supérieur droit de n’importe quel
formulaire détaillé des devises.

![La présentation du formulaire détaillé de devise vierge dans Odoo
Comptabilité.](../../../../../_images/blank-currency-detail-form.png)

Sur le formulaire détaillé de devise vierge, saisissez le code de la devise
souhaitée dans le champ Devise. En dessous, saisissez le nom de la devise dans
le champ Nom.

Ensuite, faites basculer la disponibilité de la devise avec le bouton ACtif.

Sur la droite du formulaire détaillé de la devise, saisissez l”Unité monétaire
appropriée (par ex. `Dollars`) et la Sous-unité monétaire appropriée (par ex.
`Cents`).

Si la devise est destinée à être utilisée sur eBay, activez l’option Utiliser
sur eBay.

Ensuite, dans l’onglet Taux, ajoutez un nouveau taux en cliquant sur Ajouter
une ligne. Ensuite, confirmez et modifiez les champs Date, Société, Unité
par…, et …par Unité pour vous assurer que toutes les informations remplies
automatiquement sont exactes.

Note

Le _…_ dans les deux dernières colonnes

## Listes de prix spécifiques aux devises

Il est recommandé de créer _au moins_ une liste de prix par devise active dans
la base de données. Pour créer (ou assigner) une liste de prix à une devise
spécifique, allez à l’application Ventes ‣ Produits ‣ Listes de prix.

Sur la page Listes de prix, sélectionnez une liste de prix existante à
modifier ou cliquez sur Nouveau pour créer une nouvelle liste de prix.

Sur le formulaire détaillé de la liste de prix, pour une liste de prix
existante ou nouvelle, modifiez le champ Devise comme vous le souhaitez.

Pour plus d'infos

Consultez la page [Listes de prix, remises et formules](pricing.html) pour en
savoir plus sur la configuration des listes de prix.

## Auto-conversion à partir du prix public

Il convient de noter que le prix public affiché sur les produits est
directement lié à la devise principale de l’entreprise, qui est configurée en
allant à l’application Comptabilité ‣ Configuration ‣ Paramètres ‣ section
Devises ‣ Devise principale ‣ menu déroulant Devise.

Le prix de vente est automatiquement mis à jour si la liste de prix est
remplacée par une autre liste de prix dont la devise est différente de la
devise principale de l’entreprise. Le changement de prix est directement lié
au taux de conversion mis à jour pour cette devise.

## Fixer les prix des produits

Pour définir les prix des produits afin d’éviter toute modification des taux
de change, allez à l’application Ventes ‣ Produits ‣ Produits.

Sur la page Produits, sélectionnez le produit que vous voulez modifier. Ou
créez un nouveau produit en cliquant sur le bouton Nouveau.

Ensuite, sur le formulaire détaillé du produit, cliquez sur le bouton
intelligent Prix supplémentaires, situé dans le coin supérieur gauche. Cette
opération fait apparaître une page séparée Règles de prix, spécifique à ce
produit particulier.

![Comment définir les prix de produits basés sur des listes de prix en devise
étrangère dans Odoo Ventes.](../../../../../_images/price-rules-
currencies.png)

Cliquez sur Nouveau et sélectionnez la liste de prix souhaité dans le menu
déroulant dans la colonne Liste de prix.

Le champ Appliqué à est rempli automatiquement avec le produit, alors
saisissez les chiffres souhaités dans les champs Quantité min. et Prix.

Note

Le chiffre dans le champ Quantité min. signifie que le Prix défini ne sera
appliqué **que** si cette quantité de produit est achetée.

Si nécessaire, configurez une Date de début et une Date de fin pour les prix
définis. En laissant ces colonnes vides, le prix fixé restera valable, quelle
que soit la date de vente.

Si vous travaillez dans un environnement multi-sociétés, indiquez dans le
champ Société à quelle société cette règle de prix doit s’appliquer. En
laissant le champ vide, la règle de prix s’applique à toutes les entreprises
de la base de données.

Une fois ces configurations terminées, quelles que soient les
modifications/mises à jour de la conversion, chaque fois que ces listes de
prix sont appliquées à un client essayant d’acheter ce produit spécifique, ces
prix prédéterminés s’affichent.

Pour plus d'infos

[Listes de prix, remises et formules](pricing.html)

