# Modèles d’email

Les modèles d’email sont des emails enregistrés qui sont utilisés
régulièrement pour envoyer des emails à partir de la base de données. Ils
permettent à l’utilisateur d’envoyer des communications de qualité, sans avoir
à composer le même texte à plusieurs reprises.

La création de différents modèles adaptés à des situations spécifiques permet
donc aux utilisateurs de choisir le bon message pour le bon public. Cela
augmente la qualité du message et le taux d’engagement global.

Note

Les modèles d’email dans Odoo utilisent QWeb ou XML, ce qui permet de modifier
les emails dans leur rendu final et de rendre les personnalisations plus
robustes, sans avoir à modifier le code. Ceci signifie qu’Odoo peut utiliser
une interface graphique utilisateur (GUI) pour modifier les emails, ainsi que
le code en backend. Lorsque l’email reçu est lu par le programme de
l’utilisateur final, différents formats et graphiques apparaîtront dans le
rendu final de l’email.

Accédez aux modèles d’email en [mode
développeur](../developer_mode.html#developer-mode) en allant aux Paramètres ‣
menu Technique ‣ Email ‣ Modèles d’email.

## Modifier les modèles d’email

La fonctionnalité _boîte à outils_ peut être utilisée pour travailler avec les
modèles d’email. Elle permet de modifier directement la mise en forme et le
texte dans un modèle d’email, ainsi que d’ajouter des liens, des boutons, des
options de prise de rendez-vous ou des images.

De plus, le code XML/HTML du modèle d’email peut être modifié directement à
l’aide de l’icône </>. Les placeholders dynamiques (faisant référence à des
champs dans Odoo) sont également disponibles pour être utilisés dans le modèle
d’email.

### Boîte à outils

La fonctionnalité _boîte à outils_ est un éditeur de texte enrichi avec
différentes options de formatage, de mise en page et de texte. Elle peut
également être utilisée pour ajouter des fonctionnalités XML/HTML dans un
modèle d’email. La boîte à outils est activée en tapant une barre oblique `/`
dans le corps du modèle d’email.

Lorsque vous tapez une barre oblique `/` dans le corps d’un modèle d’email, un
menu déroulant avec les options suivantes s’affiche :

Structure

  * Liste à puces : Créer une simple liste à puces.

  * Liste numérotée : Créer une liste avec numérotation.

  * Check-list : Suivre les tâches grâce à une check-list.

  * Tableau : Insérer un tableau.

  * Séparateur : Insérer une ligne horizontale de séparation.

  * Citation : Ajouter une section de citation.

  * Code : Ajouter une section de code.

  * 2 colommes : Convertir en deux colommes.

  * 3 colommes : Convertir en trois colommes.

  * 4 colommes : Convertir en quatre colommes.

Format

  * Titre 1 : Grand titre de section.

  * Titre 2 : Moyen titre de section.

  * Titre 3 : Petit titre de section.

  * Changer de direction : Changer la direction du texte.

  * Texte : Bloc de paragraphe.

Média

  * Image : Insérer une image.

  * Article : Lier un article.

Navigation

  * Lien : Ajouter un lien.

  * Bouton : Ajouter un bouton.

  * Rendez-vous : Ajouter un rendez-vous spécifique.

  * Calendrier : Programmer un rendez-vous.

Widgets

  * 3 étoiles : Insérer une note sur trois étoiles.

  * 5 étoiles : Insérer une note sur cinq étoiles.

Blocs de base

  * Signature : Insérer votre signature.

Outils marketing

  * Placeholder dynamique : Insérer votre contenu personnalisé.

Astuce

Pour utiliser l’une de ces options, cliquez sur la fonction souhaitée dans le
menu déroulant de la boîte à outils. Pour mettre en forme un texte existant à
l’aide d’une option liée au texte (par ex. Titre 1, Changer de direction,
etc.), mettez le texte en surbrillance, tapez la clé d’activation (barre
oblique) `/`, et sélectionnez l’option souhaitée dans le menu déroulant.

![Fonctionnalité boîte à outils dans le modèle
d'email.](../../../_images/powerbox-feature.png)

Pour plus d'infos

Utiliser des placeholders dynamiques

### Éditeur de code XML/HTML

Pour accéder à l’éditeur XML/HTML d’un modèle d’email, activez d’abord le
[mode développeur](../developer_mode.html#developer-mode). Cliquez ensuite sur
l’icône </> dans le coin supérieur droit du modèle et modifiez le XML/HTML.
Pour revenir à l’éditeur de texte standard, cliquez à nouveau sur l’icône </>.

![Éditeur HTML dans le modèle d'email.](../../../_images/html-code-editor.png)

Avertissement

L’éditeur XML/HTML doit être utilisé avec précaution, car il s’agit du code
dans le backend du modèle. La modification du code peut entraîner la rupture
du modèle d’email immédiatement ou lors de la mise à niveau de la base de
données.

### Placeholders dynamiques

Les _placeholders dynamiques_ font référence à certains champs dans la base de
données Odoo pour produire des données uniques dans le modèle d’email.

Example

De nombreuses entreprises aiment personnaliser leurs emails en ajoutant un
élément d’information personnalisé sur le client pour attirer son attention.
Dans Odoo, vous pouvez faire référence à un champ dans un modèle en insérant
un placeholder dynamique. Par exemple, le nom d’un client peut être référencé
dans l’email à partir du champ Client sur le modèle du Bon de commande. Le
placeholder dynamique de ce champ est : `{{ object.partner_id }}`.

Les placeholders dynamiques sont codés pour afficher des champs de la base de
données. Les placeholders dynamiques peuvent être utilisés dans le corps
(onglet Contenu) du modèle d’email. Ils peuvent également être utilisés dans
les champs de l’onglet Configuration de l’email, le Sujet de l’email et la
Langue.

Pour utiliser les placeholders dynamiques dans le corps d’un email, ouvrez la
**boîte à outils** en tapant `/` dans le corps du modèle d’email dans l’onglet
Contenu. Faites défiler la liste des options jusqu’aux Outils marketing et
cliquez sur Placeholder dynamique. Sélectionnez ensuite le placeholder
dynamique dans la liste des options disponibles et suivez les instructions
pour le configurer avec le champ Odoo correspondant souhaité. La configuration
de chaque placeholder dynamique sera différente.

![Utiliser des placeholders dynamiques dans un modèle
d'email.](../../../_images/dynamic-placeholders.png)

Note

Chaque combinaison unique de Champs, Sous-modèles et Sous-champs crée un
placeholder dynamique différent. Considérez-le comme une combinaison avec le
champ en cours de création.

Pour effectuer une recherche parmi les champs disponibles, tapez simplement le
nom frontend (sur l’interface utilisateur) du champ dans la barre de
recherche. Vous obtiendrez un résultat pour tous les champs disponibles pour
le modèle pour lequel le modèle d’email a été créé.

Avertissement

L’assistance d’Odoo ne prend pas en charge la personnalisation des modèles
d’email.

### Éditeur de texte enrichi

Il est possible d’accéder à une barre d’outils d’édition de texte enrichi en
mettant en surbrillance du texte dans le modèle d’email. Vous pouvez ainsi
modifier le titre, la taille/le style de la police, la couleur, ajouter un
type de liste ou un lien.

![Éditeur de texte enrichi dans le modèle d'email.](../../../_images/rich-
text-editor.png)

### Réinitialiser les modèles d’email

Si le modèle d’email ne fonctionne pas parce que le code a été modifié, il
peut être réinitialisé pour revenir au modèle par défaut. Il suffit de cliquer
sur le bouton Réinitialiser le modèle dans le coin supérieur gauche de l’écran
pour réinitialiser le modèle.

![Réinitialisation du modèle d'email.](../../../_images/reset.png)

### Réponse par défaut aux modèles d’email

Dans l’onglet Configuration de l’email d’un modèle d’email, il y a un champ
Répondre à. Ajoutez dans ce champ les adresses email auxquelles les réponses
sont redirigées lors de l’envoi d’emails en masse à l’aide de ce modèle.

Astuce

Ajoutez plusieurs adresses email en ajoutant une virgule `,` entre les
adresses ou les placeholders dynamiques.

![Champ répondre à sur un modèle.](../../../_images/reply-to-template-
sales.png)

Le champ Répondre à est **uniquement** utilisé pour les envois en masse. Les
emails en masse peuvent être envoyés dans presque toutes les applications Odoo
qui ont une option d’affichage de liste.

Pour envoyer des emails en masse, dans la vue de liste, cochez les cases à
côté des enregistrements souhaités où les emails doivent être envoyés, cliquez
sur le bouton Action (représenté par une icône d’engrenage ⚙️), et
sélectionnez l’option d’email souhaitée dans le menu déroulant Action. Les
options d’email peuvent varier en fonction de la vue de liste et de
l’application.

S’il est possible d’envoyer un email, une fenêtre contextuelle de composition
d’email s’ouvre, dans laquelle vous pouvez définir et personnaliser des
valeurs. Cette option sera disponible dans le menu déroulant Action sur les
pages où les emails peuvent être envoyés en masse—par exemple, sur la page
Clients de l’application CRM. Cette action se produit dans toute la base de
données Odoo.

![Compositeur d'email en mode envoi en masse avec le champ Répondre à en
surbrillance.](../../../_images/composer-mass-mailing.png)

## Emails transactionnels et URLs correspondantes

Dans Odoo, plusieurs événements peuvent déclencher l’envoi d’emails
automatisés. Ces emails sont appelés des _emails transactionnels_ et
contiennent parfois des liens pointant vers la base de données Odoo.

Par défaut, les liens générés par la base de données utilisent la clé
dynamique `web.base.url` définie dans les paramètres système. Pour plus
d’informations à ce sujet, consultez les [paramètres
système](../../websites/website/configuration/domain_names.html#domain-name-
web-base-url).

Si l’application _Site Web_ n’est pas installée, la clé `web.base.url` sera
toujours le paramètre par défaut utilisé pour générer tous les liens.

Important

La clé `web.base.url` ne peut avoir qu’une seule valeur, ce qui signifie que
dans un environnement de base de données multi-sites/sociétés, même s’il y a
un nom de domaine spécifique pour chaque site web, les liens générés pour
partager un document (ou les liens dans un email transactionnel) peuvent
rester les mêmes, quel(le) que soit le site web/la société associé(e) à
l’envoi de l’email/du document.

Example

Si la Valeur du paramètre système web.base.url est `https://www.mycompany.com`
et s’il y a deux sociétés distinctes dans Odoo avec des URLs de site web
différentes : `https://www.mycompany2.com` et `https://www.mycompany1.com`,
les liens créés par Odoo pour partager un document ou pour envoyer un email
transactionnel, proviennent du domaine : `https://www.mycompany.com`, quelle
que soit la société qui a envoyé le document ou l’email.

Ce n’est pas toujours le cas, car certaines applications Odoo (_eCommerce_ par
exemple) ont un lien établi dans la base de données avec l’application _Site
Web_. Dans ce cas, si un domaine spécifique est précisé pour le site web,
l’URL générée dans le modèle d’email utilise le domaine défini sur le site web
correspondant de la société.

Example

Lorsqu’un client fait un achat sur un site d” _eCommerce_ d’Odoo, la commande
a un lien établi avec ce site web. Par conséquence, les liens dans l’email de
confirmation envoyé au client utilisent le nom de domaine de ce site web en
particulier.

Note

Un document partagé à l’aide de l’application _Documents_ utilisera
**toujours** la clé `web.base.url`, car le document partagé n’est associé à
aucun site web en particulier. Ceci signifie que l’URL sera toujours la même
(la valeur de la clé `web.base.url`), quelle que soit la société à partir de
laquelle le document a été partagé. C’est une limitation connue.

For more information about how to configure domains, check out the [domain
name documentation](../../websites/website/configuration/domain_names.html).

### Mise à jour des traductions dans les modèles d’email

Dans Odoo, les modèles d’email sont automatiquement traduits pour tous les
utilisateurs dans la base de données pour toutes les langues installées. Il ne
devrait pas être nécessaire de modifier les traductions. Si toutefois les
traductions doivent être modifiées pour une raison particulière, c’est
possible.

Avertissement

Comme toute modification de code, gardez à l’esprit que les modifications de
traduction qui ne sont pas faites correctement (par exemple, des modifications
conduisant à des erreurs de syntaxe) peuvent casser le modèle et par
conséquent, afficher un modèle vide.

Pour modifier les traductions, activez d’abord le [mode
développeur](../developer_mode.html#developer-mode). Cliquez ensuite sur le
modèle d’email sur le bouton Modifier et cliquez sur le bouton de langue,
représenté par les initiales de la langue en cours d’utilisation (par ex. EN
pour l’anglais).

![Modifier la langue d'un modèle.](../../../_images/edit-language-
template.png)

Note

S’il n’y a qu’une seule langue installée et activée dans la base de données ou
si l’utilisateur n’a pas des droits d’accès d’administration, le bouton de
langue n’apparaît pas.

Une fenêtre contextuelle avec les différentes langues installées dans la base
de données s’ouvre. Il est possible de modifier les traductions dans cette
fenêtre contextuelle. Lorsque les modifications souhaitées ont été effectuées,
cliquez sur le bouton Enregistrer pour enregistrer les modifications.

![Traduction du corps du modèle de Prise de rendez-
vous.](../../../_images/translation-body.png)

Note

Lors de la modification des traductions, la langue par défaut de la base de
données apparaît en **gras**.

