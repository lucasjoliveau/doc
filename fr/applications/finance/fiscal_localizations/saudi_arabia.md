# Arabie saoudite

## Configuration

[Installez](../../general/apps_modules#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
saoudienne.

Nom | Nom technique | Description  
---|---|---  
Arabie saoudite - Comptabilité | `l10n_sa` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut  
Arabie saoudite - Facturation électronique | `l10n_sa_edi` | Implémentation de la facturation électronique de la ZATCA  
Arabie saoudite - Facturation électronique (simplifiée) | `l10n_sa_edi_simplified` | Implémentation de la facturation électronique simplifiée de la ZATCA (Point de Vente)  
Arabie saoudite - Point de vente | `l10n_sa_pos` | Conformité Point de Vente  
  
## Facturation électronique ZATCA

Le système de facturation électronique ZATCA est conçu pour rationaliser et
numériser le processus de facturation des entreprises opérant en Arabie
Saoudite.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Pages/default.aspx">Page sur la facturation électronique ZATCA</a></p>
</div>

### Informations relatives à l’entreprise

Allez aux Paramètres ‣ Paramètres généraux ‣ Sociétés, cliquez sur **Mettre à
jour les informations** et assurez-vous que les informations suivantes sont
complètes et à jour.

  * Le **Nom complet de la société**.

  * Tous les champs d”**Adresse** pertinents, y compris le **Numéro de bâtiment** et l”**Identification de la parcelle** (quatre chiffres chacun).

  * Sélectionnez un **Système d’identification** de l’entreprise. Il est recommandé d’utiliser le **Numéro d’enregistrement commercial**.

  * Saisissez le **Numéro d’identification** pour le **Système d’identification** sélectionné.

  * Le numéro de **TVA**.

  * Assurez-vous que la **Devise** est définie sur **SAR**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous devez également compléter ces informations pour les entreprises partenaires.</p>
</div>

### Mode simulation

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Il est fortement recommandé de tester soigneusement tous les flux de facturation en utilisant d’abord le portail de <b>simulation</b> Fatoora, car <b>toute</b> facture soumise au portail normal de Fatoora sera comptabilisée, ce qui pourrait entraîner des amendes et des pénalités.</p>
</div>

#### Portail de simulation de Fatoora

Connectez-vous au [portail Fatoora](https://fatoora.zatca.gov.sa/) en
utilisant les identifiants ZATCA de la société. Ensuite, cliquez sur le bouton
**Portail de simulation Fatoora** pour basculer vers le portail de simulation.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf">ZACTA Fatoora portal user manual version 3 (May 2023)</a></p>
</div>

#### Intégration de l’API ZATCA

Dans Konvergo ERP, allez à Comptabilité ‣ Configuration ‣ Paramètres. Sous
**Intégration de l’API ZATCA** , sélectionnez le **mode API** **Simulation
(Préproduction)** et cliquez sur **Enregistrer**.

#### Journaux de vente

Chaque journal de vente dans Konvergo ERP doit être configuré. Pour ce faire, allez à
Comptabilité ‣ Configuration ‣ Journaux, ouvrez n’importe quel journal de
vente (par ex. Factures clients) et allez à l’onglet **ZATCA**. Saisissez
ensuite un **Numéro de série** pour identifier le journal.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez utiliser le même numéro de série pour tous les journaux de vente de la société.</p>
</div>

Cliquez ensuite sur **Intégrer le journal**. Dans la boîte de dialogue, vous
devez fournir un code OTP. Pour le récupérer, ouvrez le [portail de simulation
Fatoora](https://fatoora.zatca.gov.sa/), cliquez sur **Onboard New Solution
Unit/Device** , choisissez le nombre de codes OTP à générer (un par journal à
configurer) et cliquez sur **Générer un code OTP**. Copiez un code OTP,
collez-le dans la boîte de dialogue dans Konvergo ERP et cliquez sur **Demander**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les codes OTP expirent après une heure.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si un problème survient pendant l’intégration, cliquez sur <b>Regénérer CSR</b> pour recommencer.</p>
</div>

#### Mode test

Lors de la confirmation d’une facture, il existe désormais une option de
traiter la facture, de l’envoyer directement au portail de simulation Fatoora.
Konvergo ERP affiche la réponse du portail après chaque soumission. Seules les
factures rejetées peuvent être remises en brouillon et éditées sur Konvergo ERP. De
plus, à la fin de chaque journée, Konvergo ERP envoie toutes les factures non traitées
au portail.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>Il est recommandé de tester tous les flux de facturation, de préférence avec des factures réelles et pendant une durée raisonnable.</p></li>
<li><p>Comparez la page des statistiques des factures reçues sur le portail de simulation Fatoora avec la liste des factures sur Konvergo ERP pour vous assurer que les deux sont alignées.</p></li>
</ul>
</div>

#### Taxes

Lorsque vous utilisez une **taxe 0%** sur une facture client, vous devez
préciser la raison d’un tel taux. Pour configurer des taxes, allez à
Comptabilité ‣ Configuration ‣ Paramètres ‣ Taxes, et ouvrez la taxe à
modifier. Dans l’onglet **Options avancées** , sélectionnez un **Code de motif
d’exonération** et cliquez sur **Enregistrer**.

Lors de l’utilisation de la **rétention** ou de la **retenue d’un montant**
dans une facture client, la taxe utilisée pour retenir le montant doit être
précisée.

### Mode production

Lorsque vous êtes prêt pour la production, changez le mode de l’API en
**Production** et cliquez sur **Enregistrer**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Le passage du <b>mode de l’API</b> en <b>Production</b> est <b>irréversible</b>.</p>
</div>

Les journaux de vente initialement liés au portail de simulation doivent
désormais être liés au portail normal. Pour ce faire, répétez l’étape Intégrer
les journaux en veillant à utiliser le [portail normal de
Fatoora](https://fatoora.zatca.gov.sa/) cette fois-ci.

  *[OTP]: mot de passe unique

