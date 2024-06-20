# Transactions

L’importation de transactions depuis vos relevés bancaires permet de suivre
les transactions de votre compte bancaire et de les rapprocher avec celles
enregistrées dans votre comptabilité.

La [synchronisation bancaire](bank_synchronization.html) automatise le
processus. Cependant, si vous ne souhaitez pas l’utiliser ou si votre banque
n’est pas encore prise en charge, vous disposez d’autres options :

  * L”importation des relevés bancaires fournis par votre banque ;

  * L”enregistrement manuel des transactions bancaires.

Note

Le regroupement des transactions par relevé bancaire est optionnel.

## Importer les transactions

Odoo prend en charge de nombreux formats de fichiers pour importer les
transactions bancaires :

  * Le format Cash Management (CAMT.053) recommandé par SEPA ;

  * Le format CSV (valeurs séparées par des virgules) ;

  * Open Financial Exchange (.OFX) ;

  * Quicken Interchange Format (.QIF) ;

  * Belgique : Extrait de compte codifié (.CODA) ;

Pour importer un fichier, allez au Tableau de bord de Comptabilité, dans dans
le journal de Banque, cliquez sur Importer des transactions.

![Importez des transactions bancaires depuis le journal de
banque](../../../../_images/import-transactions.png)

Ensuite, sélectionnez le fichier et chargez-le.

Après avoir configuré les options de formatage nécessaires et fait
correspondre les colonnes du fichier avec leurs champs Odoo associés, vous
pouvez exécuter un Test et Importer vos transactions bancaires.

Pour plus d'infos

[Exporter et importer des
données](../../../essentials/export_import_data.html)

## Enregistrer les transactions bancaires manuellement

Vous pouvez également enregistrer manuellement vos transactions bancaires.
Pour ce faire, allez au Tableau de bord de Comptabilité, cliquez sur le
journal de Banque, puis sur Nouveau. Assurez-vous de compléter les champs
Partnenaire et Libellé pour faciliter le processus de rapprochement.

## Relevés bancaires

Un **relevé bancaire** est un document fourni par une banque ou un
établissement financier qui répertorie les transactions effectuées sur un
compte bancaire particulier sur une période donnée.

Dans Odoo Comptabilité, il n’est pas obligatoire de regrouper les transactions
dans leur relevé associé, mais en fonction de votre flux commercial, il se
peut que vous vouliez les enregistrer à des fins de contrôle.

Important

Si vous souhaitez comparer le solde final de vos relevés bancaires avec le
solde final de vos enregistrements financiers, _n’oubliez pas de créer une
transaction d’ouverture_ pour enregistrer le solde du compte bancaire à la
date à laquelle vous commencez à synchroniser ou à importer des transactions.
Ceci est nécessaire pour assurer l’exactitude de votre comptabilité.

Pour accéder à une liste des relevés, allez au Tableau de bord de
comptabilité, cliquez sur le bouton d’ellipse vertical (⋮) à côté du journal
de banque ou d’espèces que vous souhaitez consulter, puis sur Relevés.

### Créer des relevés depuis la vue kanban

Ouvrez la vue du rapprochement bancaire en cliquant sur le nom du journal de
banque et en identifiant la transaction correspondant à la dernière
transaction de votre relevé bancaire. Cliquez sur le bouton RELEVÉ lorsque
vous passez la souris sur la ligne de séparation supérieure.

![Un bouton "RELEVÉ" apparaît lorsque vous passez la souris sur la ligne de
séparation entre deux transactions.](../../../../_images/statements-
kanban.png)

Complétez les détails du relevé et enregistrez. Le relevé nouvellement créé
comprend les transactions antérieures au dernier relevé.

### Créer des relevés depuis la vue liste

Ouvrez la liste des transactions en cliquant sur le nom du journal de banque
et en passant à la vue liste. Sélectionnez toutes les transactions
correspondant au relevé bancaire et dans la colonne Relevé, sélectionnez un
relevé existant ou créez-en un nouveau en saisissant sa référence, en cliquant
sur Créer et modifier…, en complétant les détails du relevé et en cliquant sur
enregistrer.

