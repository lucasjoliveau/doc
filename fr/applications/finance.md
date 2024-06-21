# Finance

  * [Comptabilité et Facturation](finance/accounting)
    * [Comptabilité en partie double](finance/accounting#double-entry-bookkeeping)
    * [Comptabilité d’engagement et de trésorerie](finance/accounting#accrual-and-cash-basis)
    * [Multi-sociétés](finance/accounting#multi-company)
    * [Environnement multi-devise](finance/accounting#multi-currency-environment)
    * [Standards internationaux](finance/accounting#international-standards)
    * [Les comptes clients et fournisseurs](finance/accounting#accounts-receivable-and-payable)
    * Analyse
      * [Déclaration de TVA](finance/accounting#tax-report)
    * [Synchronisation bancaire](finance/accounting#bank-synchronization)
    * [Valorisation des stocks](finance/accounting#inventory-valuation)
    * [Bénéfices non distribués](finance/accounting#retained-earnings)
    * Fiduciaires
      * [Bien démarrer](finance/accounting/get_started)
        * Bannière d’intégration Comptabilité
          * [Données sur la société](finance/accounting/get_started#company-data)
          * [Compte bancaire](finance/accounting/get_started#bank-account)
          * [Périodes comptables](finance/accounting/get_started#accounting-periods)
          * [Plan comptable](finance/accounting/get_started#chart-of-accounts)
        * Bannière d’intégration Facturation
          * [Données sur la société](finance/accounting/get_started#invoicing-setup-company)
          * [Mise en page de la facture](finance/accounting/get_started#invoice-layout)
          * [Mode de paiement](finance/accounting/get_started#payment-method)
          * Exemple de facture
            * Aide-mémoire de la comptabilité
              * Plan comptable
                * [Exemple](finance/accounting/get_started/cheat_sheet#example)
              * [Pièces comptables](finance/accounting/get_started/cheat_sheet#journal-entries)
              * [Lettrage](finance/accounting/get_started/cheat_sheet#reconciliation)
              * [Rapprochement bancaire](finance/accounting/get_started/cheat_sheet#bank-reconciliation)
              * [Traitement des chèques](finance/accounting/get_started/cheat_sheet#checks-handling)
            * Plan comptable
              * Configuration d’un compte
                * [Code et nom](finance/accounting/get_started/chart_of_accounts#code-and-name)
                * Type
                  * [Automatisation des actifs, des charges constatées d’avance et des produits constatés d’avance](finance/accounting/get_started/chart_of_accounts#assets-deferred-expenses-and-deferred-revenues-automation)
                * [Taxes par défaut](finance/accounting/get_started/chart_of_accounts#default-taxes)
                * [Étiquettes](finance/accounting/get_started/chart_of_accounts#tags)
                * Groupes de comptes
                  * [Créer manuellement des groupes de comptes](finance/accounting/get_started/chart_of_accounts#create-account-groups-manually)
                * [Autoriser le lettrage](finance/accounting/get_started/chart_of_accounts#allow-reconciliation)
                * [Obsolète](finance/accounting/get_started/chart_of_accounts#deprecated)
            * Système multidevise
              * Configuration
                * [Devise principale](finance/accounting/get_started/multi_currency#main-currency)
                * [Activer les devises étrangères](finance/accounting/get_started/multi_currency#enable-foreign-currencies)
                * Taux de change
                  * [Mise à jour manuelle](finance/accounting/get_started/multi_currency#manual-update)
                  * [Mise à jour automatique](finance/accounting/get_started/multi_currency#automatic-update)
                * [Écritures de différence de change](finance/accounting/get_started/multi_currency#exchange-difference-entries)
                * [Plan comptable](finance/accounting/get_started/multi_currency#chart-of-accounts)
                * [Journaux](finance/accounting/get_started/multi_currency#journals)
              * Comptabilité multidevise
                * [Factures clients, factures fournisseurs et autres documents](finance/accounting/get_started/multi_currency#invoices-bills-and-other-documents)
                * [Enregistrement des paiements](finance/accounting/get_started/multi_currency#payment-registration)
                * [Transactions bancaires](finance/accounting/get_started/multi_currency#bank-transactions)
                * [Écritures de différence de change](finance/accounting/get_started/multi_currency#exchange-rate-journal-entries)
            * Average price on returned goods
              * [Configuration](finance/accounting/get_started/avg_price_valuation#configuration)
              * Using average cost valuation
                * [Formule](finance/accounting/get_started/avg_price_valuation#formula)
                * Compute average cost
                  * [Product delivery (use case)](finance/accounting/get_started/avg_price_valuation#product-delivery-use-case)
              * Return items to supplier (use case)
                * [Eliminate stock valuation errors in outgoing products](finance/accounting/get_started/avg_price_valuation#eliminate-stock-valuation-errors-in-outgoing-products)
              * Anglo-Saxon accounting
                * Product reception
                  * [Résumé](finance/accounting/get_started/avg_price_valuation#summary)
                  * Accounts balanced at received products
                    * [Dans Konvergo ERP](finance/accounting/get_started/avg_price_valuation#in-odoo)
                  * Accounts balanced at received vendor bill
                    * [Dans Konvergo ERP](finance/accounting/get_started/avg_price_valuation#id1)
                * [On product delivery](finance/accounting/get_started/avg_price_valuation#on-product-delivery)
                * [On product return](finance/accounting/get_started/avg_price_valuation#on-product-return)
            * Unités TVA
              * Configuration
                * [Position fiscale](finance/accounting/get_started/vat_units#fiscal-position)
              * [Déclaration de TVA](finance/accounting/get_started/vat_units#tax-report)
      * [Taxes](finance/accounting/taxes)
        * [Taxes par défaut](finance/accounting/taxes#default-taxes)
        * [Activer les Taxes de vente à partir de la vue Liste](finance/accounting/taxes#activate-sales-taxes-from-the-list-view)
        * Configuration
          * Options de base
            * [Nom de la taxe](finance/accounting/taxes#tax-name)
            * [Calcul de la taxe](finance/accounting/taxes#tax-computation)
            * [Actif](finance/accounting/taxes#active)
            * [Portée de la taxe](finance/accounting/taxes#tax-scope)
          * [Onglet Définition](finance/accounting/taxes#definition-tab)
          * Onglet Options avancées
            * [Étiquettes sur les factures](finance/accounting/taxes#label-on-invoices)
            * [Groupe de taxes](finance/accounting/taxes#tax-group)
            * [Inclure dans le coût analytique](finance/accounting/taxes#include-in-analytic-cost)
            * [Inclus dans le prix](finance/accounting/taxes#included-in-price)
            * Impacter la base des taxes ultérieures
              * TVA sur encaissements
                * [Configuration](finance/accounting/taxes/cash_basis#configuration)
                * [Impact de la TVA sur encaissements sur la comptabilité](finance/accounting/taxes/cash_basis#impact-of-cash-basis-taxes-on-accounting)
              * Retenues à la source
                * [Configuration](finance/accounting/taxes/retention#configuration)
                * [Application des retenues à la source aux factures](finance/accounting/taxes/retention#applying-retention-taxes-on-invoices)
              * Vérification des numéros de TVA (VIES)
                * [Configuration](finance/accounting/taxes/vat_verification#configuration)
                * [Validation du numéro de TVA](finance/accounting/taxes/vat_verification#vat-number-validation)
              * Positions fiscales (correspondances de taxes et de comptes)
                * Configuration
                  * [Correspondances de taxes et de comptes](finance/accounting/taxes/fiscal_positions#tax-and-account-mapping)
                * Application
                  * [Application automatique](finance/accounting/taxes/fiscal_positions#automatic-application)
                  * [Application manuelle](finance/accounting/taxes/fiscal_positions#manual-application)
                  * [Assigner à un partenaire](finance/accounting/taxes/fiscal_positions#assign-to-a-partner)
              * [AvaTax integration](finance/accounting/taxes/avatax)
                * Set up on AvaTax
                  * [Create basic company profile](finance/accounting/taxes/avatax#create-basic-company-profile)
                  * [Connect to AvaTax](finance/accounting/taxes/avatax#connect-to-avatax)
                * Konvergo ERP configuration
                  * [Fiscal country](finance/accounting/taxes/avatax#fiscal-country)
                  * [Company settings](finance/accounting/taxes/avatax#company-settings)
                  * [Module installation](finance/accounting/taxes/avatax#module-installation)
                  * Konvergo ERP AvaTax settings
                    * [Conditions préalables](finance/accounting/taxes/avatax#prerequisites)
                    * [Identifiants](finance/accounting/taxes/avatax#credentials)
                    * [Transaction options](finance/accounting/taxes/avatax#transaction-options)
                    * [Validation de l’adresse](finance/accounting/taxes/avatax#address-validation)
                    * [Test connection](finance/accounting/taxes/avatax#test-connection)
                    * [Sync parameters](finance/accounting/taxes/avatax#sync-parameters)
                  * Position fiscale
                    * [AvaTax accounts](finance/accounting/taxes/avatax#avatax-accounts)
                  * Correspondance de taxes
                    * [Product category mapping](finance/accounting/taxes/avatax#product-category-mapping)
                    * Product mapping
                      * AvaTax use
                        * Calcul des taxes
                          * [Automatic triggers](finance/accounting/taxes/avatax/avatax_use#automatic-triggers)
                          * [Manual triggers](finance/accounting/taxes/avatax/avatax_use#manual-triggers)
                        * [AvaTax synchronization](finance/accounting/taxes/avatax/avatax_use#avatax-synchronization)
                        * [Fixed price discounts](finance/accounting/taxes/avatax/avatax_use#fixed-price-discounts)
                        * [Journalisation](finance/accounting/taxes/avatax/avatax_use#logging)
                      * Avalara (Avatax) portal
                        * Transactions
                          * [Edit transaction](finance/accounting/taxes/avatax/avalara_portal#edit-transaction)
                          * [Filtrer](finance/accounting/taxes/avatax/avalara_portal#filter)
                          * Trier par
                            * [Customize columns](finance/accounting/taxes/avatax/avalara_portal#customize-columns)
                          * [Import-export](finance/accounting/taxes/avatax/avalara_portal#import-export)
                          * [Rapports](finance/accounting/taxes/avatax/avalara_portal#reports)
                        * [Add more jurisdictions](finance/accounting/taxes/avatax/avalara_portal#add-more-jurisdictions)
                        * [Tax exemption certificate](finance/accounting/taxes/avatax/avalara_portal#tax-exemption-certificate)
                        * [End-of-year operations](finance/accounting/taxes/avatax/avalara_portal#end-of-year-operations)
              * Intégration TaxCloud
                * [Inscription à TaxCloud](finance/accounting/taxes/taxcloud#taxcloud-registration)
                * [Activer TaxCloud](finance/accounting/taxes/taxcloud#enable-taxcloud)
                * [Définir des catégories TaxCloud sur des produits](finance/accounting/taxes/taxcloud#set-taxcloud-categories-on-products)
                * [Comptabiliser automatiquement les taxes dans le bon compte de taxes à payer](finance/accounting/taxes/taxcloud#automatically-post-taxes-in-the-correct-tax-payable-account)
                * [Détecter automatiquement la position fiscale](finance/accounting/taxes/taxcloud#automatically-detect-the-fiscal-position)
                * [Interaction avec des coupons et des promotions](finance/accounting/taxes/taxcloud#interaction-with-coupons-and-promotions)
              * Vente à distance intracommunautaire UE
                * [Configuration](finance/accounting/taxes/eu_distance_selling#configuration)
                * Guichet unique (OSS)
                  * [Rapports](finance/accounting/taxes/eu_distance_selling#reports)
              * Prix B2B (hors taxes) et B2C (toutes taxes comprises)
                * Configuration
                  * [Introduction](finance/accounting/taxes/B2B_B2C#introduction)
                  * [eCommerce](finance/accounting/taxes/B2B_B2C#ecommerce)
                  * [Configurer vos produits](finance/accounting/taxes/B2B_B2C#setting-your-products)
                  * [Configuration de la position fiscale B2C](finance/accounting/taxes/B2B_B2C#setting-the-b2c-fiscal-position)
                * [Tester en créant un devis](finance/accounting/taxes/B2B_B2C#test-by-creating-a-quotation)
                * [Éviter de changer chaque commande client](finance/accounting/taxes/B2B_B2C#avoid-changing-every-sale-order)
      * [Factures clients](finance/accounting/customer_invoices)
        * De la facture client à l’encaissement des paiements
          * [De la facture brouillon au compte de résultat](finance/accounting/customer_invoices#from-draft-invoice-to-profit-and-loss)
          * [Création d’une facture](finance/accounting/customer_invoices#invoice-creation)
          * [Factures brouillon](finance/accounting/customer_invoices#draft-invoices)
          * [Factures ouvertes ou pro forma](finance/accounting/customer_invoices#open-or-pro-forma-invoices)
          * [Envoyer la facture au client](finance/accounting/customer_invoices#send-the-invoice-to-customer)
          * [Paiement](finance/accounting/customer_invoices#payment)
          * [Recevoir un paiement partiel par le relevé bancaire](finance/accounting/customer_invoices#receive-a-partial-payment-through-the-bank-statement)
          * [Rapprocher](finance/accounting/customer_invoices#reconcile)
          * Suivi du paiement
            * [Balance âgée des clients :](finance/accounting/customer_invoices#customer-aging-report)
          * [Compte de résultat](finance/accounting/customer_invoices#profit-and-loss)
          * Bilan
            * Processus de facturation
              * Ventes
                * [Commande client ‣ Facture](finance/accounting/customer_invoices/overview#sales-order-invoice)
                * [Commande client ‣ Bon de livraison ‣ Facture](finance/accounting/customer_invoices/overview#sales-order-delivery-order-invoice)
                * [Commande eCommerce ‣ Facture](finance/accounting/customer_invoices/overview#ecommerce-order-invoice)
              * Contrats
                * [Contrats réguliers ‣ Factures](finance/accounting/customer_invoices/overview#regular-contracts-invoices)
                * [Contrats récurrents ‣ Factures](finance/accounting/customer_invoices/overview#recurring-contracts-invoices)
              * Autres
                * [Créer une facture manuellement](finance/accounting/customer_invoices/overview#creating-an-invoice-manually)
                * [Modules spécifiques](finance/accounting/customer_invoices/overview#specific-modules)
                * [Réordonnancement des factures](finance/accounting/customer_invoices/overview#resequencing-of-the-invoices)
                * [Numérisation des factures grâce à la reconnaissance optique de caractères (OCR)](finance/accounting/customer_invoices/overview#invoice-digitization-with-optical-character-recognition-ocr)
            * Adresses de livraison et de facturation
              * [Configuration](finance/accounting/customer_invoices/customer_addresses#configuration)
              * [Facturer et livrer à des adresses différentes](finance/accounting/customer_invoices/customer_addresses#invoice-and-deliver-to-different-addresses)
            * Conditions de paiement et plans de paiement échelonné
              * [Configuration](finance/accounting/customer_invoices/payment_terms#configuration)
              * [Utiliser des conditions de paiement](finance/accounting/customer_invoices/payment_terms#using-payment-terms)
              * [Pièces comptables](finance/accounting/customer_invoices/payment_terms#journal-entries)
            * Conditions générales par défaut (CG)
              * [Configuration](finance/accounting/customer_invoices/terms_conditions#configuration)
            * Escomptes et réduction d’impôt
              * Configuration
                * [Réductions d’impôt](finance/accounting/customer_invoices/cash_discounts#tax-reductions)
                * [Comptes des pertes/gains d’escompte](finance/accounting/customer_invoices/cash_discounts#cash-discount-gain-loss-accounts)
                * [Délais de paiement](finance/accounting/customer_invoices/cash_discounts#payment-terms)
              * Appliquer un escompte à une facture client
                * [Rapprochement des paiements](finance/accounting/customer_invoices/cash_discounts#payment-reconciliation)
            * Avoirs et remboursements
              * Émettre un avoir
                * [Remboursement partiel](finance/accounting/customer_invoices/credit_notes#partial-refund)
                * [Remboursement intégral](finance/accounting/customer_invoices/credit_notes#full-refund)
                * [Remboursement intégral et nouvelle facture brouillon](finance/accounting/customer_invoices/credit_notes#full-refund-and-new-draft-invoice)
              * [Émettre une note de débit](finance/accounting/customer_invoices/credit_notes#issue-a-debit-note)
              * [Enregistrer un remboursement fournisseur](finance/accounting/customer_invoices/credit_notes#record-a-vendor-refund)
              * [Enregistrer une note de débit](finance/accounting/customer_invoices/credit_notes#record-a-debit-note)
              * [Pièces comptables](finance/accounting/customer_invoices/credit_notes#journal-entries)
            * Arrondi des paiements en espèces
              * [Configuration](finance/accounting/customer_invoices/cash_rounding#configuration)
              * [Appliquer les arrondis](finance/accounting/customer_invoices/cash_rounding#apply-roundings)
            * Produits constatés d’avance
              * Conditions préalables
                * [Configurer un compte de produits constatés d’avance](finance/accounting/customer_invoices/deferred_revenues#configure-a-deferred-revenue-account)
                * Enregistrer un revenu sur le bon compte
                  * [Sélectionner le compte sur une facture brouillon](finance/accounting/customer_invoices/deferred_revenues#select-the-account-on-a-draft-invoice)
                  * [Choisir un compte des revenus différent pour des produits spécifiques](finance/accounting/customer_invoices/deferred_revenues#choose-a-different-income-account-for-specific-products)
                  * [Modifier le compte d’une écriture comptable comptabilisée](finance/accounting/customer_invoices/deferred_revenues#change-the-account-of-a-posted-journal-item)
              * Écritures de produits constatés d’avance
                * Créer une nouvelle écriture
                  * [Que signifie « Prorata Temporis » ?](finance/accounting/customer_invoices/deferred_revenues#what-does-prorata-temporis-mean)
                * [Écriture à reporter à partir du Journal des ventes](finance/accounting/customer_invoices/deferred_revenues#deferred-entry-from-the-sales-journal)
              * Modèles de produits constatés d’avance
                * [Appliquer un modèle de produits constatés d’avance à une nouvelle écriture](finance/accounting/customer_invoices/deferred_revenues#apply-a-deferred-revenue-model-to-a-new-entry)
              * [Automatiser les produits constatés d’avance](finance/accounting/customer_invoices/deferred_revenues#automate-the-deferred-revenues)
            * Facturation électronique (EDI)
              * [Configuration](finance/accounting/customer_invoices/electronic_invoicing#configuration)
            * Envoi postal
              * [Configuration](finance/accounting/customer_invoices/snailmail#configuration)
              * [Envoyer des factures par la poste](finance/accounting/customer_invoices/snailmail#send-invoices-by-post)
              * [Tarification](finance/accounting/customer_invoices/snailmail#pricing)
            * Les codes QR de l’EPC
              * Configuration
                * [Configurer le journal de votre compte bancaire](finance/accounting/customer_invoices/epc_qr_code#configure-your-bank-account-s-journal)
              * [Émettre des factures avec des codes QR de l’EPC](finance/accounting/customer_invoices/epc_qr_code#issue-invoices-with-epc-qr-codes)
            * Incoterms
              * [Définir un Incoterm](finance/accounting/customer_invoices/incoterms#define-an-incoterm)
              * [Configuration par défaut de l’Incoterm](finance/accounting/customer_invoices/incoterms#default-incoterm-configuration)
      * [Factures fournisseurs](finance/accounting/vendor_bills)
        * Création d’une facture fournisseur
          * [Manuellement](finance/accounting/vendor_bills#manually)
          * [Automatiquement](finance/accounting/vendor_bills#automatically)
        * [Remplissage de la facture](finance/accounting/vendor_bills#bill-completion)
        * [Confirmation de la facture](finance/accounting/vendor_bills#bill-confirmation)
        * [Paiement de la facture](finance/accounting/vendor_bills#bill-payment)
        * Balance âgée des fournisseurs
          * Numérisation de documents assistée par IA
            * [Configuration](finance/accounting/vendor_bills/invoice_digitization#configuration)
            * Chargement des factures
              * [Charger les factures manuellement](finance/accounting/vendor_bills/invoice_digitization#upload-invoices-manually)
              * [Charger des factures à l’aide d’un alias d’email](finance/accounting/vendor_bills/invoice_digitization#upload-invoices-using-an-email-alias)
            * [Numérisation des factures](finance/accounting/vendor_bills/invoice_digitization#invoice-digitization)
            * [Reconnaissance des données avec l’IA](finance/accounting/vendor_bills/invoice_digitization#data-recognition-with-ai)
            * [Tarification](finance/accounting/vendor_bills/invoice_digitization#pricing)
          * Actifs immobilisés et immobilisations
            * Conditions préalables
              * [Configurer un compte d’actifs](finance/accounting/vendor_bills/assets#configure-an-assets-account)
              * Comptabiliser une charge sur le bon compte
                * [Sélectionner le compte sur une facture fournisseur brouillon](finance/accounting/vendor_bills/assets#select-the-account-on-a-draft-bill)
                * [Choisir un compte de charges différent pour des produits spécifiques](finance/accounting/vendor_bills/assets#choose-a-different-expense-account-for-specific-products)
                * [Modifier le compte d’une écriture comptable comptabilisée](finance/accounting/vendor_bills/assets#change-the-account-of-a-posted-journal-item)
            * Écritures d’actifs
              * Créer une nouvelle écriture
                * [Que signifie « Prorata Temporis » ?](finance/accounting/vendor_bills/assets#what-does-prorata-temporis-mean)
                * [Quelles sont les différentes méthodes d’amortissement](finance/accounting/vendor_bills/assets#what-are-the-different-depreciation-methods)
              * [Actifs à partir du Journal des ventes](finance/accounting/vendor_bills/assets#assets-from-the-purchases-journal)
            * [Modification d’un actif](finance/accounting/vendor_bills/assets#modification-of-an-asset)
            * [Cession d’immobilisations](finance/accounting/vendor_bills/assets#disposal-of-fixed-assets)
            * Modèles d’actifs
              * [Appliquer un modèle d’actif à une nouvelle écriture](finance/accounting/vendor_bills/assets#apply-an-asset-model-to-a-new-entry)
            * [Automatiser les actifs](finance/accounting/vendor_bills/assets#automate-the-assets)
          * Charges constatées d’avance et acomptes
            * Conditions préalables
              * [Configurer un compte de charges constatées d’avance](finance/accounting/vendor_bills/deferred_expenses#configure-a-deferred-expense-account)
              * Comptabiliser une charge sur le bon compte
                * [Sélectionner le compte sur une facture fournisseur brouillon](finance/accounting/vendor_bills/deferred_expenses#select-the-account-on-a-draft-bill)
                * [Choisir un compte de charges différent pour des produits spécifiques](finance/accounting/vendor_bills/deferred_expenses#choose-a-different-expense-account-for-specific-products)
                * [Modifier le compte d’une écriture comptable comptabilisée](finance/accounting/vendor_bills/deferred_expenses#change-the-account-of-a-posted-journal-item)
            * Écritures de charges constatées d’avance
              * Créer une nouvelle écriture
                * [Que signifie « Prorata Temporis » ?](finance/accounting/vendor_bills/deferred_expenses#what-does-prorata-temporis-mean)
              * [Écriture à reporter à partir du Journal des achats](finance/accounting/vendor_bills/deferred_expenses#deferred-entry-from-the-purchases-journal)
            * Modèles de charges constatées d’avance
              * [Appliquer un modèle de charges constatées d’avance à une nouvelle écriture](finance/accounting/vendor_bills/deferred_expenses#apply-a-deferred-expense-model-to-a-new-entry)
            * [Automatiser les charges constatées d’avance](finance/accounting/vendor_bills/deferred_expenses#automate-the-deferred-expenses)
      * [Paiements](finance/accounting/payments)
        * [Enregistrer un paiement à partir d’une facture client ou d’une facture fournisseur](finance/accounting/payments#registering-payment-from-an-invoice-or-bill)
        * Enregistrer des paiements non associés à une facture client ou fournisseur
          * [Lettrer les factures clients et fournisseurs aux paiements](finance/accounting/payments#matching-invoices-and-bills-with-payments)
          * [Paiements par lot](finance/accounting/payments#batch-payment)
          * [Lettrage des paiements](finance/accounting/payments#payments-matching)
          * [Lettrage des paiements par lot](finance/accounting/payments#batch-payments-matching)
        * [Registering a partial payment](finance/accounting/payments#registering-a-partial-payment)
        * Rapprocher des paiements avec les relevés bancaires
          * [Paiements en ligne](finance/accounting/payments/online)
            * Installer le patch pour désactiver le paiement des factures en ligne
              * [Mettre à jour Konvergo ERP à la dernière version](finance/accounting/payments/online/install_portal_patch#update-odoo-to-the-latest-release)
              * [Mettre à jour la liste des modules disponibles](finance/accounting/payments/online/install_portal_patch#update-the-list-of-available-modules)
              * [Installez le module Patch de paiement des factures en ligne.](finance/accounting/payments/online/install_portal_patch#install-the-module-invoice-online-payment-patch)
            * [Configuration](finance/accounting/payments/online#configuration)
            * [Portail client](finance/accounting/payments/online#customer-portal)
          * Chèques
            * [Méthode 1 : Compte en suspens](finance/accounting/payments/checks#method-1-outstanding-account)
            * [Méthode 2 : Contournement du rapprochement](finance/accounting/payments/checks#method-2-reconciliation-bypass)
            * [Enregistrement des paiements](finance/accounting/payments/checks#payment-registration)
            * Pièces comptables
              * [Compte en suspens](finance/accounting/payments/checks#outstanding-account)
              * [Contournement du rapprochement](finance/accounting/payments/checks#reconciliation-bypass)
          * Paiements par lot par dépôt bancaire
            * [Configuration](finance/accounting/payments/batch#configuration)
            * Déposer plusieurs paiements dans un lot
              * [Enregistrer les paiements](finance/accounting/payments/batch#register-payments)
              * [Ajouter des paiements à un dépôt par lot](finance/accounting/payments/batch#add-payments-to-a-batch-deposit)
              * [Rapprochement bancaire](finance/accounting/payments/batch#bank-reconciliation)
          * Paiements par lot : Prélèvement SEPA (SDD)
            * [Configuration](finance/accounting/payments/batch_sdd#configuration)
            * Mandats de prélèvement SEPA
              * [Créer un mandat](finance/accounting/payments/batch_sdd#create-a-mandate)
              * [Le prélèvement SEPA comme mode de paiement](finance/accounting/payments/batch_sdd#sepa-direct-debit-as-a-payment-method)
              * [Résilier ou révoquer un mandat](finance/accounting/payments/batch_sdd#close-or-revoke-a-mandate)
            * Être payé avec les paiements par lot du prélèvement SEPA
              * [Factures clients](finance/accounting/payments/batch_sdd#customer-invoices)
              * [Générer des fichiers de prélèvement SEPA `.XML` pour soumettre des paiements](finance/accounting/payments/batch_sdd#generate-sepa-direct-debit-xml-files-to-submit-payments)
          * Suivi des factures
            * [Configuration](finance/accounting/payments/follow_up#configuration)
            * Rapports de relance
              * [Niveau de confiance du débiteur](finance/accounting/payments/follow_up#debtor-s-trust-level)
              * [Envoyer des rappels groupés](finance/accounting/payments/follow_up#send-reminders-in-batches)
          * Virements internes
            * [Configuration](finance/accounting/payments/internal_transfers#configuration)
            * Enregistrer un virement interne d’une banque à une autre
              * Enregistrer un virement interne
                * [Journal de banque (Banque A)](finance/accounting/payments/internal_transfers#bank-journal-bank-a)
                * [Comptabilisation automatisée - Journal de banque (BANQUE B)](finance/accounting/payments/internal_transfers#automated-booking-bank-journal-bank-b)
              * Gérer et rapprocher les relevés bancaires
                * [Écriture comptable](finance/accounting/payments/internal_transfers#bank-journal-entry)
                * [Écriture comptable](finance/accounting/payments/internal_transfers#id1)
          * Payer avec SEPA
            * Configuration
              * [Activer les virements SEPA (SEPA Credit Transfer - SCT)](finance/accounting/payments/pay_sepa#activate-sepa-credit-transfer-sct)
              * [Activer les modes de paiement SEPA sur les banques](finance/accounting/payments/pay_sepa#activate-sepa-payment-methods-on-banks)
              * [Enregistrer des paiements](finance/accounting/payments/pay_sepa#registering-payments)
          * Payer par chèque
            * Configuration
              * [Activer le mode de paiement par chèque](finance/accounting/payments/pay_checks#activate-checks-payment-methods)
            * Papier à chèque compatible pour l’impression de chèques
              * [États-Unis](finance/accounting/payments/pay_checks#united-states)
            * Payer une facture fournisseur par chèque
              * [Enregistrer un paiement par chèque](finance/accounting/payments/pay_checks#register-a-payment-by-check)
              * [Imprimer des chèques](finance/accounting/payments/pay_checks#print-checks)
          * Prévoir les futures factures à payer
            * [Configuration : conditions de paiement](finance/accounting/payments/forecast#configuration-payment-terms)
            * [Prévoir les factures à payer avec la balance âgée des fournisseurs](finance/accounting/payments/forecast#forecast-bills-to-pay-with-the-aged-payable-report)
            * [Sélectionner les factures à payer](finance/accounting/payments/forecast#select-bills-to-pay)
      * [Comptes bancaires et d’espèces](finance/accounting/bank)
        * Gérer vos comptes bancaires et d’espèces
          * [Connecter votre banque pour la synchronisation automatique](finance/accounting/bank#connect-your-bank-for-automatic-synchronization)
          * [Créer un compte bancaire](finance/accounting/bank#create-a-bank-account)
          * [Créer un journal d’espèces](finance/accounting/bank#create-a-cash-journal)
          * [Modifier un journal de banque ou d’espèces existant](finance/accounting/bank#edit-an-existing-bank-or-cash-journal)
        * Configuration
          * [Compte d’attente](finance/accounting/bank#suspense-account)
          * [Comptes de perte et de profit](finance/accounting/bank#profit-and-loss-accounts)
          * [Devise](finance/accounting/bank#currency)
          * [Numéro de compte](finance/accounting/bank#account-number)
          * [Flux de données bancaires](finance/accounting/bank#bank-feeds)
        * Comptes en suspens
          * [Configuration des comptes par défaut](finance/accounting/bank#default-accounts-configuration)
          * Configuration des journaux de banque et d’espèces
            * [Synchronisation bancaire](finance/accounting/bank/bank_synchronization)
              * Configuration
                * [Utilisateurs On-premise](finance/accounting/bank/bank_synchronization#on-premise-users)
                * [Première synchronisation](finance/accounting/bank/bank_synchronization#first-synchronization)
                * [Synchroniser manuellement](finance/accounting/bank/bank_synchronization#synchronize-manually)
              * Problèmes
                * [Erreur de synchronisation](finance/accounting/bank/bank_synchronization#synchronization-in-error)
                * [Synchronisation déconnectée](finance/accounting/bank/bank_synchronization#synchronization-disconnected)
              * [Processus de migration pour les utilisateurs ayant installé Konvergo ERP avant décembre 2020](finance/accounting/bank/bank_synchronization#migration-process-for-users-having-installed-odoo-before-december-2020)
              * FAQ
                * [La synchronisation ne fonctionne pas en temps réel. Est-ce normal ?](finance/accounting/bank/bank_synchronization#the-synchronization-is-not-working-in-real-time-is-that-normal)
                * [La fonctionnalité de synchronisation bancaire en ligne est-elle incluse dans mon contrat ?](finance/accounting/bank/bank_synchronization#is-the-online-bank-synchronization-feature-included-in-my-contract)
                * [Certaines banques ont un statut « Bêta ». Qu’est-ce que cela signifie ?](finance/accounting/bank/bank_synchronization#some-banks-have-a-status-beta-what-does-this-mean)
                * [Pourquoi mes transactions ne se synchronisent-elles que lorsque j’actualise manuellement ?](finance/accounting/bank/bank_synchronization#why-do-my-transactions-only-synchronize-when-i-refresh-manually)
                * [Toutes mes transactions passées ne sont pas dans Konvergo ERP, pourquoi ?](finance/accounting/bank/bank_synchronization#not-all-of-my-past-transactions-are-in-odoo-why)
                * [Pourquoi ne vois-je aucune transaction ?](finance/accounting/bank/bank_synchronization#why-don-t-i-see-any-transactions)
                * Comment mettre à jour mes identifiants bancaires ?
                  * Salt Edge
                    * Configuration
                      * [Lier ses comptes bancaires avec Konvergo ERP](finance/accounting/bank/bank_synchronization/saltedge#link-your-bank-accounts-with-odoo)
                      * [Mettre à jour ses identifiants](finance/accounting/bank/bank_synchronization/saltedge#update-your-credentials)
                      * [Récupérer de nouveaux comptes](finance/accounting/bank/bank_synchronization/saltedge#fetch-new-accounts)
                    * FAQ
                      * [Une erreur survient lorsque j’essaye de supprimer ma synchronisation dans Konvergo ERP](finance/accounting/bank/bank_synchronization/saltedge#i-have-an-error-when-i-try-to-delete-my-synchronization-within-odoo)
                      * [Une erreur me dit que j’ai déjà synchronisé ce compte](finance/accounting/bank/bank_synchronization/saltedge#i-have-an-error-saying-that-i-have-already-synchronized-this-account)
                  * Ponto
                    * Configuration
                      * [Lier ses comptes bancaires avec Ponto](finance/accounting/bank/bank_synchronization/ponto#link-your-bank-accounts-with-ponto)
                      * [Lier son compte Ponto à sa base de données Konvergo ERP](finance/accounting/bank/bank_synchronization/ponto#link-your-ponto-account-with-your-odoo-database)
                      * [Mettre à jour ses identifiants de synchronisation](finance/accounting/bank/bank_synchronization/ponto#update-your-synchronization-credentials)
                      * [Récupérer de nouveaux comptes](finance/accounting/bank/bank_synchronization/ponto#fetch-new-accounts)
                    * FAQ
                      * [Après ma synchronisation, aucun compte n’apparaît](finance/accounting/bank/bank_synchronization/ponto#after-my-synchronization-no-account-appears)
                      * [Une erreur survient indiquant que mon autorisation a expiré](finance/accounting/bank/bank_synchronization/ponto#i-have-an-error-about-that-my-authorization-has-expired)
                      * [J’ai des erreurs avec mon établissement bêta](finance/accounting/bank/bank_synchronization/ponto#i-have-some-errors-with-my-beta-institution)
                  * Enable Banking
                    * Configuration
                      * [Lier des comptes bancaires avec Konvergo ERP](finance/accounting/bank/bank_synchronization/enablebanking#link-bank-accounts-with-odoo)
            * Transactions
              * [Importer les transactions](finance/accounting/bank/transactions#import-transactions)
              * [Enregistrer les transactions bancaires manuellement](finance/accounting/bank/transactions#register-bank-transactions-manually)
              * Relevés bancaires
                * [Créer des relevés depuis la vue kanban](finance/accounting/bank/transactions#statement-creation-from-the-kanban-view)
                * [Créer des relevés depuis la vue liste](finance/accounting/bank/transactions#statement-creation-from-the-list-view)
            * Rapprochement bancaire
              * [Vue du rapprochement bancaire](finance/accounting/bank/reconciliation#bank-reconciliation-view)
              * Rapprocher des transactions
                * [Rapprocher des écritures existantes](finance/accounting/bank/reconciliation#match-existing-entries)
                * [Paiements par lot](finance/accounting/bank/reconciliation#batch-payments)
                * [Opérations manuelles](finance/accounting/bank/reconciliation#manual-operations)
                * [Boutons des modèles de rapprochement](finance/accounting/bank/reconciliation#reconciliation-model-buttons)
            * Modèles de lettrage
              * [Reconciliation model types](finance/accounting/bank/reconciliation_models#reconciliation-model-types)
              * Default reconciliation models
                * [Invoices/Bills perfect match](finance/accounting/bank/reconciliation_models#invoices-bills-perfect-match)
                * [Invoices/Bills partial match if underpaid](finance/accounting/bank/reconciliation_models#invoices-bills-partial-match-if-underpaid)
                * [Line with bank fees](finance/accounting/bank/reconciliation_models#line-with-bank-fees)
              * [Partner mapping](finance/accounting/bank/reconciliation_models#partner-mapping)
            * Gérer un compte bancaire en devise étrangère
              * Configuration
                * [Activer l’option multi-devises](finance/accounting/bank/foreign_currency#activate-multi-currencies)
                * [Configurer des devises](finance/accounting/bank/foreign_currency#configure-currencies)
                * [Créer un nouveau compte bancaire](finance/accounting/bank/foreign_currency#create-a-new-bank-account)
              * [Facture fournisseur en devise étrangère](finance/accounting/bank/foreign_currency#vendor-bill-in-a-foreign-currency)
              * [Rapport d’écarts de conversion](finance/accounting/bank/foreign_currency#unrealized-currency-gains-losses-report)
            * Caisse
              * [Configuration](finance/accounting/bank/cash_register#configuration)
              * Utilisation
                * [Comment enregistrer des paiements en espèces ?](finance/accounting/bank/cash_register#how-to-register-cash-payments)
                * [Déposer de l’argent](finance/accounting/bank/cash_register#put-money-in)
                * [Sortir de l’argent](finance/accounting/bank/cash_register#take-money-out)
      * [Analyse](finance/accounting/reporting)
        * Principaux rapports disponibles
          * [Bilan](finance/accounting/reporting#balance-sheet)
          * [Compte de résultat](finance/accounting/reporting#profit-and-loss)
          * [Résumé général](finance/accounting/reporting#executive-summary)
          * [Grand livre](finance/accounting/reporting#general-ledger)
          * [Balance âgée des fournisseurs](finance/accounting/reporting#aged-payable)
          * [Balance âgée des clients](finance/accounting/reporting#aged-receivable)
          * [Flux de trésorerie](finance/accounting/reporting#cash-flow-statement)
          * Déclaration de TVA
            * Déclaration d’impôt
              * Conditions préalables
                * [Périodicité de la déclaration d’impôt](finance/accounting/reporting/tax_returns#tax-return-periodicity)
                * [Grilles de taxes](finance/accounting/reporting/tax_returns#tax-grids)
              * Clôturer une période fiscale
                * [Date de verrouillage de la taxe](finance/accounting/reporting/tax_returns#tax-lock-date)
                * [Déclaration de TVA](finance/accounting/reporting/tax_returns#tax-report)
            * [Report fiscal](finance/accounting/reporting/tax_carryover)
            * Comptabilité analytique
              * [Configuration](finance/accounting/reporting/analytic_accounting#configuration)
              * [Comptes analytiques](finance/accounting/reporting/analytic_accounting#analytic-accounts)
              * [Plans analytiques](finance/accounting/reporting/analytic_accounting#analytic-plans)
              * Distribution analytique
                * [Modèles de distribution analytique](finance/accounting/reporting/analytic_accounting#analytic-distribution-models)
            * Budget financier
              * Configuration
                * [Postes budgétaires](finance/accounting/reporting/budget#budgetary-positions)
              * Cas d’utilisation
                * [Comptes analytiques](finance/accounting/reporting/budget#analytical-accounts)
                * [Définir le budget](finance/accounting/reporting/budget#define-the-budget)
                * [Vérifier votre budget](finance/accounting/reporting/budget#check-your-budget)
            * Intrastat
              * Configuration générale
                * [Codes de transaction par défaut : facture et remboursement](finance/accounting/reporting/intrastat#default-transaction-codes-invoice-and-refund)
                * [Code de région](finance/accounting/reporting/intrastat#region-code)
              * Configuration du produit
                * [Code marchandises](finance/accounting/reporting/intrastat#commodity-code)
                * [Quantité : poids et unités supplémentaires](finance/accounting/reporting/intrastat#quantity-weight-and-supplementary-unit)
                * [Pays d’origine](finance/accounting/reporting/intrastat#country-of-origin)
              * Configuration des factures clients et fournisseurs
                * [Code de transaction](finance/accounting/reporting/intrastat#transaction-code)
                * [Pays partenaire](finance/accounting/reporting/intrastat#partner-country)
                * [Code de transport](finance/accounting/reporting/intrastat#transport-code)
                * [Valeur des marchandises](finance/accounting/reporting/intrastat#value-of-the-goods)
              * [Configuration du partenaire](finance/accounting/reporting/intrastat#partner-configuration)
              * [Générer le rapport Intrastat](finance/accounting/reporting/intrastat#generate-the-intrastat-report)
            * Rapport de vérification de l’inaltérabilité des données
              * [Verrouiller les écritures comptabilisées avec hachage](finance/accounting/reporting/data_inalterability#lock-posted-entries-with-hash)
              * [Télécharger le rapport](finance/accounting/reporting/data_inalterability#report-download)
            * Intégration Silverfin
              * Configuration
                * Clé API Konvergo ERP
                  * [Per database](finance/accounting/reporting/silverfin#per-database)
                  * [For all databases (fiduciaries)](finance/accounting/reporting/silverfin#for-all-databases-fiduciaries)
            * Rapports personnalisés
              * [Rapports racines](finance/accounting/reporting/customize#root-reports)
              * [Variantes](finance/accounting/reporting/customize#variants)
              * [Lignes](finance/accounting/reporting/customize#lines)
              * Expressions
                * [Moteur “Domaine Konvergo ERP”](finance/accounting/reporting/customize#odoo-domain-engine)
                * [Moteur des “Étiquettes de taxes”](finance/accounting/reporting/customize#tax-tags-engine)
                * [Moteur “Agréger d’autres formules”](finance/accounting/reporting/customize#aggregate-other-formulas-engine)
                * [Moteur “Préfixe des codes de compte”](finance/accounting/reporting/customize#prefix-of-account-codes-engine)
                * [Moteur “Valeur externe”](finance/accounting/reporting/customize#external-value-engine)
                * [Moteur “Fonction Python personnalisée”](finance/accounting/reporting/customize#custom-python-function-engine)
              * [Colonnes](finance/accounting/reporting/customize#columns)
            * Clôture de l’exercice
              * [Exercices fiscaux](finance/accounting/reporting/year_end#fiscal-years)
              * Check-list de fin d’exercice
                * [Avant la clôture](finance/accounting/reporting/year_end#before-closure)
                * Clôture d’un exercice fiscal
                  * [Bénéfices de l’exercice en cours](finance/accounting/reporting/year_end#current-year-s-earnings)
  * [Notes de frais](finance/expenses)
    * [Définir des catégories de notes de frais](finance/expenses#set-expense-categories)
    * Enregistrer des notes de frais
      * Créer manuellement une nouvelle note de frais
        * [Joindre un reçu](finance/expenses#attach-a-receipt)
      * [Créer de nouvelles notes de frais à partir d’un reçu numérisé](finance/expenses#create-new-expenses-from-a-scanned-receipt)
      * [Créer automatiquement de nouvelles notes de frais à partir d’un email](finance/expenses#automatically-create-new-expenses-from-an-email)
    * Créer une note de frais
      * [Soumettre un rapport de notes de frais](finance/expenses#submit-an-expense-report)
    * [Approuver des notes de frais](finance/expenses#approve-expenses)
    * [Enregistrer des notes de frais dans la comptabilité](finance/expenses#post-expenses-in-accounting)
    * [Rembourser les employés](finance/expenses#reimburse-employees)
    * Refacturer des notes de frais aux clients
      * [Configuration](finance/expenses#setup)
      * [Créer une note de frais](finance/expenses#create-an-expense)
      * [Valider et comptabiliser des notes de frais](finance/expenses#validate-and-post-expenses)
      * [Facturer les notes de frais](finance/expenses#invoice-expenses)
  * [Paiements en ligne](finance/payment_providers)
    * Virements bancaires
      * [Configuration](finance/payment_providers/wire_transfer#configuration)
    * Adyen
      * Configuration
        * Onglet des identifiants
          * [Clé API et Clé client](finance/payment_providers/adyen#api-key-and-client-key)
          * [Clé HMAC](finance/payment_providers/adyen#hmac-key)
          * [URLs API](finance/payment_providers/adyen#api-urls)
        * Compte d’Adyen
          * [Autoriser les paiements d’une origine spécifique](finance/payment_providers/adyen#allow-payments-from-a-specific-origin)
        * [Faire une réservation sur une carte](finance/payment_providers/adyen#place-a-hold-on-a-card)
    * Alipay
      * Configuration
        * [Onglet des identifiants](finance/payment_providers/alipay#credentials-tab)
    * Amazon Payment Services
      * [Configuration sur le tableau de bord APS](finance/payment_providers/amazon_payment_services#configuration-on-aps-dashboard)
      * [Configuration dans Konvergo ERP](finance/payment_providers/amazon_payment_services#configuration-on-odoo)
    * AsiaPay
      * [Configuration sur le tableau de bord d’AsiaPay](finance/payment_providers/asiapay#configuration-on-asiapay-dashboard)
      * [Configuration dans Konvergo ERP](finance/payment_providers/asiapay#configuration-on-odoo)
    * Authorize.Net
      * Configuration
        * [Onglet des identifiants](finance/payment_providers/authorize#credentials-tab)
        * Onglet de configuration
          * [Faire une réservation sur une carte](finance/payment_providers/authorize#place-a-hold-on-a-card)
      * Paiements ACH (uniquement les USA)
        * [Configuration](finance/payment_providers/authorize#id2)
      * Importer un relevé Authorize.Net
        * [Exporter depuis Authorize.Net](finance/payment_providers/authorize#export-from-authorize-net)
        * [Importer dans Konvergo ERP](finance/payment_providers/authorize#import-into-odoo)
    * Buckaroo
      * [Configuration sur Buckaroo Plaza](finance/payment_providers/buckaroo#configuration-on-buckaroo-plaza)
      * [Configuration dans Konvergo ERP](finance/payment_providers/buckaroo#configuration-on-odoo)
    * Démo
      * [Configuration](finance/payment_providers/demo#configuration)
      * [Résultat du paiement](finance/payment_providers/demo#payment-outcome)
      * [Statut de la transaction](finance/payment_providers/demo#transaction-state)
    * Flutterwave
      * [Configuration sur le tableau de bord Flutterwave](finance/payment_providers/flutterwave#configuration-on-flutterwave-dashboard)
      * [Configuration dans Konvergo ERP](finance/payment_providers/flutterwave#configuration-on-odoo)
    * Mercado Pago
      * [Configuration sur le tableau de bord Mercado Pago](finance/payment_providers/mercado_pago#configuration-on-mercado-pago-dashboard)
      * [Configuration dans Konvergo ERP](finance/payment_providers/mercado_pago#configuration-on-odoo)
    * Mollie
      * Configuration
        * [Onglet des identifiants](finance/payment_providers/mollie#credentials-tab)
    * Ogone
      * Paramètres dans Ogone
        * [Créer un utilisateur API](finance/payment_providers/ogone#create-an-api-user)
        * [Configurer Ogone pour Konvergo ERP](finance/payment_providers/ogone#set-up-ogone-for-odoo)
      * [Paramètres dans Konvergo ERP](finance/payment_providers/ogone#settings-in-odoo)
    * PayPal
      * Paramètres dans PayPal
        * [Renvoi automatique](finance/payment_providers/paypal#auto-return)
        * [Transfert des données de paiement (PDT)](finance/payment_providers/paypal#payment-data-transfer-pdt)
        * [Notification instantanée de paiement (IPN)](finance/payment_providers/paypal#instant-payment-notification-ipn)
        * [Compte PayPal facultatif](finance/payment_providers/paypal#paypal-account-optional)
        * [Format des messages de paiement](finance/payment_providers/paypal#payment-messages-format)
      * Paramètres dans Konvergo ERP
        * [Identifiants](finance/payment_providers/paypal#credentials)
        * [Frais supplémentaires](finance/payment_providers/paypal#extra-fees)
      * Environnement de test
        * [Configuration](finance/payment_providers/paypal#configuration)
    * Razorpay
      * [Configuration sur le tableau de bord de Razorpay](finance/payment_providers/razorpay#configuration-on-razorpay-dashboard)
      * [Configuration dans Konvergo ERP](finance/payment_providers/razorpay#configuration-on-odoo)
    * SIPS
      * Configuration
        * [Onglet des identifiants](finance/payment_providers/sips#credentials-tab)
    * Stripe
      * Create your Stripe account with Konvergo ERP
        * [Remplir vos identifiants](finance/payment_providers/stripe#fill-in-your-credentials)
        * [Générer un webhook](finance/payment_providers/stripe#generate-a-webhook)
      * [Activer les modes de paiement locaux](finance/payment_providers/stripe#enable-local-payment-methods)
      * [Activer Apple Pay](finance/payment_providers/stripe#enable-apple-pay)
    * Fournisseurs de paiement pris en charge
      * [Fournisseurs de paiement en ligne](finance/payment_providers#online-payment-providers)
      * [Paiements bancaires](finance/payment_providers#bank-payments)
    * Enable a payment provider
      * [Mode test](finance/payment_providers#test-mode)
    * [Payment form](finance/payment_providers#payment-form)
    * [Tokenisation](finance/payment_providers#tokenization)
    * [Capture manuelle](finance/payment_providers#manual-capture)
    * [Remboursements](finance/payment_providers#refunds)
    * [Paiement rapide](finance/payment_providers#express-checkout)
    * [Frais supplémentaires](finance/payment_providers#extra-fees)
    * Disponibilité
      * [Currencies and countries](finance/payment_providers#currencies-and-countries)
      * [Maximum amount](finance/payment_providers#maximum-amount)
    * Journal des paiements
      * [Perspective comptable](finance/payment_providers#accounting-perspective)
  * [Localisations fiscales](finance/fiscal_localizations)
    * Packages de localisation fiscale
      * [Configuration](finance/fiscal_localizations#configuration)
      * [Utilisation](finance/fiscal_localizations#use)
    * Liste des pays pris en charge
      * Argentine
        * [Webinars](finance/fiscal_localizations/argentina#webinars)
        * Configuration
          * [Installation des modules](finance/fiscal_localizations/argentina#modules-installation)
          * [Configurer votre société](finance/fiscal_localizations/argentina#configure-your-company)
          * [Plan comptable](finance/fiscal_localizations/argentina#chart-of-account)
          * Configurer les données de base
            * Identifiants de facturation électronique
              * [Environnement](finance/fiscal_localizations/argentina#environment)
              * [Certificats AFIP](finance/fiscal_localizations/argentina#afip-certificates)
            * Partenaire
              * [Type d’identification et TVA](finance/fiscal_localizations/argentina#identification-type-and-vat)
              * [Type de responsabilité AFIP](finance/fiscal_localizations/argentina#afip-responsibility-type)
            * Taxes
              * [Types de taxes](finance/fiscal_localizations/argentina#taxes-types)
              * [Taxes spéciales](finance/fiscal_localizations/argentina#special-taxes)
            * Types de document
              * [Lettres](finance/fiscal_localizations/argentina#letters)
              * [Utilisation sur les factures](finance/fiscal_localizations/argentina#use-on-invoices)
          * Journaux
            * Informations AFIP (ou Point de Vente AFIP)
              * [Services web](finance/fiscal_localizations/argentina#web-services)
            * [Séquences](finance/fiscal_localizations/argentina#sequences)
        * Utilisation et tests
          * Facture
            * [Attribution du type de document](finance/fiscal_localizations/argentina#document-type-assignation)
            * [Éléments de la facture électronique](finance/fiscal_localizations/argentina#electronic-invoice-elements)
            * [Taxes sur les factures](finance/fiscal_localizations/argentina#invoice-taxes)
            * Cas d’utilisation particuliers
              * [Factures pour des services](finance/fiscal_localizations/argentina#invoices-for-services)
              * [Factures d’exportation](finance/fiscal_localizations/argentina#exportation-invoices)
              * [Bon fiscal](finance/fiscal_localizations/argentina#fiscal-bond)
              * [Facture de crédit électronique MiPyMe (FCE)](finance/fiscal_localizations/argentina#electronic-credit-invoice-mipyme-fce)
            * [Rapport imprimé de la facture](finance/fiscal_localizations/argentina#invoice-printed-report)
            * [Résolution des problèmes et audit](finance/fiscal_localizations/argentina#troubleshooting-and-auditing)
          * Factures fournisseurs
            * Validez le numéro de la facture fournisseur dans AFIP
              * [Valider les factures fournisseurs dans Konvergo ERP](finance/fiscal_localizations/argentina#validate-vendor-bills-in-odoo)
            * Cas d’utilisation particuliers
              * [Postes exonérés](finance/fiscal_localizations/argentina#untaxed-concepts)
              * [Taxes de perception](finance/fiscal_localizations/argentina#perception-taxes)
          * Gestion des chèques
            * Chèques propres
              * [Gestion des chèques propres](finance/fiscal_localizations/argentina#management-of-own-checks)
              * [Annuler un chèque propre](finance/fiscal_localizations/argentina#cancel-an-own-check)
            * Chèques de tiers
              * [Nouveau chèques de tiers](finance/fiscal_localizations/argentina#new-third-party-checks)
              * [Chèques de tiers existants](finance/fiscal_localizations/argentina#existing-third-party-checks)
        * Rapports
          * Rapports TVA
            * [Livre des ventes TVA](finance/fiscal_localizations/argentina#sales-vat-book)
            * [Livre des achats TVA](finance/fiscal_localizations/argentina#purchases-vat-book)
            * [Récapitulatif TVA](finance/fiscal_localizations/argentina#vat-summary)
          * IIBB (Impôt sur le revenu brut) - Rapports
            * [IIBB (Impôt sur le revenu brut) - Ventes par province](finance/fiscal_localizations/argentina#iibb-sales-by-jurisdiction)
            * [IIBB (Impôt sur le revenu brut) - Ventes par province](finance/fiscal_localizations/argentina#iibb-purchases-by-jurisdiction)
      * Australie
        * Paie australienne avec Employment Hero
          * [Configuration](finance/fiscal_localizations/australia#configuration)
          * [Comment fonctionne l’API ?](finance/fiscal_localizations/australia#how-does-the-api-work)
      * Belgique
        * [Configuration](finance/fiscal_localizations/belgium#configuration)
        * [Plan comptable](finance/fiscal_localizations/belgium#chart-of-accounts)
        * Taxes
          * [Taxes non déductibles](finance/fiscal_localizations/belgium#non-deductible-taxes)
        * Rapports
          * Rapport de dépenses non admises
            * [Frais de restaurant](finance/fiscal_localizations/belgium#restaurant-expenses)
            * [Frais de voiture : Répartition des véhicules](finance/fiscal_localizations/belgium#car-expenses-vehicle-split)
        * Fiche fiscale 281.50 et relevé 325
          * [Fiche fiscale 281.50](finance/fiscal_localizations/belgium#fee-form-281-50)
          * [Relevé 325](finance/fiscal_localizations/belgium#form-325)
        * Fichiers CODA et SODA
          * [CODA](finance/fiscal_localizations/belgium#coda)
          * [SODA](finance/fiscal_localizations/belgium#soda)
        * [Facturation électronique](finance/fiscal_localizations/belgium#electronic-invoicing)
        * [Escompte](finance/fiscal_localizations/belgium#cash-discount)
        * Certification fiscale : PdV restaurant
          * [Système de caisse certifié](finance/fiscal_localizations/belgium#certified-pos-system)
          * Fiscal Data Module (FDM)
            * Configuration
              * [Module boîte noire](finance/fiscal_localizations/belgium#black-box-module)
              * [IoT Box](finance/fiscal_localizations/belgium#iot-box)
          * [VAT signing card](finance/fiscal_localizations/belgium#vat-signing-card)
      * Brésil
        * [Introduction](finance/fiscal_localizations/brazil#introduction)
        * Configuration
          * [Installation des modules](finance/fiscal_localizations/brazil#modules-installation)
          * [Configurer votre société](finance/fiscal_localizations/brazil#configure-your-company)
          * Configurer l’intégration d’AvaTax
            * [Configuration des identifiants](finance/fiscal_localizations/brazil#credential-configuration)
          * Configurer les données de base
            * [Plan comptable](finance/fiscal_localizations/brazil#chart-of-accounts)
            * [Taxes](finance/fiscal_localizations/brazil#taxes)
            * [Produits](finance/fiscal_localizations/brazil#products)
            * [Contacts](finance/fiscal_localizations/brazil#contacts)
            * [Positions fiscales](finance/fiscal_localizations/brazil#fiscal-positions)
        * Flux de travail
          * [Calculs des taxes sur les devis / commandes clients](finance/fiscal_localizations/brazil#tax-calculations-on-quotation-sales-orders)
          * [Calculs des taxes sur les factures](finance/fiscal_localizations/brazil#tax-calculations-on-invoices)
      * Chili
        * [Modules](finance/fiscal_localizations/chile#modules)
        * [Informations relatives à l’entreprise](finance/fiscal_localizations/chile#company-information)
        * Accounting settings
          * [Informations fiscales](finance/fiscal_localizations/chile#fiscal-information)
          * [Electronic invoice data](finance/fiscal_localizations/chile#electronic-invoice-data)
        * DTE incoming email server
          * [Certificat](finance/fiscal_localizations/chile#certificate)
        * [Multi-devises](finance/fiscal_localizations/chile#multicurrency)
        * [Informations relatives au partenaire](finance/fiscal_localizations/chile#partner-information)
        * Types de document
          * [Utilisation sur les factures](finance/fiscal_localizations/chile#use-on-invoices)
        * Journaux
          * [Create a sales journal](finance/fiscal_localizations/chile#create-a-sales-journal)
        * CAF
          * [Upload CAF files](finance/fiscal_localizations/chile#upload-caf-files)
        * [Plan comptable](finance/fiscal_localizations/chile#chart-of-accounts)
        * [Taxes](finance/fiscal_localizations/chile#taxes)
        * Utilisation et tests
          * [Electronic invoice workflow](finance/fiscal_localizations/chile#electronic-invoice-workflow)
          * Customer invoice emission
            * [Validation and DTE status](finance/fiscal_localizations/chile#validation-and-dte-status)
            * [Références croisées](finance/fiscal_localizations/chile#crossed-references)
            * [Rapport PDF de la facture](finance/fiscal_localizations/chile#invoice-pdf-report)
            * [Commercial validation](finance/fiscal_localizations/chile#commercial-validation)
            * [Processed for claimed invoices](finance/fiscal_localizations/chile#processed-for-claimed-invoices)
            * [Erreurs courantes](finance/fiscal_localizations/chile#common-errors)
          * Avoirs
            * Cas d’utilisation
              * [Cancel referenced document](finance/fiscal_localizations/chile#cancel-referenced-document)
              * [Correct referenced document](finance/fiscal_localizations/chile#correct-referenced-document)
              * [Corrects referenced document amount](finance/fiscal_localizations/chile#corrects-referenced-document-amount)
          * Notes de débit
            * Cas d’utilisation
              * [Add debt on invoices](finance/fiscal_localizations/chile#add-debt-on-invoices)
              * [Cancel credit notes](finance/fiscal_localizations/chile#cancel-credit-notes)
          * Factures fournisseurs
            * [Réception](finance/fiscal_localizations/chile#reception)
            * [Acceptation](finance/fiscal_localizations/chile#acceptation)
            * [Réclamation](finance/fiscal_localizations/chile#claim)
          * Electronic purchase invoice
            * [Configuration](finance/fiscal_localizations/chile#configuration)
            * [Generate an electronic purchase invoice](finance/fiscal_localizations/chile#generate-an-electronic-purchase-invoice)
          * Guide de livraison
            * [Delivery guide from a sales process](finance/fiscal_localizations/chile#delivery-guide-from-a-sales-process)
          * Electronic receipt
            * [Validation and DTE status](finance/fiscal_localizations/chile#id2)
          * Electronic export of goods
            * [Contact configurations](finance/fiscal_localizations/chile#contact-configurations)
            * [Chilean customs](finance/fiscal_localizations/chile#chilean-customs)
            * [PDF report](finance/fiscal_localizations/chile#pdf-report)
        * Rapports financiers
          * [Balance tributario de 8 columnas](finance/fiscal_localizations/chile#balance-tributario-de-8-columnas)
          * [Propuesta F29](finance/fiscal_localizations/chile#propuesta-f29)
      * Colombie
        * Configuration
          * [Installation des modules](finance/fiscal_localizations/colombia#modules-installation)
          * [Configuration de l’entreprise](finance/fiscal_localizations/colombia#company-configuration)
          * [Configuration des identifiants Carjaval](finance/fiscal_localizations/colombia#carjaval-credentials-configuration)
          * [Configuration des données du rapport](finance/fiscal_localizations/colombia#report-data-configuration)
          * Configuration des données de base
            * Partenaire
              * [Informations d’identification](finance/fiscal_localizations/colombia#identification-information)
              * [Informations fiscales](finance/fiscal_localizations/colombia#fiscal-information)
            * [Produits](finance/fiscal_localizations/colombia#products)
            * [Taxes](finance/fiscal_localizations/colombia#taxes)
            * Journaux de vente
              * [Séquence des factures](finance/fiscal_localizations/colombia#invoice-sequence)
              * [Journaux des achats](finance/fiscal_localizations/colombia#purchase-journals)
              * [Plan comptable](finance/fiscal_localizations/colombia#chart-of-accounts)
        * Principaux flux de travail
          * Facturation électronique
            * [Création d’une facture](finance/fiscal_localizations/colombia#invoice-creation)
            * [Validation des factures](finance/fiscal_localizations/colombia#invoice-validation)
            * [Réception des fichiers juridiques XML et PDF](finance/fiscal_localizations/colombia#reception-of-legal-xml-and-pdf)
          * [Avoirs](finance/fiscal_localizations/colombia#credit-notes)
          * [Notes de débit](finance/fiscal_localizations/colombia#debit-notes)
          * [Document d’accompagnement pour les factures fournisseurs](finance/fiscal_localizations/colombia#support-document-for-vendor-bills)
          * [Erreurs courantes](finance/fiscal_localizations/colombia#common-errors)
        * Rapports financiers
          * [Certificado de Retención en ICA](finance/fiscal_localizations/colombia#certificado-de-retencion-en-ica)
          * [Certificado de Retención en IVA](finance/fiscal_localizations/colombia#certificado-de-retencion-en-iva)
          * [Certificado de Retención en la Fuente](finance/fiscal_localizations/colombia#certificado-de-retencion-en-la-fuente)
      * Équateur
        * Introduction
          * [Glossaire](finance/fiscal_localizations/ecuador#glossary)
        * Configuration
          * [Installation des modules](finance/fiscal_localizations/ecuador#modules-installation)
          * [Configurer votre société](finance/fiscal_localizations/ecuador#configure-your-company)
          * [Documents électroniques](finance/fiscal_localizations/ecuador#electronic-documents)
          * [Retenue de la TVA](finance/fiscal_localizations/ecuador#vat-withholding)
          * [Points d’impression](finance/fiscal_localizations/ecuador#printer-points)
          * [Retenue](finance/fiscal_localizations/ecuador#withholding)
          * [Preuves d’achat](finance/fiscal_localizations/ecuador#purchase-liquidations)
          * Configurer les données de base
            * [Plan comptable](finance/fiscal_localizations/ecuador#chart-of-accounts)
            * [Produits](finance/fiscal_localizations/ecuador#products)
            * [Contacts](finance/fiscal_localizations/ecuador#contacts)
            * [Revoir vos taxes](finance/fiscal_localizations/ecuador#review-your-taxes)
            * [Revoir vos types de documents](finance/fiscal_localizations/ecuador#review-your-document-types)
        * Flux de travail
          * Documents de vente
            * [Factures clients](finance/fiscal_localizations/ecuador#customer-invoices)
            * [Avoir client](finance/fiscal_localizations/ecuador#customer-credit-note)
            * [Note de débit client](finance/fiscal_localizations/ecuador#customer-debit-note)
            * [Retenue client](finance/fiscal_localizations/ecuador#customer-withholding)
          * Documents d’achat
            * [Facture fournisseur](finance/fiscal_localizations/ecuador#vendor-bill)
            * [Preuve d’achat](finance/fiscal_localizations/ecuador#purchase-liquidation)
            * [Retenue sur les achats](finance/fiscal_localizations/ecuador#purchase-withholding)
        * Rapports financiers
          * [Déclaration 103](finance/fiscal_localizations/ecuador#report-103)
          * [Déclaration 104](finance/fiscal_localizations/ecuador#report-104)
          * ATS report
            * Configuration
              * [Factures fournisseurs](finance/fiscal_localizations/ecuador#vendor-bills)
              * [Credit and debit notes](finance/fiscal_localizations/ecuador#credit-and-debit-notes)
            * [XML generation](finance/fiscal_localizations/ecuador#xml-generation)
      * Égypte
        * [Installation](finance/fiscal_localizations/egypt#installation)
        * Facturation électronique égyptienne
          * [Enregistrer Konvergo ERP sur votre portail ETA](finance/fiscal_localizations/egypt#register-odoo-on-your-eta-portal)
          * Configuration dans Konvergo ERP
            * [Codes ETA](finance/fiscal_localizations/egypt#eta-codes)
            * [Branches](finance/fiscal_localizations/egypt#branches)
            * [Clients](finance/fiscal_localizations/egypt#customers)
            * [Produits](finance/fiscal_localizations/egypt#products)
          * Authentification par USB
            * [Installer Konvergo ERP en tant que proxy local sur votre ordinateur](finance/fiscal_localizations/egypt#install-odoo-as-a-local-proxy-on-your-computer)
            * [Configurer la clé USB](finance/fiscal_localizations/egypt#configure-the-usb-key)
      * France
        * FEC - Fichier des écritures comptables
          * Import FEC
            * [Formats de fichier](finance/fiscal_localizations/france#file-formats)
            * [Description et utilisation des champs](finance/fiscal_localizations/france#fields-description-and-use)
            * Détails de la mise en œuvre
              * [Comptes](finance/fiscal_localizations/france#accounts)
              * [Correspondance des codes](finance/fiscal_localizations/france#code-matching)
              * [Indicateur de lettrage](finance/fiscal_localizations/france#reconcilable-flag)
              * [Correspondance entre le type de compte et les modèles](finance/fiscal_localizations/france#account-type-and-templates-matching)
              * [Journaux](finance/fiscal_localizations/france#journals)
              * [Détermination du type de journal](finance/fiscal_localizations/france#journal-type-determination)
              * [Partenaires](finance/fiscal_localizations/france#partners)
              * [Écritures](finance/fiscal_localizations/france#moves)
              * [Problèmes d’arrondi](finance/fiscal_localizations/france#rounding-issues)
              * [Nom d’écriture manquant](finance/fiscal_localizations/france#missing-move-name)
              * [Informations relatives au partenaire](finance/fiscal_localizations/france#partner-information)
          * [Export](finance/fiscal_localizations/france#export)
        * [Rapports comptables français](finance/fiscal_localizations/france#french-accounting-reports)
        * Se conformer à la législation anti-fraude TVA avec Konvergo ERP
          * [Mon entreprise est-elle tenue d’utiliser un logiciel anti-fraude ?](finance/fiscal_localizations/france#is-my-company-required-to-use-anti-fraud-software)
          * [Se conformer à la législation avec Konvergo ERP](finance/fiscal_localizations/france#get-certified-with-odoo)
          * Fonctionnalités anti-fraude
            * [Inaltérabilité](finance/fiscal_localizations/france#inalterability)
            * [Sécurisation](finance/fiscal_localizations/france#security)
            * [Conservation](finance/fiscal_localizations/france#storage)
          * [Responsabilités](finance/fiscal_localizations/france#responsibilities)
          * [Plus d’informations](finance/fiscal_localizations/france#more-information)
      * Allemagne
        * [Plan comptable allemand](finance/fiscal_localizations/germany#german-chart-of-accounts)
        * [Rapports comptables allemands](finance/fiscal_localizations/germany#german-accounting-reports)
        * [Exporter d’Konvergo ERP vers Datev](finance/fiscal_localizations/germany#export-from-odoo-to-datev)
        * Point de vente en Allemagne : Système de sécurité technique
          * Configuration
            * [Installation des modules](finance/fiscal_localizations/germany#modules-installation)
            * [Enregistrer votre entreprise auprès de l’autorité financière](finance/fiscal_localizations/germany#register-your-company-at-the-financial-authority)
            * [Créer et lier un Système de sécurité technique à votre PdV](finance/fiscal_localizations/germany#create-and-link-a-technical-security-system-to-your-pos)
          * [DSFinV-K](finance/fiscal_localizations/germany#dsfinv-k)
        * Normes comptables fiscales allemandes : Le guide Konvergo ERP de la conformité aux normes GoBD
          * [Que faut-il savoir sur le GoBD lorsqu’on utilise un logiciel de comptabilité ?](finance/fiscal_localizations/germany#what-do-you-need-to-know-about-gobd-when-relying-on-accounting-software)
          * [Qu’en est-il de la sécurité des données ?](finance/fiscal_localizations/germany#what-about-data-security)
          * [Responsabilité de l’éditeur de logiciel](finance/fiscal_localizations/germany#responsibility-of-the-software-editor)
          * [Comment est-ce qu’Konvergo ERP peut vous aider à être conforme ?](finance/fiscal_localizations/germany#how-can-odoo-help-you-achieve-compliance)
          * [Avez-vous besoin d’un export GoBD ?](finance/fiscal_localizations/germany#do-you-need-a-gobd-export)
          * [Quel est le rôle et la signification de la certification de conformité ?](finance/fiscal_localizations/germany#what-is-the-role-and-meaning-of-the-compliance-certification)
          * [Que se passe-t-il si vous n’êtes pas en conformité ?](finance/fiscal_localizations/germany#what-happens-if-you-are-not-compliant)
      * Inde
        * [Installation](finance/fiscal_localizations/india#installation)
        * Système de facturation électronique
          * Configuration
            * [Enregistrement NIC e-Invoice](finance/fiscal_localizations/india#nic-e-invoice-registration)
            * Configuration dans Konvergo ERP
              * [Journaux](finance/fiscal_localizations/india#journals)
          * Flux de travail
            * [Validation des factures](finance/fiscal_localizations/india#invoice-validation)
            * [Rapport PDF de la facture](finance/fiscal_localizations/india#invoice-pdf-report)
            * [Annulation de la facture électronique](finance/fiscal_localizations/india#e-invoice-cancellation)
            * [Vérification de la facture électronique GST](finance/fiscal_localizations/india#gst-e-invoice-verification)
        * E-Way bill
          * Configuration
            * [Enregistrement API sur NIC E-Way bill](finance/fiscal_localizations/india#api-registration-on-nic-e-way-bill)
            * [Configuration dans Konvergo ERP](finance/fiscal_localizations/india#india-e-waybill-configuration)
          * Flux de travail
            * [Envoyer un E-Way bill](finance/fiscal_localizations/india#send-an-e-way-bill)
            * [Validation des factures](finance/fiscal_localizations/india#india-invoice-validation-e-way)
            * [Rapport PDF de la facture](finance/fiscal_localizations/india#id6)
            * [Annulation de l’E-Way bill](finance/fiscal_localizations/india#e-way-bill-cancellation)
        * Dépôt déclaration GST en Inde
          * [Activer l’accès API](finance/fiscal_localizations/india#enable-api-access)
          * [Service GST indien dans Konvergo ERP](finance/fiscal_localizations/india#indian-gst-service-in-odoo)
          * Déposer une déclaration GST
            * [Envoyer GSTR-1](finance/fiscal_localizations/india#send-gstr-1)
            * [Recevoir GSTR-2B](finance/fiscal_localizations/india#receive-gstr-2b)
            * [Rapport GSTR-3](finance/fiscal_localizations/india#gstr-3-report)
        * Déclarations d’impôt
          * [Rapport GSTR-1](finance/fiscal_localizations/india#gstr-1-report)
          * [Rapport GSTR-3](finance/fiscal_localizations/india#india-gstr-3-report)
      * Indonésie
        * Module E-Faktur
          * [Paramètres NPWP/NIK](finance/fiscal_localizations/indonesia#npwp-nik-settings)
          * Utilisation
            * [Générer le numéro de série de la facture fiscale](finance/fiscal_localizations/indonesia#generate-tax-invoice-serial-number)
            * [Générer e-faktur csv pour une seule facture ou un lot de factures](finance/fiscal_localizations/indonesia#generate-e-faktur-csv-for-a-single-invoice-or-a-batch-invoices)
            * [Kode Transaksi FP (Code de transaction)](finance/fiscal_localizations/indonesia#kode-transaksi-fp-transaction-code)
            * [Corriger une facture qui a été comptabilisée et téléchargée : Fonctionnalité Remplacer la facture](finance/fiscal_localizations/indonesia#correct-an-invoice-that-has-been-posted-and-downloaded-replace-invoice-feature)
            * [Corriger une facture qui a été comptabilisée, mais pas encore téléchargée : Réinitialiser e-Faktur](finance/fiscal_localizations/indonesia#correct-an-invoice-that-has-been-posted-but-not-downloaded-yet-reset-e-faktur)
      * Italie
        * Configuration
          * [Informations relatives à l’entreprise](finance/fiscal_localizations/italy#company-information)
          * Facturation électronique
            * [Échange de données informatisé (EDI)](finance/fiscal_localizations/italy#electronic-data-interchange-edi)
          * [Autorisation de traitement des fichiers (Konvergo ERP)](finance/fiscal_localizations/italy#file-processing-authorization-odoo)
        * Configuration des taxes
          * Autoliquidation externe
            * [Factures clients](finance/fiscal_localizations/italy#invoices)
            * [Factures fournisseurs](finance/fiscal_localizations/italy#vendor-bills)
          * [Autoliquidation interne](finance/fiscal_localizations/italy#internal-reverse-charge)
          * [Grilles fiscales d’autoliquidation](finance/fiscal_localizations/italy#reverse-charge-tax-grids)
        * Saint-Marin
          * [Factures clients](finance/fiscal_localizations/italy#id1)
          * [Factures fournisseurs](finance/fiscal_localizations/italy#bills)
        * Pubblica amministrazione (B2G)
          * [Signature numérique qualifiée](finance/fiscal_localizations/italy#digital-qualified-signature)
          * [CIG, CUP, DatiOrdineAcquisto](finance/fiscal_localizations/italy#cig-cup-datiordineacquisto)
      * Kenya
        * [Configuration](finance/fiscal_localizations/kenya#configuration)
        * Intégration TIMS au Kenya
          * [Installer le serveur proxy sur un appareil Windows](finance/fiscal_localizations/kenya#installing-the-proxy-server-on-a-windows-device)
          * [Envoyer les données à la KRA via l’Unité de contrôle G03 Tremol](finance/fiscal_localizations/kenya#sending-the-data-to-kra-using-the-tremol-g03-control-unit)
      * Luxembourg
        * [Configuration](finance/fiscal_localizations/luxembourg#configuration)
        * [Plan comptable normalisé - PCN 2020](finance/fiscal_localizations/luxembourg#standard-chart-of-accounts-pcn-2020)
        * [Déclaration de TVA eCDF](finance/fiscal_localizations/luxembourg#ecdf-tax-return)
        * [Déclaration de TVA annuelle](finance/fiscal_localizations/luxembourg#annual-tax-report)
        * FAIA (SAF-T)
          * [Exporter le fichier FAIA](finance/fiscal_localizations/luxembourg#export-faia-file)
      * Mexique
        * [Webinars](finance/fiscal_localizations/mexico#webinars)
        * [Introduction](finance/fiscal_localizations/mexico#introduction)
        * Configuration
          * [Prérequis](finance/fiscal_localizations/mexico#requirements)
          * [Installing modules](finance/fiscal_localizations/mexico#installing-modules)
          * [Configurer votre société](finance/fiscal_localizations/mexico#configure-your-company)
          * [Contacts](finance/fiscal_localizations/mexico#contacts)
          * Taxes
            * [Type de facteur](finance/fiscal_localizations/mexico#factor-type)
            * [Objet fiscal](finance/fiscal_localizations/mexico#tax-object)
            * [Autres configurations fiscales](finance/fiscal_localizations/mexico#other-tax-configurations)
          * [Produits](finance/fiscal_localizations/mexico#products)
          * Facturation électronique
            * [Identifiants PAC](finance/fiscal_localizations/mexico#pac-credentials)
            * [Certificats .cer et .key](finance/fiscal_localizations/mexico#cer-and-key-certificates)
        * Flux de travail
          * Facturation électronique
            * [Factures clients](finance/fiscal_localizations/mexico#customer-invoices)
            * [Avoirs](finance/fiscal_localizations/mexico#credit-notes)
            * Compléments de paiement
              * [Politique de paiement](finance/fiscal_localizations/mexico#payment-policy)
              * [Flux de paiement](finance/fiscal_localizations/mexico#payment-flow)
            * Annulation des factures
              * [01 - factures envoyées avec des erreurs avec relation](finance/fiscal_localizations/mexico#invoices-sent-with-errors-with-a-relation)
              * [02 - factures envoyées avec des erreurs sans relation](finance/fiscal_localizations/mexico#invoices-sent-with-errors-without-a-relation)
              * [Annulation de paiement](finance/fiscal_localizations/mexico#payment-cancellations)
            * Cas d’utilisation particuliers de la facturation
              * [CFDI au public](finance/fiscal_localizations/mexico#cfdi-to-public)
              * [Multi-devises](finance/fiscal_localizations/mexico#multicurrency)
              * [Acomptes](finance/fiscal_localizations/mexico#down-payments)
          * Commerce extérieur
            * Configuration
              * [Contacts](finance/fiscal_localizations/mexico#id3)
              * [Produits](finance/fiscal_localizations/mexico#id4)
            * [Flux de facturation](finance/fiscal_localizations/mexico#invoicing-flow)
          * Guide de livraison
            * Configuration
              * [Contacts et véhicules](finance/fiscal_localizations/mexico#contacts-and-vehicles)
              * [Produits](finance/fiscal_localizations/mexico#id6)
            * Flux de vente et d’inventaire
              * [Risques dangereux](finance/fiscal_localizations/mexico#dangerous-hazards)
          * Numéros de douane
            * [Configuration](finance/fiscal_localizations/mexico#id8)
            * [Flux d’achats et de ventes](finance/fiscal_localizations/mexico#purchase-and-sales-flow)
          * Comptabilité électronique
            * [Plan comptable](finance/fiscal_localizations/mexico#chart-of-accounts)
            * [Balance générale](finance/fiscal_localizations/mexico#trial-balance)
            * [Grand livre](finance/fiscal_localizations/mexico#general-ledger)
            * [Déclaration DIOT](finance/fiscal_localizations/mexico#diot-report)
      * Pays-Bas
        * [Export XAF](finance/fiscal_localizations/netherlands#xaf-export)
        * [Rapports comptables néerlandais](finance/fiscal_localizations/netherlands#dutch-accounting-reports)
      * Roumanie
        * [Configuration](finance/fiscal_localizations/romania#configuration)
        * Déclaration D.406
          * Configuration
            * [Société](finance/fiscal_localizations/romania#company)
            * [Plan comptable](finance/fiscal_localizations/romania#chart-of-accounts)
            * [Client et fournisseur](finance/fiscal_localizations/romania#customer-and-supplier)
            * [Taxe](finance/fiscal_localizations/romania#tax)
            * [Produit](finance/fiscal_localizations/romania#product)
            * [Facture fournisseur](finance/fiscal_localizations/romania#vendor-bill)
          * Générer la déclaration
            * [Exporter vos données](finance/fiscal_localizations/romania#exporting-your-data)
            * [Signer le rapport](finance/fiscal_localizations/romania#signing-the-report)
      * Pérou
        * [Introduction](finance/fiscal_localizations/peru#introduction)
        * Configuration
          * Installer les modules de la localisation péruvienne
            * [Configurer votre société](finance/fiscal_localizations/peru#configure-your-company)
            * [Plan comptable](finance/fiscal_localizations/peru#chart-of-account)
          * Paramètres de la comptabilité
            * [Concepts de base](finance/fiscal_localizations/peru#basic-concepts)
            * Fournisseur de signature
              * IAP (Achats In-App d’Konvergo ERP)
                * [Qu’est-ce que l’IAP ?](finance/fiscal_localizations/peru#what-is-the-iap)
                * [Comment cela fonctionne-t-il ?](finance/fiscal_localizations/peru#how-does-it-work)
                * [Que devez-vous faire ?](finance/fiscal_localizations/peru#what-do-you-need-to-do)
              * [Digiflow](finance/fiscal_localizations/peru#digiflow)
              * [SUNAT](finance/fiscal_localizations/peru#sunat)
            * [Environnement de test](finance/fiscal_localizations/peru#testing-environment)
            * [Certificat](finance/fiscal_localizations/peru#certificate)
            * [Multi-devises](finance/fiscal_localizations/peru#multicurrency)
          * Configurer les données de base
            * Taxes
              * [Configuration EDI](finance/fiscal_localizations/peru#edi-configuration)
            * [Positions fiscales](finance/fiscal_localizations/peru#fiscal-positions)
            * [Types de documents](finance/fiscal_localizations/peru#document-types)
            * Journaux
              * [Utiliser les documents](finance/fiscal_localizations/peru#use-documents)
              * [Échange de données informatisé](finance/fiscal_localizations/peru#electronic-data-interchange)
            * Partenaire
              * [Type d’identification et TVA](finance/fiscal_localizations/peru#identification-type-and-vat)
            * [Produit](finance/fiscal_localizations/peru#product)
        * Utilisation et tests
          * Facture client
            * [Éléments EDI](finance/fiscal_localizations/peru#edi-elements)
            * Validation des factures
              * [Statut de la facture électronique](finance/fiscal_localizations/peru#electronic-invoice-status)
            * [Erreurs courantes](finance/fiscal_localizations/peru#common-errors)
            * [Rapport PDF de la facture](finance/fiscal_localizations/peru#invoice-pdf-report)
            * [Crédits IAP](finance/fiscal_localizations/peru#iap-credits)
            * Cas d’utilisation particuliers
              * Processus d’annulation
                * [Statut de la facture électronique](finance/fiscal_localizations/peru#id3)
              * [Processus d’annulation](finance/fiscal_localizations/peru#id4)
              * [Acomptes](finance/fiscal_localizations/peru#advance-payments)
              * [Factures de rabais](finance/fiscal_localizations/peru#detraction-invoices)
          * [Avoirs](finance/fiscal_localizations/peru#credit-notes)
          * [Notes de débit](finance/fiscal_localizations/peru#debit-notes)
          * Electronic delivery guide 2.0
            * Delivery guide types
              * [Expéditeur](finance/fiscal_localizations/peru#sender)
              * [Transporteur](finance/fiscal_localizations/peru#carrier)
            * Transportation types
              * [Privée](finance/fiscal_localizations/peru#private)
              * [Public](finance/fiscal_localizations/peru#public)
            * [Direct submission to SUNAT](finance/fiscal_localizations/peru#direct-submission-to-sunat)
            * [Required information](finance/fiscal_localizations/peru#required-information)
            * [Cancellations](finance/fiscal_localizations/peru#cancellations)
            * [Mode test](finance/fiscal_localizations/peru#testing)
            * Configuration
              * [Opérateur](finance/fiscal_localizations/peru#operator)
              * [Transporteur](finance/fiscal_localizations/peru#id6)
              * [Véhicules](finance/fiscal_localizations/peru#vehicles)
              * [Produits](finance/fiscal_localizations/peru#products)
            * [Generating a GRE](finance/fiscal_localizations/peru#generating-a-gre)
            * [Erreurs courantes](finance/fiscal_localizations/peru#id7)
      * Les Philippines
        * Configuration
          * [Plan comptable et taxes](finance/fiscal_localizations/philippines#chart-of-accounts-and-taxes)
          * [Contacts](finance/fiscal_localizations/philippines#contacts)
        * [Rapport BIR 2307](finance/fiscal_localizations/philippines#bir-2307-report)
      * Arabie saoudite
        * [Configuration](finance/fiscal_localizations/saudi_arabia#configuration)
        * Facturation électronique ZATCA
          * [Informations relatives à l’entreprise](finance/fiscal_localizations/saudi_arabia#company-information)
          * Mode simulation
            * [Portail de simulation de Fatoora](finance/fiscal_localizations/saudi_arabia#fatoora-simulation-portal)
            * [Intégration de l’API ZATCA](finance/fiscal_localizations/saudi_arabia#zatca-api-integration)
            * [Journaux de vente](finance/fiscal_localizations/saudi_arabia#sales-journals)
            * [Mode test](finance/fiscal_localizations/saudi_arabia#testing)
            * [Taxes](finance/fiscal_localizations/saudi_arabia#taxes)
          * [Mode production](finance/fiscal_localizations/saudi_arabia#production-mode)
      * Espagne
        * [Spanish chart of accounts](finance/fiscal_localizations/spain#spanish-chart-of-accounts)
        * [Spanish accounting reports](finance/fiscal_localizations/spain#spanish-accounting-reports)
      * Suisse
        * BVR (bulletin de versement avec numéro de référence)
          * [Référence BVR sur les factures](finance/fiscal_localizations/switzerland#isr-reference-on-invoices)
        * [Mise à jour du taux de change en direct](finance/fiscal_localizations/switzerland#currency-rate-live-update)
        * Mise à jour de la TVA à partir de janvier 2018
          * [Comment mettre à jour vos taxes dans Konvergo ERP Enterprise (Konvergo ERP Online ou On-premise) ?](finance/fiscal_localizations/switzerland#how-to-update-your-taxes-in-odoo-enterprise-odoo-online-or-on-premise)
      * Thaïlande
        * [Configuration](finance/fiscal_localizations/thailand#configuration)
        * [Plan comptable et taxes](finance/fiscal_localizations/thailand#chart-of-accounts-and-taxes)
        * Déclaration de TVA
          * [Rapport sur la taxe sur les ventes et les achats](finance/fiscal_localizations/thailand#sales-and-purchase-tax-report)
          * [Retenue à la source PND](finance/fiscal_localizations/thailand#withholding-pnd-tax-report)
        * Facture fiscale
          * [Paramétrage du numéro de siège social/de la filiale](finance/fiscal_localizations/thailand#headquarter-branch-number-settings)
      * Émirats arabes unis
        * [Installation](finance/fiscal_localizations/united_arab_emirates#installation)
        * [Plan comptable](finance/fiscal_localizations/united_arab_emirates#chart-of-accounts)
        * [Taxes](finance/fiscal_localizations/united_arab_emirates#taxes)
        * [Taux de change](finance/fiscal_localizations/united_arab_emirates#currency-exchange-rates)
        * Paie
          * [Règles salariales](finance/fiscal_localizations/united_arab_emirates#salary-rules)
          * [Provision de fin de service](finance/fiscal_localizations/united_arab_emirates#end-of-service-provision)
          * [Factures clients](finance/fiscal_localizations/united_arab_emirates#invoices)
      * Royaume-Uni
        * [Configuration](finance/fiscal_localizations/united_kingdom#configuration)
        * [Plan comptable](finance/fiscal_localizations/united_kingdom#chart-of-accounts)
        * Taxes
          * Making Tax Digital (MTD)
            * [Enregistrer votre entreprise auprès du HMRC avant la première soumission](finance/fiscal_localizations/united_kingdom#register-your-company-to-hmrc-before-the-first-submission)
            * [Soumission périodique au HMRC](finance/fiscal_localizations/united_kingdom#periodic-submission-to-hmrc)
            * [Soumission périodique au HMRC pour plusieurs sociétés](finance/fiscal_localizations/united_kingdom#periodic-submission-to-hmrc-for-multi-company)

  *[EDI]: échange de données informatisé

