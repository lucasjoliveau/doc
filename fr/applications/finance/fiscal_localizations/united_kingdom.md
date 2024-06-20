# Royaume-Uni

## Configuration

[Installez](../../general/apps_modules.html#general-install) les modules
Royaume-Uni - Comptabilité et Royaume-Uni - Rapports comptables pour obtenir
toutes les fonctionnalités de la localisation du Royaume-Uni.

Nom | Nom technique | Description  
---|---|---  
Royaume-Uni - Comptabilité | `l10n_uk` | 

  * Plan comptable prêt pour le CT600
  * Structure fiscale prête pour le formulaire TVA100
  * Liste des pays d’Infologic Royaume-Uni

  
Royaume-Uni - Rapports comptables | `l10n_uk_reports` | 

  * Rapports comptables pour le Royaume-Uni
  * Permet d’envoyer la déclaration de TVA via l’API MTD-VAT au HMRC.

  
![Packages du Royaume-Uni proposés par Odoo](../../../_images/uk.png)

Note

  * Seules les sociétés situées au Royaume-Uni peuvent soumettre des rapports au HMRC.

  * L’installation du module Royaume-Uni - Rapports comptables installe les deux modules en une fois.

Pour plus d'infos

  * [HM Revenue & Customs](https://www.gov.uk/government/organisations/hm-revenue-customs/)

  * [Overview of Making Tax Digital](https://www.gov.uk/government/publications/making-tax-digital/overview-of-making-tax-digital/)

## Plan comptable

Le plan comptable britannique est inclut dans le module Royaume-Uni -
Comptabilité. Allez à Comptabilité ‣ Configuration ‣ Comptabilité : Plan
comptable pour y accéder.

Configurez votre CoA en allant à Comptabilité ‣ Configuration ‣ Paramètres ‣
Comptabilité section Import et choisissez de Réviser manuellement ou Importer
(recommandé) vos soldes initiaux.

## Taxes

Dans le cadre du module de localisation, les taxes britanniques sont créées
automatiquement avec leurs comptes financiers et leur configuration
correspondants.

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ Taxes pour mettre à jour
les Taxes par défaut, la Périodicité de la déclaration d’impôt ou pour
Configurer vos comptes de taxes.

Pour modifier des taxes existantes ou Créer une nouvelle taxe, allez à
Comptabilité ‣ Configuration ‣ Comptabilité : Taxes.

Pour plus d'infos

  * [taxes](../accounting/taxes.html)

  * Tutoriel : [Déclaration de TVA et d’impôt](https://www.odoo.com/slides/slide/tax-report-and-return-1719?fullscreen=1).

### Making Tax Digital (MTD)

Au Royaume-Uni, toutes les entreprises assujetties à la TVA doivent suivre les
règles du MTD en utilisant un logiciel pour soumettre leurs déclarations de
TVA.

Le module **Royaume-Uni - Rapports comptables** vous permet de vous conformer
aux exigences du [HM Revenue &
Customs](https://www.gov.uk/government/organisations/hm-revenue-customs/)
concernant [Making Tax
Digital](https://www.gov.uk/government/publications/making-tax-
digital/overview-of-making-tax-digital/).

Important

Si votre déclaration périodique a plus de trois mois de retard, il n’est plus
possible de la soumettre via Odoo, puisqu’Odoo ne récupère que les obligations
ouvertes des trois derniers mois. Votre déclaration doit être effectuée
manuellement en contactant le HMRC.

#### Enregistrer votre entreprise auprès du HMRC avant la première soumission

Allez à Comptabilité ‣ Analyse ‣ Déclaration de TVA et cliquez sur Connexion à
HMRC. Saisissez les informations relatives à votre société sur la plateforme
du HMRC. Vous ne devez le faire qu’une seule fois.

#### Soumission périodique au HMRC

Importez vos obligations HMRC, filtrez sur la période que vous souhaitez
soumettre et envoyez votre déclaration de TVA en cliquant sur Envoyer au HMRC.

Astuce

You can use dummy credentials to demo the HMRC flow. To do so, activate the
[developer mode](../../general/developer_mode.html#developer-mode) and go to
General Settings ‣ Technical ‣ System Parameters. From here, search for
`l10n_uk_reports.hmrc_mode` and change the value line to `demo`. You can get
such credentials from the [HMRC Developer
Hub](https://developer.service.hmrc.gov.uk/api-test-user).

#### Soumission périodique au HMRC pour plusieurs sociétés

Une seule société et un seul utilisateur peuvent se connecter simultanément au
HMRC. Si plusieurs sociétés basées au Royaume-Uni se trouvent dans la même
base de données, l’utilisateur qui soumet le rapport HMRC doit suivre ces
instructions avant chaque soumission :

  1. Se connecter à la société pour laquelle la déclaration doit être soumise.

  2. Allez aux Paramètres généraux et dans la section Utilisateurs, cliquez sur Gérer les utilisateurs. Sélectionnez l’utilisateur qui est lié au HMRC.

  3. Allez à l’onglet Intégration HMRC UK et cliquez sur le bouton Réinitialiser les identifiants d’authentification ou Supprimer les identifiants d’authentification.

  4. Vous pouvez à présent enregistrer votre société auprès du HMRC et soumettre la déclaration de TVA pour cette société.

  5. Répétez les étapes pour les soumissions HMRC des autres sociétés.

Note

Pendant ce processus, le bouton Connexion au HMRC n’apparaît plus pour les
sociétés basées au Royaume-Uni.

  *[CoA]: plan comptable

