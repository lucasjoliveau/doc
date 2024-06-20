# Transférer des produits entre entrepôts à l’aide du réassort

Pour les entreprises qui utilisent plusieurs entrepôts, il est souvent
nécessaire de transférer des articles entre eux. C’est ce qu’on appelle un
_transfert entre entrepôts_. Odoo _Inventaire_ gère le processus administratif
des transferts entre entrepôts pour assurer que l’inventaire reste exact
pendant et après le transfert. Ce document détaille la méthode pour effectuer
un transfert entre entrepôts à l’aide du réassort.

## Configurer des entrepôts pour le réassort entre entrepôts

Tout d’abord, assurez-vous que le paramètre Routes en plusieurs étapes est
activé en allant à Inventaire ‣ Configuration ‣ Paramètres et cochez la case
sous l’onglet Entrepôt. Vous disposerez alors d’options de configuration
supplémentaires lors de la création d’un deuxième entrepôt qui sont
nécessaires pour le réassort entre entrepôts.

Par défaut, un entrepôt principal est déjà configuré sur Odoo. Si aucun
entrepôt supplémentaire n’est déjà créé, faites-le maintenant à partir du
module Inventaire en sélectionnant Configuration ‣ Entrepôts ‣ Créer. Sinon,
sélectionnez l’entrepôt vers lequel les produits sont transférés à partir de
la page Entrepôts et cliquez ensuite sur Modifier pour modifier ses
paramètres. Configurez l’entrepôt comme suit :

  * Entrepôt : choisissez un nom qui n’est pas déjà utilisé pour un autre entrepôt (par ex. `Entrepôt alternatif`)

  * Nom court : choisissez un nom court par lequel l’entrepôt sera identifié (par ex. `ENT_ALT`)

Cliquez sur Enregistrer et le nouvel entrepôt sera créé. De plus, un nouveau
champ Réapprovisionner depuis apparaîtra sur le formulaire de l’entrepôt.
Cliquez sur Modifier et cochez ensuite la case à côté de l’entrepôt qui sera
utilisé pour réapprovisionner l’entrepôt qui est en cours de configuration.

![Un formulaire des paramètres de l'entrepôt configuré pour permettre le
réassort entre entrepôts.](../../../../../_images/new-warehouse-
configuration1.png)

Note

Dans le cadre de cette démonstration, l’entrepôt à partir duquel les produits
sont transférés (sortant) sera intitulé « San Francisco » et l’entrepôt vers
lequel les produits sont transférés (entrant) sera intitulé « San Francisco 2
».

## Configurer des produits pour le réassort entre entrepôts

Les produits doivent également être configurés correctement pour qu’ils
puissent être transférés entre entrepôts. Allez à Inventaire ‣ Produits ‣
Produits et sélectionnez un produit existant ou créez-en un nouveau, si
nécessaire.

Ensuite, sur la fiche du produit, allez à l’onglet Inventaire et cochez la
case de X : Réapprovisionner le produit depuis Y, _X_ étant l’entrepôt qui
reçoit les produits transférés et _Y_ étant l’entrepôt depuis lequel les
produits sont transférés.

![Cochez la case pour réapprovisionner un entrepôt depuis un
autre.](../../../../../_images/product-transfer-configuration.png)

## Réapprovisionner un entrepôt depuis un autre

À partir du module Inventaire, sélectionnez Produits ‣ Produits et choisissez
ensuite le produit à réapprovisionner. Cliquez sur le bouton Réapprovisionner
dans le coin supérieur gauche de la fiche du produit et complétez le
formulaire qui apparaît comme suit :

  * Quantité : le nombre d’unités qui seront envoyées à l’entrepôt à réapprovisionner

  * Date prévue : la date à laquelle le réassort est prévu

  * Entrepôt : l’entrepôt à réapprovisionner

  * Routes préférées : sélectionnez `X : Réapprovisionner le produit depuis Y`, _X_ étant l’entrepôt à réapprovisionner et _Y_ étant l’entrepôt depuis lequel le produit sera transféré

![Le formulaire pour réapprovisionner un
produit.](../../../../../_images/product-replenishment-form.png)

