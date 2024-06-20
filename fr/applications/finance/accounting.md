# Comptabilité et Facturation

**Odoo Facturation** est une application de facturation autonome pour créer
des factures, les envoyer à vos clients et gérer les paiements.

**Odoo Comptabilité** est une application de comptabilité complète. La
productivité comptable est au cœur de son développement avec des
fonctionnalités telles que la reconnaissance des factures alimentée par l’IA,
la synchronisation avec vos comptes bancaires, les suggestions de lettrage
intelligentes, etc.

Pour plus d'infos

[Tutoriels Odoo : Comptabilité](https://www.odoo.com/slides/accounting-19)

#### [Get startedBasic concepts of accounting and initial setup of your
accounting ](accounting/get_started.html)#### [TaxesTaxes, fiscal positions,
and integrations ](accounting/taxes.html)#### [Customer invoicesCustomer
invoices, payment terms, and electronic invoicing
](accounting/customer_invoices.html)#### [Vendor billsVendor bills, assets,
and invoice digitization (OCR) ](accounting/vendor_bills.html)####
[PaymentsInvoices and bills payments (online, checks, batches) and follow-up
on invoices ](accounting/payments.html)#### [Bank and cash accountsBank
synchronization, reconciliation, and cash registers
](accounting/bank.html)#### [ReportingReporting, declarations, and analytic
accounting ](accounting/reporting.html)

## Comptabilité en partie double

Odoo crée automatiquement toutes les pièces comptables sous-jacentes pour
toutes les transactions comptables (par ex. factures clients, factures
fournisseurs, commandes de point de vente, notes de frais, valorisations des
stocks, etc.).

Odoo utilise le système de comptabilité en partie double, selon lequel chaque
écriture doit avoir une contrepartie correspondante et opposée dans un compte
différent, avec un compte débité et un compte crédité. Ce système garantit que
toutes les transactions sont enregistrées de manière précise et cohérente et
que les comptes sont toujours équilibrés.

Pour plus d'infos

[Aide-mémoire de comptabilité](accounting/get_started/cheat_sheet.html)

## Comptabilité d’engagement et de trésorerie

Odoo prend en charge à la fois la comptabilité d’engagement et la comptabilité
de trésorerie. Cela permet de déclarer les recettes et les dépenses soit
lorsque la transaction a lieu (comptabilité d’engagement), soit lorsque le
paiement est effectué ou reçu (comptabilité de trésorerie).

Pour plus d'infos

[Comptabilité de trésorerie](accounting/taxes/cash_basis.html)

## Multi-sociétés

Plusieurs sociétés peuvent être gérées au sein d’une même base de données.
Chaque société dispose son propre [plan
comptable](accounting/get_started/chart_of_accounts.html), ce qui est
également utile pour générer des rapports de consolidation. Les utilisateurs
peuvent accéder à plusieurs sociétés, mais ne peuvent travailler que sur la
comptabilité d’une seule société à la fois.

## Environnement multi-devise

Un environnement [multi-devise](accounting/get_started/multi_currency.html)
avec un taux de change automatisé pour faciliter les transactions
internationales est disponible dans Odoo. Chaque transaction est enregistrée
dans la devise par défaut de la société ; pour les transactions effectuées
dans une autre devise, Odoo enregistre à la fois la valeur dans la devise de
la société et la valeur de la devise de la transaction. Odoo génère des gains
et des pertes de change après avoir lettré les écritures comptables.

Pour plus d'infos

[Gérer une banque dans une devise
étrangère](accounting/bank/foreign_currency.html)

## Standards internationaux

Odoo Comptabilité prend en charge plus de 70 pays. L’application fournit des
normes et mécanismes centraux communs à toutes les nations, et grâce aux
modules spécifiques à chaque pays, les exigences locales sont respectées. Des
positions fiscales existent pour répondre aux spécificités régionales telles
que le plan comptable, les taxes ou toute autre exigence.

Pour plus d'infos

[Packages de localisation fiscale](fiscal_localizations.html)

## Les comptes clients et fournisseurs

Par défaut, il n’y a qu’un seul compte pour les créances et un seul compte
pour les dettes. Comme les transactions sont liées à vos **contacts** , vous
pouvez générer un rapport par client, vendeur ou fournisseur.

