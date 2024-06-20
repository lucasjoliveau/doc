# Créer des demandes de prix alternatives pour plusieurs fournisseurs

Parfois, les entreprises souhaitent demander des devis à plusieurs
fournisseurs en même temps, en les invitant à soumettre des offres pour des
biens ou des services similaires en une seule fois. Cela aide les entreprises
à sélectionner les fournisseurs les moins chers (et les plus rapides), en
fonction de leurs besoins spécifiques.

Dans Odoo, cela peut se faire en ajoutant des demandes de prix alternatives
pour différentes fournisseurs. Une fois que vous recevez une réponse de chaque
fournisseur, vous pouvez comparer les lignes de produits de chaque demande de
prix et décider quels produits vous allez acheter auprès de quels
fournisseurs.

Parfois appelé un _appel d’offres_ , ce processus est principalement utilisé
par les organisations du secteur public, qui sont légalement tenues de
l’utiliser lorsqu’elles effectuent un achat. Cependant, les entreprises
privées peuvent également utiliser des demandes de prix alternatives pour
dépenser efficacement leur argent.

Pour plus d'infos

[Utiliser des contrats-cadres pour créer des conventions d’achat avec des
fournisseurs](blanket_orders.html)

## Configurer les paramètres de la convention d’achat

Pour créer des demandes de prix alternatives directement à partir d’un devis,
vous devez d’abord activer la fonctionnalité _Conventions d’achat_ dans
l’application _Achats_. Pour ce faire, allez à Achats ‣ Configuration ‣
Paramètres et dans la section Commandes, cochez la case à côté de Conventions
d’achat. Ceci permet d’activer la possibilité de créer des demandes de prix
alternatives et des _contrats-cadres_.

![La fonctionnalité Conventions d'achat activée dans les paramètres de
l'application Achats.](../../../../_images/calls-for-tenders-settings-
page.png)

Astuce

Pour gagner du temps lors d’un _appel d’offres_ , il est possible de définir
des fournisseurs, des prix et des délais de livraison personnalisés dans
l’onglet Achats d’une fiche de produit. Pour ce faire, allez à Achats ‣
Produits ‣ Produits et sélectionnez un produit à modifier. À partir de la
fiche de produit, cliquez sur l’onglet Achat et cliquez sur Ajouter une ligne.
Dans le menu déroulant, choisissez un fournisseur à définir dans la colonne
Fournisseur et définissez un Prix et un Délai de livraison si vous le
souhaitez. En cliquant sur l’icône des options supplémentaires (deux points),
vous obtiendrez des options de visibilité supplémentaires à ajouter à la
ligne.

## Créer une demande de prix

Pour créer une nouvelle demande de prix, allez à l’application Achats et
cliquez sur Nouveau.

Ajoutez ensuite des informations au formulaire de demande de prix :
sélectionnez un fournisseur dans le menu déroulant à côté du champ Fournisseur
et cliquez sur Ajouter un produit pour choisir un produit dans le menu
déroulant dans la colonne Produit. Ensuite, définissez la quantité que vous
voulez acheter dans la colonne Quantité et modifiez le prix d’achat dans la
colonne Prix unitaire, si vous le souhaitez.

En cliquant sur l’icône des options supplémentaires (deux points), vous
obtiendrez des options de visibilité supplémentaires à ajouter à la ligne.
Répétez ces étapes pour ajouter autant d’options que vous le souhaitez, y
compris l”UdM (Unité de mesure) dans laquelle vous achetez les produits et la
date d”Arrivée prévue.

Une fois que vous êtes prêt, cliquez sur Envoyer par email. Une fenêtre
contextuelle permettant de Rédiger un email apparaît alors, dans laquelle vous
pouvez personnaliser le message destiné au vendeur. Une fois prêt, cliquez sur
Envoyer. La demande de prix est alors transformée en bon de commande et un
email est envoyé au fournisseur répertorié sur le bon de commande.

![Fenêtre contextuelle permettant de rédiger et d'envoyer un email de
devis.](../../../../_images/calls-for-tenders-email-popup.png)

