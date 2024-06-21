# Konvergo ERP.sh

  * Vue d’ensemble
    * [Introduction à Konvergo ERP.sh](odoo_sh/overview/introduction)
  * Les prémices
    * Créer votre projet
      * [Déployer votre plateforme](odoo_sh/getting_started/create#deploy-your-platform)
      * [Se connecter avec Github](odoo_sh/getting_started/create#sign-in-with-github)
      * [Autoriser Konvergo ERP.sh](odoo_sh/getting_started/create#authorize-odoo-sh)
      * [Soumettre votre projet](odoo_sh/getting_started/create#submit-your-project)
      * [C’est fait !](odoo_sh/getting_started/create#you-re-done)
      * Importer votre base de données
        * [Pousser vos modules en production](odoo_sh/getting_started/create#push-your-modules-in-production)
        * Télécharger une sauvegarde
          * [Bases de données On Premise](odoo_sh/getting_started/create#on-premise-databases)
          * [Bases de données Konvergo ERP Online](odoo_sh/getting_started/create#odoo-online-databases)
        * [Charger la sauvegarde](odoo_sh/getting_started/create#upload-the-backup)
        * [Vérifier vos serveurs de messagerie sortants](odoo_sh/getting_started/create#check-your-outgoing-email-servers)
        * [Vérifier vos actions planifiées](odoo_sh/getting_started/create#check-your-scheduled-actions)
        * [Enregistrer votre abonnement](odoo_sh/getting_started/create#register-your-subscription)
    * Branches
      * [Vue d’ensemble](odoo_sh/getting_started/branches#overview)
      * Phases
        * [Production](odoo_sh/getting_started/branches#production)
        * [Simulation](odoo_sh/getting_started/branches#staging)
        * [Développement](odoo_sh/getting_started/branches#development)
        * [Fusionner vos branches](odoo_sh/getting_started/branches#merging-your-branches)
      * Onglets
        * [Historique](odoo_sh/getting_started/branches#history)
        * [Emails](odoo_sh/getting_started/branches#mails)
        * [Shell](odoo_sh/getting_started/branches#shell)
        * [Editor](odoo_sh/getting_started/branches#editor)
        * [Monitoring](odoo_sh/getting_started/branches#monitoring)
        * [Journaux](odoo_sh/getting_started/branches#logs)
        * [Sauvegardes](odoo_sh/getting_started/branches#backups)
        * [Mettre à niveau](odoo_sh/getting_started/branches#upgrade)
        * [Paramètres](odoo_sh/getting_started/branches#settings)
      * Commandes shell
        * [Clone](odoo_sh/getting_started/branches#clone)
        * [Fork](odoo_sh/getting_started/branches#fork)
        * [Merge](odoo_sh/getting_started/branches#merge)
        * SSH
          * [Configuration](odoo_sh/getting_started/branches#setup)
          * [Connexion](odoo_sh/getting_started/branches#connection)
        * [Sous-module](odoo_sh/getting_started/branches#submodule)
        * [Supprimer](odoo_sh/getting_started/branches#delete)
    * Builds
      * [Vue d’ensemble](odoo_sh/getting_started/builds#overview)
      * Phases
        * [Production](odoo_sh/getting_started/builds#production)
        * [Simulation](odoo_sh/getting_started/builds#staging)
        * [Développement](odoo_sh/getting_started/builds#development)
      * [Fonctionnalités](odoo_sh/getting_started/builds#features)
    * Statut
      * [Vue d’ensemble](odoo_sh/getting_started/status#overview)
    * Paramètres
      * [Vue d’ensemble](odoo_sh/getting_started/settings#overview)
      * [Nom du projet](odoo_sh/getting_started/settings#project-name)
      * [Collaborateurs](odoo_sh/getting_started/settings#collaborators)
      * [Accès public](odoo_sh/getting_started/settings#public-access)
      * [Domaines personnalisés](odoo_sh/getting_started/settings#custom-domains)
      * [Sous-modules](odoo_sh/getting_started/settings#submodules)
      * [Taille de stockage](odoo_sh/getting_started/settings#storage-size)
      * [Workers de base de données](odoo_sh/getting_started/settings#database-workers)
      * [Branches de simulation](odoo_sh/getting_started/settings#staging-branches)
      * [Activation](odoo_sh/getting_started/settings#activation)
    * Éditeur en ligne
      * [Vue d’ensemble](odoo_sh/getting_started/online-editor#overview)
      * [Modifier le code source](odoo_sh/getting_started/online-editor#edit-the-source-code)
      * [Commiter & pousser vos changements](odoo_sh/getting_started/online-editor#commit-push-your-changes)
      * [Consoles](odoo_sh/getting_started/online-editor#consoles)
    * Votre premier module
      * [Vue d’ensemble](odoo_sh/getting_started/first_module#overview)
      * Créer la branche de développement
        * [À partir de Konvergo ERP.sh](odoo_sh/getting_started/first_module#from-odoo-sh)
        * [À partir de votre ordinateur](odoo_sh/getting_started/first_module#from-your-computer)
      * Créer la structure du module
        * [Échafauder le module](odoo_sh/getting_started/first_module#scaffolding-the-module)
        * [Manuellement](odoo_sh/getting_started/first_module#manually)
      * [Pousser la branche de développement](odoo_sh/getting_started/first_module#push-the-development-branch)
      * [Tester votre module](odoo_sh/getting_started/first_module#test-your-module)
      * Tester avec les données de production
        * [Installer votre module](odoo_sh/getting_started/first_module#install-your-module)
      * Déployer en production
        * [Installer votre module](odoo_sh/getting_started/first_module#id1)
      * [Ajouter un changement](odoo_sh/getting_started/first_module#add-a-change)
      * [Utiliser une bibliothèque Python externe](odoo_sh/getting_started/first_module#use-an-external-python-library)
  * Avancé
    * Conteneurs
      * [Vue d’ensemble](odoo_sh/advanced/containers#overview)
      * [Structure du répertoire](odoo_sh/advanced/containers#directory-structure)
      * [Shell de base de données](odoo_sh/advanced/containers#database-shell)
      * [Faire fonctionner un serveur Konvergo ERP](odoo_sh/advanced/containers#run-an-odoo-server)
      * [Débogage dans Konvergo ERP.sh](odoo_sh/advanced/containers#debugging-in-odoo-sh)
    * Sous-modules
      * [Vue d’ensemble](odoo_sh/advanced/submodules#overview)
      * Ajouter un sous-module
        * [Avec Konvergo ERP.sh (facile)](odoo_sh/advanced/submodules#with-odoo-sh-simple)
        * [Avec Git (avancé)](odoo_sh/advanced/submodules#with-git-advanced)
      * [Ignorer des modules](odoo_sh/advanced/submodules#ignore-modules)
    * Questions techniques fréquentes
      * [« Les actions planifiées ne s’exécutent pas à l’heure exacte à laquelle elles étaient prévues »](odoo_sh/advanced/frequent_technical_questions#scheduled-actions-do-not-run-at-the-exact-time-they-were-expected)
      * [Existe-t-il des « meilleures pratiques » concernant les actions planifiées ?](odoo_sh/advanced/frequent_technical_questions#are-there-best-practices-regarding-scheduled-actions)