Le **Grand livre des partenaires** affiche le solde de vos clients et de vos
fournisseurs. Il est disponible en allant à Comptabilité ‣ Analyse ‣ Grand
livre des partenaires.

## Analyse

Les [rapports](accounting/reporting.html) financiers suivants sont disponibles
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
  
Astuce

[Créez et personnalisez des rapports](accounting/reporting/customize.html)
avec le moteur des rapports d’Odoo.

### Déclaration de TVA

Odoo calcule toutes les transactions comptables pour la période fiscale
spécifique et utilise ces totaux pour calculer l’obligation fiscale.

Important

Une fois que la déclaration de TVA a été générée pour une période, Odoo la
verrouille et empêche la création de nouvelles pièces comptables impliquant la
TVA. Toute correction aux factures clients et aux factures fournisseurs doit
être enregistrée au cours de la période suivante.

Note

En fonction de la localisation du pays, une version XML de la déclaration de
TVA peut être générée afin de pouvoir la charger sur la plateforme TVA de
l’autorité fiscale concernée.

## Synchronisation bancaire

Le système de synchronisation bancaire se connecte directement à votre
établissement bancaire pour importer automatiquement toutes les transactions
dans votre base de données. Il vous donne un aperçu de votre flux de
trésorerie sans devoir vous connecter à l’établissement bancaire en ligne ou
attendre les relevés bancaires papier.

Pour plus d'infos

[Synchronisation bancaire](accounting/bank/bank_synchronization.html)

## Valorisation des stocks

La valorisations des stocks périodique (manuelle) et la valorisation des
stocks perpétuelle (automatisée) sont prises en charge par Odoo. Les méthodes
disponibles sont prix standard, prix moyen, LIFO et FIFO (First-In, First-
Out).

Pour plus d'infos

[Configuration de la valorisation des
stocks](../inventory_and_mrp/inventory/warehouses_storage/inventory_valuation/inventory_valuation_config.html)

## Bénéfices non distribués

Les bénéfices non distribués sont la partie de la recette retenue par une
entreprise. Odoo calcule les bénéfices de l’année en cours en temps réel, de
sorte qu’aucun journal de fin d’exercice ou report n’est nécessaire. Les
pertes et profits sont automatiquement reportés dans le bilan.

Pour plus d'infos

[Aide-mémoire de comptabilité](accounting/get_started/cheat_sheet.html)

## Fiduciaires

