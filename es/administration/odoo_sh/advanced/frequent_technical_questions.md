# Preguntas técnicas más frecuentes

## «Las acciones planificadas no se ejecutan en el momento exacto en que se
esperaban»

En la plataforma de Odoo.sh, no podemos garantizar un tiempo de ejecución
exacto para las acciones planificadas.

Esto se debe a que quizás haya varios clientes en el mismo servidor y debemos
garantizar una repartición justa del servidor a cada uno. Por lo tanto, las
acciones planificadas se llevan a cabo de manera algo distinta a como se haría
en un servidor regular de Odoo y se ejecutan bajo una política de _mayor
esfuerzo_.

Advertencia

No espere que ninguna acción planificada se ejecute con una frecuencia mayor a
cada 5 minutos.

## ¿Hay «mejores prácticas» respecto a las acciones planificadas?

**Odoo.sh siempre limita el tiempo de ejecución de las acciones planificadas
(*también conocidas como* crons).** Por lo tanto, debe tener esto en cuenta
cuando desarrolle sus propios crons.

Le aconsejamos lo siguiente:

  * Sus acciones planificadas deben trabajar en pequeños lotes de registros.

  * Sus acciones planificadas deben confirmar su trabajo después de procesar cada lote. De esta forma, si las interrumpe el límite de tiempo, no es necesario volver a empezar.

  * Sus acciones planificadas deben ser [idempotentes](https://stackoverflow.com/a/1077421/3332416). No deben causar efectos secundarios si se activan con una mayor frecuencia a la esperada.

