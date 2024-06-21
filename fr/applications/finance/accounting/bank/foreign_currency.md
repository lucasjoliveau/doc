# Gérer un compte bancaire en devise étrangère

Dans Konvergo ERP, chaque transaction est enregistrée dans la devise par défaut de
l’entreprise et les rapports sont tous basés sur cette devise par défaut.
Lorsque vous possédez un compte bancaire dans une devise étrangère, pour
chaque transaction, Konvergo ERP enregistre deux valeurs :

  * Le débit/crédit dans la devise de la _société_ ;

  * Le débit/crédit dans la devise du _compte bancaire_.

Les taux de change sont automatiquement mis à jour en utilisant les services
web d’un établissement bancaire. Par défaut, Konvergo ERP utilise les services web de
la Banque centrale européenne, mais il y a aussi d’autres options.

## Configuration

### Activer l’option multi-devises

Pour travailler avec plusieurs devises, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Devises et cochez **Multi-devises**. Dans **Enregistrer les
écritures de différence de change dans :** , saisissez un **Journal** , un
**Compte de gain** , un **Compte de perte** et cliquez sur **Enregistrer**.

### Configurer des devises

Une fois qu’Konvergo ERP est configuré pour prendre en charge plusieurs devises, elles
sont toutes créées par défaut, mais pas nécessairement actives. Pour activer
de nouvelles devises, cliquez sur **Activer d’autres devises** dans le
paramètre **Multi-Devises** ou allez à Comptabilité ‣ Configuration ‣
Comptabilité : Devises.

Lorsque les devises sont activées, vous pouvez choisir d” _automatiser_ la
mise à jour du taux de change ou de laisser l’automatisation **manuelle**.
Pour configurer la mise à jour du taux, allez à Comptabilité ‣ Configuration ‣
Paramètres ‣ Devises, cochez **Taux de change automatiques** , définissez
l”**Intervalle** sur votre fréquence souhaitée et cliquez sur **Enregistrer**.
Vous avez également l’option de choisir le **Service** dont vous souhaitez
obtenir les taux de change.

Cliquez sur le bouton Mettre à jour maintenant (**🗘**) à côté du champ
**Prochaine exécution** pour mettre à jour les taux de change manuellement.

### Créer un nouveau compte bancaire

Dans l’application Comptabilité, allez à Comptabilité ‣ Configuration ‣
Journaux et créez-en un nouveau. Saisissez un **Nom de journal** et définissez
le **Type** sur `Banque`. Dans l’onglet **Pièces comptables** , saisissez un
**code court** , une **devise** et cliquez finalement sur le champ **Compte
bancaire** pour créer un nouveau compte. Dans la fenêtre contextuelle de la
création de compte, saisissez un nom, un code (par ex. 550007), définissez son
type sur `Banque et Espèces`, configurez un type de devise et enregistrez. De
retour sur le **journal** , cliquez sur le champ **Numéro de compte** et dans
la fenêtre contextuelle, complétez le **Numéro de compte** , la **Banque** de
votre compte et enregistrez.

![Exemple d'un journal de banque créé.](../../../../_images/foreign-
journal.png)

Lors de la création du journal, Konvergo ERP lie automatiquement le compte bancaire au
journal. Vous pouvez le retrouver dans Comptabilité ‣ Configuration ‣
Comptabilité : Plan comptable.

## Facture fournisseur en devise étrangère

Afin de payer une facture fournisseur en devise étrangère, il suffit
simplement de sélectionner la devise à côté du champ **Journal** et
d’enregistrer le paiement. Konvergo ERP crée et comptabilise automatiquement **le gain
ou la perte de change** de la devise étrangère comme une nouvelle pièce
comptable.

![Comment configurer une devise de facture
fournisseur.](../../../../_images/foreign-bill-currency.png)
<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Notez que vous pouvez payer une facture fournisseur étrangère avec une autre devise. Dans ce cas, Konvergo ERP fait automatiquement la conversion d’une devise à l’autre.</p>
</div>

## Rapport d’écarts de conversion

Ce rapport vous donne un aperçu de tous les montants non réalisés en devise
étrangère dans votre bilan et vous permet d’ajuster une entrée ou de définir
manuellement un taux de change. Pour accéder à ce rapport, allez à Analyse ‣
Gestion : Écarts de conversion. À partir de là, vous pouvez accéder à toutes
les écritures ouvertes dans votre **bilan**.

![Vue du journal des écarts de conversion](../../../../_images/foreign-gains-
losses.png)

Si vous souhaitez utiliser un taux de change différent que celui configuré
dans Comptabilité ‣ Configuration ‣ Paramètres ‣ Devises, cliquez sur le
bouton **Taux de change** et modifiez le taux des devises étrangères dans le
rapport.

![Menu permettant de modifier manuellement les taux de
change.](../../../../_images/foreign-exchange-rates.png)

Lors du changement manuel des **taux de change** , une bannière jaune apparaît
et vous permet de revenir au taux d’Konvergo ERP. Pour ce faire, cliquez simplement
sur **Réinitialiser au taux d’Konvergo ERP**.

![Bannière permettant de réinitialiser au taux
d'Konvergo ERP.](../../../../_images/foreign-reset-rates.png)

Afin de mettre à jour votre **bilan** avec le montant de la colonne
**ajustement** , cliquez sur le bouton **Écriture d’ajustement**. Dans la
fenêtre contextuelle, sélectionnez un **Journal** , un **Compte de charges**
et un **Compte de produits** pour calculer et traiter les **écarts de
conversion**.

Vous pouvez définir la date du rapport dans le champ **Date**. Konvergo ERP extourne
automatiquement l’écriture à la date définie dans **Date d’extourne**.

Une fois comptabilisée, la colonne **ajustement** devrait indiquer `0,00`,
signifiant que tous les **écarts de conversion** ont été ajustés.

![Le rapport d'écarts de conversion après
l'ajustement.](../../../../_images/foreign-adjustment.png)

