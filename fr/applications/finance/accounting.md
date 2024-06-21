# Comptabilité et Facturation

**Konvergo ERP Facturation** est une application de facturation autonome pour créer
des factures, les envoyer à vos clients et gérer les paiements.

**Konvergo ERP Comptabilité** est une application de comptabilité complète. La
productivité comptable est au cœur de son développement avec des
fonctionnalités telles que la reconnaissance des factures alimentée par l’IA,
la synchronisation avec vos comptes bancaires, les suggestions de lettrage
intelligentes, etc.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.odoo.com/slides/accounting-19">Tutoriels Konvergo ERP : Comptabilité</a></p>
</div>

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting)

## Comptabilité en partie double

Konvergo ERP crée automatiquement toutes les pièces comptables sous-jacentes pour
toutes les transactions comptables (par ex. factures clients, factures
fournisseurs, commandes de point de vente, notes de frais, valorisations des
stocks, etc.).

Konvergo ERP utilise le système de comptabilité en partie double, selon lequel chaque
écriture doit avoir une contrepartie correspondante et opposée dans un compte
différent, avec un compte débité et un compte crédité. Ce système garantit que
toutes les transactions sont enregistrées de manière précise et cohérente et
que les comptes sont toujours équilibrés.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="accounting/get_started/cheat_sheet">Aide-mémoire de comptabilité</a></p>
</div>

## Comptabilité d’engagement et de trésorerie

Konvergo ERP prend en charge à la fois la comptabilité d’engagement et la comptabilité
de trésorerie. Cela permet de déclarer les recettes et les dépenses soit
lorsque la transaction a lieu (comptabilité d’engagement), soit lorsque le
paiement est effectué ou reçu (comptabilité de trésorerie).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="accounting/taxes/cash_basis">Comptabilité de trésorerie</a></p>
</div>

## Multi-sociétés

Plusieurs sociétés peuvent être gérées au sein d’une même base de données.
Chaque société dispose son propre [plan
comptable](accounting/get_started/chart_of_accounts), ce qui est
également utile pour générer des rapports de consolidation. Les utilisateurs
peuvent accéder à plusieurs sociétés, mais ne peuvent travailler que sur la
comptabilité d’une seule société à la fois.

## Environnement multi-devise

Un environnement [multi-devise](accounting/get_started/multi_currency)
avec un taux de change automatisé pour faciliter les transactions
internationales est disponible dans Konvergo ERP. Chaque transaction est enregistrée
dans la devise par défaut de la société ; pour les transactions effectuées
dans une autre devise, Konvergo ERP enregistre à la fois la valeur dans la devise de
la société et la valeur de la devise de la transaction. Konvergo ERP génère des gains
et des pertes de change après avoir lettré les écritures comptables.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="accounting/bank/foreign_currency">Gérer une banque dans une devise étrangère</a></p>
</div>

## Standards internationaux

Konvergo ERP Comptabilité prend en charge plus de 70 pays. L’application fournit des
normes et mécanismes centraux communs à toutes les nations, et grâce aux
modules spécifiques à chaque pays, les exigences locales sont respectées. Des
positions fiscales existent pour répondre aux spécificités régionales telles
que le plan comptable, les taxes ou toute autre exigence.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="fiscal_localizations">Packages de localisation fiscale</a></p>
</div>

## Les comptes clients et fournisseurs

Par défaut, il n’y a qu’un seul compte pour les créances et un seul compte
pour les dettes. Comme les transactions sont liées à vos **contacts** , vous
pouvez générer un rapport par client, vendeur ou fournisseur.

Le **Grand livre des partenaires** affiche le solde de vos clients et de vos
fournisseurs. Il est disponible en allant à Comptabilité ‣ Analyse ‣ Grand
livre des partenaires.

## Analyse

Les [rapports](accounting/reporting) financiers suivants sont disponibles
et mis à jour en temps réel :

