# Indonésie

## Module E-Faktur

Le **Module E-Faktur** est installé par défaut en même temps que le module de
localisation indonésienne. Il vous permet de générer un fichier CSV pour une
facture fiscale ou pour un lot de factures fiscales à télécharger dans
l’application **e-Faktur de l’administration fiscale**.

### Paramètres NPWP/NIK

  * **Votre société**

Cette information est utilisée dans la ligne FAPR dans le format de fichier
effect. Vous devez définir un numéro de TVA sur le partenaire concerné de
votre société Konvergo ERP. À défaut, vous ne pourrez pas créer d’e-Facture à partir
d’une facture.

  * **Vos clients**

Vous devez cocher la case _ID PKP_ afin de générer des e-fakturs pour un
client. Vous pouvez utiliser le champ TVA sur la fiche du client pour
configurer le numéro NPWP nécessaire à la génération du fichier e-Faktur. Si
votre client n’a pas de NPWP, saisissez simplement le NIK dans le même champ
TVA.

![../../../_images/indonesia-partner-nik.png](../../../_images/indonesia-
partner-nik.png)

### Utilisation

#### Générer le numéro de série de la facture fiscale

  1. Allez à Comptabilité ‣ Clients ‣ e-Faktur. Pour pouvoir exporter des factures clients en e-Faktur pour le gouvernement indonésien, vous devez indiquer ici les plages des numéros qui vous ont été attribuées par le gouvernement. Lorsque vous validez une facture, un numéro sera assigné en fonction de ces plages. Ensuite, vous pouvez filtrer les factures encore à exporter dans la liste des factures et cliquez sur _Action_ , et sur _Télécharger e-Faktur_.

  2. Après avoir reçu de nouveaux numéros de série de l’administration fiscale indonésienne, vous pouvez créer un ensemble de numéros de série de factures fiscales à partir de cette vue de liste. Vous n’avez qu’à préciser le Min et le Max de chaque groupe de numéros de série et Konvergo ERP formatera automatiquement le numéro en un numéro à 13 chiffres, comme il est requis par l’administration fiscale indonésienne.

  3. Il y a un compteur pour vous informer du nombre de numéros inutilisés restant dans ce groupe.

![../../../_images/indonesia-sn-count.png](../../../_images/indonesia-sn-
count.png)

#### Générer e-faktur csv pour une seule facture ou un lot de factures

  1. Créez une facture à partir de Comptabilité ‣ Clients ‣ Factures. Si le pays du client de la facture est l’Indonésie et le client est défini comme _ID PKP_ , Konvergo ERP vous permettra de créer une e-Faktur.

  2. Définissez un Kode Transaksi pour l’e-Faktur. Il y a des contraintes liées au Kode Transaksi et le type de TVA appliqué aux lignes de facture.

![../../../_images/indonesia-kode-transaksi.png](../../../_images/indonesia-
kode-transaksi.png)

  3. Konvergo ERP choisira automatiquement le prochain numéro de série disponible dans le tableau des numéros e-Faktur (voir la section ci-dessus) et générera le numéro e-faktur en combinant le Kode Transaksi et le numéro de série. Vous pouvez voir cela dans la vue du formulaire de facturation sous la page _Informations supplémentaires_ dans la case _Taxe électronique_.

![../../../_images/indonesia-e-faktur-sn.png](../../../_images/indonesia-e-
faktur-sn.png)

  4. Une fois la facture comptabilisée, vous pouvez générer et télécharger l’e-Faktur en cliquant sur _Télécharger e-faktur_ dans le menu _Action_. La case _CSV créé_ sera cochée.

![../../../_images/indonesia-csv-created.png](../../../_images/indonesia-csv-
created.png)

  5. Vous pouvez sélectionner plusieurs factures dans la vue liste et générer un lot d’eFaktur .csv.

#### Kode Transaksi FP (Code de transaction)

Les codes suivants sont disponibles lors de la génération d’une e-Faktur. - 01
Kepada Pihak yang Bukan Pemungut PPN (Customer Biasa) - 02 Kepada Pemungut
Bendaharawan (Dinas Kepemerintahan) - 03 Kepada Pemungut Selain Bendaharawan
(BUMN) - 04 DPP Nilai Lain (PPN 1%) - 06 Penyerahan Lainnya (Turis Asing) - 07
Penyerahan yang PPN-nya Tidak Dipungut (Kawasan Ekonomi Khusus/ Batam) - 08
Penyerahan yang PPN-nya Dibebaskan (Impor Barang Tertentu) - 09 Penyerahan
Aktiva (Pasal 16D UU PPN)

#### Corriger une facture qui a été comptabilisée et téléchargée :
Fonctionnalité Remplacer la facture

  1. Annulez la facture originale erronée dans Konvergo ERP. Par exemple, nous allons changer le Kode Transaksi de 01 à 03 pour INV/2020/0001.

  2. Créez une nouvelle facture et choisissez la facture annulée dans le champ _Remplacer la facture_. Dans ce champ, nous ne pouvons sélectionner que les factures dont le statut est _Annulé_ du même client.

  3. En validant, Konvergo ERP utilisera automatiquement le même numéro de série e-Faktur que la facture annulée et remplacée en remplaçant le troisième chiffre du numéro de série original par _1_ (comme demandé pour charger une facture de remplacement dans l’app e-Faktur).

![../../../_images/indonesia-replace-invoice.png](../../../_images/indonesia-
replace-invoice.png)

#### Corriger une facture qui a été comptabilisée, mais pas encore téléchargée
: Réinitialiser e-Faktur

  1. Réinitialisez la facture en brouillon et annulez-la.

  2. Cliquez sur le bouton _Réinitialiser e-Faktur_ dans la vue du formulaire de la facture.

  3. Le numéro de série n’est plus attribué et il est possible de réinitialiser la facture en brouillon, de la modifier et de lui attribuer un nouveau numéro de série.

![../../../_images/indonesia-e-faktur-reset.png](../../../_images/indonesia-e-
faktur-reset.png)

