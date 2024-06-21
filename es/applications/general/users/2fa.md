# Autenticación en dos pasos

La autenticación de dos factores («A2F») es una buena manera de mejorar la
seguridad de una cuenta. Así será menos probable que una persona que no sea
usted inicie sesión.

En resumen, se trata de guardar un secreto dentro de un _autenticador_
(normalmente su teléfono) y intercambiar un código desde su autenticador
cuando quiera iniciar sesión.

Esto significa que un atacante tendría que haber hecho _ambas cosas_ ,
adivinar (o encontrar) su contraseña y tener acceso (o robar) su
autentificador, lo cual es mucho más difícil que uno u otro.

## Requisitos

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Las listas solo son ejemplos, no son respaldos de un software específico.</p>
</div>

Si todavía no tiene uno, tendrá que elegir un autenticador.

Los autentificadores basados en teléfonos son los más fáciles de usar y
también los más comunes, así que asumiremos que elegirá e instalará uno en su
celular. Entre los ejemplos están [Authy](https://authy.com/),
[FreeOTP](https://freeotp.github.io/), [Google
Authenticator](https://support.google.com/accounts/answer/1066447?hl=en),
[LastPass Authenticator](https://lastpass.com/auth/), [Microsoft
Authenticator](https://www.microsoft.com/en-
gb/account/authenticator?cmp=h66ftb_42hbak), entre otros. Los gestores de
contraseñas también incluyen compatibilidad con la A2P, por ejemplo,
[1Password](https://support.1password.com/one-time-passwords/),
[Bitwarden](https://bitwarden.com/help/article/authenticator-keys/), etcétera.

Por motivos de esta demostración, usaremos el autenticador de Google (no
porque sea bueno, sino porque es el más común).

## Configurar la autenticación de dos pasos

Una vez que tenga su autentificador elegido, vaya a la instancia de Konvergo ERP que
quiere configurar con A2P, después, abra las **Preferencias** (or **Mi
perfil**):

![../../../_images/preferences.png](../../../_images/preferences.png)

Abra la pestaña **Seguridad de la cuenta** , después haga clic en el botón
**Habilitar la autenticación en dos pasos** :

![../../../_images/sec_tab.png](../../../_images/sec_tab.png)

Ya que esta es una acción importante para la seguridad, deberá escribir su
contraseña:

![../../../_images/sec_enhanced.png](../../../_images/sec_enhanced.png)

Después de eso, verá esta pantalla con un código de barras:

![../../../_images/totp_scan.png](../../../_images/totp_scan.png)

En la mayoría de las aplicaciones, puede solamente _escanear el código de
barras_ a través del autenticador de su elección, que se encargará de hacer
toda la configuración:

![../../../_images/scan_barcode.jpg](../../../_images/scan_barcode.jpg)

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Si no puede escanear la pantalla (por ejemplo, porque realizará la configuración en el mismo teléfono que la aplicación de autentificación), puede hacer clic en el vínculo proporcionado, o puede copiar el secreto para configurar manualmente el autenticador:</p>
<div class="figure align-center">
<img alt="../../../_images/secret_visible.png" src="../../../_images/secret_visible.png"/>
</div>
<div class="figure align-center">
<img alt="../../../_images/input_secret.png" src="../../../_images/input_secret.png"/>
</div>
</div>

Una vez que haya hecho esto, el autenticador mostrará un _código de
verificación_ con información útil de identificación (por ejemplo, el dominio
e inicio de sesión para el que es el código):

![../../../_images/authenticator.png](../../../_images/authenticator.png)

Ahora puede poner el código en el campo de **Código de verificación** ,
después haga clic en el botón de **Habilitar la autenticación en dos pasos**.

¡Felicidades, su cuenta ahora está protegida con la autenticación de dos
pasos!

![../../../_images/totp_enabled.png](../../../_images/totp_enabled.png)

## Iniciar sesión

Ahora debe **Cerrar sesión** para continuar con el proceso.

En la página de inicio de sesión, introduzca el nombre de usuario y la
contraseña de la cuenta con la que configuró la A2P, en lugar de ingresar a
Konvergo ERP inmediatamente ahora verá una segunda pantalla de inicio de sesión:

![../../../_images/2fa_input.png](../../../_images/2fa_input.png)

Tome su autenticador, ingrese el código que le da para el dominio y la cuenta,
valide y finalmente inició sesión.

Eso es todo. De ahora en adelante, a no ser que desactive la `A2P
(autenticación de 2 pasos)`, tendrá que pasar por un proceso de dos pasos para
iniciar sesión, en lugar del antiguo proceso de un paso.

<div class="alert alert-danger">
<p class="alert-title">
Peligro</p><p>No pierda su autenticador, si lo hace, necesitará un <em>Administrador de Konvergo ERP</em> para desactivar la <code>A2P (autenticación de 2 pasos)</code> en la cuenta.</p>
</div>

  *[A2P]: autenticación de 2 pasos