Rapports financiers  
---  
Relevé | Bilan  
Compte de résultat  
Flux de trésorerie  
Déclaration de TVA  
Relevé intra-communautaire  
Audit | Grand livre  
Balance générale  
Rapport du journal  
Rapport Intrastat  
Registre des chèques  
Partenaire | Grand livre des partenaires  
Balance âgée des clients  
Balance âgée des fournisseurs  
Gestion | Analyse des factures  
Écarts latents de change  
Tableau d’amortissement  
Dépenses non admises  
Analyse des budgets  
Marges des produits  
Rapport 1099  
<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p><a href="accounting/reporting/customize">Créez et personnalisez des rapports</a> avec le moteur des rapports d’Konvergo ERP.</p>
</div>

### Déclaration de TVA

Konvergo ERP calcule toutes les transactions comptables pour la période fiscale
spécifique et utilise ces totaux pour calculer l’obligation fiscale.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Une fois que la déclaration de TVA a été générée pour une période, Konvergo ERP la verrouille et empêche la création de nouvelles pièces comptables impliquant la TVA. Toute correction aux factures clients et aux factures fournisseurs doit être enregistrée au cours de la période suivante.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>En fonction de la localisation du pays, une version XML de la déclaration de TVA peut être générée afin de pouvoir la charger sur la plateforme TVA de l’autorité fiscale concernée.</p>
</div>

## Synchronisation bancaire

Le système de synchronisation bancaire se connecte directement à votre
établissement bancaire pour importer automatiquement toutes les transactions
dans votre base de données. Il vous donne un aperçu de votre flux de
trésorerie sans devoir vous connecter à l’établissement bancaire en ligne ou
attendre les relevés bancaires papier.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="accounting/bank/bank_synchronization">Synchronisation bancaire</a></p>
</div>

## Valorisation des stocks

La valorisations des stocks périodique (manuelle) et la valorisation des
stocks perpétuelle (automatisée) sont prises en charge par Konvergo ERP. Les méthodes
disponibles sont prix standard, prix moyen, LIFO et FIFO (First-In, First-
Out).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config">Configuration de la valorisation des stocks</a></p>
</div>

## Bénéfices non distribués

Les bénéfices non distribués sont la partie de la recette retenue par une
entreprise. Konvergo ERP calcule les bénéfices de l’année en cours en temps réel, de
sorte qu’aucun journal de fin d’exercice ou report n’est nécessaire. Les
pertes et profits sont automatiquement reportés dans le bilan.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="accounting/get_started/cheat_sheet">Aide-mémoire de comptabilité</a></p>
</div>0

## Fiduciaires

