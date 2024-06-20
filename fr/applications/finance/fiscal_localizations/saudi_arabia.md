# Arabie saoudite

## Configuration

[Installez](../../general/apps_modules.html#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
saoudienne.

Nom | Nom technique | Description  
---|---|---  
Arabie saoudite - Comptabilité | `l10n_sa` | Le [package de localisation fiscale](../fiscal_localizations.html#fiscal-localizations-packages) par défaut  
Arabie saoudite - Facturation électronique | `l10n_sa_edi` | Implémentation de la facturation électronique de la ZATCA  
Arabie saoudite - Facturation électronique (simplifiée) | `l10n_sa_edi_simplified` | Implémentation de la facturation électronique simplifiée de la ZATCA (Point de Vente)  
Arabie saoudite - Point de vente | `l10n_sa_pos` | Conformité Point de Vente  
  
## Facturation électronique ZATCA

Le système de facturation électronique ZATCA est conçu pour rationaliser et
numériser le processus de facturation des entreprises opérant en Arabie
Saoudite.

Pour plus d'infos

[Page sur la facturation électronique
ZATCA](https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx)

### Informations relatives à l’entreprise

Allez aux Paramètres ‣ Paramètres généraux ‣ Sociétés, cliquez sur Mettre à
jour les informations et assurez-vous que les informations suivantes sont
complètes et à jour.

  * Le Nom complet de la société.

  * Tous les champs d”Adresse pertinents, y compris le Numéro de bâtiment et l”Identification de la parcelle (quatre chiffres chacun).

  * Sélectionnez un Système d’identification de l’entreprise. Il est recommandé d’utiliser le Numéro d’enregistrement commercial.

  * Saisissez le Numéro d’identification pour le Système d’identification sélectionné.

  * Le numéro de TVA.

  * Assurez-vous que la Devise est définie sur SAR.

Note

Vous devez également compléter ces informations pour les entreprises
partenaires.

### Mode simulation

Important

Il est fortement recommandé de tester soigneusement tous les flux de
facturation en utilisant d’abord le portail de **simulation** Fatoora, car
**toute** facture soumise au portail normal de Fatoora sera comptabilisée, ce
qui pourrait entraîner des amendes et des pénalités.

#### Portail de simulation de Fatoora

Connectez-vous au [portail Fatoora](https://fatoora.zatca.gov.sa/) en
utilisant les identifiants ZATCA de la société. Ensuite, cliquez sur le bouton
Portail de simulation Fatoora pour basculer vers le portail de simulation.

Pour plus d'infos

[ZACTA Fatoora portal user manual version 3 (May
2023)](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf)

#### Intégration de l’API ZATCA

Dans Odoo, allez à Comptabilité ‣ Configuration ‣ Paramètres. Sous Intégration
de l’API ZATCA, sélectionnez le mode API Simulation (Préproduction) et cliquez
sur Enregistrer.

#### Journaux de vente

Chaque journal de vente dans Odoo doit être configuré. Pour ce faire, allez à
Comptabilité ‣ Configuration ‣ Journaux, ouvrez n’importe quel journal de
vente (par ex. Factures clients) et allez à l’onglet ZATCA. Saisissez ensuite
un Numéro de série pour identifier le journal.

Note

Vous pouvez utiliser le même numéro de série pour tous les journaux de vente
de la société.

Cliquez ensuite sur Intégrer le journal. Dans la boîte de dialogue, vous devez
fournir un code OTP. Pour le récupérer, ouvrez le [portail de simulation
Fatoora](https://fatoora.zatca.gov.sa/), cliquez sur Onboard New Solution
Unit/Device, choisissez le nombre de codes OTP à générer (un par journal à
configurer) et cliquez sur Générer un code OTP. Copiez un code OTP, collez-le
dans la boîte de dialogue dans Odoo et cliquez sur Demander.

Note

Les codes OTP expirent après une heure.

Astuce

Si un problème survient pendant l’intégration, cliquez sur Regénérer CSR pour
recommencer.

#### Mode test

Lors de la confirmation d’une facture, il existe désormais une option de
traiter la facture, de l’envoyer directement au portail de simulation Fatoora.
Odoo affiche la réponse du portail après chaque soumission. Seules les
factures rejetées peuvent être remises en brouillon et éditées sur Odoo. De
plus, à la fin de chaque journée, Odoo envoie toutes les factures non traitées
au portail.

Astuce

  * Il est recommandé de tester tous les flux de facturation, de préférence avec des factures réelles et pendant une durée raisonnable.

  * Comparez la page des statistiques des factures reçues sur le portail de simulation Fatoora avec la liste des factures sur Odoo pour vous assurer que les deux sont alignées.

#### Taxes

Lorsque vous utilisez une **taxe 0%** sur une facture client, vous devez
préciser la raison d’un tel taux. Pour configurer des taxes, allez à
Comptabilité ‣ Configuration ‣ Paramètres ‣ Taxes, et ouvrez la taxe à
modifier. Dans l’onglet Options avancées, sélectionnez un Code de motif
d’exonération et cliquez sur Enregistrer.

Lors de l’utilisation de la **rétention** ou de la **retenue d’un montant**
dans une facture client, la taxe utilisée pour retenir le montant doit être
précisée.

### Mode production

Lorsque vous êtes prêt pour la production, changez le mode de l’API en
Production et cliquez sur Enregistrer.

Avertissement

Le passage du mode de l’API en Production est **irréversible**.

Les journaux de vente initialement liés au portail de simulation doivent
désormais être liés au portail normal. Pour ce faire, répétez l’étape Intégrer
les journaux en veillant à utiliser le [portail normal de
Fatoora](https://fatoora.zatca.gov.sa/) cette fois-ci.

  *[OTP]: mot de passe unique

