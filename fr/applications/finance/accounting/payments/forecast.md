# Prévoir les futures factures à payer

Dans Odoo, vous pouvez gérer les paiements en définissant des **Conditions de
paiement** et des **relances** automatiques.

## Configuration : conditions de paiement

Afin de suivre les conditions des fournisseurs, nous utilisons des
**Conditions de paiement** dans Odoo. Elles permettre de garder une trace des
dates d’échéance sur les factures. Voici quelques exemples de **Conditions de
paiement** :

  * 50% dans les 30 jours

  * 50% dans les 45 jours

Pour les créer, allez à Comptabilité ‣ Configuration ‣ Facturation :
Conditions de paiement et cliquez sur Créer pour ajouter de nouvelles
conditions ou cliquez sur des conditions existantes pour les modifier.

Pour plus d'infos

[Tutoriels Odoo : Conditions de
paiement](https://www.odoo.com/slides/slide/payment-terms-1679?fullscreen=1)

Une fois que les **Conditions de paiement** sont définis, vous pouvez les
assigner à votre fournisseur par défaut. Pour ce faire, allez à Fournisseurs ‣
Fournisseurs, sélectionnez un fournisseur, cliquez sur l’onglet Ventes &
Achats et sélectionnez des **Conditions de paiement** spécifiques. Ainsi,
chaque fois que vous achetez auprès de ce fournisseur, Odoo propose
automatiquement les conditions de paiement sélectionnées.

Note

Si vous ne définissez pas de conditions de paiement spécifiques sur un
fournisseur, vous pouvez toujours en définir sur la facture fournisseur.

## Prévoir les factures à payer avec la balance âgée des fournisseurs

Pour suivre les montants à payer aux fournisseurs, vous pouvez utiliser la
**Balance âgée des fournisseurs**. Vous pouvez y accéder en allant à
Comptabilité ‣ Analyse ‣ Rapports de partenaires : Balance âgée des
fournisseurs. Ce rapport vous donne un résumé par fournisseur des montants à
payer, comparés à leur date d’échéance (la date d’échéance étant calculée sur
chaque facture à l’aide des conditions). Ce rapport vous indique combien vous
devez payer dans les mois à venir.

## Sélectionner les factures à payer

Vous pouvez obtenir une liste de toutes vos factures fournisseurs en allant à
Fournisseurs ‣ Factures fournisseurs. Pour uniquement afficher les factures
que vous devez payer, cliquez sur Filtres ‣ Factures à payer. Pour uniquement
afficher les paiements en retard, sélectionnez plutôt le filtre En retard.

Vous pouvez également regrouper les factures par date d’échéance en cliquant
sur Regrouper par ‣ Date d’échéance et en sélectionnant une période.

