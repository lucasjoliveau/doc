# Questions chronométrées et aléatoires

Lors de la création d’un sondage dans Konvergo ERP, certaines options permettent de
fixer une limite de temps pour le sondage et rendre les questions aléatoires.

## Limite de temps

Dans le cadre d’un sondage chronométré, les participants doivent terminer le
sondage dans un laps de temps défini. La limite de temps est souvent utilisée
pour réduire la possibilité qu’un participant cherche la réponse via une
ressource externe (par ex. internet) et pour réduire le sondage à un
environnement de test « à livre fermé ».

Le paramètre **Limite de temps du sondage** se trouve dans l’onglet
**Options** du formulaire du sondage, sous la section **Questions**.

![Champ de la limite de temps dans l'onglet Options d'un formulaire du modèle
de sondage.](../../../_images/time-limit.png)

Lorsque l’option **Limite de temps du sondage** est activée, un minuteur
s’affiche sur chaque page du sondage, permettant aux participants de garder un
œil sur le temps restant quand ils répondent au sondage.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Les participants qui ne soumettent pas leur sondage dans le laps de temps prédéfini ne verront <em>pas</em> leurs réponses enregistrées.</p>
</div>

## Sélection aléatoire

Lorsqu’un sondage est aléatoire, Konvergo ERP mélange les questions et les révèle dans
un ordre aléatoire chaque fois qu’un participant commence le questionnaire. Le
mode aléatoire décourage les participants de regarder les réponses des autres
et permet de contrôler les tests individuels.

Pour rendre un sondage aléatoire, cliquez sur l’onglet **Options** dans le
formulaire du sondage. Dans la section **Questions** , sélectionnez
**Aléatoire par section** dans le champ **Sélection**. Après l’avoir activé,
allez à l’onglet **Questions** et regardez dans la colonne **Nombre de
questions aléatoires**. Vous pouvez y définir le nombre de questions (par
section) que Konvergo ERP devrait sélectionner et afficher pendant le mélange des
questions.

![Nombre de questions aléatoires dans l'onglet Questions d'un
sondage.](../../../_images/random-questions.png) <div class="alert alert-secondary">
<p class="alert-title">
Pour plus d'infos</p><p><a href="scoring">Noter les sondages</a></p>
</div>

