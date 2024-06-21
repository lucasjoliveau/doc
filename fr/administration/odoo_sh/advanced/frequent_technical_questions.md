# Questions techniques fréquentes

## « Les actions planifiées ne s’exécutent pas à l’heure exacte à laquelle
elles étaient prévues »

Sur la plateforme Konvergo ERP.sh, nous ne pouvons pas garantir une heure d’exécution
exacte pour les actions planifiées.

Ceci est dû au fait qu’il peut y avoir plusieurs clients sur le même serveur
et nous devons garantir une part équitable du serveur pour chaque client. Les
actions planifiées sont donc mises en œuvre légèrement différemment que sur un
serveur Konvergo ERP normal et sont exécutées selon une politique de _meilleur
effort_.

<div class="alert alert-warning">
<p class="alert-title">
Avertissement</p><p>Ne vous attendez pas qu’une action planifiée soit exécutée plus souvent que toutes les 5 minutes.</p>
</div>

## Existe-t-il des « meilleures pratiques » concernant les actions planifiées
?

**Konvergo ERP.sh limitera toujours le temps d’exécution des actions planifiées (*aka*
crons).** Par conséquent, vous devez garder ce fait à l’esprit lorsque vous
développez vos propres crons.

Nous conseillons ce qui suit :

  * Vos actions planifiées doivent s’exécuter sur de petits lots d’enregistrements.

  * Vos actions planifiées doivent commiter leur travail après avoir traité chaque lot ; ainsi, si elles sont interrompues par la limite de temps, il n’est pas nécessaire de recommencer.

  * Vos actions planifiées doivent être [idempotentes](https://stackoverflow.com/a/1077421/3332416) : elles ne doivent pas provoquer d’effets secondaires si elles sont lancées plus souvent que prévu.

