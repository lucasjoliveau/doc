# Pourboires

Laisser des pourboires est une coutume dans de nombreux pays. Point de Vente
permet de laisser des pourboires dans les
[boutiques](../../point_of_sale#pos-sell), [bars](../restaurant) ou
[restaurants](../restaurant).

## Configuration

Pour autoriser les pourboires dans votre PdV, activez la fonctionnalité
**Pourboires** dans Point de Vente ‣ Configuration ‣ Paramètres. En haut de la
page, sélectionnez le PdV dans lequel vous souhaitez autoriser **les
pourboires** , faites défiler la page jusqu’à la section **Paiement** et
cochez la case **Pourboires**. Une fois cette option activée, ajoutez un
**produit de pourboire** dans le champ correspondant et enregistrez. Le
produit désigné sera utilisé comme référence sur les reçus du client.

![activer les pourboires dans un PdV](../../../../_images/tips-setup.png)

### Produits de pourboire

Les **produits de pourboire** peuvent être créés sur place. Pour ce faire,
saisissez le nom d’un produit dans le champ produit de pourboire et cliquez
sur **Créer** ou appuyez sur **enter**. Le produit est automatiquement
configuré pour être utilisé comme pourboire à l’écran de paiement.

Toutefois, si vous voulez pouvoir sélectionner le produit de pourboire dans
une session du PdV, vous devez activer le paramètre **Disponible dans le
PdV**. Pour ce faire, cliquez sur **Créer et modifier…** pour ouvrir le
formulaire de configuration du produit. Allez ensuite à l’onglet **Vente** ,
cochez la case **Disponible dans le PdV** et cliquez sur **Enregistrer &
Fermer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Lorsque vous créez un produit à utiliser comme pourboire, laissez le <b>type de produit</b> comme <b>Consommable</b> pour éviter des mouvements de stock inutiles.</p></li>
<li><p>Vous ne pouvez sélectionner qu’un seul produit de pourboire par PdV, mais vous pouvez en choisir un différent pour chaque PdV.</p></li>
</ul>
</div>

### Les pourboires via un terminal Adyen

Si vous utilisez un terminal de paiement
[Adyen](../payment_methods/terminals/adyen) et si vous souhaitez activer
les **pourboires** via le terminal, cochez **Ajouter un pourboire via le
terminal de paiement (Adyen)** dans les paramètres des pourboires.

### Les pourboires après le paiement

Si vous utilisez un système de point de vente dans un bar ou dans un
restaurant, vous pouvez activer l’option **Ajouter un pourboire après le
paiement (spécifique à l’Amérique du Nord)**. Cela génère une addition à
imprimer et à compléter manuellement par le client et le serveur. Cette
addition indique la valeur du pourboire que le client choisit de donner après
le paiement.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Pour utiliser cette fonctionnalité, le mode de paiement sélectionné doit avoir un journal bancaire attribué.</p>
</div>

## Ajouter des pourboires

Pour ajouter des pourboires à une commande, [accéder à l’écran de
paiement](../../point_of_sale#pos-sell) et cliquez sur **♥ Pourboire**.
Ensuite, saisissez le montant du pourboire, cliquez sur **Confirmer** pour
valider et traitez le paiement.

![fenêtre contextuelle des pourboires](../../../../_images/add-tip.png)

Vous pouvez également sélectionner le produit de pourboire sur l’interface du
PdV pour l’ajouter au panier. Lorsqu’il est sélectionné, le produit est
automatiquement défini comme un pourboire et sa valeur par défaut est égale à
son **prix de vente**.

### Les pourboires via un terminal Adyen

Lors du passage en caisse, sélectionnez **Adyen** comme terminal de paiement
et envoyez la demande de paiement à l’appareil en cliquant sur **Envoyer**.
Les clients sont invités à saisir le montant du pourboire qu’ils souhaitent
donner sur l’écran du terminal avant de procéder au paiement.

### Les pourboires après le paiement

Lors du passage en caisse, sélectionnez un mode de paiement par carte et
cliquez sur **Fermer la note**. Cela génère une addition à compléter par le
client.

![note de pourboire après le paiement à compléter par les
clients](../../../../_images/tipping-bill.png)

Sur l’écrant suivant, cliquez sur le pourcentage (**15%** , **20%** ,
**25%**), **Aucun pourboire** ou saisissez le montant du pourboire que le
client veut donner. Cliquez ensuite sur **Régler** pour passer à la commande
suivante.

![écran pour sélectionner un montant de pourboire à donner après le
paiement](../../../../_images/tip-after-payment.png)

