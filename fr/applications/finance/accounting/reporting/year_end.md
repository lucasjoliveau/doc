# Clôture de l’exercice

La clôture de l’exercice est essentielle pour maintenir l’exactitude
financière, se conformer aux réglementations, prendre des décisions informées
et garantir la transparence des rapports.

## Exercices fiscaux

Par défaut, l’exercice fiscal est fixé à 12 mois et prend fin le 31 décembre.
Cependant, sa durée et sa date de fin peuvent varier en fonction de
considérations culturelles, administratives et économiques.

Pour modifier ces valeurs, allez à Comptabilité ‣ Configuration ‣ Paramètres.
Dans la section **Périodes fiscales** , modifiez la valeur du champ **Dernier
jour** le cas échéant.

Si la période dure _plus_ ou _moins_ de 12 mois, activez l’option **Exercices
fiscaux** et cliquez sur **Enregistrer**. Retournez à la section **Périodes
fiscales** et cliquez sur **➜ Exercices fiscaux**. Cliquez ensuite sur
**Créer** et remplissez les champs **Nom** , **Date de début** et **Date de
fin**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une fois que la période fiscale définie est terminée, Konvergo ERP revient automatiquement à la périodicité par défaut, en tenant compte de la valeur précisée dans le champ <b>Dernier jour</b>.</p>
</div>

## Check-list de fin d’exercice

### Avant la clôture

Avant de clôturer un exercice fiscal, assurez-vous que tout est exact et à
jour :

  * Assurez-vous que tous les comptes bancaires sont intégralement [rapprochés](../bank/reconciliation) jusqu’à la fin de l’exercice et confirmez que les soldes finaux correspondent aux soldes des relevés bancaires.

  * Vérifiez que toutes les [factures clients](../customer_invoices) ont été enregistrées et approuvées et qu’il n’y a pas de factures brouillon.

  * Confirmez que toutes les [factures fournisseurs](../vendor_bills) ont été enregistrées et approuvées.

  * Validez toutes les [notes de frais](../../expenses), en s’assurant de leur exactitude.

  * Vérifiez que tous les [paiements reçus](../payments) ont été encodés et enregistrés avec précision.

  * Clôturez tous les [comptes d’attente](../bank#bank-accounts-suspense).

  * Comptabilisez toutes les écritures d”[amortissement](../vendor_bills/assets) et de [produits constatés d’avance](../customer_invoices/deferred_revenues).

### Clôture d’un exercice fiscal

Ensuite, pour clôturer l’exercice fiscal :

  * Générez une [déclaration de TVA](../reporting#reporting-tax-report), et vérifiez que toutes les informations fiscales sont correctes.

  * Lettrez tous les comptes du [bilan](../reporting#reporting-balance-sheet):

    * Mettez à jour les soldes bancaires dans Konvergo ERP en fonction des soldes réels trouvés sur les relevés bancaires.

    * Rapprochez toutes les transactions des comptes d’espèces et bancaires en exécutant la [balance âgée des clients](../reporting#reporting-aged-receivable) et la [balance âgée des fournisseurs](../reporting#reporting-aged-payable).

    * Auditez tous les comptes, en s’assurant de bien comprendre toutes les transactions et leur nature et d’inclure les prêts et les immobilisations.

    * Si vous le souhaitez, effectuez un [lettrage des paiements](../payments#payments-matching) pour valider toutes les factures clients et fournisseurs avec leurs paiements. Alors que cette étape est optionnelle, elle pourrait faciliter le processus de clôture de l’exercice si tous les paiements et factures en suspens étaient lettrés, ce qui permettrait de détecter des anomalies dans le système.

Ensuite, le comptable vérifie probablement les postes du bilan et les pièces
comptables concernant :

>   * les ajustements manuels de fin d’exercice,
>
>   * les travaux en cours,
>
>   * les écritures d’amortissement,
>
>   * les prêts,
>
>   * les ajustements fiscaux,
>
>   * etc.
>
>

Si le comptable effectue l’audit de fin d’exercice, il peut vouloir avoir des
copies papier de tous les postes du bilan (tels que les prêts, les comptes
bancaires, les acomptes, les déclarations de taxe sur les ventes, etc.) afin
de les confronter à vos soldes dans Konvergo ERP.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Au cours de ce processus, il est bon de fixer une <b>Date de verrouillage des pièces comptables</b> au dernier jour (inclus) de l’exercice fiscal précédent en allant à Comptabilité ‣ Comptabilité ‣ Dates de verrouillage. Le comptable peut ainsi être sûr que personne ne modifie les transactions lors de l’audit des comptes. Les utilisateurs du groupe d’accès <em>comptable</em> peuvent toujours créer et modifier des pièces comptables.</p>
</div>

#### Bénéfices de l’exercice en cours

Konvergo ERP utilise un type de compte unique intitulé **bénéfices de l’exercice en
cours** pour afficher la différence de montant entre les comptes de
**produits** et de **charges**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le plan comptable ne peut contenir qu’un seul compte de ce type. Par défaut, il s’agit d’un compte 999999 intitulé <b>Profits/pertes non distribués</b>.</p>
</div>

Pour affecter les bénéfices de l’exercice en cours, créez une entrée diverse
pour les comptabiliser dans n’importe quel compte de capitaux propres. Une
fois cette opération terminée, confirmez si les bénéfices de l’exercice en
cours dans le **bilan** affiche correctement un solde de zéro. Si c’est le
cas, fixez une **Date de verrouillage pour tous les utilisateurs** au dernier
jour de l’exercice fiscal en allant à Comptabilité ‣ Comptabilité ‣ Dates de
verrouillage.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Install the <b>Irreversible Lock Date</b> (<code>account_lock</code>) module to make the <b>All
Users Lock Date</b> <em>irreversible</em> once set.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Une écriture spécifique de clôture de l’exercice est <b>optionnelle</b> afin de clôturer le <b>compte de résultat</b>. Les rapports sont créés en temps réel, ce qui signifie que le compte de résultat correspond directement à la date de fin d’exercice précisée dans Konvergo ERP. Par conséquent, chaque fois que le <b>compte de résultat</b> est généré, la date de début correspond au début de l”<b>exercice fiscal</b> et tous les soldes des comptes doivent être égaux à zéro.</p>
</div>

