# Tarification SMS et FAQ

## De quoi ai-je besoin pour envoyer des SMS ?

La messagerie texte SMS est un service d’achat in-app (IAP) qui _nécessite des
crédits prépayés_ pour fonctionner.

## Combien de types de SMS existe-t-il ?

Il y a 2 types : GSM7 et UNICODE.

**GSM7** est le format standard, avec une limite de 160 caractères par
message, qui comprend les caractères suivants :

![Caractères GSM7 disponibles dans Konvergo ERP SMS
Marketing.](../../../../_images/faq1.png)

**UNICODE** est le format appliqué si un caractère spécial, qui _ne figure
pas_ dans la liste GSM7, est utilisé. Limite par SMS : 70 caractères.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>La limite de taille pour GSM7 SMS est de 160 caractères et de 70 caractères pour Unicode. <em>Au-delà de ces limites, le contenu est divisé en un message en plusieurs parties</em> et la limite des caractères est réduite à 153 pour GSM7 et à 67 pour Unicode. Le système vous informera en temps réel du nombre de SMS que votre message représente.</p>
</div>

## Combien coûte l’envoi d’un SMS ?

Le prix d’un SMS dépend de sa destination et de sa longueur (nombre de
caractères). Pour voir le **prix par pays, consultez** : [Konvergo ERP SMS -
FAQ](https://iap-services.odoo.com/iap/sms/pricing#sms_faq_01).

Le nombre de SMS qu’un message représente sera toujours visible dans la base
de données.

![Nombre de caractères GSM7 que peut contenir un SMS dans Konvergo ERP SMS
Marketing.](../../../../_images/faq2.png)

## Comment acheter des crédits ?

Allez à Paramètres ‣ Acheter des crédits.

![Acheter des crédits pour le SMS Marketing dans Konvergo ERP
Paramètres](../../../../_images/faq3.png)

Ou allez à Paramètres ‣ Voir mes services.

![Utilisez Konvergo ERP IAP pour recharger les crédits pour le SMS Marketing dans Konvergo ERP
Paramètres.](../../../../_images/faq4.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Si vous utilisez Konvergo ERP Online (Saas) ou Konvergo ERP Enterprise, des crédits d’essai gratuits sont disponibles pour que vous puissiez tester la fonctionnalité.</p>
</div>

## Questions plus fréquentes

  1. **Est-ce que mes crédits ont une date d’expiration ?**

Non, les crédits n’expirent pas.

  2. **Puis-je envoyer un SMS vers un numéro (qui n’est pas un mobile) parce que je vois l’icône devant le champ “téléphone” ?**

Seulement si ce numéro de téléphone prend en charge les SMS (par ex. les
téléphones SIP).

  3. **Est-ce que je reçois une facture pour l’achat de mes crédits ?**

Oui.

  4. **Le destinataire peut-il me répondre ?**

Non, il est impossible de répondre au SMS.

  5. **Que se passe-t-il si j’envoie plusieurs SMS à la fois, mais que je n’ai pas assez de crédits pour les envoyer tous ?**

Les SMS multiples envoyés en une fois sont considérés comme une seule
transaction, donc aucun SMS ne sera envoyé tant que vous n’avez pas assez de
crédits pour les envoyer tous.

  6. **Ai-je un historique des SMS envoyés ?**

Un historique des SMS envoyés et de toutes les informations pertinentes
relatives à ses contacts (et au message) se trouvent dans la colonne
**Envoyé** du tableau de bord principal de **SMS Marketing** (dans la vue
**Kanban**).

> Pour obtenir plus d’informations détaillées, sélectionnez un SMS dans le
> tableau de bord principal (dans la vue **Kanban**) et cliquez sur n’importe
> quel lien dans la bannière bleue au-dessus du formulaire détaillé du SMS
> pour en apprendre plus.

  7. **Puis-je envoyer autant de SMS que je veux en une fois ?**

Oui, si vous avez suffisamment de crédits.

  8. **Est-ce que je perds des crédits si j’envoie un SMS à un numéro qui n’existe pas dans la liste des destinataires ?**

Non, pas si le numéro de téléphone n’est pas dans le bon format (par ex. trop
de chiffres). Toutefois, si le SMS est envoyé à la mauvaise personne (ou à un
faux numéro), le crédit de ce SMS sera perdu.

  9. **Que se passe-t-il si j’envoie un SMS à un numéro payant (par ex. un concours pour gagner un ticket pour un festival) ?**

Le SMS ne sera pas livré à ce type de numéro, donc aucun crédit ne sera
déduit.

  10. **Puis-je identifier les numéros qui n’existent pas lorsque j’envoie plusieurs SMS ?**

Seulement ceux dont le format n’est pas valide.

  11. **Comment le règlement RGPD affecte-t-il ce service ?**

Vous trouverez notre [Politique vie privée
ici](https://iap.odoo.com/privacy#sms).

  12. **Puis-je utiliser mon propre fournisseur de SMS ?**

Oui, mais il n’est pas disponible d’entrée de jeu. Les experts d’Konvergo ERP peuvent
vous aider à personnaliser une base de données pour autoriser l’utilisation
d’un fournisseur de SMS personnel. Veuillez consulter nos Success Packs
[ici](https://www.odoo.com/pricing-packs).

