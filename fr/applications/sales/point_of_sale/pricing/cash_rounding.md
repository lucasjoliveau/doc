# Arrondi des paiements en espèces

**L’arrondi des paiements en espèces** est requis lorsque la plus petite
devise physique, ou la plus petite pièce de monnaie, est supérieure à la plus
petite unité de compte.

Par exemple, certains pays demandent aux entreprises d’arrondir le total de
leurs factures aux cinq centimes les plus proches, lorsque le paiement est
effectué en espèces.

Chaque point de vente dans Odoo peut être configuré pour appliquer l’arrondi
des paiements en espèces aux totaux de ses factures ou de ses reçus.

## Configuration

Allez à Point de vente ‣ Configuration ‣ Paramètres et activez l’option
_Arrondi des paiements en espèces_ , puis cliquez sur _Enregistrer_.

![../../../../_images/cash_rounding011.png](../../../../_images/cash_rounding011.png)

Allez à Point de vente ‣ Configuration ‣ Points de vente, ouvrez le point de
vente à configurer et activez l’option _Arrondi des paiements en espèces_.

Pour définir la **Méthode d’arrondi** , ouvrez la liste déroulante et cliquez
sur _Créer et modifier…_.

Définissez-y votre _Précision d’arrondi_ , votre _Compte de profit_ et votre
_Compte de perte_ , puis enregistrez les deux méthodes d’arrondi dans les
paramètres de votre Point de Vente.

![../../../../_images/cash_rounding02.png](../../../../_images/cash_rounding02.png)

Désormais, une ligne est ajoutée à tous les montants totaux de ce point de
vente pour appliquer l’arrondi selon vos paramètres.

![../../../../_images/cash_rounding03.png](../../../../_images/cash_rounding03.png)

Note

Le Point de Vente d’Odoo ne prend en charge que la stratégie d’arrondi Ajotuer
une ligne d’arrondi.

