# Signer

**Odoo Sign** allows you to send, sign, and approve documents online, using
electronic signatures.

Une **signature électronique** montre l’accord d’une personne sur le contenu
d’un document. Tout comme une signature manuscrite, la signature électronique
représentant un engagement légal par rapport aux conditions du document signé.

With Sign, you can upload any PDF file and add fields to it. These fields can
be automatically filled in with the user’s details present in your database.

Pour plus d'infos

  * [Odoo Signature : page produit](https://www.odoo.com/app/sign)

  * [Odoo Tutorials: Sign [video]](https://www.odoo.com/slides/sign-61)

## Validité des signatures électroniques

Les documents signés par l’application Signature sont des signatures
électroniques valides dans l’Union européenne et les États-Unis d’Amérique.
Elles répondent également aux exigences relatives aux signatures électroniques
dans la plupart des pays. La validité légale des signatures électroniques
générées par Odoo dépend de la législation de votre pays. Les entreprises qui
font des affaires à l’étranger doivent également prendre en considération la
législation des autres pays relative à la signature électronique.

### Union européenne

Le [Règlement eIDAS](http://data.europa.eu/eli/reg/2014/910/oj) fournit le
cadre des signatures électroniques dans les [27 États membres de l’Union
européenne](https://europa.eu/european-union/about-eu/countries_en). Il
reconnaît trois types de signatures électroniques :

  1. Signatures électroniques simples

  2. Signatures électroniques avancées

  3. Signatures électroniques qualifiées

Odoo génère le premier type, les **signatures électroniques simples** ; ces
signatures sont légalement valides au sein de l’Union européenne, comme le
stipule le Règlement eIDAS.

Les signatures électroniques peuvent ne pas être automatiquement reconnues
comme valides. Il se peut que vous deviez apporter des preuves de la validité
d’une signature. Alors que l’application Signature fournit une signature
électronique simple, certaines preuves sont automatiquement recueillies au
cours du processus de signature, telles que :

  1. Validation par mail et par SMS (si activée)

  2. Preuve d’identité solide via itsme® (disponible en Belgique et aux Pays-Bas)

  3. Journaux d’accès horodatés, IP et géographiquement traçables aux documents et aux signatures associées.

  4. Traçabilité et inaltérabilité des documents (toute altération apportée à un document signé est détectée par Odoo grâce à l’aide de preuves cryptographiques)

### États-Unis d’Amérique

L”[ESIGN Act (Electronic Signatures in Global and National Commerce
Act)](https://www.fdic.gov/regulations/compliance/manual/10/X-3.1.pdf), aux
niveaux interétatique et international, et l”[UETA (Uniform Electronic
Transactions Act)](https://www.uniformlaws.org/committees/community-
home/librarydocuments?communitykey=2c04b76c-2b7d-4399-977e-d5876ba7e034&tab=librarydocuments),
au niveau étatique, fournissent le cadre juridique des signatures
électroniques. Notez que
[l’Illinois](https://www.ilga.gov/legislation/ilcs/ilcs5.asp?ActID=89&) et
[New York](https://its.ny.gov/electronic-signatures-and-records-act-esra)
n’ont pas adopté l’UETA, mais des législations similaires à la place.

Globalement, pour être reconnues comme valides, les signatures électroniques
doivent répondre à cinq critères :

  1. Le signataire doit montrer une **intention claire de signer**. Par exemple, l’utilisation d’une souris pour dessiner une signature peut montrer l’intention. Le signataire doit également avoir la possibilité de se retirer du document électronique.

  2. Le signataire doit d’abord exprimer ou impliquer son **consentement à la conduite des affaires par voie électronique**.

  3. **La signature doit être clairement attribuée**. Dans Odoo, les métadonnées, telles que l’adresse IP du signataire, sont ajoutées à la signature, qui peuvent être utilisées comme preuve.

  4. **La signature doit être associée au document signé** , par exemple, en conservant un enregistrement détaillant la façon dont la signature a été saisie.

  5. Les documents signés électroniquement doivent être **conservés et stockés** par toutes les parties concernées ; par exemple, en fournissant au signataire soit une copie entièrement signée, soit la possibilité de télécharger une copie.

Important

Les informations susmentionnées n’ont aucune valeur juridique ; elles ne sont
fournies qu’à titre d’information générale. Les législations régissant les
signatures électroniques évoluant rapidement, nous ne pouvons garantir que
toutes les informations sont mises à jour. Nous conseillons de contacter un
avocat local pour obtenir des conseils juridiques sur la conformité et la
validité des signatures électroniques.

## Send a document to sign

### One-time signature

You can click Upload a PDF to sign from your dashboard for a one-time
signature. Select your document, open it, and drag and drop the required
fields in your document. You can modify the role assigned to a field by
clicking on it and selecting the one you want.

When ready, click Send, and fill in the required fields. Once sent, your
document remains available. Go to Documents ‣ All Documents to see your
document and the status of the signatures.

![Signature status](../../_images/signature-status.png)

### Modèles

You can create document templates when you have to send the same document
several times. From your dashboard, click Upload a PDF template. Select the
document and add the required fields. You can modify the role of a field by
clicking on it and selecting the one you want.

Click Template Properties to add Tags to your template, define a Signed
Document Workspace, add Signed Document Tags, set a Redirect Link that will be
available in the signature confirmation message received after the signature,
or define Authorized Users if you want to restrict the use of your template to
specific authorized users or groups.

Your templates are visible by default on your dashboard. You can click Send to
quickly send a document template to a signer or Sign Now if you are ready to
sign your document immediately.

Astuce

You can **create a template from a document that was previously sent**. To do
so, go to Documents ‣ All Documents. On the document you want to retrieve,
click on ⋮, then Template. Click on ⋮ again, then Restore. Your document now
appears on your dashboard next to your other templates.

## Rôles

Each field in a Sign document is related to a role corresponding to a specific
person. When a document is being signed, the person assigned to the role must
fill in their assigned fields and sign it.

Les rôles sont disponibles en allant dans Signature ‣ Configuration ‣ Rôles.

It is possible to update existing roles or to create new roles by clicking on
New. Choose a Role Name, add an Extra Authentication Step to confirm the
identity of the signing person, and if the document can be reassigned to
another contact, select Change Authorized for the role. A Color can also be
chosen for the role. This color can help understand which roles are
responsible for which field when configuring a template.

### Identification sécurisée

As the owner of a document, you may request an Extra Authentication Step
through SMS verification or via Itsme® (available in Belgium and the
Netherlands). Both authentication options require
[credits](../essentials/in_app_purchase.html#iap-buying-credits). If you do
not have any credits left, the authentication steps will be skipped.

Pour plus d'infos

  * [In-App Purchase (IAP)](../essentials/in_app_purchase.html)

  * [Tarif des SMS et FAQ](../marketing/sms_marketing/pricing/pricing_and_faq.html)

#### Vérification par SMS

Allez à Signature ‣ Configuration ‣ Rôles. Cliquez sur la colonne Étape
d’authentification supplémentaire du rôle et sélectionnez Code unique par SMS.

Note

Before being able to send SMS Text Messages, you need to register your phone
number. To do so, go to Sign ‣ Configuration ‣ Settings and click Buy credits
under Authenticate by SMS.

Go to the document to sign, add the field for which the SMS verification is
required, for example, the Signature field, and click Send. On the new page,
select the customer and click Send.

The person signing the document fills in the Signature field, then Sign, and
clicks Validate & Send Completed Document. A Final Validation page pops up
where to add their phone number. One-time codes are sent by SMS.

![Ajoutez un hachage à votre document](../../_images/sms-verification.png)

Note

  * Cette fonctionnalité est désactivée par défaut.

  * Dès que l”Étape d’authentification supplémentaire s’applique à un rôle, cette étape de validation est requise pour tout champ assigné à ce rôle.

#### Itsme®

Itsme® authentication can be used to allow signatories to provide their
identity using itsme®. This feature is only available in **Belgium** and the
**Netherlands**.

The feature can be enabled in Sign Settings and applies automatically to the
Customer (identified with itsme®) role. To enable it for other roles, go to
Sign ‣ Configuration ‣ Roles. Click in the Extra Authentication Step column
for the role, and select Via itsme®.

Go to the document that needs to be signed and add the Signature field. Switch
to any role configured to use the feature, and click Validate and Send.

![Sélectionnez le client identifié avec itsme®](../../_images/itsme-
identification.png)

Upon signing the document, the signer completes the Signature field and
proceeds by clicking on Validate & Send Completed Document, triggering a Final
verification page where authentication via itsme® is required.

## Hachage du signataire

Each time someone signs a document, a **hash** \- a unique digital signature
of the operation - is generated to ensure traceability, integrity, and
inalterability. This process guarantees that any changes made after a
signature is affixed can be easily detected, maintaining the document’s
authenticity and security throughout its lifecycle.

A visual security frame displaying the beginning of the hash is added to the
signatures. Internal users can hide or show it by turning the Frame option on
or off when signing the document.

![Adding the visual security frame to a signature.](../../_images/sign-
hash.png)

## Étiquettes

Tags can be used to categorize and organize documents, allowing users to
search for and filter documents based on specific criteria quickly.

You can manage tags by going to Configuration ‣ Tags. To create a tag, click
New. On the new line, add the Tag Name and select a Color Index for your tag.

To apply a tag to a document, use the dropdown list available in your
document.

## Sign order

When a document needs to be signed by different parties, the signing order
lets you control the order in which your recipients receive it for signature.

By going to Configuration ‣ Settings, you can Enable Signing Order. Each
recipient receives the signature request notification only once the previous
recipient has completed their action.

Add at least two Signature fields with different roles to your document. Click
Send, go to the Options tab, and tick the Specify signing order box.

Add the signer’s Name or email information. You can decide on the Sign Order
by typing 1 or 2 in the Sign Order column.

Pour plus d'infos

[Odoo Quick Tips: Sign order
[video]](https://www.youtube.com/watch?v=2KUq7RPt1cU/)

## Field types

Fields are used in a document to indicate what information must be completed
by the signers. You can add fields to your document simply by dragging and
dropping them for the left column into your document.

Various field types can be used to sign documents (placeholder,
autocompletion, etc.). By configuring your own field types, also known as
signature item types, the signing process can be even faster for your
customers, partners, and employees.

Pour créer et modifier les types de champ, allez à Signature ‣ Configuration ‣
Paramètres ‣ Modifier les types de champ.

You can select an existing field by clicking on it, or you can Create a new
one. First, edit the Field Name. Then, select a Field Type:

  * Signature : les utilisateurs sont invités à saisir leur signature, soit en la dessinant, soit en générant une signature automatique basée sur leur nom, soit en téléchargeant un fichier local (généralement une image). Chaque type de champ Signature suivant réutilise les données saisies dans le premier champ.

  * Initiales : les utilisateurs sont invités à saisir leurs initiales, de la même manière que le champ Signature.

  * Texte : les utilisateurs saisissent du texte sur une seule ligne.

  * Texte multiligne : les utilisateurs saisissent du texte sur plusieurs lignes.

  * Case à cocher : les utilisateurs peuvent cocher une case (par ex. pour marquer leur approbation ou leur consentement).

  * Sélection : les utilisateurs choisissent une option unique parmi une variété d’options.

Le paramètre Remplir automatiquement le champ partenaire est utilisé pour
compléter automatiquement un champ pendant le processus de signature. Il
utilise la valeur d’un des champs du modèle de contact (`res.partner`) du
signataire du document. Pour ce faire, saisissez le nom technique du champ du
modèle de contact.

Astuce

Pour connaître le nom technique d’un champ, activez le mode développeur et
passez votre souris sur le point d’interrogation situé à côté du champ.

Note

Les valeurs complétées automatiquement sont des suggestions et peuvent être
modifiées comme le demande le signataire du document.

The size of the fields can also be changed by editing the Default Width and
Default Height. Both sizes are defined as a percentage of the full page
expressed as a decimal, with 1 equalling the full page’s width or height. By
default, the width of new fields you create is set to 15% (0.150) of a full
page’s width, while their height is set to 1.5% (0.015) of a full page’s
height.

Rédigez ensuite un Conseil. Les conseils sont affichés à l’intérieur de
flèches sur le côté gauche de l’écran de l’utilisateur pendant le processus de
signature pour l’aider à comprendre ce que l’étape implique (par ex. « Signer
ici » ou “Saisir votre date de naissance”). Vous pouvez également utiliser un
texte Placeholder qui s’affichera dans le champ avant qu’il ne soit complété.

![Exemple de conseil et de placeholder dans Odoo Signature](../../_images/tip-
placeholder.png)

