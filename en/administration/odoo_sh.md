# Odoo.sh

  * Overview
    * [Introduction to Odoo.sh](odoo_sh/overview/introduction.html)
  * Get started
    * Create your project
      * [Deploy your platform](odoo_sh/getting_started/create.html#deploy-your-platform)
      * [Sign in with Github](odoo_sh/getting_started/create.html#sign-in-with-github)
      * [Authorize Odoo.sh](odoo_sh/getting_started/create.html#authorize-odoo-sh)
      * [Submit your project](odoo_sh/getting_started/create.html#submit-your-project)
      * [You’re done !](odoo_sh/getting_started/create.html#you-re-done)
      * Import your database
        * [Push your modules in production](odoo_sh/getting_started/create.html#push-your-modules-in-production)
        * Download a backup
          * [On-premise databases](odoo_sh/getting_started/create.html#on-premise-databases)
          * [Odoo Online databases](odoo_sh/getting_started/create.html#odoo-online-databases)
        * [Upload the backup](odoo_sh/getting_started/create.html#upload-the-backup)
        * [Check your outgoing email servers](odoo_sh/getting_started/create.html#check-your-outgoing-email-servers)
        * [Check your scheduled actions](odoo_sh/getting_started/create.html#check-your-scheduled-actions)
        * [Register your subscription](odoo_sh/getting_started/create.html#register-your-subscription)
    * Branches
      * [Overview](odoo_sh/getting_started/branches.html#overview)
      * Stages
        * [Production](odoo_sh/getting_started/branches.html#production)
        * [Staging](odoo_sh/getting_started/branches.html#staging)
        * [Development](odoo_sh/getting_started/branches.html#development)
        * [Merging your branches](odoo_sh/getting_started/branches.html#merging-your-branches)
      * Tabs
        * [History](odoo_sh/getting_started/branches.html#history)
        * [Mails](odoo_sh/getting_started/branches.html#mails)
        * [Shell](odoo_sh/getting_started/branches.html#shell)
        * [Editor](odoo_sh/getting_started/branches.html#editor)
        * [Monitoring](odoo_sh/getting_started/branches.html#monitoring)
        * [Logs](odoo_sh/getting_started/branches.html#logs)
        * [Backups](odoo_sh/getting_started/branches.html#backups)
        * [Upgrade](odoo_sh/getting_started/branches.html#upgrade)
        * [Settings](odoo_sh/getting_started/branches.html#settings)
      * Shell commands
        * [Clone](odoo_sh/getting_started/branches.html#clone)
        * [Fork](odoo_sh/getting_started/branches.html#fork)
        * [Merge](odoo_sh/getting_started/branches.html#merge)
        * SSH
          * [Setup](odoo_sh/getting_started/branches.html#setup)
          * [Connection](odoo_sh/getting_started/branches.html#connection)
        * [Submodule](odoo_sh/getting_started/branches.html#submodule)
        * [Delete](odoo_sh/getting_started/branches.html#delete)
    * Builds
      * [Overview](odoo_sh/getting_started/builds.html#overview)
      * Stages
        * [Production](odoo_sh/getting_started/builds.html#production)
        * [Staging](odoo_sh/getting_started/builds.html#staging)
        * [Development](odoo_sh/getting_started/builds.html#development)
      * [Features](odoo_sh/getting_started/builds.html#features)
    * Status
      * [Overview](odoo_sh/getting_started/status.html#overview)
    * Settings
      * [Overview](odoo_sh/getting_started/settings.html#overview)
      * [Project name](odoo_sh/getting_started/settings.html#project-name)
      * [Collaborators](odoo_sh/getting_started/settings.html#collaborators)
      * [Public Access](odoo_sh/getting_started/settings.html#public-access)
      * [Custom domains](odoo_sh/getting_started/settings.html#custom-domains)
      * [Submodules](odoo_sh/getting_started/settings.html#submodules)
      * [Storage Size](odoo_sh/getting_started/settings.html#storage-size)
      * [Database Workers](odoo_sh/getting_started/settings.html#database-workers)
      * [Staging Branches](odoo_sh/getting_started/settings.html#staging-branches)
      * [Activation](odoo_sh/getting_started/settings.html#activation)
    * Online Editor
      * [Overview](odoo_sh/getting_started/online-editor.html#overview)
      * [Edit the source code](odoo_sh/getting_started/online-editor.html#edit-the-source-code)
      * [Commit & Push your changes](odoo_sh/getting_started/online-editor.html#commit-push-your-changes)
      * [Consoles](odoo_sh/getting_started/online-editor.html#consoles)
    * Your first module
      * [Overview](odoo_sh/getting_started/first_module.html#overview)
      * Create the development branch
        * [From Odoo.sh](odoo_sh/getting_started/first_module.html#from-odoo-sh)
        * [From your computer](odoo_sh/getting_started/first_module.html#from-your-computer)
      * Create the module structure
        * [Scaffolding the module](odoo_sh/getting_started/first_module.html#scaffolding-the-module)
        * [Manually](odoo_sh/getting_started/first_module.html#manually)
      * [Push the development branch](odoo_sh/getting_started/first_module.html#push-the-development-branch)
      * [Test your module](odoo_sh/getting_started/first_module.html#test-your-module)
      * Test with the production data
        * [Install your module](odoo_sh/getting_started/first_module.html#install-your-module)
      * Deploy in production
        * [Install your module](odoo_sh/getting_started/first_module.html#id1)
      * [Add a change](odoo_sh/getting_started/first_module.html#add-a-change)
      * [Use an external Python library](odoo_sh/getting_started/first_module.html#use-an-external-python-library)
  * Advanced
    * Containers
      * [Overview](odoo_sh/advanced/containers.html#overview)
      * [Directory structure](odoo_sh/advanced/containers.html#directory-structure)
      * [Database shell](odoo_sh/advanced/containers.html#database-shell)
      * [Run an Odoo server](odoo_sh/advanced/containers.html#run-an-odoo-server)
      * [Debugging in Odoo.sh](odoo_sh/advanced/containers.html#debugging-in-odoo-sh)
    * Submodules
      * [Overview](odoo_sh/advanced/submodules.html#overview)
      * Adding a submodule
        * [With Odoo.sh (simple)](odoo_sh/advanced/submodules.html#with-odoo-sh-simple)
        * [With Git (advanced)](odoo_sh/advanced/submodules.html#with-git-advanced)
      * [Ignore modules](odoo_sh/advanced/submodules.html#ignore-modules)
    * Frequent Technical Questions
      * [“Scheduled actions do not run at the exact time they were expected”](odoo_sh/advanced/frequent_technical_questions.html#scheduled-actions-do-not-run-at-the-exact-time-they-were-expected)
      * [Are there “best practices” regarding scheduled actions?](odoo_sh/advanced/frequent_technical_questions.html#are-there-best-practices-regarding-scheduled-actions)

