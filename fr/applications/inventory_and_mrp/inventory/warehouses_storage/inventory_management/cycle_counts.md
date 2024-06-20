# Comptages cycliques

Pour la plupart des entreprises, l’inventaire de l’entrepôt ne doit être
compté qu’une fois par an. C’est pourquoi, par défaut, après avoir effectué un
_ajustement d’inventaire_ dans Odoo, la date prévue pour le prochain
inventaire est fixée au 31 décembre de l’année en cours.

Toutefois, pour certaines entreprises, il est essentiel d’avoir un inventaire
précis à tout moment. Ces entreprises utilisent des _comptages cycliques_ pour
maintenir des niveaux de stocks critiques exacts. Le comptage cyclique est une
méthode permettant aux entreprises de compter leurs stocks plus souvent dans
certains _emplacements_ , afin de s’assurer que leurs inventaires physiques
correspondent à leurs enregistrements d’inventaire.

## Activer les emplacements de stockage

Dans Odoo, les comptages cycliques sont basés sur l’emplacement. Par
conséquent, la fonctionnalité _emplacements de stockage_ doit être activée
avant d’effectuer un comptage cyclique.

Pour activer cette fonctionnalité, allez à l’application Inventaire ‣
Configuration ‣ Paramètres, et faites défiler jusqu’à la section Entrepôt.
Cliquez ensuite sur la case à côté d”Emplacements de stockage. Cliquez sur
Enregistrer pour enregistrer tous les changements.

![Paramètre des emplacements de stockage activé dans les paramètres
d'inventaire.](../../../../../_images/cycle-counts-enabled-setting.png)

## Modifier la fréquence d’inventaire par emplacement

Une fois que le paramètre des emplacements de stockage est activé, la
fréquence d’inventaire peut être modifiée pour des emplacements spécifiques
créés dans l’entrepôt.

Pour afficher et modifier les emplacements, allez à l’application Inventaire ‣
Configuration ‣ Emplacements. Une page Emplacements s’ouvre en contient tous
les emplacements actuellement créés et répertoriés dans l’entrepôt.

Sur cette page, cliquez sur un emplacement pour afficher la page des
paramètres de cet emplacement. Cliquez sur Modifier pour modifier les
paramètres d’emplacement.

Dans la section Inventaire cyclique, trouvez le champ Fréquence de
l’inventaire (Jours) qui devrait être défini sur `0` (si cet emplacement n’a
pas été modifié auparavant). Modifiez la valeur dans le champ pour obtenir le
nombre de jours souhaité.

![Paramètre de la fréquence de l'inventaire sur
l'emplacement.](../../../../../_images/cycle-counts-location-frequency.png)

Example

Pour un emplacement nécessitant un inventaire tous les 30 jours, la Valeur de
la fréquence (Jours) doit être définie sur `30`.

Une fois que la fréquence a été modifiée en fonction du nombre de jours
souhaité, cliquez sur Enregistrer pour enregistrer les changements. Désormais,
lorsqu’un ajustement d’inventaire est appliqué à cet emplacement, la prochaine
date d’inventaire prévue est automatiquement fixée, en fonction de la valeur
saisie dans le champ Fréquence de l’inventaire (Jours).

## Comptage de l’inventaire par emplacement

Pour effectuer un comptage cyclique pour un emplacement spécifique dans
l’entrepôt, allez à l’application Inventaire ‣ Opérations ‣ Ajustements
d’inventaire. Une page Ajustements d’inventaire s’affiche et contient tous les
produits actuellement en stock, chaque produit étant répertorié sur sa propre
ligne.

Sur cette page, vous pouvez utiliser les boutons Filtres et Regrouper par (en
haut de la page, sous la barre Rechercher…) pour sélectionner des emplacements
spécifiques et effectuer des comptages d’inventaire.

![Page des ajustements d'inventaire.](../../../../../_images/cycle-counts-
inventory-adjustments-page.png)

Pour sélectionner un emplacement spécifique et voir tous les produits qui s’y
trouvent, cliquez sur Regrouper par et cliquez sur Ajouter un groupe
personnalisé pour afficher un nouveau menu déroulant sur la droite.

Cliquez sur Emplacement dans le menu déroulant, puis cliquez sur Appliquer. La
page montre à présent des menus déroulants condensés pour chaque emplacement
de l’entrepôt qui a des produits en stock, et un comptage cyclique peut être
effectué pour tous les produits de cet emplacement.

Astuce

Dans les grands entrepôts ayant plusieurs emplacements et un volume important
de produits, il peut être plus facile de rechercher l’emplacement spécifique
souhaité. Pour ce faire, sur la page des Ajustements d’inventaire, cliquez sur
Filtres. Puis cliquez sur Ajouter un filtre personnalisé pour afficher un
nouveau menu sur la droite. Cliquez sur ce menu pour faire apparaître trois
menus déroulants.

Pour le premier champ, sélectionnez Emplacement dans le menu déroulant. Pour
le deuxième champ, laissez la valeur contient inchangée. Pour le troisième
champ, tapez le nom de l’emplacement que vous recherchez. Cliquez sur
Appliquer pour que cet emplacement apparaisse sur la page.

![Filtres et Regrouper par sur la page des ajustements
d'inventaire.](../../../../../_images/cycle-counts-filters.png)

## Modifier la fréquence des inventaires complets

Bien que les comptages cycliques soient généralement effectués par
emplacement, la date prévue pour les inventaires complets de tout ce qui est
en stock dans l’entrepôt peut également être modifiée manuellement pour
avancer la date.

Pour modifier la date prévue par défaut, allez à l’application Inventaire ‣
Configuration ‣ Paramètres. Dans la section Opérations, localisez le champ
Jour et mois de l’inventaire annuel qui contient un menu déroulant défini le
`31` décembre par défaut.

![Champ de fréquence dans les paramètres de l'application
Inventaire.](../../../../../_images/cycle-counts-frequency-settings.png)

Pour modifier le jour, cliquez sur `31`, et remplacez-le par un jour compris
entre `1 et 31`, en fonction du mois de l’année souhaité.

Pour modifier le mois, cliquez sur Décembre pour faire apparaître le menu
déroulant et sélectionnez le mois souhaité.

Une fois que tous les changements ont été apportés, cliquez sur Enregistrer
pour enregistrer tous les changements.

Pour plus d'infos

[Ajustements d’inventaire](count_products.html)

