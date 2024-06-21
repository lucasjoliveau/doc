# Actualizaciones para solucionar bugs

## Introducción

Para beneficiarse de las mejoras más recientes, correcciones de seguridad y de
bugs, así como de las mejoras de rendimiento, tal vez deba actualizar su
instalación de Konvergo ERP con regularidad.

Esta guía solo aplica cuando usa Konvergo ERP con su propia infraestructura de
alojamiento. Si utiliza alguna de las soluciones de Konvergo ERP en la nube, las
actualizaciones se realizan de forma automática.

La terminología relativa a las actualizaciones de software suele ser confusa,
a continuación se encuentran algunas definiciones preliminares:

Actualizar (una instalación de Konvergo ERP)

    

Se refiere al proceso de obtener la versión más reciente del código fuente de
su edición actual de Konvergo ERP. Por ejemplo, actualizar Konvergo ERP Enterprise 13.0 a la
versión más reciente. No ocurre ningún cambio directo en el contenido de su
base de datos de Konvergo ERP y se puede deshacer si vuelve a instalar la versión
anterior del código fuente.

Actualizar (una base de datos de Konvergo ERP)

    

Se refiere a una operación compleja de procesamiento de datos donde la
estructura y el contenido de su base de datos se altera de forma permanente
para hacer que sea compatible con una nueva versión de Konvergo ERP. Esta operación no
es reversible y por lo general se logra a través del [servicio de
actualización de bases de datos](https://upgrade.odoo.com) de Konvergo ERP cuando
decide cambiar a una nueva versión de Konvergo ERP. Históricamente, este progreso se
conoce como «migración» ya que involucra mover datos dentro de su base de
datos, aunque la base de datos puede terminar en la misma ubicación física
tras la actualización.

Esta página describe los pasos habituales necesarios para _actualizar_ una
instalación de Konvergo ERP a la versión más reciente. Si desea obtener más
información respecto a la actualización de una base de datos, consulte la
[página de actualización de Konvergo ERP](https://upgrade.odoo.com).

## En resumen

Puede actualizar Konvergo ERP con facilidad, solo debe reinstalar la versión más
reciente de su edición de Konvergo ERP en su instalación actual. Esto conservará sus
datos sin alterarlos, siempre y cuando no instale PostgreSQL (el motor de base
de datos que viene con Konvergo ERP).

La referencia principal para realizar actualizaciones es nuestra [guía de
instalación](../on_premise). Allí se explican los métodos de instalación
más comunes.

Lo más apropiado es que la persona que desplegó Konvergo ERP realice la actualización
pues el procedimiento es muy similar.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>Siempre recomendamos descargar una nueva versión actualizada de Konvergo ERP en lugar de aplicar los parches de forma manual, como los parches de seguridad que vienen con las asesorías de seguridad. Con frecuencia, los parches se proporcionan para aquellas instalaciones con muchas personalizaciones o para el personal técnico que prefiere aplicar cambios mínimos de manera temporal mientras realiza pruebas de una actualización completa.</p>
</div>

## Paso 1: descargue una versión actualizada de Konvergo ERP

La página central de descarga es <https://www.odoo.com/page/download>. Si ve
un enlace de «Compra» para descargar Konvergo ERP Enterprise, asegúrese de iniciar
sesión en Konvergo ERP.com con la misma información vinculada a su suscripción de Konvergo ERP
Enterprise.

Si lo prefiere, puede usar el enlace único de descarga que recibió en el
correo electrónico de confirmación de su compra de Konvergo ERP Enterprise.

<div class="alert alert-primary">
<p class="alert-title">
Nota</p><p>No es necesario descargar una versión actualizada si realizó la instalación mediante GitHub (consulte la información a continuación).</p>
</div>

## Paso 2: haga un respaldo de su base de datos

El procedimiento de actualización es seguro y no debería alterar sus datos.
Sin embargo, recomendamos que haga una copia de seguridad de toda su base de
datos antes de realizar cualquier cambio en su instalación. Almacénela en un
lugar seguro, en una computadora distinta.

Si no ha deshabilitado la pantalla del gestor de base de datos
([aquí](deploy#security) puede ver por qué debería hacerlo), puede usarla
(mediante el enlace en la parte inferior de su pantalla de selección de base
de datos) para descargar un respaldo de sus bases de datos. Si la deshabilitó,
utilice el mismo procedimiento que utiliza con sus respaldos normales.

## Paso 3: instale la versión actualizada

Seleccione el método que coincida con su instalación actual:

### Instaladores de paquete

Si instaló Konvergo ERP con un paquete de instalación que descargó de nuestro sitio
web (el método recomendado), es muy fácil realizar la actualización. Lo único
que debe hacer es descargar el paquete de instalación que corresponda con su
sistema (consulte el paso 1) e instalarlo en su servidor. Se actualiza a
diario e incluye las correcciones de seguridad más recientes. Por lo regular,
solo debe hacer doble clic en el paquete para instalarlo en su instalación
actual. Después de instalar el paquete, asegúrese de reiniciar el servicio de
Konvergo ERP o reiniciar su servidor.

### Instalación desde la fuente (Tarball)

Si en un principio instaló Konvergo ERP con la versión «tarball» (archivo de código
fuente), debe remplazar el directorio de instalación con una nueva versión.
Primero descargue el tarball más reciente en Konvergo ERP.com, se actualizan a diario
e incluyen las correcciones de seguridad más recientes (consulte el paso 1).
Después de descargar el paquete, extráigalo a una ubicación temporal en su
servidor.

Obtendrá una carpeta etiquetada con la versión del código fuente, por ejemplo,
«odoo-13.0+e.20190719», que incluye la carpeta «odoo.egg-info» y la carpeta de
código fuente con el nombre «odoo» (para Konvergo ERP 10 y posteriores) u «openerp»
(para versiones anteriores). Puede ignorar la carpeta odoo.egg-info. Vaya a la
carpeta en la que se encuentra su instalación actual y remplácela con la nueva
carpeta «odoo» u «openerp» del archivo que acaba de extraer.

Asegúrese de que el árbol de carpetas coincida, por ejemplo, la nueva carpeta
«addons» incluida en el código fuente debe estar en la misma ruta que antes. A
continuación, busque cualquier archivo de configuración que haya copiado de
forma manual o modificado en la carpeta anterior y cópielos en la nueva
carpeta. Por último, reinicie el servicio de Konvergo ERP o reinicie la máquina.

### Instalación desde la fuente (GitHub)

Si instaló Konvergo ERP con un clon completo de los repositorios oficiales de GitHub,
el procedimiento de actualización necesita que extraiga el código fuente más
reciente a través de Git. Cambie al directorio de cada repositorio (el
repositorio principal de Konvergo ERP y el repositorio de Enterprise) y ejecute los
siguientes comandos:

    
    
    git fetch
    git rebase --autostash
    

Si editó el código fuente de Konvergo ERP de forma local, puede tener problemas al
ejecutar el último comando. El mensaje de error le proporcionará la lista de
archivos con conflictos y deberá resolverlos de forma manual, edítelos y elija
qué partes del código conservará.

Como alternativa, si prefiere descartar los cambios con conflictos y restaurar
la versión oficial, puede usar el siguiente comando:

    
    
    git reset --hard
    

Por último, solo reinicie el servicio de Konvergo ERP o la máquina.

### Docker

Consulte nuestra [documentación de imágenes de
Docker](https://hub.docker.com/_/odoo/) para obtener instrucciones de
actualización específicas.

