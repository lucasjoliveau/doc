# Rapports PDF

Avec Studio, vous pouvez modifier des rapports PDF existants (par ex,
commandes et devis) ou en créer de nouveaux.

Important

Pour modifier un rapport PDF standard, il est fortement recommandé de le
**dupliquer** et de modifier la version dupliquée, puisque les changements
apportés aux rapports standards seront annulés après une mise à niveau d’Odoo.
Pour dupliquer un rapport, allez à Studio ‣ Rapports. Passez le curseur de la
souris sur le coin supérieur droit du rapport, cliquez sur l’icône d’ellipse
verticale (⋮), et sélectionnez Dupliquer.

![Dupliquer un rapport PDF](../../_images/duplicate-report.png)

## Présentation par défaut

La mise en page par défaut des rapports est gérée en dehors de Studio. Allez à
Paramètres ‣ Sociétés : Mise en page du document ‣ Configurer la mise en page
du document. Les paramètres de la mise en page s’appliquent à tous les
rapports, mais uniquement de la société en vigueur.

Astuce

Utilisez Télécharger un aperçu du PDF pour voir comment les différents
paramètres affectent la mise en page d’un exemple de facture.

### Agencement

Quatre mises en page sont disponibles.

LightBoxedBoldStriped

![Exemple d'une mise en page légère du rapport](../../_images/light.png)

![Exemple d'une mise en page encadrée du rapport](../../_images/boxed.png)

![Exemple d'une mise en page en gras du rapport](../../_images/bold.png)

![Exemple d'une mise en page rayée d'un rapport](../../_images/striped.png)

### Fonte

Sept polices sont disponibles. Cliquez sur les liens ci-dessous pour les
afficher dans [Google Fonts](https://fonts.google.com/).

  * [Lato](https://fonts.google.com/specimen/Lato#type-tester)

  * [Roboto](https://fonts.google.com/specimen/Roboto#type-tester)

  * [Open Sans](https://fonts.google.com/specimen/Open+Sans#type-tester)

  * [Montserrat](https://fonts.google.com/specimen/Montserrat#type-tester)

  * [Oswald](https://fonts.google.com/specimen/Oswald#type-tester)

  * [Raleway](https://fonts.google.com/specimen/Raleway#type-tester)

  * [Tajawal](https://fonts.google.com/specimen/Tajawal#type-tester)

Note

Tajawal prend en charge les caractères arabes et latins.

### Logo de la société

Chargez un fichier image pour ajouter un logo de la société.

Note

Cette opération ajoute le logo à l’enregistrement de la société sur le modèle
de la _Société_ , auquel vous pouvez accéder en allant aux Paramètres généraux
‣ Sociétés ‣ Mise à jour de l’information.

### Couleurs

Changez les couleurs primaires et secondaires utilisées dans les rapports pour
mettre en évidence les éléments importants. Les couleurs par défaut sont
générées automatiquement sur la base des couleurs du logo.

### Arrière-plan de la mise en page

Changez l”Arrière-plan de la mise en page du rapport :

  * Vide : rien n’est affiché.

  * Géométrique : une image représentant des formes géométriques est affichée en arrière-plan.

  * Personnalisé : chargez une image d’arrière-plan personnalisée.

### Slogan de la société

Le Slogan de la société s’affiche dans l’en-tête des Rapports externes. Vous
pouvez ajouter plusieurs lignes de texte.

### Détails de la société

Les Détails de la société s’affichent dans l’en-tête des Rapports externes.
Vous pouvez ajouter plusieurs lignes de texte.

### Pied de page

Utilisez le champ Pied de page pour insérer un texte dans les pieds de page
des Rapports externes”. Vous pouvez ajouter plusieurs lignes de texte.

### Format de papier

Utilisez le champ Format de papier pour changer le format du papier des
rapports. Vous pouvez sélectionner A4 (21 cm x 29.7 cm) ou US Letter (21.59 cm
x 27.54 cm).

Astuce

Vous pouvez changer le format de papier de chaque rapport. Ouvrez
l’application contenant le rapport, puis cliquez sur Studio ‣ Rapports ‣
Sélectionnez ou créez un rapport ‣ Report ‣ Sélectionnez un format de papier.

![Fenêtre contextuelle de configuration de la mise en page par défaut des
rapports PDF](../../_images/default-layout.png)

## En-tête et pied de page

Lors de la création d’un nouveau rapport dans Studio, vous devez choisir entre
trois styles de rapport. Ce choix déterminera uniquement ce qui s’affiche dans
l’en-tête et le pied de page. Pour ce faire, allez à l’application dans
laquelle vous voulez ajouter un nouveau rapport, puis cliquez sur le bouton
Studio ‣ Rapports ‣ Créer et sélectionnez Externe, Interne ou Vide.

### Externe

L’en-tête affiche le Logo de la société de la société et plusieurs valeurs
définies dans le modèle de la _Société_ : le nom de la société, le numéro de
téléphone, l”email, et le site web.

Astuce

Pour modifier les informations d’une société, allez à Paramètres ‣ Sociétés ‣
Mise à jour de l’information.

![Exemple d'une en-tête externe](../../_images/external-header.png)

Le pied de page affiche les valeurs définies dans les champs Pied de page,
Détails de la société et Slogan de la société, ainsi que le numéro de page.

![Exemple d'un pied de page externe](../../_images/external-footer.png)

### Interne

L’en-tête affiche la date et l’heure actuelles de l’utilisateur, le nom de la
société et le numéro de page.

Il n’y a pas de pied de page.

### Vide

Il n’y a ni en-tête ni pied de page.

## Ajouter un onglet

Après avoir ouvert un rapport existant ou créé un nouveau rapport, allez à
l’onglet Ajouter pour ajouter ou modifier des éléments. Les éléments sont
organisés en quatre catégories : Bloc, Inline, Tableau, et Colonne.

### Bloc

Les éléments de type bloc commencent sur une nouvelle ligne et occupent toute
la largeur de la page.

Astuce

Vous pouvez définir la largeur d’un élément en le sélectionnant et en accédant
à l’onglet Options.

  * Texte : ajoutez n’importe quel texte en utilisant une petite taille de police par défaut.

  * Bloc de titre : ajoutez n’importe quel texte en utilisant une police de taille supérieure par défaut.

  * Image : ajoutez une image. Vous pouvez soit en charger une depuis votre appareil, en ajouter une depuis une URL ou en sélectionner une qui existe déjà dans votre base de données.

  * Champ : permet d’ajouter de manière dynamique la valeur d’un champ.

  * Champ & Libellé : permet d’ajouter de manière dynamique la valeur et le libellé d’un champ.

  * Bloc d’adresse : permet d’ajouter de manière dynamique les valeurs éventuelles d’un contact (modèle `res.partner`) : _Nom_ , _Adresse_ , _Téléphone_ , _Mobile_ et _Email_.

![Exemple d'un bloc d'adresse](../../_images/address-block.png)

### Inline

Les éléments de type inline sont utilisés autour d’autres éléments. Ils ne
commencent pas sur une nouvelle ligne et la largeur s’adapte à la longueur du
contenu.

Astuce

Vous pouvez définir la largeur et les marges d’un élément en le sélectionnant
et en allant à l’onglet Options.

  * Texte : ajoutez n’importe quel texte en utilisant une petite taille de police par défaut.

  * Champ : permet d’ajouter de manière dynamique la valeur d’un champ.

### Tableau

Les éléments de type tableau sont utilisés ensemble pour créer un tableau de
données.

  * Tableau de données : permet de créer un tableau et d’ajouter de manière dynamique une première colonne affichant les valeurs de _nom_ d’un champ [Many2Many](fields.html#studio-fields-relational-fields-many2many) ou [One2Many](fields.html#studio-fields-relational-fields-one2many) sur votre modèle.

![Exemple d'un tableau de données](../../_images/data-table.png)

  * Champ colonne : permet d’ajouter une nouvelle colonne au tableau affichant les valeurs d’un [champ associé](fields.html#studio-fields-relational-fields-related-field) à celui utilisé pour créer le tableau de données.

  * Texte dans cellule : permet d’ajouter n’importe quel texte dans une cellule existante.

  * Champ dans cellule : permet d’ajouter, dans une cellule existante, les valeurs d’un [champ associé](fields.html#studio-fields-relational-fields-related-field) à celui utilisé pour créer le tableau de données.

  * Sous-total & Total : permet d’ajouter la valeur d’un champ Total existant. S’il existe un champ Taxes, les montants hors taxes et toutes taxes comprises sont ajoutés avant le montant total.

### Colonne

Les colonnes sont utilisées pour ajouter plusieurs éléments de bloc sur la
même ligne.

  * Deux colonnes : permet d’ajouter n’importe quel texte dans deux colonnes différentes.

  * Trois colonnes : permet d’ajouter n’importe quel texte dans trois colonnes différentes.

## Onglet Rapport

Plusieurs options de configuration sont disponibles sous l’onglet Rapport.

  * Nom : modifiez le nom du rapport. Le nouveau nom s’applique partout (dans Studio, sous le bouton Imprimer et pour le nom du fichier PDF).

  * Format de papier : modifiez le format papier du rapport.

  * Ajouter à l’impression : permet d’ajouter le rapport sous le bouton 🖶 Imprimer disponible sur l’enregistrement.

  * Limit visibility to groups: limit the availability of the PDF report to specific [user groups](../general/users/access_rights.html).

## Onglet Options

Sélectionnez un élément sur le rapport pour accéder aux options d’un élément
et les modifier.

![L'onglet Options pour un élément de texte](../../_images/text-options-
tab.png)

Note

Vous pouvez sélectionner et modifier plusieurs éléments à la fois en cliquant
sur les différentes sections ou divisions (par ex. `div`, `table`, etc.).

Les options les plus courantes sont représentées ci-dessous :

  * Marges : permet d’ajouter un espace en haut, à droite, en bas, et à gauche de l’élément.

  * Largeur : permet de définir la largeur maximale de l’élément.

  * Visible si : permet de définir sous quelle(s) condition(s) l’élément doit être affiché.

  * Visible for: set for which [users groups](../general/users/access_rights.html) the element should be displayed.

  * Supprimer de la vue : permet de supprimer l’élément de la vue du rapport.

  * Décoration du texte : mettre la police en gras, en italique et la souligner.

  * Alignement : permet d’aligner l’élément à gauche, au centre ou à droite du rapport.

  * Police de caractères : permet d’utiliser l’un des polices par défaut.

  * Couleurs : permet de changer la couleur de la police et la couleur de fond.

Note

Il se peut que vous deviez sélectionner une section ou une division au-dessus
de l’élément que vous voulez modifier pour voir certaines des options décrites
ci-dessus.

