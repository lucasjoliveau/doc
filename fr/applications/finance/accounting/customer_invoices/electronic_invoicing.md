# Facturation électronique (EDI)

L’EDI, ou échange de données informatisé, est la communication inter-
entreprise de documents commerciaux, tels que les bons de commande et les
factures, dans un format standard. L’envoi de documents selon une norme EDI
garantit que l’appareil qui reçoit le message peut interpréter correctement
l’information. Différents formats de fichiers EDI existent et sont disponibles
en fonction du pays de votre société.

La fonctionnalité EDI permet d’automatiser l’administration entre entreprises
et peut également être exigée par certains gouvernements à des fins de
contrôle fiscal ou pour faciliter la gestion.

La facturation électronique de vos documents tels que les factures clients,
les avoirs ou les factures fournisseurs est l’une des applications de l’EDI.

Odoo prend en charge notamment les formats suivants :

Nom du format | Applicabilité  
---|---  
Factur-X (PDF/A-3) | Pour les entreprises françaises et allemandes  
Peppol BIS Billing 3.0 (UBL) | Pour les entreprises dont les pays figurent sur la [liste EAS](https://docs.peppol.eu/poacc/billing/3.0/codelist/eas/)  
E-FFF | Pour les entreprises belges  
XRechnung (UBL) | Pour les entreprises allemandes  
Fattura PA (IT) | Pour les entreprises italiennes  
CFDI (4.0) | Pour les entreprises mexicaines  
Peru UBL 2.1 | Pour les entreprises péruviennes  
SII IVA Llevanza de libros registro (ES) | Pour les entreprises espagnoles  
UBL 2.1 (Columbia) | Pour les entreprises colombiennes  
Egyptian Tax Authority | Pour les entreprises égyptiennes  
E-Invoice (IN) | Pour les entreprises indiennes  
NLCIUS (Netherlands) | Pour les entreprises néerlandaises  
EHF 3.0 | Pour les entreprises norvégiennes  
SG BIS Billing 3.0 | Pour les entreprises singapouriennes  
A-NZ BIS Billing 3.0 | Pour les entreprises australiennes et néo-zélandaises  
  
Pour plus d'infos

[Packages de localisation fiscale](../../fiscal_localizations.html#fiscal-
localizations-packages)

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Journaux ‣ Factures clients ‣
Paramètres avancés ‣ Facturation électronique et activez les formats dont vous
avez besoin pour ce journal.

![Sélectionnez le format EDI dont vous avez
besoin](../../../../_images/formats.png)

Lorsqu’un format de facturation électronique est activé, des documents XML
sont générés lorsque l’on clique sur Confirmer dans des documents tels que des
factures, des avoirs, etc. Ces documents sont soit visibles dans la section
des pièces jointes, soit intégrés dans le PDF.

Note

  * Pour E-FFF, le fichier xml n’apparaît qu’après avoir généré le PDF (le bouton Imprimer ou Envoyer & Imprimer), puisque le PDF doit être incorporé dans le xml.

  * Chaque PDF généré à partir d’Odoo contient un fichier XML Factur-X (à des fins d’interopérabilité). Pour les entreprises françaises et allemandes, l’option Factur-X (PDF/A-3) permet en outre d’effectuer des contrôles de validation sur la facture et de générer un fichier de conformité PDF/A-3, demandé par des plateformes comme Chorus Pro.

  * Les formats disponibles dépendent du pays sélectionné dans les Informations générales de votre entreprise.

  * Odoo prend en charge le format **Peppol BIS Billing 3.0** qui peut être utilisé via les points d’accès existants.

  *[EDI]: échange de données informatisé

