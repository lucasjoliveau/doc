# Documents

**Odoo Documents** vous permet de stocker, d’afficher et de gérer des fichiers
dans Odoo.

Vous pouvez charger n’importe quel type de fichier (max. 64MB par fichier sur
Odoo Online) et les organiser dans différents espaces de travail.

Pour plus d'infos

  * [Odoo Documents : page produit](https://www.odoo.com/app/documents)

  * [Tutoriels Odoo : Les bases de Documents](https://www.odoo.com/slides/slide/documents-basics-674)

  * [Tutoriels Odoo : Utiliser Documents avec votre application Comptabilité](https://www.odoo.com/slides/slide/using-documents-with-your-accounting-app-675?fullscreen=1#)

## Configuration

En allant à Documents ‣ Configuration ‣ Paramètres, vous pouvez activer la
centralisation des fichiers associés à un domaine spécifique de votre
activité. Par exemple, en cochant Ressources humaines, vos documents RH sont
automatiquement disponibles dans l’espace de travail RH, alors que les
documents liés à la Paie sont automatiquement disponibles dans l’espace de
travail sous-jacent Paie. Vous pouvez modifier l’espace de travail par défaut
en utilisant le menu déroulant et modifier ses propriétés en cliquant sur le
bouton de lien interne (➔).

![Activez la centralisation des fichiers associés à un domaine spécifique de
votre activité.](../../_images/files-centralization.png)

Note

  * Si vous activez la centralisation de vos fichiers et documents comptables, il est nécessaire de cliquer sur Journaux et de définir chaque journal indépendamment pour permettre la synchronisation automatique.

![Activez la centralisation des fichiers associés à votre
comptabilité.](../../_images/accounting-files-centralization.png)

  * Si vous sélectionnez un nouvel espace de travail, les documents existants ne sont pas déplacés. Seuls les documents nouvellement créés se retrouveront dans le nouvel espace de travail.

## Espaces de travail

Les espaces de travail sont des dossiers hiérarchiques qui ont leur propre
ensemble d’étiquettes et d’actions. Il existe des espaces de travail par
défaut, mais vous pouvez créer votre propre espace de travail en allant à
Documents ‣ Configuration ‣ Espaces de travail et en cliquant sur Créer.

Note

Les Espaces de travail et les Espaces de travail sous-jacents peuvent être
créés, modifiés ou supprimés en cliquant sur l’icône d’engrenage ⚙ dans le
menu de gauche.

![Créez des espaces de travail sous-jacents à partir du menu de
gauche](../../_images/sub-workspaces-creation.png)

## Étiquettes

Les étiquettes sont utilisées dans les espaces de travail pour ajouter un
niveau de différenciation entre les documents. Elles sont organisées par
catégorie et vous pouvez utiliser des filtres pour les trier.

Note

  * Les étiquettes d’un espace de travail parent s’appliquent automatiquement aux espaces de travail enfants.

  * Les étiquettes peuvent être créés et modifiés en allant à Configuration ‣ Étiquettes.

  * Les étiquettes peuvent également être créées, modifiées ou supprimées en cliquant sur l’icône d’engrenage ⚙ dans le menu de gauche.

## Gestion des documents

Lorsque vous cliquez sur un document spécifique, le panneau de droite affiche
différentes options. En haut, des options supplémentaires peuvent être
disponibles : Télécharger, Partager, Remplacer, Verrouiller ou Diviser. Vous
pouvez aussi Ouvrir le chatter ou Archiver le document.

![Options du panneau de droite](../../_images/right-panel-options.png)

Ensuite, vous pouvez modifier le nom de votre fichier en cliquant sur
Document. Vous pouvez assigner un Contact ou un Propriétaire. L”Espace de
travail associé peut être modifié et il est possible d’accéder à la Pièce
comptable associée ou d’ajouter des Étiquettes.

Note

  * Le Contact est la personne liée au document et assignée à celui-ci. Il peut uniquement visualiser le document, sans possibilité de le modifier. Par exemple, un fournisseur existant dans votre base de données est le contact pour sa facture.

  * La personne qui crée un document est, par défaut, son Propriétaire et a tous les droits sur le document. Il est possible de remplacer le propriétaire d’un document. Par exemple, un employé doit être propriétaire d’un document pour pouvoir le voir dans « Mon profil ».

Enfin, différentes Actions sont disponibles en bas du panneau de droite, en
fonction de l’espace de travail dans lequel votre document est stocké.

## Actions de flux de travail

Les actions de flux de travail vous aident à rationaliser la gestion de vos
documents et de vos opérations commerciales en général. Il s’agit d’action
automatisées qui peuvent être créées et personnalisées pour chaque espace de
travail. Par exemple, créer des documents, traiter des factures, signer,
organiser des fichiers, ajouter des étiquettes à un fichier ou le déplacer
vers un autre espace de travail en un seul clic, etc. Ces actions de flux de
travail apparaissent dans le panneau de droite lorsqu’elles répondent aux
critères que vous avez définis.

### Créer des actions de flux de travail

Pour créer des actions de flux de travail, allez à Documents ‣ Configuration ‣
Actions et cliquez sur Créer.

Note

Une action s’applique à tous les Espaces de travail enfants sous l”Espace de
travail parent que vous avez sélectionné.

### Définir les conditions

Vous pouvez Créer une nouvelle Action ou modifier une action existante. Vous
pouvez définir le Nom de l’action et définir les conditions qui déclenchent
l’apparition du bouton d’action (▶) sur le panneau de droite lors de la
sélection d’un fichier.

Vous pouvez définir trois types de conditions de base :

  1. Étiquettes : vous pouvez à la fois utiliser les conditions Contient et Ne contient pas, ce qui signifie que les fichiers _doivent avoir_ ou _ne doivent ne pas avoir_ les étiquettes définies ici.

  2. Contact : les fichiers doivent être associés au contact défini ici.

  3. Propriétaire : les fichiers doivent être associés au propriétaire défini ici.

![Exemple d'une condition de base d'une action de flux de travail dans Odoo
Documents](../../_images/basic-condition-example.png)

Astuce

Si vous ne définissez aucune condition, le bouton d’action apparaît pour tous
les fichiers qui se trouvent dans l’espace de travail sélectionné.

#### Type de condition avancée : domaine

Important

Il est recommandé d’avoir une certaine connaissance du développement Odoo pour
configurer correctement les filtres _Domaine_.

Pour accéder à la condition _Domaine_ , vous devez activer le [mode
développeur](../general/developer_mode.html#developer-mode). Une fois cela
fait, sélectionnez le type de condition Domaine et cliquez sur Ajouter un
filtre.

![Activez le type de condition Domaine dans Odoo
Documents](../../_images/activate-domain-condition.png)

Pour créer une règle, vous sélectionnez habituellement un champ, un opérateur
et une valeur. Par exemple, si vous voulez ajouter une action de flux de
travail à tous les fichiers PDF dans un espace de travail, définissez le champ
sur _Type de mime_ , l”opérateur sur _contient_ et la valeur sur _pdf_.

![Exemple d'une condition de domaine d'une action de flux de travail dans Odoo
Documents](../../_images/domain-condition-example.png)

Cliquez sur Ajouter un nœud (icône plus encerclé) et Ajouter une branche
(icône d’ellipse) pour ajouter des conditions et des sous-conditions. Vous
pouvez ensuite préciser si une règle doit correspondre à TOUTES ou à UNE
condition. Vous pouvez également modifier la règle directement à l’aide de
l”Éditeur de code.

![Ajoutez un nœud ou une branche à une condition d'une action de flux de
travail dans Odoo Documents](../../_images/use-domain-condition.png)

### Configurer les actions

Sélectionnez l’onglet Actions pour configurer votre action. Vous pouvez en
même temps :

  * **Définir le contact** : ajouter un contact au fichier ou remplacer un contact existant par un nouveau.

  * **Définir le propriétaire** : ajouter un propriétaire au fichier ou remplacer un propriétaire existant par un nouveau.

  * **Déplacer vers l’espace de travail** : déplacer le fichier vers n’importe quel espace de travail.

  * **Créer** : créer l’un des éléments suivants associés au fichier dans votre base de données :

>     * **Modèle de produit** : créer un produit que vous pouvez modifier
> directement.
>
>     * **Tâche** : créer une tâche de projet que vous pouvez modifier
> directement.
>
>     * **Demande de signature** : créer un nouveau modèle de signature à
> envoyer.
>
>     * **Signer directement** : créer un modèle de signature pour signer
> directement.
>
>     * **Facture fournisseur** : créer une facture fournisseur à l’aide de
> l’OCR et de l’IA pour extraire les informations du contenu du fichier.
>
>     * **Facture client** : créer une facture client à l’aide de l’OCR et de
> l’IA pour extraire les informations du fichier.
>
>     * **Avoir fournisseur** : créer un avoir fournisseur à l’aide de l’OCR
> et de l’IA pour extraire les informations du fichier.
>
>     * **Avoir client** : créez un avoir client à l’aide de l’OCR et de l’IA
> pour extraire les informations du fichier.
>
>     * **Candidat** : créer une nouvelle candidature RH que vous pouvez
> modifier directement.

  * **Définir les étiquettes** : ajouter, supprimer et remplacer un nombre quelconque d’étiquettes.

  * **Activités - Tout marquer comme fait** : marquer toutes les activités associées au fichier comme faites.

  * **Activités - Planifier une activité** : créer une nouvelle activité associée au fichier tel que configuré dans l’action. Vous pouvez choisir de définir l’activité sur le propriétaire du document.

![Exemple d'une action de flux de travail dans Odoo
Documents](../../_images/workflow-action-example.png)

## Numériser les documents grâce à l’IA et la reconnaissance optique de
caractères (OCR)

Les documents disponibles dans l’espace de travail Finance peuvent être
numérisés. Sélectionnez le document que vous voulez numériser, cliquez sur
Créer une facture fournisseur, Créer une facture client ou Créer un avoir et
cliquez ensuite sur Envoi pour numérisation.

Pour plus d'infos

[Numérisation de documents à l’aide de
l’IA](../finance/accounting/vendor_bills/invoice_digitization.html)

