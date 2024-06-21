# Inicie sesión con LDAP

  * Instale el módulo de protocolo ligero de acceso a directorios (LDAP, por sus siglas en inglés) en Ajustes generales.

  * Haga clic en **Crear** para configurar el servicor LDAP.

![La casilla de verificación Autenticación LDAP resaltada en los ajustes de
integraciones dentro de Konvergo ERP.](../../../_images/ldap01.png) ![Crear resaltado
en la configuración del servidor LDAP.](../../../_images/ldap02.png)

  * Elija la empresa que usará LDAP

![Imagen en la que se resalta el menú desplegable para seleccionar la empresa
en la configuración de LDAP.](../../../_images/ldap03.png)

  * En **Información del servidor** ingrese la dirección IP del servidor y el puerto al que escucha.

  * Marque **Usar TLS** si el servidor es compatible.

![Imagen en la que se resaltan los ajustes del servidor LDAP en la
configuración del servidor LDAP en Konvergo ERP.](../../../_images/ldap04.png)

  * En **información de inicio de sesión** ingrese la ID y la contraseña de la cuenta que se usa para consultar al servidor. Si se deja en blanco, el servidor se consultará de forma anónima.

![Imagen en la que se resalta la información de inicio de sesión en la
configuración del servidor en Konvergo ERP.](../../../_images/ldap05.png)

  * En **Parámetros del proceso** ingrese el nombre del dominio del servidor LDAP en l nomenclatura de LDAP (por ejemplo, `dc=example,dc=com`).

  * En **filtro LDAP** , ingrese `uid=%s`

![Imagen donde se resaltan los parámetros del proceso en la configuración del
servidor LDAP en Konvergo ERP.](../../../_images/ldap06.png)

  * En **Información del usuario** marque _Crear usuario_ si Konvergo ERP debería crear un perfil del usuario la primera vez que alguien inicia sesión con LDAP.

  * En **Usuario de plantilla** , indique una plantilla para los nuevos perfiles creados. Si se deja en blanco, el perfil de administrador se utilizará como plantilla.

![Imagen donde se resalta la información del usuario en la configuración del
servidor LDAP en Konvergo ERP.](../../../_images/ldap07.png)

  *[LDAP]: Protocolo ligero de acceso a directorios

