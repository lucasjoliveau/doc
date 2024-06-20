# Suisse

## BVR (bulletin de versement avec numéro de référence)

Les BVR sont des bulletins de paiement utilisés en Suisse. Vous pouvez les
imprimer directement depuis Odoo. Sur les factures clients, il y a un nouveau
bouton intitulé _Imprimer BVR_.

![../../../_images/switzerland00.png](../../../_images/switzerland00.png)

Astuce

Le bouton _Imprimer BVR_ s’affiche uniquement lorsqu’un compte bancaire est
défini sur la facture. Vous pouvez utiliser CH6309000000250097798 en tant que
numéro de compte bancaire et 010391391 en tant que référence BVR CHF.

![../../../_images/switzerland01.png](../../../_images/switzerland01.png)

Ouvrez ensuite un pdf avec le BVR.

![../../../_images/switzerland02.png](../../../_images/switzerland02.png)

Il existe deux présentations pour le BVR : l’une avec et l’autre sans les
coordonnées bancaires. Pour choisir l’une ou l’autre, il existe une option
permettant d’imprimer les informations bancaires sur le BVR. Pour l’activer,
allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Factures clients et
activez **Imprimer la banque sur le BVR** :

![../../../_images/switzerland03.png](../../../_images/switzerland03.png)

### Référence BVR sur les factures

Pour faciliter le processus de lettrage, vous pouvez ajouter votre référence
BVR en tant que **Référence de paiement** sur vos factures.

Pour ce faire, vous devez configurer le Journal que vous utilisez
habituellement pour émettre des factures. Allez à Comptabilité ‣ Configuration
‣ Journaux, ouvrez le Journal que vous souhaitez modifier (par défaut, le
Journal est intitulé _Factures clients_), cliquez sur _Modifier_ et ouvrez
l’onglet _Paramètres avancés_. Dans le champ **Standard de référence** ,
sélectionnez la _Suisse_ et cliquez sur _Enregistrer_.

![Configurez votre Journal pour afficher votre BVR en tant que référence de
paiement sur vos factures dans Odoo](../../../_images/switzerland-isr-
reference.png)

## Mise à jour du taux de change en direct

Vous pouvez automatiquement mettre à jour vos taux de change en fonction de
l’Administration fédérale des contributions de la Suisse. Pour ce faire, allez
à Comptabilité ‣ Paramètres, activez le paramètre multi-devises et choisissez
le service que vous souhaitez.

![../../../_images/switzerland04.png](../../../_images/switzerland04.png)

## Mise à jour de la TVA à partir de janvier 2018

À partir du 1 janvier 2018, de nouveaux taux de TVA réduits sont appliqués en
Suisse. Le taux normal de 8,0% passe à 7,7% et le taux spécifique au secteur
hôtelier passe de 3,8% à 3,7%.

### Comment mettre à jour vos taxes dans Odoo Enterprise (Odoo Online ou On-
premise) ?

Si vous êtes sur la version V11.1, vous n’avez rien à faire.

Si vous avez démarré sur une version antérieure, vous devez d’abord mettre à
jour le module « Suisse - Rapports comptables ». Pour cela, allez aux Apps ‣
supprimez le filtre « Apps » ‣ recherchez « Suisse - Rapports comptables » ‣
ouvrez le module ‣ et cliquez sur « mettre à niveau ».

![../../../_images/switzerland05.png](../../../_images/switzerland05.png)

Une fois que cela est fait, vous pouvez créer de nouvelles taxes pour les taux
mis à jour.

Astuce

**Ne supprimez ou ne modifiez pas les taux existants** (8,0% ou 3,8%). Vous
devez les conserver, puisqu’il se peut que vous deviez utiliser les deux taux
pendant une courte période. Pensez plutôt à les archiver une fois que vous
aurez encodé toutes vos transactions de 2017.

La création de ces taxes doit se faire de la manière suivante :

  * **Taxes sur les achats** : copier la taxe d’origine, copier son nom, le libellé sur la facture, le taux et le groupe de taxes (uniquement en vigueur à partir de la version 10)

  * **Taxes sur les ventes** : copier la taxe d’origine, modifier son nom, le libellé sur les factures, le taux et le groupe de taxes (uniquement en vigueur à partir de la version 10). Puisque la déclaration de TVA affiche désormais les détails pour les anciens et les nouveaux taux, vous devez également définir les étiquettes en conséquence pour

    * Pour des taxes de 7,7 % : Formulaire suisse pour la déclaration TVA : grille de base 302, Formulaire suisse pour la déclaration TVA : grille d’impôt 302

    * Pour des taxes de 3,7 % : Formulaire suisse pour la déclaration TVA : grille de base 342, Formulaire suisse pour la déclaration TVA : grille d’impôt 342

Vous trouverez ci-dessous, à titre d’exemple, la bonne configuration pour
toutes les taxes incluses par défaut dans Odoo.

**Nom de la taxe** | **Taux** | **Libellé sur les factures** | **Groupe de taxes (à partir de V10)** | **Portée de la taxe** | **Étiquette**  
---|---|---|---|---|---  
TVA 7,7 % sur les achats B&S (TN) | 7,7 % | 7,7 % achat | TVA 7,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 400  
TVA 7,7 % sur achat B&S (Incl. TN) | 7,7 % | 7,7 % achats Incl. | TVA 7,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 400  
TVA 7,7 % sur invest. et autres ch. (TN) | 7,7 % | 7,7 % invest. | TVA 7,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 405  
TVA 7,7 % sur invest. et autres ch. (Incl. TN) | 7,7 % | 7,7 % invest. Incl. | TVA 7,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 405  
TVA 3,7 % sur achat B&S (TS) | 3,7 % | 3,7 % achat | TVA 3,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 400  
TVA 3,7 % sur achat B&S (Incl. TS) | 3,7 % | 3,7 % achat Incl. | TVA 3,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 400  
TVA 3,7 % sur invest. et autres ch. (TS) | 3,7 % | 3,7 % invest | TVA 3,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 405  
TVA 3,7 % sur invest. et autres ch. (Incl. TS) | 3,7 % | 3,7 % invest Incl. | TVA 3,7 % | Achats | Formulaire suisse pour la déclaration TVA : grille 405  
TVA due à 7,7 % (TN) | 7,7 % | 7,7 % | TVA 7,7 % | Ventes | Formulaire suisse pour la déclaration TVA : grille de base 302, Formulaire suisse pour la déclaration TVA : grille d’impôt 302  
TVA due à 7,7 % (Incl. TN) | 7,7 % | 7,7 % Incl. | TVA 7,7 % | Ventes | Formulaire suisse pour la déclaration TVA : grille de base 302, Formulaire suisse pour la déclaration TVA : grille d’impôt 302  
TVA due à 3,7% (TS) | 3,7 % | 3,7 % | TVA 3,7 % | Ventes | Formulaire suisse pour la déclaration TVA : grille de base 342, Formulaire suisse pour la déclaration TVA : grille d’impôt 342  
TVA due à 3,7 % (Incl. TS) | 3,7 % | 3,7 % Incl. | TVA 3,7 % | Ventes | Formulaire suisse pour la déclaration TVA : grille de base 342, Formulaire suisse pour la déclaration TVA : grille d’impôt 342  
  
Si vous avez des questions ou des remarques, veuillez contacter notre
assistance via odoo.com/help.

Astuce

N’oubliez pas de mettre à jour vos positions fiscales. Si vous avez une
version 11.1 (ou supérieure), il n’y a rien à faire. Sinon, vous devrez
également mettre à jour vos positions fiscales en conséquence.

