# Créer des feuilles de temps lors de la validation des congés

Odoo établit automatiquement des feuilles de temps sur les projets/tâches lors
des demandes de congés. Cela permet un meilleur contrôle global sur la
validation des feuilles de temps, car il ne laisse pas de place aux oublis et
aux questions après les heures non renseignées par l’employé.

Activez le [mode développeur](../../../general/developer_mode.html#developer-
mode), allez à _Feuilles de temps_ et modifiez le _Projet_ et la _Tâche_
définis par défaut, si vous le souhaitez.

![Vue du paramètre des Feuilles de temps permettant d'activer la fonction
d'enregistrement des congés dans Odoo Feuilles de
temps](../../../../_images/record_time_off.png)

Allez à Congés ‣ Configuration ‣ Types de congés. Sélectionnez le type
nécessaire ou créez-le et décidez si vous souhaitez que les demandes soient
validées ou non.

![Vue d'un formulaire de types de congé mettant en évident les demandes de
congé et la section des feuilles de temps dans Odoo
Congés](../../../../_images/time_off_types.png)

Désormais, une fois que l’employé a demandé son congé et que la demande a été
validée (ou non, selon le paramètre choisi), le temps est automatiquement
attribué sur _Feuilles de temps_ , sous le projet et la tâche respectifs.

Dans l’exemple suivant, l’utilisateur a demandé des _congés payés_ du 13 au 15
juillet.

![Vue d'un formulaire de demande de congé dans Odoo
Congés](../../../../_images/time_off_request.png)

Étant donné qu’aucune validation n’est requise, le congé demandé est
automatiquement affiché dans _Feuilles de temps_. Si une validation est
nécessaire, le temps est automatiquement alloué après que la personne
responsable de la validation l’a fait.

![Vue des feuilles de temps mettant en évident le congé demande par l'employé
dans Odoo Feuilles de temps](../../../../_images/timesheets.png)

Cliquez sur la loupe, survolant la cellule concernée, pour accéder à toutes
les données agrégées sur cette cellule (jour), et voir les détails concernant
le projet/la tâche.

![Vue des détails d'un projet/tâche dans Odoo Feuilles de
temps](../../../../_images/timesheet_description.png)

