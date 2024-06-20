# Pérou

## Introduction

La localisation péruvienne a été améliorée et étendue. Les modules suivants
sont disponibles dans cette version :

  * **l10n_pe** : Ajoute des fonctionnalités comptables pour la localisation péruvienne, qui représentent la configuration minimale requise pour qu’une entreprise puisse fonctionner au Pérou conformément aux réglementations et aux directives de la SUNAT. Les éléments principaux inclus dans ce module sont le plan comptable, les taxes et les types de documents.

  * **l10n_pe_edi** : Comprend toutes les exigences techniques et fonctionnelles pour générer et valider des factures électroniques, conformément aux spécifications de la SUNAT pour créer et traiter des documents électroniques valides. Pour plus de détails techniques, vous pouvez consulter les [spécifications EDI de la SUNAT](https://cpe.sunat.gob.pe/node/88/), qui suit les nouveaux changements et les mises à jour. Les fonctionnalités de ce module sont basées sur les résolutions publiées dans la [législation de la SUNAT](https://www.sunat.gob.pe/legislacion/general/index.html/).

Pour plus d'infos

  * [App Tour - Localización de Peru](https://youtu.be/Ic3mGovkf8Y)

  * [Tutoriel intelligent - Localización de Peru](https://www.odoo.com/slides/smart-tutorial-localizacion-de-peru-133)

## Configuration

### Installer les modules de la localisation péruvienne

Allez aux _Apps_ et recherchez Pérou. Cliquez ensuite sur installer dans la
carte du module EDI pour le Pérou. Ce module a une dépendance avec _Pérou -
Comptabilité_. Si ce dernier module n’est pas installé, Odoo l’installe
automatiquement avec EDI.

![Le filtre "Module" lit "Pérou"](../../../_images/peru-modules.png)

Note

Lorsque vous installez une base de données à partir de zéro en sélectionnant
le Pérou comme pays, Odoo installe automatiquement le module de base : Pérou -
Comptabilité.

#### Configurer votre société

En plus des informations de base de la Société, vous devez configurer le Pérou
comme Pays pour que la facturation électronique fonctionne correctement. Le
champ **Code de type d’adresse** représente le code d’établissement assigné
par la SUNAT lorsque les sociétés enregistrent leur RUC (numéro
d’enregistrement de contribuable unique) :

![Données de société pour le Pérou, y compris le RUC et le code de type
d'adresse](../../../_images/peru-company.png)

Astuce

Si le code de type d’adresse est inconnu, vous devez le configurer sur la
valeur par défaut : 0000. Attention, si une valeur incorrecte est saisie, la
validation de la facturation électronique risque d’entraîner des erreurs.

Note

Le NIF doit être défini selon le format RUC.

#### Plan comptable

Le plan comptable est installé par défaut puisqu’il fait partie de l’ensemble
des données incluses dans le module de localisation. Les comptes sont mappés
automatiquement dans :

  * Taxes

  * Compte fournisseur par défaut.

  * Compte client par défaut

Le plan comptable pour le Pérou est basé sur la version la plus récente du
PCGE, qui est regroupé en plusieurs catégories et est compatible avec la
comptabilité NIIF.

### Paramètres de la comptabilité

Une fois que vous avez installé les modules et configuré les informations de
base de votre société, vous devez configurer les éléments requis pour la
facturation électronique. Allez à Comptabilité ‣ Paramètres ‣ Localisation
péruvienne.

#### Concepts de base

Voici quelques termes qui sont essentiels sur la localisation péruvienne :

  * **EDI** : Échange de données informatisé, qui désigne ici la facture électronique.

  * **SUNAT** : l’organisation qui applique les douanes et la fiscalité au Pérou.

  * **OSE** : Opérateur de services électroniques, [définition OSE SUNAT](https://cpe.sunat.gob.pe/aliados/ose#:~:text=El%20Operador%20de%20Servicios%20Electr%C3%B3nicos%20\(OSE\)%20es%20qui%C3%A9n%20se%20encarga,otro%20documento%20que%20se%20emita).

  * **CDR** : Certificat de réception (Constancia de Recepción).

  * **Identifiants SOL** : Opératinos en ligne SUNAT. L’utilisateur et le mot de passe sont fournis par la SUNAT et donnent accès aux systèmes des opérations en ligne.

#### Fournisseur de signature

Dans le cadre des exigences relatives à la facturation électronique au Pérou,
votre entreprise doit choisir un fournisseur de signature qui s’occupera du
processus de signature du document et gérera la réponse de validation de la
SUNAT. Odoo propose trois options :

  1. IAP (Achats In-App d’Odoo)

  2. Digiflow

  3. SUNAT

Lisez les sections suivantes pour connaître les détails et les considérations
de chaque option.

##### IAP (Achats In-App d’Odoo)

Il s’agit de l’option suggérée par défaut, étant donné que le certificat
numérique est inclus dans les services.

![Option IAP comme fournisseurs de signature](../../../_images/peru-IAP.png)

###### Qu’est-ce que l’IAP ?

Il s’agit d’un service de signature proposé directement par Odoo, le service
prend en charge le processus suivant :

  1. Fournit le certificat de facture électronique, de sorte que vous n’avez pas besoin d’en acquérir un vous-même.

  2. Envoyer le document à l’OSE, en l’occurrence Digiflow.

  3. Recevoir la validation OSE et le CDR.

###### Comment cela fonctionne-t-il ?

Le service nécessite des crédits pour traiter vos documents électroniques.
Odoo fournit gratuitement 1.000 crédits pour les nouvelles bases de données.
Une fois ces crédits consommés, vous devez acheter un Package de crédits.

Crédits | EUR  
---|---  
1.000 | 22  
5.000 | 110  
10.000 | 220  
20.000 | 440  
  
Les crédits sont consommés par document qui est envoyé à l’OSE.

Important

Si vous avez une erreur de validation et le document doit être envoyé plus
d’une fois, un crédit additionnel vous sera chargé. Il est donc primordial de
vérifier que toutes les informations sont correctes avant d’envoyer votre
document à l’OSE.

###### Que devez-vous faire ?

  * Dans Odoo, une fois que votre contrat d’entreprise est activé et que vous commencez à travailler dans un environnement de production, vous devez acheter des crédits une fois que les 1.000 premiers crédits sont consommés.

  * Puisque Digiflow est l’OSE utilisé dans l’IAP, vous devez l’affilier en tant qu’OSE officiel de votre société sur le site web de la SUNAT. C’est une procédure simple. Pour plus d’informations, veuillez consulter le [guide d’affiliation OSE](https://drive.google.com/file/d/1BkrMTZIiJyi5XI0lGMi3rbMzHddOL1pa/view?usp=sharing).

  * Enregistrez Digiflow en tant que PSE (Fournisseur de services électroniques) autorisé, veuillez consulter le [guide d’affiliation PSE](https://drive.google.com/file/d/1QZoqWvtQERpS0pqp6LcKmw7EBlm9EroU/view?usp=sharing).

##### Digiflow

Cette option peut être utilisée comme alternative. Au lieu d’utiliser les
services IAP, vous pouvez envoyer la validation de vos documents directement à
Digiflow. Dans ce cas, vous devez prendre en compte les points suivants :

  * Acheter votre propre certificat numérique : Pour plus de détails relatifs à la liste des fournisseurs officiels et le processus d’acquisition, veuillez vous référer aux [certificats numériques de la SUNAT](https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/).

  * Signer un accord de service directement avec [Digiflow](https://www.digiflow.pe/).

  * Fournir vos identifiants SOL.

![Digiflow](../../../_images/peru-Digiflow.png)

##### SUNAT

Si votre société souhaite directement signer avec la SUNAT, il est possible de
sélectionner cette option dans votre configuration. Dans ce cas, vous devez
prendre en considération les points suivants : - Faire accepter le processus
de certification de la SUNAT.

  * Acheter votre propre certificat numérique : Pour plus de détails relatifs à la liste des fournisseurs officiels et le processus d’acquisition, veuillez vous référer aux [certificats numériques de la SUNAT](https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/).

  * Fournir vos identifiants SOL.

Important

En cas de connexion directe avec la SUNAT, l’utilisateur SOL doit être définir
avec le RUT et l’identifiant utilisateur de la société. Par exemple :
`20121888549JOHNSMITH`

#### Environnement de test

Odoo fournit un environnement de test qui peut être activé avant que votre
entreprise ne passe en production.

Lorsque vous utilisez l’environnement de test et la signature IAP, vous n’avez
pas besoin d’acheter des crédits de test pour vos transactions, car elles sont
toutes validées par défaut.

Astuce

Par défaut, les bases de données sont configurées pour fonctionner en
production. Assurez-vous d’activer le mode de test si nécessaire.

#### Certificat

Si vous n’utilisez pas Odoo IAP, afin de générer la signature électronique de
la facture, un certificat numérique avec l’extension `.pfx` est requis. Passez
à cette section et chargez votre fichier et votre mot de passe.

![Assistant de certificat EDI](../../../_images/peru-Certificate.png)

#### Multi-devises

Le taux de change officiel au Pérou est fourni par la Banque du Pérou. Odoo
peut se connecter directement à ses services et obtenir le taux de change
automatiquement ou manuellement.

![La Banque du Pérou s'affiche dans l'option Service multi-
devises.](../../../_images/peru-multicurrency.png)

Veuillez consulter la section suivante de notre documentation pour obtenir
plus d’informations sur les [multi-
devises](../accounting/get_started/multi_currency.html).

### Configurer les données de base

#### Taxes

Dans le cadre du module de localisation, les taxes sont créées automatiquement
avec leur compte financier associé et la configuration de la facture
électronique.

![Liste des taxes par défaut](../../../_images/peru-taxes.png)

##### Configuration EDI

Dans le cadre de la configuration des taxes, il y a trois nouveaux champs
requis pour la facture électronique. Les taxes créées par défaut comprennent
ces données, mais si vous créez de nouvelles taxes, assurez-vous de remplir
les champs suivants :

![Données EDI des taxes pour le Pérou](../../../_images/peru-taxes-edi.png)

#### Positions fiscales

Deux positions fiscales principales sont incluses par défaut lorsque vous
installez la localisation péruvienne.

**Extranjero - Exportación** : Définissez cette position fiscale sur les
clients pour les transactions d’exportation.

**Pérou local** : Définissez cette position fiscale sur les clients locaux.

#### Types de documents

Dans certains pays d’Amérique latine, dont le Pérou, certaines transactions
comptables telles que les factures clients et les factures fournisseurs sont
classées par types de document, définis par les autorités fiscales
gouvernementales, en l’occurrence la SUNAT.

Chaque type de document se voit attribuer une séquence unique selon le journal
auquel il est affecté. Dans le cadre de la localisation, le type de document
inclut le pays sur lequel le document est applicable et les données sont
créées automatiquement lors de l’installation du module de localisation.

Les informations requises pour les types de documents sont incluses par
défaut, de sorte que l’utilisateur n’a rien à compléter dans cette vue :

![Liste des types de documents](../../../_images/peru-document-type.png)

Avertissement

Les documents actuellement pris en charge sur les factures clients sont :
Facture, Boleta, Note de débit et Avoir.

#### Journaux

Lors de la création des journaux de vente, les informations suivantes doivent
être complétées, en plus des champs standards sur les journaux :

##### Utiliser les documents

Ce champ est utilisé pour définir si le journal utilise des types de
documents. Il ne s’applique qu’aux journaux de vente et d’achat, qui peuvent
être liés aux différents types de documents disponibles au Pérou. Par défaut,
tous les journaux de vente créés utilisent des documents.

##### Échange de données informatisé

Cette section indique quel flux de travail EDI est utilisé dans la facture.
Pour le Pérou, vous devez sélectionner « Peru UBL 2.1 ».

![Champ EDI journal](../../../_images/peru-journal-edi.png)

Avertissement

Par défaut, la valeur Factur-X (FR) s’affiche toujours. Assurez-vous de la
décocher manuellement.

#### Partenaire

##### Type d’identification et TVA

Dans le cadre de la localisation péruvienne, les types d’identification
définis par la SUNAT sont désormais disponibles sur le formulaire partenaire.
Ces informations sont essentielles pour la plupart des transactions, tant pour
la société expéditrice que pour le client. Assurez-vous de remplir ces
informations sur vos enregistrements.

![Type d'identification du partenaire](../../../_images/peru-id-type.png)

#### Produit

En plus des informations de base de vos produits, pour la localisation
péruvienne, le Code UNSPC sur le produit est une valeur obligatoire à
configurer.

![Code UNSPC sur les produits](../../../_images/peru-unspc-code.png)

## Utilisation et tests

### Facture client

#### Éléments EDI

Une fois que vous avez configuré vos données de base, les factures peuvent
être créées à partir de votre commande ou manuellement. En plus des
informations de base décrites sur [notre page concernant le processus de
facturation](../accounting/customer_invoices/overview.html), quelques champs
sont requis dans le cadre de l’EDI pour le Pérou :

  * **Type de document** : La valeur par défaut est « Factura Electrónica », mais vous pouvez modifier manuellement le type de document si nécessaire et sélectionnez Boleta par exemple.

![Champ type de document sur une facture](../../../_images/peru-invoice-
document-type.png)

  * **Type d’opération** : Cette valeur est obligatoire pour la facture électronique et indique le type de transaction. La valeur par défaut est « Internal Sale », mais une autre valeur peut être sélectionnée manuellement si nécessaire, par exemple Exportation de marchandises.

![Champ de type d'opération sur une facture](../../../_images/peru-operation-
type.png)

  * **Motif de l’affectation EDI** : Dans les lignes de la facture, en plus de la taxe, il y a un champ « Motif de l’affectation EDI » qui détermine le champ d’application de la taxe sur la base de la liste de la SUNAT qui est affichée. Toutes les taxes chargées par défaut sont associées à un motif d’affectation EDI par défaut. Si nécessaire, vous pouvez en sélectionner un autre manuellement lors de la création de la facture.

![Motif de l'affectation de la taxe dans la ligne de
facture](../../../_images/peru-tax-affectation-reason.png)

#### Validation des factures

Une fois que vous avez vérifié que toutes les informations de votre facture
sont correctes, vous pouvez procéder à sa validation. Cette action enregistre
le transfert de compte et déclenche le flux de facturation électronique pour
l’envoyer à l’OSE et à la SUNAT. Le message suivant s’affiche en haut de la
facture :

![Envoi de la facture EDI en bleu](../../../_images/peru-posted-invoice.png)

Asynchrone signifie que le document n’est pas envoyé automatiquement après la
comptabilisation de la facture.

##### Statut de la facture électronique

**To be Sent** : Indicates the document is ready to be sent to the OSE, this
can be done either automatically by Odoo with a _cron_ that runs every hour,
or the user can send it immediately by clicking on the button “Sent now”.

![Envoyer l'EDI manuellement](../../../_images/peru-sent-manual.png)

**Envoyé** : Indique que le document a été envoyé à l’OSE et a été validé avec
succès. Dans le cadre de la validation, un fichier ZIP est téléchargé et un
message est enregistré dans le chatter indiquant la validation correcte par le
gouvernement.

![Message sur le chatter après la validation de la
facture](../../../_images/peru-invoice-sent.png)

En cas d’erreur de validation, le statut de la facture électronique reste sur
« À envoyer » afin que les corrections puissent être apportées et que la
facture puisse être envoyée à nouveau.

Avertissement

Un crédit est consommé chaque fois que vous envoyez un document pour
validation, c’est-à-dire que si une erreur est détectée sur une facture et que
vous l’envoyez une nouvelle fois, deux crédits sont consommés au total.

#### Erreurs courantes

Il y a de multiples raisons derrière un rejet de l’OSE ou de la SUNAT. Lorsque
cela se produit, Odoo envoie un message en haut de la facture indiquant les
détails de l’erreur et, dans les cas les plus courants, un conseil pour
résoudre le problème.

Si une erreur de validation est reçue, vous avez deux possibilités :

  * Si l’erreur est liée aux données de base du partenaire, du client ou des taxes, vous pouvez simplement appliquer la modification sur l’enregistrement (par exemple, le type d’identification du client) et une fois que c’est fait, cliquez sur le bouton Réessayer.

  * Si l’erreur est liée à des données enregistrées sur la facture directement (type d’opération, données manquantes sur les lignes de la facture), la bonne solution consiste à remettre la facture en brouillon, à appliquer les modifications, puis à envoyer à nouveau la facture à la SUNAT pour une nouvelle validation.

![Liste des erreurs courantes sur les factures](../../../_images/peru-
errors.png)

Pour plus de détails, veuillez consulter les [Erreurs courantes dans
SUNAT](https://www.nubefact.com/codigos-error-sunat/).

#### Rapport PDF de la facture

Après que la facture est acceptée et validée par la SUNAT, le rapport PDF de
la facture peut être imprimé. Le rapport inclut un code QR, indiquant que la
facture est un document fiscal valide.

![Rapport PDF de la facture](../../../_images/peru-PDF.png)

#### Crédits IAP

L’IAP électronique d’Odoo offre 1.000 crédits gratuitement. Une fois que ces
crédits sont consommés dans votre base de données de production, votre société
doit acheter de nouveaux crédits afin de traiter vos transactions.

Lorsque vous n’avez plus de crédits, un libellé rouge s’affiche en haut de la
facture indiquant que des crédits supplémentaires sont requis. Vous pouvez
facilement les acheter en cliquant sur le lien fourni dans le message.

![Acheter des crédits dans l'IAP](../../../_images/peru-credits-IAP.png)

Les services d’IAP comprennent des packages dont les prix varient en fonction
du nombre de crédits. La liste des prix dans l’IAP s’exprime toujours en EUR.

#### Cas d’utilisation particuliers

##### Processus d’annulation

Certains scénarios nécessitent une annulation de facture, par exemple
lorsqu’une facture a été créée par erreur. Si la facture a déjà été envoyée à
et validée par la SUNAT, la bonne façon de procéder est de cliquer sur le
bouton Demande d’annulation :

![Bouton de demande d'annulation sur une facture](../../../_images/peru-
cancellation.png)

Afin d’annuler une facture, indiquez un motif d’annulation.

###### Statut de la facture électronique

**À annuler** : Indique que la demande d’annulation est prête à être envoyée à
l’OSE. Cela peut être fait automatiquement par Odoo avec un _cron_ qui
s’exécute toutes les heures ou l’utilisateur peut l’envoyer immédiatement en
cliquant sur le bouton « Envoyer maintenant ». Une fois qu’elle est envoyée,
un ticket d’annulation est créé et le message suivant et le fichier CDR sont
enregistrés dans le chatter :

![CDR d'annulation envoyé par la SUNAT](../../../_images/peru-cancellation-
cdr.png)

**Annulé** : Indique que la demande d’annulation a été envoyée à l’OSE et a
été validée avec succès. Dans le cadre de la validation, un fichier ZIP est
téléchargé et un message est enregistré dans le chatter indiquant la
validation correcte par le gouvernement.

![Facture après annulation](../../../_images/peru-cancelled.png)

Avertissement

Un crédit est consommé par demande d’annulation.

##### Processus d’annulation

Lors de la création de factures d’exportation, tenez compte des considérations
suivantes :

  * Le type d’identification de votre client doit être ID Étranger.

  * Le type d’opération de votre facture doit être Exportation.

  * Les taxes incluses dans les lignes de facture doivent être des taxes EXP.

![Données principales des factures d'exportation](../../../_images/peru-exp-
invoice.png)

##### Acomptes

  1. Créez la facture d’acompte et appliquez le paiement correspondant.

  2. Créez la facture finale sans tenir compte de l’acompte.

  3. Créez un avoir pour la facture finale avec le montant de l’acompte.

  4. Rapprochez l’avoir avec la facture finale.

  5. Le solde de la facture finale doit être payé par une transaction de paiement normale.

##### Factures de rabais

Lorsque vous créez des factures soumises à des rabais, tenez compte des
considérations suivantes :

  1. Tous les produits inclus dans la facture doivent avoir ces champs configurés :

![Champs de rabais sur les produits](../../../_images/peru-detraction.png)

  2. Le type d’opération de votre facture doit être `1001`

![Code de rabais sur les factures.](../../../_images/peru-detraction-
invoice.png)

### Avoirs

Lorsqu’une correction ou un remboursement est nécessaire sur une facture
validée, un avoir doit être généré. Il suffit de cliquer sur le bouton «
Ajouter un avoir ». Dans le cadre de la localisation péruvienne, vous devez
prouver un Motif de crédit en sélectionnant l’une des options de la liste.

![Ajouter un avoir à partir de la facture](../../../_images/peru-credit-
note.png)

Astuce

Lors de la création de votre premier avoir, sélectionnez la Méthode de crédit
: Remboursement partiel, ce qui vous permet de définir la séquence de l’avoir.

Par défaut, l’avoir est défini dans le type de document :

![Type de document Avoir](../../../_images/peru-credit-note-document.png)

Pour terminer le flux de travail, suivez les instructions sur [notre page sur
les avoirs](../accounting/customer_invoices/credit_notes.html).

Note

Le flux de travail EDI pour les avoirs fonctionne de la même manière que pour
les factures.

### Notes de débit

Dans le cadre de la localisation péruvienne, en plus de créer des avoirs à
partir d’un document existant, vous pouvez également créer des Notes de débit.
Cliquez simplement sur le bouton « Ajouter une note de débit ».

Par défaut, la Note de débit est définie dans le type de document.

### Electronic delivery guide 2.0

The _Guía de Remisión Electrónica_ (GRE) is an electronic document generated
by the shipper to support the transportation or transfer of goods from one
place to another, such as a warehouse or establishment. In Odoo, there are
several configuration steps needed before you can successfully use this
feature.

The use of the _guía de remisión electrónica_ electronic document is mandatory
and required by SUNAT for taxpayers who need to transfer their products,
except those under the _Single Simplified Regime_ (régimen único simplificado
or RUS).

#### Delivery guide types

##### Expéditeur

The _Sender_ delivery guide type is issued when a sale is made, a service is
rendered (including processing), goods are assigned for use, or goods are
transferred between premises of the same company and others.

This delivery guide is issued by the owner of the goods (i.e., the sender) at
the beginning of the shipment. The sender delivery guide is supported in Odoo.

Pour plus d'infos

[SUNAT guía de remisión](https://www.gob.pe/7899-guia-de-remision)

##### Transporteur

The _Carrier_ delivery guide type justifies the transportation service the
driver (or carrier) performs.

This delivery guide is issued by the carrier and must be issued to each
shipper when the shipment goes through public transport.

Important

The carrier delivery guide is **not** supported in Odoo.

Pour plus d'infos

[SUNAT guía de remisión transportista](https://tefacturo.pe/blog/sunat/guia-
de-remision-electronica/guia-de-remision-transportista/)

#### Transportation types

##### Privée

The _Private_ transportation type option is used when the owner transfers
goods using their own vehicles. In this case, a sender’s delivery guide must
be issued.

##### Public

The _Public_ transportation type option is used when an external carrier moves
the goods. In this case, two delivery guides must be issued: the sender’s
delivery guide and the carrier’s delivery guide.

#### Direct submission to SUNAT

The creation of the GRE delivery guide in Odoo **must** be sent directly to
the SUNAT, regardless of the electronic document provider: IAP, Digiflow, or
SUNAT.

#### Required information

Version 2.0 of the electronic delivery guide requires additional information
on the general configuration, vehicles, contacts, and products. In the general
configuration, it is necessary to add new credentials that you can retrieve
from the SUNAT portal.

#### Cancellations

**Both** the sender and the carrier can cancel the electronic waybill as long
as the following conditions are met:

  * The shipment has not been initiated.

  * If the shipment has been initiated, the receiver **must** be changed before reaching the final destination.

Important

The SUNAT no longer uses the term « Anula », but now uses the term « Dar de
baja » for cancellations.

#### Mode test

The SUNAT does not support a test environment. This means that any delivery
guides that were generated by mistake **will** be sent to the SUNAT.

If, by mistake, the waybill was created in this environment, it is necessary
to delete it from the SUNAT portal.

#### Configuration

Important

  * Electronic sender’s GRE is currently the only supported type of waybill in Odoo.

  * The delivery guide is dependent on the Odoo _Inventory_ app, the l10n_pe_edi and l10n_pe modules.

  * A second user **must** be added for the creation of electronic documents.

After following the steps to configure the electronic invoicing and the master
data, [install](../../general/apps_modules.html#general-install) the Peruvian
- Electronic Delivery Note 2.0 module (`l10n_pe_edi_stock_20`).

Next, you need to retrieve the _client ID_ and _client secret_ from SUNAT. To
do so, follow the [manual de servicios web plataforma nueva
GRE](https://cpe.sunat.gob.pe/sites/default/files/inline-
files/Manual_Servicios_GRE.pdf).

Note

In the SUNAT portal, it is important to have the correct access rights
enabled, as they may differ from the user set for electronic invoicing.

These credentials should be used to configure the delivery guide general
settings from Accounting ‣ Configuration ‣ Settings ‣ Peruvian Electronic
Invoicing.

![Example for the SUNAT Delivery Guide API section
configuration.](../../../_images/gre-fields-example.png)

Note

It is required to follow the format `RUC + UsuarioSol` (e.g.,
`20557912879SOLUSER`) for the Guide SOL User field, depending on the user
selected when generating the GRE API credentials in the SUNAT portal.

##### Opérateur

The _operator_ is the vehicle’s driver in cases where the delivery guide is
through _private_ transport.

To create a new operator, navigate to Contacts ‣ Create and fill out the
contact information.

First, select Individual as the Company Type. Then, add the Operator License
in the Accounting tab of the contact form.

For the customer address, make sure the following fields are complete:

  * District

  * Tax ID (DNI/RUC)

  * Tax ID Number

![Individual type operator configurations in the Contact
form.](../../../_images/operator-configuration.png)

##### Transporteur

The _carrier_ is used when the delivery guide is through _public_ transport.

To create a new carrier, navigate to Contacts ‣ Create and fill out the
contact information.

First, select Company as the Company Type. Then, add the MTC Registration
Number, Authorization Issuing Entity, and the Authorization Number.

For the company address, make sure the following fields are complete:

  * District

  * Tax ID (DNI/RUC)

  * Tax ID Number

![Company type operator configurations in the Contact
form.](../../../_images/company-operator-configuration.png)

##### Véhicules

To configure the available vehicles, navigate to Inventory ‣ Configuration ‣
Vehicles and fill in the vehicle form with the information needed for the
vehicle:

  * Vehicle Name

  * License Plate

  * Is M1 or L?

  * Special Authorization Issuing Entity

  * Authorization Number

  * Default Operator

  * Company

Important

It is important to check the Is M1 or L? checkbox if the vehicle has fewer
than four wheels or fewer than eight seats.

![Vehicle not selected as an M1 or L type with extra fields
shown.](../../../_images/vehicle-not-m1-or-l-pe.png)

##### Produits

To configure the available products, navigate to Inventory ‣ Products and open
the product to be configured.

Make sure that the applicable information in the product form is fully
configured. The Partida Arancelaria (Tariff Item) field needs to be completed.

#### Generating a GRE

Once the delivery from inventory is created during the sales workflow, make
sure you complete the GRE fields on the top-right section of the transfer form
for the fields:

  * Transport Type

  * Reason for Transfer

  * Departure start date

It is also required to complete the Vehicle and Operator fields under the Guia
de Remision PE tab.

The delivery transfer has to be marked as _Done_ for the Generar Guia de
Remision button to appear on the left menu of the transfer form.

![Generar Guia de Remision button on a transfer form in the Done
stage.](../../../_images/generate-gre-transferview.png)

Once the transfer form is correctly validated by SUNAT, the generated XML file
becomes available in the chatter. You can now print the delivery slip that
shows the transfer details and the QR code validated by SUNAT.

![Transfer details and QR code on generated delivery
slip.](../../../_images/gre-delivery-slip.png)

#### Erreurs courantes

  * `Diferente prefijo para productos (T001 en algunos, T002 en otros)`

At the moment, Odoo does not support the automation of prefixes for products.
This can be done manually for each product output. This can also be done for
non-storable products. However, keep in mind that there will be no
traceability.

  * `2325 - GrossWeightMeasure - El dato no cumple con el formato establecido "Hace falta el campo" "Peso"" en el producto`

This error occurs when the weight on the product is set as `0.00`. To fix
this, you need to cancel the waybill and recreate it. Make sure that you fix
the weight on the product before creating the new waybill, or it will result
in the same error.

  * `JSONDecodeError: Expecting value: line 1 column 1 (char 0) when creating a Delivery Guide`

This error is typically generated due to SOL user issues. Verify the user’s
connection with the SUNAT; the SOL user must be established with the company
RUT + user ID. For example `2012188549JOHNSMITH`.

  * `El número de documento relacionado al traslado de mercancía no cumple con el formato establecido: error: documento relacionado`

The _Related Document Type_ and _Related Document Number_ fields only apply to
invoices and receipts.

  * `400 Client error: Bad Request for URL`

This error is not solvable from Odoo; it is advised you reach out to the SUNAT
and verify the user. It may be necessary to create a new user.

  * `Invalid content was found starting with element 'cac:BuyerCustomerParty'`

This error occurs when the transfer reason is set as _other_. Please select
another option. Following to the official documentation of the SUNAT’s waybill
guide, the transfer reasons _03 (sale with shipment to third party)_ or _12
(others)_ does not work in Odoo, since you should not have an empty or blank
customer.

  * `Duda cliente: consumo de créditos IAP al usar GRE 2.0`

For live clients using IAP, no credit is consumed (in theory) because it does
not go through the OSE, i.e., these documents are directly sent to the SUNAT.

  * `Errores con formato credenciales GRE 2.0 (traceback error)`

Odoo currently throws an error with a traceback instead of a message that the
credentials are not correctly configured in the database. If this occurs on
your database, please verify your credentials.

  *[PCGE]: Plan Contable General Empresarial
  *[SUNAT]: Superintendencia Nacional de Aduanas y de Administración Tributaria
  *[GRE]: Guía de Remisión Electrónica

