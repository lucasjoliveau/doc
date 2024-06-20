# Réceptions et bons de livraison

Il existe plusieurs façons de gérer comment un entrepôt reçoit des produits
(réceptions) et expédie des produits (livraisons). En fonction de plusieurs
facteurs, tels que le type de produits stockés et vendus, la taille de
l’entrepôt et le nombre de réceptions et bons de livraisons confirmés par
jour, la façon dont les produits sont gérés lors de leur entrée et sortie de
l’entrepôt peut différer grandement. Vous pouvez configurer plusieurs
paramètres pour les réceptions et les livraisons et il n’est pas nécessaire de
les configurer pour qu’elles aient le même nombre d’étapes.

Pour plus d'infos

  * [Utiliser des routes (Tutoriel eLearning)](https://www.odoo.com/slides/slide/using-routes-1018)

  * [Routes de flux tirés & poussés (Tutoriel eLearning)](https://www.odoo.com/slides/slide/push-pull-rules-1024)

## Choisir le bon flux d’inventaire pour gérer les réceptions et les
livraisons

Par défaut, Odoo gère les expéditions et les réceptions de trois façons
différentes : en une, deux ou trois étapes. La configuration la plus simple
est une étape, qui est la configuration par défaut. Chaque étape
supplémentaire nécessaire pour les réceptions ou les expéditions d’un entrepôt
ajoute une couche supplémentaire d’opérations à effectuer avant qu’un produit
soit expédié ou réceptionné. Ces configurations dépendent entièrement des
exigences pour les produits stockés, tels que des contrôles qualité sur les
produits reçus ou un emballage spécial pour les produits expédiés.

### Flux en une étape

Les règles de réception et d’expédition dans le cadre d’une configuration en
une étape sont les suivantes :

  * **Réception** : Réceptionnez les produits directement dans le stock. Il n’y a aucune étape intermédiaire entre la réception et le stock, telle qu’un transfert vers un emplacement de contrôle qualité.

  * **Shipping** : Ship products directly from stock. No intermediate steps between stock and shipping occur, such as a transfer to a packing location.

  * Peut uniquement être utilisé si vous n’utilisez pas les stratégies d’enlèvement FIFO, LIFO ou FEFO.

  * Les réceptions et/ou les livraisons sont gérées rapidement.

  * Recommandé pour les petits entrepôts avec de faibles niveaux de stock et des articles non périssables.

  * Les articles directement réceptionnés ou expédiés dans/depuis le stock.

Pour plus d'infos

[Traiter des réceptions et des livraisons en une
étape](receipts_delivery_one_step.html)

### Flux en deux étapes

Les règles de réception et d’expédition dans le cadre d’une configuration en
deux étapes sont les suivantes :

  * **Emplacement d’entrée + stock**. Amenez des produits à un emplacement d’entrée _avant_ de les mettre en stock. Les produits peuvent être organisés par différents emplacements de stockage internes, tels que plusieurs étagères, congélateurs et zones fermées, avant d’être stockés dans l’entrepôt.

  * **Transfert + expédition** : Amenez des produits à un emplacement de sortie avant l’expédition. Les colis peuvent être organisés par différents transporteurs ou quais d’expédition avant d’être expédiés.

  * Exigence minimale pour utiliser des numéros de lot ou des numéros de série pour suivre des produits dans le cadre d’une stratégie d’enlèvement FIFO, LIFO ou FEFO.

  * Recommandé pour des entrepôts plus grands avec des niveaux de stock élevés ou pour le stockage d’articles volumineux (matelas, gros meubles, machines lourdes, etc.).

  * Les produits reçus ne seront pas disponibles pour la fabrication, l’expédition, etc. tant qu’ils n’auront pas été transférés dans le stock.

Pour plus d'infos

[Traiter les réceptions et les livraisons en deux
étapes](receipts_delivery_two_steps.html#inventory-receipts-delivery-two-
steps)

### Flux en trois étapes

Les règles de réception et d’expédition dans le cadre d’une configuration en
trois étapes sont les suivantes :

  * **Emplacement d’entrée + contrôle qualité + stock** : Recevez des produits à l’emplacement d’entrée, transférez-les vers une zone de contrôle qualité et mettez en stock les produits qui ont passé l’inspection.

  * **Transfert + colisage + expédition** : Transférez des produits en fonction de leur stratégie d’enlèvement, emballez-les dans une zone de colisage dédiée et amenez-les à un emplacement de sortie pour les expédier.

  * Peut être utilisé pour le suivi des produits par lots ou numéros de série dans le cadre d’une stratégie d’enlèvement FIFO, LIFO ou FEFO.

  * Recommandé pour les très grands entrepôts avec des niveaux de stock très élevés.

  * Nécessaire pour tout entrepôt devant effectuer des contrôles qualité avant de mettre les articles en stock.

  * Les produits reçus ne seront pas disponibles pour la fabrication, l’expédition, etc. tant qu’ils n’auront pas été transférés dans le stock.

Pour plus d'infos

  * [Traiter les réceptions en trois étapes](receipts_three_steps.html#inventory-receipts-three-steps)

  * [Traiter les livraisons en trois étapes](delivery_three_steps.html#inventory-delivery-three-steps)

  *[FIFO]: First In, First Out
  *[LIFO]: Last In, First Out
  *[FEFO]: First Expired, First Out

