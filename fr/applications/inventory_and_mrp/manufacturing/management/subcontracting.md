# Sous-traiter votre fabrication

L’externalisation d’une partie ou de la totalité des besoins de votre société
en matière de fabrication n’est pas chose aisée. Pour que cela fonctionne,
vous devez :

  * Gérer l’inventaire des manières premières chez votre sous-traitant

  * Expédier les matières premières à vos sous-traitants, au bon moment

  * Contrôler la qualité des marchandises entrantes

  * Contrôler les factures des sous-traitants

Voici un exemple de la sous-traitance de la fabrication de « C », produit à
partir des matières premières « A » et « B ».

![](../../../../_images/subcontracting_01.png)

Grâce à sa fonctionnalité de sous-traitance MRP, Odoo vous aide à gérer ce
flux facilement.

## Configuration

Pour utiliser la fonctionnalité de sous-traitance, allez à Fabrication ‣
Configuration ‣ Paramètres et cochez la case _Sous-traitance_.

![](../../../../_images/sbc_1.png)

Pour définir si un produit doit être sous-traité, utilisez une _nomenclature_
de type _sous-traitance_.

Pour créer une nouvelle _nomenclature_ , allez à Fabrication ‣ Produits ‣
Nomenclature et cliquez sur créer. Listez ensuite les composants dont votre
sous-traitant a besoin pour fabriquer le produit. Afin de calculer les coûts,
vous pouvez enregistrer tous les composants, même ceux qui proviennent
directement du sous-traitant.

Une fois que vous avez défini le _type de nomenclature_ sur _sous-traitance_ ,
indiquez un ou plusieurs sous-traitants.

![](../../../../_images/sbc_2.png)

## Flux de sous-traitance de base

Pour indiquer à votre sous-traitant le nombre de produits dont vous avez
besoin, créez et envoyez-lui des bons de commande. Pour ce faire, accédez à
l’application _Achats_ et créez un nouveau bon de commande. Veillez à envoyer
le bon de commande à un fournisseur qui est défini comme sous-traitant sur la
_nomenclature_ de ces produits.

![](../../../../_images/subcontracting_04.png)

Une fois le _bon de commande_ validé (1), une réception en attente est créée.
À la réception des produits, validez la réception (2), avec la quantité réelle
reçue. En conséquence, Odoo fait les choses suivantes pour vous :

  * Consomme les composants respectifs chez le sous-traitant, selon la _nomenclature_ et votre entrée (3) ;

  * Produit les produits finis chez le sous-traitant (4) ;

  * Transfère les produits de l’emplacement de sous-traitance à votre entreprise YourCompany par le biais de la réception validée (5).

Note

Le _bon de commande_ est optionnel. Si vous créez une réception manuellement,
avec le bon sous-traitant, Odoo effectue quand même tous les déplacements.
Cela peut être utile si le sous-traitant ne facture pas un prix fixe par
article, mais plutôt le temps et les matériaux utilisés.

## Valorisation des stocks

Le coût du produit fabriqué « C » est défini comme suit :

**C = A + B + s**

Avec :

  * **A** : Coût des matières premières venant de YourCompany ;

  * **B** : Coût des matières premières venant directement du
    

sous-traitant ;

  * **s** : Coût du service sous-traité.

L’envoi de matières premières à vos sous-traitants (**A**) n’a pas d’incidence
sur la valorisation des stocks, car les composants sont toujours valorisés
comme faisant partie de votre stock. Cette situation est gérée en faisant de
l” _emplacement de sous-traitance_ un _emplacement interne_.

Ensuite, le prix fournisseur défini sur la fiche du produit C doit
correspondre à ce qui doit être payé au sous-traitant pour ses pièces et son
temps de service : **B + s**. Le coût du produit doit être : **A + B + s** ,
c’est-à-dire la valeur du produit dans la comptabilité.

Enfin, la facture du sous-traitant correspond au bon de commande, avec le prix
proposé pour les produits finis C.

Note

S’il n’est pas nécessaire de gérer le réassort des matières premières **B**
chez votre sous-traitant, il suffit d’inclure le coût de **B** dans le prix du
sous-traitant **s** et de supprimer les produits **B** de la _nomenclature_.

