# Ajouter un nouvel équipement

In Konvergo ERP, _equipment_ refers to any item that is used in everyday operations,
including the manufacturing of products. This can mean a piece of machinery on
a production line, a tool that is used in different locations, or a computer
in an office space. Equipment registered in Konvergo ERP can be owned by the company
that uses the Konvergo ERP database, or by a third party, such as a vendor in the case
of equipment rentals.

Using Konvergo ERP _Maintenance_ , it is possible to track individual pieces of
equipment, along with information about their maintenance requirements. To add
a new piece of equipment, navigate to the **Maintenance** module, select
Equipments ‣ Machines & Tools ‣ Create, and configure the equipment as
follows:

  * **Nom de l’équipement** : le nom de produit de l’équipement

  * **Cagtégorie d’équipement** : la catégorie à laquelle l’équipement appartient, par ex. ordinateurs, machines, outils, etc. Il est possible de créer de nouvelles catégories en allant à Configuration ‣ Catégories d’équipement et en cliquant sur **Créer**

  * **Société** : la société qui possède l’équipement ; là encore, il peut s’agir de la société qui utilise la base de données Konvergo ERP ou d’une société externe

  * **Utilisé par** : précisez si l’équipement est utilisé par un employé spécifique, un département ou les deux ; sélectionnez **Autre** pour préciser à la fois un employé et un département

  * **Équipe de maintenance** : l’équipe responsable de la maintenance de l’équipement ; il est possible de créer de nouvelles équipes en allant à Configuration ‣ Équipes de maintenance et en sélectionnant **Créer** ; les membres de chaque équipe peuvent également être assignés à partir de cette page

  * **Technicien** : la personne responsable de la maintenance de l’équipement ; ceci peut être utilisé pour assigner une personne spécifique dans le cas où aucune équipe de maintenance n’est assignée ou lorsqu’un membre spécifique que l’équipe assignée doit toujours être responsable de l’équipement ; toute personne ajoutée à Konvergo ERP en tant qu’utilisateur peut être assignée en tant que technicien

  * **Lieu d’utilisation** : le lieu où l’équipement est utilisé ; il s’agit d’un simple champ de texte qui peut être utilisé pour préciser des lieux qui ne sont pas des postes de travail, comme un bureau

  * **Poste de travail** : si l’équipement est utilisé à un poste de travail, précisez-le ici ; l’équipement peut également être assigné à un poste de travail en allant à Maintenance ‣ Équipements ‣ Postes de travail, en sélectionnant un poste de travail ou en en créant un nouveau à l’aide du bouton **Créer** et en cliquant sur l’onglet **Équipement** sur le formulaire du poste de travail

![Exemple de formulaire de nouvel équipement entièrement
configuré.](../../../../_images/new-equipment-form.png)

## Inclure des informations supplémentaires sur le produit

L’onglet **Informations sur le produit** au bas du formulaire peut être
utilisé pour fournir plus de détails sur l’équipement :

  * **Fournisseur** : le fournisseur auprès duquel l’équipement a été acheté

  * **Référence fournisseur** : le code de référence attribué au fournisseur

  * **Modèle** : le modèle spécifique de l’équipement

  * **Numéro de série** : le numéro de série unique de l’équipement

  * **Date d’effet** : la date à laquelle l’équipement devient opérationnel ; cette date est utilisée pour calculer le MTBF

  * **Coût** : le montant pour lequel l’équipement a été acheté

  * **Date d’expiration de garantie** : la date à laquelle la garantie de l’équipement expire

![L'onglet des informations sur le produit du nouvel
équipement.](../../../../_images/new-equipment-product-information.png)

## Ajouter des détails de maintenance

L’onglet **Maintenance** contient des informations qui peuvent être utiles aux
équipes de maintenance :

  * **Fréquence de la maintenance préventive** : précise la fréquence à laquelle la maintenance doit être effectuée pour prévenir les défaillances de l’équipement

  * **Durée de maintenance** : le temps nécessaire pour réparer l’équipement lorsqu’il tombe en panne

  * **Temps moyen entre défaillances attendu** : la durée moyenne pendant laquelle l’équipement est censé fonctionner avant de tomber en panne

![L'onglet Maintenance du nouvel équipement.](../../../../_images/new-
equipment-maintenance.png) <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>L’onglet <b>Maintenance</b> contient également les sections <b>Temps moyen entre défaillances</b>, <b>Estimation de la prochaine défaillance</b>, <b>Dernière défaillance</b> et <b>Temps moyen de réparation</b>. Ces valeurs sont calculées automatiquement en fonction des demandes de maintenance, s’il y en a.</p>
</div> <div class="alert alert-info">
<p class="alert-title">
Astuce</p><p>Pour afficher les demandes de maintenance d’un équipement, allez à la page de l’équipement et cliquez sur <b>Maintenance</b> dans le coin supérieur droit du formulaire.</p>
</div>

  *[MTBF]: Temps moyen entre défaillances

