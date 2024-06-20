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
Configuration ‣ Paramètres, et dans la section Devis & Commandes, cochez la
case à côté de l’option Facture pro forma. Cliquez ensuite sur Enregistrer
pour enregistrer tous les changements.

![La fonctionnalité de facture pro forma dans l'application Ventes
d'Odoo.](../../../../_images/pro-forma-setting.png)

## Envoyer une facture pro forma

Une fois que la fonctionnalité Facture pro forma est activée, l’option
d’envoyer une facture pro forma est désormais disponible sur tous les devis ou
commandes clients, en cliquant sur le bouton Envoyer la facture pro forma.

![Le bouton Envoyer la facture pro forma sur une commande typique dans Odoo
Ventes.](../../../../_images/send-pro-forma-invoice-button.png)

Note

Il n’est **pas** possible d’envoyer des factures pro forma pour une commande
ou un devis si une facture d’acompte a déjà été envoyée, ou pour un abonnement
récurrent.

Dans les deux cas, le bouton Envoyer une facture pro forma n’apparaît **pas**.

Toutefois, des factures pro forma **peuvent** être envoyées pour des services,
inscriptions à des événements, cours et/ou nouveaux abonnements. Les factures
pro forme ne sont pas limitées aux biens physiques, consommables ou
stockables.

Lorsque vous cliquez sur le bouton Envoyer une facture pro forma, une fenêtre
contextuelle s’ouvre, à partir de laquelle vous pouvez envoyer un email.

Dans la fenêtre contextuelle, le champ Destinataires est automatiquement
rempli avec le client de la commande ou du devis. Le champ Objet et le corps
de l’email peuvent être modifiés si nécessaire.

La facture pro forma est automatiquement ajoutée en tant que pièce jointe à
l’email.

Quand l’email est prêt, cliquez sur Envoyer et Odoo envoie l’email
instantanément avec la facture pro forma en pièce jointe au client.

![La fenêtre contextuelle de l'email apparaît avec la facture pro forma en
pièce jointe dans Odoo Ventes.](../../../../_images/pro-forma-email-message-
pop-up.png)

Astuce

Pour avoir un aperçu de la facture pro forma, cliquez sur le PDF en bas de la
fenêtre contextuelle d’email _avant_ de cliquer sur Envoyer. Lorsque vous
cliquez sur ce bouton, la facture pro forma est immédiatement téléchargée.
Ouvrez ce PDF pour voir (et réviser) la facture pro forma.

![Exemple d'une facture pro forma au format PDF dans Odoo
Ventes.](../../../../_images/pro-forma-pdf.png)

Pour plus d'infos

[Facturation basée sur les quantités livrées ou
commandées](invoicing_policy.html)

