# Suivi des factures

Un message de suivi peut être envoyé aux clients lorsqu’un paiement est en
retard. Konvergo ERP vous aide à identifier les paiements en retard et vous permet de
planifier et d’envoyer des rappels appropriés en utilisant des **actions de
relance** qui déclenchent automatiquement une ou plusieurs actions en fonction
du nombre de jours de retard. Vous pouvez envoyer des rappels par différents
moyens, tels que par email, par courrier postal ou par SMS.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="https://www.odoo.com/slides/slide/payment-follow-up-1682">Tutoriels Konvergo ERP : Suivi des paiements</a></p></li>
</ul>
</div>

## Configuration

Pour configurer une **Action de relance** , allez à Comptabilité ‣
Configuration ‣ Niveaux de relance, et sélectionnez ou créez un (de)
nouveau(x) niveau(x) de relance. Plusieurs actions de relance sont disponibles
par défaut dans l’onglet **Notification** et vous pouvez modifier le **nom**
et le **nombre de jours**. Les **Actions** de relance disponibles sont :

  * **Envoyer un email** ;

  * [Envoyer une lettre](../customer_invoices/snailmail#customer-invoices-snailmail);

  * [Envoyer un message SMS](../../../marketing/sms_marketing/pricing/pricing_and_faq#pricing-pricing-and-faq).

Vous pouvez utiliser un modèle prérempli pour vos messages en sélectionnant un
**Modèle de contenu**. Pour changer le modèle utilisé, survolez le champ et
cliquez sur **– >**. Si cette option est activée, les messages SMS disposent
d’un champ spécifique **Modèle de SMS**.

Il est possible d’envoyer automatiquement un rappel en activant l’option
**Automatique** et de joindre la ou les factures _ouvertes_ en activant
l’option **Joindre des factures** , dans le cadre d’une action de relance
spécifique.

En cliquant sur l’onglet **Activité** , il est possible de planifier des
activités (tâches). Ainis, une activité est automatiquement planifiée lorsque
la relance est déclenchée. Pour ce faire, activez l’option **Planifier une
activité** et sélectionnez une personne **Responsable** pour la tâche.
Choisissez un **Type d’activité** et saisissez un **Résumé** de la façon de
traiter l’activité, si vous le souhaitez.

<div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Définissez un nombre de jours négatif pour envoyer un rappel avant la date d’échéance réelle.</p>
</div>

## Rapports de relance

Les factures en retard que vous devez suivre sont disponibles dans
Comptabilité ‣ Clients ‣ Rapports de relance. Konvergo ERP applique par défaut le
filtre **Factures en retard** , mais vous pouvez également filtrer par
**Nécessite une action** dans le menu des **Filtres**.

Lorsque vous sélectionnez une facture, vous pouvez voir toutes les factures
impayées du client (en retard ou non), les dates d’échéance des factures en
retard apparaissant en rouge. Vous pouvez exclure des factures d’un rappel en
cliquant sur **Exclure des relances**. Vous pouvez définir des rappels
**automatiques** ou **Manuels** , ainsi qu’une personne **responsable** pour
ce client.

Pour envoyer des rappels, cliquez sur **Relance** et sélectionnez l’action ou
les actions que vous souhaitez effectuer :

  * **Imprimer** ;

  * **Email** ;

  * **SMS** ;

  * **Par la poste**.

Vous pouvez **joindre des factures** et modifier les modèles de contenu dans
cette vue. Lorsque vous avez fini, cliquez sur **Envoyer** ou **Envoyer &
Imprimer**.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Les informations de contact figurant sur la facture ou la fiche du contact sont utilisées pour envoyer le rappel.</p></li>
<li><p>Lorsque le rappel est envoyé, il est documenté dans le chatter de la facture.</p></li>
<li><p>Si ce n’est pas le moment d’envoyer un rappel, vous pouvez indiquer la date du <b>Prochain rappel</b>. Vous recevrez le prochain rapport en fonction de la date du prochain rappel.</p></li>
</ul>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Rapprochez tous les relevés bancaires juste avant de lancer le processus de rappel pour éviter d’envoyer un rappel à un client qui a déjà payé la facture.</p>
</div>

### Niveau de confiance du débiteur

Pour savoir si un client paie généralement en retard ou non, vous pouvez
définir un niveau de confiance en le marquant comme **Bon débiteur** ,
**Débiteur normal** , ou **Mauvais débiteur** sur leur rapport de relance.
Pour ce faire, cliquez sur la puce à côté du nom du client et sélectionnez un
niveau de confiance.

![Définir le niveau de confiance du débiteur](../../../../_images/debtor-
level.png)

### Envoyer des rappels groupés

Vous pouvez envoyer des emails de rappel groupés à partir de la page des
**Rapports de relance**. Pour ce faire, sélectionnez tous les rapports que
vous souhaitez traiter, cliquez sur l’icône d’engrenage **Action** et
sélectionnez **Traiter les relances**.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
<li><p><a href="../../../marketing/sms_marketing/pricing/pricing_and_faq">Tarification SMS et FAQ</a></p></li>
<li><p><a href="../customer_invoices/snailmail">Envoi postal</a></p></li>
</ul>
</div>

