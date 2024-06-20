# Salt Edge

**Salt Edge** est un fournisseur tiers qui regroupe les informations bancaires
de vos comptes bancaires. Il prend en charge environ 5.000 établissements dans
plus de 50 pays.

![Logo Salt Edge](../../../../../_images/saltedge-logo.png)

Odoo peut être synchronisé directement avec votre banque pour que tous les
relevés bancaires soient automatiquement importés dans votre base de données.

Pour plus d'infos

  * [Synchronisation bancaire](../bank_synchronization.html)

  * [Transactions](../transactions.html)

## Configuration

### Lier ses comptes bancaires avec Odoo

  1. Lancez la synchronisation en cliquant sur Comptabilité ‣ Configuration ‣ Ajouter un compte bancaire.

  2. Sélectionnez l’établissement que vous souhaitez synchroniser. Vous pouvez voir si Salt Edge est le fournisseur tiers de l’établissement en le sélectionnant.

  3. Après avoir saisi votre numéro de téléphone, il vous est demandé de fournir une adresse email. Cette adresse email est utilisée pour créer votre compte Salt Edge. Veuillez vous assurer de saisir une adresse email valide, sinon vous ne pourrez pas accéder à votre compte Salt Edge.

![Adresse email à fournir à Salt Edge pour la création de votre
compte.](../../../../../_images/saltedge-contact-email.png)

  4. Après avoir saisi votre adresse email, vous êtes redirigé vers Salt Edge pour poursuivre le processus de synchronisation.

![Page de connexion de Salt Edge.](../../../../../_images/saltedge-login-
page.png)

  5. Assurez-vous de donner votre consentement en cochant la case de consentement.

![Page de consentement de Salt Edge.](../../../../../_images/saltedge-give-
consent.png)

  6. Terminez la synchronisation en suivant les étapes.

### Mettre à jour ses identifiants

Il se peut que vous deviez mettre à jour vos identifiants Salt Edge ou
modifier les paramètres de synchronisation.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Synchronisation en ligne
et sélectionnez l’établissement dont vous souhaitez mettre à jour les
identifiants. Cliquez sur le bouton _Mettre à jour les identifiants_ pour
lancer le flux et suivez les étapes.

N’oubliez pas de cocher la case de consentement. Sinon, il se peut qu’Odoo ne
puisse pas accéder à vos informations.

### Récupérer de nouveaux comptes

Vous pouvez ajouter de nouveaux comptes en ligne à votre connexion.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Synchronisation en ligne
et sélectionnez l’établissement pour récupérer les nouveaux comptes. Cliquez
sur le bouton _Récupérer les comptes_ pour lancer le flux et suivez les
étapes.

N’oubliez pas de cocher la case de consentement. Sinon, il se peut qu’Odoo ne
puisse pas accéder à vos informations.

## FAQ

### Une erreur survient lorsque j’essaye de supprimer ma synchronisation dans
Odoo

Odoo ne peut pas supprimer définitivement la connexion que vous avez créée
avec l’établissement bancaire. Cependant, il peut révoquer le consentement que
vous avez donné afin qu’Odoo ne puisse plus accéder à votre compte. L’erreur
que vous voyez est probablement un message vous indiquant que le consentement
a été révoqué, mais l’enregistrement n’a pas pu être supprimé, car il existe
toujours dans Salt Edge. Si vous souhaitez supprimer complètement la
connexion, veuillez vous connecter à votre [compte Salt
Edge](https://www.saltedge.com/dashboard) et supprimer manuellement votre
synchronisation. Une fois cela fait, vous pouvez revenir dans Odoo pour
supprimer l’enregistrement.

### Une erreur me dit que j’ai déjà synchronisé ce compte

Vous avez probablement déjà synchronisé votre compte bancaire avec Salt Edge,
veuillez vérifier sur votre [tableau de
bord](https://www.saltedge.com/dashboard) si vous n’avez pas déjà établi une
connexion avec les mêmes identifiants.

Si vous avez déjà une synchronisation avec les mêmes identifiants présents sur
votre tableau de bord Salt Edge et que cette synchronisation n’a pas été créée
avec Odoo, veuillez la supprimer et la créer à partir de votre base de données
Odoo.

Dans le cas où vous avez déjà une connexion avec les mêmes identifiants
présents sur votre tableau de bord Salt Edge et que cette synchronisation a
été créée avec Odoo, vous pourrez normalement la retrouver en allant à
Comptabilité ‣ Configuration ‣ Synchronisation en ligne. Veuillez vous assurer
de _Mettre à jour les identifiants_ pour réactiver la connexion.