Le mode **Fiduciaires** peut être activé en allant à Comptabilité ‣
Configuration ‣ Paramètres ‣ Mode Fiduciaires. Lorsqu’il est activé :

  * La séquence du document devient modifiable sur tous les documents ;

  * Le champ **Total (toutes taxes comprises)** apparaît pour accélérer et contrôler l’encodage en automatisant la création de lignes avec le bon compte et taxe ;

  * La **Date de la facture client** et la **Date de la facture fournisseur** sont préremplies lors de l’encodage d’une transaction.

  * Une option **Encodage rapide** est disponible pour les factures clients et les factures fournisseurs.

  * [Bien démarrer](accounting/get_started)
    * [Aide-mémoire de la comptabilité](accounting/get_started/cheat_sheet)
    * [Plan comptable](accounting/get_started/chart_of_accounts)
    * [Système multidevise](accounting/get_started/multi_currency)
    * [Average price on returned goods](accounting/get_started/avg_price_valuation)
    * [Unités TVA](accounting/get_started/vat_units)
  * [Taxes](accounting/taxes)
    * [TVA sur encaissements](accounting/taxes/cash_basis)
    * [Retenues à la source](accounting/taxes/retention)
    * [Vérification des numéros de TVA (VIES)](accounting/taxes/vat_verification)
    * [Positions fiscales (correspondances de taxes et de comptes)](accounting/taxes/fiscal_positions)
    * [AvaTax integration](accounting/taxes/avatax)
      * [AvaTax use](accounting/taxes/avatax/avatax_use)
      * [Avalara (Avatax) portal](accounting/taxes/avatax/avalara_portal)
    * [Intégration TaxCloud](accounting/taxes/taxcloud)
    * [Vente à distance intracommunautaire UE](accounting/taxes/eu_distance_selling)
    * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](accounting/taxes/B2B_B2C)
  * [Factures clients](accounting/customer_invoices)
    * [Processus de facturation](accounting/customer_invoices/overview)
    * [Adresses de livraison et de facturation](accounting/customer_invoices/customer_addresses)
    * [Conditions de paiement et plans de paiement échelonné](accounting/customer_invoices/payment_terms)
    * [Conditions générales par défaut (CG)](accounting/customer_invoices/terms_conditions)
    * [Escomptes et réduction d’impôt](accounting/customer_invoices/cash_discounts)
    * [Avoirs et remboursements](accounting/customer_invoices/credit_notes)
    * [Arrondi des paiements en espèces](accounting/customer_invoices/cash_rounding)
    * [Produits constatés d’avance](accounting/customer_invoices/deferred_revenues)
    * [Facturation électronique (EDI)](accounting/customer_invoices/electronic_invoicing)
    * [Envoi postal](accounting/customer_invoices/snailmail)
    * [Les codes QR de l’EPC](accounting/customer_invoices/epc_qr_code)
    * [Incoterms](accounting/customer_invoices/incoterms)
  * [Factures fournisseurs](accounting/vendor_bills)
    * [Numérisation de documents assistée par IA](accounting/vendor_bills/invoice_digitization)
    * [Actifs immobilisés et immobilisations](accounting/vendor_bills/assets)
    * [Charges constatées d’avance et acomptes](accounting/vendor_bills/deferred_expenses)
  * [Paiements](accounting/payments)
    * [Paiements en ligne](accounting/payments/online)
      * [Installer le patch pour désactiver le paiement des factures en ligne](accounting/payments/online/install_portal_patch)
    * [Chèques](accounting/payments/checks)
    * [Paiements par lot par dépôt bancaire](accounting/payments/batch)
    * [Paiements par lot : Prélèvement SEPA (SDD)](accounting/payments/batch_sdd)
    * [Suivi des factures](accounting/payments/follow_up)
    * [Virements internes](accounting/payments/internal_transfers)
    * [Payer avec SEPA](accounting/payments/pay_sepa)
    * [Payer par chèque](accounting/payments/pay_checks)
    * [Prévoir les futures factures à payer](accounting/payments/forecast)
  * [Comptes bancaires et d’espèces](accounting/bank)
    * [Synchronisation bancaire](accounting/bank/bank_synchronization)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge)
      * [Ponto](accounting/bank/bank_synchronization/ponto)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking)
    * [Transactions](accounting/bank/transactions)
    * [Rapprochement bancaire](accounting/bank/reconciliation)
    * [Modèles de lettrage](accounting/bank/reconciliation_models)
    * [Gérer un compte bancaire en devise étrangère](accounting/bank/foreign_currency)
    * [Caisse](accounting/bank/cash_register)
  * [Analyse](accounting/reporting)
    * [Déclaration d’impôt](accounting/reporting/tax_returns)
    * [Report fiscal](accounting/reporting/tax_carryover)
    * [Comptabilité analytique](accounting/reporting/analytic_accounting)
    * [Budget financier](accounting/reporting/budget)
    * [Intrastat](accounting/reporting/intrastat)
    * [Rapport de vérification de l’inaltérabilité des données](accounting/reporting/data_inalterability)
    * [Intégration Silverfin](accounting/reporting/silverfin)
    * [Rapports personnalisés](accounting/reporting/customize)
    * [Clôture de l’exercice](accounting/reporting/year_end)

  *[LIFO]: Last-In, First-Out
  *[EDI]: échange de données informatisé

