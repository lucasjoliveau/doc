# Retenues à la source

Une retenue à la source, aussi appelé une taxe de rétention, est une exigence
du gouvernement pour le payeur d’une facture client de retenir ou de déduire
la taxe du paiement, et de payer cette taxe au gouvernement. Dans la plupart
des juridictions, la retenue à la source s’applique aux revenus
professionnels.

Dans le cas de taxes normales, la TVA est ajoutée au sous-total pour vous
donner le total à payer. Contrairement aux taxes normales, les retenues à la
source sont déduites du montant à payer, étant donné que la taxe sera payée
par le client.

Par exemple, en Colombie, vous pouvez avoir la facture suivante :

![../../../../_images/retention03.png](../../../../_images/retention03.png)

Dans cet exemple, l”**entreprise** qui a envoyé la facture doit 20 $ de taxes
au **gouvernement** et le **client** doit 10 $ de taxes au **gouvernement**.

## Configuration

Dans Konvergo ERP, une retenue à la source est définie par la création d’une taxe
négative. Pour une rétention de 10%, vous pouvez configurer la TVA suivante
(accessible via Configuration -> Taxes) :

![../../../../_images/retention04.png](../../../../_images/retention04.png)

Pour la faire apparaître comme une retenue sur la facture, vous devez définir
un groupe fiscal spécifique **Retenue** sur vos taxes, dans l’onglet **Options
avancées**.

![../../../../_images/retention02.png](../../../../_images/retention02.png)

Une fois que la taxe est définie, vous pouvez l’utiliser sur vos produits,
commandes clients ou factures.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si la retenue est un pourcentage d’une taxe normale, créer une Taxe avec un <b>Calcul de la taxe</b> comme un <b>Groupe de taxe</b> et définissez les deux taxes dans ce groupe (taxe normale et retenue).</p>
</div>

## Application des retenues à la source aux factures

Une fois que votre taxe est créée, vous pouvez l’utiliser sur les fiches
clients, les commandes clients ou les factures clients. Vous pouvez appliquer
plusieurs taxes sur une seule ligne de facture client.

![../../../../_images/retention01.png](../../../../_images/retention01.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Quand vous visualisez la facture client à l’écran, vous voyez seulement une ligne <b>Taxes</b> résumant toutes les taxes (taxes normales et retenues). Mais lorsque vous imprimez ou envoyez la facture, Konvergo ERP fait le regroupement correct de toutes les taxes.</p>
</div>

La facture imprimée montrera les différents montants de chaque groupe de taxe.

![../../../../_images/retention03.png](../../../../_images/retention03.png)
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../taxes">Taxes</a></p></li>
</ul>
</div>

