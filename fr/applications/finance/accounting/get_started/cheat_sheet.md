# Aide-mémoire de la comptabilité

Le **Bilan** est un aperçu des finances de la société à une date spécifique
(contrairement au compte de résultat, qui propose une analyse sur une
période).

  * Les **actifs** représentent la richesse de la société et les biens qui lui appartiennent. Les immobilisations corporelles incluent les bâtiments et les bureaux, alors que les actifs circulants incluent les comptes bancaires et les espèces. L’argent dû par un client est un actif. Un employé n’est pas un actif.

  * Les **passifs** sont des obligations d’événements passés que la société devra payer à l’avenir (factures de services d’utilité publique, dettes, fournisseurs impayés). Le passif peut également être défini comme une source de financement fournie à la société, également appelé _levier financier_.

  * Les **fonds propres** représentent le montant des fonds apportés par les propriétaires de la société (fondateurs ou actionnaires) plus les bénéfices (ou pertes) non distribués. Chaque année, les bénéfices (ou pertes) nets peuvent être reportés comme bénéfices non distribués ou distribués aux actionnaires (en tant que dividende).

Ce qui est possédé (un actif) a été financé par des dettes à rembourser
(passif) ou des fonds propres (bénéfices, capital).

Une distinction est faite entre les **actifs** et les **charges** :

    

  * Un **actif** est une ressource ayant une valeur économique qu’un individu, une société ou un pays possède ou contrôle dans l’attente d’un avantage futur. Les actifs sont inscrits au bilan d’une entreprise. Ils sont achetés ou créés pour augmenter la valeur de l’entreprise ou pour bénéficier à ses activités.

  * Une **charge** est le coût des opérations qu’une entreprise supporte pour générer des recettes.

Le **compte de résultat** montre la performance de l’entreprise sur une
période donnée, généralement un trimestre ou un exercice fiscal.

>   * Les **produits** correspondent à l’argent gagné par la société en
> vendant des biens et/ou des services.
>
>   * Le **coût des marchandises vendues** (COGS ou « Coût des ventes »)
> correspond aux coûts de la vente des marchandises (par ex. le coût des
> matières premières et de la main-d’œuvre utilisés pour créer les
> marchandises).
>
>     * Le **Bénéfice brut** est égal aux produits des ventes moins le coût
> des marchandises vendues.
>
>     * Les **Charges d’exploitation** (OPEX) incluent les salaires des
> services administratifs, de vente et de R&D, les loyers et les services
> d’utilité publique, les frais divers, les assurances, ainsi que tous les
> coûts autres que le coût des produits vendus ou le coût des ventes.
>
>

> Actifs = Passifs + Fonds propres

## Plan comptable

Le **plan comptable** répertorie tous les comptes de la société : les comptes
de bilan et les comptes de résultat. Chaque transaction est enregistrée en
débitant et en créditant plusieurs comptes dans une pièce comptable. Le plan
comptable est en quelque sorte l’ADN de l’entreprise !

Chaque compte répertorié dans le plan comptable appartient à une catégorie
spécifique. Dans Odoo, chaque compte a un code unique et appartient à une de
ces catégories :

  * **Fonds propres et emprunts subordonnés**
    
    * Les **fonds propres** représentent le montant d’argent investi par les actionnaires d’une société pour financer les activités de la société.

    * Les **dettes subordonnés** représentent le montant d’argent prêté par un tiers à une société pour financer ses activités. En cas de dissolution de la société, ces tiers sont remboursés avant les actionnaires.

  * Les **immobilisations** sont des éléments ou des biens tangibles (c’est-à-dire physiques) qu’une société achète et utilise pour produire ses biens et ses services. Les immobilisations sont des actifs à long terme. Cela signifie que les actifs ont une durée de vie utile de plus d’un an. Elles incluent les propriétés, les usines et les équipements (également connus sous le nom d’immobilisations corporelles) et sont inscrites au bilan avec cette classification.

  * **Actifs et passifs circulants**
    
    * Le compte de l”**actif circulant** est un poste du bilan figurant dans la section Actifs, qui comptabilise tous les actifs appartenant à la société qui peuvent être convertis en liquidité dans un délai d’un an. Les actifs circulants comprennent les liquidités, les équivalents de liquidités, les créances, les stocks, les titres négociables, les dettes payées d’avance et autres actifs liquides.

    * Les **passifs circulants** sont les obligations financières à court terme d’une société échéant dans l’année. Un exemple d’un passif circulant est l’argent dû aux fournisseurs sous la forme de dettes.

  * **Compte bancaire et compte en espèces**
    
    * Un **compte bancaire** est un compte financier tenu par une banque ou un autre établissement financier dans lequel sont enregistrées les transactions financières entre la banque et un client.

    * Un **compte en espèces** , ou un livre de caisse, peut désigner un grand livre dans lequel sont enregistrées toutes les transactions en espèces. Le compte en espèces comprend à la fois les journaux d’encaissement et de décaissement.

  * **Charges et produits**
    
    * Une **charge** est le coût des opérations qu’une société supporte pour générer des recettes. Elle se définit simplement comme le coût que l’on doit dépenser pour obtenir quelque chose. Parmi les charges habituelles figurent les paiements aux fournisseurs, les salaires des employés, les contrats de location d’usine et l’amortissement des équipements.

    * Le terme de « **produits** » désigne généralement le montant d’argent, de biens et d’autres transferts de valeur reçus au cours d’une période donnée en échange de services ou de produits.

