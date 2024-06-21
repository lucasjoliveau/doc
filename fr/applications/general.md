# General settings

  * Applications et modules
    * [Installer des applications et des modules](general/apps_modules#install-apps-and-modules)
    * [Mettre à niveau des applications et des modules](general/apps_modules#upgrade-apps-and-modules)
    * [Désinstaller des applications et des modules](general/apps_modules#uninstall-apps-and-modules)
  * [Utilisateurs](general/users)
    * Ajouter des utilisateurs individuels
      * [User type](general/users#user-type)
    * Désactiver des utilisateurs
      * [Error: too many users](general/users#error-too-many-users)
    * Password management
      * Reset password
        * [Enable password reset from login page](general/users#enable-password-reset-from-login-page)
        * [Send reset instructions](general/users#send-reset-instructions)
      * [Change user password](general/users#change-user-password)
    * Multi-sociétés
      * Changer la langue
        * [Ajouter la langue désirée](general/users/language#load-your-desired-language)
        * [Modifier votre langue](general/users/language#change-your-language)
        * [Modifier la langue d’un autre utilisateur](general/users/language#change-another-user-s-language)
      * Authentification à deux facteurs
        * [Exigences](general/users/2fa#requirements)
        * [Configuration de l’authentification à deux facteurs](general/users/2fa#setting-up-two-factor-authentication)
        * [Se connecter](general/users/2fa#logging-in)
      * Droits d’accès
        * [Utilisateurs](general/users/access_rights#users)
        * [Create and modify groups](general/users/access_rights#create-and-modify-groups)
        * [Superuser mode](general/users/access_rights#superuser-mode)
      * Accès au portail
        * [Donner un accès au portail aux clients](general/users/portal#provide-portal-access-to-customers)
        * [Changer le nom d’utilisateur du portail](general/users/portal#change-portal-username)
        * Changements du portail client
          * [Changer les coordonnées du client](general/users/portal#change-customer-info)
          * [Changer le mot de passe](general/users/portal#change-password)
          * [Ajouter l’authentification à deux facteurs](general/users/portal#add-two-factor-authentication)
          * [Changer les informations de paiement](general/users/portal#change-payment-info)
      * Authentification de connexion Google
        * Configuration
          * Tableau de bord de l’API Google
            * [Écran de consentement OAuth](general/users/google#oauth-consent-screen)
            * [Identifiants](general/users/google#credentials)
          * Authentification Google sur Konvergo ERP
            * [Récupérer l’ID client](general/users/google#retrieve-the-client-id)
            * [Activation sur Konvergo ERP](general/users/google#odoo-activation)
        * [Se connecter à Konvergo ERP avec Google](general/users/google#log-in-to-odoo-with-google)
      * Authentification de connexion Microsoft Azure
        * Configuration
          * [Paramètres système d’Konvergo ERP](general/users/azure#odoo-system-parameter)
          * Tableau de bord Microsoft Azure
            * [Créer une nouvelle application](general/users/azure#create-a-new-application)
            * [Authentification](general/users/azure#authentication)
            * [Rassembler des identifiants](general/users/azure#gather-credentials)
          * [Configuration Konvergo ERP](general/users/azure#odoo-setup)
          * [Flux de l’expérience utilisateur](general/users/azure#user-experience-flows)
      * [Se connecter avec LDAP](general/users/ldap)
  * [Sociétés](general/companies)
    * [Gérer les sociétés et les enregistrements](general/companies#manage-companies-and-records)
    * [Accès des employés](general/companies#employees-access)
    * [Format des documents](general/companies#documents-format)
    * Opérations inter-entreprises
      * Digest emails
        * [Customize default digest email](general/companies/digest_emails#customize-default-digest-email)
        * [Deactivate digest email](general/companies/digest_emails#deactivate-digest-email)
        * [Manually send digest email](general/companies/digest_emails#manually-send-digest-email)
        * [KPIs](general/companies/digest_emails#kpis)
        * [Destinataires](general/companies/digest_emails#recipients)
        * [Create digest emails](general/companies/digest_emails#create-digest-emails)
        * Custom KPIs with Konvergo ERP Studio
          * [Table de référence des valeurs calculées](general/companies/digest_emails#computed-values-reference-table)
      * Modèles d’email
        * Modifier les modèles d’email
          * [Boîte à outils](general/companies/email_template#powerbox)
          * [Éditeur de code XML/HTML](general/companies/email_template#xml-html-code-editor)
          * [Placeholders dynamiques](general/companies/email_template#dynamic-placeholders)
          * [Éditeur de texte enrichi](general/companies/email_template#rich-text-editor)
          * [Réinitialiser les modèles d’email](general/companies/email_template#resetting-email-templates)
          * [Réponse par défaut aux modèles d’email](general/companies/email_template#default-reply-on-email-templates)
        * Emails transactionnels et URLs correspondantes
          * [Mise à jour des traductions dans les modèles d’email](general/companies/email_template#updating-translations-within-email-templates)
  * [Internet des objets (IoT)](general/iot)
    * Configuration
      * Connecter une IoT box à Konvergo ERP
        * [Connexion Ethernet](general/iot/config/connect#ethernet-connection)
        * [Connexion WiFi](general/iot/config/connect#wifi-connection)
        * [Connecter l’IoT Box manuellement à l’aide du jeton](general/iot/config/connect#manually-connecting-the-iot-box-using-the-token)
        * Schéma de l’IoT Box
          * [Raspberry Pi 4](general/iot/config/connect#raspberry-pi-4)
          * [Raspberry Pi 3](general/iot/config/connect#raspberry-pi-3)
      * Utiliser une IoT box avec un Point de Vente
        * [Conditions préalables](general/iot/config/pos#prerequisites)
        * [Configuration](general/iot/config/pos#setup)
      * Certificat HTTPS (IoT)
        * Qu’est-ce que HTTPS ?
          * [Pourquoi est-ce nécessaire ?](general/iot/config/https_certificate_iot#why-is-it-needed)
        * Comment obtenir un certificat Hypertext Transfer Protocol Secure (HTTPS)
          * [Éligibilité à l’Internet des objets (IoT)](general/iot/config/https_certificate_iot#internet-of-things-iot-eligibility)
        * Dépannage des erreurs de certificat Hypertext Transfer Protocol Secure (HTTPS)
          * [`ERR_IOT_HTTPS_CHECK_NO_SERVER`](general/iot/config/https_certificate_iot#err-iot-https-check-no-server)
          * [`ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`](general/iot/config/https_certificate_iot#err-iot-https-check-cert-read-exception)
          * [`ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`](general/iot/config/https_certificate_iot#err-iot-https-load-no-credential)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`](general/iot/config/https_certificate_iot#err-iot-https-load-request-exception)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`](general/iot/config/https_certificate_iot#err-iot-https-load-request-status)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`](general/iot/config/https_certificate_iot#err-iot-https-load-request-no-result)
        * [Comment s’assurer que le certificat HTTPS est correct](general/iot/config/https_certificate_iot#how-to-ensure-that-the-https-certificate-is-correct)
        * Problème de Domain Name System (DNS)
          * [Solution au problème de Domain Name System (DNS)](general/iot/config/https_certificate_iot#domain-name-system-dns-issue-solution)
      * Updating (IoT)
        * [Flashing the SD card on IoT box](general/iot/config/updating_iot#flashing-the-sd-card-on-iot-box)
        * Windows IoT update
          * [Désinstaller Windows pour l’IoT](general/iot/config/updating_iot#uninstalling-windows-iot)
          * [Download and re-install](general/iot/config/updating_iot#download-and-re-install)
          * [Set the destination and complete the installation](general/iot/config/updating_iot#set-the-destination-and-complete-the-installation)
        * [Update from the IoT box home page](general/iot/config/updating_iot#update-from-the-iot-box-home-page)
        * [Handler (driver) update](general/iot/config/updating_iot#handler-driver-update)
      * Aide au dépannage
        * Connexion à l’IoT box
          * [Je ne trouve pas le code d’appariement pour connecter l’IoT box](general/iot/config/troubleshooting#unable-to-locate-the-pairing-code-to-connect-the-iot-box)
          * [IoT box is connected but it is not showing in the database](general/iot/config/troubleshooting#iot-box-is-connected-but-it-is-not-showing-in-the-database)
          * [L’IoT box est connectée à la base de données Konvergo ERP, mais n’est pas accessible](general/iot/config/troubleshooting#the-iot-box-is-connected-to-the-odoo-database-but-cannot-be-reached)
          * [The HTTPS certificate does not generate](general/iot/config/troubleshooting#the-https-certificate-does-not-generate)
        * Imprimante
          * [L’imprimante n’est pas détectée](general/iot/config/troubleshooting#the-printer-is-not-detected)
          * L’imprimante produit un texte aléatoire
            * Cas particulier de la configuration Epson
              * Processus pour forcer la commande ESC *
                * [Compatibilité de l’imprimante Epson](general/iot/config/troubleshooting#epson-printer-compatibility)
                * [Configuration de l’IoT box pour ESC *](general/iot/config/troubleshooting#iot-box-configuration-for-esc)
          * DYMO LabelWriter print issue
            * [DYMO LabelWriter not printing](general/iot/config/troubleshooting#dymo-labelwriter-not-printing)
            * [DYMO LabelWriter print delay](general/iot/config/troubleshooting#dymo-labelwriter-print-delay)
          * [The Zebra printer does not print anything](general/iot/config/troubleshooting#the-zebra-printer-does-not-print-anything)
        * Lecteur de codes-barres
          * [The characters read by the barcode scanner do not match the barcode](general/iot/config/troubleshooting#the-characters-read-by-the-barcode-scanner-do-not-match-the-barcode)
          * [Rien ne se passe lorsqu’un code-barres est scanné](general/iot/config/troubleshooting#nothing-happens-when-a-barcode-is-scanned)
          * [Le lecteur de codes-barres est détecté comme un clavier](general/iot/config/troubleshooting#the-barcode-scanner-is-detected-as-a-keyboard)
          * [Barcode scanner processes barcode characters individually](general/iot/config/troubleshooting#barcode-scanner-processes-barcode-characters-individually)
        * Tiroir caisse
          * [Le tiroir caisse ne s’ouvre pas](general/iot/config/troubleshooting#the-cash-drawer-does-not-open)
        * Balance
          * Set up Ariva S scales
            * [Cable](general/iot/config/troubleshooting#cable)
            * [Configuration](general/iot/config/troubleshooting#setup)
      * Connecter Windows pour l’IoT à Konvergo ERP
        * [Prérequis](general/iot/config/windows_iot#pre-requisites)
        * Connect the Windows virtual IoT box to an Konvergo ERP database
          * [Téléchargement et installation initiale](general/iot/config/windows_iot#download-and-initial-installation)
          * [Définir la destination et finaliser l’installation](general/iot/config/windows_iot#setting-the-destination-and-completing-the-installation)
          * [Connecter des appareils](general/iot/config/windows_iot#connecting-devices)
        * Aide au dépannage
          * [Redémarrer l’IoT box de Windows](general/iot/config/windows_iot#restart-windows-iot-box)
          * Pare-feu
            * Créer une exception dans Windows Defender
              * [Créer une règle dans Windows Defender](general/iot/config/windows_iot#create-a-rule-in-windows-defender)
              * [Configurer une nouvelle règle](general/iot/config/windows_iot#configure-new-rule)
            * [Worldline exception](general/iot/config/windows_iot#worldline-exception)
          * [Désinstaller Windows pour l’IoT](general/iot/config/windows_iot#uninstalling-windows-iot)
    * [Périphériques](general/iot/devices)
      * Connecter un écran
        * [Connexion](general/iot/devices/screen#connection)
        * Utilisation
          * [Afficher les commandes du Point de Vente aux clients](general/iot/devices/screen#show-point-of-sale-orders-to-customers)
          * [Afficher un site web à l’écran](general/iot/devices/screen#display-a-website-on-the-screen)
      * Connecter un outil de mesure
        * [Connecter via USB (universal serial bus)](general/iot/devices/measurement_tool#connect-with-universal-serial-bus-usb)
        * [Connecter via Bluetooth](general/iot/devices/measurement_tool#connect-with-bluetooth)
        * [Lier un outil de mesure à un point de contrôle qualité dans le processus de fabrication](general/iot/devices/measurement_tool#link-a-measurement-tool-to-a-quality-control-point-in-the-manufacturing-process)
        * [Lier un outil de mesure à un poste de travail dans l’application Fabrication](general/iot/devices/measurement_tool#link-a-measurement-tool-to-a-work-center-in-the-manufacturing-app)
      * Connecter une caméra
        * [Connexion](general/iot/devices/camera#connection)
        * [Lier une caméra à un point de contrôle qualité dans le processus de fabrication](general/iot/devices/camera#link-camera-to-quality-control-point-in-manufacturing-process)
        * [Lier une caméra à un poste de travail dans l’application Fabrication](general/iot/devices/camera#link-camera-to-a-work-center-in-the-manufacturing-app)
      * Connecter une pédale de commande
        * [Connexion](general/iot/devices/footswitch#connection)
        * [Lier une pédale de commande à un post de travail dans l’application Fabrication d’Konvergo ERP.](general/iot/devices/footswitch#link-a-footswitch-to-a-work-center-in-the-odoo-manufacturing-app)
      * Connecter une imprimante
        * [Connexion](general/iot/devices/printer#connection)
        * Lier une imprimante
          * [Lier une imprimante aux ordres de travail](general/iot/devices/printer#link-printer-to-work-orders)
          * [Lier une imprimante à un poste de travail dans l’application Fabrication](general/iot/devices/printer#link-a-printer-to-a-work-center-in-the-manufacturing-app)
          * [Lier une imprimante aux rapports](general/iot/devices/printer#link-printer-to-reports)
      * Connecter une balance
        * [Connexion](general/iot/devices/scale#connection)
        * [Utiliser une balance dans un système de point de vente (PdV)](general/iot/devices/scale#use-a-scale-in-a-point-of-sale-pos-system)
  * Email communication
    * Envoyer et recevoir des emails dans Konvergo ERP avec un serveur de messagerie
      * [Utilisateurs d’Konvergo ERP Online ou d’Konvergo ERP.sh](general/email_communication/email_servers#odoo-online-or-odoo-sh-users)
      * [Le but de cette documentation](general/email_communication/email_servers#scope-of-this-documentation)
      * [Notifications par défaut](general/email_communication/email_servers#default-notifications-system)
      * Comment gérer les messages sortants
        * [Restriction de port](general/email_communication/email_servers#port-restriction)
        * [Utiliser une adresse email « De » par défaut](general/email_communication/email_servers#use-a-default-from-email-address)
        * [Utiliser le filtre « De » sur un serveur de messagerie sortant](general/email_communication/email_servers#utilizing-the-from-filter-on-an-outgoing-email-server)
        * [Configurer différents serveurs dédiés pour les emails transactionnels et les envois de masse](general/email_communication/email_servers#set-up-different-dedicated-servers-for-transactional-and-mass-emails)
      * Comment gérer les messages entrants
        * [Paramètres système qui préviennent les boucles de rétraction](general/email_communication/email_servers#system-parameters-that-prevent-feedback-loops)
        * [Allow alias domain system parameter](general/email_communication/email_servers#allow-alias-domain-system-parameter)
    * Configurer les enregistrements DNS pour envoyer des emails dans Konvergo ERP
      * [Vue d’ensemble des étiquettes SPAM](general/email_communication/email_domain#spam-labels-overview)
      * [Être conforme au SPF](general/email_communication/email_domain#be-spf-compliant)
      * [Activer DKIM](general/email_communication/email_domain#enable-dkim)
      * [Verifier la politique DMARC](general/email_communication/email_domain#check-the-dmarc-policy)
      * [Documentation SPF, DKIM & DMARC des fournisseurs courants](general/email_communication/email_domain#spf-dkim-dmarc-documentation-of-common-providers)
    * Connecter Microsoft Outlook 365 à Konvergo ERP avec Azure OAuth
      * Configuration dans le portail Microsoft Azure
        * [Créer une nouvelle application](general/email_communication/azure_oauth#create-a-new-application)
        * [API autorisées](general/email_communication/azure_oauth#api-permissions)
      * Assigner des utilisateurs et des groupes
        * [Créer des identifiants](general/email_communication/azure_oauth#create-credentials)
      * Configuration dans Konvergo ERP
        * [Saisir des identifiants de Microsoft Outlook](general/email_communication/azure_oauth#enter-microsoft-outlook-credentials)
        * Configurer le serveur de messagerie sortant
          * [Configuration avec un seul serveur de messagerie sortant](general/email_communication/azure_oauth#configuration-with-a-single-outgoing-mail-server)
          * Configuration spécifique à l’utilisateur (plusieurs utilisateurs)
            * [Configuration](general/email_communication/azure_oauth#setup)
        * [Configurer le serveur de messagerie entrant](general/email_communication/azure_oauth#configure-incoming-email-server)
    * Connecter Gmail à Konvergo ERP en utilisant Google OAuth
      * Configuration dans Google
        * [Créer un nouveau projet](general/email_communication/google_oauth#create-a-new-project)
        * [Écran de consentement OAuth](general/email_communication/google_oauth#oauth-consent-screen)
        * [Modifier l’enregistrement de l’application](general/email_communication/google_oauth#edit-app-registration)
        * [Créer des identifiants](general/email_communication/google_oauth#create-credentials)
      * Configuration dans Konvergo ERP
        * [Saisir des identifiants Google](general/email_communication/google_oauth#enter-google-credentials)
        * [Configurer le serveur de messagerie sortant](general/email_communication/google_oauth#configure-outgoing-email-server)
      * FAQ Google OAuth
        * [Statut de publication Production VS Test](general/email_communication/google_oauth#production-vs-testing-publishing-status)
        * [Aucun utilisateur test ajouté](general/email_communication/google_oauth#no-test-users-added)
        * [Module Gmail non mis à jour](general/email_communication/google_oauth#gmail-module-not-updated)
        * [Type d’application](general/email_communication/google_oauth#application-type)
    * API Mailjet
      * Configuration dans Mailjet
        * [Créer des identifiants d’API](general/email_communication/mailjet_api#create-api-credentials)
        * [Ajouter une ou plusieurs adresses d’expéditeur vérifiées](general/email_communication/mailjet_api#add-verified-sender-address-es)
        * Ajouter un domaine
          * [Configuration dans le DNS du domaine](general/email_communication/mailjet_api#setup-in-the-domain-s-dns)
          * [Revenir aux informations du compte Mailjet](general/email_communication/mailjet_api#return-to-mailjet-account-information)
      * [Configuration dans Konvergo ERP](general/email_communication/mailjet_api#set-up-in-odoo)
    * Problèmes d’email
      * Emails sortants
        * L’email n’est pas envoyé
          * Messages d’erreur fréquents
            * [Limite journalière atteinte](general/email_communication/faq#daily-limit-reached)
            * Erreur SMTP
              * [Pas d’informations sur l’erreur](general/email_communication/faq#no-error-populated)
        * [L’email est envoyé en retard](general/email_communication/faq#email-is-sent-late)
      * Emails entrants
        * [L’email n’est pas reçu](general/email_communication/faq#email-is-not-received)
      * [Obtenir de l’aide de l’assistance Konvergo ERP](general/email_communication/faq#get-help-from-odoo-support)
  * Intégrations
    * [Plugins de messagerie](general/integrations/mail_plugins)
      * Plugin Outlook
        * Configuration
          * [Activer le plugin de messagerie](general/integrations/mail_plugins/outlook#enable-mail-plugin)
          * [Installer le plugin Outlook](general/integrations/mail_plugins/outlook#install-the-outlook-plugin)
          * [Connecter la base de données](general/integrations/mail_plugins/outlook#connect-the-database)
          * [Ajouter un raccourci au plugin](general/integrations/mail_plugins/outlook#add-a-shortcut-to-the-plugin)
          * [Utiliser le plugin](general/integrations/mail_plugins/outlook#using-the-plugin)
      * Plugin Gmail
        * Utilisateurs d’Konvergo ERP Online
          * [Installer le plugin Gmail](general/integrations/mail_plugins/gmail#install-the-gmail-plugin)
          * [Configurer la base de données Konvergo ERP](general/integrations/mail_plugins/gmail#configure-the-odoo-database)
          * [Configurer la boîte de réception Gmail](general/integrations/mail_plugins/gmail#configure-the-gmail-inbox)
        * Utilisateurs d’Konvergo ERP On-Premise
          * [Installer le plugin Gmail](general/integrations/mail_plugins/gmail#id1)
          * [Configurer la base de données Konvergo ERP](general/integrations/mail_plugins/gmail#id2)
          * [Configurer la boîte de réception Gmail](general/integrations/mail_plugins/gmail#id3)
      * Tarif
        * [Service IAP de génération des pistes](general/integrations/mail_plugins#lead-generation-iap-service)
    * [Unsplash](general/integrations/unsplash)
    * [Géolocalisation](general/integrations/geolocation)
  * Developer mode (debug mode)
    * [Activation](general/developer_mode#activation)
    * [Developer tools and technical menu](general/developer_mode#developer-tools-and-technical-menu)

