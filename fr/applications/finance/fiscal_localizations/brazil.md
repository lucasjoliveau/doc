# Brésil

## Introduction

Avec la localisation brésilienne, vous pouvez automatiquement les taxes de
vente sur les marchandises avec AvaTax (Avalara) par le biais d’appels d’API,
et également configurer les taxes pour les services.

Pour la partie calcul des taxes sur les marchandises, vous devez configurer
les contacts, la société, les produits, et créer un compte dans Avatax à part
des paramètres généraux d’Konvergo ERP.

Pour les taxes sur les services, vous pouvez les créer et les configurer
directement à partir d’Konvergo ERP sans les calculer avec AvaTax.

La localisation comprend également les taxes et un modèle de plan comptable
qui peut être modifié le cas échéant.

## Configuration

### Installation des modules

[Installez](../../general/apps_modules#general-install) les modules
suivants pour bénéficier de toutes les fonctionnalités de la localisation
brésilienne :

Nom | Nom technique | Description  
---|---|---  
**Brézil - Comptabilité** | `l10n_br` | Le [package de localisation fiscale](../fiscal_localizations#fiscal-localizations-packages) par défaut - ajoute des caractéristiques comptables pour la localisation brésilienne, qui représentent la configuration minimale requise pour qu’une société puisse opérer au Brésil. L’installation du module charge automatiquement : le plan comptable, les taxes et les champs requis pour correctement configurer le contact.  
**Brésil - Rapports comptables** | `l10n_br_reports` | Ajoute une déclaration de TVA simple qui permet de vérifier le montant de la taxe par groupe de taxe au cours d’une certaine période de temps. Ajoute également le compte de résultat et le bilan pour le marché brésilien.  
**Avatax Brazil** | `l10n_br_avatax` | Ajoute le calcul des taxes brésiliennes via Avatax et tous les champs nécessaires pour configurer Konvergo ERP afin d’utiliser correctement Avatax et d’envoyer les informations fiscales nécessaires pour récupérer les taxes correctes.  
**Avatax for SOs in Brazil** | `l10n_br_avatax_sale` | Identique au module `l10n_br_avatax` avec l’extension au module des commandes clients.  
  
### Configurer votre société

Pour configurer les informations de votre société, allez à l’application
Contacts et recherchez le nom donné à votre société.

  1. Sélectionnez l’option **Société** en haut de la page. Configurez ensuite les champs suivants :

     * **Nom**

     * **Adresse** (Ajoutez la **Ville** , l”**État** , le **Code postal** et le **Pays**)

     * Numéro d’identification fiscale (**CNPJ**)

     * **IE** (Enregistrement de l’État)

     * **IM** (Enregistrement de la municipalité)

     * **Code SUFRAMA** (Superintendence of the Manaus Free Trade Zone - À ajouter si d’application)

     * **Téléphone**

     * **Email**

![Configuration de la société.](../../../_images/company-configuration.png)

  2. Configurez les **informations fiscales** dans l’onglet **Ventes & Achats** :

     * Ajoutez la **Position fiscale** pour Avatax Brazil.

     * **Régime fiscal** (Régime fiscal fédéral)

     * **Type de contribuable ICMS** (indique le résumé ICMS, le statut d’exonération ou non-contribuable.)

     * **Secteur d’activité principal**

![Configuration fiscale de la société.](../../../_images/contact-fiscal-
configuration.png)

  3. Enfin, chargez un logo de la société et enregistrez le contact.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous avez un régime simplifié, vous devez configurer le taux ICMS dans Comptabilité ‣ Configuration ‣ Paramètres ‣ Taxes ‣ Avatax Brazil.</p>
</div>

### Configurer l’intégration d’AvaTax

Avalara AxaTax est un fournisseur de calcul de taxes qui peut être intégré
dans Konvergo ERP pour calculer automatiquement les taxes en prenant en compte la
société, le contact (le client), le produit et les informations de transaction
pour récupérer la taxe correcte à utiliser.

Konvergo ERP est un partenaire certifié d’Avalara Brésil, ce qui signifie que les
experts d’Avalara ont examiné les flux de travail couverts par le champ
d’application de l’intégration.

Using this integration requires [In-App-Purchases
(IAPs)](../../essentials/in_app_purchase) to compute taxes. Every time
you compute taxes, an API call is made, using credits from your IAP credits
balance.

#### Configuration des identifiants

Pour activer AvaTax dans Konvergo ERP, vous devez créer un compte. Pour ce faire,
allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Taxes, et dans la section
**AvaTax Brazil** , ajoutez l’adresse email que vous voulez utiliser pour vous
connecter au portail AvaTax et cliquez sur **Créer un compte**. Cet email est
utilisé comme adresse email de l’administrateur dans AvaTax.

Après avoir créé le compte dans Konvergo ERP, vous devez accéder au portail d’Avalara
pour configurer votre mot de passe :

  1. Accédez au [portail Avalara](https://portal.avalarabrasil.com.br/Login)

  2. Cliquez sur **Meu primeiro acesso**

  3. Ajoutez l’adresse email que vous avez utilisée dans Konvergo ERP pour créer le compte Avalara/Avatax et cliquez ensuite sur **Solicitar Senha**

  4. Vous recevrez un email avec un jeton et un lien pour créer votre mot de passe. Cliquez sur ce lien et copiez-collez le jeton pour attribuer le mot de passe souhaité.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous envisagez de d’abord tester l’intégration sur une base de données de test ou sandbox, il est recommandé d’utiliser une autre adresse email, puisque vous ne pourrez plus réutiliser la même adresse email sur votre base de données de production.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Vous pouvez utiliser AvaTax dans Konvergo ERP sans créer de mot de passe et sans accéder au portail Avalara ; pour Konvergo ERP, la seule exigence pour commencer à utiliser le moteur de calcul fiscal d’Avalara est de créer un compte à partir de la page des paramètres.</p>
</div> ![Configuration du compte
Avatax.](../../../_images/avatax-account-configuration.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez transférer les identifiants API. N’utilisez cette option que si vous avez déjà créé un compte dans une autre instance Konvergo ERP et que vous souhaitez le réutiliser.</p>
</div>

### Configurer les données de base

#### Plan comptable

Le [plan comptable](../accounting/get_started/chart_of_accounts) est
installé par défaut dans l’ensemble des données du module de localisation. Les
comptes sont mappés automatiquement dans leurs taxes correspondantes et les
champs Compte fournisseur par défaut et Compte client par défaut.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Le plan comptable pour le Brésil est basé sur le SPED CoA, qui donne une base de référence des comptes nécessaires au Brésil.</p>
<p>Vous pouvez ajouter ou supprimer des comptes selon les besoins de l’entreprise.</p>
</div>

#### Taxes

Les taxes sont automatiquement créées lors de l’installation de la
localisation brésilienne. Les taxes sont déjà configurées et certaines d’entre
elles sont utilisées par Avalara lors du calcul des taxes sur la commande ou
la facture.

Il est possible de modifier les taxes ou d’en ajouter d’autres. Par exemple,
certaines taxes utilisées pour les services doivent être ajoutées et
configurées manuellement, car le taux peut varier en fonction de la ville où
vous offrez le service.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les taxes sur les services ne sont pas calculées par AvaTax. Seules les taxes sur les marchandises sont calculées.</p>
</div>

Lorsque vous configurez une taxe utilisée pour un service qui est inclus dans
le prix final (lorsque la taxe n’est pas ajoutée ou soustraite en plus du prix
du produit), définissez le **Calcul de la taxe** sur **Pourcentage du prix
toutes taxes comprises** et dans l’onglet **Options avancées** , cochez
l’option **Inclus dans le prix**.

Pour plus d’informations sur la configuration des taxes afin de mieux répondre
à vos besoins, consultez la [documentation fonctionnelle relative aux
taxes](../accounting/taxes).

![Configuration des taxes.](../../../_images/tax-configuration.png)
<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Ne supprimez pas les taxes, car elles sont utilisées dans le calcul de la taxe par AvaTax. Si vous les supprimez, Konvergo ERP les crée à nouveau lorsqu’elles sont utilisées dans une commande client ou dans une facture et qu’elles calculent les taxes avec AvaTax, mais le compte utilisé pour enregistrer les taxes doit être reconfiguré dans l’onglet <b>Définition</b> de la taxe, dans les sections <b>Répartition pour les factures</b> et <b>Répartition pour les remboursements</b>.</p>
</div>

#### Produits

Pour utiliser l’intégration d’AvaTax sur les commandes clients et les
factures, précisez d’abord les informations suivantes sur le produit :

  * **Code CEST** (Code des produits soumis à la substitution fiscale de l’ICMS)

  * **Code NCM Mercosul** (Code produit de la Nomenclature Commune du Mercosur)

  * **Source d’origine** (Indique l’origine du produit, qui peut être étrangère ou nationale, parmi d’autres options possibles en fonction du cas d’utilisation spécifique)

  * **Type de produit fiscal SPED** (Type de produit fiscal selon le tableau de la liste SPED)

  * **Finalité de l’utilisation** (Précisez l’utilisation prévue de ce produit)

![Configuration du produit.](../../../_images/product-configuration.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Konvergo ERP crée automatiquement trois produits à utiliser pour les frais de transport associés aux ventes. Ils s’intitulent <code>Fret</code>, <code>Assurance</code>, et <code>Autres coûts</code>. Ils sont déjà configurés. Si vous devez en créer d’autres, dupliquez-les et utilisez la même configuration (configuration nécessaire : <b>Type de produit</b> <code>Service</code>, <b>Type de coût de transport</b> <code>Assurance</code>, <code>Fret</code>, ou <code>Autres coûts</code>)</p>
</div>

#### Contacts

Avant d’utiliser l’intégration, précisez les informations suivantes sur le
contact :

  1. Informations générales relatives au contact :

     * Cochez l’option **Société** pour un contact avec un numéro d’identification fiscale (CNPJ), ou cochez **Particulier** pour un contact avec un CPF.

     * **Nom**

     * **Adresse** : le **code postal** est un champ requis pour calculer les taxes correctement.

     * **Numéro d’identification fiscale** ou **CPF** : Utilisez CPF pour les particuliers et le numéro d’identification fiscale (CNPJ) pour les sociétés.

     * **IE** : numéro d’identification fiscale de l’État

     * **IM** : numéro d’identification fiscale de la municipalité

     * **Code SUFRAMA** : Numéro d’enregistrement SUFRAMA

     * **Téléphone**

     * **Email**

![Configuration du contact.](../../../_images/contact-configuration.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les champs <b>CPF</b>, <b>IE</b>, <b>IM</b>, et <b>Code SUFRAMA</b> sont masqués jusqu’à ce que le <b>Pays</b> soit défini sur <code>Brésil</code>.</p>
</div>

  2. Informations fiscales relatives au contact dans l’onglet **Ventes & Achats** :

     * **Position fiscale** : ajoutez la position fiscale AvaTax pour automatiquement calculer les taxes sur les commandes clients et les factures.

     * **Régime fiscal** : régime fiscal fédéral

     * **Type de contribuable ICMS** : le type de contribuable détermine si le contact est soumis au régime ICMS, s’il est exonéré ou s’il n’est pas contribuable.

     * **Secteur d’activité principal** : liste des secteurs d’activité principaux du contact

![Configuration fiscale du contact.](../../../_images/contact-fiscal-
configuration.png)

#### Positions fiscales

Pour calculer les taxes sur les commandes clients ou les factures, il est
nécessaire d’avoir une **Position fiscale** et d’activer les options
**Détecter automatiquement** et **Utiliser l’API AvaTax**.

La **Position fiscale** peut être configurée sur le contact ou sélectionnée
lors de la création d’une commande client ou d’une facture.

![Configuration de la position fiscale](../../../_images/fiscal-position-
configuration.png)

## Flux de travail

Cette section fournit une vue d’ensemble des actions qui déclenchent des
appels d’API pour le calcul des taxes.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Veuillez noter que chaque appel d’API entraîne un coût. Soyez attentif aux actions qui déclenchent ces appels afin de gérer les coûts de manière efficace.</p>
</div>

### Calculs des taxes sur les devis / commandes clients

Déclenchez un appel d’API pour calculer automatiquement les taxes sur un devis
ou une commande client avec AvaTax de l’une des manières suivantes :

  * **Confirmation du devis**
    

Confirmez un devis en commande client.

  * **Déclencheur manuel**
    

Cliquez sur **Calculer les taxes avec Avatax**.

  * **Aperçu**
    

Cliquez sur le bouton **Aperçu**.

  * **Envoyer un devis / commande client par email**
    

Envoyez un devis ou une commande client à un client par email.

  * **Accès aux devis en ligne**
    

Lorsqu’un client accède aux devis en ligne (par la vue portail), l’appel d’API
est déclenché.

### Calculs des taxes sur les factures

Déclenchez un appel d’API pour calculer automatiquement les taxes sur une
facture client avec AvaTax de l’une des manières suivantes :

  * **Déclencheur manuel**
    

Cliquez sur **Calculer les taxes avec AvaTax**.

  * **Aperçu**
    

Cliquez sur le bouton **Aperçu**.

  * **Accès aux factures en ligne**
    

Lorsqu’un client accède à la facture en ligne (par la vue portail), l’appel
d’API est déclenché.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous envisagez de d’abord tester l’intégration sur une base de données de test ou sandbox, il est recommandé d’utiliser une autre adresse email, puisque vous ne pourrez plus réutiliser la même adresse email sur votre base de données de production.</p>
</div>0 <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous envisagez de d’abord tester l’intégration sur une base de données de test ou sandbox, il est recommandé d’utiliser une autre adresse email, puisque vous ne pourrez plus réutiliser la même adresse email sur votre base de données de production.</p>
</div>1

  *[IAP]: In-app-purchase

