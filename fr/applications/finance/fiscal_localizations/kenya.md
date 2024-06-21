# Kenya

## Configuration

[Installez](../../general/apps_modules#general-install) les modules
suivants pour obtenir toutes les fonctionnalités de la localisation kenyane :

Nom | Nom technique | Description  
---|---|---  
**Kenya - Comptabilité** | `l10n_ke` | L’installation de ce module vous donne accès à la liste des comptes utilisés dans les GAAP locaux et la liste des taxes courantes (TVA, etc.).  
**Kenya - Rapports comptables** | `l10n_ke_reports` | L’installation de ce module vous donne accès aux rapports comptables améliorés pour le Kenya, tels que le compte de résultat et le bilan.  
  
Vous devez également installer le package **Intégration de l’appareil Tremol
pour l’EDI au Kenya** pour pouvoir déclarer vos taxes à la **Kenya Revenue
Authority (KRA)** en utilisant l’Unité de contrôle G03 Tremol :

Nom | Nom technique | Description  
---|---|---  
**Intégration de l’appareil Tremol pour l’EDI au Kenya** | `l10n_ke_edi_tremol` | L’installation de ce module s’intègre à l’unité de contrôle kenyane G03 tremol pour déclarer les taxes à la KRA par le biais de TIMS.  
![Les trois modules du package de localisation fiscale kenyane dans
Konvergo ERP](../../../_images/modules.png)

## Intégration TIMS au Kenya

La Kenya Revenue Authority (KRA) a décidé de digitaliser le recouvrement des
taxes via le **Tax Invoice Management System (TIMS)**. À partir du 1er
décembre 2022, toutes les personnes assujetties à la TVA doivent se conformer
au TIMS. L’objectif est de réduire la fraude à la TVA, d’augmenter les
recettes fiscales et d’améliorer la conformité à la TVA grâce à la
normalisation, la validation et la transmission des factures à la KRA en temps
réel ou presque.

Tous les contribuables assujettis à la TVA doivent utiliser un **registre
fiscal conforme**. Konvergo ERP a décidé de développer l’intégration de l”**Unité de
contrôle G03 Tremol (type C)** , qui peut s’exécuter localement via USB. Ce
dispositif valide les factures pour assurer que les documents financiers
répondent aux nouvelles réglementation et envoie les factures fiscales
validées directement à la KRA. Vous devez installer un serveur proxy qui
fournit une passerelle entre les utilisateurs et l’internet.

### Installer le serveur proxy sur un appareil Windows

Allez à [odoo.com/download](https://www.odoo.com/page/download), complétez les
informations requises et cliquez sur **Télécharger**.

![Installez le serveur proxy sur un appareil
Windows](../../../_images/download.png)

Une fois qu’il est chargé sur votre ordinateur, un assistant s’ouvre. Vous
devez lire et accepter les conditions générales. Sur la page suivante,
sélectionnez le **type d’installation : Konvergo ERP IoT**. Puis cliquez sur
**Suivant** et sur **Installer**. Une fois l’installation terminée, cliquez
sur **Suivant**. Cochez la case **Lancer Konvergo ERP** pour être redirigé
automatiquement vers Konvergo ERP, puis cliquez sur **Terminer**.

A new page opens, confirming your [IoT
Box](../../general/iot/config/connect) is up and running. Connect your
physical device **Tremol G03 Control Unit (type C)** to your laptop via USB.
In the **IoT Device** section, check that your Tremol G03 Control Unit (type
C) appears, confirming the connection between the device and your computer.

![Votre IoT box est fonctionnelle](../../../_images/iot-box.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Si le dispositif n’est pas détecté, essayez de le rebrancher ou cliquez sur le bouton <b>Relancer</b> dans le coin supérieur droit.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../general/iot/config/connect">Connect an IoT box to your database</a></p>
</div>

### Envoyer les données à la KRA via l’Unité de contrôle G03 Tremol

Comme prérequis, vérifiez que les modules comptables kenyans sont installés
sur votre base de données. Allez ensuite à Comptabilité ‣ Configuration ‣
Paramètres ‣ section Intégration TIMS au Kenya et vérifiez que l”**Adresse
proxy de l’unité de contrôle** correspond à l’adresse de l’IoT box.

Pour envoyer les données à la KRA, créez une nouvelle facture en allant au
tableau de bord Comptabilité ‣ Carte de facturation client en cliquant sur
**Nouvelle facture**. Lors de la confirmation d’une nouvelle facture, le
bouton **Envoyer la facture au dispositif fiscal** s’affiche. Le fait de
cliquer dessus envoie les détails de la facture au dispositif et du dispositif
au gouvernement. Le champ **Numéro de facture CU** est désormais complété dans
votre facture, confirmant l’envoi des informations.

L’onglet **Dispositif fiscal G03 Tremol** contient des champs qui sont
complétés automatiquement une fois que la facture est envoyée au gouvernement
:

  * **Code QR CU** : Url du portail KRA qui reflète un code QR.

  * **Numéro de série CU** : reflète le numéro de série de l’appareil.

  * **Date et heure de signature CU** : La date et l’heure auxquelles la facture a été envoyée à la KRA.

Si vous cliquez sur **Envoyer et imprimer** , un .pdf de la facture est
généré. Les **informations du dispositif fiscal kenyan** sont mentionnées sur
le document.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Pour vérifier que la KRA a reçu les informations relatives à la facture, notez le <b>Numéro de facture CU</b> et saisissez-le dans la section <b>Vérificateur de numéro de facture</b> sur le <a href="https://itax.kra.go.ke/KRA-Portal">site web de la Kenya Revenue Authority</a>. Cliquez sur <b>Valider</b> et trouvez les détails de la facture.</p>
</div>

