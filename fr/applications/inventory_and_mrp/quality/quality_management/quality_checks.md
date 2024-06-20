# Contrôles qualité

Les contrôles qualité sont des inspections manuelles effectuées par les
employés et sont utilisés pour assurer la qualité des produits. Dans Odoo, un
contrôle qualité peut être effectué pour un seul produit ou pour plusieurs
produits d’une même opération d’inventaire ou ordre de fabrication.

Using a Quality Control Point (QCP), it is possible to create quality checks
automatically at regular intervals. When quality checks are created by a QCP,
they appear on a manufacturing or inventory order, where the employee
processing the order will be prompted to complete them. For a full explanation
of how to create and configure a QCP, see the documentation on [quality
control points](quality_control_points.html#quality-quality-management-
quality-control-points).

Bien que les contrôles qualité soient le plus souvent créés automatiquement
par un |PCQ|, il est également possible de créer un contrôle qualité unique
manuellement. La création manuelle d’un contrôle est utile lorsqu’un employé
souhaite programmer un contrôle qualité qui n’aurait lieu qu’une seule fois,
ou enregistrer un contrôle qualité qu’il effectue sans y être invité.

## Contrôle qualité manuel

Pour manuellement créer un seul contrôle qualité, allez à Qualité ‣ Contrôle
qualité ‣ Contrôles qualité, et cliquez sur Nouveau. Sur le formulaire du
contrôle qualité, sélectionnez une option dans le menu déroulant Contrôle par
:

  * Opération demande un contrôle pour l’ensemble d’une opération (par ex. bon de livraison) et tous les produits qu’elle contient.

  * Produit demande un contrôle pour chaque unité d’un produit faisant partie d’une opération (par ex. chaque unité d’un produit d’un bon de livraison).

  * Qualité représente un contrôle pour chaque quantité d’un produit faisant partie d’une opération (par ex. un contrôle pour cinq unités d’un produit d’un bon de livraison). La sélection de Quantité fait également apparaître un menu déroulant Lot/série, où vous pouvez sélectionner un lot ou un numéro de série spécifique pour lequel le contrôle qualité doit être effectué.

Sélectionnez ensuite une opération d’inventaire dans le menu déroulant
Transfert ou un ordre de fabrication dans le menu déroulant Ordre de
production. Ceci est nécessaire, car Odoo a besoin de savoir pour quelle
opération le contrôle qualité est effectué.

Si le contrôle qualité doit être attribué à un |PCQ| spécifique, sélectionnez-
le dans le menu déroulant Point de contrôle. Ceci est utile si le contrôle
qualité est créé manuellement, mais qu’il doit quand même être reconnu comme
appartenant à un |PCQ| spécifique.

Sélectionnez un type de contrôle qualité dans le menu déroulant Type :

  * Instructions fournit des instructions spécifiques sur la manière d’effectuer le contrôle qualité.

  * Prendre une photo exige qu’une photo soit jointe au contrôle avant que celui-ci ne puisse être effectué.

  * Réussite - Échec est utilisé lorsque le produit contrôle doit répondre à certains critères pour réussir le contrôle.

  * La sélection de Mesure fait apparaître un champ de saisie Mesure, dans lequel une mesure doit être saisie avant que le contrôle ne puisse être effectué.

  * La sélection de Feuille de travail fait apparaître un menu déroulant Modèle qualité. Il permet de sélectionner une feuille de travail de qualité à remplir pour effectuer le contrôle.

Dans le champ Équipe, sélectionnez l’équipe de qualité responsable du contrôle
qualité. Dans le champ Société, sélectionnez la société propriétaire du
produit inspecté.

Dans l’onglet Notes au bas du formulaire, saisissez toutes les instructions
pertinentes dans le champ de saisie Instructions (par ex. “Joindre une photo
du produit”). Dans le champ de saisie Notes, saisissez toutes les informations
pertinentes sur le contrôle qualité (qui l’a créé, pourquoi, etc.).