## Traçabilité

Si les produits reçus du sous-traitant contiennent des composants trackés,
leurs numéros de série ou de lot doivent être précisés lors de la réception.

Dans ce cas, lors de la réception du produit sous-traité, un bouton
_Enregistrer les composants_ apparaît. Cliquez dessus pour ouvrir une boîte de
dialogue et enregistrez les numéros de série/lot des composants. Si le produit
fini est également suivi, son numéro de série/lot peut également être
enregistré ici.

![](../../../../_images/sbc_3.png)

À des fins d’audit, il est possible de vérifier les numéros de lot enregistrés
sur une réception en utilisant l’icône située à droite des produits finis :

![](../../../../_images/sbc_4.png)

Notez également que si la consommation flexible a été sélectionnée sur la
nomenclature sous-traitée pour un produit non suivi, l’option d’enregistrement
des composants apparaîtra de manière optionnelle sur chaque ligne, si vous
voulez enregistrer plus ou moins de consommation de composants à l’emplacement
de sous-traitance, lors de la réception de votre produit fini.

![](../../../../_images/sbc_5.png)

Comme vous pouvez le constater, la réception de ces deux produits non trackés
peut être effectuée en sélectionnant l’option “Définir les quantités” ou via
le menu hamburger des lignes de mouvement.

## Automatiser le réapprovisionnement des sous-traitants

Il existe deux façons d’automatiser l’approvisionnement en matières premières
de vos sous-traitants lors de l’achat du produit fini. La méthode choisie
dépend du fait que vous souhaitiez ou non que les matériaux passent par votre
entrepôt. Ces deux méthodes sont décrites comme des mécanismes de type
“tirer”, car leur déclencheur est le bon de commande initial du sous-traitant,
qui crée un besoin de manières premières à l’emplacement de sous-traitance.

Si vous fournissez des matières premières à votre sous-traitant à partir de
votre propre entrepôt, vous devez activer la route “Réapprovisionner le sous-
traitant sur demande” comme indiqué ci-dessous. S’il s’agit d’un composant que
vous achetez auprès d’un fournisseur, la route “Acheter” doit également être
activée.

![](../../../../_images/sbc_6.png)

Désormais, si vous souhaitiez que votre fournisseur approvisionne directement
votre sous-traitant, vous devez choisir l’option “Sous-traitant dropship sur
commande”. Pour que cette option soit active sur la fiche produit, vous devez
d’abord activer l’option de dropshipping dans Achats ‣ Configuration ‣
Paramètres ‣ Dropshipping. Une fois que la commande auprès du sous-traitant
est validée, cette route créera une demande de prix de dropshipping de votre
fournisseur à ce sous-traitant. Vous n’avez plus qu’à l’examiner et le
valider.

![](../../../../_images/sbc_7.png)

Notez que la route “Acheter” n’est pas sélectionnée dans ce cas, car la route
“dropshipping” est déjà une route d’achat.

Enfin, si vous souhaitiez tracker le stock de ces matières premières à vos
emplacements de sous-traitance, vous devez activer l’option _Routes en
plusieurs étapes_ dans Inventaire ‣ Configuration ‣ Paramètres ‣ Emplacements
de stockage.

À partir du formulaire de l’emplacement, vous pouvez accéder au Stock actuel.

![](../../../../_images/sbc_8.png)

### Réassort manuel

Vous pouvez également choisir de réapprovisionner vos sous-traitants
manuellement.

Si vous voulez envoyer des composants à votre sous-traitant à votre
convenance, sélectionnez le type d’opération “Réapprovisionner le sous-
traitant” à partir du module _Inventaire_ et créez un transfert en précisant à
quel sous-traitant vous livrez.

![](../../../../_images/sbc_9.png)

Vous pouvez également demander à votre fournisseur de réapprovisionner le
sous-traitant en créant un bon de commande de type dropshipping, en
définissant votre sous-traitant en tant qu’adresse de livraison.

![../../../../_images/sbc_10.png](../../../../_images/sbc_10.png)

