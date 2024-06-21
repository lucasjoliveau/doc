# General settings

  * Apps and modules
    * [Install apps and modules](general/apps_modules#install-apps-and-modules)
    * [Upgrade apps and modules](general/apps_modules#upgrade-apps-and-modules)
    * [Uninstall apps and modules](general/apps_modules#uninstall-apps-and-modules)
  * [Users](general/users)
    * Add individual users
      * [User type](general/users#user-type)
    * Deactivate users
      * [Error: too many users](general/users#error-too-many-users)
    * Password management
      * Reset password
        * [Enable password reset from login page](general/users#enable-password-reset-from-login-page)
        * [Send reset instructions](general/users#send-reset-instructions)
      * [Change user password](general/users#change-user-password)
    * Multi Companies
      * Change language
        * [Load your desired language](general/users/language#load-your-desired-language)
        * [Change your language](general/users/language#change-your-language)
        * [Change another user’s language](general/users/language#change-another-user-s-language)
      * Two-factor Authentication
        * [Requirements](general/users/2fa#requirements)
        * [Setting up two-factor authentication](general/users/2fa#setting-up-two-factor-authentication)
        * [Logging in](general/users/2fa#logging-in)
      * Access rights
        * [Users](general/users/access_rights#users)
        * [Create and modify groups](general/users/access_rights#create-and-modify-groups)
        * [Superuser mode](general/users/access_rights#superuser-mode)
      * Portal access
        * [Provide portal access to customers](general/users/portal#provide-portal-access-to-customers)
        * [Change portal username](general/users/portal#change-portal-username)
        * Customer portal changes
          * [Change customer info](general/users/portal#change-customer-info)
          * [Change password](general/users/portal#change-password)
          * [Add two-factor authentication](general/users/portal#add-two-factor-authentication)
          * [Change payment info](general/users/portal#change-payment-info)
      * Google Sign-In Authentication
        * Configuration
          * Google API Dashboard
            * [OAuth consent screen](general/users/google#oauth-consent-screen)
            * [Credentials](general/users/google#credentials)
          * Google Authentication on Konvergo ERP
            * [Retrieve the Client ID](general/users/google#retrieve-the-client-id)
            * [Konvergo ERP activation](general/users/google#odoo-activation)
        * [Log in to Konvergo ERP with Google](general/users/google#log-in-to-odoo-with-google)
      * Microsoft Azure sign-in authentication
        * Configuration
          * [Konvergo ERP System Parameter](general/users/azure#odoo-system-parameter)
          * Microsoft Azure dashboard
            * [Create a new application](general/users/azure#create-a-new-application)
            * [Authentication](general/users/azure#authentication)
            * [Gather credentials](general/users/azure#gather-credentials)
          * [Konvergo ERP setup](general/users/azure#odoo-setup)
          * [User experience flows](general/users/azure#user-experience-flows)
      * [Sign in with LDAP](general/users/ldap)
  * [Companies](general/companies)
    * [Manage companies and records](general/companies#manage-companies-and-records)
    * [Employees’ access](general/companies#employees-access)
    * [Documents’ format](general/companies#documents-format)
    * Inter-Company Transactions
      * Digest emails
        * [Customize default digest email](general/companies/digest_emails#customize-default-digest-email)
        * [Deactivate digest email](general/companies/digest_emails#deactivate-digest-email)
        * [Manually send digest email](general/companies/digest_emails#manually-send-digest-email)
        * [KPIs](general/companies/digest_emails#kpis)
        * [Recipients](general/companies/digest_emails#recipients)
        * [Create digest emails](general/companies/digest_emails#create-digest-emails)
        * Custom KPIs with Konvergo ERP Studio
          * [Computed values reference table](general/companies/digest_emails#computed-values-reference-table)
      * Email templates
        * Editing email templates
          * [Powerbox](general/companies/email_template#powerbox)
          * [XML/HTML code editor](general/companies/email_template#xml-html-code-editor)
          * [Dynamic placeholders](general/companies/email_template#dynamic-placeholders)
          * [Rich text editor](general/companies/email_template#rich-text-editor)
          * [Resetting email templates](general/companies/email_template#resetting-email-templates)
          * [Default reply on email templates](general/companies/email_template#default-reply-on-email-templates)
        * Transactional emails and corresponding URLs
          * [Updating translations within email templates](general/companies/email_template#updating-translations-within-email-templates)
  * [Internet of Things (IoT)](general/iot)
    * Configuration
      * Connect an IoT box to Konvergo ERP
        * [Ethernet connection](general/iot/config/connect#ethernet-connection)
        * [WiFi connection](general/iot/config/connect#wifi-connection)
        * [Manually connecting the IoT box using the token](general/iot/config/connect#manually-connecting-the-iot-box-using-the-token)
        * IoT box schema
          * [Raspberry Pi 4](general/iot/config/connect#raspberry-pi-4)
          * [Raspberry Pi 3](general/iot/config/connect#raspberry-pi-3)
      * Use an IoT box with a PoS
        * [Prerequisites](general/iot/config/pos#prerequisites)
        * [Setup](general/iot/config/pos#setup)
      * HTTPS certificate (IoT)
        * What is HTTPS?
          * [Why is it needed?](general/iot/config/https_certificate_iot#why-is-it-needed)
        * How to obtain a Hypertext Transfer Protocol Secure (HTTPS) certificate
          * [Internet of Things (IoT) eligibility](general/iot/config/https_certificate_iot#internet-of-things-iot-eligibility)
        * Troubleshooting Hypertext Transfer Protocol Secure (HTTPS) certificate errors
          * [`ERR_IOT_HTTPS_CHECK_NO_SERVER`](general/iot/config/https_certificate_iot#err-iot-https-check-no-server)
          * [`ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`](general/iot/config/https_certificate_iot#err-iot-https-check-cert-read-exception)
          * [`ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`](general/iot/config/https_certificate_iot#err-iot-https-load-no-credential)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`](general/iot/config/https_certificate_iot#err-iot-https-load-request-exception)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`](general/iot/config/https_certificate_iot#err-iot-https-load-request-status)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`](general/iot/config/https_certificate_iot#err-iot-https-load-request-no-result)
        * [How to ensure that the HTTPS certificate is correct](general/iot/config/https_certificate_iot#how-to-ensure-that-the-https-certificate-is-correct)
        * Domain Name System (DNS) issue
          * [Domain Name System (DNS) issue solution](general/iot/config/https_certificate_iot#domain-name-system-dns-issue-solution)
      * Updating (IoT)
        * [Flashing the SD card on IoT box](general/iot/config/updating_iot#flashing-the-sd-card-on-iot-box)
        * Windows IoT update
          * [Uninstalling Windows IoT](general/iot/config/updating_iot#uninstalling-windows-iot)
          * [Download and re-install](general/iot/config/updating_iot#download-and-re-install)
          * [Set the destination and complete the installation](general/iot/config/updating_iot#set-the-destination-and-complete-the-installation)
        * [Update from the IoT box home page](general/iot/config/updating_iot#update-from-the-iot-box-home-page)
        * [Handler (driver) update](general/iot/config/updating_iot#handler-driver-update)
      * Troubleshooting
        * IoT box connection
          * [Unable to locate the pairing code to connect the IoT box](general/iot/config/troubleshooting#unable-to-locate-the-pairing-code-to-connect-the-iot-box)
          * [IoT box is connected but it is not showing in the database](general/iot/config/troubleshooting#iot-box-is-connected-but-it-is-not-showing-in-the-database)
          * [The IoT box is connected to the Konvergo ERP database, but cannot be reached](general/iot/config/troubleshooting#the-iot-box-is-connected-to-the-odoo-database-but-cannot-be-reached)
          * [The HTTPS certificate does not generate](general/iot/config/troubleshooting#the-https-certificate-does-not-generate)
        * Printer
          * [The printer is not detected](general/iot/config/troubleshooting#the-printer-is-not-detected)
          * The printer outputs random text
            * Epson configuration special case
              * Process to force ESC * command
                * [Epson printer compatibility](general/iot/config/troubleshooting#epson-printer-compatibility)
                * [IoT box configuration for ESC *](general/iot/config/troubleshooting#iot-box-configuration-for-esc)
          * DYMO LabelWriter print issue
            * [DYMO LabelWriter not printing](general/iot/config/troubleshooting#dymo-labelwriter-not-printing)
            * [DYMO LabelWriter print delay](general/iot/config/troubleshooting#dymo-labelwriter-print-delay)
          * [The Zebra printer does not print anything](general/iot/config/troubleshooting#the-zebra-printer-does-not-print-anything)
        * Barcode scanner
          * [The characters read by the barcode scanner do not match the barcode](general/iot/config/troubleshooting#the-characters-read-by-the-barcode-scanner-do-not-match-the-barcode)
          * [Nothing happens when a barcode is scanned](general/iot/config/troubleshooting#nothing-happens-when-a-barcode-is-scanned)
          * [The barcode scanner is detected as a keyboard](general/iot/config/troubleshooting#the-barcode-scanner-is-detected-as-a-keyboard)
          * [Barcode scanner processes barcode characters individually](general/iot/config/troubleshooting#barcode-scanner-processes-barcode-characters-individually)
        * Cash drawer
          * [The cash drawer does not open](general/iot/config/troubleshooting#the-cash-drawer-does-not-open)
        * Scale
          * Set up Ariva S scales
            * [Cable](general/iot/config/troubleshooting#cable)
            * [Setup](general/iot/config/troubleshooting#setup)
      * Connect Windows IoT Konvergo ERP
        * [Pre-requisites](general/iot/config/windows_iot#pre-requisites)
        * Connect the Windows virtual IoT box to an Konvergo ERP database
          * [Download and initial installation](general/iot/config/windows_iot#download-and-initial-installation)
          * [Setting the destination and completing the installation](general/iot/config/windows_iot#setting-the-destination-and-completing-the-installation)
          * [Connecting devices](general/iot/config/windows_iot#connecting-devices)
        * Troubleshooting
          * [Restart Windows IoT box](general/iot/config/windows_iot#restart-windows-iot-box)
          * Firewalls
            * Making an exception on Windows Defender
              * [Create a rule in Windows Defender](general/iot/config/windows_iot#create-a-rule-in-windows-defender)
              * [Configure new rule](general/iot/config/windows_iot#configure-new-rule)
            * [Worldline exception](general/iot/config/windows_iot#worldline-exception)
          * [Uninstalling Windows IoT](general/iot/config/windows_iot#uninstalling-windows-iot)
    * [Devices](general/iot/devices)
      * Connect a screen
        * [Connection](general/iot/devices/screen#connection)
        * Usage
          * [Show Point of Sale orders to customers](general/iot/devices/screen#show-point-of-sale-orders-to-customers)
          * [Display a website on the screen](general/iot/devices/screen#display-a-website-on-the-screen)
      * Connect a measurement tool
        * [Connect with universal serial bus (USB)](general/iot/devices/measurement_tool#connect-with-universal-serial-bus-usb)
        * [Connect with bluetooth](general/iot/devices/measurement_tool#connect-with-bluetooth)
        * [Link a measurement tool to a quality control point in the manufacturing process](general/iot/devices/measurement_tool#link-a-measurement-tool-to-a-quality-control-point-in-the-manufacturing-process)
        * [Link a measurement tool to a work center in the Manufacturing app](general/iot/devices/measurement_tool#link-a-measurement-tool-to-a-work-center-in-the-manufacturing-app)
      * Connect a camera
        * [Connection](general/iot/devices/camera#connection)
        * [Link camera to quality control point in manufacturing process](general/iot/devices/camera#link-camera-to-quality-control-point-in-manufacturing-process)
        * [Link camera to a work center in the Manufacturing app](general/iot/devices/camera#link-camera-to-a-work-center-in-the-manufacturing-app)
      * Connect a footswitch
        * [Connection](general/iot/devices/footswitch#connection)
        * [Link a footswitch to a work center in the Konvergo ERP Manufacturing app](general/iot/devices/footswitch#link-a-footswitch-to-a-work-center-in-the-odoo-manufacturing-app)
      * Connect a printer
        * [Connection](general/iot/devices/printer#connection)
        * Link printer
          * [Link printer to work orders](general/iot/devices/printer#link-printer-to-work-orders)
          * [Link a printer to a work center in the Manufacturing app](general/iot/devices/printer#link-a-printer-to-a-work-center-in-the-manufacturing-app)
          * [Link printer to reports](general/iot/devices/printer#link-printer-to-reports)
      * Connect a scale
        * [Connection](general/iot/devices/scale#connection)
        * [Use a scale in a point of sale (POS) system](general/iot/devices/scale#use-a-scale-in-a-point-of-sale-pos-system)
  * Email communication
    * Send and receive emails in Konvergo ERP with an email server
      * [Konvergo ERP Online or Konvergo ERP.sh users](general/email_communication/email_servers#odoo-online-or-odoo-sh-users)
      * [Scope of this documentation](general/email_communication/email_servers#scope-of-this-documentation)
      * [Default notifications system](general/email_communication/email_servers#default-notifications-system)
      * Manage outbound messages
        * [Port restriction](general/email_communication/email_servers#port-restriction)
        * [Use a default “From” email address](general/email_communication/email_servers#use-a-default-from-email-address)
        * [Utilizing the “From” filter on an outgoing email server](general/email_communication/email_servers#utilizing-the-from-filter-on-an-outgoing-email-server)
        * [Set up different dedicated servers for transactional and mass emails](general/email_communication/email_servers#set-up-different-dedicated-servers-for-transactional-and-mass-emails)
      * Manage inbound messages
        * [System parameters that prevent feedback loops](general/email_communication/email_servers#system-parameters-that-prevent-feedback-loops)
        * [Allow alias domain system parameter](general/email_communication/email_servers#allow-alias-domain-system-parameter)
    * Configure DNS records to send emails in Konvergo ERP
      * [SPAM labels overview](general/email_communication/email_domain#spam-labels-overview)
      * [Be SPF compliant](general/email_communication/email_domain#be-spf-compliant)
      * [Enable DKIM](general/email_communication/email_domain#enable-dkim)
      * [Check the DMARC policy](general/email_communication/email_domain#check-the-dmarc-policy)
      * [SPF, DKIM & DMARC documentation of common providers](general/email_communication/email_domain#spf-dkim-dmarc-documentation-of-common-providers)
    * Connect Microsoft Outlook 365 to Konvergo ERP using Azure OAuth
      * Setup in Microsoft Azure Portal
        * [Create a new application](general/email_communication/azure_oauth#create-a-new-application)
        * [API permissions](general/email_communication/azure_oauth#api-permissions)
      * Assign users and groups
        * [Create credentials](general/email_communication/azure_oauth#create-credentials)
      * Setup in Konvergo ERP
        * [Enter Microsoft Outlook credentials](general/email_communication/azure_oauth#enter-microsoft-outlook-credentials)
        * Configure outgoing email server
          * [Configuration with a single outgoing mail server](general/email_communication/azure_oauth#configuration-with-a-single-outgoing-mail-server)
          * User-specific (multiple user) configuration
            * [Setup](general/email_communication/azure_oauth#setup)
        * [Configure incoming email server](general/email_communication/azure_oauth#configure-incoming-email-server)
    * Connect Gmail to Konvergo ERP using Google OAuth
      * Setup in Google
        * [Create a new project](general/email_communication/google_oauth#create-a-new-project)
        * [OAuth consent screen](general/email_communication/google_oauth#oauth-consent-screen)
        * [Edit app registration](general/email_communication/google_oauth#edit-app-registration)
        * [Create Credentials](general/email_communication/google_oauth#create-credentials)
      * Setup in Konvergo ERP
        * [Enter Google Credentials](general/email_communication/google_oauth#enter-google-credentials)
        * [Configure outgoing email server](general/email_communication/google_oauth#configure-outgoing-email-server)
      * Google OAuth FAQ
        * [Production VS Testing Publishing Status](general/email_communication/google_oauth#production-vs-testing-publishing-status)
        * [No Test Users Added](general/email_communication/google_oauth#no-test-users-added)
        * [Gmail Module not updated](general/email_communication/google_oauth#gmail-module-not-updated)
        * [Application Type](general/email_communication/google_oauth#application-type)
    * Mailjet API
      * Set up in Mailjet
        * [Create API credentials](general/email_communication/mailjet_api#create-api-credentials)
        * [Add verified sender address(es)](general/email_communication/mailjet_api#add-verified-sender-address-es)
        * Add a domain
          * [Setup in the domain’s DNS](general/email_communication/mailjet_api#setup-in-the-domain-s-dns)
          * [Return to Mailjet account information](general/email_communication/mailjet_api#return-to-mailjet-account-information)
      * [Set up in Konvergo ERP](general/email_communication/mailjet_api#set-up-in-odoo)
    * Email issues
      * Outgoing emails
        * Email is not sent
          * Common error messages
            * [Daily limit reached](general/email_communication/faq#daily-limit-reached)
            * SMTP error
              * [No error populated](general/email_communication/faq#no-error-populated)
        * [Email is sent late](general/email_communication/faq#email-is-sent-late)
      * Incoming emails
        * [Email is not received](general/email_communication/faq#email-is-not-received)
      * [Get help from Konvergo ERP support](general/email_communication/faq#get-help-from-odoo-support)
  * Integrations
    * [Mail Plugins](general/integrations/mail_plugins)
      * Outlook Plugin
        * Configuration
          * [Enable Mail Plugin](general/integrations/mail_plugins/outlook#enable-mail-plugin)
          * [Install the Outlook Plugin](general/integrations/mail_plugins/outlook#install-the-outlook-plugin)
          * [Connect the database](general/integrations/mail_plugins/outlook#connect-the-database)
          * [Add a shortcut to the plugin](general/integrations/mail_plugins/outlook#add-a-shortcut-to-the-plugin)
          * [Using the plugin](general/integrations/mail_plugins/outlook#using-the-plugin)
      * Gmail Plugin
        * Konvergo ERP Online users
          * [Install the Gmail Plugin](general/integrations/mail_plugins/gmail#install-the-gmail-plugin)
          * [Configure the Konvergo ERP database](general/integrations/mail_plugins/gmail#configure-the-odoo-database)
          * [Configure the Gmail inbox](general/integrations/mail_plugins/gmail#configure-the-gmail-inbox)
        * Konvergo ERP On-Premise users
          * [Install the Gmail Plugin](general/integrations/mail_plugins/gmail#id1)
          * [Configure the Konvergo ERP database](general/integrations/mail_plugins/gmail#id2)
          * [Configure the Gmail inbox](general/integrations/mail_plugins/gmail#id3)
      * Pricing
        * [Lead Generation IAP service](general/integrations/mail_plugins#lead-generation-iap-service)
    * [Unsplash](general/integrations/unsplash)
    * [Geolocation](general/integrations/geolocation)
  * Developer mode (debug mode)
    * [Activation](general/developer_mode#activation)
    * [Developer tools and technical menu](general/developer_mode#developer-tools-and-technical-menu)

