# Payer avec SEPA

SEPA, l’espace unique de paiements en euros, est une initiative d’intégration
des paiements de l’Union européenne visant à simplifier les virements
bancaires en euros. SEPA vous permet d’envoyer des ordres de paiement à votre
banque afin d’automatiser les virements bancaires.

Le SEPA est pris en charge par les banques des 27 États membres de l’Union
européenne, ainsi que par :

les pays AELE :

  * Islande ;

  * Liechtenstein ;

  * Norvège ;

  * Suisse.

Pays SEPA non-EEE :

  * Andorre ;

  * Monaco ;

  * Saint-Marin ;

  * Royaume-Uni ;

  * Vatican.

Territoires non-EEE :

  * Saint-Pierre-et-Miquelon ;

  * Guernesey ;

  * Jersey ;

  * Île de Man.

Lorsque vous payez une facture fournisseur dans Odoo, vous pouvez sélectionner
les mandats SEPA en tant qu’option de paiement. À la fin de la journée, vous
pouvez générer le fichier SEPA contenant tous les virements bancaires et
l’envoyer à la banque.

Par défaut, le fichier respecte les spécifications **“pain.001.001.03”** du
virement SEPA. Il s’agit d’une norme bien définie entre les banques.
Toutefois, pour les entreprises suisses et allemandes, d’autres formats sont
utilisés : **“pain.001.001.03.ch.02”** pour la Suisse et **“pain.001.003.03”**
pour l’Allemagne.

Une fois que les paiements sont traités par votre banque, vous pouvez
directement importer le relevé de compte dans Odoo. Le processus de
rapprochement bancaire fera correspondre de manière transparente les ordres
SEPA que vous avez envoyés à votre banque avec les relevés bancaires
effectifs.

## Configuration

### Activer les virements SEPA (SEPA Credit Transfer - SCT)

Pour payer les fournisseurs avec SEPA, vous devez activer le paramètre
**Virement SEPA**. Pour ce faire, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Paiements fournisseurs : virement SEPA (SCT). En activant le
paramètre et en complétant les données de votre entreprise, vous pourrez
utiliser l’option SCT lors du paiement de votre fournisseur.

Note

En fonction du package de localisation installé, les modules **Prélèvement
SEPA** et **Virement SEPA** peuvent être installés par défaut. Si ce n’est pas
le cas, il faut les [installer](../../../general/apps_modules.html#general-
install).

### Activer les modes de paiement SEPA sur les banques

À partir du tableau de bord de comptabilité, cliquez sur le menu déroulant (⋮)
de votre journal de banque et sélectionnez Configuration. Cliquez sur l’onglet
des Paiements sortants et, si ce n’est pas déjà le cas, ajoutez Virement SEPA
dans Mode de paiement.

Assurez-vous de préciser le numéro de compte IBAN (numéros de compte nationaux
ne fonctionnent pas avec SEPA) et le BIC (code d’identification de banque)
dans l’onglet Pièces comptables.

### Enregistrer des paiements

Il est possible d’enregistrer les paiements fournisseurs effectués par SEPA.
Pour ce faire, allez à Comptabilité ‣ Fournisseurs ‣ Paiements. Lorsque vous
créez votre paiement, sélectionnez Virement SEPA en tant que Mode de paiement.

La première fois que vous payez un fournisseur par SEPA, vous devez compléter
le champ Compte bancaire du destinataire avec le nom de la banque, l’IBAN et
le BIC (Code d’identification de la banque). Odoo vérifie automatiquement si
le format IBAN est respecté.

Pour les paiements futurs à ce fournisseur, Odoo vous proposera
automatiquement le compte bancaire, mais vous serez en mesure d’en
sélectionner un nouveau.

Une fois que votre paiement est enregistré, n’oubliez pas de le confirmer.
Vous pouvez également payer les factures fournisseurs directement depuis la
facture en cliquant sur le bouton Enregistrer un paiement en haut d’une
facture fournisseur. Le formulaire est le même, mais le paiement est
directement lié à la facture et sera automatiquement lettré avec elle.

