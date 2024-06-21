# Créer des alertes qualité

La configuration des points de contrôle qualité est un excellent moyen de
s’assurer que des contrôles de qualité sont effectués à des étapes de routine
au cours d’opérations spécifiques. Cependant, des problèmes de qualité peuvent
souvent apparaître en dehors de ces contrôles planifiés. En utilisant Konvergo ERP
_Qualité_ , les utilisateurs peuvent créer des alertes qualité pour les
problèmes qui ne sont pas détectés par les processus automatisés.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="quality_control_points">Ajouter des points de contrôle qualité</a></p>
</div>

## Compléter le formulaire d’alerte qualité

Dans certaines situations, il faut manuellement créer des alertes qualité dans
le module _Qualité_.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Un utilisateur du service d’assistance qui est informé d’un défaut de produit par un ticket client peut créer une alerte qui porte le problème à l’attention de l’équipe qualité concernée.</p>
</div>

Pour créer une nouvelle alerte qualité, allez à l’application Qualité et
sélectionnez Contrôle qualité ‣ Alertes qualité ‣ Créer. Le formulaire
d’alerte qualité peut être complété comme suit :

  * **Titre** : choisissez un titre concis, mais descriptif pour l’alerte qualité

  * **Produit** : le produit pour lequel l’alerte qualité est créée

  * **Variante de produit** : la variante spécifique du produit qui a le problème de qualité, le cas échéant

  * **Lot** : le numéro de lot assigné au produit

  * **Poste de travail** : le poste de travail d’où provient le problème de qualité

  * **Transfert** : l’opération de transfert pendant lequel est survenu le problème de qualité

  * **Équipe** : l’équipe de qualité qui sera informée de l’alerte qualité

  * **Responsable** : la personne responsable de la gestion de l’alerte qualité

  * **Étiquettes** : classer l’alerte qualité en fonction des étiquettes créées par l’utilisateur

  * **Cause première** : la cause du problème de qualité, si elle est connue

  * **Priorité** : assigner une priorité entre une ou trois étoiles pour s’assurer que les problèmes les plus urgents sont traités en priorité

Vous pouvez utiliser les onglets en bas du formulaire pour fournir des
informations supplémentaires aux équipes de qualité :

  * **Description** : fournir plus de détails sur le problème de qualité

  * **Mesures correctives** : méthode de correction des produits concernés

  * **Mesures préventives** : procédures visant à éviter que le problème ne se reproduise à l’avenir

  * **Divers** : le fournisseur du produit (le cas échéant), l’entreprise qui fabrique le produit et la date d’assignation

![Un exemple de formulaire d'alerte qualité
complété.](../../../../_images/quality-alert-form.png)

## Ajouter des alertes qualité pendant le processus de fabrication

Konvergo ERP permet aux employés de fabrication de créer des alertes qualité au sein
d’un ordre de travail sans accéder au module _Qualité_. À partir de la vue
tablette de l’ordre de travail, cliquez sur l’icône :guilabel:` ☰ ` du menu
hamburger dans le coin supérieur gauche et sélectionnez **Alerte qualité**.

![Accédez au menu de l'ordre de travail.](../../../../_images/work-order-
tablet-view-menu-button.png)

Le formulaire d’alerte qualité peut ensuite être complété comme il est
détaillé dans la section précédente. Après avoir sauvegardé le formulaire, une
nouvelle alerte apparaîtra dans le tableau de bord des **Alertes qualité** qui
se trouvent dans le menu Qualité ‣ Contrôle qualité.

## Gérer les alertes qualité existantes

Par défaut, les alertes qualité sont organisées dans un tableau de bord
kanban. Les étapes du tableau kanban sont entièrement personnalisables et les
alertes peuvent être déplacées d’une étape à une autre par glisser-déposer ou
en cliquant sur chaque alerte. D’autres options sont disponibles pour afficher
les alertes, y compris les vues graphique, calendrier et tableau croisé
dynamique.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Filtrez les alertes en fonction de divers critères, tels que la date d’assignation ou la date de clôture. Il est également possible de regrouper les alertes par équipe de qualité, cause première ou d’autres paramètres qui figurent dans le menu <b>Filtres</b>.</p>
</div>

