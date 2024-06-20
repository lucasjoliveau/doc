# Odoo.sh

  * Vue d’ensemble
    * [Introduction à Odoo.sh](odoo_sh/overview/introduction.html)
  * Les prémices
    * Créer votre projet
      * [Déployer votre plateforme](odoo_sh/getting_started/create.html#deploy-your-platform)
      * [Se connecter avec Github](odoo_sh/getting_started/create.html#sign-in-with-github)
      * [Autoriser Odoo.sh](odoo_sh/getting_started/create.html#authorize-odoo-sh)
      * [Soumettre votre projet](odoo_sh/getting_started/create.html#submit-your-project)
      * [C’est fait !](odoo_sh/getting_started/create.html#you-re-done)
      * Importer votre base de données
        * [Pousser vos modules en production](odoo_sh/getting_started/create.html#push-your-modules-in-production)
        * Télécharger une sauvegarde
          * [Bases de données On Premise](odoo_sh/getting_started/create.html#on-premise-databases)
          * [Bases de données Odoo Online](odoo_sh/getting_started/create.html#odoo-online-databases)
        * [Charger la sauvegarde](odoo_sh/getting_started/create.html#upload-the-backup)
        * [Vérifier vos serveurs de messagerie sortants](odoo_sh/getting_started/create.html#check-your-outgoing-email-servers)
        * [Vérifier vos actions planifiées](odoo_sh/getting_started/create.html#check-your-scheduled-actions)
        * [Enregistrer votre abonnement](odoo_sh/getting_started/create.html#register-your-subscription)
    * Branches
      * [Vue d’ensemble](odoo_sh/getting_started/branches.html#overview)
      * Phases
        * [Production](odoo_sh/getting_started/branches.html#production)
        * [Simulation](odoo_sh/getting_started/branches.html#staging)
        * [Développement](odoo_sh/getting_started/branches.html#development)
        * [Fusionner vos branches](odoo_sh/getting_started/branches.html#merging-your-branches)
      * Onglets
        * [Historique](odoo_sh/getting_started/branches.html#history)
        * [Emails](odoo_sh/getting_started/branches.html#mails)
        * [Shell](odoo_sh/getting_started/branches.html#shell)
        * [Editor](odoo_sh/getting_started/branches.html#editor)
        * [Monitoring](odoo_sh/getting_started/branches.html#monitoring)
        * [Journaux](odoo_sh/getting_started/branches.html#logs)
        * [Sauvegardes](odoo_sh/getting_started/branches.html#backups)
        * [Mettre à niveau](odoo_sh/getting_started/branches.html#upgrade)
        * [Paramètres](odoo_sh/getting_started/branches.html#settings)
      * Commandes shell
        * [Clone](odoo_sh/getting_started/branches.html#clone)
        * [Fork](odoo_sh/getting_started/branches.html#fork)
        * [Merge](odoo_sh/getting_started/branches.html#merge)
        * SSH
          * [Configuration](odoo_sh/getting_started/branches.html#setup)
          * [Connexion](odoo_sh/getting_started/branches.html#connection)
        * [Sous-module](odoo_sh/getting_started/branches.html#submodule)
        * [Supprimer](odoo_sh/getting_started/branches.html#delete)
    * Builds
      * [Vue d’ensemble](odoo_sh/getting_started/builds.html#overview)
      * Phases
        * [Production](odoo_sh/getting_started/builds.html#production)
        * [Simulation](odoo_sh/getting_started/builds.html#staging)
        * [Développement](odoo_sh/getting_started/builds.html#development)
      * [Fonctionnalités](odoo_sh/getting_started/builds.html#features)
    * Statut
      * [Vue d’ensemble](odoo_sh/getting_started/status.html#overview)
    * Paramètres
      * [Vue d’ensemble](odoo_sh/getting_started/settings.html#overview)
      * [Nom du projet](odoo_sh/getting_started/settings.html#project-name)
      * [Collaborateurs](odoo_sh/getting_started/settings.html#collaborators)
      * [Accès public](odoo_sh/getting_started/settings.html#public-access)
      * [Domaines personnalisés](odoo_sh/getting_started/settings.html#custom-domains)
      * [Sous-modules](odoo_sh/getting_started/settings.html#submodules)
      * [Taille de stockage](odoo_sh/getting_started/settings.html#storage-size)
      * [Workers de base de données](odoo_sh/getting_started/settings.html#database-workers)
      * [Branches de simulation](odoo_sh/getting_started/settings.html#staging-branches)
      * [Activation](odoo_sh/getting_started/settings.html#activation)
    * Éditeur en ligne
      * [Vue d’ensemble](odoo_sh/getting_started/online-editor.html#overview)
      * [Modifier le code source](odoo_sh/getting_started/online-editor.html#edit-the-source-code)
      * [Commiter & pousser vos changements](odoo_sh/getting_started/online-editor.html#commit-push-your-changes)
      * [Consoles](odoo_sh/getting_started/online-editor.html#consoles)
    * Votre premier module
      * [Vue d’ensemble](odoo_sh/getting_started/first_module.html#overview)
      * Créer la branche de développement
        * [À partir de Odoo.sh](odoo_sh/getting_started/first_module.html#from-odoo-sh)
        * [À partir de votre ordinateur](odoo_sh/getting_started/first_module.html#from-your-computer)
      * Créer la structure du module
        * [Échafauder le module](odoo_sh/getting_started/first_module.html#scaffolding-the-module)
        * [Manuellement](odoo_sh/getting_started/first_module.html#manually)
      * [Pousser la branche de développement](odoo_sh/getting_started/first_module.html#push-the-development-branch)
      * [Tester votre module](odoo_sh/getting_started/first_module.html#test-your-module)
      * Tester avec les données de production
        * [Installer votre module](odoo_sh/getting_started/first_module.html#install-your-module)
      * Déployer en production
        * [Installer votre module](odoo_sh/getting_started/first_module.html#id1)
      * [Ajouter un changement](odoo_sh/getting_started/first_module.html#add-a-change)
      * [Utiliser une bibliothèque Python externe](odoo_sh/getting_started/first_module.html#use-an-external-python-library)
  * Avancé
    * Conteneurs
      * [Vue d’ensemble](odoo_sh/advanced/containers.html#overview)
      * [Structure du répertoire](odoo_sh/advanced/containers.html#directory-structure)
      * [Shell de base de données](odoo_sh/advanced/containers.html#database-shell)
      * [Faire fonctionner un serveur Odoo](odoo_sh/advanced/containers.html#run-an-odoo-server)
      * [Débogage dans Odoo.sh](odoo_sh/advanced/containers.html#debugging-in-odoo-sh)
    * Sous-modules
      * [Vue d’ensemble](odoo_sh/advanced/submodules.html#overview)
      * Ajouter un sous-module
        * [Avec Odoo.sh (facile)](odoo_sh/advanced/submodules.html#with-odoo-sh-simple)
        * [Avec Git (avancé)](odoo_sh/advanced/submodules.html#with-git-advanced)
      * [Ignorer des modules](odoo_sh/advanced/submodules.html#ignore-modules)
    * Questions techniques fréquentes
      * [« Les actions planifiées ne s’exécutent pas à l’heure exacte à laquelle elles étaient prévues »](odoo_sh/advanced/frequent_technical_questions.html#scheduled-actions-do-not-run-at-the-exact-time-they-were-expected)
      * [Existe-t-il des « meilleures pratiques » concernant les actions planifiées ?](odoo_sh/advanced/frequent_technical_questions.html#are-there-best-practices-regarding-scheduled-actions)

