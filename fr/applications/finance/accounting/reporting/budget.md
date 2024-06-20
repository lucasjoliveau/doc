# Budget financier

La gestion des budgets est un élément essentiel de la gestion d’une
entreprise. Les budgets permettent aux gens de réaliser comment l’argent est
dépensé et d’organiser et prioriser leur travail pour atteindre leurs
objectifs financiers. Ils permettent aussi de planifier le résultat financier
souhaité et de mesurer les performances réelles par rapport aux prévisions.
Odoo gère les budgets grâce à l’aide de **comptes généraux** et de **comptes
analytiques**.

## Configuration

Allez à Comptabilité ‣ Configuration ‣ Paramètres ‣ section Analytique et
activez la fonctionnalité Gestion du budget.

### Postes budgétaires

Les postes budgétaires sont des listes de comptes pour lesquels vous souhaitez
conserver des budgets (généralement des comptes de charges ou de produits).

Pour définir des postes budgétaires, allez à Comptabilité ‣ Configuration ‣
Gestion : Postes budgétaires et cliquez sur Nouveau. Donnez un Nom à votre
poste budgétaire et sélectionnez la Société à laquelle il s’applique. Cliquez
sur Ajouter une ligne pour ajouter un ou plusieurs comptes.

Note

Chaque poste budgétaire peut avoir un nombre indéfini de comptes du plan
comptable, mais il doit en avoir au moins un.

## Cas d’utilisation

Prenons un exemple simple.

Nous venons de lancer un projet avec _Smith & Co_ et nous aimerions budgétiser
les produits et les charges de ce projet. Nous prévoyons un chiffre d’affaires
de 1.000 et nous ne voulons pas dépenser plus de 700.

Tout d’abord, nous devons définir quels comptes s’associent aux charges de
notre projet. Allez à Comptabilité ‣ Configuration ‣ Gestion : Postes
budgétaires et cliquez sur Nouveau pour ajouter un poste. Ajoutez les comptes
dans lesquels les charges seront enregistrées.

![Afficher les charges du projet de Smith & Co](../../../../_images/smith-and-
co-expenses.png)

Répétons les étapes pour créer un poste budgétaire qui reflète les produits.

![Afficher les produits du produit de Smith & Co](../../../../_images/smith-
and-co-revenue.png)

### Comptes analytiques

Odoo doit savoir quels coûts ou charges sont pertinents pour un budget
spécifique, puisque les comptes généraux susmentionnés peuvent être utilisés
pour différents projets. Allez à Comptabilité ‣ Configuration ‣ Comptabilité
analytique : Comptes analytiques et cliquez sur Nouveau pour ajouter un
nouveau **Compte analytique** intitulé _Smith & Co_.

Vous devez remplir le champ Plan, car les plans regroupent plusieurs comptes
analytiques, ils distribuent les coûts et les bénéfices afin d’analyser les
performances commerciales. Vous pouvez créer ou configurer les **Plans
analytiques** en allant à Comptabilité ‣ Configuration ‣ Comptabilité
analytique : Plans analytiques.

Lors de la création d’une nouvelle facture client et/ou facture fournisseur,
vous devez faire référence à ce compte analytique.

![Ajoutez des comptes analytiques à une nouvelle facture client ou
fournisseur.](../../../../_images/analytic-accounts.png)

### Définir le budget

Fixons à présent nos objectifs. Nous avons précisé que nous espérions gagner
1.000 avec ce projet et nous aimerions ne pas dépenser plus de 700. Allez à
Comptabiilté ‣ Gestion : Budgets et cliquez sur Nouveau pour créer un nouveau
budget pour le projet _Smith & Co_.

Tout d’abord, complétez le Nom du budget. Ensuite, sélectionnez la Période
pendant laquelle le budget s’applique. Ajoutez ensuite le Poste budgétaire que
vous voulez suivre, définissez le Compte analytique associé et ajoutez le
Montant prévu.

![Affichage des lignes budgétaires](../../../../_images/define-the-budget.png)

Note

Lors de l’enregistrement d’un montant prévu lié aux charges, le montant doit
être négatif.

### Vérifier votre budget

Allez à Comptabilité ‣ Gestion : Budgets et trouvez le projet _Smith & Co_
pour voir comment il évolue en fonction des charges ou des produits du compte
analytique correspondant.

Le Montant réel évolue lorsqu’une nouvelle pièce comptable associée à votre
compte analytique et à un compte de votre poste budgétaire est créée.

Le Montant théorique représente la somme d’argent que vous auriez
théoriquement pu dépenser ou auriez dû recevoir en fonction de la date. Par
exemple, supposons que votre budget s’élève à 1.200 pour 12 mois (janvier à
décembre) et qu’aujourd’hui, nous sommes le 31 janvier. Dans ce cas, le
montant théorique s’élève à 100 puisque c’est le montant réel qui aurait pu
être réalisé.

