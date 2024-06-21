# SIPS

[SIPS](https://sips.worldline.com/) est une solution de paiement en ligne de
la multinationale Worldline.

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Onglet des identifiants

Konvergo ERP a besoin de vos **identifiants API** pour se connecter à votre compte
SIPS. Ils incluent :

  * **Identifiant du marchand** : L’identifiant utilisé uniquement pour identifier le compte marchand auprès de SIPS.

  * **Clé secrète** : La clé pour signer le compte marchand avec SIPS.

  * **Version clé secrète** : La version de la clé, préremplie.

  * **Version Interface** : Préremplie, ne la modifiez pas.

Vous pouvez copier vos identifiants à partir de la documentation
d’informations sur votre environnement SIPS, dans la section **PROD** , et les
coller dans les champs associés dans l’onglet **Identifiants**.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous testez SIPS avec les informations d’identification <em>TEST</em>, définissez le <b>Statut</b> sur <em>Mode test</em>. Nous vous recommandons de le faire sur une base de données de test Konvergo ERP, plutôt que sur votre base de données principale.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

