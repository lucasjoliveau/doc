# Vérification des numéros de TVA (VIES)

Le **Système d’échange d’informations en matière de TVA** \- en abrégé
**VIES** \- est un outil fourni par la Commission européenne qui vous permet
de vérifier la validité des numéros de TVA des entreprises enregistrées dans
l’Union européenne.

Odoo fournit une fonctionnalité permettant de **vérifier les numéros de TVA**
lorsque vous enregistrez un contact. Cela vous aide à vous assurer que vos
contacts vous ont fourni un numéro de TVA valide sans quitter l’interface
Odoo.

## Configuration

Pour activer cette fonctionnalité, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Taxes, activez la fonction **Vérifier les numéros de TVA** et
cliquez sur _Enregistrer_.

![Activez l'option "Vérifier les numéros de TVA" dans Odoo
Comptabilité](../../../../_images/vat-validation-configuration.png)

## Validation du numéro de TVA

Lors de la création ou la modification d’un contact, assurez-vous de compléter
les champs **Pays** et **TVA**.

![Complétez le pays et le numéro de TVA dans le formulaire de contact avant de
cliquer sur *Enregistrer*.](../../../../_images/vat-validation-contact-
form.png)

Lorsque vous cliquez sur _Enregistrer_ , Odoo exécute une vérification du
numéro de TVA par VIES et affiche un message d’erreur si le numéro de TVA
n’est pas valide.

![Odoo affiche un message d'erreur au lieu d'enregistrer le numéro de TVA
lorsque ce dernier n'est pas valide.](../../../../_images/vat-validation-
error.png)

Important

Cet outil vérifie la validité du numéro de TVA, mais ne vérifie pas la
validité des autres champs.

Pour plus d'infos

  * [Commission européenne : moteur de recherche VIES](https://ec.europa.eu/taxation_customs/vies/vatRequest.html)

