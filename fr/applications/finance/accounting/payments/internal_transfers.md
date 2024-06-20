# Virements internes

Dans Odoo, vous pouvez effectuer des virements internes en quelques clics.
Vous avez besoin d’au moins deux comptes bancaires, deux journaux d’espèces ou
un compte bancaire et un journal d’espèces.

## Configuration

Un compte de virement interne est automatiquement créé dans votre base de
données en fonction de la localisation de votre entreprise et de la
législation de votre pays. Le cas échéant, le compte de virement interne par
défaut peut être modifié en allant à l’application Comptabilité ‣
Configuration ‣ Paramètres, dans la section Comptes par défaut.

Note

Vous avez besoin d’au moins deux comptes bancaires pour effectuer des
virements internes. Consultez la [section relative aux comptes de banque et
d’espèces](../bank.html) pour savoir comment ajouter un compte bancaire
supplémentaire à votre base de données.

## Enregistrer un virement interne d’une banque à une autre

Disons que vous avez deux comptes bancaires enregistrés dans votre base de
données et que vous voulez verser 1.000 USD de la Banque A à la Banque B.

### Enregistrer un virement interne

Dans le Tableau de bord de Comptabilité, cliquez sur le bouton du menu
déroulant (⋮) d’une de vos banques. Dans la colonne Nouveau, cliquez sur
Virement interne et saisissez les informations relatives au virement.

![Complétez les informations relatives à votre virement
interne](../../../../_images/internal_transfer.png)

Note

Remplissez le champ Mémo pour un rapprochement automatique.

Enregistrez et confirmez pour enregistrer votre virement interne. L’argent est
maintenant comptabilisé dans le compte de virement et un autre paiement est
**automatiquement** créé dans le journal de destination (Banque B).

#### Journal de banque (Banque A)

**Compte** | **Débit** | **Crédit**  
---|---|---  
Compte de paiements sortants en suspens |  | 1.000 $  
**Compte de virement interne** | **1.000 $** |   
  
#### Comptabilisation automatisée - Journal de banque (BANQUE B)

**Compte** | **Débit** | **Crédit**  
---|---|---  
Compte de paiements entrants en suspens | 1.000 $ |   
**Compte de virement interne** |  | **1.000 $**  
  
Note

Un paiement sortant en suspens et un paiement entrant en suspens sont en
attente dans les journaux de vos deux comptes bancaires, parce que le relevé
bancaire confirmant l’envoi et la réception de l’argent n’a pas encore été
enregistré.

![Paiements sortants/entrants en suspens en attendant l'enregistrement du
relevé bancaire](../../../../_images/outstanding-payments-receipts.png)

### Gérer et rapprocher les relevés bancaires

L’étape suivante consiste à enregistrer les relevés bancaires pour finaliser
la transaction en créant, [en important](../bank/transactions.html), ou [en
synchronisant](../bank/bank_synchronization.html) vos Lignes de transactions.
Remplissez le Solde final et cliquez sur le bouton Rapprocher.

![Lignes de transaction à remplir avant le
rapprochement](../../../../_images/transactions-line.png)

Pour plus d'infos

[Rapprochement bancaire](../bank/reconciliation.html)

Dans la fenêtre suivante, choisissez les contreparties du paiement - dans cet
exemple, le compte de paiements sortants en suspens - puis cliquez sur
Valider.

![Rapprocher votre paiement](../../../../_images/bank-reconciliation.png)

#### Écriture comptable

**Compte** | **Débit** | **Crédit**  
---|---|---  
Paiement sortant en suspens | 1.000 $ |   
Compte bancaire (BANQUE A) |  | **1.000 $**  
  
Vous devez répéter les mêmes étapes dès que vous recevez le relevé bancaire
associé à la Banque. Enregistre et rapprochez vos lignes de relevé bancaire.

#### Écriture comptable

**Compte** | **Débit** | **Crédit**  
---|---|---  
Paiement entrant en suspens |  | 1.000 $  
Compte bancaire (BANQUE B) | **1.000 $** | 

