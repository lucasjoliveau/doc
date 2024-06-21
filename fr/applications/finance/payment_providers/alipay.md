# Alipay

[Alipay](https://www.alipay.com/) est une plateforme de paiement en ligne
établie en Chine par le groupe Alibaba.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Le fournisseur Alipay est obsolète. Nous vous recommandons d’utiliser plutôt <a href="asiapay">AsiaPay</a>.</p>
</div>

## Configuration

<div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers#payment-providers-add-new"><span class="std std-ref">Enable a payment provider</span></a></p></li>
</ul>
</div>

### Onglet des identifiants

Konvergo ERP a besoin de vos **identifiants API** pour se connecter à votre compte
Alipay. Ils incluent :

  * **Compte** : Selon l’endroit où vous vous trouvez - `Paiement rapide` si vous êtes un marchand chinois. - `Transfrontalier` si vous ne l’êtes pas.

  * **Email du vendeur Alipay** : L’adresse email publique de votre partenaire Alipay (pour le paiement rapide uniquement).

  * **ID Partenaire Marchand** : L’identifiant du partenaire public uniquement utilisé pour identifier le compte auprès d’Alipay.

  * **Clé de signature MD5** : La clé de signature.

Vous pouvez copier vos identifiants depuis votre compte Alipay et les coller
dans les champs associés dans l’onglet **Identifiants**.

Pour les récupérer, connectez-vous à votre compte Alipay, ils sont en première
page.

<div class="alert alert-warning">
<p class="alert-title">
Important</p><p>Si vous testez Alipay, dans le <em>sandbox</em>, changez le <b>statut</b> en <em>Mode test</em>. Nous vous recommandons de le faire sur une base de données de test Konvergo ERP, plutôt que sur votre base de données principale.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><ul>
<li><p><a href="../payment_providers">Paiements en ligne</a></p></li>
</ul>
</div>

