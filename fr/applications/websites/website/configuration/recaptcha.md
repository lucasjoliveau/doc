# reCAPTCHA v3 sur les formulaires

Le reCAPTCHA de Google protège les formulaires de site web contre les spams et
les abus. Il tente de faire la distinction entre les soumissions humaines et
celles des robots.

Avertissement

reCAPTCHA v3 may not be compliant with local data protection regulations.

Note

reCAPTCHA v3 fonctionne en arrière-plan et n’interrompt pas les visiteurs.
Toutefois, si la vérification échoue, les visiteurs ne peuvent pas soumettre
le formulaire.

Pour plus d'infos

[Guide reCAPTCHA v3 de
Google](https://developers.google.com/recaptcha/docs/v3)

## Configuration

### Dans Google

Ouvrez [la page d’inscription au site web
reCAPTCHA](https://www.google.com/recaptcha/admin/create). Connectez-vous ou
créez un compte Google le cas échéant.

Sur la page d’inscription au site web :

  * Donnez un Libellé au site web.

  * Laissez le type de reCAPTCHA sur Basé sur le score (v3).

  * Saisissez un ou plusieurs Domaines (par ex. _example.com_ ou _subdomain.example.com_).

  * Sur Google Cloud Platform, un projet est automatiquement sélectionné s’il a déjà été créé avec le compte Google connecté. Si ce n’est pas le cas, un projet est automatiquement créé. Cliquez sur Google Cloud Platform pour sélectionner un projet vous-même ou pour renommer le projet créé automatiquement.

  * Acceptez les conditions d’utilisation.

  * Cliquez sur Soumettre.

![Exemple d'inscription au site web reCAPTCHA](../../../../_images/recaptcha-
google-configuration.png)

Une nouvelle page contenant les clés générées s’affiche alors. Laissez-la
ouverte pour plus de facilité, car vous devrez copier les clés dans Odoo
ultérieurement.

### Dans Odoo

  * Depuis le tableau de bord de la base de données, cliquez sur Paramètres. Sous Intégrations, activez reCAPTCHA le cas échéant.

Avertissement

Ne désactivez pas la fonctionnalité reCAPTCHA ou ne désinstallez pas le module
Intégration Google reCAPTCHA, car de nombreux autres modules seraient
également supprimés.

  * Ouvrez la page Google reCAPTCHA, copiez la Clé du site et collez-la dans le champ Clé du site dans Odoo.

  * Ouvrez la page Google reCAPTCHA, copiez la Clé secrète et collez-la dans le champ Clé secrète dans Odoo.

  * Changez le Score minimum par défaut (`0.5`) si nécessaire, en utilisant une valeur entre `1.0` et `0.0`. Plus le seuil est élevé, plus il est difficile de passer le reCAPTCHA, et vice versa.

  * Cliquez sur Enregistrer.

Toutes les pages utilisant les snippets Formulaire, Bloc Newsletter, Fenêtre
contextuelle Newsletter et le formulaire d’eCommerce Étape supplémentaire lors
du paiement sont désormais protégés par reCAPTCHA.

Note

  * Si la vérification reCAPTCHA échoue, le message d’erreur suivant s’affiche :

![Message d'erreur de vérification reCAPTCHA
Google](../../../../_images/recaptcha-error.png)

  * reCAPTCHA v3 est gratuit jusqu’à [1 million de vérifications par mois](https://developers.google.com/recaptcha/docs/faq#are-there-any-qps-or-daily-limits-on-my-use-of-recaptcha).

Astuce

  * Des analyses et des paramètres supplémentaires sont disponibles sur la [page d’administration reCAPTCHA de Google](https://www.google.com/recaptcha/admin/). Par exemple, vous pouvez recevoir des alertes par email lorsque Google détecte un trafic suspect sur votre site web ou afficher le pourcentage de demandes suspectes, ce qui peut vous aider à déterminer le score minimum adéquat.

  * Vous pouvez informer les visiteurs que reCAPTCHA protège un formulaire. Pour ce faire, ouvrez l’éditeur de site web et allez au formulaire. Ensuite, cliquez quelque part sur le formulaire et dans l’onglet Personnaliser de la barre latérale droite, cochez la case Afficher la politique reCAPTCHA qui se trouve dans la section Formulaire.

![Message de politique reCAPTCHA affiché sur un
formulaire](../../../../_images/recaptcha-policy.png)

