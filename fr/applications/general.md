# General settings

  * Applications et modules
    * [Installer des applications et des modules](general/apps_modules.html#install-apps-and-modules)
    * [Mettre à niveau des applications et des modules](general/apps_modules.html#upgrade-apps-and-modules)
    * [Désinstaller des applications et des modules](general/apps_modules.html#uninstall-apps-and-modules)
  * [Utilisateurs](general/users.html)
    * Ajouter des utilisateurs individuels
      * [User type](general/users.html#user-type)
    * Désactiver des utilisateurs
      * [Error: too many users](general/users.html#error-too-many-users)
    * Password management
      * Reset password
        * [Enable password reset from login page](general/users.html#enable-password-reset-from-login-page)
        * [Send reset instructions](general/users.html#send-reset-instructions)
      * [Change user password](general/users.html#change-user-password)
    * Multi-sociétés
      * Changer la langue
        * [Ajouter la langue désirée](general/users/language.html#load-your-desired-language)
        * [Modifier votre langue](general/users/language.html#change-your-language)
        * [Modifier la langue d’un autre utilisateur](general/users/language.html#change-another-user-s-language)
      * Authentification à deux facteurs
        * [Exigences](general/users/2fa.html#requirements)
        * [Configuration de l’authentification à deux facteurs](general/users/2fa.html#setting-up-two-factor-authentication)
        * [Se connecter](general/users/2fa.html#logging-in)
      * Droits d’accès
        * [Utilisateurs](general/users/access_rights.html#users)
        * [Create and modify groups](general/users/access_rights.html#create-and-modify-groups)
        * [Superuser mode](general/users/access_rights.html#superuser-mode)
      * Accès au portail
        * [Donner un accès au portail aux clients](general/users/portal.html#provide-portal-access-to-customers)
        * [Changer le nom d’utilisateur du portail](general/users/portal.html#change-portal-username)
        * Changements du portail client
          * [Changer les coordonnées du client](general/users/portal.html#change-customer-info)
          * [Changer le mot de passe](general/users/portal.html#change-password)
          * [Ajouter l’authentification à deux facteurs](general/users/portal.html#add-two-factor-authentication)
          * [Changer les informations de paiement](general/users/portal.html#change-payment-info)
      * Authentification de connexion Google
        * Configuration
          * Tableau de bord de l’API Google
            * [Écran de consentement OAuth](general/users/google.html#oauth-consent-screen)
            * [Identifiants](general/users/google.html#credentials)
          * Authentification Google sur Odoo
            * [Récupérer l’ID client](general/users/google.html#retrieve-the-client-id)
            * [Activation sur Odoo](general/users/google.html#odoo-activation)
        * [Se connecter à Odoo avec Google](general/users/google.html#log-in-to-odoo-with-google)
      * Authentification de connexion Microsoft Azure
        * Configuration
          * [Paramètres système d’Odoo](general/users/azure.html#odoo-system-parameter)
          * Tableau de bord Microsoft Azure
            * [Créer une nouvelle application](general/users/azure.html#create-a-new-application)
            * [Authentification](general/users/azure.html#authentication)
            * [Rassembler des identifiants](general/users/azure.html#gather-credentials)
          * [Configuration Odoo](general/users/azure.html#odoo-setup)
          * [Flux de l’expérience utilisateur](general/users/azure.html#user-experience-flows)
      * [Se connecter avec LDAP](general/users/ldap.html)
  * [Sociétés](general/companies.html)
    * [Gérer les sociétés et les enregistrements](general/companies.html#manage-companies-and-records)
    * [Accès des employés](general/companies.html#employees-access)
    * [Format des documents](general/companies.html#documents-format)
    * Opérations inter-entreprises
      * Digest emails
        * [Customize default digest email](general/companies/digest_emails.html#customize-default-digest-email)
        * [Deactivate digest email](general/companies/digest_emails.html#deactivate-digest-email)
        * [Manually send digest email](general/companies/digest_emails.html#manually-send-digest-email)
        * [KPIs](general/companies/digest_emails.html#kpis)
        * [Destinataires](general/companies/digest_emails.html#recipients)
        * [Create digest emails](general/companies/digest_emails.html#create-digest-emails)
        * Custom KPIs with Odoo Studio
          * [Table de référence des valeurs calculées](general/companies/digest_emails.html#computed-values-reference-table)
      * Modèles d’email
        * Modifier les modèles d’email
          * [Boîte à outils](general/companies/email_template.html#powerbox)
          * [Éditeur de code XML/HTML](general/companies/email_template.html#xml-html-code-editor)
          * [Placeholders dynamiques](general/companies/email_template.html#dynamic-placeholders)
          * [Éditeur de texte enrichi](general/companies/email_template.html#rich-text-editor)
          * [Réinitialiser les modèles d’email](general/companies/email_template.html#resetting-email-templates)
          * [Réponse par défaut aux modèles d’email](general/companies/email_template.html#default-reply-on-email-templates)
        * Emails transactionnels et URLs correspondantes
          * [Mise à jour des traductions dans les modèles d’email](general/companies/email_template.html#updating-translations-within-email-templates)
  * [Internet des objets (IoT)](general/iot.html)
    * Configuration
      * Connecter une IoT box à Odoo
        * [Connexion Ethernet](general/iot/config/connect.html#ethernet-connection)
        * [Connexion WiFi](general/iot/config/connect.html#wifi-connection)
        * [Connecter l’IoT Box manuellement à l’aide du jeton](general/iot/config/connect.html#manually-connecting-the-iot-box-using-the-token)
        * Schéma de l’IoT Box
          * [Raspberry Pi 4](general/iot/config/connect.html#raspberry-pi-4)
          * [Raspberry Pi 3](general/iot/config/connect.html#raspberry-pi-3)
      * Utiliser une IoT box avec un Point de Vente
        * [Conditions préalables](general/iot/config/pos.html#prerequisites)
        * [Configuration](general/iot/config/pos.html#setup)
      * Certificat HTTPS (IoT)
        * Qu’est-ce que HTTPS ?
          * [Pourquoi est-ce nécessaire ?](general/iot/config/https_certificate_iot.html#why-is-it-needed)
        * Comment obtenir un certificat Hypertext Transfer Protocol Secure (HTTPS)
          * [Éligibilité à l’Internet des objets (IoT)](general/iot/config/https_certificate_iot.html#internet-of-things-iot-eligibility)
        * Dépannage des erreurs de certificat Hypertext Transfer Protocol Secure (HTTPS)
          * [`ERR_IOT_HTTPS_CHECK_NO_SERVER`](general/iot/config/https_certificate_iot.html#err-iot-https-check-no-server)
          * [`ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-check-cert-read-exception)
          * [`ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`](general/iot/config/https_certificate_iot.html#err-iot-https-load-no-credential)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-exception)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-status)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-no-result)
        * [Comment s’assurer que le certificat HTTPS est correct](general/iot/config/https_certificate_iot.html#how-to-ensure-that-the-https-certificate-is-correct)
        * Problème de Domain Name System (DNS)
          * [Solution au problème de Domain Name System (DNS)](general/iot/config/https_certificate_iot.html#domain-name-system-dns-issue-solution)
      * Updating (IoT)
        * [Flashing the SD card on IoT box](general/iot/config/updating_iot.html#flashing-the-sd-card-on-iot-box)
        * Windows IoT update
          * [Désinstaller Windows pour l’IoT](general/iot/config/updating_iot.html#uninstalling-windows-iot)
          * [Download and re-install](general/iot/config/updating_iot.html#download-and-re-install)
          * [Set the destination and complete the installation](general/iot/config/updating_iot.html#set-the-destination-and-complete-the-installation)
        * [Update from the IoT box home page](general/iot/config/updating_iot.html#update-from-the-iot-box-home-page)
        * [Handler (driver) update](general/iot/config/updating_iot.html#handler-driver-update)
      * Aide au dépannage
        * Connexion à l’IoT box
          * [Je ne trouve pas le code d’appariement pour connecter l’IoT box](general/iot/config/troubleshooting.html#unable-to-locate-the-pairing-code-to-connect-the-iot-box)
          * [IoT box is connected but it is not showing in the database](general/iot/config/troubleshooting.html#iot-box-is-connected-but-it-is-not-showing-in-the-database)
          * [L’IoT box est connectée à la base de données Odoo, mais n’est pas accessible](general/iot/config/troubleshooting.html#the-iot-box-is-connected-to-the-odoo-database-but-cannot-be-reached)
          * [The HTTPS certificate does not generate](general/iot/config/troubleshooting.html#the-https-certificate-does-not-generate)
        * Imprimante
          * [L’imprimante n’est pas détectée](general/iot/config/troubleshooting.html#the-printer-is-not-detected)
          * L’imprimante produit un texte aléatoire
            * Cas particulier de la configuration Epson
              * Processus pour forcer la commande ESC *
                * [Compatibilité de l’imprimante Epson](general/iot/config/troubleshooting.html#epson-printer-compatibility)
                * [Configuration de l’IoT box pour ESC *](general/iot/config/troubleshooting.html#iot-box-configuration-for-esc)
          * DYMO LabelWriter print issue
            * [DYMO LabelWriter not printing](general/iot/config/troubleshooting.html#dymo-labelwriter-not-printing)
            * [DYMO LabelWriter print delay](general/iot/config/troubleshooting.html#dymo-labelwriter-print-delay)
          * [The Zebra printer does not print anything](general/iot/config/troubleshooting.html#the-zebra-printer-does-not-print-anything)
        * Lecteur de codes-barres
          * [The characters read by the barcode scanner do not match the barcode](general/iot/config/troubleshooting.html#the-characters-read-by-the-barcode-scanner-do-not-match-the-barcode)
          * [Rien ne se passe lorsqu’un code-barres est scanné](general/iot/config/troubleshooting.html#nothing-happens-when-a-barcode-is-scanned)
          * [Le lecteur de codes-barres est détecté comme un clavier](general/iot/config/troubleshooting.html#the-barcode-scanner-is-detected-as-a-keyboard)
          * [Barcode scanner processes barcode characters individually](general/iot/config/troubleshooting.html#barcode-scanner-processes-barcode-characters-individually)
        * Tiroir caisse
          * [Le tiroir caisse ne s’ouvre pas](general/iot/config/troubleshooting.html#the-cash-drawer-does-not-open)
        * Balance
          * Set up Ariva S scales
            * [Cable](general/iot/config/troubleshooting.html#cable)
            * [Configuration](general/iot/config/troubleshooting.html#setup)
      * Connecter Windows pour l’IoT à Odoo
        * [Prérequis](general/iot/config/windows_iot.html#pre-requisites)
        * Connect the Windows virtual IoT box to an Odoo database
          * [Téléchargement et installation initiale](general/iot/config/windows_iot.html#download-and-initial-installation)
          * [Définir la destination et finaliser l’installation](general/iot/config/windows_iot.html#setting-the-destination-and-completing-the-installation)
          * [Connecter des appareils](general/iot/config/windows_iot.html#connecting-devices)
        * Aide au dépannage
          * [Redémarrer l’IoT box de Windows](general/iot/config/windows_iot.html#restart-windows-iot-box)
          * Pare-feu
            * Créer une exception dans Windows Defender
              * [Créer une règle dans Windows Defender](general/iot/config/windows_iot.html#create-a-rule-in-windows-defender)
              * [Configurer une nouvelle règle](general/iot/config/windows_iot.html#configure-new-rule)
            * [Worldline exception](general/iot/config/windows_iot.html#worldline-exception)
          * [Désinstaller Windows pour l’IoT](general/iot/config/windows_iot.html#uninstalling-windows-iot)
    * [Périphériques](general/iot/devices.html)
      * Connecter un écran
        * [Connexion](general/iot/devices/screen.html#connection)
        * Utilisation
          * [Afficher les commandes du Point de Vente aux clients](general/iot/devices/screen.html#show-point-of-sale-orders-to-customers)
          * [Afficher un site web à l’écran](general/iot/devices/screen.html#display-a-website-on-the-screen)
      * Connecter un outil de mesure
        * [Connecter via USB (universal serial bus)](general/iot/devices/measurement_tool.html#connect-with-universal-serial-bus-usb)
        * [Connecter via Bluetooth](general/iot/devices/measurement_tool.html#connect-with-bluetooth)
        * [Lier un outil de mesure à un point de contrôle qualité dans le processus de fabrication](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-quality-control-point-in-the-manufacturing-process)
        * [Lier un outil de mesure à un poste de travail dans l’application Fabrication](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-work-center-in-the-manufacturing-app)
      * Connecter une caméra
        * [Connexion](general/iot/devices/camera.html#connection)
        * [Lier une caméra à un point de contrôle qualité dans le processus de fabrication](general/iot/devices/camera.html#link-camera-to-quality-control-point-in-manufacturing-process)
        * [Lier une caméra à un poste de travail dans l’application Fabrication](general/iot/devices/camera.html#link-camera-to-a-work-center-in-the-manufacturing-app)
      * Connecter une pédale de commande
        * [Connexion](general/iot/devices/footswitch.html#connection)
        * [Lier une pédale de commande à un post de travail dans l’application Fabrication d’Odoo.](general/iot/devices/footswitch.html#link-a-footswitch-to-a-work-center-in-the-odoo-manufacturing-app)
      * Connecter une imprimante
        * [Connexion](general/iot/devices/printer.html#connection)
        * Lier une imprimante
          * [Lier une imprimante aux ordres de travail](general/iot/devices/printer.html#link-printer-to-work-orders)
          * [Lier une imprimante à un poste de travail dans l’application Fabrication](general/iot/devices/printer.html#link-a-printer-to-a-work-center-in-the-manufacturing-app)
          * [Lier une imprimante aux rapports](general/iot/devices/printer.html#link-printer-to-reports)
      * Connecter une balance
        * [Connexion](general/iot/devices/scale.html#connection)
        * [Utiliser une balance dans un système de point de vente (PdV)](general/iot/devices/scale.html#use-a-scale-in-a-point-of-sale-pos-system)
  * Email communication
    * Envoyer et recevoir des emails dans Odoo avec un serveur de messagerie
      * [Utilisateurs d’Odoo Online ou d’Odoo.sh](general/email_communication/email_servers.html#odoo-online-or-odoo-sh-users)
      * [Le but de cette documentation](general/email_communication/email_servers.html#scope-of-this-documentation)
      * [Notifications par défaut](general/email_communication/email_servers.html#default-notifications-system)
      * Comment gérer les messages sortants
        * [Restriction de port](general/email_communication/email_servers.html#port-restriction)
        * [Utiliser une adresse email « De » par défaut](general/email_communication/email_servers.html#use-a-default-from-email-address)
        * [Utiliser le filtre « De » sur un serveur de messagerie sortant](general/email_communication/email_servers.html#utilizing-the-from-filter-on-an-outgoing-email-server)
        * [Configurer différents serveurs dédiés pour les emails transactionnels et les envois de masse](general/email_communication/email_servers.html#set-up-different-dedicated-servers-for-transactional-and-mass-emails)
      * Comment gérer les messages entrants
        * [Paramètres système qui préviennent les boucles de rétraction](general/email_communication/email_servers.html#system-parameters-that-prevent-feedback-loops)
        * [Allow alias domain system parameter](general/email_communication/email_servers.html#allow-alias-domain-system-parameter)
    * Configurer les enregistrements DNS pour envoyer des emails dans Odoo
      * [Vue d’ensemble des étiquettes SPAM](general/email_communication/email_domain.html#spam-labels-overview)
      * [Être conforme au SPF](general/email_communication/email_domain.html#be-spf-compliant)
      * [Activer DKIM](general/email_communication/email_domain.html#enable-dkim)
      * [Verifier la politique DMARC](general/email_communication/email_domain.html#check-the-dmarc-policy)
      * [Documentation SPF, DKIM & DMARC des fournisseurs courants](general/email_communication/email_domain.html#spf-dkim-dmarc-documentation-of-common-providers)
    * Connecter Microsoft Outlook 365 à Odoo avec Azure OAuth
      * Configuration dans le portail Microsoft Azure
        * [Créer une nouvelle application](general/email_communication/azure_oauth.html#create-a-new-application)
        * [API autorisées](general/email_communication/azure_oauth.html#api-permissions)
      * Assigner des utilisateurs et des groupes
        * [Créer des identifiants](general/email_communication/azure_oauth.html#create-credentials)
      * Configuration dans Odoo
        * [Saisir des identifiants de Microsoft Outlook](general/email_communication/azure_oauth.html#enter-microsoft-outlook-credentials)
        * Configurer le serveur de messagerie sortant
          * [Configuration avec un seul serveur de messagerie sortant](general/email_communication/azure_oauth.html#configuration-with-a-single-outgoing-mail-server)
          * Configuration spécifique à l’utilisateur (plusieurs utilisateurs)
            * [Configuration](general/email_communication/azure_oauth.html#setup)
        * [Configurer le serveur de messagerie entrant](general/email_communication/azure_oauth.html#configure-incoming-email-server)
    * Connecter Gmail à Odoo en utilisant Google OAuth
      * Configuration dans Google
        * [Créer un nouveau projet](general/email_communication/google_oauth.html#create-a-new-project)
        * [Écran de consentement OAuth](general/email_communication/google_oauth.html#oauth-consent-screen)
        * [Modifier l’enregistrement de l’application](general/email_communication/google_oauth.html#edit-app-registration)
        * [Créer des identifiants](general/email_communication/google_oauth.html#create-credentials)
      * Configuration dans Odoo
        * [Saisir des identifiants Google](general/email_communication/google_oauth.html#enter-google-credentials)
        * [Configurer le serveur de messagerie sortant](general/email_communication/google_oauth.html#configure-outgoing-email-server)
      * FAQ Google OAuth
        * [Statut de publication Production VS Test](general/email_communication/google_oauth.html#production-vs-testing-publishing-status)
        * [Aucun utilisateur test ajouté](general/email_communication/google_oauth.html#no-test-users-added)
        * [Module Gmail non mis à jour](general/email_communication/google_oauth.html#gmail-module-not-updated)
        * [Type d’application](general/email_communication/google_oauth.html#application-type)
    * API Mailjet
      * Configuration dans Mailjet
        * [Créer des identifiants d’API](general/email_communication/mailjet_api.html#create-api-credentials)
        * [Ajouter une ou plusieurs adresses d’expéditeur vérifiées](general/email_communication/mailjet_api.html#add-verified-sender-address-es)
        * Ajouter un domaine
          * [Configuration dans le DNS du domaine](general/email_communication/mailjet_api.html#setup-in-the-domain-s-dns)
          * [Revenir aux informations du compte Mailjet](general/email_communication/mailjet_api.html#return-to-mailjet-account-information)
      * [Configuration dans Odoo](general/email_communication/mailjet_api.html#set-up-in-odoo)
    * Problèmes d’email
      * Emails sortants
        * L’email n’est pas envoyé
          * Messages d’erreur fréquents
            * [Limite journalière atteinte](general/email_communication/faq.html#daily-limit-reached)
            * Erreur SMTP
              * [Pas d’informations sur l’erreur](general/email_communication/faq.html#no-error-populated)
        * [L’email est envoyé en retard](general/email_communication/faq.html#email-is-sent-late)
      * Emails entrants
        * [L’email n’est pas reçu](general/email_communication/faq.html#email-is-not-received)
      * [Obtenir de l’aide de l’assistance Odoo](general/email_communication/faq.html#get-help-from-odoo-support)
  * Intégrations
    * [Plugins de messagerie](general/integrations/mail_plugins.html)
      * Plugin Outlook
        * Configuration
          * [Activer le plugin de messagerie](general/integrations/mail_plugins/outlook.html#enable-mail-plugin)
          * [Installer le plugin Outlook](general/integrations/mail_plugins/outlook.html#install-the-outlook-plugin)
          * [Connecter la base de données](general/integrations/mail_plugins/outlook.html#connect-the-database)
          * [Ajouter un raccourci au plugin](general/integrations/mail_plugins/outlook.html#add-a-shortcut-to-the-plugin)
          * [Utiliser le plugin](general/integrations/mail_plugins/outlook.html#using-the-plugin)
      * Plugin Gmail
        * Utilisateurs d’Odoo Online
          * [Installer le plugin Gmail](general/integrations/mail_plugins/gmail.html#install-the-gmail-plugin)
          * [Configurer la base de données Odoo](general/integrations/mail_plugins/gmail.html#configure-the-odoo-database)
          * [Configurer la boîte de réception Gmail](general/integrations/mail_plugins/gmail.html#configure-the-gmail-inbox)
        * Utilisateurs d’Odoo On-Premise
          * [Installer le plugin Gmail](general/integrations/mail_plugins/gmail.html#id1)
          * [Configurer la base de données Odoo](general/integrations/mail_plugins/gmail.html#id2)
          * [Configurer la boîte de réception Gmail](general/integrations/mail_plugins/gmail.html#id3)
      * Tarif
        * [Service IAP de génération des pistes](general/integrations/mail_plugins.html#lead-generation-iap-service)
    * [Unsplash](general/integrations/unsplash.html)
    * [Géolocalisation](general/integrations/geolocation.html)
  * Developer mode (debug mode)
    * [Activation](general/developer_mode.html#activation)
    * [Developer tools and technical menu](general/developer_mode.html#developer-tools-and-technical-menu)

