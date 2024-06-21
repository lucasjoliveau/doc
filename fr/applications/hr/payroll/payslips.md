# Fiches de paie

Les fiches de paie sont créées par les employés eux-mêmes ou par leurs
managers et sont approuvées par des employés autorisés (généralement les
managers). Ensuite, une fois les fiches de paie approuvées, les employés
reçoivent leur fiche de paie et sont payés par chèque ou par virement, en
fonction de la configuration de leur profil employé.

L’en-tête déroulante **Fiches de paie** de l’application Paie contient trois
sections : **À payer** , **Toutes les fiches de paie** , et **Lots**.

Ces trois sections fournissent tous les outils nécessaires pour créer des
fiches de paie pour les employés, y compris les fiches de paie individuelles,
un lot de fiches de paie ou des fiches de paie de commissions.

![Menu de sélection Fiches de paie dans l'application
Paie.](../../../_images/payslips.png)

## À payer

Cliquez sur l’application Paie ‣ Fiches de paie ‣ À payer pour voir les fiches
de paie qui doivent être payées. Sur cette page, Konvergo ERP affiche les fiches de
paie qui n’ont pas encore été générées et qui peuvent être créées à partir de
ce tableau de bord.

![Visualisez toutes les fiches de paie qui doivent être payées sur la page des
fiches de paie à payer.](../../../_images/all-pay-slips.png)

Chaque fiche de paie répertorie le numéro de **Référence** de la fiche de paie
individuelle, le nom de l”**Employé** , le **Nom du lot** , les dates **De**
et **Au** , la **Société** , le **Salaire de base** , le **Salaire net** , et
le **Statut** de la fiche de paie.

Le fait de cliquer sur une entrée de fiche de paie individuelle permet
d’afficher les détails de cette fiche de paie individuelle.

### Créer une nouvelle fiche de paie

Vous pouvez créer une nouvelle fiche de paie à partir de la page **Fiches de
paie à payer** (app Paie ‣ Fiches de paie ‣ A payer) ou la page **Fiches de
paie des employés** (app Paie ‣ Fiches de paie ‣ Toutes les fiches de paie),
en cliquant sur le bouton **Créer** dans le coin supérieur gauche.

Après avoir cliqué sur **Créer** , un formulaire de fiche de paie vierge
s’ouvre dans lequel vous pouvez saisir toutes les informations nécessaires.

#### Champs obligatoires

Sur le formulaire de fiche de paie vierge, certains champs sont obligatoires
et doivent être complétés. Ces champs obligatoires sont affichés en **gras**.

![Les champs obligatoires d'une nouvelle fiche de paie.](../../../_images/new-
payslip.png)

  * **Employé** : Saisissez le nom d’un employé ou sélectionnez l’employé souhaité dans la liste déroulante. Après avoir sélectionné un employé, plusieurs autres champs de la fiche de paie pourraient se remplir automatiquement. Généralement, après avoir sélectionné l”**Employé** , Konvergo ERP remplit automatiquement les champs **Contrat** , **Structure** , et **Nom de la fiche de paie** , mais **seulement** si ces informations figurent déjà dans la fiche employé dans l’application _Employés_.

  * **Période** : Cliquez sur la date par défaut pour faire apparaître un calendrier. Sur ce calendrier, utilisez les icônes **< (inférieur à)** et **> (supérieur à)** pour sélectionner le mois souhaité et cliquez sur le jour souhaité pour sélectionner cette date spécifique comme date de début de la fiche de paie. Répétez les mêmes étapes pour ajouter une date de fin à la fiche de paie dans le champ suivant.

  * **Contrat** : À l’aide du menu déroulant, sélectionnez le contrat souhaité pour l’employé. Seuls les contrats correspondants disponibles pour l’employé sélectionné figurent parmi les options.

  * **Structure** : Sélectionnez le type de structure salariale dans le menu déroulant. Seules les structures correspondantes disponibles pour le contrat sélectionné pour cet employé spécifique figurent parmi les options.

  * **Nom de la fiche de paie** : Dans le champ vierge, tapez le nom de la fiche de paie. Le nom doit être court et descriptif, par exemple `Avril 2023`.

  * **Société** : Dans l’onglet **Informations comptables** , sélectionnez la société à laquelle la fiche de paie s’applique dans le menu déroulant **Société**.

  * **Journal des salaires** : Dans l’onglet **Informations comptables** , saisissez le journal des salaires dans lequel le paiement sera comptabilisé et qui se trouve dans l’application _Comptabilité_.

