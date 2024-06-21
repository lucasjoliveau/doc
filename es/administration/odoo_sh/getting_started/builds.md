# Compilaciones

## Información general

En Konvergo ERP.sh, una compilación se considera una base de datos que cargó un
servidor de Konvergo ERP ([odoo/odoo](https://github.com/odoo/odoo) y
[odoo/enterprise](https://github.com/odoo/enterprise)) y se ejecuta en una
revisión específica del repositorio de su proyecto en un entorno
contenedorizado. Su objetivo es probar el comportamiento correcto del
servidor, la base de datos y las funciones de esta revisión.

![../../../_images/interface-builds.png](../../../_images/interface-
builds.png)

En esta vista, una fila representa una rama y una celda en la fila representa
una compilación de esta rama.

Muchas veces, las compilaciones se crean después de enviar los cambios a las
ramas de su repositorio de GitHub. También se pueden crear cuando realiza
otras operaciones, como importar una base de datos a Konvergo ERP.sh o solicitar que
se vuelva a crear una compilación para una rama en su proyecto.

Se considera que una compilación tuvo éxito si no aparecen errores o
advertencias durante su creación. Una compilación exitosa se resalta en verde.

Se considera que una compilación ha fallado si aparecen errores durante su
creación. Una compilación fallida aparecerá resaltada en rojo.

Si se producen advertencias durante la creación, pero no hay errores, la
compilación se considera casi exitosa y aparecerá resaltada en amarillo para
notificar al desarrollador de las advertencias presentadas.

Las compilaciones no siempre crean una base de datos desde cero. Por ejemplo,
cuando se realiza un cambio en la rama de producción, la compilación creada
simplemente inicia el servidor con su nueva revisión e intenta cargar la base
de datos de producción actual. Si no aparecen errores, la construcción se
considera exitosa, y en caso contrario, fallida.

## Etapas

### Etapa de producción

La primera compilación de una rama de producción crea una base de datos desde
cero. Si esta construcción es exitosa, esta base de datos se considera como la
base de datos de producción de su proyecto.

A partir de ahí, los cambios que suba de la rama de producción crearán nuevas
compilaciones que intentarán actualizar la base de datos utilizando un
servidor que funcione con la nueva revisión.

Si la compilación es exitosa, o tiene advertencias pero no errores, la base de
datos de producción se ejecutará con esta compilación y su revisión asociada.

Si la compilación no logra cargar o actualizar la base de datos, se volverá a
utilizar la compilación anterior que sí lo consiguió y, por lo tanto, la base
de datos se ejecutará utilizando un servidor que funcione con la revisión
anterior.

La compilación utilizada para ejecutar la base de datos de producción siempre
será la primera en la lista de compilaciones. Si una compilación falla, se
colocará después de la compilación que está ejecutando la base de datos de
producción.

### Etapa de prueba

Las compilaciones de prueba duplican la base de datos de producción e intentan
actualizarla con las revisiones de las ramas de prueba.

Cada vez que se envía una nueva revisión a una rama de prueba, la compilación
creada utiliza una nueva copia de la base de datos de producción. Las bases de
datos no se reutilizan entre compilaciones de la misma rama. Esto garantiza
que:

  * Las compilaciones de prueba utilicen bases de datos que se aproximen al aspecto de la producción, para que no haga sus pruebas con datos desactualizados,

  * Pueda probar todo lo que quiera en la misma base de datos de prueba y luego pueda solicitar una nueva compilación cuando quiera volver a empezar con una nueva copia de la producción.

No obstante, esto significa que si realiza cambios de configuración en las
bases de datos de prueba y no se aplican en la producción, no aparecerán en la
siguiente compilación de la misma rama de prueba.

### Etapa de desarrollo

Las compilaciones de desarrollo crean nuevas bases de datos, cargan los datos
de demostración y ejecutan las pruebas unitarias.

Si las pruebas fallan durante la instalación, se considerará que la
compilación ha fallado y se resaltará en rojo, ya que están pensadas para que
se produzcan errores si ocurre algo que no debería suceder.

Si las pruebas funcionan bien y no se produce ningún error, la compilación se
considerará exitosa.

Según la lista de módulos a instalar y probar, una compilación de desarrollo
puede tardar hasta una hora en estar lista. Esto se debe al gran número de
pruebas establecidas en el conjunto de módulos predeterminado de Konvergo ERP.

## Funciones

Siempre aparecerá la rama de producción primero y luego las demás ramas se
ordenarán según la última compilación creada. Puede filtrar las ramas.

![../../../_images/interface-builds-branches.png](../../../_images/interface-
builds-branches.png)

Puede acceder a la base de datos de la última versión de cada rama mediante el
enlace _Conectar_ y acceder al código de la rama mediante el enlace de
_GitHub_. Para las otras ramas que no sean la de producción, puede crear una
nueva compilación que utilizará la última revisión de la rama utilizando el
enlace _nueva compilación_. Este último enlace no estará disponible cuando ya
haya una compilación en curso para la rama.

![../../../_images/interface-builds-build.png](../../../_images/interface-
builds-build.png)

Para cada compilación, puede acceder a los cambios de revisión utilizando el
botón con el icono de GitHub. Puede acceder a la base de datos de la
compilación como administrador utilizando el botón _Conectar_. También puede
acceder a la base de datos con otro usuario utilizando el botón _Conectar
como_ , en el menú desplegable del botón _Conectar_.

![../../../_images/interface-builds-build-
dropdown.png](../../../_images/interface-builds-build-dropdown.png)

En el menú desplegable de la compilación, puede acceder a las mismas funciones
que en la [vista de las ramas](branches#odoosh-gettingstarted-branches-
tabs): _Registros_ , _Webshell_ , _Editor_ , _Correos de salida_. También
tiene la posibilidad de _descargar un dump_ de la base de datos de la
compilación.

