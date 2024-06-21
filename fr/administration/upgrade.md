# Mettre à niveau

An upgrade is the process of moving your database from an older version to a
newer [supported version](supported_versions) (e.g., Konvergo ERP 14.0 to Konvergo ERP
16.0). Frequently upgrading is essential as each version comes with new and
improved features, bug fixes, and security patches.

<div class="accordion accordion-flush o_spoiler alert" id="upgrade-faq-rolling-release"><div class="accordion-item"><span class="accordion-header" id="o_spoiler_header_0"><button aria-controls="o_spoiler_content_0" aria-expanded="false" class="accordion-button collapsed flex-row-reverse justify-content-end fw-bold p-0 border-bottom-0" data-bs-target="#o_spoiler_content_0" data-bs-toggle="collapse" type="button">Automatic upgrades: Konvergo ERP Online's Rolling Release process</button></span><div aria-labelledby="o_spoiler_header_0" class="accordion-collapse collapse border-bottom-0" id="o_spoiler_content_0"><div class="accordion-body"><p>Le processus de Rolling Release permet aux clients d’Konvergo ERP Online de mettre à jour leur base de données directement à partir d’un message envoyé à l’administrateur de la base de données dès qu’une nouvelle version est publiée. L’invitation à la mise à niveau n’est envoyée que si aucun problème n’est détecté lors des tests automatiques.</p>
<img alt="Le message de mise à niveau en haut à droite de la base de données" src="../_images/rr-upgrade-message.png"/>
<p>Il est fortement recommandé de tester manuellement <a href="#upgrade-test-your-db"><span class="std std-ref">la mise à niveau d’abord</span></a>. Le fait de cliquer sur <b>Je veux d’abord tester</b> redirige vers <a href="https://www.odoo.com/my/databases/">le gestionnaire de base de données</a>, où il est possible de demander une base de données test mise à niveau et de vérifier si elle présente des anomalies.</p>
<p>Il n’est <b>pas</b> recommandé de cliquer sur <b>Mettre à niveau maintenant</b> sans tester d’abord, car cela déclenche immédiatement la mise à niveau de la base de données de production en direct.</p>
<p>Si le processus de Rolling Release détecte un problème avec la mise à niveau, celle-ci sera désactivée jusqu’à ce que le problème soit résolu.</p>
</div></div></div></div>

Une mise à niveau ne couvre pas :

>   * La rétrogradation vers une version antérieure d’Konvergo ERP
>
>   * [Switching editions](on_premise/community_to_enterprise) (e.g.,
> from Community to Enterprise)
>
>   * [Changing hosting type](hosting#hosting-change-solution) (e.g.,
> from on-premise to Konvergo ERP Online)
>
>   * La migration d’un autre ERP vers Konvergo ERP
>
>

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>

