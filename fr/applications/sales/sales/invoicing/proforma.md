# Factures pro forma

Une _facture pro forma_ est une facture abrégée ou estimée envoyée avant la
livraison des marchandises. Elle indique la nature et la quantité des
marchandises, leur valeur et d’autres informations importantes, telles que le
poids et les frais de transport.

Les factures pro forma sont généralement utilisées comme factures
préliminaires à un devis. Elles sont également utilisées lors de l’importation
à des fins douanières. Elles diffèrent d’une facture normale en ce sens
qu’elles ne constituent _pas_ une demande (ou requête) de paiement.

## Configuration

Pour utiliser les factures pro forma, la fonctionnalité _Facture pro forma_
**doit** être activée.

Pour activer cette fonctionnalité, allez à l’application Ventes ‣
Configuration ‣ Paramètres, et dans la section **Devis & Commandes**, cochez
la case à côté de l’option **Facture pro forma**. Cliquez ensuite sur
**Enregistrer** pour enregistrer tous les changements.

![La fonctionnalité de facture pro forma dans l'application Ventes
d'Konvergo ERP.](../../../../_images/pro-forma-setting.png)

## Envoyer une facture pro forma

Une fois que la fonctionnalité **Facture pro forma** est activée, l’option
d’envoyer une facture pro forma est désormais disponible sur tous les devis ou
commandes clients, en cliquant sur le bouton **Envoyer la facture pro forma**.

![Le bouton Envoyer la facture pro forma sur une commande typique dans Konvergo ERP
Ventes.](../../../../_images/send-pro-forma-invoice-button.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Il n’est <b>pas</b> possible d’envoyer des factures pro forma pour une commande ou un devis si une facture d’acompte a déjà été envoyée, ou pour un abonnement récurrent.</p>
<p>Dans les deux cas, le bouton <b>Envoyer une facture pro forma</b> n’apparaît <b>pas</b>.</p>
<p>Toutefois, des factures pro forma <b>peuvent</b> être envoyées pour des services, inscriptions à des événements, cours et/ou nouveaux abonnements. Les factures pro forme ne sont pas limitées aux biens physiques, consommables ou stockables.</p>
</div>

Lorsque vous cliquez sur le bouton **Envoyer une facture pro forma** , une
fenêtre contextuelle s’ouvre, à partir de laquelle vous pouvez envoyer un
email.

Dans la fenêtre contextuelle, le champ **Destinataires** est automatiquement
rempli avec le client de la commande ou du devis. Le champ **Objet** et le
corps de l’email peuvent être modifiés si nécessaire.

La facture pro forma est automatiquement ajoutée en tant que pièce jointe à
l’email.

Quand l’email est prêt, cliquez sur **Envoyer** et Konvergo ERP envoie l’email
instantanément avec la facture pro forma en pièce jointe au client.

![La fenêtre contextuelle de l'email apparaît avec la facture pro forma en
pièce jointe dans Konvergo ERP Ventes.](../../../../_images/pro-forma-email-message-
pop-up.png) <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour avoir un aperçu de la facture pro forma, cliquez sur le PDF en bas de la fenêtre contextuelle d’email <em>avant</em> de cliquer sur <b>Envoyer</b>. Lorsque vous cliquez sur ce bouton, la facture pro forma est immédiatement téléchargée. Ouvrez ce PDF pour voir (et réviser) la facture pro forma.</p>
<img alt="Exemple d'une facture pro forma au format PDF dans Konvergo ERP Ventes." class="align-center" src="../../../../_images/pro-forma-pdf.png"/>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="invoicing_policy">Facturation basée sur les quantités livrées ou commandées</a></p>
</div>