![Les champs obligatoires d'une nouvelle fiche de paie dans l'onglet
Informations comptables.](../../../_images/new-payslip-tab.png)
<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il est recommandé de vérifier auprès du département comptable que chaque entrée affectant l’application <em>Comptabilité</em> est correcte.</p>
</div>

#### Champs optionnels

  * **Référence** : Toute note ou référence pour la nouvelle entrée peut être saisie ici.

  * **Véhicule de société** : Le cas échéant, sélectionnez le véhicule de société dans le menu déroulant.

  * **Jours travaillés** : Dans l’onglet **Jours travaillés & Entrées**, les entrées sous **Jours travaillés** (y compris le **Type** , la **Description** , le **Nombre de jours** , le **Nombre d’heures** , et le **Montant**) sont remplies automatiquement, en fonction des champs **Période** , **Contrat** , et **Structure** de la fiche de paie.

  * **Calcul du salaire** : L’onglet **Calcul du salaire** est automatiquement complété après avoir cliqué sur le bouton **Calculer la feuille**. Ceci permet d’afficher tous les salaires, déductions, taxes, etc. de l’entrée.

  * **Nom du lot** : Dans l’onglet **Informations comptables** , sélectionnez le lot de fiches de paie auquel cette nouvelle fiche de paie doit être ajoutée dans le menu déroulant.

  * **Date de compte** : Dans l’onglet **Informations comptables** , saisissez la date à laquelle la fiche de paie doit être comptabilisée, en cliquent sur le menu déroulant et en naviguant au bon mois et à la bonne année à l’aide des icônes **< > (inférieur à/supérieur à)** dans le calendrier qui s’affiche. Cliquez ensuite sur la date souhaitée.

  * **Journal des salaires** : Ce champ, situé dans l’onglet **Informations comptables** , représente le journal dans lequel la fiche de paie sera enregistrée et est sélectionné automatiquement lorsque les champs **Contrat** et **Structure** sont complétés dans la fiche de paie.

  * **Entrée comptable** : Ce champ, situé dans l’onglet **Informations comptables** , est complété automatiquement dès que la fiche de paie est confirmée.

#### Enregistrer et traiter une nouvelle fiche de paie

Lorsque vous avez saisi toutes les informations nécessaires sur la fiche de
paie, cliquez sur **Enregistrer** pour enregistrer les données ou sur
**Ignorer** pour supprimer l’entrée.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il n’est pas obligatoire d’enregistrer l’entrée pour calculer la feuille, bien qu’il soit préférable de le faire. Vous pouvez cliquer sur le bouton <b>Calculer la feuille</b> sans enregistrer la fiche de paie au préalable. Vous enregistrez ainsi l’entrée <em>et</em> vous calculez la feuille.</p>
</div>

Cliquez sur le bouton **Calculer la feuille** pour enregistrer toutes les
informations et remplir l’onglet **Calcul du salaire**. Si vous devez apporter
des modifications, cliquez sur le bouton **Modifier** , effectuez les
modifications nécessaires et cliquez sur le bouton **Recalculer les jours
travaillés** pour refléter les changements dans les onglets **Jours
travaillés** et **Calcul du salaire**.

Pour imprimer la fiche de paie, cliquez sur le bouton **Imprimer**. Pour
annuler la fiche de paie, cliquez sur le bouton **Annuler la fiche de paie**.

Une fois que tous les éléments de la fiche de paie sont corrects, cliquez sur
le bouton **Créer une entrée brouillon** pour créer la fiche de paie. Le
chatter est automatiquement mis à jour pour afficher l’email envoyé à
l’employé, avec la copie PDF de la fiche de paie.

