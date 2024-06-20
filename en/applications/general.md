# General settings

  * Apps and modules
    * [Install apps and modules](general/apps_modules.html#install-apps-and-modules)
    * [Upgrade apps and modules](general/apps_modules.html#upgrade-apps-and-modules)
    * [Uninstall apps and modules](general/apps_modules.html#uninstall-apps-and-modules)
  * [Users](general/users.html)
    * Add individual users
      * [User type](general/users.html#user-type)
    * Deactivate users
      * [Error: too many users](general/users.html#error-too-many-users)
    * Password management
      * Reset password
        * [Enable password reset from login page](general/users.html#enable-password-reset-from-login-page)
        * [Send reset instructions](general/users.html#send-reset-instructions)
      * [Change user password](general/users.html#change-user-password)
    * Multi Companies
      * Change language
        * [Load your desired language](general/users/language.html#load-your-desired-language)
        * [Change your language](general/users/language.html#change-your-language)
        * [Change another user’s language](general/users/language.html#change-another-user-s-language)
      * Two-factor Authentication
        * [Requirements](general/users/2fa.html#requirements)
        * [Setting up two-factor authentication](general/users/2fa.html#setting-up-two-factor-authentication)
        * [Logging in](general/users/2fa.html#logging-in)
      * Access rights
        * [Users](general/users/access_rights.html#users)
        * [Create and modify groups](general/users/access_rights.html#create-and-modify-groups)
        * [Superuser mode](general/users/access_rights.html#superuser-mode)
      * Portal access
        * [Provide portal access to customers](general/users/portal.html#provide-portal-access-to-customers)
        * [Change portal username](general/users/portal.html#change-portal-username)
        * Customer portal changes
          * [Change customer info](general/users/portal.html#change-customer-info)
          * [Change password](general/users/portal.html#change-password)
          * [Add two-factor authentication](general/users/portal.html#add-two-factor-authentication)
          * [Change payment info](general/users/portal.html#change-payment-info)
      * Google Sign-In Authentication
        * Configuration
          * Google API Dashboard
            * [OAuth consent screen](general/users/google.html#oauth-consent-screen)
            * [Credentials](general/users/google.html#credentials)
          * Google Authentication on Odoo
            * [Retrieve the Client ID](general/users/google.html#retrieve-the-client-id)
            * [Odoo activation](general/users/google.html#odoo-activation)
        * [Log in to Odoo with Google](general/users/google.html#log-in-to-odoo-with-google)
      * Microsoft Azure sign-in authentication
        * Configuration
          * [Odoo System Parameter](general/users/azure.html#odoo-system-parameter)
          * Microsoft Azure dashboard
            * [Create a new application](general/users/azure.html#create-a-new-application)
            * [Authentication](general/users/azure.html#authentication)
            * [Gather credentials](general/users/azure.html#gather-credentials)
          * [Odoo setup](general/users/azure.html#odoo-setup)
          * [User experience flows](general/users/azure.html#user-experience-flows)
      * [Sign in with LDAP](general/users/ldap.html)
  * [Companies](general/companies.html)
    * [Manage companies and records](general/companies.html#manage-companies-and-records)
    * [Employees’ access](general/companies.html#employees-access)
    * [Documents’ format](general/companies.html#documents-format)
    * Inter-Company Transactions
      * Digest emails
        * [Customize default digest email](general/companies/digest_emails.html#customize-default-digest-email)
        * [Deactivate digest email](general/companies/digest_emails.html#deactivate-digest-email)
        * [Manually send digest email](general/companies/digest_emails.html#manually-send-digest-email)
        * [KPIs](general/companies/digest_emails.html#kpis)
        * [Recipients](general/companies/digest_emails.html#recipients)
        * [Create digest emails](general/companies/digest_emails.html#create-digest-emails)
        * Custom KPIs with Odoo Studio
          * [Computed values reference table](general/companies/digest_emails.html#computed-values-reference-table)
      * Email templates
        * Editing email templates
          * [Powerbox](general/companies/email_template.html#powerbox)
          * [XML/HTML code editor](general/companies/email_template.html#xml-html-code-editor)
          * [Dynamic placeholders](general/companies/email_template.html#dynamic-placeholders)
          * [Rich text editor](general/companies/email_template.html#rich-text-editor)
          * [Resetting email templates](general/companies/email_template.html#resetting-email-templates)
          * [Default reply on email templates](general/companies/email_template.html#default-reply-on-email-templates)
        * Transactional emails and corresponding URLs
          * [Updating translations within email templates](general/companies/email_template.html#updating-translations-within-email-templates)
  * [Internet of Things (IoT)](general/iot.html)
    * Configuration
      * Connect an IoT box to Odoo
        * [Ethernet connection](general/iot/config/connect.html#ethernet-connection)
        * [WiFi connection](general/iot/config/connect.html#wifi-connection)
        * [Manually connecting the IoT box using the token](general/iot/config/connect.html#manually-connecting-the-iot-box-using-the-token)
        * IoT box schema
          * [Raspberry Pi 4](general/iot/config/connect.html#raspberry-pi-4)
          * [Raspberry Pi 3](general/iot/config/connect.html#raspberry-pi-3)
      * Use an IoT box with a PoS
        * [Prerequisites](general/iot/config/pos.html#prerequisites)
        * [Setup](general/iot/config/pos.html#setup)
      * HTTPS certificate (IoT)
        * What is HTTPS?
          * [Why is it needed?](general/iot/config/https_certificate_iot.html#why-is-it-needed)
        * How to obtain a Hypertext Transfer Protocol Secure (HTTPS) certificate
          * [Internet of Things (IoT) eligibility](general/iot/config/https_certificate_iot.html#internet-of-things-iot-eligibility)
        * Troubleshooting Hypertext Transfer Protocol Secure (HTTPS) certificate errors
          * [`ERR_IOT_HTTPS_CHECK_NO_SERVER`](general/iot/config/https_certificate_iot.html#err-iot-https-check-no-server)
          * [`ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-check-cert-read-exception)
          * [`ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`](general/iot/config/https_certificate_iot.html#err-iot-https-load-no-credential)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-exception)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-status)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-no-result)
        * [How to ensure that the HTTPS certificate is correct](general/iot/config/https_certificate_iot.html#how-to-ensure-that-the-https-certificate-is-correct)
        * Domain Name System (DNS) issue
          * [Domain Name System (DNS) issue solution](general/iot/config/https_certificate_iot.html#domain-name-system-dns-issue-solution)
      * Updating (IoT)
        * [Flashing the SD card on IoT box](general/iot/config/updating_iot.html#flashing-the-sd-card-on-iot-box)
        * Windows IoT update
          * [Uninstalling Windows IoT](general/iot/config/updating_iot.html#uninstalling-windows-iot)
          * [Download and re-install](general/iot/config/updating_iot.html#download-and-re-install)
          * [Set the destination and complete the installation](general/iot/config/updating_iot.html#set-the-destination-and-complete-the-installation)
        * [Update from the IoT box home page](general/iot/config/updating_iot.html#update-from-the-iot-box-home-page)
        * [Handler (driver) update](general/iot/config/updating_iot.html#handler-driver-update)
      * Troubleshooting
        * IoT box connection
          * [Unable to locate the pairing code to connect the IoT box](general/iot/config/troubleshooting.html#unable-to-locate-the-pairing-code-to-connect-the-iot-box)
          * [IoT box is connected but it is not showing in the database](general/iot/config/troubleshooting.html#iot-box-is-connected-but-it-is-not-showing-in-the-database)
          * [The IoT box is connected to the Odoo database, but cannot be reached](general/iot/config/troubleshooting.html#the-iot-box-is-connected-to-the-odoo-database-but-cannot-be-reached)
          * [The HTTPS certificate does not generate](general/iot/config/troubleshooting.html#the-https-certificate-does-not-generate)
        * Printer
          * [The printer is not detected](general/iot/config/troubleshooting.html#the-printer-is-not-detected)
          * The printer outputs random text
            * Epson configuration special case
              * Process to force ESC * command
                * [Epson printer compatibility](general/iot/config/troubleshooting.html#epson-printer-compatibility)
                * [IoT box configuration for ESC *](general/iot/config/troubleshooting.html#iot-box-configuration-for-esc)
          * DYMO LabelWriter print issue
            * [DYMO LabelWriter not printing](general/iot/config/troubleshooting.html#dymo-labelwriter-not-printing)
            * [DYMO LabelWriter print delay](general/iot/config/troubleshooting.html#dymo-labelwriter-print-delay)
          * [The Zebra printer does not print anything](general/iot/config/troubleshooting.html#the-zebra-printer-does-not-print-anything)
        * Barcode scanner
          * [The characters read by the barcode scanner do not match the barcode](general/iot/config/troubleshooting.html#the-characters-read-by-the-barcode-scanner-do-not-match-the-barcode)
          * [Nothing happens when a barcode is scanned](general/iot/config/troubleshooting.html#nothing-happens-when-a-barcode-is-scanned)
          * [The barcode scanner is detected as a keyboard](general/iot/config/troubleshooting.html#the-barcode-scanner-is-detected-as-a-keyboard)
          * [Barcode scanner processes barcode characters individually](general/iot/config/troubleshooting.html#barcode-scanner-processes-barcode-characters-individually)
        * Cash drawer
          * [The cash drawer does not open](general/iot/config/troubleshooting.html#the-cash-drawer-does-not-open)
        * Scale
          * Set up Ariva S scales
            * [Cable](general/iot/config/troubleshooting.html#cable)
            * [Setup](general/iot/config/troubleshooting.html#setup)
      * Connect Windows IoT Odoo
        * [Pre-requisites](general/iot/config/windows_iot.html#pre-requisites)
        * Connect the Windows virtual IoT box to an Odoo database
          * [Download and initial installation](general/iot/config/windows_iot.html#download-and-initial-installation)
          * [Setting the destination and completing the installation](general/iot/config/windows_iot.html#setting-the-destination-and-completing-the-installation)
          * [Connecting devices](general/iot/config/windows_iot.html#connecting-devices)
        * Troubleshooting
          * [Restart Windows IoT box](general/iot/config/windows_iot.html#restart-windows-iot-box)
          * Firewalls
            * Making an exception on Windows Defender
              * [Create a rule in Windows Defender](general/iot/config/windows_iot.html#create-a-rule-in-windows-defender)
              * [Configure new rule](general/iot/config/windows_iot.html#configure-new-rule)
            * [Worldline exception](general/iot/config/windows_iot.html#worldline-exception)
          * [Uninstalling Windows IoT](general/iot/config/windows_iot.html#uninstalling-windows-iot)
    * [Devices](general/iot/devices.html)
      * Connect a screen
        * [Connection](general/iot/devices/screen.html#connection)
        * Usage
          * [Show Point of Sale orders to customers](general/iot/devices/screen.html#show-point-of-sale-orders-to-customers)
          * [Display a website on the screen](general/iot/devices/screen.html#display-a-website-on-the-screen)
      * Connect a measurement tool
        * [Connect with universal serial bus (USB)](general/iot/devices/measurement_tool.html#connect-with-universal-serial-bus-usb)
        * [Connect with bluetooth](general/iot/devices/measurement_tool.html#connect-with-bluetooth)
        * [Link a measurement tool to a quality control point in the manufacturing process](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-quality-control-point-in-the-manufacturing-process)
        * [Link a measurement tool to a work center in the Manufacturing app](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-work-center-in-the-manufacturing-app)
      * Connect a camera
        * [Connection](general/iot/devices/camera.html#connection)
        * [Link camera to quality control point in manufacturing process](general/iot/devices/camera.html#link-camera-to-quality-control-point-in-manufacturing-process)
        * [Link camera to a work center in the Manufacturing app](general/iot/devices/camera.html#link-camera-to-a-work-center-in-the-manufacturing-app)
      * Connect a footswitch
        * [Connection](general/iot/devices/footswitch.html#connection)
        * [Link a footswitch to a work center in the Odoo Manufacturing app](general/iot/devices/footswitch.html#link-a-footswitch-to-a-work-center-in-the-odoo-manufacturing-app)
      * Connect a printer
        * [Connection](general/iot/devices/printer.html#connection)
        * Link printer
          * [Link printer to work orders](general/iot/devices/printer.html#link-printer-to-work-orders)
          * [Link a printer to a work center in the Manufacturing app](general/iot/devices/printer.html#link-a-printer-to-a-work-center-in-the-manufacturing-app)
          * [Link printer to reports](general/iot/devices/printer.html#link-printer-to-reports)
      * Connect a scale
        * [Connection](general/iot/devices/scale.html#connection)
        * [Use a scale in a point of sale (POS) system](general/iot/devices/scale.html#use-a-scale-in-a-point-of-sale-pos-system)
  * Email communication
    * Send and receive emails in Odoo with an email server
      * [Odoo Online or Odoo.sh users](general/email_communication/email_servers.html#odoo-online-or-odoo-sh-users)
      * [Scope of this documentation](general/email_communication/email_servers.html#scope-of-this-documentation)
      * [Default notifications system](general/email_communication/email_servers.html#default-notifications-system)
      * Manage outbound messages
        * [Port restriction](general/email_communication/email_servers.html#port-restriction)
        * [Use a default “From” email address](general/email_communication/email_servers.html#use-a-default-from-email-address)
        * [Utilizing the “From” filter on an outgoing email server](general/email_communication/email_servers.html#utilizing-the-from-filter-on-an-outgoing-email-server)
        * [Set up different dedicated servers for transactional and mass emails](general/email_communication/email_servers.html#set-up-different-dedicated-servers-for-transactional-and-mass-emails)
      * Manage inbound messages
        * [System parameters that prevent feedback loops](general/email_communication/email_servers.html#system-parameters-that-prevent-feedback-loops)
        * [Allow alias domain system parameter](general/email_communication/email_servers.html#allow-alias-domain-system-parameter)
    * Configure DNS records to send emails in Odoo
      * [SPAM labels overview](general/email_communication/email_domain.html#spam-labels-overview)
      * [Be SPF compliant](general/email_communication/email_domain.html#be-spf-compliant)
      * [Enable DKIM](general/email_communication/email_domain.html#enable-dkim)
      * [Check the DMARC policy](general/email_communication/email_domain.html#check-the-dmarc-policy)
      * [SPF, DKIM & DMARC documentation of common providers](general/email_communication/email_domain.html#spf-dkim-dmarc-documentation-of-common-providers)
    * Connect Microsoft Outlook 365 to Odoo using Azure OAuth
      * Setup in Microsoft Azure Portal
        * [Create a new application](general/email_communication/azure_oauth.html#create-a-new-application)
        * [API permissions](general/email_communication/azure_oauth.html#api-permissions)
      * Assign users and groups
        * [Create credentials](general/email_communication/azure_oauth.html#create-credentials)
      * Setup in Odoo
        * [Enter Microsoft Outlook credentials](general/email_communication/azure_oauth.html#enter-microsoft-outlook-credentials)
        * Configure outgoing email server
          * [Configuration with a single outgoing mail server](general/email_communication/azure_oauth.html#configuration-with-a-single-outgoing-mail-server)
          * User-specific (multiple user) configuration
            * [Setup](general/email_communication/azure_oauth.html#setup)
        * [Configure incoming email server](general/email_communication/azure_oauth.html#configure-incoming-email-server)
    * Connect Gmail to Odoo using Google OAuth
      * Setup in Google
        * [Create a new project](general/email_communication/google_oauth.html#create-a-new-project)
        * [OAuth consent screen](general/email_communication/google_oauth.html#oauth-consent-screen)
        * [Edit app registration](general/email_communication/google_oauth.html#edit-app-registration)
        * [Create Credentials](general/email_communication/google_oauth.html#create-credentials)
      * Setup in Odoo
        * [Enter Google Credentials](general/email_communication/google_oauth.html#enter-google-credentials)
        * [Configure outgoing email server](general/email_communication/google_oauth.html#configure-outgoing-email-server)
      * Google OAuth FAQ
        * [Production VS Testing Publishing Status](general/email_communication/google_oauth.html#production-vs-testing-publishing-status)
        * [No Test Users Added](general/email_communication/google_oauth.html#no-test-users-added)
        * [Gmail Module not updated](general/email_communication/google_oauth.html#gmail-module-not-updated)
        * [Application Type](general/email_communication/google_oauth.html#application-type)
    * Mailjet API
      * Set up in Mailjet
        * [Create API credentials](general/email_communication/mailjet_api.html#create-api-credentials)
        * [Add verified sender address(es)](general/email_communication/mailjet_api.html#add-verified-sender-address-es)
        * Add a domain
          * [Setup in the domain’s DNS](general/email_communication/mailjet_api.html#setup-in-the-domain-s-dns)
          * [Return to Mailjet account information](general/email_communication/mailjet_api.html#return-to-mailjet-account-information)
      * [Set up in Odoo](general/email_communication/mailjet_api.html#set-up-in-odoo)
    * Email issues
      * Outgoing emails
        * Email is not sent
          * Common error messages
            * [Daily limit reached](general/email_communication/faq.html#daily-limit-reached)
            * SMTP error
              * [No error populated](general/email_communication/faq.html#no-error-populated)
        * [Email is sent late](general/email_communication/faq.html#email-is-sent-late)
      * Incoming emails
        * [Email is not received](general/email_communication/faq.html#email-is-not-received)
      * [Get help from Odoo support](general/email_communication/faq.html#get-help-from-odoo-support)
  * Integrations
    * [Mail Plugins](general/integrations/mail_plugins.html)
      * Outlook Plugin
        * Configuration
          * [Enable Mail Plugin](general/integrations/mail_plugins/outlook.html#enable-mail-plugin)
          * [Install the Outlook Plugin](general/integrations/mail_plugins/outlook.html#install-the-outlook-plugin)
          * [Connect the database](general/integrations/mail_plugins/outlook.html#connect-the-database)
          * [Add a shortcut to the plugin](general/integrations/mail_plugins/outlook.html#add-a-shortcut-to-the-plugin)
          * [Using the plugin](general/integrations/mail_plugins/outlook.html#using-the-plugin)
      * Gmail Plugin
        * Odoo Online users
          * [Install the Gmail Plugin](general/integrations/mail_plugins/gmail.html#install-the-gmail-plugin)
          * [Configure the Odoo database](general/integrations/mail_plugins/gmail.html#configure-the-odoo-database)
          * [Configure the Gmail inbox](general/integrations/mail_plugins/gmail.html#configure-the-gmail-inbox)
        * Odoo On-Premise users
          * [Install the Gmail Plugin](general/integrations/mail_plugins/gmail.html#id1)
          * [Configure the Odoo database](general/integrations/mail_plugins/gmail.html#id2)
          * [Configure the Gmail inbox](general/integrations/mail_plugins/gmail.html#id3)
      * Pricing
        * [Lead Generation IAP service](general/integrations/mail_plugins.html#lead-generation-iap-service)
    * [Unsplash](general/integrations/unsplash.html)
    * [Geolocation](general/integrations/geolocation.html)
  * Developer mode (debug mode)
    * [Activation](general/developer_mode.html#activation)
    * [Developer tools and technical menu](general/developer_mode.html#developer-tools-and-technical-menu)

