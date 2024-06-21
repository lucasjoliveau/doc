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

Konvergo ERP prend en charge notamment les formats suivants :

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
<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="../../fiscal_localizations#fiscal-localizations-packages"><span class="std std-ref">Packages de localisation fiscale</span></a></p>
</div>

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Journaux ‣ Factures clients ‣
Paramètres avancés ‣ Facturation électronique et activez les formats dont vous
avez besoin pour ce journal.

![Sélectionnez le format EDI dont vous avez
besoin](../../../../_images/formats.png)

Lorsqu’un format de facturation électronique est activé, des documents XML
sont générés lorsque l’on clique sur **Confirmer** dans des documents tels que
des factures, des avoirs, etc. Ces documents sont soit visibles dans la
section des pièces jointes, soit intégrés dans le PDF.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><ul>
<li><p>Pour E-FFF, le fichier xml n’apparaît qu’après avoir généré le PDF (le bouton <b>Imprimer</b> ou <b>Envoyer &amp; Imprimer</b>), puisque le PDF doit être incorporé dans le xml.</p></li>
<li><p>Chaque PDF généré à partir d’Konvergo ERP contient un fichier XML <b>Factur-X</b> (à des fins d’interopérabilité). Pour les entreprises françaises et allemandes, l’option <b>Factur-X (PDF/A-3)</b> permet en outre d’effectuer des contrôles de validation sur la facture et de générer un fichier de conformité PDF/A-3, demandé par des plateformes comme Chorus Pro.</p></li>
<li><p>Les formats disponibles dépendent du pays sélectionné dans les <b>Informations générales</b> de votre entreprise.</p></li>
<li><p>Konvergo ERP prend en charge le format <b>Peppol BIS Billing 3.0</b> qui peut être utilisé via les points d’accès existants.</p></li>
</ul>
</div>

  *[EDI]: échange de données informatisé

