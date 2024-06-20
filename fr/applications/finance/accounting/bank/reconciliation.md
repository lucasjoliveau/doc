# Rapprochement bancaire

Le **Rapprochement bancaire** est le processus de rapprocher vos [transactions
bancaires](transactions.html) avec vos enregistrements commerciaux, tels que
les [factures clients](../customer_invoices.html), les [factures
fournisseurs](../vendor_bills.html), et les [paiements](../payments.html). Non
seulement ce processus est obligatoire pour la plupart des entreprises, mais
il offre également plusieurs avantages, tels que la réduction du risque
d’erreurs dans les rapports financiers, la détection des activités
frauduleuses et l’amélioration de la gestion des flux de trésorerie.

Grâce aux [modèles de rapprochement](reconciliation_models.html) bancaire,
Odoo présélectionne automatiquement les écritures correspondantes.

Pour plus d'infos

  * [Odoo Tutoriels : Rapprochement bancaire](https://www.odoo.com/slides/slide/bank-reconciliation-2724)

  * [Synchronisation bancaire](bank_synchronization.html)

  * [Transactions](transactions.html)

## Vue du rapprochement bancaire

Pour accéder à la **vue de rapprochement** d’un journal de banque, allez à
votre tableau de bord de comptabilité et :

  * cliquez sur le nom du journal (par ex. Banque) pour afficher toutes les transactions, y compris celles qui ont déjà été rapprochées, ou

  * cliquez sur le bouton Rapprocher articles pour afficher toutes les transactions qu’Odoo a présélectionnées pour le rapprochement. Vous pouvez supprimer le filtre Non lettré de la barre de recherche pour inclure les transactions qui ont déjà été rapprochées.

![Accéder à l'outil de rapprochement bancaire à partir de votre tableau de
bord de comptabilité](../../../../_images/bank-card.png)

La vue de rapprochement bancaire est structurée en trois sessions distinctes :
les transactions, les écritures de contrepartie et l’écriture résultante.

![L'interface utilisateur de la vue de rapprochement d'un journal de
banque.](../../../../_images/user-interface.png)

Transactions

    

La section des transactions sur la gauche répertorie toutes les transactions
bancaires, les plus récentes étant affichées en premier. Cliquez sur une
transaction pour la sélectionner.

Écritures de contrepartie

    

La section des écritures de contrepartie, en bas à droite, affiche les options
pour rapprocher la transaction bancaire sélectionné. Plusieurs onglets sont
disponibles, tels que Rapprocher des écritures existantes, Paiements par lot,
Opérations manuelles, et Discussion, qui contient le chatter de la transaction
bancaire sélectionnée.

Écriture résultante

    

The resulting entry section on the top right displays the selected bank
transaction matched with the counterpart entries and includes any remaining
debits or credits. In this section, you can validate the reconciliation or
mark it as To Check. Any reconciliation model buttons are also available in
the resulting entry section.

## Rapprocher des transactions

Transactions can be matched automatically with the use of [reconciliation
models](reconciliation_models.html), or they can be matched with existing
entries, batch payments, manual operations, and reconciliation model buttons.

  1. Sélectionnez une transaction parmi les transactions bancaires non rapprochées.

  2. Define the counterpart. There are several options for defining a counterpart, including matching existing entries, manual operations, batch payments, and reconciliation model buttons.

  3. Si l’écriture résultante n’est pas totalement équilibrée, équilibrez-la en ajoutant une autre écriture de contrepartie existante ou en l’annulant à l’aide d’une opération manuelle.

  4. Cliquez sur le bouton Valider pour confirmer le rapprochement et passez à la transaction suivante.

Astuce

Si vous ne savez pas comment rapprocher une transaction particulière et que
vous souhaitez la traiter plus tard, utilisez plutôt le bouton À vérifier.
Toutes les transactions marquées comme À vérifier peuvent être affichées à
l’aide du filtre À vérifier.

Note

Les transactions bancaires sont comptabilisées sur le **compte d’attente du
journal** jusqu’au rapprochement. À ce stade, le rapprochement modifie la
pièce comptable de la transaction en remplaçant le compte d’attente de la
banque par le compte de créance, de dettes ou en suspens correspondant.

### Rapprocher des écritures existantes

This tab contains matching entries Odoo automatically pre-selects according to
the reconciliation models. The entry order is based on [reconciliation
models](reconciliation_models.html), with suggested entries appearing first.

Astuce

La barre de recherche dans l’onglet Rapprocher des écritures existantes vous
permet de rechercher des écritures comptables spécifiques.

### Paiements par lot

Les [Paiements par lot](payments/batch-payments) vous permettent de regrouper
plusieurs paiements pour faciliter le rapprochement. Utilisez l’onglet
Paiements par lot pour trouver des paiements par lot pour les clients et les
fournisseurs. Tout comme l’onglet Rapprocher des écritures existantes,
l’onglet Paiements par lot a une barre de recherche qui vous permet de
rechercher des paiements par lot spécifiques.

### Opérations manuelles

S’il n’y a pas d’écriture existante pour rapprocher la transaction
sélectionnée, il se peut que vous vouliez rapprocher la transaction
manuellement en sélectionnant le bon compte et le bon montant. Complétez
ensuite tous les champs optionnels pertinents.

Astuce

Vous pouvez utiliser l’option entièrement payé pour rapprocher un paiement,
même si vous n’avez reçu qu’un paiement partiel. Une nouvelle ligne apparaît
dans la section de l’écriture résultante pour refléter le solde ouvert
enregistré par défaut sur le compte client. Vous pouvez choisir un autre
compte en cliquant sur la nouvelle ligne dans la section de l’écriture
résultante et en sélectionnant le Compte pour comptabiliser le solde ouvert.

![Cliquez sur entièrement payé pour définir manuellement une facture comme
entièrement payée.](../../../../_images/fully-paid.png)

### Boutons des modèles de rapprochement

Use a [reconciliation model](reconciliation_models.html) button for manual
operations that are frequently used. These custom buttons allow you to quickly
reconcile bank transactions manually and can also be used in combination with
existing entries.

