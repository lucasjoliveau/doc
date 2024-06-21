# Synchronisation bancaire

Konvergo ERP peut être directement synchronisé avec votre établissement bancaire pour
que tous les relevés bancaires soient automatiquement importés dans votre base
de données.

Pour vérifier si votre banque est compatible avec Konvergo ERP, allez aux
[Fonctionnalités comptables d’Konvergo ERP](https://www.odoo.com/page/accounting-
features), et cliquez sur **Voir la liste des établissements pris en charge**.

Konvergo ERP prend en charge plus de 25.000 établissements dans le monde entier.

Pour se connecter aux banques, Konvergo ERP utilise plusieurs services web :

  * **Plaid** : États-Unis d’Amérique et Canada

  * **Yodlee** : Dans le monde entier

  * [Salt Edge](bank_synchronization/saltedge): Worldwide

  * [Ponto](bank_synchronization/ponto): Europe

  * [Enable Banking](bank_synchronization/enablebanking): Pays scandinaves

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="transactions">Transactions</a></p>
</div>

## Configuration

### Utilisateurs On-premise

Pour pouvoir utiliser ce service, vous devez disposer d’un abonnement Konvergo ERP
Enterprise valide. Assurez-vous donc que votre base de données est enregistrée
avec votre contrat Konvergo ERP Enterprise. Nous utilisons également un proxy entre
votre base de données et le fournisseur tiers donc, en cas d’erreur de
connexion, veuillez vérifier que vous n’avez pas de pare-feu ou de proxy
bloquant l’adresse suivante :

  * <https://production.odoofin.com/>

### Première synchronisation

Vous pouvez lancer la synchronisation en allant à l’application Comptabilité
et Tableau de bord de Comptabilité ‣ Configuration ‣ Banques : Ajouter un
compte bancaire.

Vous pouvez maintenant rechercher votre établissement bancaire. Sélectionnez-
le et suivez les étapes pour vous synchroniser.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si vous rencontrez des problèmes pendant votre première synchronisation, veuillez vérifier que votre navigateur web ne bloque pas les fenêtres contextuelles et que votre bloqueur de publicités est désactivé.</p>
</div> <div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Lorsque vous choisissez la date de la première synchronisation des relevés bancaires, choisissez la date à laquelle vous commencez à enregistrer les transactions comptables dans votre base de données Konvergo ERP. Par exemple, si vous importez votre solde de clôture dans Konvergo ERP le 31/12/2022 et que vous commencez à enregistrer des transactions comptables le 01/01/2023, votre date de synchronisation devrait être le 01/01/2023.</p>
</div>

Vous devez fournir un numéro de téléphone pendant votre première
synchronisation pour sécuriser votre compte. Nous demandons ces informations
parce que nous ne voulons pas que vos données tombent entre de mauvaises
mains. Par conséquent, si nous détectons des activités suspectes sur votre
compte, nous bloquons toutes les demandes provenant de votre compte, et vous
devez le réactiver en utilisant ce numéro de téléphone.

Le fournisseur tiers peut demander plus d’informations afin de se connecter à
votre établissement bancaire. Ces informations ne sont pas stockées sur les
serveurs d’Konvergo ERP.

Par défaut, les transactions récupérées à partir d’une source en ligne sont
regroupées dans le même relevé, et un relevé bancaire est créé par mois. Vous
pouvez modifier la périodicité de création des relevés bancaires dans les
paramètres de votre journal.

Vous pouvez retrouver toutes vos synchronisations en allant au Tableau de bord
de Comptabilité ‣ Configuration ‣ Comptabilité : Synchronisation en ligne.

### Synchroniser manuellement

Après votre première synchronisation, les journaux créés sont synchronisés par
défaut toutes les 12 heures. Si vous le souhaitez, vous pouvez synchroniser
manuellement en cliquant sur le bouton **Synchroniser maintenant** sur le
tableau de bord.

Ou vous pouvez aller au Tableau de bord de Comptabilité ‣ Configuration ‣
Comptabilité : Synchronisation en ligne, sélectionnez votre établissement et
cliquez sur le bouton **Récupérer les transactions**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Certains établissements n’autorisent pas la récupération automatique des transactions. Pour ces établissements, lors de la synchronisation automatique du compte, vous recevez un message d’erreur vous demandant de désactiver la synchronisation automatique. Ce message se trouve dans le chatter de vos synchronisations en ligne. Dans ce cas, assurez-vous d’effectuer des synchronisations manuelles.</p>
</div>

## Problèmes

### Erreur de synchronisation

