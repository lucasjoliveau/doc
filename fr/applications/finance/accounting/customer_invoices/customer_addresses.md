# Adresses de livraison et de facturation

Les entreprises ont souvent plusieurs sites et il arrive souvent qu’une
facture client doit être envoyée à une adresse et que la livraison doit être
effectuée à une autre. La fonctionnalités **Adresses du client** d’Odoo est
conçue pour gérer cette situation et permet de préciser l’adresse à utiliser
dans chaque cas.

Pour plus d'infos

[Processus de facturation](overview.html)

## Configuration

Pour définir les adresses de facturation et de livraison sur une commande
client, allez d’abord à Comptabilité ‣ Configuration ‣ Paramètres. Dans la
section Factures clients, activez Adresses du client et cliquez sur
Enregistrer.

Sur les devis et les commandes, vous trouvez désormais les champs Adresse de
facturation et Adresse de livraison. Si le client a une adresse de facturation
ou de livraison précisée sur leur fiche, le champ correspondant utilisera
cette adresse par défaut, mais l’adresse de n’importe quel contact peut être
utilisée à la place.

## Facturer et livrer à des adresses différentes

Les bons de livraison et leurs bordereaux utilisent l’adresse définie comme
Adresse de livraison sur la commande. Par défaut, les rapports de facturation
indiquent à la fois l’adresse de livraison et l’adresse de facturation afin de
garantir au client que la livraison est effectuée au bon endroit.

Les emails sont également envoyés à des adresses différentes. Le devis et la
commande sont envoyés à l’email du contact principal, comme d’habitude, mais
la facture est envoyée à l’email de l’adresse définie comme Adresse de
facturation sur la commande.

Note

  * Reports, such as the delivery slip and invoice report, can be [customized using Studio](../../../studio/pdf_reports.html).

  * Si l’option [Envoyer par la poste](snailmail.html) est cochée, la facture sera envoyée à l’adresse de facturation lorsque vous cliquez sur Envoyer & Imprimer.

