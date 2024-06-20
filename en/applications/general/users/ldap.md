# Sign in with LDAP

  * Install the Lightweight Directory Access Protocol (LDAP) module in General Settings.

  * Click on **Create** in Setup the LDAP Server.

![LDAP Authentication checkbox highlighted in the integrations settings on
Odoo.](../../../_images/ldap01.png) ![Create highlighted in the LDAP server
settings.](../../../_images/ldap02.png)

  * Choose the company using the LDAP.

![Select the company drop-down menu highlighted in LDAP
setup.](../../../_images/ldap03.png)

  * In **Server Information** , enter the IP address of the server and the port it listens to.

  * Tick **Use TLS** if the server is compatible.

![LDAP server settings highlighted in LDAP server setup on
Odoo.](../../../_images/ldap04.png)

  * In **Login Information** , enter ID and password of the account used to query the server. If left empty, the server queries anonymously.

![Login information highlighted in LDAP server setup on
Odoo.](../../../_images/ldap05.png)

  * In **Process Parameter** , enter the domain name of the LDAP server in LDAP nomenclature (e.g. `dc=example,dc=com`).

  * In **LDAP filter** , enter `uid=%s`

![Process parameter highlighted in LDAP server setup on
Odoo.](../../../_images/ldap06.png)

  * In **User Information** , tick _Create User_ if Odoo should create a User profile the first time someone logs in with LDAP.

  * In **Template User** , indicate a template for the new profiles created. If left blanked, the admin profile will be used as template.

![User information highlighted on LDAP server setup on
Odoo.](../../../_images/ldap07.png)

  *[LDAP]: Lightweight Directory Access Protocol

