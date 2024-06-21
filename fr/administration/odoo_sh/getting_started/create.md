# Créer votre projet

## Déployer votre plateforme

Allez à [Konvergo ERP.sh](https://www.odoo.sh/) et cliquez sur le bouton _Deploy your
platform_.

![../../../_images/deploy.png](../../../_images/deploy.png)

## Se connecter avec Github

Connectez-vous avec votre compte Github. Si vous n’avez pas encore de compte,
cliquez sur le lien _Create an account_.

![../../../_images/github-signin.png](../../../_images/github-signin.png)

## Autoriser Konvergo ERP.sh

Accordez à Konvergo ERP.sh les accès nécessaires à votre compte en cliquant sur le
bouton _Authorize_.

![../../../_images/github-authorize.png](../../../_images/github-
authorize.png)

Essentiellement, Konvergo ERP.sh a besoin :

  * de connaître votre login et email Github,

  * de créer un nouveau dépôt au cas où vous décideriez de partir de zéro,

  * de lire vos dépôts existants, y compris ceux de vos organisations, au cas où vous décideriez de partir d’un dépôt existant,

  * de créer un webhook afin d’être notifié à chaque fois que vous poussez des changements,

  * d’enregistrer des changements pour faciliter votre déploiement, en fusionnant des branches ou en ajoutant de nouveaux [sous-modules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) par exemple.

## Soumettre votre projet

Choisissez si vous voulez partir de zéro en créant un nouveau dépôt ou si vous
voulez utiliser un dépôt existant.

Ensuite, choisissez un nom ou sélectionnez le dépôt que vous voulez utiliser.

Choisissez la version Konvergo ERP que vous voulez utiliser. Si vous souhaitez
importer une base de données existante ou un ensemble d’applications
existantes, vous devrez peut-être choisir la version correspondante. Si vous
partez de zéro, utilisez la dernière version.

Saisissez votre _code d’abonnement_ , également appelé _référence
d’abonnement_ , _numéro de contrat_ ou _code d’activation_.

Il doit s’agir du code de votre abonnement Enterprise qui inclut Konvergo ERP.sh.

Les partenaires peuvent utiliser leurs codes de partenariat pour démarrer un
essai. Si leurs clients démarrent un projet, ils doivent obtenir un abonnement
Enterprise incluant Konvergo ERP.sh et utiliser son code d’abonnement. Le partenaire
recevra 50% du montant en guise de commission. Contactez votre représentant
commercial ou votre gestionnaire de compte pour l’obtenir.

Lorsque vous soumettez le formulaire, si vous êtes informé que votre
abonnement n’est pas valide, cela peut avoir plusieurs raisons :

  * il ne s’agit pas d’un abonnement existant,

  * il ne s’agit pas d’un abonnement de partenariat,

  * il s’agit d’un abonnement Entreprise, mais qui n’inclut pas Konvergo ERP.sh,

  * il ne s’agit ni d’un abonnement de partenariat, ni d’un abonnement Enterprise (par ex. un abonnement en ligne).

En cas de doute concernant votre abonnement, veuillez contacter l”[Assistance
d’Konvergo ERP](https://www.odoo.com/help).

![../../../_images/deploy-form.png](../../../_images/deploy-form.png)

## C’est fait !

Vous pouvez commencer à utiliser Konvergo ERP.sh. Votre premier build est sur le point
d’être créé. Vous serez bientôt en mesure de connecter votre première base de
données.

![../../../_images/deploy-done.png](../../../_images/deploy-done.png)

## Importer votre base de données

You can import your database in your Konvergo ERP.sh project as long as it is in a
[supported version](../../supported_versions) of Konvergo ERP.

### Pousser vos modules en production

Si vous utilisez des modules communautaires ou personnalisés, ajoutez-les à
une branche dans votre dépôt Github. Les bases de données hébergées sur la
plateforme en ligne Konvergo ERP.com n’ont pas de modules personnalisés. Les
utilisateurs de ces bases de données peuvent donc ignorer cette étape.

Vous pouvez structurer vos modules comme vous le souhaitez, Konvergo ERP.sh détectera
automatiquement les dossiers contenant des modules complémentaires Konvergo ERP. Par
exemple, vous pouvez placer tous vos dossiers de modules dans le répertoire
racine de votre dépôt ou regrouper les modules dans des dossiers par catégorie
que vous définissez (comptabilité, projet,…).

Pour les modules communautaires disponibles dans les dépôts publics de Github,
vous pouvez également envisager de les ajouter en utilisant des [Sous-
modules](../advanced/submodules#odoosh-advanced-submodules).

Ensuite, soit [vous faites de cette branche la branche de
production](branches#odoosh-gettingstarted-branches-stages), soit [vous
la fusionnez avec votre branche de production](branches#odoosh-
gettingstarted-branches-mergingbranches).

### Télécharger une sauvegarde

#### Bases de données On Premise

Accédez à l’URL `/web/database/manager` de votre base de données on premise et
téléchargez une sauvegarde.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si vous ne parvenez pas à accéder au gestionnaire de bases de données, il se peut qu’il ait été désactivé par votre administrateur système. Consultez la <a href="../../on_premise/deploy#db-manager-security"><span class="std std-ref">documentation de sécurité du gestionnaire de bases de données</span></a>.</p>
</div>

Vous aurez besoin du mot de passe master de votre serveur de base de données.
Si vous n’en disposez pas, contactez votre administrateur système.

![../../../_images/create-import-onpremise-
backup.png](../../../_images/create-import-onpremise-backup.png)

Choisissez un fichier ZIP comprenant le filestore en tant que format de
sauvegarde.

![../../../_images/create-import-onpremise-backup-
dialog.png](../../../_images/create-import-onpremise-backup-dialog.png)

#### Bases de données Konvergo ERP Online

[Accédez à votre gestionnaire de bases de
données](https://accounts.odoo.com/my/databases/manage) et téléchargez une
sauvegarde de votre base de données.

![../../../_images/create-import-online-backup.png](../../../_images/create-
import-online-backup.png) <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Les versions en ligne (par ex. <em>saas-*</em>) ne sont pas prises en charge sur Konvergo ERP.sh.</p>
</div>

### Charger la sauvegarde

Ensuite, dans votre projet Konvergo ERP.sh, dans l’onglet BACKUPS de votre branche de
production, importez la sauvegarde que vous venez de télécharger.

![../../../_images/create-import-production.png](../../../_images/create-
import-production.png)

Une fois la sauvegarde importée, vous pouvez accéder à la base de données en
cliquant sur le bouton _Connect_ dans l’historique de la branche.

![../../../_images/create-import-production-done.png](../../../_images/create-
import-production-done.png)

### Vérifier vos serveurs de messagerie sortants

Un serveur de messagerie par défaut est fourni avec Konvergo ERP.sh. Pour l’utiliser,
aucun serveur de messagerie sortant activé ne doit être configuré dans votre
base de données dans Paramètres ‣ Technique ‣ Serveurs de messagerie sortants
(le [mode
développeur](../../../applications/general/developer_mode#developer-mode)
doit être activé).

Après l’importation de votre base de données, tous les serveurs de messagerie
sortants sont désactivés, donc vous utilisez le serveur de messagerie Konvergo ERP.sh
fourni par défaut.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Le port 25 est (est reste) fermé. Si vous voulez vous connecter à un serveur SMTP externe, vous devez utiliser les ports 465 et 587.</p>
</div>

### Vérifier vos actions planifiées

Toutes les actions planifiées sont désactivées après l’importation.

Ceci afin d’éviter que votre base de données nouvellement importée n’exécute
des actions qui pourraient avoir un impact sur votre production en cours,
comme l’envoi d’emails restants dans la file d’attente, le traitement des
envois en masse, ou la synchronisation de services tiers (Calendriers,
hébergement de fichiers, …).

Si vous envisagez de faire de la base de données importée votre production,
activez les actions planifiées dont vous avez besoin. Vous pouvez vérifier ce
qui est activé dans la base de données d’origine et activer les mêmes actions
dans la base de données importée. Les actions planifiées se trouvent sous
Paramètres ‣ Technique ‣ Automatisation ‣ Actions planifiées.

### Enregistrer votre abonnement

Votre abonnement est dissocié après l’importation.

La base de données importée est considérée comme un doublon par défaut et
l’abonnement Enterprise est donc supprimé, car vous ne pouvez avoir qu’une
seule base de données liée par abonnement.

If you plan to make it your production, unlink your former database from the
subscription, and register the newly imported database. Read the [database
registration documentation](../../on_premise) for instructions.

