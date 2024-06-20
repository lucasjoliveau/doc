# API Mailjet

Odoo est compatible avec l”API de Mailjet pour les envois en masse. Configurez
un serveur de mailing dédié via Mailjet en configurant les paramètres du
compte dans le compte Mailjet et la base de données Odoo. Dans certains cas,
les paramètres doivent également être configurés sur les paramètres DNS du
domaine personnalisé.

## Configuration dans Mailjet

### Créer des identifiants d’API

Pour commencer, connectez-vous à la page [Informations du compte
Mailjet](https://app.mailjet.com/account). Ensuite, allez à la section
Expéditeurs & Domaines et cliquez sur Paramètres SMTP et SEND API.

![Lien des paramètres SMTP et Send API dans la section Expéditeurs & Domaines
de Mailjet.](../../../_images/api-settings.png)

Ensuite, copiez les paramètres de configuration SMTP dans un bloc-notes. Ils
se trouvent dans la section Configuration (SMTP seulement). Les paramètres de
configuration SMTP comprennent l’adresse du serveur, l’option de sécurité
requise (Utilisez SSL/TLS), et le numéro de port. Les paramètres sont
nécessaires pour configurer Mailjet dans Odoo, ce qui est abordé dans la
dernière section.

Pour plus d'infos

[Mailjet : Comment configurer mes paramètres SMTP
?](https://documentation.mailjet.com/hc/articles/360043229473)

Important

Odoo bloque le `port 25` sur les bases de données Odoo Online et Odoo.sh.
[Voir la référence ici](email_servers.html#email-servers-restriction).

![Confirmation SMTP dans Mailjet.](../../../_images/smtp-config.png)

Cliquez ensuite sur le bouton Voir tous les identifiants API pour récupérer
les identifiants API de Mailjet.

Ensuite, cliquez sur l’icône de l’œil pour révéler la Clé API. Copiez cette
clé dans un bloc-notes, car elle sert de Nom d’utilisateur dans la
configuration Odoo. Cliquez ensuite sur le bouton Générer une clé secrète pour
générer la Clé secrète. Copiez cette clé dans un bloc-notes, car elle sert de
Mot de passe dans la configuration Odoo.

### Ajouter une ou plusieurs adresses d’expéditeur vérifiées

La prochaine étape est d’ajouter une adresse ou un domaine d’expéditeur dans
les paramètres du compte Mailjet, pour que l’adresse email ou le domaine
puisse envoyer des emails en utilisant les serveurs de Mailjet. Allez d’abord
à la page des [Informations du compte
Mailjet](https://app.mailjet.com/account). Cliquez sur le lien Ajout d’un
domaine ou d’une adresse d’expéditeur dans la section Expéditeurs & Domaines.

![Ajouter un domaine ou une adresse d'expéditeur dans l'interface de
Mailjet.](../../../_images/add-domain-email.png)

Déterminez si l’adresse email de l’expéditeur ou l’ensemble du domaine doit
être ajouté aux paramètres de Mailjet. Il peut être plus facile de configurer
le domaine dans son ensemble si l’accès DNS est disponible. Allez à la section
Ajouter un domaine pour connaître les étapes de l’ajout du domaine.

Note

il est possible de configurer toutes les adresses email des utilisateurs de la
base de données Odoo qui envoient des emails en utilisant les serveurs de
Mailjet doivent être configurées ou le ou les domaines des adresses email des
utilisateurs.

Par défaut, l’adresse email initialement configurée dans le compte Mailjet est
ajoutée en tant qu’expéditeur de confiance. Pour ajouter une autre adresse
email, cliquez sur le bouton Ajouter une autre adresse d’envoi. Ensuite,
ajoutez l’adresse email qui est configurée pour envoyer à partir du domaine
personnalisé.

Au minimum les adresses email suivantes doivent être configurées dans le
fournisseur et vérifiées dans Mailjet :

  * notifications@yourdomain.com

  * bounce@yourdomain.com

  * catchall@yourdomain.com

Note

Remplacez `yourdomain` par le domaine personnalisé de la base de données Odoo.
S’il n’y en a pas, utilisez le paramètre système mail.catchall.domain.

Ensuite, remplissez le formulaire Informations email, veillant à sélectionner
le type d’email approprié : email transactionnel ou envois en masse. Après
avoir complété le formulaire, un email d’activation est envoyé à l’adresse
email et l’expéditeur de confiance peut être activé.

Il est recommandé de configurer les paramètres SPF/DKIM/DMARC sur le domaine
de l’expéditeur.

Pour plus d'infos

[Documentation de Mailjet sur
SPF/DKIM/DMARC](https://documentation.mailjet.com/hc/articles/360042412734-Authenticating-
Domains-with-SPF-DKIM)

Important

Si la base de données n’utilise pas de domaine personnalisé, alors afin de
vérifier l’adresse de l’expéditeur, un alias temporaire (des trois adresses
email susmentionnées) doit être configuré dans Odoo CRM pour créer une piste.
Ensuite, la base de données est capable de recevoir l’email de vérification et
de vérifier les comptes.

### Ajouter un domaine

En ajoutant un domaine entier au compte Mailjet, toutes les adresses
d’expéditeur liées à ce domaine sont automatiquement validées pour l’envoi
d’emails en utilisant les serveurs Mailjet. Allez d’abord à la page
[Informations du compte Mailjet](https://app.mailjet.com/account). Ensuite,
cliquez sur le lien Ajout d’un domaine ou d’une adresse d’expéditeur dans la
section Expéditeurs & Domaines. Cliquez ensuite sur Ajouter un domaine pour
ajouter le domaine personnalisé.

Note

Le domaine doit être ajouté au compte Mailjet et ensuite validé via le DNS.

Après cela, complétez la page Ajouter un nouveau nom de domaine sur Mailjet et
cliquez sur Continuer.

Après avoir ajouté le domaine, une page de validation s’affichera. Sauf si la
base de données Odoo est sur serveur (dans lequel cas, choisissez l”Option 1),
choisissez l”Option 2 : Créer un enregistrement DNS. Copiez les informations
de l’enregistrement TXT dans un bloc-notes et allez au fournisseur DNS du
domaine pour finaliser la validation.

![Les informations d'enregistrement TXT à saisir dans le DNS du
domaine.](../../../_images/host-value-dns.png)

#### Configuration dans le DNS du domaine

Après avoir obtenu les informations de l’enregistrement TXT du compte Mailjet,
ajoutez un enregistrement TXT au DNS du domaine. Ce processus varie en
fonction du fournisseur DNS. Consultez le fournisseur pour connaître le
processus de configuration spécifiques. Les informations de l’enregistrement
TXT contiennent l”Hôte et la Valeur. Collez ces informations dans les champs
correspondants de l’enregistrement TXT.

#### Revenir aux informations du compte Mailjet

Après avoir ajouté l’enregistrement TXT au abbr:`DNS (Domain Name System)` du
domaine, revenez au compte Mailjet. Allez ensuite aux Informations du compte ‣
Ajout d’un domaine ou d’une adresse expéditeur, cliquez sur l’icône
d’engrenage à côté de Domaine et sélectionnez Valider.

Cette action peut également être effectuée en allant à la page [Domaines et
adresses de l’expéditeur](https://app.mailjet.com/account/sender) dans les
Informations du compte Mailjet et en cliquant sur Gérer.

Ensuite, cliquez sur Vérifier maintenant pour valider l’enregistrement TXT qui
a été ajouté au domaine. Un écran de réussite s’affichera si le domaine est
configuré correctement.

![Vérifiez l'enregistrement DNS dans Mailjet.](../../../_images/check-dns.png)

Après avoir configuré le domaine avec succès, il y a une option pour
Authentifier ce domaine (SPF/DKIM). Ce bouton affiche les enregistrements SPF
& DKIM.

Pour plus d'infos

[Documentation de Mailjet sur
SPF/DKIM/DMARC](https://documentation.mailjet.com/hc/articles/360042412734-Authenticating-
Domains-with-SPF-DKIM)

![Authentifier le domaine avec les enregistrements SPF/DKIM dans
Mailjet.](../../../_images/authenticate.png)

## Configuration dans Odoo

Pour compléter la configuration, allez à la base de données Odoo et allez aux
Paramètres. En activant le mode développeur, allez au menu Technique ‣ Email ‣
Serveurs de messagerie sortants. Ensuite, créez une nouvelle configuration de
serveur sortant en cliquant sur le bouton Créer.

Ensuite, saisissez le `serveur SMTP` (in-v3.mailjet.com), le `numéro de port`
(587 ou 465), et la `Sécurité (SSL/TLS)` que vous avez copiés auparavant du
compte Mailjet. Vous pouvez les trouver
[ici](https://app.mailjet.com/account/setup). Il est recommandé d’utiliser
SSL/TLS même si Mailjet ne l’exige pas.

Pour le Nom d’utilisateur, saisissiez la CLÉ API. Pour le Mot de passe,
saisissez la CLÉ SECRÈTE que vous avez copiée auparavant du compte Mailjet
dans le bloc-notes. Vous pouvez trouver ces paramètres dans Mailjet ‣
Paramètres du compte ‣ Paramètres SMTP et SEND API.

Si le serveur Mailjet est utilisé pour les envois en masse, définissez une
valeur de Priorité supérieure à celle de tout serveur de messagerie
transactionnel. Enfin, enregistrez les paramètres et procéder au Test de
connexion.

![Paramètres de serveur de messagerie sortant
d'Odoo.](../../../_images/server-settings.png)

Important

Pour que la fonction de notification fonctionne avec Mailjet, trois paramètres
doivent être configurés dans Odoo.

  1. Le filtre expéditeur doit être défini dans la configuration du serveur. Il est recommandé de le configurer comme un domaine et pas comme une adresse email complète. Il doit correspondre au domaine dans les deux étapes suivantes. Vous trouverez plus d’informations [ici](email_servers.html#email-communication-from-filter).

  2. Le paramètre système mail.default.from doit avoir la valeur `notifications@yourdomain.com`.

  3. Le paramètre système mail.default.from_filter doit avoir la valeur `yourdomain.com`. Remplacez `yourdomain` avec le domaine personnalisé pour la base de données Odoo. S’il n’y en a pas, utilisez le paramètre système mail.catchall.domain.

Pour plus d’informations, consultez [Utiliser une adresse email par
défaut](email_servers.html#email-communication-default).

The System Parameters can be accessed by activating the [developer
mode](../developer_mode.html#developer-mode).

Une fois la configuration terminée, la base de données Odoo est prête à
utiliser le serveur de messagerie Mailjet pour des envois en masse ou des
emails transactionnels !

  *[API]: Application Programming Interface
  *[DNS]: Domain Name System
  *[SMTP]: Simple Mail Transfer Protocol
  *[SSL]: Secure Sockets Layer
  *[TLS]: Transport Layer Security
  *[SPF]: Sender Policy Framework
  *[DKIM]: DomainKeys Identified Mail) à fournir au fournisseur :abbr:`DNS (Domain Name System
  *[DMARC]: Domain-based Message Authentication, Reporting, and Conformance

