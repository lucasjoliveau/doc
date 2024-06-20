# Traspaso de impuestos

Al realizar reportes de impuestos, la función de **traspaso de impuestos**
permite traspasar importes de un periodo a otro sin crear nuevos asientos.

Se creó para cumplir los requisitos legales de ubicaciones determinadas, donde
los importes deben transferirse de un periodo a otro (por ejemplo, porque el
total de la línea es negativo).

La función se activa de forma predeterminada en países en los que es
necesaria, como Bélgica, Francia e Italia. No se necesita de ninguna
configuración específica.

Veamos el ejemplo de una empresa belga que crea una nota de crédito por 100
para uno de sus clientes. Los impuestos adeudados son del 21%.

![Ejemplo de una nota de crédito](../../../../_images/belgian-example.png)

En este caso, según las regulaciones locales, la casilla 81 del reporte de
impuestos puede contener un importe negativo. Debe declararse al gobierno como
cero, y el importe negativo debe traspasarse al siguiente periodo.

Si accede a Contabilidad ‣ Reportes ‣ Reporte de impuestos, una ventana
emergente en la línea 81 explica que el importe se traspasará al siguiente
periodo.

![Mensaje emergente que indica el importe que se traspasará al siguiente
periodo](../../../../_images/pop-up.png)

En el momento del cierre del periodo fiscal, el reporte de impuestos muestra
que el importe se traspasó del periodo anterior. También indica el importe que
se traspasará a esta línea en el siguiente periodo según las transacciones
existentes y el traspaso del periodo anterior.

![Ejemplo de una declaración de impuestos](../../../../_images/tax-return.png)

