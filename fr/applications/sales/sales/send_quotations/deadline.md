# Dates limites des devis

Dans l’application _Ventes_ d’Odoo, il est possible de définir des dates
limites sur des devis. Cela encourage les clients à agir rapidement pendant
les négociations de vente, car ils peuvent craindre de manquer une bonne
affaire. En outre, les dates limites peuvent également servir de protection
pour une entreprise au cas où une commande devrait être exécutée à un prix qui
n’est plus rentable pour l’entreprise.

## Expiration du devis

Dans Odoo _Ventes_ , vous avez la possibilité d’ajouter une date d’expiration
à un devis.

Pour ajouter une date d’expiration à un devis, allez à l’application Ventes et
sélectionnez un devis ou créez-en un nouveau en cliquant sur Nouveau.

Sur le formulaire de devis, cliquez sur le champ Expiration pour afficher un
calendrier contextuel. Dans ce calendrier, sélectionnez le mois et la date
souhaités comme date d’expiration du devis.

![Le champ Expiration sur un formulaire de devis standard dans Odoo
Ventes.](../../../../_images/quotation-deadlines-expiration-field.png)

Astuce

En cliquant sur le bouton Aperçu sur un devis, Odoo affiche clairement la date
d’expiration de cette offre spécifique.

![Comment les clients voient les dates limites dans Odoo
Ventes.](../../../../_images/quotation-deadlines-preview.png)

## Expiration d’un modèle de devis

L’application Odoo _Ventes_ vous permet également d’ajouter une date limite
d’expiration aux modèles de devis.

Pour ajouter une date d’expiration à un modèle de devis, allez à l’application
Ventes ‣ Configuration ‣ Modèles de devis, sélectionnez le modèle de devis
auquel vous voulez ajouter une date limite ou cliquez sur Nouveau pour créer
un nouveau modèle de devis à partir de zéro.

Sur le modèle de devis, ajoutez un nombre spécifique de jours dans le champ
Devis expire après, situé sous le nom du modèle de devis. Le nombre de jours
représente la durée de validité du devis avant son expiration.

![Le champ Devis expire après sur un modèle de devis dans Odoo
Ventes.](../../../../_images/quotation-deadlines-expires-after.png)

Ensuite, lorsque ce modèle de devis en particulier est utilisé dans un devis,
la date d’expiration est créée automatiquement, en fonction du nombre de jours
susmentionné. Cependant, cette date peut être modifiée avant d’envoyer le
devis au client.

Pour plus d'infos

[Modèles de devis](quote_template.html)

