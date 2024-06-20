# Mettre à niveau

An upgrade is the process of moving your database from an older version to a
newer [supported version](supported_versions.html) (e.g., Odoo 14.0 to Odoo
16.0). Frequently upgrading is essential as each version comes with new and
improved features, bug fixes, and security patches.

Automatic upgrades: Odoo Online's Rolling Release process

Le processus de Rolling Release permet aux clients d’Odoo Online de mettre à
jour leur base de données directement à partir d’un message envoyé à
l’administrateur de la base de données dès qu’une nouvelle version est
publiée. L’invitation à la mise à niveau n’est envoyée que si aucun problème
n’est détecté lors des tests automatiques.

![Le message de mise à niveau en haut à droite de la base de
données](../_images/rr-upgrade-message.png)

Il est fortement recommandé de tester manuellement la mise à niveau d’abord.
Le fait de cliquer sur Je veux d’abord tester redirige vers [le gestionnaire
de base de données](https://www.odoo.com/my/databases/), où il est possible de
demander une base de données test mise à niveau et de vérifier si elle
présente des anomalies.

Il n’est **pas** recommandé de cliquer sur Mettre à niveau maintenant sans
tester d’abord, car cela déclenche immédiatement la mise à niveau de la base
de données de production en direct.

Si le processus de Rolling Release détecte un problème avec la mise à niveau,
celle-ci sera désactivée jusqu’à ce que le problème soit résolu.

Une mise à niveau ne couvre pas :

>   * La rétrogradation vers une version antérieure d’Odoo
>
>   * [Switching editions](on_premise/community_to_enterprise.html) (e.g.,
> from Community to Enterprise)
>
>   * [Changing hosting type](hosting.html#hosting-change-solution) (e.g.,
> from on-premise to Odoo Online)
>
>   * La migration d’un autre ERP vers Odoo
>
>

Avertissement

Si votre base de données contient des modules personnalisés, elle ne peut pas
être mise à niveau tant qu’une version de vos modules personnalisés n’est pas
disponible pour la version ciblée d’Odoo. Pour les clients qui maintiennent
leurs propres modules personnalisés, nous vous recommandons de paralléliser le
processus en demandant une base de données mise à niveau tout en [mettant à
niveau le code source de vos modules
personnalisés](../developer/howtos/upgrade_custom_db.html).

## La mise à niveau en quelques mots

  1. Demandez une base de données test mise à niveau (voir obtenir une base de données test mise à niveau).

  2. Le cas échéant, mettez à niveau le code source de votre module personnalisé pour qu’il soit compatible avec la nouvelle version d’Odoo (voir [Upgrade a customized database](../developer/howtos/upgrade_custom_db.html)).

  3. Testez minutieusement la base de données mise à niveau (voir tester la nouvelle version de la base de données).

  4. Report any issue encountered during the testing to Odoo by [submitting a ticket for an issue related to my future upgrade (I am testing an upgrade)](https://odoo.com/help?stage=migration).

  5. Une fois que tous les problèmes sont résolus et que vous êtes sûr que la base de données mise à niveau peut être utilisée comme base de données principale sans aucun problème, planifiez la mise à niveau de votre base de données de production.

  6. Demandez la mise à niveau de la base de données de production, ce qui la rend indisponible pendant la durée du processus (voir mettre à niveau la base de données de production).

  7. Report any issue encountered during the upgrade to Odoo by [submitting a ticket for an issue related to my upgrade (production)](https://odoo.com/help?stage=post_upgrade).

## Obtenir une base de données test mise à niveau

La [Page de mise à niveau](https://upgrade.odoo.com/) est la plateforme
principale pour demander une base de données mise à niveau. Cependant, en
fonction du type d’hébergement, vous pouvez mettre à niveau à partir de la
ligne de commande (on-premise), du [gestionnaire de base de données Odoo
Online](https://odoo.com/my/databases), ou de votre [projet
Odoo.sh](https://odoo.sh/project).

Note

La plateforme de mise à niveau suit la même [Politique vie
privée](https://www.odoo.com/privacy) que les autres services d’Odoo.com.
Consultez la [page du Règlement général sur la protection des
données](https://www.odoo.com/gdpr) pour en savoir plus sur la façon dont Odoo
traite vos données et votre vie privée.

Odoo OnlineOdoo.shOn-premise

Les bases de données d’Odoo Online peuvent être mises à niveau manuellement
via le [gestionnaire de base de données](https://odoo.com/my/databases).

Le gestionnaire de base de données affiche toutes les bases de données
associées au compte de l’utilisateur. Les bases de données qui ne sont pas sur
la version la plus récente d’Odoo affichent une flèche dans un cercle à côté
de leur nom, indiquant qu’elles peuvent être mises à niveau.

![Le gestionnaire de base de données avec un bouton de mise à niveau à côté du
nom d'une base de données.](../_images/databases-page.png)

Cliquez sur la **flèche dans un cercle** pour lancer le processus de mise à
niveau. Dans la fenêtre contextuelle, remplissez les champs suivants :

  * La **version** d’Odoo vers laquelle vous souhaitez vous mettre à niveau, généralement la version la plus récente

  * L’adresse **email** qui doit recevoir le lien vers la base de données mise à niveau

  * La Finalité de la mise à niveau, qui est automatiquement définie sur Test pour votre première demande de mise à niveau

![La fenêtre contextuelle "Mettre à niveau votre base de
données".](../_images/upgrade-popup.png)

L’étiquette Mise à niveau en cours s’affiche à côté du nom de la base de
données jusqu’à la fin du processus. Une fois le processus terminé, un email
contenant un lien vers la base de données test mise à niveau est envoyé à
l’adresse fournie. La base de données est également accessible à partir du
gestionnaire de base de données en cliquant sur la flèche déroulante devant le
nom de la base de données.

![Le fait de cliquer sur la flèche déroulante affiche la base de données test
mise à niveau.](../_images/access-upgraded-db.png)

Odoo.sh est intégré à la plateforme de mise à niveau pour simplifier le
processus de mise à niveau.

![Projet et onglets Odoo.sh](../_images/odoo-sh-staging.png)

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

Important

Dans les bases de données où des modules personnalisés sont installés, leur
code source doit être mis à jour avec la version cible d’Odoo avant que la
mise à niveau puisse être effectuée. S’il n’y en a pas, le mode « mettre à
jour sur commit » est ignoré, la base de données mise à niveau est construite
dès qu’elle est transférée de la plateforme de mise à niveau, et le mode de
mise à niveau est quitté.

Consultez la page [Upgrade a customized
database](../developer/howtos/upgrade_custom_db.html) pour plus
d’informations.

Le processus de mise à niveau standard peut être initié en saisissant la ligne
de commande suivante sur la machine sur laquelle la base de données est
hébergée :

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) test -d <your db name> -t <target version>
    

La commande suivante peut être utilisée pour afficher l’aide générale et les
commandes principales :

    
    
    $ python <(curl -s https://upgrade.odoo.com/upgrade) --help
    

Une base de données test mise à niveau peut également être demandée via la
[Page de mise à niveau](https://upgrade.odoo.com/).

Important

Dans les bases de données où des modules personnalisés sont installés, leur
code source doit être mis à jour avec la version cible d’Odoo avant la mise à
niveau. Consultez la page [Upgrade a customized
database](../developer/howtos/upgrade_custom_db.html) pour plus
d’informations.

Note

  * Pour des raisons de sécurité, seule la personne qui a soumis la demande de mise à niveau peut la télécharger.

  * Pour des raisons de stockage, la copie de la base de données est soumise au serveur de mise à niveau sans filestore. Par conséquent, la base de données mise à niveau ne contient pas le filestore de production.

  * Avant de restaurer la base de données mise à niveau, son mémoire fichier doit être fusionné avec le mémoire fichier de production pour pouvoir effectuer des tests dans les mêmes conditions que dans la nouvelle version.

  * La base de données mise à niveau contient :

    * Un fichier `dump.sql` contenant la base de données mise à niveau

    * Un dossier `filestore` contenant des fichiers qui ont été extraits des enregistrements de la base de données vers les pièces jointes (s’il y en a) et les nouveaux fichiers Odoo standard de la version Odoo ciblée (comme les nouvelles images, icônes, logos des fournisseurs de paiement, etc.). Il s’agit du dossier qui doit être fusionné avec le mémoire fichier de production afin d’obtenir le mémoire fichier complet mis à jour.

Note

Vous pouvez demander plusieurs bases de données de test si vous voulez tester
la mise à niveau plus d’une fois.

Note

Lorsqu’une demande de mise à niveau est complétée, un rapport de mise à niveau
est jointe à l’email de mise à niveau réussie et il devient accessible dans
l’application Discussion pour les utilisateurs qui font partie du groupe «
Administration / Paramètres ». Ce rapport fournit des informations importantes
sur les changements introduits par la nouvelle version.

## Tester la nouvelle version de la base de données

Il est essentiel de passer du temps à tester la base de données test mise à
niveau pour s’assurer que vous ne serez pas bloqué dans vos activités
quotidiennes par un changement de vue, de comportement ou par un message
d’erreur lorsque la mise à niveau sera opérationnelle.

Note

Les bases de données test sont neutralisées et certaines fonctionnalités sont
désactivées pour éviter qu’elles n’aient un impact sur la base de données de
production :

  1. Les actions planifiées sont désactivées.

  2. Les serveurs de messagerie sortants sont désactivés en archivant les serveurs existants et en ajoutant un faux serveur.

  3. Les fournisseurs de paiement et les transporteurs sont réinitialisés dans l’environnement de test.

  4. La synchronisation bancaire est désactivée. Si vous voulez tester la synchronisation, contactez votre fournisseur de synchronisation bancaire pour obtenir des identifiants sandbox.

Il est fortement recommandé de tester le plus de flux commerciaux possible
pour s’assurer qu’ils fonctionnent correctement et pour se familiariser avec
la nouvelle version.

Check-list des tests de base

  * Il y a-t-il des vues qui sont désactivées dans votre base de données de test, mais actives dans votre base de données de production ?

  * Vos vues habituelles s’affichent-elles correctement ?

  * Vos rapports (facture, commande, etc.) sont-ils correctement générés ?

  * Les pages de votre site web fonctionnent-elles correctement ?

  * Êtes-vous en mesure de créer et de modifier des enregistrements ? (commandes, factures, bons de commande, utilisateurs, contacts, sociétés, etc.)

  * Rencontrez-vous des problèmes avec vos modèles d’email ?

  * Rencontrez-vous des problèmes avec les traductions enregistrées ?

  * Vos filtres de recherche sont-ils toujours présents ?

  * Pouvez-vous exporter vos données ?

Example of end-to-end testing

  * Vérifier un produit aléatoire dans votre catalogue de produits et comparer ses données de test et de production pour vérifie que tout est identique (catégorie de produit, prix de vente, coût, fournisseur, comptes, routes, etc.).

  * Acheter ce produit (application Achats)

  * Confirmer la réception de ce produit (application Inventaire).

  * Vérifier si la route pour recevoir ce produit est la même dans votre base de données de production (application Inventaire).

  * Vendre ce produit (application Ventes) à un client aléatoire.

  * Ouvrir votre base de données client (application Contacts), sélectionner un client (ou une société) et vérifier ses données.

  * Expédier ce produit (application Inventaire).

  * Vérifier si la route pour expédier ce produit est la même que dans votre base de données de production (application Inventaire).

  * Valider la facture d’un client (application Facturation ou Comptabilité).

  * Créditer la facture (émettre un avoir) et vérifier si le comportement est le même que dans votre base de données de production.

  * Vérifier les résultats de vos rapports (application Comptabilité).

  * Vérifier vos taxes, devises, comptes bancaires et exercice fiscal de manière aléatoire (application Comptabilité).

  * Placer une commande en ligne (applications Site Web) à partir de la sélection de produits dans votre boutique jusqu’au passage en caisse et vérifier si le comportement est le même que dans votre base de données de production.

Cette liste n’est **pas** exhaustive. Étendez l’exemple à vos autres
applications en fonction de votre utilisation d’Odoo.

If you face an issue while testing your upgraded test database, you can
request the assistance of Odoo by [submitting a ticket for an issue related to
my future upgrade (I am testing an
upgrade)](https://odoo.com/help?stage=migration). In any case, it is essential
to report any problem encountered during the testing to fix it before
upgrading your production database.

Il se peut que vous rencontriez des différentes significatives avec les vues,
fonctionnalités, champs et modèles standards pendant les tests. Ces
changements ne peuvent pas être annulés au cas par cas. Cependant, si un
changement introduit par une nouvelle version casse une personnalisation, il
est de la responsabilité du mainteneur de votre module personnalisé de le
rendre compatible avec la nouvelle version d’Odoo.

Astuce

N’oubliez pas de tester :

  * Les intégrations avec les logiciels externes (EDI, APIs, etc.)

  * Les flux de travail entre différentes applications (ventes en ligne avec eCommerce, convertir une piste en commande, livraison de produits, etc.)

  * Les exports de données

  * Les actions automatisées

  * Les actions serveur dans le menu d’action sur les formulaires, ainsi qu’en sélectionnant plusieurs enregistrements sur les vues de liste.

## Mettre à niveau la base de données de production

Once the tests are completed and you are confident that the upgraded database
can be used as your main database without any issues, it is time to plan the
go-live day. It can be planned in coordination with Odoo’s upgrade support
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

Important

La mise en production sans avoir effectué de tests préalables peut entraîner :

  * Des utilisateurs qui ne s’adaptent pas aux changements et aux nouvelles fonctionnalités

  * Des interruptions d’activité (par ex. ne plus avoir la possibilité de valider une action)

  * Une mauvaise expérience client (par ex. un site web d’eCommerce qui ne fonctionne pas correctement)

Le processus de mise à niveau d’une base de données de production est
similaire à la mise à niveau d’une base de données de test avec quelques
exceptions.

Odoo OnlineOdoo.shOn-premise

Le processus est similaire à l”obtention d’une base de données de test mise à
niveau, à l’exception de l’option de finalité, qui doit être définie sur
Production au lieu de Test.

Avertissement

Une fois que la mise à niveau est demandée, la base de données ne sera pas
disponible jusqu’à la fin de la mise à niveau. Une fois le processus terminé,
il est impossible de revenir à la version précédente.

Le processus est similaire à l”obtention d’une base de données de test mise à
niveau sur la branche de Production.

![Vue de l'onglet Mise à niveau](../_images/odoo-sh-prod.png)

Le processus est **déclenché dès qu’un nouveau commit est effectué** sur la
branche. Cela permet de synchroniser le processus de mise à niveau avec le
déploiement du code source mis à niveau des modules personnalisés. S’il n’y a
pas de modules personnalisés, le processus de mise à niveau est déclenché
immédiatement.

Important

La base de données n’est pas disponible pendant le processus. En cas de
problème, la plateforme annule automatiquement la mise à niveau, comme elle le
fait pour une mise à jour régulière. En cas de réussite, une sauvegarde de la
base de données avant la mise à niveau est créée.

La mise à jour de vos modules personnalisés doit être réussie pour compléter
le processus de mise à niveau. Assurez-vous que le statut de votre mise à jour
de staging est réussi avant de l’essayer en production. Plus d’informations
sur la façon de mettre à niveau vos modules personnalisés peuvent être
trouvées sur [Upgrade a customized
database](../developer/howtos/upgrade_custom_db.html).

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

Important

Lors de la demande d’une base de données mise à niveau à des fins de
production, la copie est soumise sans mémoire fichier. Par conséquent, le
mémoire fichier de la base de données mise à niveau doit être fusionné avec le
mémoire fichier de production avant de déployer la nouvelle version.

In case of an issue with your production database, you can request the
assistance of Odoo by [submitting a ticket for an issue related to my upgrade
(production)](https://odoo.com/help?stage=post_upgrade).

## Accord de niveau de service (SLA)

Avec Odoo Enterprise, la mise à niveau d’une base de données vers la version
la plus récente d’Odoo est **gratuite** , y compris toute assistance
nécessaire pour rectifier les écarts potentiels dans la base de données mise à
niveau.

Des informations sur les services de mise à niveau inclus dans la licence
d’entreprise sont disponibles dans le contrat d’abonnement [Odoo Enterprise
Subscription Agreement](../legal/terms/enterprise.html#upgrade). Cependant,
cette section clarifie les services de mise à niveau auxquels vous pouvez vous
attendre.

### Services de mise à niveau couverts par le SLA

Les bases de données hébergées sur les plateformes cloud d’Odoo (Odoo Online
et Odoo.sh) ou hébergées sur vos serveurs (On-Premise) bénéficient des
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

  * la mise à niveau des **modules personnalisés créés en interne ou par des tiers** , y compris les partenaires d’Odoo ;

  * les lignes de **code ajoutées aux modules standards** , c’est-à-dire les personnalisations créées en dehors de l’application Studio, le code saisi manuellement et les [actions automatisées utilisant le code Python](../applications/studio/automated_actions.html#studio-automated-actions-action) ; et

  * la **formation** à l’utilisation des fonctionnalités et des flux de travail de la version mise à jour.

Pour plus d'infos

  * [Documentation Odoo.sh](odoo_sh.html)

  * [Supported Odoo versions](supported_versions.html)

