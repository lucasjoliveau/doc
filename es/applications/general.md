# Ajustes generales

  * Aplicaciones y módulos
    * [Instale aplicaciones y módulos](general/apps_modules.html#install-apps-and-modules)
    * [Actualice aplicaciones y módulos](general/apps_modules.html#upgrade-apps-and-modules)
    * [Desinstale aplicaciones y módulos](general/apps_modules.html#uninstall-apps-and-modules)
  * [Usuarios](general/users.html)
    * Agregar usuarios individuales
      * [Tipo de usuario](general/users.html#user-type)
    * Desactivar usuarios
      * [Error: demasiados usuarios](general/users.html#error-too-many-users)
    * Gestión de contraseñas
      * Restablecer contraseña
        * [Habilitar restablecimiento de la contraseña desde la página de inicio de sesión](general/users.html#enable-password-reset-from-login-page)
        * [Enviar instrucciones de restablecimiento](general/users.html#send-reset-instructions)
      * [Cambiar la contraseña del usuario](general/users.html#change-user-password)
    * Multiempresas
      * Cambiar idioma
        * [Descargue el idioma deseado](general/users/language.html#load-your-desired-language)
        * [Cambiar idioma](general/users/language.html#change-your-language)
        * [Cambiar el idioma de otro usuario](general/users/language.html#change-another-user-s-language)
      * Autenticación en dos pasos
        * [Requisitos](general/users/2fa.html#requirements)
        * [Configurar la autenticación de dos pasos](general/users/2fa.html#setting-up-two-factor-authentication)
        * [Iniciar sesión](general/users/2fa.html#logging-in)
      * Permisos de acceso
        * [Usuarios](general/users/access_rights.html#users)
        * [Crear y modificar grupos](general/users/access_rights.html#create-and-modify-groups)
        * [Modo de superusuario](general/users/access_rights.html#superuser-mode)
      * Acceso al portal
        * [Otorgar acceso al portal a sus clientes](general/users/portal.html#provide-portal-access-to-customers)
        * [Cambiar el nombre de usuario del portal](general/users/portal.html#change-portal-username)
        * Cambios en el portal del cliente
          * [Cambiar la información del cliente](general/users/portal.html#change-customer-info)
          * [Cambiar contraseña](general/users/portal.html#change-password)
          * [Agregar autenticación de dos factores](general/users/portal.html#add-two-factor-authentication)
          * [Cambiar información de pago](general/users/portal.html#change-payment-info)
      * Autenticación de inicio de sesión de Google
        * Configuración
          * Tablero de la API de Google
            * [OAuth pantalla de consentimiento](general/users/google.html#oauth-consent-screen)
            * [Credenciales](general/users/google.html#credentials)
          * Autenticaciión de Google en Odoo
            * [Recuperar el ID del cliente](general/users/google.html#retrieve-the-client-id)
            * [Activación de Odoo](general/users/google.html#odoo-activation)
        * [Inicie sesión en Odoo con Google](general/users/google.html#log-in-to-odoo-with-google)
      * Autenticación de inicio de sesión de Microsoft Azure
        * Configuración
          * [Parámetros del sistema de Odoo](general/users/azure.html#odoo-system-parameter)
          * Tablero de Microsoft Azure
            * [Crear una nueva aplicación](general/users/azure.html#create-a-new-application)
            * [Autentificación](general/users/azure.html#authentication)
            * [Obtener las credenciales](general/users/azure.html#gather-credentials)
          * [Configuración en Odoo](general/users/azure.html#odoo-setup)
          * [Flujos de experiencia del usuario](general/users/azure.html#user-experience-flows)
      * [Inicie sesión con LDAP](general/users/ldap.html)
  * [Empresas](general/companies.html)
    * [Gestionar empresas y registros](general/companies.html#manage-companies-and-records)
    * [Acceso de empleados](general/companies.html#employees-access)
    * [Formato de los documentos](general/companies.html#documents-format)
    * Transacciones dentro de la empresa
      * Correos electrónicos de resumen
        * [Personalizar correos electrónicos de resumen](general/companies/digest_emails.html#customize-default-digest-email)
        * [Desactivar el correo de resumen](general/companies/digest_emails.html#deactivate-digest-email)
        * [Enviar el correo de resumen de forma manual](general/companies/digest_emails.html#manually-send-digest-email)
        * [KPIs](general/companies/digest_emails.html#kpis)
        * [Destinatarios](general/companies/digest_emails.html#recipients)
        * [Crear correos electrónicos de resumen](general/companies/digest_emails.html#create-digest-emails)
        * KPI personalizados con Studio
          * [Tabla de referencia de los valores calculados](general/companies/digest_emails.html#computed-values-reference-table)
      * Plantillas de correo electrónico
        * Editar las plantillas de correo electrónico
          * [Paleta de comandos](general/companies/email_template.html#powerbox)
          * [Editor de código XML/HTML](general/companies/email_template.html#xml-html-code-editor)
          * [Marcadores de posición dinámicos](general/companies/email_template.html#dynamic-placeholders)
          * [Editor de texto enriquecido](general/companies/email_template.html#rich-text-editor)
          * [Restablecer plantillas de correo electrónico](general/companies/email_template.html#resetting-email-templates)
          * [Respuesta predeterminada en las plantillas de correo electrónico](general/companies/email_template.html#default-reply-on-email-templates)
        * Correos electrónicos transaccionales y URLs correspondientes
          * [Actualizar traducciones en plantillas de correos electrónicos](general/companies/email_template.html#updating-translations-within-email-templates)
  * [Internet de las cosas (IoT)](general/iot.html)
    * Configuración
      * Conectar una caja IoT a Odoo
        * [Conexión ethernet](general/iot/config/connect.html#ethernet-connection)
        * [Conexión wifi](general/iot/config/connect.html#wifi-connection)
        * [Conectar la caja IoT de forma manual utilizando el token](general/iot/config/connect.html#manually-connecting-the-iot-box-using-the-token)
        * Diagrama de la caja IoT
          * [Raspberry Pi 4](general/iot/config/connect.html#raspberry-pi-4)
          * [Raspberry Pi 3](general/iot/config/connect.html#raspberry-pi-3)
      * Utilizar una caja IoT con un PdV
        * [Prerrequisitos](general/iot/config/pos.html#prerequisites)
        * [Configurar](general/iot/config/pos.html#setup)
      * Certificado HTTPS (IoT)
        * ¿Qué es HTTPS?
          * [¿Por qué es necesario?](general/iot/config/https_certificate_iot.html#why-is-it-needed)
        * Cómo obtener un certificado de protocolo seguro de transferencia de hipertexto (HTTPS)
          * [Criterios de elegibilidad para IoT](general/iot/config/https_certificate_iot.html#internet-of-things-iot-eligibility)
        * Solución de errores de certificado del Protocolo seguro de transferencia de hipertexto (HTTPS)
          * [`ERR_IOT_HTTPS_CHECK_NO_SERVER`](general/iot/config/https_certificate_iot.html#err-iot-https-check-no-server)
          * [`ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-check-cert-read-exception)
          * [`ERR_IOT_HTTPS_LOAD_NO_CREDENTIAL`](general/iot/config/https_certificate_iot.html#err-iot-https-load-no-credential)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_EXCEPTION`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-exception)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_STATUS`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-status)
          * [`ERR_IOT_HTTPS_LOAD_REQUEST_NO_RESULT`](general/iot/config/https_certificate_iot.html#err-iot-https-load-request-no-result)
        * [Cómo asegurarse de que el certificado HTTPS es correcto](general/iot/config/https_certificate_iot.html#how-to-ensure-that-the-https-certificate-is-correct)
        * Errores del sistema de nombres de dominio (DNS)
          * [Solución de errores del sistema de nombres de dominio (DNS)](general/iot/config/https_certificate_iot.html#domain-name-system-dns-issue-solution)
      * Actualizar (IoT)
        * [Actualizar la memoria SD en la caja IoT](general/iot/config/updating_iot.html#flashing-the-sd-card-on-iot-box)
        * Actualización de la caja IoT de Windows
          * [Desinstalar Windows IoT](general/iot/config/updating_iot.html#uninstalling-windows-iot)
          * [Descargar y volver a instalar](general/iot/config/updating_iot.html#download-and-re-install)
          * [Seleccionar una carpeta de destino y completar la instalación](general/iot/config/updating_iot.html#set-the-destination-and-complete-the-installation)
        * [Actualizar desde la página de inicio de la caja IoT](general/iot/config/updating_iot.html#update-from-the-iot-box-home-page)
        * [Actualización de controlador (driver)](general/iot/config/updating_iot.html#handler-driver-update)
      * Solución de problemas
        * Conexión de la caja IoT
          * [No es posible localizar el código de emparejamiento para conectar la caja IoT](general/iot/config/troubleshooting.html#unable-to-locate-the-pairing-code-to-connect-the-iot-box)
          * [La caja IoT está conectada pero no aparece en la base de datos](general/iot/config/troubleshooting.html#iot-box-is-connected-but-it-is-not-showing-in-the-database)
          * [La caja IoT está conectada a la base de datos de Odoo pero no puede localizarla](general/iot/config/troubleshooting.html#the-iot-box-is-connected-to-the-odoo-database-but-cannot-be-reached)
          * [No se genera el certificado HTTPS](general/iot/config/troubleshooting.html#the-https-certificate-does-not-generate)
        * Impresora
          * [No se detecta la impresora](general/iot/config/troubleshooting.html#the-printer-is-not-detected)
          * La impresora imprime texto aleatorio
            * Caso especial de uso de Epson
              * Proceso para forzar el comando ESC*
                * [Compatibilidad de la impresora Epson](general/iot/config/troubleshooting.html#epson-printer-compatibility)
                * [configuración de la caja IoT para ESC*](general/iot/config/troubleshooting.html#iot-box-configuration-for-esc)
          * Problemas con la impresora DYMO LabelWriter
            * [DYMO LabelWriter no está imprimiendo](general/iot/config/troubleshooting.html#dymo-labelwriter-not-printing)
            * [Retraso de impresión en DYMO LabelWriter](general/iot/config/troubleshooting.html#dymo-labelwriter-print-delay)
          * [La impresora Zebra no imprime nada](general/iot/config/troubleshooting.html#the-zebra-printer-does-not-print-anything)
        * Lector de código de barras
          * [El lector de códigos de barras lee caracteres que no coinciden con el código de barras](general/iot/config/troubleshooting.html#the-characters-read-by-the-barcode-scanner-do-not-match-the-barcode)
          * [No ocurre nada al escanear un código de barras](general/iot/config/troubleshooting.html#nothing-happens-when-a-barcode-is-scanned)
          * [El lector de códigos de barras se detecta como un teclado](general/iot/config/troubleshooting.html#the-barcode-scanner-is-detected-as-a-keyboard)
          * [El lector de código de barras procesa los caracteres del código de barras de forma individual](general/iot/config/troubleshooting.html#barcode-scanner-processes-barcode-characters-individually)
        * Caja registradora
          * [La caja registradora no abre](general/iot/config/troubleshooting.html#the-cash-drawer-does-not-open)
        * Báscula
          * Configuración de las básculas Ariva S
            * [Cable](general/iot/config/troubleshooting.html#cable)
            * [Configurar](general/iot/config/troubleshooting.html#setup)
      * Conectar Windows IoT a Odoo
        * [Requisitos previos](general/iot/config/windows_iot.html#pre-requisites)
        * Conectar la caja virtual IoT de Windows a una base de datos de Odoo
          * [Descarga e instalación inicial](general/iot/config/windows_iot.html#download-and-initial-installation)
          * [Seleccionar una carpeta de destino y completar la instalación](general/iot/config/windows_iot.html#setting-the-destination-and-completing-the-installation)
          * [Conectar dispositivos](general/iot/config/windows_iot.html#connecting-devices)
        * Solución de problemas
          * [Reiniciar la caja IoT de Windows](general/iot/config/windows_iot.html#restart-windows-iot-box)
          * Firewalls
            * Hacer una excepción en Windows Defender
              * [Crear una regla en Windows Defender](general/iot/config/windows_iot.html#create-a-rule-in-windows-defender)
              * [Configurar una nueva regla](general/iot/config/windows_iot.html#configure-new-rule)
            * [Excepción para Worldline](general/iot/config/windows_iot.html#worldline-exception)
          * [Desinstalar Windows IoT](general/iot/config/windows_iot.html#uninstalling-windows-iot)
    * [Dispositivos](general/iot/devices.html)
      * Conectar una pantalla
        * [Conexión](general/iot/devices/screen.html#connection)
        * Uso
          * [Mostrar órdenes del Punto de Venta a los clientes](general/iot/devices/screen.html#show-point-of-sale-orders-to-customers)
          * [Mostrar un sitio web en la pantalla](general/iot/devices/screen.html#display-a-website-on-the-screen)
      * Conectar una herramienta de medición
        * [Conectar con una USB](general/iot/devices/measurement_tool.html#connect-with-universal-serial-bus-usb)
        * [Conectar con Bluetooth](general/iot/devices/measurement_tool.html#connect-with-bluetooth)
        * [Vincule una herramienta de medición a un punto de control de calidad en el proceso de fabricación](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-quality-control-point-in-the-manufacturing-process)
        * [Vincular una herramienta de medición a un centro de trabajo en la aplicación Fabricación](general/iot/devices/measurement_tool.html#link-a-measurement-tool-to-a-work-center-in-the-manufacturing-app)
      * Conectar una cámara
        * [Conexión](general/iot/devices/camera.html#connection)
        * [Vincular una cámara al punto de control de calidad de un proceso de fabricación](general/iot/devices/camera.html#link-camera-to-quality-control-point-in-manufacturing-process)
        * [Vincular una cámara a un centro de trabajo en la aplicación Fabricación](general/iot/devices/camera.html#link-camera-to-a-work-center-in-the-manufacturing-app)
      * Conectar un pedal
        * [Conexión](general/iot/devices/footswitch.html#connection)
        * [Vincule un interruptor a un centro de trabajo en la aplicación Fabricación de Odoo](general/iot/devices/footswitch.html#link-a-footswitch-to-a-work-center-in-the-odoo-manufacturing-app)
      * Conectar una impresora
        * [Conexión](general/iot/devices/printer.html#connection)
        * Vincular una impresora
          * [Vincular una impresora a las órdenes de trabajo](general/iot/devices/printer.html#link-printer-to-work-orders)
          * [Vincule una impresora a un centro de trabajo en la aplicación Fabricación](general/iot/devices/printer.html#link-a-printer-to-a-work-center-in-the-manufacturing-app)
          * [Vincular impresora a los reportes](general/iot/devices/printer.html#link-printer-to-reports)
      * Conectar una báscula
        * [Conexión](general/iot/devices/scale.html#connection)
        * [Usar una báscula en el sistema del punto de venta (PdV)](general/iot/devices/scale.html#use-a-scale-in-a-point-of-sale-pos-system)
  * Comunicación por correo electrónico
    * Enviar y recibir correos electrónicos en Odoo con un servidor de correo electrónico
      * [Usuarios de Odoo en línea o Odoo.sh](general/email_communication/email_servers.html#odoo-online-or-odoo-sh-users)
      * [Alcance de esta documentación](general/email_communication/email_servers.html#scope-of-this-documentation)
      * [Notificaciones predeterminadas del sistema](general/email_communication/email_servers.html#default-notifications-system)
      * Gestionar mensajes salientes
        * [Restricción del puerto](general/email_communication/email_servers.html#port-restriction)
        * [Utilizar una dirección de correo electrónico «De» predeterminada](general/email_communication/email_servers.html#use-a-default-from-email-address)
        * [Utilizar el filtro «De» en un servidor de correo electrónico saliente](general/email_communication/email_servers.html#utilizing-the-from-filter-on-an-outgoing-email-server)
        * [Configurar distintos servidores dedicados para correos masivos y transaccionales](general/email_communication/email_servers.html#set-up-different-dedicated-servers-for-transactional-and-mass-emails)
      * Gestionar mensajes entrantes
        * [Parámetros del sistema que previenen bucles de retroalimentación](general/email_communication/email_servers.html#system-parameters-that-prevent-feedback-loops)
        * [Permitir el parámetro del sistema de seudónimo del dominio](general/email_communication/email_servers.html#allow-alias-domain-system-parameter)
    * Configure los registros DNS para enviar correos en Odoo
      * [Resumen de las etiquetas SPAM](general/email_communication/email_domain.html#spam-labels-overview)
      * [Cumplimiento SPF](general/email_communication/email_domain.html#be-spf-compliant)
      * [Habilitar DKIM](general/email_communication/email_domain.html#enable-dkim)
      * [Verificar la política DMARC](general/email_communication/email_domain.html#check-the-dmarc-policy)
      * [Documentación de SPF, DKIM y DMARC de los proveedores más comunes](general/email_communication/email_domain.html#spf-dkim-dmarc-documentation-of-common-providers)
    * Conecte Microsoft Outlook 365 a Odoo con Azure OAuth
      * Configuración en el portal de Microsoft Azure
        * [Crear una nueva aplicación](general/email_communication/azure_oauth.html#create-a-new-application)
        * [Permisos de la API](general/email_communication/azure_oauth.html#api-permissions)
      * Asignación de usuarios y grupos
        * [Creación de credenciales](general/email_communication/azure_oauth.html#create-credentials)
      * Configuración en Odoo
        * [Ingresar credenciales de Microsoft Outlook.](general/email_communication/azure_oauth.html#enter-microsoft-outlook-credentials)
        * Configurar servidor de correos electrónicos salientes
          * [Configuración con un solo servidor de correos electrónicos salientes](general/email_communication/azure_oauth.html#configuration-with-a-single-outgoing-mail-server)
          * Configuración específica del usuario (varios usuarios)
            * [Configurar](general/email_communication/azure_oauth.html#setup)
        * [Configure un servidor de correo electrónico de llegada](general/email_communication/azure_oauth.html#configure-incoming-email-server)
    * Conectar Gmail con Odoo mediante Google OAuth
      * Configuración en Google
        * [Crear un nuevo proyecto](general/email_communication/google_oauth.html#create-a-new-project)
        * [OAuth pantalla de consentimiento](general/email_communication/google_oauth.html#oauth-consent-screen)
        * [Editar el registro a la aplicación](general/email_communication/google_oauth.html#edit-app-registration)
        * [Crear credenciales](general/email_communication/google_oauth.html#create-credentials)
      * Configuración en Odoo
        * [Introducir credenciales de Google](general/email_communication/google_oauth.html#enter-google-credentials)
        * [Configurar servidor de correos electrónicos salientes](general/email_communication/google_oauth.html#configure-outgoing-email-server)
      * Preguntas frecuentes sobre la autenticación OAuth de Google
        * [Estados de publicación de producción y de prueba](general/email_communication/google_oauth.html#production-vs-testing-publishing-status)
        * [No se agregaron usuarios de prueba](general/email_communication/google_oauth.html#no-test-users-added)
        * [El módulo de Gmail no se actualizó](general/email_communication/google_oauth.html#gmail-module-not-updated)
        * [Tipo de aplicación](general/email_communication/google_oauth.html#application-type)
    * API de Mailjet
      * Configuración en Mailjet
        * [Crear credenciales API](general/email_communication/mailjet_api.html#create-api-credentials)
        * [Agregar direcciones de remitente verificadas](general/email_communication/mailjet_api.html#add-verified-sender-address-es)
        * Agregar un dominio
          * [Configuración en el DNS del dominio](general/email_communication/mailjet_api.html#setup-in-the-domain-s-dns)
          * [Regresar a la información de cuenta de Mailjet](general/email_communication/mailjet_api.html#return-to-mailjet-account-information)
      * [Configuración en Odoo](general/email_communication/mailjet_api.html#set-up-in-odoo)
    * Problemas con el correo electrónico
      * Correos electrónicos salientes
        * El correo electrónico no se envía
          * Mensajes de error comunes
            * [Límite diario alcanzado](general/email_communication/faq.html#daily-limit-reached)
            * Errores del SMTP
              * [Sin error](general/email_communication/faq.html#no-error-populated)
        * [El correo se envío a destiempo](general/email_communication/faq.html#email-is-sent-late)
      * Correos electrónicos entrantes
        * [El correo electrónico no se recibe](general/email_communication/faq.html#email-is-not-received)
      * [Obtenga ayuda de soporte de Odoo](general/email_communication/faq.html#get-help-from-odoo-support)
  * Integraciones
    * [Complementos de correo](general/integrations/mail_plugins.html)
      * Complemento de Outlook
        * Configuración
          * [Habilitar el complemento de correo](general/integrations/mail_plugins/outlook.html#enable-mail-plugin)
          * [Instalar el complemento de Outlook](general/integrations/mail_plugins/outlook.html#install-the-outlook-plugin)
          * [Conectar la base de datos](general/integrations/mail_plugins/outlook.html#connect-the-database)
          * [Agregar un atajo al complemento](general/integrations/mail_plugins/outlook.html#add-a-shortcut-to-the-plugin)
          * [Uso del plugin](general/integrations/mail_plugins/outlook.html#using-the-plugin)
      * Complemento de Gmail
        * Usuarios de Odoo en línea
          * [Instalar el complemento de Gmail](general/integrations/mail_plugins/gmail.html#install-the-gmail-plugin)
          * [Configurar la base de datos de Odoo](general/integrations/mail_plugins/gmail.html#configure-the-odoo-database)
          * [Configurar la bandeja de entrada de Gmail](general/integrations/mail_plugins/gmail.html#configure-the-gmail-inbox)
        * Usuarios de Odoo con alojamiento local
          * [Instalar el complemento de Gmail](general/integrations/mail_plugins/gmail.html#id1)
          * [Configurar la base de datos de Odoo](general/integrations/mail_plugins/gmail.html#id2)
          * [Configurar la bandeja de entrada de Gmail](general/integrations/mail_plugins/gmail.html#id3)
      * Precio
        * [Servicio de compras dentro de la aplicación para la generación de leads](general/integrations/mail_plugins.html#lead-generation-iap-service)
    * [Unsplash](general/integrations/unsplash.html)
    * [Geolocalización](general/integrations/geolocation.html)
  * Modo de desarrollador (modo de depuración)
    * [Activación](general/developer_mode.html#activation)
    * [Herramientas de desarrollador y menú técnico](general/developer_mode.html#developer-tools-and-technical-menu)

