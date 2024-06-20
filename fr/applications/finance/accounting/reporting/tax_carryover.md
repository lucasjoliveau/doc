# Report fiscal

Lors de l’établissement d’une déclaration de TVA, la fonctionnalité **report
fiscal** permet de reporter des montants d’une période à une autre sans créer
de nouvelles écritures.

Elle a été créée pour répondre aux exigences légales de certains pays, où des
montants doivent être transférés d’une période à l’autre (par exemple, parce
que le total de la ligne est négatif).

La fonctionnalité est activée par défaut dans les pays où elle est requise,
tels que la Belgique, la France et l’Italie. Aucune configuration spécifique
n’est requise.

Prenons l’exemple d’une entreprise belge qui a créé un avoir de 100 € pour
l’un de ses clients. La taxe due est de 21%.

![Illustration avec un avoir](../../../../_images/belgian-example.png)

Dans ce cas, conformément à la réglementation locale, la grille 81 de la
déclaration de TVA peut contenir un montant négatif. Mais il doit être déclaré
au gouvernement comme zéro et le montant négatif doit être reporté à la
période suivante.

Si nous allons à l’application Comptabilité ‣ Analyse ‣ Déclaration de TVA,
une fenêtre contextuelle sur la ligne 81 explique que le montant sera reporté
à la période suivante.

![Fenêtre contextuelle indiquant que le montant sera reporté à la période
suivante](../../../../_images/pop-up.png)

Au moment de la période de clôture fiscale, la déclaration de TVA indique que
le montant a été reporté de la période précédente. Elle indique également le
montant qui sera reporté à cette ligne dans la période suivante sur la base
des transactions existantes et le report de la période précédente.

![Illustration de la déclaration d'impôt](../../../../_images/tax-return.png)