![La nouvelle fiche de paie est envoyée par email à l'employé et l'email
s'affiche dans le chatter.](../../../_images/payslip-chatter.png)

Ensuite, le paiement doit être envoyé à l’employé. Pour ce faire, cliquez sur
le bouton **Exécuter le paiement**. Un formulaire contextuel s’ouvre, dans
lequel vous pouvez sélectionner le **Journal de banque** souhaité sur lequel
le paiement doit être effectué dans le menu déroulant. Cliquez ensuite sur le
bouton **Confirmer** pour confirmer le journal et revenir à la fiche de paie.

![Cliquez sur Exécuter le paiement pour envoyer le paiement à
l'employé.](../../../_images/make-payment.png)

Si un paiement doit être annulé ou remboursé, cliquez sur le bouton
**Rembourser** ou **Annuler la fiche de paie** , situé en haut de la fiche de
paie.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour qu’une fiche de paie puisse être payée, l’employé <em>doit</em> saisir un compte bancaire dans ses coordonnées. En l’absence d’informations bancaires, il est impossible de payer une fiche de paie et une erreur apparaît en cliquant sur le bouton <b>Exécuter le paiement</b>. Les informations bancaires se trouvent dans l’onglet <b>Informations privées</b> de la fiche de l’employé. Modifiez la fiche de l’employé et ajoutez les informations bancaires si elles sont manquantes.</p>
<img alt="Vous pouvez saisir les informations bancaires sur la fiche de l'employé." class="align-center" src="../../../_images/banking.png"/>
</div>

## Toutes les fiches de paie

Pour afficher toutes les fiches de paie, indépendamment de leur statut, allez
à l’application Paie ‣ Fiches de paie ‣ Toutes les fiches de paie. Toutes les
fiches de paie y sont organisées par lot (dans une vue de liste par défaut).

Cliquez sur la flèche **▶** à côté du nom du lot individuel pour afficher
toutes les fiches de paie de ce lot en particulier, ainsi que tous les
détails. Le nombre de fiches de paie dans le lot est noté entre parenthèses
après le nom du lot. Le **Statut** de chaque fiche de paie individuelle
s’affiche à l’extrême droite, indiquant si elle est en **Brouillon** , **En
attente** , ou si c’est **Fait**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p><b>Brouillon</b> indique que la fiche de paie est créée et qu’il est toujours possible de la modifier, puisque les montants ne sont pas encore calculés.</p></li>
<li><p><code>En attente</code> indique que la fiche de paie a été calculée et que les détails du salaire figurent dans l’onglet <em>Calcul du salaire</em>.</p></li>
<li><p><code>Fait</code> indique que la fiche de paie est calculée et prête à être payée.</p></li>
</ul>
</div> ![Visualisez toutes les fiches de paie organisées par
lots. Cliquez sur la flèche pour développer chaque lot.](../../../_images/all-
payslips.png)

Cliquez sur une fiche de paie individuelle pour voir les détails de cette
fiche dans une page séparée. À l’aide du fil d’Ariane, cliquez sur **Fiches de
paie des employés** pour revenir à la vue de liste de toutes les fiches de
paie.

Une nouvelle fiche de paie peut être créée à partir de la page **Fiches de
paie des employés** , en cliquant sur le bouton **Créer** dans le coin
supérieur gauche. Un formulaire de fiche de paie vierge s’ouvre alors.
Saisissez-y toutes les informations nécessaires, comme indiqué dans la section
Créer une nouvelle fiche de paie.

Pour imprimer des versions PDF des fiches de paie à partir des pages **Fiches
de paie à payer** ou **Fiches de paie des employés** , sélectionnez d’abord
les fiches de paie souhaitées en cochant la case à côté de chaque fiche de
paie à imprimer. Vous pouvez également cocher la case à côté de **Référence**
, ce qui permet de sélectionner toutes les fiches de paie visibles sur la
page. Cliquez ensuite sur le bouton **Imprimer** pour imprimer les fiches de
paie.

![Cliquez sur le bouton intelligent Imprimer pour imprimer les fiches de paie
au format PDF.](../../../_images/print.png)

Les fiches de paie peuvent aussi être exportées vers une feuille de calcul
Excel. Lors de l’exportation, toutes les fiches de paie sont exportées, que
certaines soient sélectionnées ou non. Cliquez sur le bouton **Exporter tout**
(icône de téléchargement) pour exporter toutes les fiches de paie vers une
feuille de calcul Excel.

![Cliquez sur le bouton intelligent Exporter tout pour exporter toutes les
fiches de paie vers une fiche de paie Excel.](../../../_images/export.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les options <em>À payer</em> et <em>Toutes les fiches de paie</em> affichent toutes deux les informations détaillées de chaque fiche de paie.</p>
</div>

## Lots

Pour voir les fiches de paie par lots, allez à l’application Paie ‣ Fiches de
paie ‣ Lots pour afficher tous les lots de fiches de paie qui ont été créés.
Ces lots s’affichent par défaut dans une vue de liste.

Chaque lot affiche le **Nom** , la **Date de début** et la **Date de fin** ,
s’il s’agit d’un **Avoir** , son **Statut** , et la **Société**.

![Vue affichant tous les lots créés.](../../../_images/batches.png)

Cliquez sur un lot individuel pour voir les détails de ce lot sur une page
séparée. Sur cette page de détail des lots, il est possible d’apporter des
modifications en cliquant sur le bouton **Modifier**. Procédez ensuite à
toutes les modifications nécessaires.

Lorsque toutes les modifications souhaitées ont été apportées, cliquez sur
**Enregistrer** pour enregistrer les modifications ou sur **Ignorer** pour
revenir aux données d’origine.

Une fois les modifications enregistrées, cliquez sur le bouton **Générer les
fiches de paie** pour faire apparaître un formulaire contextuel **Générer les
fiches de paie** dans lequel vous pouvez créer ou modifier les fiches de paie
affectées par les modifications.

Toutes les fiches de paie associées au lot sont affichées dans la section
employés de la fenêtre contextuelle **Générer les fiches de paie**. Pour
filtrer les résultats par **Structure salariale** et/ou par **Département** ,
sélectionnez une structure salariale et/ou un département dans les menus
déroulants respectifs.

Seuls les employés qui correspondent à la **Structure salariale** et/ou au
**Département** sélectionnés apparaissent dans la liste des employés. Cliquez
sur le bouton **Générer** au bas de la fenêtre contextuelle **Générer les
fiches de paie** pour générer les fiches de paie modifiées et fermer la
fenêtre contextuelle.

![Générez des fiches de paie à partir du lot
modifié.](../../../_images/generate-payslips-batch.png)

De retour sur la page des détails du lot, cliquez sur le bouton intelligent
**Créer une entrée brouillon** pour créer un brouillon des fiches de paie.

![Générez des fiches de paie à partir du lot modifié.](../../../_images/draft-
from-batch.png)

Une fois les fiches de paie brouillon créées, le bouton devient **Exécuter le
paiement**. Cliquez sur le bouton **Exécuter le paiement**. Une fenêtre
contextuelle s’ouvre, dans laquelle vous devez saisir les informations
bancaires. Sélectionnez le **Journal de banque** dans la liste déroulante et
cliquez sur **Confirmer** pour traiter les fiches de paie et payer les
employés.

Sur la page de détails du lot, le nombre de fiches de paie dans le lot est
accessible via le bouton intelligent **Fiches de paie** , situé dans le coin
supérieur droit. Les fiches de paie individuelles du lot peuvent être
visualisées en cliquant sur le bouton intelligent **Fiches de paie** dans le
coin supérieur droit.

Utilisez le fil d’Ariane pour revenir à la page de détails du lot individuel
ou à la liste de tous les lots.

![Cliquez sur le bouton intelligent Fiches de paie pour voir les fiches de
paie individuelles du lot.](../../../_images/payslip-batches.png)

### Créer un nouveau lot

Pour créer un nouveau lot de fiches de paie à partir de la page **Lots de
fiches de paie** (app Paie ‣ Fiches de paie ‣ Lots), cliquez sur le bouton
**Créer** dans le coin supérieur gauche. Un formulaire de lot de fiches de
paie vierge s’ouvre dans une page séparée.

Sur le formulaire de lot de fiches de paie, donnez un **Nom** au lot et
sélectionnez la plage de dates à laquelle le lot s’applique, en cliquant sur
l’icône **▼ (menu déroulant)** dans les champs **Période** , révélant ainsi un
calendrier. Dans cette fenêtre contextuelle, allez au bon mois et cliquez sur
le jour correspondant aux dates de début et de fin.

![Saisissez les détails du nouveau lot.](../../../_images/new-batch-
details.png)

Si le lot est un avoir, cochez la case à côté d”**Avoir**. Puis, dans le champ
**Date de génération** , sélectionnez la date à laquelle les fiches de paie
doivent être générées dans un calendrier. Cette date générée est reprise dans
les pièces comptables.

Enfin, dans le champ **Société** , sélectionnez la société pour laquelle ces
fiches de paie sont établies.

Lorsque toutes les informations figurant sur le lot de fiches de paie sont
correctes, cliquez sur le bouton **Enregistrer** pour enregistrer les
informations. Pour supprimer l’entrée, cliquez sur le bouton **Ignorer**.

Pour créer les fiches de paie du lot nouvellement créé, cliquez sur le bouton
**Générer les fiches de paie** en haut du formulaire.

Une fenêtre contextuelle s’affiche alors, indiquant toutes les fiches de paie
qui seront créées. Pour supprimer des fiches de paie individuelles, cliquez
sur l’icône noire **✖** à l’extrême droite de la ligne de la fiche de paie.

Si vous devez préciser une **Structure salariale** ou un **Département** pour
le lot, sélectionnez-les dans les menus déroulants correspondants.

Cliquez sur le bouton **Générer** au bas de la fenêtre contextuelle pour créer
la fiche de paie du lot.

![Générer les fiches de paie du nouveau lot.](../../../_images/generate-
payslips.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Dans la fenêtre contextuelle <b>Générer les fiches de paie</b>, la sélection d’un <b>Département</b> et/ou d’une <b>Structure salariale</b> n’affiche que les fiches de paie qui s’appliquent à ces paramètres spécifiquement sélectionnés.</p>
</div>

Si des erreurs ou des problèmes empêchant la génération des fiches de paie, un
message d’erreur apparaît dans la partie supérieure droite. Cette boîte
d’erreur disparaît d’elle-même au bout de quelques secondes, ou cliquez sur
l’icône **✖** pour fermer l’avertissement.

Pour remédier au problème, effectuez les modifications nécessaires (par ex.
supprimez les lignes de la fiche de paie qui ne peuvent pas être traitées),
puis cliquez à nouveau sur le bouton **Générer**.

Lorsque les fiches de paie ont été générées avec succès, l’écran revient au
formulaire de lot de fiches de paie.

À partir de là, cliquez le bouton **Générer une entrée brouillon** pour faire
passer le statut des fiches de paie de **Brouillon** à **Fait**.

Une fois les fiches de paie générées, cliquez sur le bouton **Exécuter le
paiement** pour traiter les paiements. Une fenêtre contextuelle s’ouvre, dans
laquelle les informations bancaires appropriées doivent être saisies. Dans
cette fenêtre contextuelle, sélectionnez le **Journal de banque** dans le menu
déroulant et saisissez le nom de fichier adéquat.

Lorsque vous avez terminé, cliquez sur le bouton **Confirmer** pour confirmer
les informations ou cliquez sur **Annuler** pour ne pas les saisir.

### Générer les fiches de paie de commissions

Les fiches de paie de commissions peuvent être générées directement à partir
de la page **Lots de fiches de paie** (app Paie ‣ Fiches de paie ‣ Lots). Pour
générer des fiches de paie de commissions à partir de cette page, cliquez sur
le(s) lot(s) souhaité(s) pour créer des fiches de paie de commissions, puis
cliquez sur le bouton **Générer les fiches de paie de commissions**.

Une fenêtre contextuelle **Générer une fiche de paie de commission** s’ouvre,
dans laquelle vous **devez** remplir les informations nécessaires.

![Saisissez les détails de la commission.](../../../_images/commission-
details.png)

Dans cette fenêtre contextuelle, cliquez sur les mens déroulants situés à côté
du champ **Période** pour faire apparaître des fenêtres contextuelles de
calendrier. Dans ces fenêtres, sélectionnez la période souhaitée pour laquelle
les fiches de paie sont générées. En utilisant les flèches **< (gauche)** et
**> (droite)**, allez au bon mois et cliquez sur la date pour la sélectionner.

Dans le champ **Département** , sélectionnez le département souhaité dans le
menu déroulant.

Lorsqu’un département est sélectionné, les employés répertoriés pour ce
département apparaissent dans la section **Employé**.

Dans la section **Employé** , saisissez le **Montant de commission** de chaque
employé dans la colonne appropriée. Pour supprimer un employé, cliquez sur
l’icône **🗑️ (corbeille)** pour supprimer la ligne.

Ajoutez une nouvelle entrée en cliquant sur **Ajouter un ligne** et en
saisissant l”**Employé** et le **Montant de la commission** approprié.

Cliquez sur le bouton **Charger votre fichier** pour ajouter un fichier, le
cas échéant. Tous les types de fichiers sont acceptés.

À l’aide du menu déroulant à côté du champ **Type de commission** ,
sélectionnez **Commission classique** ou **Warrant**. La commission
**classique** est la plus courante, tandis que le **Warrant** est
principalement utilisé par les entreprises belges.

Une fois que toutes les commissions ont été correctement saisies, cliquez sur
le bouton **Générer les fiches de paie** pour créer les fiches de paie des
commissions.

