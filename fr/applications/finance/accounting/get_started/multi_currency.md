# Système multidevise

Konvergo ERP vous permet d’émettre des factures clients, de recevoir des factures
fournisseurs et d’enregistrer les transactions dans des devises autre que la
devise principale configurée pour votre entreprise. Vous pouvez également
configurer des comptes bancaires dans d’autres devises et exécuter des
rapports sur vos activités en devises étrangères.

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../bank/foreign_currency">Gérer un compte bancaire en devise étrangère</a></p></li>
</ul>
</div>

## Configuration

### Devise principale

La **devise principale** est définie par défaut en fonction du pays de
l’entreprise. Vous pouvez la modifier en allant à Comptabilité ‣ Configuration
‣ Paramètres ‣ Devises et en modifiant la devise dans le paramètre **Devise
principale**.

### Activer les devises étrangères

Allez à Comptabilité ‣ Configuration ‣ Devises, et activez les devises que
vous souhaitez utiliser en cliquant sur le bouton **Actif**.

![Activez les devises que vous souhaitez
utiliser.](../../../../_images/enable-foreign-currencies.png)

### Taux de change

#### Mise à jour manuelle

Pour manuellement créer et définir un taux de change, allez à Comptabilité ‣
Configuration ‣ Devises, cliquez sur la devise pour laquelle vous souhaitez
modifier le taux et dans l’onglet **Taux** , cliquez sur **Ajouter une ligne**
pour créer un nouveau taux.

![Créez ou modifiez le taux de change.](../../../../_images/manual-rate-
update.png)

#### Mise à jour automatique

Lorsque vous activez une seconde devise pour la première fois, l’option **Taux
de change automatiques** apparaît sur le Tableau de bord Comptabilité ‣
Configuration ‣ Paramètres ‣ Devises. Par défaut, vous devez cliquer sur le
bouton **Mettre à jour maintenant** (**🗘**) pour mettre à jour les taux.

Konvergo ERP peut mettre à jour les taux à des intervalles réguliers. Pour ce faire,
modifiez l”**Intervalle** de **Manuellement** en **Quotidien** ,
**Hebdomadaire** ou **Mensuel**. Vous pouvez également sélectionner le service
web à partir duquel vous souhaitez récupérer les derniers taux de change en
cliquant sur le champ **Service**.

### Écritures de différence de change

Konvergo ERP enregistre automatiquement les écritures de différences de change sur les
comptes dédiés, dans un journal dédié.

Vous pouvez définir le journal et les comptes à utiliser pour **enregistrer
les écritures de différence de change** en allant à Comptabilité ‣
Configuration ‣ Paramètres ‣ Comptes par défaut et en modifiant le **Journal**
, le **Compte des gains** , et le **Compte des pertes**.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>Si vous recevez le paiement d’une facture client un mois après son émission, le taux de change a probablement changé depuis. Par conséquent, cette fluctuation implique un gain ou une perte en raison de la différence de change, qu’Konvergo ERP enregistre automatiquement dans le journal <b>Différence de change</b> par défaut.</p>
</div>

### Plan comptable

Chaque compte peut avoir une devise définie. Ainsi, tous les mouvements
relatifs au compte sont forcés d’utiliser la devise de ce compte.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Plan comptable et
sélectionnez une devise dans le champ **Devise du compte**. Si le champ est
vide, toutes les devises actives sont prises en compte au lieu d’une seule.

### Journaux

Si une devise est définie sur un **journal** ; ce journal prend uniquement en
compte les transactions dans cette devise.

Pour ce faire, allez à Comptabilité ‣ Configuration ‣ Journaux, ouvrez le
journal que vous souhaitez modifier et sélectionnez une devise dans le champ
**Devise**.

![Sélectionnez la devise que le journal doit prendre en
compte.](../../../../_images/journal-currency.png)

## Comptabilité multidevise

### Factures clients, factures fournisseurs et autres documents

Pour tous les documents, vous pouvez sélectionner la devise et le journal à
utiliser pour la transaction sur le document même.

![Sélectionnez la devise et le journal à
utiliser.](../../../../_images/currency-field.png)

### Enregistrement des paiements

Pour enregistrer un paiement dans une devise autre que la devise principale de
votre société, cliquez sur le bouton de paiement **Enregistrer un paiement**
de votre document et, dans la fenêtre contextuelle, sélectionnez une
**devise** dans le champ **Montant**.

![Sélectionnez la devise et le journal à utiliser avant d'enregistrer le
paiement.](../../../../_images/register-payment.png)

### Transactions bancaires

Lors de la création ou de l’importation des transactions bancaires, le montant
est exprimé dans la devise principale de la société. Pour saisir une **devise
étrangère** , sélectionnez une devise dans le champ **Devise étrangère**. Une
fois la devise sélectionnée, saisissez le **Montant** dans votre devise
principale pour qu’il soit automatiquement converti dans la devise étrangère
dans le champ **Montant en devise**.

![Les champs supplémentaires liés aux devises
étrangères.](../../../../_images/foreign-fields.png)

Lors du lettrage, Konvergo ERP affiche à la fois le montant en devise étrangère et le
montant équivalent dans la devise principale de votre société.

### Écritures de différence de change

Pour voir les **écritures de différence de change** , allez au Tableau de bord
Comptabilité ‣ Comptabilité ‣ Journaux : Divers.

![Écriture de différence de change.](../../../../_images/exchange-journal-
currency.png)

