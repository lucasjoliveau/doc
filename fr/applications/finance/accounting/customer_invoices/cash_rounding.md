# Arrondi des paiements en espèces

**L’arrondi des paiements en espèces** est requis lorsque la plus petite
devise physique, ou la plus petite monnaie, est supérieure à la plus petite
unité de compte.

Par exemple, certains pays demandent aux entreprises d’arrondir le total de
leurs factures de cinq cents vers le haut ou vers le bas lorsque le paiement
se fait en espèces.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres et activez l’option _Arrondi
des paiements en espèces_ , puis cliquez sur _Enregistrer_.

![../../../../_images/cash_rounding01.png](../../../../_images/cash_rounding01.png)

Allez à Comptabilité ‣ Configuration ‣ Arrondi des paiements en espèces, et
cliquez sur _Créer_.

Définissez ici la _Précision d’arrondi_ , la _Stratégie d’arrondi_ et la
_Méthode d’arrondi_.

Odoo prend en charge deux **stratégies d’arrondi** :

  1. **Ajouter une ligne d’arrondi** : une ligne d” _arrondi_ est ajoutée à la facture. Vous devez définir quel compte enregistre les arrondis des paiements en espèces.

  2. **Modifier le montant des taxes** : l’arrondi est appliqué dans la section des taxes.

## Appliquer les arrondis

Lors de la modification d’une facture brouillon, ouvrez l’onglet _Autres
informations_ , allez à la section _Comptabilité_ et sélectionnez la _Méthode
d’arrondi des paiements en espèces_ appropriée.

