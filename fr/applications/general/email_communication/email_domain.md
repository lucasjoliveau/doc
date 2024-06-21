# Configurer les enregistrements DNS pour envoyer des emails dans Konvergo ERP

## Vue d’ensemble des étiquettes SPAM

Il arrive que des emails provenant d’Konvergo ERP sont mal classés par les différents
fournisseurs de messagerie et se retrouvent dans les dossiers de spam.
Actuellement, certains paramètres sont hors du contrôle d’Konvergo ERP, notamment la
façon dont les différents fournisseurs de messagerie classent les emails
d’Konvergo ERP en fonction de leur propre politique de restriction et/ou de leurs
propres limitations.

Il est standard dans Konvergo ERP que les emails soient reçus à partir du `"nom de
l'auteur" <notifications@mycompany.odoo.com>`. En d’autres termes, cela peut
être traduit par : `"nom de l'auteur"
<{ICP.mail.from.filter}@{mail.catchall.domain}>`. Dans ce cas, ICP signifie
`ir.config.parameters`, c’est-à-dire les Paramètres du système. La
[configuration des notifications](email_servers#email-servers-
notifications) permet d’améliorer considérablement la délivrabilité.

Pour que les serveurs acceptent des emails d’Konvergo ERP plus régulièrement, l’une
des solutions consiste pour les clients à créer des règles dans leur propre
boîte de messagerie. Il est possible d’ajouter un filtre à la boîte de
réception de sorte que lorsqu’un email est reçu d’Konvergo ERP
(`notifications@mycompany.odoo.com`), il est déplacé vers la boîte de
réception. Il est également possible d’ajouter le domaine de la base de
données Konvergo ERP à une liste d’expéditeurs sûrs ou à une liste blanche sur le
domaine de réception.

