# Ponto

**Ponto** est un service qui permet aux entreprises et aux professionnels de
regrouper leurs comptes en un seul endroit et de voir directement toutes leurs
transactions au sein d’une seule application. Il s’agit d’une solution tierce
qui augmente en permanence le nombre d’établissements bancaires pouvant être
synchronisés avec Odoo.

![Logo de la marque Ponto](../../../../../_images/ponto-logo.png)

**Odoo** peut être directement synchronisé avec votre banque pour importer
automatiquement tous les relevés bancaires dans votre base de données.

Ponto est un fournisseur tiers payant qui peut gérer la synchronisation entre
vos comptes bancaires et Odoo. [Son tarif est de 4€/mois par
compte/intégration](https://myponto.com/en#pricing).

Pour plus d'infos

  * [Synchronisation bancaire](../bank_synchronization.html)

  * [Transactions](../transactions.html)

## Configuration

### Lier ses comptes bancaires avec Ponto

  1. Allez au [site web de Ponto (https://myponto.com)](https://myponto.com).

  2. Créez un compte si vous n’en avez pas encore.

  3. Une fois que vous êtes connecté, créez une _organisation_.

![Remplissez le formulaire pour ajouter une entreprise dans
Ponto.](../../../../../_images/ponto-organization.png)

  4. Allez aux Comptes ‣ Live, et cliquez sur _Ajouter un compte_.

Il se peut que vous deviez d’abord ajouter vos **Informations de
facturation**.

  5. Sélectionnez votre pays, vos établissements bancaires, donnez votre consentement à Ponto et suivez les étapes à l’écran pour lier votre compte bancaire à votre compte Ponto.

![Ajoutez vos comptes bancaires à votre compte
Ponto.](../../../../../_images/ponto-add-account.png)

  6. Assurez-vous d’ajouter tous les comptes bancaires que vous souhaitez synchroniser avec votre base de données Odoo avant de passer aux étapes suivantes.

### Lier son compte Ponto à sa base de données Odoo

  1. Allez à Comptabilité ‣ Configuration ‣ Ajouter un compte bancaire.

  2. Recherchez votre établissement, assurez-vous de sélectionner le bon établissement. En le sélectionnant, vous pouvez vérifier que le fournisseur tiers est Ponto.

  3. Cliquez sur _Connecter_ et suivez les étapes.

  4. À un moment donné, vous devez autoriser les comptes auxquels vous souhaitez accéder dans Odoo. Veuillez sélectionner **tous les comptes** que vous souhaitez synchroniser, même ceux provenant d’autres établissements bancaires.

![Sélection des comptes que vous souhaitez synchroniser avec
Odoo.](../../../../../_images/ponto-select-accounts.png)

  5. Terminez le flux.

Note

Tous les comptes auxquels vous souhaitez accéder sur Odoo doivent être
autorisés, mais Odoo filtre les comptes en fonction de l’établissement
sélectionné à la deuxième étape.

### Mettre à jour ses identifiants de synchronisation

Il se peut que vous deviez mettre à jour vos identifiants Ponto ou modifier
les paramètres de synchronisation.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Synchronisation en ligne
et sélectionnez l’établissement dont vous souhaitez récupérer les autres
comptes. Cliquez sur le bouton _Récupérer les comptes_ pour lancer le flux.

Lors de la mise à jour, sélectionnez **tous les comptes** que vous souhaitez
synchroniser, même ceux provenant d’autres établissements bancaires.

### Récupérer de nouveaux comptes

Vous pouvez ajouter de nouveaux comptes en ligne à votre connexion.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Synchronisation en ligne
et sélectionnez l’établissement dont vous souhaitez récupérer les autres
comptes. Cliquez sur le bouton _Récupérer les comptes_ pour lancer le flux.

N’oubliez pas de conserver l’autorisation pour les comptes existants (pour
tous les établissements que vous avez synchronisés avec Ponto).

## FAQ

### Après ma synchronisation, aucun compte n’apparaît

Vous avez sélectionné un établissement dans la liste et vous n’avez autorisé
aucun compte de cet établissement.

### Une erreur survient indiquant que mon autorisation a expiré

Tous les **3 mois** (90 jours), vous devez autoriser à nouveau la connexion
entre votre compte bancaire et Ponto. Cela doit être fait à partir du [site
web de Ponto](https://myponto.com). Si vous ne le faites pas, la
synchronisation s’arrêtera pour ces comptes.

### J’ai des erreurs avec mon établissement bêta

Ponto met à disposition des établissements en _beta_ , ces établissements ne
sont pas directement pris en charge par Odoo et nous vous conseillons de
contacter directement Ponto.

Important

Utiliser un établissement en bêta est bénéfique pour Ponto, cela leur permet
d’avoir un réel retour d’expérience sur la connexion avec l’établissement.

