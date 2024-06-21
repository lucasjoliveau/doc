# Évaluations des clients

Demander aux clients d’évaluer l’assistance qu’ils ont reçue d’une équipe d”
_Assistance_ permet d’évaluer les performances de l’équipe et de suivre la
satisfaction des clients. Les évaluations peuvent être publiées sur le
portail, ce qui permet aux clients d’avoir une vue d’ensemble des performances
de l’équipe.

## Activer les évaluations des clients sur une équipe d’assistance

Pour activer les _évaluations des clients_ sur une équipe d’assistance, allez
à Assistance ‣ Configuration ‣ Équipes. Sélectionnez une équipe dans la liste
et allez à la page des paramètres. Faites défiler jusqu’à la section
**Performance** et cochez la case à côté de **Évaluations des clients**.

![Aperçu de la phase des paramètres d'une équipe d'assistance mettant en
évidence la fonctionnalité d'évaluation sur le ticket dans Konvergo ERP
Assistance.](../../../../_images/ratings-enable.png)

## Définir un modèle d’email de demande d’évaluation sur une étape

Pour automatiquement demander une évaluation de la part des clients une fois
que leurs tickets sont clôturés, un modèle d’email doit être ajouté à l’étape
appropriée.

Une fois que le paramètre **Évaluations des clients** a été activé sur la page
des paramètres de l’équipe (voir ci-dessus), cliquez sur le lien **Définir un
modèle d’email par étape**. Sélectionnez une étape dans la liste ou cliquez
sur **Nouveau** pour créer une nouvelle étape.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Les clients ne doivent être invités à évaluer les tickets qu’une fois qu’un problème a été résolu et que leur ticket est clôturé. Par conséquent, un email de <em>demande d’évaluation</em> ne doit être ajouté qu’à une étape qui est <b>repliée</b> dans le kanban, car les tickets dans une <em>étape repliée</em> sont considérés comme clôturés.</p>
</div>

Sur la page des paramètres de l’étape, sélectionnez `Assistance : Demande
d'évaluation du ticket` dans le champ **Modèle d’email**. Ce modèle a été
préconfiguré avec des évaluations que les clients peuvent utiliser pour donner
leur avis. Pour afficher le modèle, cliquez sur le bouton de flèche à droite
du champ.

Une fois que le modèle a été ajouté à l’étape, il enverra automatiquement un
message lorsqu’un ticket est déplacé vers cette étape. Les clients seront
invités à évaluer l’assistance qu’ils ont reçue à l’aide d’icônes de couleur.

>   * _Visage souriant vert_ \- Satisfait
>
>   * _Visage neutre jaune_ \- Bien
>
>   * _Visage renfrogné rouge_ \- Insatisfait
>
>

![Vue d'un modèle d'email standard d'évaluation du service d'assistance pour
Konvergo ERP Assistance.](../../../../_images/ratings-customer-email.png)

Après avoir sélectionné une évaluation, les clients sont redirigés vers une
page web où ils peuvent fournir des commentaires écrits spécifiques pour
étayer leur évaluation. Une fois qu’une évaluation est soumise, elle est
ajoutée au chatter sur le ticket.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Les évaluations des clients peuvent également être consultées via le rapport des <b>Évaluations des clients</b>. Pour afficher ce rapport, allez à Assistance ‣ Analyse ‣ Évaluations des clients.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../../general/companies/email_template">Modèles d’email</a></p>
</div>

## Publier des évaluations sur le portail client

Après avoir activé le paramètre **Évaluations des clients** , une option
permettant de publier les évaluations sur le site web de l’équipe s’affiche.
L’activation de ce paramètre permet aux utilisateurs du portail d’avoir une
vue d’ensemble des évaluations reçues par l’équipe au cours des trente
derniers jours. Les commentaires écrits spécifiques ne seront pas inclus ;
seules les statistiques des performances de l’équipe seront visibles.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Afin d’afficher les évaluations sur le portail client, une équipe doit définir leur paramètre de visibilité sur <b>Utilisateurs portail invités et tous les utilisateurs internes</b>. Ce paramètre figure sur la page des paramètres de l’équipe dans <b>Visibilité</b>.</p>
</div>

Ensuite, pour publier les évaluations, allez à Assistance ‣ Configuration ‣
Équipes et sélectionnez une équipe. Faites défiler jusqu’à **Performance** et
activez la fonctionnalité **Publier les évaluations de cette équipe sur votre
site web**.

Pour afficher les évaluations pour une équipe, un client se connectera au
portail et naviguera vers l’un de ses tickets. Après avoir cliqué sur le nom
d’équipe dans le champ **Géré par** , il sera redirigé vers une page contenant
les évaluations de l’équipe au cours des trente derniers jours.

![Vue de l'aperçu de la performance des évaluations à partir du portail
client.](../../../../_images/ratings-portal-overview.png)

### Masquer manuellement les évaluations individuelles

Les évaluations individuelles peuvent être masquées manuellement à partir du
portail. Cela permet d’exclure des évaluations spécifiques des mesures de
performance affichées aux clients.

Pour rendre une évaluation uniquement visible aux utilisateurs internes,
accédez à la page de l’évaluation. Cela peut se faire d’une des manières
suivantes :

>   * Aller à Assistance ‣ Analyse ‣ Évaluations des clients et cliquez sur
> une des cartes kanban pour une évaluation individuelle.
>
>   * Aller à Assistance ‣ Tickets ‣ Tous les tickets et supprimez le filtre
> **Ouvert** de la barre de recherche. Ensuite, filtrez sur **Satisfait** ,
> **Bien** et/ou **Insatisfait**. Sélectionnez un ticket dans les résultats.
> Cliquez sur le bouton intelligent **Évaluation**.
>
>

Une fois sur la page des détails de l’évaluation, cochez la case **Visible en
interne uniquement**

![Vue de l'aperçu de la performance des évaluations à partir du portail
client.](../../../../_images/ratings-keep-internal.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../advanced/close_tickets">Clôturer des tickets</a></p></li>
<li><p><a href="reports">Analyse</a></p></li>
</ul>
</div>

