# Utiliser le programme directeur de production

Le programme directeur de production (PDP) est un outil précieux pour
planifier votre production sur la base de vos prévisions de demande.

## Configuration

Allez à l’application Fabrication ‣ Configuration ‣ Paramètres et activez la
fonctionnalité Programme directeur de production avant de cliquer sur
Enregistrer.

Astuce

Dans les paramètres du PDP, vous pouvez définir la page de temps de votre PDP
(mensuel/hebdomadaire/quotidien) et le nombre de périodes que vous voulez
afficher à tout moment.

Allez à présent à Planning ‣ Programme directeur de production et cliquez sur
_Ajouter un produit_. Vous pouvez définir le stock de sécurité (= le stock
disponible à la fin de la période) et les quantités minimales et maximales qui
peuvent ou doivent être réapprovisionnées dans chaque période.

![../../../../_images/mps_1.png](../../../../_images/mps_1.png)

Dans la vue PDP, vous pouvez décider quelles informations vous voulez afficher
en cliquant sur _lignes_. Par exemple, la _demande réelle_ vous montrera
quelle quantité de produits a déjà été commandée pour la période, ou le
_disponible à promettre_ , ce qui peut encore être vendu pendant cette même
période (ce que vous prévoyez de réapprovisionner - ce qui est déjà vendu
pendant la période). Vous pouvez également décider de masquer les lignes si
vous le voulez.

![../../../../_images/mps_2.png](../../../../_images/mps_2.png)

## Estimer votre demande et lancer le réassort

La prochaine étape consiste à estimer la demande pour la période choisie. Cela
se fait dans la ligne _Demande prévue_. À tout moment, vous pouvez comparer la
demande prévue avec la demande actuelle (= ventes confirmées). La demande
prévue pour un produit fini aura une incidence sur la demande indirecte de ses
composants.

![../../../../_images/mps_3.png](../../../../_images/mps_3.png)

Une fois la demande prévue fixée, la quantité à réapprovisionner pour les
différentes périodes sera automatiquement calculée. Les réassorts que vous
êtes censé lancer en fonction de vos délais (délai fournisseur ou délai de
fabrication) sont alors affichés en vert. Vous pouvez à présent lancer le
réassort en cliquant sur le bouton Réapprovisionner.

En fonction de la configuration du produit (acheter ou fabrication), des
demandes de prix ou des ordres de fabrication seront créés. Vous pouvez
facilement y accéder en cliquant sur la cellule _Réassort réel_.

![../../../../_images/mps_4.png](../../../../_images/mps_4.png)

Si vous modifiez manuellement la quantité de _réassort suggéré_ , une petite
croix apparaîtra à gauche de la cellule. Si vous souhaitiez revenir à la
valeur calculée automatiquement par Odoo, cliquez simplement sur la croix.

## Signification de la couleur de la cellule

Les cellules, qui font partie de la ligne de _réassort suggéré_ , peuvent
prendre différentes couleurs en fonction de la situation :

  * **Vert** : quantité de produits qui devraient être réapprovisionnés pour atteindre le stock de sécurité prévu en tenant compte de la demande prévue et de la prévision de la demande indirecte.

  * **Gris** : l’ordre de réassort a déjà été généré et sa quantité correspond toujours aux données actuelles.

  * **Rouge** : l’ordre de réassort a déjà été généré et sa quantité était trop élevée par rapport aux données actuelles.

  * **Orange** : l’ordre de réassort a déjà été généré et sa quantité était trop faible par rapport aux données actuelles.

La ligne de _stock prévu_ peut également contenir des cellules rouges, ce qui
signifie que le stock sera négatif au cours de la période concernée.

### Que faire si j’ai sous-estimé la demande ?

Vous pouvez toujours augmenter la prévision de la demande. Cela aura un impact
sur la quantité à réapprovisionner. La cellule devient orange et vous pourrez
lancer un nouveau réassort.

### Que faire si j’ai surestimé la demande ?

Vous pouvez diminuer la prévision de la demande. La cellule devient rouge pour
vous informer que vous avez commandé plus que prévu. Si pouvez encore le
faire, vous pouvez annuler manuellement une demande de prix ou un ordre de
fabrication.

### Que faire si j’ai ajouté par erreur un produit au PDP ?

Vous pouvez facilement supprimer un produit du PDP en cliquant sur l’icône de
la petite poubelle à côté de son nom.