Enfin, si le contrôle est traité immédiatement, cliquez sur le bouton Réussite
en haut à gauche de l’écran si le contrôle est réussi ou sur le bouton Échec
si le contrôle est échoué.

![Un formulaire de contrôle qualité complété pour un contrôle Réussite -
Échec.](../../../../_images/quality-check-form1.png)

## Traiter un contrôle qualité

Les contrôles qualité peuvent être traités directement sur la page du contrôle
qualité, ou à partir d’un ordre de fabrication ou d’inventaire pour lequel une
contrôle est exigé. Par ailleurs, si un contrôle qualité est créé pour une
opération spécifique de l’ordre de travail, le contrôle est traité dans la vue
de tablette de l’ordre de travail.

Note

It is not possible to manually create a single quality check that is assigned
to a specific work order operation. Quality checks for work order operations
can only be created by a QCP. See the documentation on [Quality Control
Points](quality_control_points.html#quality-quality-management-quality-
control-points) for information about how to configure a QCP that will create
quality checks for a specific work order operation.

### Page de contrôle qualité

Pour traiter un contrôle qualité à partir de la page de contrôle, allez à
Qualité ‣ Contrôle qualité ‣ Contrôles qualité, puis sélectionnez le contrôle
à traiter. Suivez les instructions relatives à la réalisation du contrôle, qui
figurent dans le champ Instructions de l’onglet Notes au bas de la page.

Si le contrôle qualité réussit, cliquez sur le bouton Réussite en haut de la
page. Si le contrôle échoue, cliquez plutôt sur le bouton Échec.

### Contrôle qualité sur un ordre

Pour traiter un contrôle qualité sur un ordre, sélectionnez un ordre de
fabrication ou d’inventaire (réception, livraison, retour, etc.), pour lequel
un contrôle est nécessaire. Vous pouvez sélectionner des ordres de fabrication
en allant à Fabrication ‣ Opérations ‣ Ordres de fabrication, et en cliquant
sur un ordre. Les ordres d’inventaire peuvent être sélectionnés en allant à
Inventaire, en cliquant sur le bouton # À traiter sur une carte d’opération et
en sélectionnant un ordre.

Sur l’ordre de fabrication ou d’inventaire sélectionné, un bouton mauve
Contrôles qualité apparaît en haut de l’ordre. Cliquez sur le bouton pour
ouvrir la fenêtre contextuelle Contrôle qualité, qui montre tous les contrôles
qualité requis pour cet ordre.

Suivez les instructions qui s’affichent dans la fenêtre contextuelle Contrôle
qualité. Si un contrôle Réussite - Échec est en cours, complétez le contrôle
en cliquant sur Réussite ou Échec au bas de la fenêtre contextuelle. Pour tous
les autres types de contrôle qualité, un bouton Valider s’affiche. Cliquez
dessus pour terminer le contrôle.

![La fenêtre contextuelle "Contrôle qualité" sur un ordre de
fabrication.](../../../../_images/quality-check-pop-up1.png)

### Contrôle qualité sur un ordre de travail

Pour traiter un contrôle qualité sur un ordre de travail, allez à Fabrication
‣ Opérations ‣ Ordres de fabrication, puis sélectionnez un ordre de
fabrication. Sélectionnez l’onglet Ordres de travail et cliquez sur le bouton
de la vue de tablette 📱 (tablette) pour l’ordre de travail qui nécessite le
contrôle qualité.

Dans la vue tablette, effectuez les étapes répertoriées à gauche de l’écran
jusqu’à l’étape du contrôle qualité, puis suivez les instructions en haut de
l’écran. Si un contrôle Réussite - Échec est en cours, terminez le contrôle en
cliquant sur Réussite ou Échec en haut de l’écran. Pour tous les autres types
de contrôle qualité, un bouton Suivant s’affiche. Cliquez dessus pour terminer
le contrôle et passer à l’étape suivante de l’ordre de travail.

![Un contrôle qualité sur un ordre de travail.](../../../../_images/work-
order-check.png)

  *[QCP]: Quality Control Point