Si un serveur de messagerie Konvergo ERP apparaît sur une liste noire, notifiez Konvergo ERP à
l’aide d’un [nouveau ticket d’assistance](https://www.odoo.com/help) et
l’équipe d’assistance s’efforcera de retirer les serveurs de la liste noire.

Si la base de données Konvergo ERP utilise un domaine personnalisé pour l’envoi
d’emails à partir d’Konvergo ERP, trois enregistrements doivent être implémentés sur
le DNS du domaine personnalisé pour assurer la délivrabilité des emails. Il
s’agit des enregistrements SPF, DKIM et DMARC. En fin de compte, c’est à la
discrétion de la boîte de réception finale.

## Être conforme au SPF

Le protocole Sender Policy Framework (SPF) permet au propriétaire d’un nom de
domaine de préciser quels serveurs sont autorisés à envoyer des emails à
partir de ce domaine. Lorsqu’un serveur reçoit un email entrant, il vérifie si
l’adresse IP du serveur d’envoi figure sur la liste des adresses IP autorisées
selon l’enregistrement SPF de l’expéditeur.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La vérification <abbr title="Sender Policy Framework">SPF</abbr> est effectuée sur le domaine mentionné dans le champ <code>Return-Path</code> de l’email. Dans le cas d’un email envoyé par Konvergo ERP, ce domaine correspond à la valeur de la clé <code>mail.catchall.domain</code> dans les paramètres de système de la base de données.</p>
</div>

La politique SPF d’un domaine se définit à l’aide d’un enregistrement TXT. La
façon de créer ou de modifier un enregistrement TXT dépend du fournisseur
hébergeant la zone DNS du nom de domaine. Pour que la vérification se fasse
correctement, chaque domaine ne peut avoir qu’un seul enregistrement SPF.

Si le nom de domaine n’a pas encore d’enregistrement SPF, créez-en un en
saisissant ce qui suit : `v=spf1 include:_spf.odoo.com ~all`

Si le nom de domaine a déjà un enregistrement SPF, l’enregistrement doit être
mis à jour (sans en créer un nouveau).

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si l’enregistrement TXT est <code>v=spf1 include:_spf.google.com ~all</code>, vous devez le modifier pour ajouter <code>include:_spf.odoo.com</code>: <code>v=spf1 include:_spf.odoo.com include:_spf.google.com ~all</code></p>
</div>

Vous pouvez vérifier si l’enregistrement SPF est valide avec un outil gratuit
tel que [MXToolbox SPF](https://mxtoolbox.com/spf.aspx).

## Activer DKIM

Le DomainKeys Identified Mail (DKIM) permet à un utilisateur d’authentifier
des emails grâce à une signature électronique.

Lors de l’envoi d’un email, le serveur Konvergo ERP inclut une signature DKIM unique
dans les en-têtes. Le serveur du destinataire déchiffre cette signature à
l’aide de l’enregistrement DKIM dans le nom de domaine de la base de données.
Si la signature et la clé contenues dans l’enregistrement correspondent, cela
garantit que le message est authentique et n’a pas été altéré pendant l’envoi.

Pour activer DKIM, ajoutez un enregistrement CNAME à la zone DNS du nom de
domaine :

`odoo._domainkey IN CNAME odoo._domainkey.odoo.com.`

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si le nom de domaine est <code>mycompany.com</code>, assurez-vous de créer un sous-domaine <code>odoo._domainkey.mycompany.com</code> dont le nom canonique est <code>odoo._domainkey.odoo.com.</code>.</p>
</div>

La façon de créer ou de modifier un enregistrement CNAME dépend du fournisseur
hébergeant la zone DNS du nom de domaine. Les fournisseurs les plus courants
sont énumérés ci-dessous.

Vérifiez si l’enregistrement DKIM est valide avec un outil gratuit, tel que
[DKIM Core](https://dkimcore.org/tools/). Si un sélecteur est demandé,
saisissez `odoo`.

## Verifier la politique DMARC

L’enregistrement Domain-based Message Authentication, Reporting, & Conformance
(DMARC) est un protocole qui unifie SPF et DKIM. Les instructions contenues
dans l’enregistrement DMARC d’un nom de domaine indiquent au serveur
destinataire ce qu’il doit faire avec un email entrant qui échoue à la
vérification SPF et/ou DKIM.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>DMARC : enregistrement TXT</p>
<p><code>v=DMARC1; p=none;</code></p>
</div>

Il y a trois politiques DMARC :

  * `p=none`

  * `p=quarantine`

  * `p=reject`

`p=quarantine` et `p=reject` indiquent au serveur qui reçoit un email de le
mettre en quarantaine ou de le refuser si la vérification SPF et/ou DKIM
échoue.

Si le nom de domaine utilise DMARC et a défini une de ces politiques, le
domaine doit être conforme au SPF ou activez DKIM.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Yahoo ou AOL sont des exemples de fournisseurs de messagerie avec une politique <abbr title="Domain-based Message Authentication, Reporting, &amp; Conformance">DMARC</abbr> définie sur <code>p=reject</code>. Konvergo ERP déconseille fortement d’utiliser une adresse <em>@yahoo.com</em> ou <em>@aol.com</em> pour les utilisateurs de la base de données. Ces emails n’atteindront jamais leur destinataire.</p>
</div>

`p=none` est utilisé pour que le propriétaire du domaine reçoive des rapports
sur les entités utilisant son domaine. Cela ne devrait pas avoir d’incidence
sur la délivrabilité si la vérification DMARC échoue.

Les enregistrements DMARC contiennent des étiquettes sous la forme
d’enregistrements DNS. Ces étiquettes/paramètres permettent d’établir des
rapports, tels que RUA et RUF, ainsi que des spécifications plus précises
telles que PCT, P, SP ADKIM & ASPF. Pour une meilleure pratique, la politique
DMARC ne doit pas être trop restrictive au départ.

Le tableau suivant illustre certaines des étiquettes disponibles :

Nom de l’étiquette | But | Exemple  
---|---|---  
v | Version du protocole | `v=DMARC1`  
pct | Pourcentage de messages soumis à un filtrage | `pct=20`  
ruf | Adresse pour les rapports forensiques | `ruf=mailto:authfail@example.com`  
rua | Adresse pour les rapports résumés | `rua=mailto:aggrep@example.com`  
p | Politique pour le Domaine Organisationnel | `p=quarantine`  
sp | Politique pour les sous-domaines du DO | `sp=reject`  
adkim | Mode d’alignement pour DKIM | `adkim=s`  
aspf | Mode d’alignement pour le SPF | `aspf=r`  
  
Vérifiez l’enregistrement DMARC d’un nom de domaine à l’aide d’un outil tel
que [MXToolbox DMARC](https://mxtoolbox.com/DMARC.aspx).

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://dmarc.org/overview/">Vous trouverez de plus amples informations sur DMARC sur DMARC.org.</a></p>
</div>

## Documentation SPF, DKIM & DMARC des fournisseurs courants

  * [DNS OVH](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/)

  * [SPF OVH](https://docs.ovh.com/us/en/domains/web_hosting_the_spf_record/)

  * [Enregistrement TXT GoDaddy](https://www.godaddy.com/help/add-a-txt-record-19232)

  * [SPF GoDaddy](https://www.godaddy.com/help/add-an-spf-record-19218)

  * [DKIM GoDaddy](https://www.godaddy.com/help/add-a-cname-record-19236)

  * [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/)

  * [DNS CloudFlare](https://support.cloudflare.com/hc/en-us/articles/360019093151)

  * [Domaines Google](https://support.google.com/domains/answer/3290350?hl=en)

  * [DNS Azure](https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal)

Pour tester entièrement la configuration, l’outil [Mail-
Tester](https://www.mail-tester.com/) vous donnera un aperçu complet du
contenu et de la configuration en un seul mail envoyé. Mail-Tester peut
également être utilisé pour configurer des enregistrements pour d’autres
fournisseurs moins connus.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="https://www.mail-tester.com/spf/">Utilisation de Mail-Tester pour configurer des enregistrements SPF pour des transporteurs spécifiques</a></p>
</div>

  *[SPF]: Sender Policy Framework
  *[DKIM]: DomainKeys Identified Mail
  *[DMARC]: Domain-based Message Authentication, Reporting, & Conformance
  *[DNS]: Domain Name System
  *[CNAME]: Canonical Name
  *[RUA]: Adresse pour les rapports résumés
  *[RUF]: Adresse pour les rapports forensiques
  *[PCT]: Pourcentage de message soumis à un filtrage
  *[P]: Politique pour le domaine organisationnel
  *[SP]: Politique pour les sous-domaines du DO
  *[ADKIM]: Mode d'alignement pour le DKIM
  *[ASPF]: Mode d'alignement pour le SPF