Le mode Fiduciaires peut être activé en allant à Comptabilité ‣ Configuration
‣ Paramètres ‣ Mode Fiduciaires. Lorsqu’il est activé :

  * La séquence du document devient modifiable sur tous les documents ;

  * Le champ Total (toutes taxes comprises) apparaît pour accélérer et contrôler l’encodage en automatisant la création de lignes avec le bon compte et taxe ;

  * La Date de la facture client et la Date de la facture fournisseur sont préremplies lors de l’encodage d’une transaction.

  * Une option Encodage rapide est disponible pour les factures clients et les factures fournisseurs.

  * [Bien démarrer](accounting/get_started.html)
    * [Aide-mémoire de la comptabilité](accounting/get_started/cheat_sheet.html)
    * [Plan comptable](accounting/get_started/chart_of_accounts.html)
    * [Système multidevise](accounting/get_started/multi_currency.html)
    * [Average price on returned goods](accounting/get_started/avg_price_valuation.html)
    * [Unités TVA](accounting/get_started/vat_units.html)
  * [Taxes](accounting/taxes.html)
    * [TVA sur encaissements](accounting/taxes/cash_basis.html)
    * [Retenues à la source](accounting/taxes/retention.html)
    * [Vérification des numéros de TVA (VIES)](accounting/taxes/vat_verification.html)
    * [Positions fiscales (correspondances de taxes et de comptes)](accounting/taxes/fiscal_positions.html)
    * [AvaTax integration](accounting/taxes/avatax.html)
      * [AvaTax use](accounting/taxes/avatax/avatax_use.html)
      * [Avalara (Avatax) portal](accounting/taxes/avatax/avalara_portal.html)
    * [Intégration TaxCloud](accounting/taxes/taxcloud.html)
    * [Vente à distance intracommunautaire UE](accounting/taxes/eu_distance_selling.html)
    * [Prix B2B (hors taxes) et B2C (toutes taxes comprises)](accounting/taxes/B2B_B2C.html)
  * [Factures clients](accounting/customer_invoices.html)
    * [Processus de facturation](accounting/customer_invoices/overview.html)
    * [Adresses de livraison et de facturation](accounting/customer_invoices/customer_addresses.html)
    * [Conditions de paiement et plans de paiement échelonné](accounting/customer_invoices/payment_terms.html)
    * [Conditions générales par défaut (CG)](accounting/customer_invoices/terms_conditions.html)
    * [Escomptes et réduction d’impôt](accounting/customer_invoices/cash_discounts.html)
    * [Avoirs et remboursements](accounting/customer_invoices/credit_notes.html)
    * [Arrondi des paiements en espèces](accounting/customer_invoices/cash_rounding.html)
    * [Produits constatés d’avance](accounting/customer_invoices/deferred_revenues.html)
    * [Facturation électronique (EDI)](accounting/customer_invoices/electronic_invoicing.html)
    * [Envoi postal](accounting/customer_invoices/snailmail.html)
    * [Les codes QR de l’EPC](accounting/customer_invoices/epc_qr_code.html)
    * [Incoterms](accounting/customer_invoices/incoterms.html)
  * [Factures fournisseurs](accounting/vendor_bills.html)
    * [Numérisation de documents assistée par IA](accounting/vendor_bills/invoice_digitization.html)
    * [Actifs immobilisés et immobilisations](accounting/vendor_bills/assets.html)
    * [Charges constatées d’avance et acomptes](accounting/vendor_bills/deferred_expenses.html)
  * [Paiements](accounting/payments.html)
    * [Paiements en ligne](accounting/payments/online.html)
      * [Installer le patch pour désactiver le paiement des factures en ligne](accounting/payments/online/install_portal_patch.html)
    * [Chèques](accounting/payments/checks.html)
    * [Paiements par lot par dépôt bancaire](accounting/payments/batch.html)
    * [Paiements par lot : Prélèvement SEPA (SDD)](accounting/payments/batch_sdd.html)
    * [Suivi des factures](accounting/payments/follow_up.html)
    * [Virements internes](accounting/payments/internal_transfers.html)
    * [Payer avec SEPA](accounting/payments/pay_sepa.html)
    * [Payer par chèque](accounting/payments/pay_checks.html)
    * [Prévoir les futures factures à payer](accounting/payments/forecast.html)
  * [Comptes bancaires et d’espèces](accounting/bank.html)
    * [Synchronisation bancaire](accounting/bank/bank_synchronization.html)
      * [Salt Edge](accounting/bank/bank_synchronization/saltedge.html)
      * [Ponto](accounting/bank/bank_synchronization/ponto.html)
      * [Enable Banking](accounting/bank/bank_synchronization/enablebanking.html)
    * [Transactions](accounting/bank/transactions.html)
    * [Rapprochement bancaire](accounting/bank/reconciliation.html)
    * [Modèles de lettrage](accounting/bank/reconciliation_models.html)
    * [Gérer un compte bancaire en devise étrangère](accounting/bank/foreign_currency.html)
    * [Caisse](accounting/bank/cash_register.html)
  * [Analyse](accounting/reporting.html)
    * [Déclaration d’impôt](accounting/reporting/tax_returns.html)
    * [Report fiscal](accounting/reporting/tax_carryover.html)
    * [Comptabilité analytique](accounting/reporting/analytic_accounting.html)
    * [Budget financier](accounting/reporting/budget.html)
    * [Intrastat](accounting/reporting/intrastat.html)
    * [Rapport de vérification de l’inaltérabilité des données](accounting/reporting/data_inalterability.html)
    * [Intégration Silverfin](accounting/reporting/silverfin.html)
    * [Rapports personnalisés](accounting/reporting/customize.html)
    * [Clôture de l’exercice](accounting/reporting/year_end.html)

  *[LIFO]: Last-In, First-Out
  *[EDI]: échange de données informatisé