Pour signaler une erreur de connexion à l”[Assistance
d’Konvergo ERP](https://www.odoo.com/help), allez au Tableau de bord de Comptabilité ‣
Configuration ‣ Comptabilité : Synchronisation en ligne, sélectionnez la
connexion en échec et copiez la description et la référence de l’erreur.

### Synchronisation déconnectée

Si votre connexion avec le proxy est interrompue, vous pouvez vous reconnecter
au proxy en cliquant sur le bouton **Récupérer le compte**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>If you are unable to reconnect using the <b>Fetch Account</b> button, please contact the
<a href="https://www.odoo.com/help">support</a> directly with your client id or the reference of the error
listed in the chatter.</p>
</div>

## Processus de migration pour les utilisateurs ayant installé Konvergo ERP avant
décembre 2020

Si vous êtes On-premise, assurez-vous d’abord que votre source est à jour avec
la dernière version d’Konvergo ERP.

Les utilisateurs qui ont créé une base de données avant décembre 2020 doivent
installer le nouveau module manuellement pour pouvoir utiliser les nouvelles
fonctionnalités.

Pour ce faire, allez aux Apps ‣ Mettre à jour la liste des Apps, supprimez le
filtre par défaut dans la barre de recherche et saisissez
`account_online_synchronization`. Vouz pouvez ensuite cliquer sur
**Installer**. Enfin, assurez-vous que tous vos utilisateurs actualisent leur
page Konvergo ERP en appuyant sur CTRL+F5.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Toutes les synchronisations précédentes sont déconnectées pendant l’installation et ne fonctionnent plus.</p></li>
<li><p>Vous pouvez les retrouver directement dans le menu synchronisation (Tableau de bord de Comptabilité ‣ Configuration ‣ Comptabilité : Synchronisation en ligne). S’il n’est pas possible de resynchroniser ces connexions, vous devez en établir des nouvelles.</p></li>
<li><p>Ne désinstallez pas <code>account_online_sync</code>, qui est le module précédent de la synchronisation en ligne. Le nouveau module le remplace.</p></li>
<li><p>Par défaut, le module <code>account_online_synchronization</code> est automatiquement installé avec Comptabilité.</p></li>
</ul>
</div>

## FAQ

### La synchronisation ne fonctionne pas en temps réel. Est-ce normal ?

Le processus n’est pas censé travailler en temps réel, car les fournisseurs
tiers synchronisent vos comptes à des intervalles différents. Pour forcer la
synchronisation et la récupération des relevés, allez à votre **Tableau de
bord de comptabilité** et cliquez sur le bouton **Synchroniser maintenant**.
Vous pouvez également synchroniser et récupérer des transactions via le
Tableau de bord de Comptabilité ‣ Configuration ‣ Comptabilité :
Synchronisation en ligne. Certains fournisseurs n’autorisent qu’une seule
actualisation par jour, il est donc possible que le fait de cliquer sur
**Synchroniser maintenant** ne vous donne pas vos dernières transactions si
vous avez déjà effectué cette action plus tôt dans la journée.

Une transaction peut être visible sur votre compte bancaire, mais ne pas être
récupérée si son statut est **En attente**. Seules les transactions dont le
statut est **Comptabilisé** seront récupérées. Si la transaction n’est pas
encore **comptabilisée** , vous devrez attendre que le statut change.

### La fonctionnalité de synchronisation bancaire en ligne est-elle incluse
dans mon contrat ?

  * **Version Community** : Non, cette fonctionnalité n’est pas incluse dans la version Community.

  * **Version en ligne** : Oui, même si vous bénéficiez du contrat One App Free.

  * **Version Entreprise** : Oui, si vous disposez d’un contrat Entreprise valide lié à votre base de données.

### Certaines banques ont un statut « Bêta ». Qu’est-ce que cela signifie ?

Cela signifie que les établissements bancaires ne sont pas encore entièrement
pris en charge par notre fournisseur tiers. Des bugs ou d’autres problèmes
peuvent survenir. Konvergo ERP ne prend pas en charge les problèmes techniques qui
surviennent avec les banques en phase bêta, mais l’utilisateur peut toujours
choisir de se connecter. La connexion avec ces banques contribue au processus
de développement puisque le fournisseur aura des données réelles et un retour
d’information de la connexion.

### Pourquoi mes transactions ne se synchronisent-elles que lorsque
j’actualise manuellement ?

Certaines banques ont des mesures de sécurité supplémentaires et nécessitent
des étapes supplémentaires, telles qu’un code d’authentification SMS/e-mail ou
un autre type de MFA. Pour cette raison, l’intégrateur ne peut pas extraire
les transactions tant que le code de sécurité n’est pas fourni.

### Toutes mes transactions passées ne sont pas dans Konvergo ERP, pourquoi ?

Pour certains établissements, les transactions ne peuvent être récupérées que
jusqu’à 3 mois en arrière.

### Pourquoi ne vois-je aucune transaction ?

Pendant votre première synchronisation, vous avez sélectionné les comptes
bancaires que vous avez décidé de synchroniser avec Konvergo ERP. Si vous n’avez
synchronisé aucun de vos comptes, vous pouvez aller au Tableau de bord de
Comptabilité ‣ Configuration ‣ Comptabilité : Synchronisation en ligne pour
cliquer sur le bouton **Récupérer le compte** sur la connexion.

Il se peut également qu’il n’y ait pas de nouvelles transactions.

Si votre compte bancaire est correctement lié à un journal et que les
transactions publiées ne sont pas visibles dans votre base de données,
veuillez [soumettre un ticket à l’assistance
d’Konvergo ERP](https://www.odoo.com/help).

### Comment mettre à jour mes identifiants bancaires ?

Vous pouvez mettre à jour vos identifiants en allant au Tableau de bord de
Comptabilité ‣ Configuration ‣ Comptabilité : Synchronisation en ligne, ouvrez
la connexion pour laquelle vous voulez mettre à jour vos identifiants et
cliquez sur le bouton **Mettre à jour les identifiants**.

  * [Salt Edge](bank_synchronization/saltedge)
  * [Ponto](bank_synchronization/ponto)
  * [Enable Banking](bank_synchronization/enablebanking)

