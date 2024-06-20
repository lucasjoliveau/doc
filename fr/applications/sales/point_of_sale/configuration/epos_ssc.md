# Certificat auto-signé pour les imprimantes ePOS

To work with Odoo, some printer models that can be used without an [IoT
box](../../../general/iot/config/connect.html) may require [the HTTPS
protocol](https.html) to establish a secure connection between the browser and
the printer. However, trying to reach the printer’s IP address using HTTPS
leads to a warning page on most web browsers. In that case, you can
temporarily force the connection, which allows you to reach the page in HTTPS
and use the ePOS printer in Odoo as long as the browser window stays open.

Avertissement

La connexion est perdue après la fermeture de la fenêtre du navigateur. Par
conséquent, cette méthode ne doit être utilisée que comme solution de
**contournement** ou comme un prérequis pour les instructions suivantes.

## Générer, exporter et importer des certificats auto-signés

Pour une solution à long terme, vous devez générer un **certificat auto-
signé**. Ensuite, vous pouvez l’exporter et l’importer dans votre navigateur.

Important

La **génération** d’un certificat SSL ne doit être fait qu”**une seule fois**.
Si vous créez un autre certificat, les appareils utilisant le précédent
perdront l’accès HTTPS.

Windows 10 & Linux OSMac OSAndroid OSiOS

Generate a self-signed certificateExport a self-signed certificateImport a
self-signed certificate

Allez à l’adresse IP de l’ePOS (par ex. `https://192.168.1.25`) et forcez la
connexion en cliquant sur Avancé et Procéder à [adresse IP] (non sécurisé).

![Page d'avertissement sur la confidentialité de la connexion dans Google
Chrome](../../../../_images/browser-https-insecure.png)

Page d’avertissement dans Google Chrome, Windows 10

Ensuite, connectez-vous en utilisant les identifiants de l’imprimante pour
accéder aux paramètres de l’imprimante ePOS. Pour vous connecter, saisissez
`epson` dans le champ ID et le numéro de série de votre imprimante dans le
champ Mot de passe.

Cliquez sur Liste des certificats dans la section Authentification et cliquez
sur créer pour générer un nouveau **Certificat auto-signé**. Le Nom commun
devrait être complété automatiquement. Si ce n’est pas le cas, complétez-le
avec le numéro d’adresse IP de l’imprimante. Sélectionnez les années de
validité du certificat dans le champ Période de validité, cliquez sur Créer et
Réinitialiser ou redémarrez l’imprimante manuellement.

Le certificat auto-signé est généré. Rechargez la page et cliquez sur SSL/TLS
dans la section Sécurité pour vous assurer que le **Certificat auto-signé**
est correctement sélectionné dans la section Certificat du serveur.

La procédure d’exportation dépend fortement du système d’exploitation et du
navigateur. Commencez par accéder aux paramètres de votre imprimante ePOS sur
votre navigateur web en allant à son adresse IP (par ex.
`https://192.168.1.25`). Forcez ensuite la connexion comme il est expliqué
dans l’onglet **Générer un certificat autosigné**.

Si vous utilisez **Google Chrome** ,

  1. cliquez sur Non sécurisé à côté de la barre de recherche et Certificat non valide ;

![Le bouton dans la navigateur Google Chrome signalant que la Connexion à
l'imprimante n'est pas sécurisée.](../../../../_images/browser-warning.png)

  2. allez à l’onglet Détails et cliquez sur Exporter ;

  3. ajoutez `.crt` à la fin du nom de fichier pour vous assurer qu’il a l’extension correcte ;

  4. sélectionnez ASCII encodé en Base64, certificat unique, en bas de la fenêtre contextuelle ;

  5. enregistrez et le certificat est exporté.

Avertissement

Assurez-vous que le certificat se termine par l’extension `.crt`. Sinon,
certains navigateurs risquent de ne pas voir le fichier pendant la procédure
d’importation.

Si vous utilisez **Mozilla Firefox** ,

  1. cliquez sur l’icône en forme de **cadenas** à gauche de la barre d’adresse ;

  2. allez à Connexion non sécurisée ‣ Plus d’informations ‣ Onglet Sécurité ‣ Afficher le certificat ;

