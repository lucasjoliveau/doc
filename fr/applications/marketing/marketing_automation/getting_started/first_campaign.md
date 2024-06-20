# Campagnes de marketing automation

L’application Odoo _Marketing Automation_ permet d’automatiser une variété de
tâches marketing en combinant des règles et des filtres spécifiques pour
générer des actions programmées. Au lieu d’avoir à construire manuellement
chaque étape d’une campagne (comme une série de massmails programmés),
l’application _Marketing Automation_ permet aux marketeurs de construire la
campagne entière et toutes ses étapes, en un seul endroit—sur un seul tableau
de bord.

## Configuration de la campagne

Pour créer une nouvelle campagne de marketing automation, allez à
l’application Marketing Automation ‣ Nouveau pour faire apparaître un
formulaire vierge.

![Un formulaire de campagne de marketing automation vierge dans l'application
Odoo Marketing Automation.](../../../../_images/blank-marketing-campaign-
form.png)

Après avoir donné un nom à la campagne de marketing, configurez l’audience
cible dans les champs restants.

Vous pouvez configurer une audience cible en saisissant des critères
spécifiques qu’Odoo utilisera pour déterminer à qui cette campagne de
marketing automation doit être envoyée.

Dans le champ Cible, utilisez le menu déroulant pour choisir sur quel modèle
les filtres de l’audience cible doivent être basés (par ex. Contact,
Piste/Opportunité, Bon de commande, etc.).

Sélectionnez Recherche avancée… dans le menu déroulant pour faire apparaître
une fenêtre contextuelle Recherche : Cible contenant toutes les options de
ciblage disponibles.

Une fois qu’une Cible est sélectionnée, il y a un champ Unicité basée sur. Ce
champ est utilisé pour éviter des doublons basés sur le modèle choisi dans le
champ Cible.

Example

Si vous choisissez Clients comme la Cible, sélectionnez Email dans le champ
Unicité basée sur pour qu’Odoo ne traite qu’un seul enregistrement pour chaque
adresse mail de client.

Sélectionnez Recherche avancée… dans le menu déroulant Unicité basée sur pour
faire apparaître toutes les options disponibles dans une fenêtre contextuelle.

Le dernier champ du formulaire de campagne est le champ Filtre. Il vous permet
d’ajouter des options de ciblage plus spécifiques à la campagne pour
restreindre davantage le nombre et le type de destinataires qui reçoivent le
matériel de marketing automation.

S’il n’est pas modifié, le champ Filtre est le suivant : Faire correspondre
tous les enregistrements. Cela signifie qu’Odoo utilise les champs Cible et
Unicité basée sur pour déterminer les destinataires. Le nombre de
destinataires est représenté en-dessous sous forme d”enregistrement(s).

### Règles de filtrage des campagnes

Pour ajouter un filtre plus spécifique à une campagne de marketing automation,
cliquez sur le bouton Ajouter une condition dans le champ Filtre. Cette
opération fait apparaître une série d’autres champs de règles de filtrage
configurables.

Dans les champs de règles, vous pouvez configurer des équations
personnalisables qu’Odoo utilisera lors du filtrage des enregistrements à
inclure ou exclure dans cette campagne de marketing spécifique.

![Présentation des champs d'équation des règles de filtrage dans l'application
Odoo Marketing Automation.](../../../../_images/filter-node-equation-
fields.png)

Note

Le champ Enregistrements fait référence aux contacts dans le système qui
correspondent aux critères précisés pour une campagne.

De plus, dès que vous cliquez sur Ajouter une condition, la possibilité
d”Enregistrer comme filtre favori devient disponible sur le formulaire de
campagne.

Il est également possible de faire correspondre des enregistrements à toutes
les règles ou une des règles configurées dans le champ Filtre.

Pour choisir l’une de ces options, cliquez sur toutes les au milieu de la
phrase « Faire correspondre les enregistrements avec toutes les règles
suivantes » pour faire apparaître un menu déroulant avec ces options.

![Faire correspondre les enregistrements à toutes ou à l'une des règles dans
le champ Filtre pour les campagnes de marketing.](../../../../_images/match-
all-any-rules-drop-down.png)

Lorsque vous cliquez sur le premier champ de l’équation de règle, un menu
déroulant imbriqué d’options apparaît à l’écran, dans lequel des critères
spécifiques sont sélectionnés en fonction des besoins de la campagne.

Les champs restants de l’équation de règle permettent de préciser les
critères, qui sont utilisés pour déterminer les enregistrements de la base de
données à inclure ou à exclure de la campagne.

Pour ajouter une autre règle, cliquez sur l’icône ➕ (signe plus) à droite de
la règle de filtrage ou cliquez sur Nouvelle règle sous les champs de
l’équation de la règle. Lorsque vous cliquez sur l’un ou l’autre option, une
nouvelle série de champs de règle s’affiche.

Pour ajouter une branche de plusieurs règles en même temps, cliquez sur
l’icône branche, située à droite de l’icône ➕ (signe plus). Lorsque vous
cliquez sur cette icône, deux champs d’équation de sous-règle supplémentaires
apparaissent sous la règle initiale.

![Exemple d'une branche de règles dans la section filtrage d'une campagne de
marketing.](../../../../_images/rule-branch-filter-sample.png)

Il est également possible d’appliquer le filtre à une ou toutes les règles de
branche configurées.

Pour plus d’informations sur la configuration des filtres des campagnes de
marketing automation, consultez [cette page de
documentation](target_audience.html).

Pour plus d'infos

  * [Activités du flux de travail de la campagne](workflow_activities.html)

  * [Tester/lancer des campagnes](testing_running.html)

