# Groupes de messagerie

La fonctionnalité des **groupes de messagerie** permet aux visiteurs du site
web d’avoir une discussion publique par email. Ils peuvent rejoindre un groupe
pour recevoir les emails des autres membres du groupe (c’est-à-dire, les
utilisateurs du site web qui se sont abonnés au groupe) et envoyer de nouveaux
emails à tous les membres du groupe.

Pour activer la fonctionnalité,
[installez](../../general/apps_modules#general-install) le module
**Groupe de messagerie site web** (`website_mail_group`).

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il ne faut pas confondre la fonctionnalité des <b>groupes de messagerie</b> avec les <a href="../../marketing/email_marketing/mailing_lists">Listes de diffusion</a> de l’application Email Marketing.</p>
</div>

## Configurer les groupes de messagerie

Pour configurer les groupes de messagerie, procédez comme suit :

  1. Configurez un alias de messagerie personnalisé en accédant aux **Paramètres généraux** , en faisant défiler vers le bas jusqu’à la section **Discussion** , en activant la fonctionnalité **Serveur de messagerie personnalisé** et en saisissant le **Domaine d’alias** (par ex. `@mycompany.com`).

  2. Allez à Site Web ‣ Configuration ‣ Listes de diffusion, puis cliquez sur **Nouveau**.

  3. Précisez le **Nom du groupe** , l”**Alias de messagerie** , et une **Description**.

  4. Activez l’option **Modérer ce groupe** et précisez les **Modérateurs** si vous voulez modérer les messages de ce groupe. Si le groupe n’est pas modéré, vous pouvez définir les **Utilisateurs responsables** qui peuvent gérer les messages dans le groupe.

  5. Dans l’onglet **Confidentialité** , définissez qui peut s’abonner au groupe de messagerie :

     * **Tout le monde** : pour rendre le groupe de messagerie public pour que tout le monde puisse s’abonner ;

     * **Membres uniquement** : pour uniquement autoriser les utilisateurs définis comme membres à s’abonner au groupe de messagerie ;

     * **Groupe d’utilisateurs sélectionné** : pour uniquement autoriser les utilisateurs du **Groupe autorisé** à s’abonner au groupe de messagerie.

  6. Si le groupe de messagerie est modéré, vous pouvez automatiquement notifier les auteurs lorsque leur message est en attente de modération en activant l’option **Notification automatique** dans l’onglet **Notifier les membres** et écrire un **Message de notification**.

  7. Si vous voulez envoyer des lignes de conduite aux nouveaux abonnés, activez l’option **Envoyer les lignes de conduite aux nouveaux abonnés** et rédigez-les dans l’onglet **Lignes de conduite**. Elles sont particulièrement utiles lorsque le groupe de messagerie est modéré.

## Utiliser les groupes de messagerie

### S’abonner/se désabonner

En fonction de la configuration du groupe de messagerie, les utilisateurs
peuvent s’abonner et se désabonner des groupes de messagerie à partir de la
page du site web (`/groups` par défaut).

![Page web du groupe de messagerie.](../../../_images/mail-group-page.png)

Les utilisateurs internes peuvent également le faire à partir de Site Web ‣
Configuration ‣ Listes de diffusion, à l’aide des boutons **Rejoindre** et
**Quitter**.

### Envoyer des messages

Pour envoyer des messages à un groupe de messagerie, les utilisateurs du sute
web peuvent envoyer un email à l”adresse email du groupe de messagerie. Les
utilisateurs internes peuvent également créer des messages directement dans
Konvergo ERP. Pour ce faire, allez au Site Web ‣ Configuration ‣ Listes de diffusion,
sélectionnez le groupe de messagerie, cliquez sur le bouton intelligent
**Emails** , et cliquez sur **Nouveau**. Remplissez ensuite les champs et
cliquez sur **Envoyer**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><ul>
<li><p>La liste des messages est également accessible en sélectionnant le groupe sur la page <code>/groups</code> du site web.</p></li>
<li><p>Les membres du groupe peuvent également se désinscrire du groupe, accéder à la page du groupe de messagerie et envoyer des emails au groupe en utilisant les URL figurant dans le pied de page des emails du groupe qu’ils ont reçus.</p>
<img alt="URL dans le pied de page d'un email de groupe." src="../../../_images/mail-group-URLs.png"/>
</li>
</ul>
</div>

## Modérer des messages d’un groupe de messagerie

Si la fonctionnalité **Modérer ce groupe** a été activée pour le groupe de
messagerie, un des **Modérateurs** doit approuver les messages du groupe avant
qu’ils ne soient envoyés aux autres membres.

Pour modérer les messages, allez au Site Web ‣ Configuration ‣ Listes de
diffusion, sélectionnez le groupe de messagerie et cliquez sur le bouton
intelligent **À vérifier**. Vous pouvez modérer les messages à l’aide des
boutons situés à la fin de la ligne de message ou sélectionner un message pour
en afficher le contenu et le modérer en conséquence.

> ![Boutons de modération dans la ligne de message.](../../../_images/mail-
> group-moderation.png)

Les actions suivantes sont disponibles :

  * **Accepter** : accepter l’email et l’envoyer aux membres du groupe de messagerie.

  * **Rejeter** : rejeter l’email. Dans la fenêtre contextuelle qui s’ouvre, cliquez sur **Rejeter sans notification** pour rejeter l’email sans notifier l’auteur ou expliquer le rejet du message, puis cliquez sur **Envoyer & Rejeter** pour rejeter le message et donner une explication à l’auteur.

  * **Liste blanche** : mettre l’auteur sur liste blanche, c’est-à-dire automatiquement accepter tous ses emails. Par conséquent, une règle de modération est créée pour l’adresse email de l’auteur avec le statut **Toujours autoriser**.

  * **Bannir** : mettre l’auteur sur liste noir, c’est-à-dire ignorer automatiquement tous ses emails. Dans la fenêtre contextuelle, cliquez sur **Bannir** pour bannir l’auteur sans le notifier ou donner une explication, puis cliquez sur **Envoyer & Bannir** pour bannir l’auteur et lui donner une explication. Par conséquent, une règle de modération est créée pour l’adresse email de l’auteur avec le statut **Exclusion permanente**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les messages peuvent également être modérés à partir de liste de messages du groupe. Allez au Site Web ‣ Groupes ‣ Groupes de listes de diffusion, sélectionnez le groupe de messagerie et cliquez sur le bouton intelligent <b>Emails</b>.</p>
</div>

## Mettre les auteurs sur liste blanche/liste noire

Vous pouvez mettre un auteur sur liste blanche ou sur liste noire directement
à partir d’un message de groupe de messagerie, ou en créant une règle de
modération. Pour ce faire, allez au Site Web ‣ Configuration ‣ Règles de
modération et cliquez sur **Nouveau**. Sélectionnez ensuite le **Groupe** ,
précisez l”**Email** de l’auteur et définissez le champ **Statut**.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les règles de modération du groupe de messagerie sont également accessibles en allant au Site Web ‣ Configuration ‣ Listes de diffusion, en sélectionnant le groupe et en cliquant sur le bouton intelligent <b>Modérations</b>.</p>
</div>