Cliquez sur Confirmer et un bon de livraison sera créé pour l’entrepôt
sortant, ainsi qu’une réception pour l’entrepôt qui recevra le produit. En
fonction des paramètres de configuration pour les entrepôts entrants et
sortants, le traitement des bons de livraison et des réceptions demande entre
une et trois étapes. Ce document explique en détail comment traiter les
livraisons et les réceptions en une seule étape.

### Traiter le bon de livraison

La première étape d’un réassort est le traitement de la livraison de
l’entrepôt depuis lequel le produit est transféré. Dans le tableau de bord
Inventaire, sélectionnez le bouton X à traiter sur la carte des Bons de
livraison pour l’entrepôt sortant, puis le bon de livraison créé pour le
réassort. Sur la page du bon de commande, cliquez sur le bouton Vérifier la
disponibilité dans le coin supérieur gauche pour réserver la quantité du
produit à transférer. Une fois la livraison expédiée, cliquez sur le bouton
Valider pour enregistrer les quantités expédiées.

![La carte des bons de livraison pour l'entrepôt
sortant.](../../../../../_images/delivery-orders-card.png)

### Traiter la réception

Une fois que les marchandises arrivent à l’entrepôt entrant, la réception
créée pour cet entrepôt doit également être traitée. Retournez au tableau de
bord Inventaire et sélectionnez le bouton X à traiter sur la carte des
Réceptions pour l’entrepôt entrant, puis la réception créée pour le réassort.
Sur la page des réceptions, cliquez sur le bouton Valider dans le coin
supérieur gauche de la page pour enregistrer les quantités reçues.

![La carte des bons de livraison pour l'entrepôt
sortant.](../../../../../_images/receipts-card.png)

Après avoir traité la réception, les produits transférés apparaîtront dans
l’inventaire de l’entrepôt entrant. Les stocks dans les deux entrepôts peuvent
être consultés en retournant à la fiche du produit et en sélectionnant le
bouton X unités disponibles en haut de l’écran.

## Automatiser le réassort entre entrepôts

Grâce aux règles de réassort, il est possible d’automatiser le processus de
réassort d’un entrepôt depuis un autre.

Pour commencer, allez à Inventaire ‣ Produits ‣ Produits et choisissez le
produit à réapprovisionner. Sur la fiche du produit, sélectionnez le bouton
intelligent Règles de réassort en haut du formulaire, et ensuite sur la page
suivante, cliquez sur Créer pour configurer le formulaire comme suit :

  * Emplacement : l’emplacement que la règle de réassort doit réapprovisionner lorsqu’elle est déclenchée : dans ce cas, l’entrepôt entrant.

  * Quantité min : lorsque la quantité disponible dans l’entrepôt entrant est inférieure à ce chiffre, la règle de réassort sera déclenchée

  * Quantité max : lorsque la règle de réassort est déclenchée, le produit sera réapprovisionné à l’entrepôt entrant jusqu’à hauteur de cette quantité

  * Quantité multiple : précisez si le produit doit être réapprovisionné par lots d’une certaine quantité ; par exemple, un produit peut être réapprovisionné par lots de 20

  * UdM : l’unité de mesure utilisée pour réapprovisionner le produit ; cette valeur peut être simplement `Unités` ou une unité de mesure spécifique pour le poids, la longueur, etc.

![Une règle de réassort totalement
configurée](../../../../../_images/reordering-rule-configuration.png)

Terminez par cliquer sur Enregistrer et la règle de réassort sera créée. À
présent, lorsque le planificateur s’exécute automatiquement chaque jour, un
transfert sera créé pour chaque règle de réassort qui a été déclenchée.

Astuce

Pour manuellement déclencher des règles de réassort, allez au module
Inventaire et sélectionnez Opérations ‣ Lancer le planificateur, cliquez sur
le bouton vert Lancer le planificateur dans la fenêtre contextuelle.

Après avoir lancé le planificateur, un bon de livraison et une réception
seront créés pour les entrepôts entrants et sortants, respectivement. À la
fois le bon de commande et la réception doivent être traités selon la même
méthode que celle décrite ci-dessus.

