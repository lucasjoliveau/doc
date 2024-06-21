# Générer des pistes/opportunités

Les alias d’email et les formulaires de contact de votre site web sont deux
moyens essentiels de générer de nouvelles pistes ou opportunités pour votre
entreprise. Konvergo ERP crée automatiquement des pistes dans votre CRM lorsque
quelqu’un envoie un message à un alias d’email de l’équipe commerciale ou
remplit un formulaire de contact sur votre site web.

## Configurer les alias d’email

Chaque équipe commerciale peut utiliser son propre alias d’email pour générer
des pistes ou des opportunités. Tout email envoyé à l’alias d’email d’une
équipe commerciale crée automatiquement une piste (si les pistes sont activées
dans les paramètres de votre CRM) ou une opportunité dans le pipeline de cette
équipe en particulier. Configurez des alias d’email personnalisés pour chaque
équipe commerciale en allant à CRM ‣ Configuration ‣ Équipes commerciales.

![En cours de configuration des équipes
commerciales](../../../../_images/sales-team-config.png)

## Utiliser des formulaires de contact sur votre site web

Par défaut, la page _Nous contacter_ de votre site web affiche le formulaire
de contact prêt à l’emploi d’Konvergo ERP. Chaque fois qu’une personne soumet ce
formulaire, une piste ou une opportunité est générée dans votre base de
données.

![Page Nous contacter affiché par défaut](../../../../_images/default-contact-
us-page.png)

Le formulaire de contact peut être activé ou désactivé à tout moment en allant
à Site Web ‣ Aller au site web ‣ Personnaliser ‣ Formulaire de contact.

![Toggle formulaire de contact](../../../../_images/contact-form-toggle.png)

Lorsque le formulaire est désactivé, la page _Nous contacter_ affiche
simplement un bouton permettant d’envoyer un email directement à votre
entreprise. Tout email envoyé de cette façon générera une piste/opportunité.

![Page Nous contacter utilisant un email](../../../../_images/default-contact-
us-page-no-form.png)

Choisissez l’équipe commerciale ou le vendeur qui sera automatiquement
attribué aux pistes/opportunités créées à partir du formulaire de contact en
allant à Site Web ‣ Configuration ‣ Paramètres ‣ Communication.

![Paramètres du formulaire de contact](../../../../_images/contact-form-
settings.png)

## Personnaliser les formulaires de contact

Les formulaires de contact peuvent être personnalisés pour obtenir les
informations spécifiques dont votre équipe a besoin, grâce au module gratuit
_Constructeur de formulaires_.

Le module _Constructeur de formulaires_ est installé automatiquement lorsqu’un
élément de formulaire est ajouté à une page web via l’éditeur du Site Web. Il
peut également être installé manuellement à partir de la page
**Applications**.

![Blocs de construction du constructeur de
formulaires](../../../../_images/form-building-block.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les formulaires peuvent être créés à partir de zéro pour servir une grande variété d’objectifs. Cependant, la page <em>Nous contacter</em> par défaut d’Konvergo ERP est conçue pour répondre aux besoins de la plupart des utilisateurs. Commencez par le formulaire par défaut et modifiez-le à partir de là.</p>
</div>

### Modifier les champs du formulaire de contact

En mode édition sur votre site web, cliquez sur n’importe quel champ pour
commencer à le modifier. Les informations suivantes peuvent être modifiées
pour chaque champ du formulaire de contact :

  * **Type** : Choisissez une option de champ personnalisé ou un champ existant. Par exemple, numéro de téléphone, téléchargement de fichiers, langue, etc.

  * **Type d’entrée** : Déterminez le type d’information que les clients doivent saisir. Les options disponibles sont texte, adresse mail, numéro de téléphone et URL.

  * **Zone de texte** : Saisissez un exemple pour guider les utilisateurs dans la saisie d’informations dont le formatage est important, comme un numéro de téléphone ou une adresse mail.

  * **Libellé** : Tapez le nom d’affichage pour montrer aux utilisateurs quelles informations ils doivent saisir.

  * **Position** : Choisissez la façon dont le libellé s’aligne avec le reste du formulaire. Le libellé peut être masqué, au-dessus du champ, à l’extrême gauche du champ ou ajusté à droite et plus près du champ.

  * **Requis** : Activez cette option pour les informations qui sont obligatoires.

  * **Masqué** : Activez cette option pour masquer le champ sans le supprimer.

  * **Afficher sur mobile** : Activez cette option pour afficher le champ aux utilisateurs d’appareils mobiles.

![Champs éditables](../../../../_images/editable-field-options.png)

Par défaut, lorsqu’un formulaire est soumis, il vous envoie un email contenant
les informations saisies par le client. Pour qu’il génère automatiquement une
piste/opportunité, modifiez le formulaire et sélectionnez **Créer une
opportunité** comme Action.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si les pistes sont activées dans vos paramètres CRM, le fait de sélectionner <b>Créer une opportunité</b> génère une piste à la place. Pour en savoir plus sur l’activation des pistes dans les paramètres CRM, consultez <a href="convert">Convertir des pistes en opportunités</a>.</p>
</div>