### Exemple

*: Les cases Remboursement client et Paiement client ne peuvent pas être cochées en même temps, puisqu’elles sont contradictoires.

> Solde = Débit - Crédit

## Pièces comptables

Chaque document financier de la société (par ex. une facture, un relevé
bancaire, une fiche de paie, un contrat d’augmentation de capital) est
enregistré comme une pièce comptable, impactant plusieurs comptes.

Pour qu’une pièce comptable soit équilibrée, la somme de tous ses débits doit
être égale à la somme de tous ses crédits.

exemples d’écritures pour diverses transactions. (voir entries.js)

## Lettrage

Le [lettrage](../bank/reconciliation.html) est le processus qui consiste à
relier les écritures comptables d’un compte spécifique et à faire correspondre
les crédits et les débits.

Son objectif premier est de relier les paiements à leurs factures
correspondantes afin de les marquer comme étant payées. Pour ce faire, un
lettrage est effectué sur le compte des créances et/ou le compte des dettes.

Le lettrage est effectué automatiquement par le système quand :

  * le paiement est enregistré directement sur la facture

  * les liens entre les paiements et les factures sont détectés automatiquement lors du rapprochement bancaire

Exemple de relevé client

Comptes clients | Débit | Crédit  
---|---|---  
Facture 1 | 100 |   
Paiement partiel 1/2 |  | 70  
Facture 2 | 65 |   
Paiement partiel 2/2 |  | 30  
Paiement 2 |  | 65  
Facture 3 | 50 |   
|  |   
Total à payer | 50 |   
  
## Rapprochement bancaire

Le rapprochement bancaire est la correspondance des lignes de relevé bancaire
(fournis par votre banque) avec les transactions enregistrées en interne
(paiements aux fournisseurs ou des clients). Chaque ligne d’un relevé bancaire
peut être :

  * **rapprochée avec un paiement enregistré précédemment** : un paiement est enregistré lors de la réception d’un chèque d’un client, puis rapproché lors de la vérification du relevé bancaire.

  * **enregistrée comme un nouveau paiement** : l’écriture du paiement est créée et rapprochée avec la facture correspondante lors du traitement du relevé bancaire.

  * **enregistrée comme une autre transaction** : virement bancaire, prélèvement automatique, etc.

Odoo devrait rapprocher automatiquement la plupart des transactions : seules
quelques unes devraient nécessiter un examen manuel. À la fin du processus de
rapprochement bancaire, le solde du compte bancaire dans Odoo doit
correspondre au solde du relevé bancaire.

## Traitement des chèques

Il existe deux approches pour gérer les chèques et les virements internes :

  * Deux pièces comptables et un lettrage

  * Une pièce comptable et un rapprochement bancaire

La première pièce comptable est créée par l’enregistrement du paiement sur la
facture. La seconde est créée lors de l’enregistrement du relevé bancaire.

Compte | Débit | Crédit | Lettrage  
---|---|---|---  
Compte client |  | 100 | Facture ABC  
Valeurs à l’encaissement | 100 |  | Chèque 0123  
Compte | Débit | Crédit | Lettrage  
---|---|---|---  
Valeurs à l’encaissement |  | 100 | Chèque 0123  
Banque | 100 |  |   
  
Une pièce comptable est créée par l’enregistrement du paiement sur la facture.
Lors du rapprochement du relevé bancaire, la ligne de relevé est reliée à la
pièce comptable existante.

Compte | Débit | Crédit | Lettrage | Relevé bancaire  
---|---|---|---|---  
Compte client |  | 100 | Facture ABC |   
Banque | 100 |  |  | Relevé XYZ