![Le bouton dans le navigateur Mozilla Firefox signalant que la connexion
n'est pas sécurisée.](../../../../_images/mozilla-not-secure.png)

  1. descendez jusqu’à la section Divers ;

  2. cliquez sur PEM (cert) dans la section Télécharger ;

  3. enregistrez et le certificat est exporté.

La procédure d’importation dépend fortement du système d’exploitation et du
navigateur.

Windows 10Linux

Windows 10 gère les certificats, ce qui signifie que les certificats auto-
signés doivent être importés depuis le fichier de certification plutôt que
depuis le navigateur. Procédez comme suit :

  1. ouvrez l’explorateur de fichiers de Windows et localisez le fichier de certification téléchargé ;

  2. cliquez droit sur le fichier de certification et cliquez sur Installer le certificat ;

  3. sélectionnez où installer le certificat et pour qui - soit pour l”utilisateur actuel, soit pour tous les utilisateurs (Ordinateur local). Cliquez ensuite sur Suivant ;

  4. sur l’écran du `Magasin de certificats`, cochez Placer tous les certificats dans le magasin suivant, cliquez sur Parcourir… et sélectionnez Autorités de certification racines de confiance ;

![../../../../_images/win-cert-wizard-store.png](../../../../_images/win-cert-
wizard-store.png)

  5. cliquez sur Terminer, acceptez la fenêtre contextuelle de sécurité ;

  6. redémarrez l’ordinateur pour vous assurer que tous les changements sont appliqués.

Si vous utilisez **Google Chrome** ,

  1. ouvrez Chrome ;

  2. allez à Paramètres ‣ Confidentialité et sécurité ‣ Sécurité ‣ Gérer les certificats ;

  3. allez à l’onglet Autorités, cliquez sur Importer et sélectionnez le fichier de certification importé ;

  4. acceptez tous les avertissements ;

  5. cliquez sur ok ;

  6. redémarrez votre navigateur.

Si vous utilisez **Mozilla Firefox** ,

  1. ouvrez Firefox ;

  2. allez à Paramètres ‣ Confidentialité & Sécurité ‣ Sécurité ‣ Afficher les certificats… ‣ Importer ;

  3. sélectionnez le fichier de certification exporté ;

  4. cochez les cases à cocher et validez ;

  5. redémarrez votre navigateur.

Sur Mac OS, vous pouvez sécuriser la connexion pour tous les navigateurs en
suivant les étapes suivantes :

  1. ouvrez Safari et allez à l’adresse IP de votre imprimante. Une page d’avertissement s’affiche ;

  2. sur la page d’avertissement, allez à Afficher les détails ‣ visiter ce site web ‣ Visiter le site web, validez ;

  3. redémarrez l’imprimante pour pouvoir l’utiliser avec n’importe quel autre navigateur.

Pour générer et exporter un certificat SSL et l’envoyer aux appareils iOS,
ouvrez **Google Chrome** ou **Mozilla Firefox**. Ensuite,

Generate a self-signed certificateExport a self-signed certificate

Allez à l’adresse IP de l’ePOS (par ex. `https://192.168.1.25`) et forcez la
connexion en cliquant sur Avancé et Procéder à [adresse IP] (non sécurisé).

![Page d'avertissement sur la confidentialité de la connexion dans Google
Chrome](../../../../_images/browser-https-insecure.png)

Page d’avertissement dans Google Chrome, Windows 10

Ensuite, connectez-vous en utilisant les identifiants de l’imprimante pour
accéder aux paramètres de l’imprimante ePOS. Pour vous connecter, saisissez
`epson` dans le champ ID et le numéro de série de votre imprimante dans le
champ Mot de passe.

Cliquez sur Liste des certificats dans la section Authentification et cliquez
sur créer pour générer un nouveau **Certificat auto-signé**. Le Nom commun
devrait être complété automatiquement. Si ce n’est pas le cas, complétez-le
avec le numéro d’adresse IP de l’imprimante. Sélectionnez les années de
validité du certificat dans le champ Période de validité, cliquez sur Créer et
Réinitialiser ou redémarrez l’imprimante manuellement.

Le certificat auto-signé est généré. Rechargez la page et cliquez sur SSL/TLS
dans la section Sécurité pour vous assurer que le **Certificat auto-signé**
est correctement sélectionné dans la section Certificat du serveur.

La procédure d’exportation dépend fortement du système d’exploitation et du
navigateur. Commencez par accéder aux paramètres de votre imprimante ePOS sur
votre navigateur web en allant à son adresse IP (par ex.
`https://192.168.1.25`). Forcez ensuite la connexion comme il est expliqué
dans l’onglet **Générer un certificat autosigné**.

Si vous utilisez **Google Chrome** ,

  1. cliquez sur Non sécurisé à côté de la barre de recherche et Certificat non valide ;

![Bouton dans Google Chrome signalant que la connexion à l'imprimante n'est
pas sécurisée](../../../../_images/browser-warning.png)

  2. allez à l’onglet Détails et cliquez sur Exporter ;

  3. ajoutez `.crt` à la fin du nom de fichier pour vous assurer qu’il a l’extension correcte ;

  4. sélectionnez ASCII encodé en Base64, certificat unique, en bas de la fenêtre contextuelle ;

  5. enregistrez et le certificat est exporté.

Avertissement

Assurez-vous que le certificat se termine par l’extension `.crt`. Sinon,
certains navigateurs pourraient ne pas trouver le fichier pendant le processus
d’importation.

Si vous utilisez **Mozilla Firefox** ,

  1. cliquez sur l’icône en forme de **cadenas** à gauche de la barre d’adresse ;

  2. allez à Connexion non sécurisée ‣ Plus d’informations ‣ Onglet Sécurité ‣ Afficher le certificat ;

![Le bouton dans Mozilla Firefox signalant que la connexion n'est pas
sécurisée](../../../../_images/mozilla-not-secure.png)

  3. descendez jusqu’à la section Divers ;

  4. cliquez sur PEM (cert) dans la section Télécharger ;

  5. enregistrez et le certificat est exporté.

Pour importer un certificat SSL sur un appareil Android, il faut d’abord le
créer et l’exporter à partir d’un ordinateur. Ensuite, transférez le fichier
`.crt` vers l’appareil par email, Bluetooth ou USB. Une fois le fichier sur
l’appareil,

  1. ouvrez les paramètres et recherchez le `certificat` ;

  2. cliquez sur Certificate AC (Installer à partir du stockage de l’appareil) ;

  3. sélectionnez le fichier de certificat pour l’installer sur l’appareil.

Note

Les étapes spécifiques pour l’installation d’un certificat peuvent dépendre
fortement de la version d’Android et du fabriquant de l’appareil.

Pour exporter un certificat SSL sur un appareil iOS, il faut d’abord le créer
et l’exporter à partir d’un ordinateur. Ensuite, transférez le fichier `.crt`
vers l’appareil par email, Bluetooth ou n’importe quel service de partage de
fichiers.

Le téléchargement de ce fichier ouvre une fenêtre contextuelle
d’avertissement. Cliquez sur Autoriser pour télécharger le profil de
configuration et fermez la deuxième fenêtre contextuelle. Ensuite,

  1. allez à l’application **Paramètres** sur l’appareil iOS ;

  2. cliquez sur Profil téléchargé dans la boîte de détails de l’utilisateur ;

  3. trouvez le fichier `.crt` téléchargé et sélectionnez-le ;

  4. cliquez sur Installer en haut à droite de l’écran ;

  5. si un mot de passe est configuré sur l’appareil, saisissez le mot de passe ;

  6. cliquez sur Installer en haut à droite de l’écran d’avertissement du certificat et de la fenêtre contextuelle ;

  7. cliquez sur Terminé.

![../../../../_images/ssl-ios-verified.png](../../../../_images/ssl-ios-
verified.png)

Le certificat est installé, mais il doit toujours être authentifié. Pour ce
faire,

  1. allez aux Paramètres ‣ Général ‣ À propos > Paramètres de confiance du certificat ;

  2. activez le certificat installé à l’aide du **bouton coulissant** ;

  3. cliquez sur Continuer dans la fenêtre contextuelle.

Important

  * Si vous devez exporter des certificats SSL à partir d’un système d’exploitation ou d’un navigateur qui n’a pas été mentionné, recherchez `exporter certificat SSL` \+ `le nom de votre navigateur ou système d'exploitation` dans votre moteur de recherche préféré.

  * De même, pour importer des certificats SSL à partir d’un système d’exploitation ou d’un navigateur, recherchez `importer certificat SSL autorité racine` \+ `le nom de votre navigateur ou système d'opération` dans votre moteur de recherche préféré.

## Vérifiez si le certificat est correctement importé

Pour confirmer que la connexion de votre imprimante est sécurisée, connectez-
vous à son adresse IP en utilisant HTTPS. Par exemple, allez à
`https://192.168.1.25` dans votre navigateur. Si le certificat SSL a été
correctement appliqué, vous ne devriez plus voir de page d’avertissement et la
barre d’adresse devrait afficher une icône de cadenas, indiquant que la
connexion est sécurisée.