## La mise à niveau en quelques mots

  1. Demandez une base de données test mise à niveau (voir obtenir une base de données test mise à niveau).

  2. Le cas échéant, mettez à niveau le code source de votre module personnalisé pour qu’il soit compatible avec la nouvelle version d’Konvergo ERP (voir [Upgrade a customized database](../developer/howtos/upgrade_custom_db)).

  3. Testez minutieusement la base de données mise à niveau (voir tester la nouvelle version de la base de données).

  4. Report any issue encountered during the testing to Konvergo ERP by [submitting a ticket for an issue related to my future upgrade (I am testing an upgrade)](https://odoo.com/help?stage=migration).

  5. Une fois que tous les problèmes sont résolus et que vous êtes sûr que la base de données mise à niveau peut être utilisée comme base de données principale sans aucun problème, planifiez la mise à niveau de votre base de données de production.

  6. Demandez la mise à niveau de la base de données de production, ce qui la rend indisponible pendant la durée du processus (voir mettre à niveau la base de données de production).

  7. Report any issue encountered during the upgrade to Konvergo ERP by [submitting a ticket for an issue related to my upgrade (production)](https://odoo.com/help?stage=post_upgrade).

## Obtenir une base de données test mise à niveau

La [Page de mise à niveau](https://upgrade.odoo.com/) est la plateforme
principale pour demander une base de données mise à niveau. Cependant, en
fonction du type d’hébergement, vous pouvez mettre à niveau à partir de la
ligne de commande (on-premise), du [gestionnaire de base de données Konvergo ERP
Online](https://odoo.com/my/databases), ou de votre [projet
Konvergo ERP.sh](https://odoo.sh/project).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La plateforme de mise à niveau suit la même <a href="https://www.odoo.com/privacy">Politique vie privée</a> que les autres services d’Konvergo ERP.com. Consultez la <a href="https://www.odoo.com/gdpr">page du Règlement général sur la protection des données</a> pour en savoir plus sur la façon dont Konvergo ERP traite vos données et votre vie privée.</p>
</div>

Konvergo ERP OnlineKonvergo ERP.shOn-premise

Les bases de données d’Konvergo ERP Online peuvent être mises à niveau manuellement
via le [gestionnaire de base de données](https://odoo.com/my/databases).

Le gestionnaire de base de données affiche toutes les bases de données
associées au compte de l’utilisateur. Les bases de données qui ne sont pas sur
la version la plus récente d’Konvergo ERP affichent une flèche dans un cercle à côté
de leur nom, indiquant qu’elles peuvent être mises à niveau.

![Le gestionnaire de base de données avec un bouton de mise à niveau à côté du
nom d'une base de données.](../_images/databases-page.png)

Cliquez sur la **flèche dans un cercle** pour lancer le processus de mise à
niveau. Dans la fenêtre contextuelle, remplissez les champs suivants :

  * La **version** d’Konvergo ERP vers laquelle vous souhaitez vous mettre à niveau, généralement la version la plus récente

  * L’adresse **email** qui doit recevoir le lien vers la base de données mise à niveau

  * La **Finalité** de la mise à niveau, qui est automatiquement définie sur **Test** pour votre première demande de mise à niveau

![La fenêtre contextuelle "Mettre à niveau votre base de
données".](../_images/upgrade-popup.png)

L’étiquette **Mise à niveau en cours** s’affiche à côté du nom de la base de
données jusqu’à la fin du processus. Une fois le processus terminé, un email
contenant un lien vers la base de données test mise à niveau est envoyé à
l’adresse fournie. La base de données est également accessible à partir du
gestionnaire de base de données en cliquant sur la flèche déroulante devant le
nom de la base de données.

![Le fait de cliquer sur la flèche déroulante affiche la base de données test
mise à niveau.](../_images/access-upgraded-db.png)

Konvergo ERP.sh est intégré à la plateforme de mise à niveau pour simplifier le
processus de mise à niveau.

![Projet et onglets Konvergo ERP.sh](../_images/odoo-sh-staging.png)

La **dernière sauvegarde automatique quotidienne de production** est envoyée à
la [plateforme de mise à niveau](https://upgrade.odoo.com).

Une fois que la plateforme de mise à niveau a fini de mettre à jour la
sauvegarde et de l’envoyer sur la branche, elle se met en **mode spécial** :
chaque fois qu’un **commit est poussé** sur la branche, une **opération de
restauration** de la sauvegarde mise à niveau et une **mise à jour de tous les
modules personnalisés** se produisent. Cela vous permet de tester vos modules
personnalisés sur une copie vierge de la base de données mise à niveau. Le
fichier journal du processus de mise à niveau est accessible dans votre
nouvelle version staging mise à niveau en allant à `~/logs/upgrade.log`.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Dans les bases de données où des modules personnalisés sont installés, leur code source doit être mis à jour avec la version cible d’Konvergo ERP avant que la mise à niveau puisse être effectuée. S’il n’y en a pas, le mode « mettre à jour sur commit » est ignoré, la base de données mise à niveau est construite dès qu’elle est transférée de la plateforme de mise à niveau, et le mode de mise à niveau est quitté.</p>
<p>Consultez la page <a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> pour plus d’informations.</p>
</div>

Le processus de mise à niveau standard peut être initié en saisissant la ligne
de commande suivante sur la machine sur laquelle la base de données est
hébergée :

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <your db name> -t <target version>
    

La commande suivante peut être utilisée pour afficher l’aide générale et les
commandes principales :

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) --help
    

Une base de données test mise à niveau peut également être demandée via la
[Page de mise à niveau](https://upgrade.odoo.com/).

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Dans les bases de données où des modules personnalisés sont installés, leur code source doit être mis à jour avec la version cible d’Konvergo ERP avant la mise à niveau. Consultez la page <a href="../developer/howtos/upgrade_custom_db">Upgrade a customized database</a> pour plus d’informations.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Pour des raisons de sécurité, seule la personne qui a soumis la demande de mise à niveau peut la télécharger.</p></li>
<li><p>Pour des raisons de stockage, la copie de la base de données est soumise au serveur de mise à niveau sans filestore. Par conséquent, la base de données mise à niveau ne contient pas le filestore de production.</p></li>
<li><p>Avant de restaurer la base de données mise à niveau, son mémoire fichier doit être fusionné avec le mémoire fichier de production pour pouvoir effectuer des tests dans les mêmes conditions que dans la nouvelle version.</p></li>
<li><p>La base de données mise à niveau contient :</p>
<ul>
<li><p>Un fichier <code>dump.sql</code> contenant la base de données mise à niveau</p></li>
<li><p>Un dossier <code>filestore</code> contenant des fichiers qui ont été extraits des enregistrements de la base de données vers les pièces jointes (s’il y en a) et les nouveaux fichiers Konvergo ERP standard de la version Konvergo ERP ciblée (comme les nouvelles images, icônes, logos des fournisseurs de paiement, etc.). Il s’agit du dossier qui doit être fusionné avec le mémoire fichier de production afin d’obtenir le mémoire fichier complet mis à jour.</p></li>
</ul>
</li>
</ul>
</div>

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Vous pouvez demander plusieurs bases de données de test si vous voulez tester la mise à niveau plus d’une fois.</p>
</div> <div class="alert alert-primary" id="upgrade-upgrade-report">
<p class="alert-title">
Note</p><p>Lorsqu’une demande de mise à niveau est complétée, un rapport de mise à niveau est jointe à l’email de mise à niveau réussie et il devient accessible dans l’application Discussion pour les utilisateurs qui font partie du groupe « Administration / Paramètres ». Ce rapport fournit des informations importantes sur les changements introduits par la nouvelle version.</p>
</div>

## Tester la nouvelle version de la base de données

Il est essentiel de passer du temps à tester la base de données test mise à
niveau pour s’assurer que vous ne serez pas bloqué dans vos activités
quotidiennes par un changement de vue, de comportement ou par un message
d’erreur lorsque la mise à niveau sera opérationnelle.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les bases de données test sont neutralisées et certaines fonctionnalités sont désactivées pour éviter qu’elles n’aient un impact sur la base de données de production :</p>
<ol class="arabic simple">
<li><p>Les actions planifiées sont désactivées.</p></li>
<li><p>Les serveurs de messagerie sortants sont désactivés en archivant les serveurs existants et en ajoutant un faux serveur.</p></li>
<li><p>Les fournisseurs de paiement et les transporteurs sont réinitialisés dans l’environnement de test.</p></li>
<li><p>La synchronisation bancaire est désactivée. Si vous voulez tester la synchronisation, contactez votre fournisseur de synchronisation bancaire pour obtenir des identifiants sandbox.</p></li>
</ol>
</div>

Il est fortement recommandé de tester le plus de flux commerciaux possible
pour s’assurer qu’ils fonctionnent correctement et pour se familiariser avec
la nouvelle version.

<div class="admonition-basic-test-checklist alert">
<p class="alert-title">
Check-list des tests de base</p><ul>
<li><p>Il y a-t-il des vues qui sont désactivées dans votre base de données de test, mais actives dans votre base de données de production ?</p></li>
<li><p>Vos vues habituelles s’affichent-elles correctement ?</p></li>
<li><p>Vos rapports (facture, commande, etc.) sont-ils correctement générés ?</p></li>
<li><p>Les pages de votre site web fonctionnent-elles correctement ?</p></li>
<li><p>Êtes-vous en mesure de créer et de modifier des enregistrements ? (commandes, factures, bons de commande, utilisateurs, contacts, sociétés, etc.)</p></li>
<li><p>Rencontrez-vous des problèmes avec vos modèles d’email ?</p></li>
<li><p>Rencontrez-vous des problèmes avec les traductions enregistrées ?</p></li>
<li><p>Vos filtres de recherche sont-ils toujours présents ?</p></li>
<li><p>Pouvez-vous exporter vos données ?</p></li>
</ul>
</div> <div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>0

If you face an issue while testing your upgraded test database, you can
request the assistance of Konvergo ERP by [submitting a ticket for an issue related to
my future upgrade (I am testing an
upgrade)](https://odoo.com/help?stage=migration). In any case, it is essential
to report any problem encountered during the testing to fix it before
upgrading your production database.

Il se peut que vous rencontriez des différentes significatives avec les vues,
fonctionnalités, champs et modèles standards pendant les tests. Ces
changements ne peuvent pas être annulés au cas par cas. Cependant, si un
changement introduit par une nouvelle version casse une personnalisation, il
est de la responsabilité du mainteneur de votre module personnalisé de le
rendre compatible avec la nouvelle version d’Konvergo ERP.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>1

## Mettre à niveau la base de données de production

Once the tests are completed and you are confident that the upgraded database
can be used as your main database without any issues, it is time to plan the
go-live day. It can be planned in coordination with Konvergo ERP’s upgrade support
analysts by [submitting a ticket for an issue related to my future upgrade (I
am testing an upgrade)](https://odoo.com/help?stage=migration).

Votre base de données de production ne sera pas disponible pendant sa mise à
niveau. Par conséquent, nous vous recommandons de planifier la mise à niveau à
un moment où l’utilisation de la base de données est minimale.

Comme les scripts de mise à niveau standard et votre base de données évoluent
constamment, il est également recommandé de demander fréquemment une autre
base de données de test mise à niveau pour s’assurer que le processus de mise
à niveau est toujours réussi, en particulier s’il prend beaucoup de temps à se
terminer. **Il est également recommandé de répéter entièrement le processus de
mise à niveau la veille de la mise à niveau de la base de données de
production.**

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>2

Le processus de mise à niveau d’une base de données de production est
similaire à la mise à niveau d’une base de données de test avec quelques
exceptions.

Konvergo ERP OnlineKonvergo ERP.shOn-premise

Le processus est similaire à l”obtention d’une base de données de test mise à
niveau, à l’exception de l’option de finalité, qui doit être définie sur
**Production** au lieu de **Test**.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>3

Le processus est similaire à l”obtention d’une base de données de test mise à
niveau sur la branche de **Production**.

![Vue de l'onglet Mise à niveau](../_images/odoo-sh-prod.png)

Le processus est **déclenché dès qu’un nouveau commit est effectué** sur la
branche. Cela permet de synchroniser le processus de mise à niveau avec le
déploiement du code source mis à niveau des modules personnalisés. S’il n’y a
pas de modules personnalisés, le processus de mise à niveau est déclenché
immédiatement.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>4

La mise à jour de vos modules personnalisés doit être réussie pour compléter
le processus de mise à niveau. Assurez-vous que le statut de votre mise à jour
de staging est **réussi** avant de l’essayer en production. Plus
d’informations sur la façon de mettre à niveau vos modules personnalisés
peuvent être trouvées sur [Upgrade a customized
database](../developer/howtos/upgrade_custom_db).

La commande de mise à niveau d’une base de données vers la production est
similaire à celle de la mise à niveau d’une base de données de test à
l’exception de l’argument `test`, qui doit être remplacé par `production`:

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) production -d <your db name> -t <target version>
    

Une base de données de production mise à jour peut également être demandée via
la [Page de mise à niveau](https://upgrade.odoo.com/). Une fois que la base de
données est chargée, toute modification à votre base de données de production
ne sera **pas** présente sur votre base de données mise à niveau. C’est la
raison pour laquelle nous vous recommandons de ne pas l’utiliser pendant le
processus de mise à niveau.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>5

In case of an issue with your production database, you can request the
assistance of Konvergo ERP by [submitting a ticket for an issue related to my upgrade
(production)](https://odoo.com/help?stage=post_upgrade).

## Accord de niveau de service (SLA)

Avec Konvergo ERP Enterprise, la mise à niveau d’une base de données vers la version
la plus récente d’Konvergo ERP est **gratuite** , y compris toute assistance
nécessaire pour rectifier les écarts potentiels dans la base de données mise à
niveau.

Des informations sur les services de mise à niveau inclus dans la licence
d’entreprise sont disponibles dans le contrat d’abonnement [Konvergo ERP Enterprise
Subscription Agreement](../legal/terms/enterprise#upgrade). Cependant,
cette section clarifie les services de mise à niveau auxquels vous pouvez vous
attendre.

### Services de mise à niveau couverts par le SLA

Les bases de données hébergées sur les plateformes cloud d’Konvergo ERP (Konvergo ERP Online
et Konvergo ERP.sh) ou hébergées sur vos serveurs (On-Premise) bénéficient des
services de mise à niveau suivants à tout moment :

  * la mise à niveau de toutes les **applications standards** ;

  * la mise à niveau de toutes les **personnalisations créées avec l’application Studio** , tant que Studio reste installée et que l’abonnement correspondant est toujours actif ; et

  * la mise à niveau de tous les **développements et personnalisations couverts par un abonnement de maintenance des personnalisations**.

Les services de mise à niveau sont limités à la conversion technique et à
l’adaptation d’une base de données (modules et données standards) pour les
rendre compatibles avec la version ciblée par la mise à niveau.

### Services de mise à niveau non couverts par le SLA

Les services de mise à niveau suivants ne sont **pas** inclus :

  * le **nettoyage** des données et des configurations préexistantes lors de la mise à niveau ;

  * la mise à niveau des **modules personnalisés créés en interne ou par des tiers** , y compris les partenaires d’Konvergo ERP ;

  * les lignes de **code ajoutées aux modules standards** , c’est-à-dire les personnalisations créées en dehors de l’application Studio, le code saisi manuellement et les [actions automatisées utilisant le code Python](../applications/studio/automated_actions#studio-automated-actions-action) ; et

  * la **formation** à l’utilisation des fonctionnalités et des flux de travail de la version mise à jour.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Si votre base de données contient des modules personnalisés, elle ne peut pas être mise à niveau tant qu’une version de vos modules personnalisés n’est pas disponible pour la version ciblée d’Konvergo ERP. Pour les clients qui maintiennent leurs propres modules personnalisés, nous vous recommandons de paralléliser le processus en <a href="#upgrade-request-test-database"><span class="std std-ref">demandant une base de données mise à niveau</span></a> tout en <a href="../developer/howtos/upgrade_custom_db">mettant à niveau le code source de vos modules personnalisés</a>.</p>
</div>6

