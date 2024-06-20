# Notes de frais

Odoo **Notes de frais** rationalise la gestion des dépenses. Après qu’un
employé a soumis ses notes de frais dans Odoo, celles-ci sont examinées par le
management et la comptabilité. Une fois qu’elles sont approuvées, il est
possible de traiter les paiements et de rembourser l’employé.

Pour plus d'infos

[Odoo Notes de frais : page produit](https://www.odoo.com/app/expenses)

## Définir des catégories de notes de frais

La première étape pour suivre les dépenses est de configurer les différents
types de notes de frais de l’entreprise (gérés comme des _catégories de notes
de frais_ dans Odoo). Chaque catégorie peut être aussi spécifique ou
généralisée que nécessaire. Allez à l’application Notes de frais ‣
Configuration ‣ Catégories de notes de frais pour afficher les catégories de
notes de frais actuelles dans une vue de liste par défaut.

![Définir les coûts sur les produits](../../_images/categories.png)

Pour créer une nouvelle catégorie de notes de frais, cliquez sur Nouveau. Un
formulaire de produit s’affiche avec le champ de description intitulé Nom du
produit.

Note

Les catégories de notes de frais sont gérées comme des produits dans Odoo. Le
formulaire de catégorie de notes de frais est similaire au formulaire de
produit standard dans Odoo et les informations saisies sont similaires. Les
produits de notes de frais seront appelés catégories de notes de frais tout au
long de ce document puisque le menu principal les désigne comme Catégories de
notes de frais.

Seuls deux champs sont obligatoires : le Nom du produit et l”Unité de Mesure.
Saisissez le Nom du produit dans le champ et sélectionnez l”Unité de Mesure
dans la liste déroulante (la plupart des produits utilisent les Unités).

Astuce

The _Sales_ app is where specification on the units of measure are created and
edited (e.g. units, miles, nights, etc.). Go to Sales app ‣ Configuration ‣
Settings and ensure `Units of Measure` is enabled in the `Product Catalog`
section. Click on the Units of Measure internal link to [view, create, and
edit the units of
measure](../inventory_and_mrp/inventory/product_management/product_replenishment/uom.html).

![Définir les coûts sur les produits](../../_images/new-expense-product.png)

Le champ Coût sur le formulaire du produit est complété par défaut avec une
valeur `0,00`. Lorsqu’une note de frais en particulier doit toujours être
remboursée à un certain prix, saisissez ce montant dans le champ Coût. Sinon,
laissez le Coût sur `0,00`, et les employés indiqueront le coût réel
lorsqu’ils soumettent leur note de frais.

Note

Le champ Coût est toujours visible sur le formulaire de catégorie de notes de
frais, mais le champ Prix de vente est _uniquement_ visible lorsque l’option
Prix de vente est sélectionnée dans la section Refacturer les notes de frais.
Sinon, le champ Prix de vente est masqué.

Example

Voici quelques exemples de situations où il convient de fixer un Coût
spécifique sur un produit plutôt que de laisser le Coût sur `0,00` :

  * **Repas** : Définissez le Coût sur `0,00`. Lorsqu’un employé enregistre une note de frais pour un repas, il saisit le montant réel de la facture et sera remboursé pour ce montant. Une note de frais pour un repas coûtant €95,23 correspondra à un remboursement de €95,23.

  * **Kilométrage** : Définissez le Coût sur `0,30`. Lorsqu’un employé enregistre une note de frais pour les « Kilomètres », il saisit le nombre de kilomètres parcourus dans le champ Quantité et est remboursé à hauteur de 0,30 par kilomètre saisi. Une note de frais de 100 kilomètres correspondra à un remboursement de €30,00.

  * **Stationnement mensuel** : Définissez le Coût sur `75,00`. Lorsqu’un employé enregistre une note de frais pour le « stationnement mensuel », le remboursement s’élève à €75,00.

  * **Notes de frais** : Définissez le Coût à `0,00`. Lorsqu’un employé enregistre une note de frais qui n’est pas un repas, un kilométrage ou un stationnement mensuel, il utilise le produit générique Notes de frais. Une note de frais pour un ordinateur portable coûtant €350,00 sera enregistrée comme un produit Notes de frais et le remboursement s’élèvera à €350,00.

Sélectionnez un Compte de charges si vous utilisez l’application
_Comptabilité_ d’Odoo. Il est recommandé de vérifier avec le département
comptable pour déterminer le bon compte à référencer dans ce champ, car cela
affectera les rapports.

Définissez une taxe sur chaque produit dans les champs Taxes fournisseur et
Taxes à la vente. Une bonne pratique consiste à utiliser une taxe qui est
configurée avec la fonction [Prix toutes taxes
comprises](accounting/taxes.html#taxes-included-in-price). Les taxes seront
automatiquement configurées si cette option est activée.

## Enregistrer des notes de frais

### Créer manuellement une nouvelle note de frais

Pour enregistrer une nouvelle note de frais, commencez dans le tableau de bord
principal de l’application Notes de frais qui affiche la vue par défaut Mes
notes de frais. Il est également possible d’accéder à cette vue depuis
l’application Notes de frais ‣ Mes notes de frais ‣ Mes notes de frais.

Cliquez d’abord sur Nouveau et complétez les différents champs du formulaire.

  * Description : Saisissez une brève description de la dépense dans le champ Description. Elle doit être courte et informative, telle que `lunch avec un client` ou `hôtel pendant la conférence`.

  * Catégorie : Sélectionnez la catégorie de notes de frais dans le menu déroulant qui correspond le plus à la note de frais. Par exemple, un billet d’avion conviendrait à une Catégorie de notes de frais intitulée Voyage en avion.

  * Total : Saisissez le montant total payé pour la note de frais de l’une des deux manières suivantes :

    1. Si la note de frais concerne un seul article/une seule dépense et la catégorie sélectionnée ne concerne qu’un seul article, saisissez le coût dans le champ Total (le champ Quantité est masqué).

    2. Si la note de frais concerne des multiples d’un même article/d’une même dépense avec un prix fixe, le Prix unitaire s’affiche. Saisissez la quantité dans le champ Quantité et le coût total est automatiquement mis à jour avec le bon total (le Prix unitaire x la Quantité = le total). Attention, le mot « total » n’apparaît pas, le coût total apparaît simplement sous la Quantité.

Example

Par exemple, dans le cas de kilomètres parcourus, le Prix unitaire correspond
au coût _par kilomètre_. Réglez la Quantité sur le _nombre de kilomètres_
parcourus et le total est calculé.

  * Toutes taxes comprises : Si les taxes ont été configurées sur la catégorie de notes de frais, le pourcentage et le montant de la taxe apparaissent automatiquement après avoir saisi le Total ou la Quantité.

Note

Lorsqu’une taxe est configurée sur une catégorie de notes de frais, la valeur
Toutes taxes comprises sera mise à jour en temps réel au fur et mesure que le
Total ou la Quantité change.

  * Employé : Dans le menu déroulant, sélectionnez l’employé pour lequel cette note de frais est créée.

  * Payé par : Cliquez sur le bouton radio pour indiquer qui a payé la dépense et qui doit être remboursé. Si l’employé a payé la dépense (et doit être remboursé), sélectionnez l”Employé (à rembourser). Si la société a payé directement (par ex. si une carte de crédit de l’entreprise a été utilisée pour payer la dépense), sélectionnez Société. En fonction de la catégorie de notes de frais sélectionnée, il se peut que ce champ n’apparaisse pas.

  * Référence de la facture : Si un texte de référence doit être inclus pour la dépense, saisissez-le dans ce champ.

  * Date de la dépense : À l’aide du module calendrier, saisissez la date de la dépense. Utilisez les flèches < (gauche) et > (droite) pour naviguer jusqu’au bon mois, puis cliquez sur le bon jour pour saisir la sélection.

  * Compte : Sélectionnez le compte de charges dans lequel cette dépense doit être enregistrée dans le menu déroulant.

  * Client à refacturer : Si la note de frais doit être payée par un client, sélectionnez la commande client et le client qui sera facturé pour cette dépense dans le menu déroulant. Toutes les commandes dans le menu déroulant mentionnent à la fois la commande et la société pour laquelle la commande est établie, mais une fois la note de frais enregistrée, le nom du client disparaît et seule la commande est visible sur la note de frais.

Example

Un client souhaite avoir une réunion sur site pour un jardin personnalisé
(conception et installation) et accepte de payer les dépenses associées
(telles que le voyage, l’hôtel, les repas, etc.). Toutes les dépenses liées à
cette réunion seraient indiquées dans la commande client pour le jardin
personnalisé (qui fait également référence au client) en tant que Client à
refacturer.

  * Distribution analytique : Sélectionnez le ou les comptes sur le(s)quel(s) la dépense doit être imputée dans le menu déroulant pour les Projets, Départements ou les deux. Plusieurs comptes peuvent être répertoriés pour chaque catégorie si nécessaire. Ajustez le pourcentage pour chaque compte analytique en saisissant le pourcentage à côté du compte.

  * Société : Si plusieurs sociétés sont configurées, sélectionnez la société pour laquelle cette note de frais doit être enregistrée dans le menu déroulant. La société actuelle est automatiquement complétée dans ce champ.

  * Notes… : Si des notes sont nécessaires pour expliciter la dépense, saisissez-les dans le champ des notes.

![Un formulaire de note de frais complétée pour un lunch avec un
client.](../../_images/expense-filled-in.png)

#### Joindre un reçu

Après que la note de frais est créée, la prochaine étape consiste à joindre un
reçu. Cliquez sur le bouton Joindre un reçu et un explorateur de fichiers
apparaît. Naviguez vers le reçu à joindre et cliquez sur Ouvrir. Le nouveau
reçu est enregistré dans le chatter et le nombre de reçus apparaît à côté de
l’icône 📎 (trombone) sous le formulaire de la note de frais. Vous pouvez
joindre plus d’un reçu à une note de frais individuelle si nécessaire. Le
nombre de reçus joints à la note de frais est indiqué sur l’icône du trombone.

![Joignez un reçu et il apparaît dans le chatter.](../../_images/receipt-
icon.png)

### Créer de nouvelles notes de frais à partir d’un reçu numérisé

Plutôt que de saisir manuellement toutes les informations relatives à une note
de frais, il est possible de créer une note de frais en numérisant un reçu en
PDF.

Tout d’abord, dans la vue principale du tableau de bord de l’application Notes
de frais (il est possible d’accéder à cette vue à partir de l’application
Notes de frais ‣ Mes notes de frais ‣ Mes notes de frais), cliquez sur
Numériser et un explorateur de fichiers s’affiche. Naviguez vers le reçu à
charger, cliquez dessus pour le sélectionner, puis cliquez sur Ouvrir.

![Créez une note de frais en numérisant un reçu. Cliquez sur Numériser en haut
de la vue du tableau de bord des Notes de frais.](../../_images/scan.png)

Le reçu est numérisé et une nouvelle entrée est créée avec la date du jour
comme Date de la note de frais et tous les autres champs pouvant être
renseignés en fonction des données numérisées, tels que le total. Cliquez sur
la nouvelle entrée pour ouvrir le formulaire de la note de frais individuelle
et apporter les modifications nécessaires. Le reçu numérisé apparaît alors
dans le chatter.

### Créer automatiquement de nouvelles notes de frais à partir d’un email

Au lieu de créer chaque note de frais individuellement dans l’application
_Notes de frais_ , il est possible de les créer automatiquement en envoyant un
email à une adresse email.

Pour ce faire, vous devez d’abord configurer un alias d’email. Allez à
l’application Notes de frais ‣ Configuration ‣ Paramètres. Assurez-vous que
l’option Emails entrants est activée.

![Créer l'alias de domaine en cliquant sur le lien.](../../_images/email-
alias.png)

Note

If the domain alias needs to be set up, Setup your domain alias will appear
beneath the incoming emails check box instead of the email address field.
Refer to this documentation for setup instructions and more information: [Noms
de domaine](../websites/website/configuration/domain_names.html). Once the
domain alias is configured, the email address field will be visible beneath
the incoming emails section.

Ensuite, saisissez l’adresse email à utiliser dans le champ email, puis
cliquez sur Enregistrer. Maintenant que l’adresse email a été saisie, vous
pouvez envoyer des emails à cet alias pour créer de nouvelles notes de frais
sans devoir être connecté à la base de données Odoo.

Pour soumettre une note de frais par email, rédigez un nouvel email et
saisissez le code _référence interne_ du produit (si disponible) et le montant
de la dépense dans le sujet de l’email. Ensuite, joignez le reçu à l’email.
Odoo crée la note de frais en prenant les informations notées dans le sujet de
l’email et en les combinant avec le reçu.

Vous vérifier la référence interne d’une catégorie de notes de frais, allez à
l’application Notes de frais ‣ Configuration ‣ Catégories de notes de frais.
Si une référence interne est répertoriée sur la catégorie de notes de frais,
elle se trouve dans la colonne Référence interne.

![Les chiffres de référence interne sont répertoriés dans la vue principale
des catégories de notes de frais.](../../_images/ref.png)

Pour ajouter une référence interne sur une catégorie de notes de frais,
cliquez sur la catégorie pour ouvrir le formulaire. Saisissez la référence
interne dans le champ. Sous le champ Référence interne, cette phrase s’affiche
: Utiliser cette référence comme préfixe de sujet lors de l’envoi par email.

![Les références internes sont répertoriées dans la vue principale des
produits de note de frais.](../../_images/mileage-internal-reference.png)

Note

Pour des raisons de sécurité, Odoo n’accepte que les emails d’employés
authentifiés lors de la création d’une note de frais à partir d’un email. Pour
confirmer l’adresse email d’un employé authentifié, allez à la fiche de
l’employé dans l’application Employés et référez-vous à l”Email professionnel.

![Créer l'alias de domaine en cliquant sur le
lien.](../../_images/authenticated-email-address.png)

Example

Si vous soumettez une note de frais par email pour un repas de €25,00 pendant
un voyage d’affaires, le sujet de l’email serait `ALIMENTATION €25,00`.

Explication :

  * La Référence interne pour la catégorie de notes de frais `Repas` est `ALIMENTATION`

  * Le Coût de la dépense s’élève à `€25,00`

## Créer une note de frais

Lorsque les notes de frais sont prêtes à être soumises (à la fin d’un voyage
d’affaires ou une fois par mois), un _rapport de notes de frais_ doit être
créé. Allez au tableau de bord de l’application Notes de frais, qui affiche
par défaut une vue Mes notes de frais ou allez à l’application Notes de frais
‣ Mes notes de frais ‣ Mes notes de frais.

Les notes de frais sont codées par couleur en fonction de leur statut. Pour
toute dépense dont le statut est À rapporter (des dépenses qui doivent
toujours être ajoutées à un rapport de note de frais), le texte apparaît en
bleu. Tous les autres statuts (À soumettre, Soumis et Approuvé), le texte
apparaît en noir.

Sélectionnez tout d’abord chaque note de frais individuelle du rapport en
cochant la case à côté de chaque entrée ou en sélectionnant rapidement toutes
les dépenses dans la liste en cochant la case à côté de la Date de la note de
frais.

Une autre façon d’ajouter rapidement toutes les notes de frais qui ne figurent
pas sur un rapport est de cliquer sur Créer un rapport sans sélectionner
aucune dépense et Odoo sélectionne toutes les notes de frais avec un statut À
soumettre qui ne sont pas encore incluses dans un rapport.

![Sélectionnez les notes de frais à soumettre, puis créez le
rapport.](../../_images/create-report.png)

Note

Toute dépense peut être sélectionnée dans la liste Mes notes de frais, quel
que soit son statut. Le bouton Créer un rapport est visible tant qu’il y a au
moins une dépense sélectionnée dont le statut À rapporter. Lorsque vous
cliquez sur le bouton Créer un rapport, seules les dépenses dont le statut est
À soumettre qui ne figurent _pas_ actuellement sur un autre rapport de notes
de frais, apparaîtront dans le rapport nouvellement créé.

Une fois que les dépenses ont été sélectionnées, cliquez sur le bouton Créer
le rapport. Le nouveau rapport contient toutes des notes de frais répertoriées
dans l’onglet Note de frais. Si un reçu est joint à une note de frais
individuelle, une icône 📎 (trombone) s’affiche à côté des colonnes Client à
refacturer et Distribution analytique.

Lorsque le rapport est créé, la plage de dates des notes de frais apparaît par
défaut dans le champ Résumé du rapport de note de frais. Il est recommandé de
modifier ce champ avec un bref résumé de chaque rapport permettant d’organiser
les notes de frais. Saisissez une brève description pour le rapport de note de
frais (tel que `Voyage client NYC` ou `Réparations voiture de société`) dans
le champ Résumé du rapport de note de frais. Ensuite, sélectionnez un Manager
dans le menu déroulant pour désigner un manager chargé d’examiner le rapport.
Si nécessaire, vous pouvez modifier le Journal. Utilisez le menu déroulant
pour sélectionner un autre Journal.

![Saisissez une brève description et sélectionnez un manager qui analysera le
rapport.](../../_images/expense-report-summary.png)

Si certaines notes de frais ne figurent pas sur le rapport, elles peuvent
toujours être ajoutées. Cliquez sur Ajouter une ligne au bas de l’onglet Note
de frais. Une fenêtre contextuelle s’affiche avec toutes les dépenses
disponibles qui peuvent être ajoutées au rapport (avec un statut À soumettre).
Cochez la case à côté de chaque dépense à ajouter, puis cliquez sur
Sélectionner. Les articles apparaissent maintenant dans le rapport qui vient
d’être créé. Si une nouvelle dépense doit être ajoutée qui n’apparaît _pas_
dans la liste, cliquez sur Nouveau pour créer une nouvelle dépense et
l’ajouter au rapport.

![Ajoutez plus de notes de frais au rapport avant de le
soumettre.](../../_images/add-an-expense-line.png)

Note

Les rapports de notes de frais peuvent être créés à trois endroits différents
:

  1. Allez au tableau de bord principal de l’application Notes de frais (vous pouvez également y accéder en allant à l’application Notes de frais ‣ Mes notes de frais ‣ Mes notes de frais).

  2. Allez à l’application Notes de frais ‣ Mes notes de frais ‣ Mes rapports.

  3. Allez à l’application Notes de frais ‣ Rapports de notes de frais.

Dans toutes ces vues, cliquez sur Nouveau pour créer un nouveau rapport de
note de frais.

### Soumettre un rapport de notes de frais

Lorsqu’un rapport de notes de frais est complété, l’étape suivante est de
soumettre le rapport à un manager pour approbation. Les rapports doivent être
soumis individuellement et ne peuvent pas être soumis en lot. Ouvrez le
rapport spécifique dans la liste des rapports de notes de frais (si le rapport
n’est pas encore ouvert). Pour voir toutes les notes de frais, allez à
l’application Notes de frais ‣ Mes notes de frais ‣ Mes rapports.

Si la liste est longue, il peut être utile de regrouper les résultats par
statut, car seuls les rapports dont le statut est À soumettre doivent être
soumis, ce qui n’est pas le cas des rapports dont le statut est Approuvé ou
Soumis.

Les dépenses À soumettre sont facilement identifiables, non seulement en
raison du statut À soumettre, mais aussi parce que le texte apparaît en bleu,
tandis que le texte des autres dépenses apparaît en noir.

![Soumettez le rapport au manager.](../../_images/expense-status.png)

Note

Le statut de chaque rapport s’affiche dans la colonne Statut sur la droite. Si
la colonne Statut n’est pas visible, cliquez sur l’icône Options
supplémentaires (deux points) à la fin de la ligne et cochez la case à côté de
Statut.

Cliquez sur un rapport pour l’ouvrir, puis cliquez sur Soumettre au manager.
Après avoir soumis un rapport, la prochaine étape est d’attendre que le
manager l’approuve.

Important

Les sections Approuver des notes de frais, Enregistrer des notes de frais dans
la comptabilité, et Rembourser les employés sont **uniquement** pour les
utilisateurs ayant les _droits nécessaires_.

## Approuver des notes de frais

Dans Odoo, tout le monde ne peut pas approuver des rapports de notes de frais
- seuls les utilisateurs ayant les droits (ou autorisations) nécessaires
peuvent le faire. Cela signifie qu’un utilisateur doit avoir au moins des
droits **Approbateur d’équipe** pour l’application _Notes de frais_. Les
employés ayant les droits nécessaires peuvent examiner des rapports de notes
de frais, les approuver ou les rejeter, ainsi que donner leur avis grâce à
l’outil de communication intégré.

Pour savoir qui a le droit d’approuver, allez à l’application principale
Paramètres et cliquez sur Gérer les utilisateurs.

Note

Si l’application _Paramètres_ n’est pas disponible, certains droits ne sont
pas définis sur le compte. Vérifiez l’onglet Droits d’accès d’une fiche
d’utilisateur dans l’application Paramètres. La section Administration (en bas
à droite de l’onglet Droits d’accès) est définie sur l’une des trois options
suivantes :

  * Rien (blanc) : L’utilisateur ne peut pas du tout accéder à l’application _Paramètres_.

  * Droits d’accès : L’utilisateur peut uniquement voir la section Utilisateurs & Sociétés de l’application _Paramètres_.

  * Paramètres : L’utilisateur a accès à l’intégralité de l’application _Paramètres_ sans restrictions.

Please refer to [this document](../general/users.html) to learn more about
managing users and their access rights.

Cliquez sur une personne pour voir sa carte, ce qui permet d’afficher l’onglet
Droits d’accès dans la vue par défaut. Faites défiler jusqu’à la section
Ressources humaines. Dans Notes de frais, il y a quatre options :

  * Rien (vierge) : Un champ vierge signifie que l’utilisateur n’a pas le droit de visualiser ou d’approuver des rapports de notes de frais. Il peut uniquement voir ses propres notes de frais.

  * Approbateur de l’équipe : L’utilisateur peut uniquement visualiser et approuver les rapports de notes de frais de sa propre équipe.

  * Approbateur de tout : L’utilisateur peut visualiser et approuver n’importe quel rapport de notes de frais.

  * Administrator : L’utilisateur peut voir et approuver n’importe quel rapport de note de frais et accéder aux menus d’analyse et de configuration de l’application _Notes de frais_.

Les utilisateurs habilités à approuver des rapports de notes de frais
(généralement les managers) peuvent facilement consulter les rapports de notes
de frais auxquels ils ont accès. Allez à l’application Notes de frais ‣
Rapports de notes de frais et une liste apparaît avec tous les rapports dont
le statut est À soumettre, Soumis, Approuvé, Publié, ou Fait. Les rapports
dont le statut est Refusé sont masqués dans la vue par défaut.

![Les rapports à valider sont disponibles sur la page des Rapports à
approuver.](../../_images/expense-reports-list.png)

Lors de l’affichage des rapports de notes de frais, vous pouvez activer ou
désactiver un panneau de filtres sur la gauche. Les trois catégories sur
lesquelles les filtres peuvent être appliquées sont Statut, Employé, et
Société. Pour n’afficher que les rapports de notes de frais avec un statut
particulier, activez le filtre de statut spécifique pour afficher les rapports
n’ayant que ce statut. Désactivez le filtre spécifique pour masquer les
rapports ayant ce statut. Pour afficher les rapports de notes de frais pour un
employé et/ou une société en particulier, activez le filtre du nom de
l’employé et/ou le filtre de la société dans les sections Employé et Société.

Les rapports peuvent être approuvés de deux façons (individuellement ou
plusieurs à la fois) et refusés d’une seule manière. Pour approuver plusieurs
rapports de notes de frais en une fois, restez dans la vue de liste.
Sélectionnez d’abord les rapports à approuver en cochant la case à côté de
chaque rapport ou cochez la case à côté de l”Employé pour sélectionner tous
les rapports dans la liste.

Important

Seuls les rapports dont le statut est Soumis peuvent être approuvés. Il est
recommandé d’uniquement afficher les rapports soumis en ajustant le filtre de
statut sur la gauche en n’activant que le filtre Soumis.

Si un rapport sélectionné ne peut pas être approuvé, le bouton Approuver le
rapport **ne s’affichera pas** , indiquant qu’il y a un problème avec le
rapport sélectionné.

Ensuite, cliquez sur le bouton Approuver le rapport.

![Approuvez plusieurs rapports en cochant les cases à côté de chaque
rapport.](../../_images/approve-report.png)

Pour approuver un rapport individuel, cliquez sur un rapport pour ouvrir sa
vue détaillée. Dans cette vue, plusieurs options sont présentées : Approuver,
Rapporter dans la prochaine fiche de paie, Refuser ou Remettre en brouillon.
Cliquez sur Approuver pour approuver le rapport.

Si vous cliquez sur Refuser, une fenêtre contextuelle s’affiche. Expliquez
brièvement le motif dans le champ Motif du refus de la note de frais et puis
cliquez sur Refuser.

![Envoyez des messages dans le chatter.](../../_images/refuse-expense.png)

Les managers d’équipe peuvent facilement voir toutes les notes de frais des
membres de leur équipe. Dans la vue Rapports de note de frais, cliquez sur la
flèche déroulante à droite du champ de recherche et cliquez sur Mon équipe
dans la section Filtres. Vous y verrez tous les rapports de l’équipe du
manager.

![Sélectionnez le filtre Mon équipe.](../../_images/my-team-filter.png)

Astuce

Si vous avez besoin de plus d’informations, par exemple un reçu manquant, vous
pouvez facilement le communiquer dans le chatter. Dans un rapport individuel,
cliquez simplement sur Envoyer un message pour ouvrir la zone de texte du
message. Écrivez le message, taguez la bonne personne (si nécessaire) et
postez-le dans le chatter en cliquant sur Envoyer. Le message est publié dans
le chatter et la personne taguée sera notifiée par email du message, ainsi que
tout autre abonné.

Les seules personnes qui peuvent être taguées dans un message sont des
_abonnés_. Pour voir qui est abonné, cliquez sur l’icône 👤 (personne) pour
voir les abonnés de la note de frais.

![Envoyez des messages dans le chatter.](../../_images/chatter.png)

## Enregistrer des notes de frais dans la comptabilité

Une fois qu’un rapport de notes de frais est approuvé, la prochaine étape
consiste à enregistrer le rapport dans le journal comptable. Pour voir tous
les rapports de notes de frais, allez à l’application Notes de frais ‣
Rapports de note de frais. Pour n’afficher que les rapports de note de frais
qui ont été approuvés et qui doivent être enregistrés, ajustez les filtres à
gauche pour que seul le statut Approuvé ne soit activé.

![Visualisez les rapports à comptabiliser en cliquant sur les rapports de
notes de frais, puis rapports à comptabiliser.](../../_images/post-
reports.png)

Tout comme les approbations, les rapports de notes de frais peuvent être
enregistrés de deux manières (individuellement ou plusieurs à la fois). Pour
enregistrer plusieurs rapports de notes de frais à la fois, restez dans la vue
de liste. Sélectionnez d’abord les rapports à enregistrer en cochant la case à
côté de chaque rapport ou cochez la case à côté de l”Employé pour sélectionner
tous les rapports de la liste. Cliquez ensuite sur Comptabiliser les
écritures.

![Comptabilisez plusieurs rapports à la fois à partir de la vue Rapports de
note de frais, avec le filtre Approuvé.](../../_images/post-entries.png)

Pour comptabiliser un rapport individuel, cliquez sur un rapport pour voir ses
détails. Dans cette vue, il y a plusieurs options : Comptabiliser les
écritures, Rapporter dans la prochaine fiche de paie, Refuser, ou Remettre en
brouillon. Cliquez sur Comptabiliser les écritures pour enregistrer le
rapport.

Si vous cliquez sur Refuser, une fenêtre contextuelle s’affiche. Expliquez
brièvement le refus dans le champ Motif du refus de la note de frais et
cliquez sur Refuser. Vous pouvez visualiser les rapports refusés en allant à
l’application Notes de frais ‣ Rapports de note de frais, puis en ajustant les
filtres à gauche pour que seule l’option Réfusé soit sélectionnée. Vous verrez
alors uniquement tous les rapports de note de frais refusés.

Important

Pour enregistrer des rapports de notes de frais dans un journal comptable,
l’utilisateur doit avoir les droits d’accès suivants :

  * Comptabilité : comptable ou conseiller

  * Notes de frais : manager

## Rembourser les employés

Après avoir enregistré un rapport de note de frais dans un journal comptable,
la prochaine étape consiste à rembourser l’employé. Pour voir tous les
rapports de note de frais à payer, allez à l’application Notes de frais ‣
Rapports de note de frais ‣ Rapports à payer.

![Visualisez les notes de frais à rembourser en cliquant sur notes de frais,
puis notes de frais à rembourser.](../../_images/reports-to-pay.png)

Tout comme les approbations et l’enregistrement, les rapports de notes de
frais peuvent être payés de deux manières (individuellement ou plusieurs à la
fois). Pour payer plusieurs rapports de notes de frais à la fois, restez dans
la vue de liste. Sélectionnez d’abord les rapports à payer en cochant la case
à côté de chaque rapport ou cochez la case à côté de l”Employé pour
sélectionner tous les rapports de la liste. Cliquez ensuite Enregistrer un
paiement.

![Enregistrez plusieurs rapports en les sélectionnant, en cliquant sur l'icône
d'engrenage et en comptabilisant les écritures.](../../_images/register-
payment1.png)

Pour payer une note de frais individuelle, cliquez sur une note de frais pour
passer à la vue détaillée de cette note. Cliquez sur Enregistrer un paiement
pour rembourser l’employé.

Une fenêtre contextuelle Enregistrer un paiement s’affiche et vous pouvez
modifier le Journal, le Mode de paiement et la Date du paiement le cas
échéant. Lorsque les sélections sont correctes, cliquez sur Créer un paiement
pour envoyer le paiement à l’employé.

Pour payer un rapport individuel, cliquez sur un rapport dans la vue de liste
pour obtenir sa vue détaillée. Cliquez sur Enregistrer un paiement pour payer
l’employé. Une fenêtre contextuelle Enregistrer un paiement s’affiche. Mais
lorsque vous payez un rapport de note de frais individuel au lieu de plusieurs
rapports à la fois, plus d’options s’affichent dans la fenêtre contextuelle.
En plus des champs Journal, Mode de paiement et Date du paiement, vous verrez
les champs Compte bancaire destinataire, Montant et Mémo. Sélectionnez le
compte bancaire de l’employé dans le menu déroulant pour directement déposer
le paiement sur son compte. Lorsque toutes les autres sélections sont
correctes, cliquez sur Créer un paiement pour envoyer le paiement à l’employé.

![Plusieurs options apparaissent lorsque vous enregistrez un rapport de note
de frais individuel versus plusieurs rapports de notes de frais à la
fois.](../../_images/two-payment-posting-options.png)

## Refacturer des notes de frais aux clients

Si les dépenses sont suivies sur des projets clients, vous pouvez
automatiquement refacturer les dépenses au client. Pour ce faire, il suffit de
créer une note de frais, de référencer la commande à laquelle la dépense doit
être ajoutée, puis de créer la note de frais. Ensuite, les managers approuvent
la note de frais et le département comptable comptabilise les pièces
comptables. Enfin, une fois que la note de frais est enregistrée dans un
journal, la dépense apparaît sur la commande référencée. La commande peut
ensuite être facturée, ce qu permet de facturer la dépense au client.

### Configuration

Tout d’abord, précisez la politique de facturation pour chaque catégorie de
notes de frais. Allez à l’application, Notes de frais ‣ Configuration ‣
Catégories de notes de frais. Cliquez sur la catégorie de notes de frais pour
ouvrir le formulaire de la catégorie de notes de frais. Dans la section
Facturation, cliquez sur le bouton ratio à côté de la section souhaitée pour
Refacturer les notes de frais. Les options sont Non, Au prix coûtant et Prix
de vente.

Refacturer les notes de frais :

  * Non : La catégorie de notes de frais n’est pas refacturée.

  * Au prix coûtant : La catégorie de notes de frais facture les dépenses à leur coût réel.

  * Prix de vente : La catégorie de notes de frais facture le prix défini sur la commande.

### Créer une note de frais

Tout d’abord, lors de la création d’une nouvelle note de frais, vous devez
saisir les informations correctes afin de pouvoir refacturer au client.
Sélectionnez la _commande client_ dans laquelle la dépense apparaîtra dans la
section Client à refacturer dans le menu déroulant. Ensuite, sélectionnez le
Compte analytique sur lequel la note de frais sera comptabilisée. Après la
création de la note de frais, le rapport doit être créé et soumis comme
d’habitude.

![Assurez-vous que le client à refacturer est défini sur la note de
frais.](../../_images/reinvoice-expense.png)

Important

Il est important de sélectionner un Client à refacturer lors de la création
d’une note de frais. En effet, c’est ce qui permet d’automatiquement facturer
les dépenses après l’approbation d’une note de frais.

Le champ Client à refacturer peut être modifié _jusqu’à ce qu’un rapport de
note de frais est_ **approuvé** , ensuite le champ ne peut plus être modifié.

### Valider et comptabiliser des notes de frais

Seuls les employés disposant des autorisations nécessaires (généralement des
managers ou des superviseurs) peuvent approuver des notes de frais. Avant
d’approuver un rapport de note de frais, assurez-vous que la Distribution
analytique est définie sur chaque ligne de la note de frais. S’il manque une
Distribution analytique, choisissez le bon compte dans le menu déroulant et
cliquez sur Approuver ou Refuser.

Le département comptable est généralement chargé de la comptabilisation des
pièces comptables. Une fois qu’un rapport de note de frais est approuvé, il
peut être comptabilisé. La commande est **uniquement** mise à jour _après la
comptabilisation des pièces comptables_. Une fois que les pièces comptables
sont comptabilisées, les dépenses apparaissent sur la commande client
référencée.

### Facturer les notes de frais

Une fois que la commande client a été mise à jour, il est temps de facturer le
client. Après l’approbation du rapport de note de frais et la comptabilisation
des pièces comptables, cliquez sur le bouton intelligent Bons de commande pour
ouvrir la commande client. Les dépenses à refacturer figurent maintenant sur
la commande client.

![Une fois le rapport de note de frais enregistré dans la pièce comptable,
vous pouvez accéder à la commande en cliquant sur le numéro de la
commande.](../../_images/sales-order.png)

Note

Vous pouvez référencer plus d’une commande sur un rapport de note de frais. Si
plusieurs commandes clients sont référencées, le bouton intelligent Bons de
commande affiche le nombre de commandes clients. Si plusieurs commandes sont
répertoriées, le bouton intelligent Bons de commande ouvre une vue de liste de
toutes les commandes sur le rapport de note de frais. Cliquez sur la commande
client pour ouvrir la commande individuelle.

Les dépenses sont répertoriées dans l’onglet Lignes de la commande de la
commande client.

![Voir les dépenses listées sur la commande après avoir cliqué
dessus.](../../_images/so-details.png)

Cliquez ensuite sur Créer une facture et sélectionnez si une facture est une
Facture normale, un Acompte (pourcentage) ou un Acompte (montant fixe) en
cliquant sur le bouton radio à côté. Ensuite, cliquez sur Créer une facture.
Les dépenses ont été facturées au client.

