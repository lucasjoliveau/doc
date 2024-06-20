# Noter les sondages

Pour mesurer les performances, les connaissances ou la satisfaction globale
d’un participant à un sondage, Odoo attribue des points aux réponses du
sondage. À la fin du sondage, ces points sont additionnés, ce qui donne le
score final d’un participant.

Pour ajouter des points aux questions, ouvrez l’application Sondages,
sélectionnez le sondage souhaité et cliquez sur l’onglet Options. Sous la
section :guilabel;`Notation`, choisissez entre Notation avec réponses à la fin
ou Notation sans réponses à la fin.

  * La Notation avec réponses à la fin permet d’afficher les réponses que les participants ont donné et de montrer les questions auxquelles ils ont donné une bonne ou mauvaise réponse. Pour les questions auxquelles ils ont donné une mauvaise réponse, la bonne réponse sera mise en évidence.

  * La Notation sans réponses à la fin permet de montrer aux participants leur score final après avoir répondu au sondage, sans détailler les réponses données.

Pour indiquer les bonnes réponses, cliquez sur l’onglet Questions et
choisissez une question. Dans le formulaire de question, cochez la case Est
une bonne réponse à côté de la bonne réponse et associez-y une note.

De retour à l’onglet Options du sondage, définissez le % pour réussir. Le
pourcentage saisi détermine le pourcentage de réponses correctes qui sont
nécessaires pour réussir le sondage.

Toujours dans l’onglet Options du sondage, les administrateurs du sondage
peuvent choisir de transformer un sondage en certification. Une certification
indique que le sondage pose des questions pour tester le niveau de
connaissances des participants sur un sujet.

Lorsque vous activez l’option Est une certification, choisissez un Modèle
d’email de certification. La certification sera automatiquement envoyée par
email à l’aide de ce modèle aux utilisateurs qui ont réussi le sondage avec un
score final supérieur ou égal au % pour réussir défini.

Dans la section Participants, les participants peuvent être invités à se
connecter pour participer au sondage. Si le paramètre Connexion requise est
activée, deux nouvelles options apparaissent : la case à cocher Limiter les
tentatives, qui permet de limiter le nombre de fois qu’un participant peut
participer au sondage et l’option de Donner un badge, situé sous les options
de Certification dans la section Notation.

![Définir la note requise \(pourcentage\), la connexion requise et le modèle
de certification.](../../../_images/required-score-login.png)

Les badges sont affichés sur la partie eLearning d’un portail utilisateur et
permettent de fixer des étapes et de récompenser les participants qui
réussissent des sondages ou gagnent des points. Outre le bénéficiaire, les
visiteurs du site web qui consultent la page Cours pourront également voir les
badges accordés.

![Exemple de présentation d'un badge sur la partie eLearning du site
web.](../../../_images/frontend-badges.png)

Pour plus d'infos

[Questions chronométrées et aléatoires](time_random.html)

