# Chèques

Il y a deux façons de traiter les paiements reçus par chèque dans Konvergo ERP, soit
en utilisant les comptes en suspens, soit en contournant le processus de
rapprochement.

**Il est recommandé d’utiliser les comptes en suspens** , car le solde de
votre compte bancaire reste exact en prenant en compte les chèques qui doivent
encore être encaissés.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les deux méthodes génèrent les mêmes données dans votre comptabilité à la fin du processus. Mais si vous avez des chèques qui n’ont pas encore été encaissés, la méthode des <b>Comptes en suspens</b> rapporte ces chèques dans le compte des <b>Paiements entrants en suspens</b>. Toutefois, les fonds apparaissent sur votre compte bancaire, qu’ils soient rapprochés ou non, puisque la valeur bancaire est reflétée au moment du relevé bancaire.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../bank#bank-outstanding-accounts"><span class="std std-ref">Comptes en suspens</span></a></p></li>
<li><p><a href="../get_started/cheat_sheet#accounting-reconciliation"><span class="std std-ref">Rapprochement bancaire</span></a></p></li>
</ul>
</div>

## Méthode 1 : Compte en suspens

Lorsque vous recevez un chèque, vous [enregistrez un
paiement](../bank/reconciliation) par chèque sur la facture. Ensuite,
lorsque votre compte bancaire est crédité du montant du chèque, vous
rapprochez le paiement et le relevé pour déplacer le montant du compte des
**Paiements entrants en suspens** au compte de **Banque**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez créer un nouveau mode de paiement intitulé <em>Chèques</em> si vous souhaitez identifier rapidement ce type de paiement. Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux ‣ Banque, cliquez sur l’onglet <b>Paiements entrants</b> et <b>Ajouter une ligne</b>. En tant que <b>Mode de paiement</b>, sélectionnez <b>Manuel</b>, saisissez <code>Chèques</code> comme nom et <b>Enregistrez</b>.</p>
</div>

## Méthode 2 : Contournement du rapprochement

Lorsque vous recevez un chèque, vous [enregistrez un
paiement](../bank/reconciliation) sur la facture concernée. Le montant
est ensuite déplacé du **Compte client** au compte **Banque** , en contournant
le rapprochement et en créant **une seule pièce comptable**.

Pour ce faire, vous _devez_ suivre la configuration suivante. Allez à
Comptabilité ‣ Configuration ‣ Journaux ‣ Banque. Cliquez sur l’onglet
**Paiements entrants** , puis sur **Ajouter un ligne** , sélectionnez
**Manuel** en tant que **Mode de paiement** , et saisissez `Chèques` comme
**Nom**. Cliquez sur le bouton bascule, cochez **Compte de paiements entrants
en suspens** et dans la colonne **Compte de paiements entrants en suspens** ,
définissez le compte **Banque** en tant que mode de paiement **Chèques**.

![Contournez le compte des paiements entrants en suspens en utilisant le
compte Banque.](../../../../_images/outstanding-payment-accounts.png)

## Enregistrement des paiements

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Par défaut, il y a deux façons d’enregistrer des paiements effectués par chèque :</p>
<ul>
<li><p><b>Manuel</b> : pour les chèques uniques ;</p></li>
<li><p><b>Par lot</b> : pour plusieurs chèques à la fois.</p></li>
</ul>
<p>Cette documentation se concentre sur les paiements <b>par chèque unique</b>. Pour les <b>dépôts par lot</b>, consultez la <a href="batch">documentation relative aux paiements par lot</a>.</p>
</div>

Lorsque vous recevez un chèque d’un client, allez à la facture concernée
(Comptabilité ‣ Client ‣ Factures) et cliquez sur **Enregistrer un paiement**.
Remplissez les informations relatives au paiement :

  * **Journal : Banque** ;

  * **Mode de paiement** : **Manuel** (ou **Chèques** si vous avez créé un mode de paiement spécifique) ;

  * **Mémo** : saisissez le numéro du chèque ;

  * Cliquez sur **Créer un paiement**.

![Informations sur le paiement par chèque](../../../../_images/payment-
checks.png)

Les pièces comptables générées sont différentes en fonction de la méthode
d’enregistrement du paiement choisie.

## Pièces comptables

### Compte en suspens

La facture est marquée comme **En paiement** dès que vous enregistrez le
paiement. Cette opération génère la **pièce comptable** suivante :

Compte | Correspondance relevé | Débit | Crédit  
---|---|---|---  
Compte client |  |  | 100,00  
Paiements entrants en suspens |  | 100,00 |   
  
Ensuite, une fois que vous recevez les relevés bancaires, faites correspondre
ce relevé avec le chèque du compte des **paiements entrants en suspens**.
Cette opération génère la **pièce comptable** suivante :

Compte | Correspondance relevé | Débit | Crédit  
---|---|---|---  
Paiements entrants en suspens | X |  | 100,00  
Banque |  | 100,00 |   
  
Si vous utilisez cette méthode pour gérer les chèques reçus, vous verrez la
liste des chèques qui n’ont pas encore été encaissés dans le compte des
**paiements entrants en suspens** (accessible, par exemple, depuis le grand
livre).

### Contournement du rapprochement

La facture est marquée comme **Payée** dès que vous enregistrez le chèque.

Grâce à cette méthode, vous contournez l’utilisation des **comptes en
suspens** , obtenant effectivement une seule pièce comptable dans vos livres
et contournant ainsi le rapprochement :

Compte | Correspondance relevé | Débit | Crédit  
---|---|---|---  
Compte client | X |  | 100,00  
Banque |  | 100,00 | 

