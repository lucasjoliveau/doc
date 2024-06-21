# Comptabilité analytique

La comptabilité analytique vous permet de suivre les coûts et les revenus et
d’analyser la rentabilité d’un projet ou d’un service. Lors de la création de
vos pièces comptables, le widget analytique permet de distribuer les coûts
dans un ou plusieurs comptes analytiques.

## Configuration

Activez la fonctionnalité **Comptabilité analytique** en allant à Comptabilité
‣ Configuration ‣ Paramètres ‣ Analytique.

## Comptes analytiques

Les compte analytiques vous donnent un aperçu de vos coûts et vos revenus.

Accédez à vos comptes analytiques existants en allant à Comptabilité ‣
Configuration ‣ Comptabilité analytique : Comptes analytiques. Pour créer un
nouveau compte analytique, cliquez sur **Nouveau** et complétez les
informations requises :

  * **Compte analytique** : ajoutez le nom de votre compte analytique ;

  * **Client** : sélectionnez le client associé à votre projet ;

  * **Référence** : ajoutez une référence pour trouver votre compte plus facilement sur votre facture fournisseur ;

  * **Plan** : ajoutez un plan analytique ;

  * **Société** : si vous gérez plusieurs sociétés, sélectionnez la société pour laquelle le compte analytique sera utilisé ;

  * **Devise** : sélectionnez la devise du compte analytique ;

Complétez ensuite les informations relatives à votre [budget](budget).

## Plans analytiques

Les plans analytiques vous permettent d’analyser votre comptabilité. Par
exemple, pour suivre les coûts et les revenus par projet ou par département.

Vous pouvez accéder aux plans analytiques en allant à Comptabilité ‣
Configuration ‣ Comptabilité analytique : Plans analytiques. Cliquez sur
**Nouveau** pour créer un nouveau plan.

![créez un plan analytique](../../../../_images/analytic_plans.png)

Vous devez compléter les informations suivantes :

  * **Parent** : liez votre plan à un autre **Plan analytique** pour établir une hiérarchie entre vos plans ;

  * **Application par défaut** : décidez comment votre plan se comporte dans le widget lors de la création d’une nouvelle pièce comptable :

>     * **Facultatif** : si cette option est sélectionnée, il n’est pas
> obligatoire d’ajouter le plan analytique au widget ;
>
>     * **Obligatoire** : si cette option est sélectionnée, une puce orange
> est visible dans le widget à côté du plan jusqu’à ce que la distribution
> analytique est terminée (la puce devient alors verte) ; il est impossible de
> confirmer l’écriture si aucun compte analytique n’est sélectionné ;
>
>     * **Non disponible** : si cette option est sélectionnée, le plan n’est
> pas disponible dans le widget.

  * **Couleur** : sélectionnez la couleur de l’étiquette associée à ce plan spécifique ;

  * **Société** : ajoutez la société à laquelle le plan s’applique ;

Vous pouvez également affiner l’application de vos plans en complétant
l’onglet **Applicabilité** :

  * **Domaine** : choisissez à quel document comptable votre plan s’applique ;

  * **Préfixe des comptes financiers** : sélectionnez le préfixe du (des) compte(s) au(x)quel(s) ce plan doit s’appliquer ;

  * **Catégorie de produits** : déterminez à quelle catégorie de produits le plan s’applique ;

  * **Applicabilité** : décidez comment votre plan se comporte dans le widget lors de la création d’une nouvelle pièce comptable.
    

L’applicabilité définie ici prime toujours sur l’applicabilité par défaut.

Deux boutons intelligents s’affichent dans le coin supérieur droit :

>   * **Sous-plans** : peuvent être créés pour obtenir une structure
> analytique plus complexe. Cliquez sur le bouton intelligent **Sous-plans**
> et puis sur **Nouveau** pour ajouter un sous-plan ;
>
>   * **Comptes analytiques** : pour aller aux comptes analytiques associés au
> plan.
>
>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Le widget analytique est prérempli sur la base de l’applicabilité et les <a href="#analytic-distribution-models"><span class="std std-ref">Modèles de distribution analytique</span></a> ;</p></li>
<li><p>Chaque plan analytique doit avoir au moins un compte analytique.</p></li>
</ul>
</div>

## Distribution analytique

Ajoutez un plan dans la colonne **Analytique** lors de la création d’une
facture client ou une facture fournisseur. Ce champ est uniquement obligatoire
si vous avez précédemment associé votre plan analytique à au moins un compte
analytique. Après avoir ajouté le plan, un **widget** s’ouvre et vous pouvez
compléter les différentes informations requises. Vous pouvez ajouter des
**étiquettes** pour refléter les comptes analytiques associés et décider
comment ventiler les coûts entre les comptes en modifiant le pourcentage.

![créez un modèle de
distribution](../../../../_images/analytic_distribution.png)

### Modèles de distribution analytique

Les modèles de distribution analytique appliquent automatiquement une
distribution spécifique sur la base de critères définis.

Pour créer un nouveau modèle de distribution analytique, allez à Comptabilité
‣ Configuration ‣ Modèles de distribution analytique, cliquez sur **Nouveau**
et définissez les conditions auxquelles votre modèle doit répondre pour
s’appliquer automatiquement :

  * **Préfixe des comptes** : cette distribution analytique s’appliquera à tous les comptes financiers avec ce préfixe ;

  * **Partenaire** : sélectionnez un partenaire pour lequel la distribution analytique sera utilisée ;

  * **Catégorie de partenaires** : ce champ n’est pas visible par défaut ; ajoutez-le en cliquant sur le bouton de sélection de colonnes et cochez la case **Catégorie de partenaires**. Ajoutez la catégorie de partenaires pour laquelle la distribution analytique sera utilisée ;

  * **Produit** : sélectionnez un produit pour lequel la distribution analytique sera utilisée ;

  * **Catégorie de produits** : ce champ n’est pas visible par défaut ; ajoutez-le en cliquant sur le bouton de sélection de colonnes et cochez la case **Catégorie de produits**. Sélectionnez la catégorie de produits pour laquelle la distribution analytique sera utilisée ;

  * **Analytique** : ajoutez les comptes analytiques et leur distribution ;

  * **Société** : sélectionnez une société pour laquelle la distribution analytique sera utilisée ;

  * **Distribution analytique** : si les conditions définies ci-dessus sont réunies, le **Plan analytique** défini dans ce champ et la distribution à appliquer entre les différents comptes analytiques sont sélectionnés automatiquement sur l’écriture.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour <b>modifier</b> plusieurs écritures en même temps, allez à Comptabilité ‣ Comptabilité ‣ Écritures comptables et sélectionnez celles qui doivent être mises à jour. Ajoutez la distribution requise dans la colonne <b>Distribution analytique</b> et cliquez sur l’icône de <b>disquette</b> pour enregistrer. Le modèle de distribution analytique s’affiche et vous pouvez l’enregistrer pour le réutiliser ultérieurement.</p>
</div>

