# Cibler un public

Proposer des campagnes de marketing au bon audience est primordial lorsqu’on
cherche à développer une entreprise. L’application _Marketing Automation_
d’Odoo aide les agents de marketing à y parvenir en fournissant des outils de
filtrage, qui peuvent être aussi simples (ou aussi complexes) que nécessaire,
pour atteindre les bons clients au bon moment.

## Configurer des filtres de ciblage

Lors de la configuration des filtres de ciblage sur une campagne marketing,
certaines options sont accompagnées d’une icône > (flèche). L’icône > (flèche)
signifie que le filtre en question contient des paramètres plus précis qui
peuvent être personnalisés.

![Le menu déroulant des filtres dans l'application Marketing
Automation.](../../../../_images/marketing-filters.png)

Les filtres peuvent être étendus en ajoutant des _branches_ et des _nœuds_. Un
_nœud_ ajoute un autre paramètre de filtrage à un groupe de conditions de
ciblage (par ex. une nouvelle ligne) et une _branche_ crée un groupe de
paramètres plus précis, permettant aux filtres d’être regroupés avec les
instructions UNE ou TOUTES.

Chaque fois qu’une nouvelle branche est créée, il y a deux options :

  * Soit les enregistrements correspondent à TOUS les critères des règles à venir (créer une instruction ET où _tous_ les critères doivent correspondre).

  * Soit les enregistrements correspondent à UN critère pour les règles à venir (créer une instruction OU où _un seul_ des critères doit correspondre).

Pour passer d’une option à l’autre, cliquez simplement sur l’icône du menu
déroulant dans la case verte et sélectionnez UNE ou TOUTES.

Pour ajouter un nœud, cliquez sur l’icône ➕ (signe plus) et pour ajouter une
autre branche, cliquez sur l’icône ⋯ (ellipse). Pour exclure un nœud ou une
branche, cliquez sur l’icône ✖ (supprimer) pour le/la supprimer.

![Le menu déroulant des filtres dans l'application Marketing
Automation.](../../../../_images/marketing-filter-nodes.png)

## Cas d’utilisation

Les scénarios suivants décrivent différentes combinaisons de filtres qu’une
campagne de marketing peut utiliser couramment.

### Scénario #1 : Cibler les nouvelles opportunités dans le pipeline

En _mode édition_ sur un formulaire de modèle de campagne (en cliquant sur le
bouton Modifier), sélectionnez le champ Cible et cliquez sur Recherche avancée
dans le menu déroulant. Recherchez ensuite Piste/Opportunité, et sélectionnez-
la.

Ensuite, cliquez sur Ajouter un filtre dans le champ Filtre. Cliquez sur
l’option de filtrage ID par défaut dans la première partie de l’équation.
Cette opération fait apparaître un menu déroulant rempli d’options de
filtrage. Dans ce menu déroulant, faites défiler jusqu’à (ou recherchez) Type.

Laissez la deuxième partie de l’équation sur l’icône 🟰 (signe égal) par
défaut.

Modifiez ensuite la troisième (et dernière) partie de l’équation de Piste en
Opportunité. Le nombre d”Enregistrements qui correspondent à cette équation
spécifique change au fur et à mesure que l’équation est personnalisée.

Ajoutez un autre nœud à ce filtre en cliquant sur l’icône ➕ (signe plus) à
droite de l’équation.

Les « nouvelles » opportunités étant ciblées par ce filtre, le deuxième nœud
se concentrera _uniquement_ sur les opportunités qui se trouvent dans l’étape
Nouveau du pipeline. Pour ce faire, sélectionnez ID par défaut dans la
première partie de l’équation et faites défiler jusqu’à (ou recherchez) Étape
dans le menu déroulant du champ.

De nouveau, laissez la deuxième partie de l’équation sur l’icône 🟰 (signe
égal).

Finalement, mettez en évidence la valeur par défaut dans la troisième (et
dernière) partie de l’équation et tapez `Nouveau`. Une fois cette étape
terminée, Odoo ciblera uniquement les opportunités qui se trouvent dans
l’étape « Nouveau » du pipeline.

![Un scénario standard utilisant des filtres dans l'application Marketing
Automation d'Odoo.](../../../../_images/filters-opportunities.png)

### Scénario #2 : Cibler les participants à un événement qui ont acheté un
ticket spécifique

En _mode édition_ sur un formulaire de modèle de campagne (en cliquant sur le
bouton Modifier), sélectionnez le champ Cible et cliquez sur Recherche avancée
dans le menu déroulant. Ensuite, faites défiles jusqu’à (ou recherchez)
Événement, et sélectionnez-la.

Ensuite, cliquez sur Ajouter un filtre dans le champ Filtre. Cliquez sur
l’option de filtrage ID par défaut dans la première partie de l’équation.
Cette opération fait apparaître un menu déroulant rempli d’options de
filtrage. Dans ce menu déroulant, descendez jusqu’à (ou cherchez) Événement.

Cliquez sur l’icône 🟰 (signe égal) par défaut dans la deuxième partie de
l’équation. Cette opération fait apparaître un menu déroulant. Dans ce menu,
sélectionnez contient.

Dans la troisième (et dernière) partie vide de l’équation, tapez le nom de
l’événement que vous voulez qu’Odoo prenne en compte pour ce filtre de
campagne.

Ajoutez ensuite un autre nœud à ce filtre en cliquant sur l’icône ➕ (signe
plus) à droite de l’équation.

Le deuxième nœud permettra de cibler cette campagne sur les participants qui
achètent un type de ticket spécifique pour l’événement mentionné dans la
première équation.

Pour ce faire, sélectionnez ID par défaut dans la première partie de
l’équation et faites défiler jusqu’à (ou recherchez) Ticket d’événement dans
le menu déroulant. Ensuite, dans ce même menu déroulant, sélectionnez Nom.

De nouveau, cliquez sur l’icône 🟰 (signe égal) par défaut dans la deuxième
partie de l’équation et sélectionnez contient.

Enfin, dans la troisième (et dernière) partie de la deuxième équation, qui est
vide, tapez le nom du type de ticket qui doit être utilisé pour le filtre.
Dans ce cas, Standard est le nom du type de ticket d’événement pour cet
exemple de filtre.

![Un filtre de ticket d'événement dans l'application Marketing Automation
d'Odoo.](../../../../_images/filters-event-ticket.png)

