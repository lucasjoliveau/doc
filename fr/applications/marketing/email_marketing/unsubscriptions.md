# Gérer les désabonnements (liste noire)

Permettre aux destinataires de se désabonner des listes de diffusion n’est pas
seulement une pratique commerciale intelligente, c’est souvent une obligation
légale. En permettant aux destinataires de se désabonner d’une liste de
diffusion, vous créez un sentiment de confiance avec le public et vous aidez
les entreprises à paraître authentiques (et non spammeurs).

## Activer la fonctionnalité Liste noire

Vous devez d’abord activer la fonctionnalité _Liste noire_. Allez à
l’application Email Marketing ‣ Configuration ‣ Paramètres, activez **Option
de liste noire lors du désabonnement** et cliquez sur **Enregistrer**.

![Vue de la fonctionnalité de liste noire sur la page des paramètres de
l'application Email Marketing d'Konvergo ERP.](../../../_images/blacklist-feature.png)

Une fois que cette fonctionnalité est activée, un lien de _désabonnement_
apparaît dans les mailings. Si les destinataires cliquent sur ce lien, Konvergo ERP
affiche une page de **Désabonnement** , où ils peuvent directement gérer leurs
abonnements.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Avec un mailing de test, le fait de cliquer sur le lien <b>Se désabonner</b> affiche une page d’erreur (<em>erreur 403 - Accès interdit</em>). Pour s’assurer que le lien fonctionne correctement, créez le mailing et envoyez-le uniquement à un email personnel.</p>
</div>

## Liste noire

Outre la possibilité de _Se désabonner_ de listes de diffusion spécifiques, le
destinataire peut également _S’ajouter à la liste noire_ , ce qui signifie
qu’il ne recevra _plus_ d’emails.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La liste de diffusion doit être configurée comme <em>publique</em> pour être visible par les utilisateurs.</p>
</div>

Pour afficher la liste complète des adresses email sur liste noire, allez à
l’application Email Marketing app ‣ Configuration ‣ Adresses email sur liste
noire.

![Vue de le page des adresses email sur liste noire dans Konvergo ERP Email
Marketing.](../../../_images/blacklisted-email-addresses.png)

Lorsqu’un enregistrement sur liste noire est sélectionné sur cette page, Konvergo ERP
affiche une page séparée avec les coordonnées du destinataire sur liste noire.

![Vue d'un formulaire de contact sur liste noire dans Konvergo ERP Email
Marketing.](../../../_images/blacklisted-contact-form.png)

Dans le **chatter** de cette page, vous trouvez un message horodaté, informant
l’utilisateur de la date à laquelle ce destinataire s’est mis sur liste noire
(via une note de journal **Mail Blacklist created**).

## Supprimer des contacts de la liste noire

Pour _supprimer des contacts de la liste noire_ , cliquez sur le bouton
**Supprimer de la liste noire** dans le coin supérieur gauche, lui permettant
d’à nouveau recevoir les mailings.

Lorsque vous cliquez sur **Supprimer de la liste noire** , une fenêtre
contextuelle s’affiche. Dans cette fenêtre contextuelle, l’adresse email
spécifique est répertoriée et il y a un champ **Motif** dans lequel vous
pouvez expliquer pourquoi ce contact a été supprimé de la liste noire.

![Vue de la fenêtre contextuelle de suppression de la liste noire dans
l'application Email Marketing d'Konvergo ERP.](../../../_images/unblacklist-popup.png)

Après avoir rempli ces champs, cliquez sur **Confirmer** pour officiellement
supprimer ce contact de la liste noire.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../email_marketing">Email Marketing</a></p></li>
<li><p><a href="mailing_lists">Listes de diffusion</a></p></li>
</ul>
</div>