Note

L’envoi d’emails à chaque fournisseur peut s’avérer utile lors de la création
de demandes de prix alternatives, car les fournisseurs peuvent confirmer si
leurs prix antérieurs sont toujours valables aujourd’hui, ce qui peut aider
les entreprises à choisir les meilleurs offres pour elles.

## Créer des alternatives à une demande de prix

Une fois qu’un bon de commande est créé et envoyé par email à un fournisseur,
il est possible de créer des demandes de prix alternatives et de les envoyer à
d’autres fournisseurs afin de comparer les prix, les délais de livraison et
d’autres facteurs et de décider auprès de quel fournisseur commander tel ou
tel produit.

Pour créer des demandes de prix alternatives, cliquez sur l’onglet
Alternatives du formulaire de bon de commande, puis cliquez sur Créer une
alternative. Une fenêtre contextuelle permettant de Créer une alternative
apparaît alors.

![Une fenêtre contextuelle d'appels d'offres s'affiche pour créer un devis
alternatif.](../../../../_images/calls-for-tenders-alternatives-popup.png)

Dans cette fenêtre, sélectionnez un nouveau/différent fournisseur dans le menu
déroulant à côté du champ Fournisseur pour lui assigner ce devis alternatif.

À côté de ce champ se trouve une case Copier les produits qui est cochée par
défaut. Si cette option est activée, les quantités de produit du bon de
commande d’origine sont copiées dans le bon de commande alternatif. Pour ce
premier devis alternatif, laissez la case cochée. Une fois que vous avez
terminé, cliquez sur Créer une alternative. Vous accéderez alors à un nouveau
bon de commande vierge.

Puisque la case Créer une alternative est restée cochée, ce nouveau formulaire
de bon de commande est déjà complété avec les mêmes produits, quantités et
autres détails que le bon de commande d’origine précédent.

Note

Lorsque la case Copier les produits est cochée lors de la création d’un devis
alternatif, il n’est pas nécessaire d’ajouter des produits supplémentaires au
bon de commande sauf si vous le souhaitez. Cependant, si un fournisseur choisi
n’est pas répertorié dans la colonne Fournisseur sur une fiche de produit
reprise sur le bon de commande, les valeurs définies sur la fiche du produit
sont reportées sur le bon de commande et doivent être modifiées manuellement,
si vous le souhaitez.

Une fois que vous êtes prêt, créez un deuxième devis alternatif en cliquant
sur l’onglet Alternatives et encore une fois sur Créer une alternative. La
fenêtre contextuelle permettant de Créer une alternative apparaît de nouveau.
Cette fois, choisissez un fournisseur différent dans le menu déroulant à côté
de Fournisseur et cette fois, _décochez_ la case Copier les produits. Cliquez
ensuite sur Créer une alternative.

Astuce

Si un devis alternatif doit être supprimé de l’onglet Alternatives, vous
pouvez le supprimer individuellement en cliquant sur l’icône Supprimer (X) au
bout de sa ligne.

Un troisième bon de commande est ainsi créé. Mais, puisque les quantités de
produits du bon de commande d’origine n’ont _pas_ été recopiées, les lignes de
produits sont vides et de nouveaux produits doivent être ajoutés en cliquant
sur Ajouter un produit et en sélectionnant les produits souhaités dans le menu
déroulant. Une fois que vous avez ajouté le nombre souhaité de produits,
cliquez sur Envoyer par email.

