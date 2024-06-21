# Vérification des numéros de TVA (VIES)

Le **Système d’échange d’informations en matière de TVA** \- en abrégé
**VIES** \- est un outil fourni par la Commission européenne qui vous permet
de vérifier la validité des numéros de TVA des entreprises enregistrées dans
l’Union européenne.

Konvergo ERP fournit une fonctionnalité permettant de **vérifier les numéros de TVA**
lorsque vous enregistrez un contact. Cela vous aide à vous assurer que vos
contacts vous ont fourni un numéro de TVA valide sans quitter l’interface
Konvergo ERP.

## Configuration

Pour activer cette fonctionnalité, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Taxes, activez la fonction **Vérifier les numéros de TVA** et
cliquez sur _Enregistrer_.

![Activez l'option "Vérifier les numéros de TVA" dans Konvergo ERP
Comptabilité](../../../../_images/vat-validation-configuration.png)

## Validation du numéro de TVA

Lors de la création ou la modification d’un contact, assurez-vous de compléter
les champs **Pays** et **TVA**.

![Complétez le pays et le numéro de TVA dans le formulaire de contact avant de
cliquer sur *Enregistrer*.](../../../../_images/vat-validation-contact-
form.png)

Lorsque vous cliquez sur _Enregistrer_ , Konvergo ERP exécute une vérification du
numéro de TVA par VIES et affiche un message d’erreur si le numéro de TVA
n’est pas valide.

![Konvergo ERP affiche un message d'erreur au lieu d'enregistrer le numéro de TVA
lorsque ce dernier n'est pas valide.](../../../../_images/vat-validation-
error.png) <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Cet outil vérifie la validité du numéro de TVA, mais ne vérifie pas la validité des autres champs.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://ec.europa.eu/taxation_customs/vies/vatRequest">Commission européenne : moteur de recherche VIES</a></p></li>
</ul>
</div>