![Devis alternatif vierge avec des alternatives dans le fil
d'Ariane.](../../../../_images/calls-for-tenders-blank-alternative.png)

Cela fait apparaître une fenêtre contextuelle permettant de Rédiger un email,
dans laquelle vous pouvez personnaliser le message destiné au fournisseur. Une
fois prêt, cliquez sur Envoyer pour envoyer un email au fournisseur répertorié
sur le bon de commande.

À partir de ce tout nouveau bon de commande, cliquez sur l’onglet
Alternatives. Dans cet onglet, les trois bons de commande figurent dans la
colonne Référence. De plus, les fournisseurs sont répertoriés dans la colonne
Fournisseur et le Total de la commande et le Statut des commandes figurent
également dans les lignes.

## Lier une nouvelle demande de prix à des devis existants

La création de devis alternatifs directement à partir d’un bon de commande
sous l’onglet Alternatives est la manière la plus simple de créer et de lier
des devis. Cependant, il est possible de lier des demandes de prix distinctes
_après_ coup, même si elles ont été créées totalement séparément au départ.

Pour créer une nouvelle demande de prix, allez à l’application Achats et
cliquez sur Nouveau.

Ajoutez ensuite des informations au formulaire de demande de prix :
sélectionnez un fournisseur dans le menu déroulant à côté du champ Fournisseur
et cliquez sur Ajouter un produit pour choisir un produit dans le menu
déroulant dans la colonne Produit. Ensuite, définissez la quantité que vous
voulez acheter dans la colonne Quantité et modifiez le prix d’achat dans la
colonne Prix unitaire, si vous le souhaitez.

Une fois que vous êtes prêt, cliquez sur Envoyer par email. Cela fait
apparaître une fenêtre contextuelle permettant de Rédiger un email, dans
laquelle vous pouvez personnaliser le message destiné au fournisseur. Une fois
le message prêt, cliquez sur Envoyer pour envoyer un email au fournisseur
répertorié sur le bon de commande.

Ensuite, cliquez de nouveau sur l’onglet Alternatives. Puisque ce nouveau bon
de commande a été créé séparément, il n’y a pas encore d’autres bons de
commande liés. Pour lier ce bon de commande aux alternatives créés
précédemment, cliquez sur Lier à une demande de prix existante sur la première
ligne de la colonne Fournisseur.

![Fenêtre contextuelle pour lier un nouveau devis aux demandes de devis
existantes.](../../../../_images/calls-for-tenders-link-existing-rfq.png)

Une nouvelle fenêtre contextuelle Ajouter : Bons de commande alternatifs
s’affiche. Sélectionnez les trois bons de commande créés précédemment et
cliquez sur Sélectionner. Ces trois bons de commande sont maintenant copiés
dans ce bon de commande sous l’onglet Alternatives.

Astuce

Si un grand nombre de bons de commande est en cours de traitement et que les
bons de commande précédents sont introuvables, essayez de cliquer sur
Regrouper par ‣ Fournisseur en dessous de la barre de recherche en haut de la
fenêtre contextuelle pour regrouper les bons de commande en fonction des
fournisseurs sélectionnés dans les bons de commande précédents.

## Comparer les lignes de produits

Lorsque plusieurs demandes de devis sont liées en tant qu’alternatives, elles
peuvent être comparées côte à côte afin de déterminer quels fournisseurs
proposent les meilleures offres pour quels produits. Pour comparer chaque
devis, allez à l’application Achats et sélectionnez l’un des devis créés
précédemment.

Ensuite, cliquez sur l’onglet Alternatives pour voir toutes les demandes de
prix liées. Ensuite, dans l’onglet Créer une alternative, cliquez sur Comparer
les lignes de produits. Vous accédez ainsi à la page permettant de comparer
les lignes de commande.

![La page permettant de comparer les lignes de produits des demandes de prix
alternatives.](../../../../_images/calls-for-tenders-compare-product-
lines.png)

La page permettant de comparer les lignes de commande est regroupée par défaut
par Produit. Chaque produit repris sur l’une des demandes de prix est affiché
dans son propre menu déroulant, avec tous les numéros de bon de commande dans
la colonne Référence.

Les colonnes supplémentaires sur cette page comprennent le Fournisseur auprès
duquel les produits ont été commandés, le Statut du devis (c’est-à-dire,
demande de prix, demande de prix envoyée) ; la Quantité des produits commandés
auprès de chaque fournisseur ; le Prix unitaire par produit et le prix total
de la commande, et bien plus encore.

Note

Pour supprimer des lignes de produits de la page permettant de comparer les
lignes de commande, cliquez sur Effacer à l’extrême droite de cette ligne de
produit. Cette opération supprime ce produit de la page en tant qu’option de
choix et fait passer à **0** le prix total de ce produit sur la page. Sur le
formulaire de bon de commande sur lequel figurait ce produit, sa quantité
commandée est également ramenée à **0**.

Une fois que les meilleures offres ont été identifiées, à la fin de chaque
ligne, il est possible de sélectionner des produits individuels en cliquant
sur Choisir. Une fois que tous les produits souhaités ont été choisis, cliquez
sur Demandes de prix (dans le fil d’Ariane en haut de la page) pour revenir à
une vue d’ensemble de toutes les demandes de prix.

## Annuler (ou conserver) des alternatives

Maintenant que les produits souhaités ont été choisis, en fonction des
fournisseurs qui ont fait la meilleure offre, les autres demandes de prix
(pour lesquelles aucun produit n’a été choisi) peuvent être annulées.

Dans la colonne Total, à l’extrême droite de chaque ligne, les commandes pour
lesquelles aucun produit n’a été choisi ont automatiquement vu leur coût total
fixé à **0**. Même si elles n’ont pas encore été annulées, elles pourront
l’être à terme sans répercussions, _une fois que_ tous les bons de commande
souhaités ont été confirmés.

![Devis annulés dans la vue d'ensemble de l'application
Achats.](../../../../_images/calls-for-tenders-canceled-quotes.png)

Pour confirmer un devis qui contient les quantités de produit choisies,
cliquez sur l’un d’entre eux. Cliquez ensuite sur Confirmer la commande. Une
fenêtre contextuelle d”Avertissement concernant l’alternative apparaît. De là,
vous pouvez décider d”Annuler les alternatives ou de Conserver les
alternatives. Si ce bon de commande ne doit _pas_ être confirmé, cliquez sur
Annuler.

Annuler les alternatives annule automatiquement les bons de commande
alternatifs. Conserver les alternatives laisse les bons de commande
alternatifs ouverts, de sorte qu’il est toujours possible d’y accéder si des
quantités supplémentaires de produits doivent être commandées. Une fois que
tous les produits sont commandés, vous pouvez choisir d”Annuler les
alternatives à partir de n’importe quel bon de commande ouvert.

Pour afficher un formulaire détaillé d’une demande de prix répertoriée,
cliquez sur la ligne correspondant à ce devis. Une fenêtre contextuelle Ouvrir
: Bons de commande alternatifs s’affiche, dans laquelle tous les détails de ce
devis particulier peuvent être consultés. Cliquez sur Fermer lorsque vous avez
terminé.

![Fenêtre contextuelle pour conserver ou annuler des demandes de prix
alternatives.](../../../../_images/calls-for-tenders-keep-cancel-
alternatives.png)

Dans la fenêtre contextuelle Avertissement concernant l’alternative, cliquez
sur Conserver les alternatives pour laisser tous les devis alternatifs ouverts
pour l’instant. Cliquez ensuite sur Demandes de prix (dans le fil d’Ariane en
haut de la page) pour retourner à la vue d’ensemble des demandes de prix.

Cliquez sur le(s) devis restant(s) qui contien(nen)t des produits à commander
et cliquez sur Confirmer la commande. Une fenêtre contextuelle Avertissement
concernant l’alternative s’affiche de nouveau. Cette fois, cliquez sur Annuler
les alternatives pour annuler toutes les autres demandes de prix alternatives
liées à ce devis.

Enfin, cliquez sur Demandes de prix (dans le fil d’Ariane, en haut de la page)
pour retourner à la vue d’ensemble de toutes les demandes de prix. Les
commandes annulées sont grisées et répertoriées avec le statut Annulé dans la
colonne Statut à l’extrême droite de leurs lignes.

Maintenant que toutes les quantités de produits ont été commandées, le
processus d’achat peut se poursuivre jusqu’à son terme, jusqu’à ce que les
produits soient reçus dans l’entrepôt.

