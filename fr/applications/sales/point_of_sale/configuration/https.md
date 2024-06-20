# Connexion sécurisée (HTTPS)

If **Direct Devices** is enabled in a Point of Sale settings (for example, if
you use an [ePos printer](epos_printers.html)), HTTP becomes the default
protocol.

## Forcer votre Point de vente à utiliser une connexion sécurisée (HTTPS)

Ajoutez une nouvelle **clé** dans les **Paramètres système** pour forcer votre
Point de vente à utiliser une connexion sécurisée avec le protocole HTTPS.

Pour ce faire, activez le [mode
développeur](../../../general/developer_mode.html#developer-mode), allez à
Paramètres ‣ Technique ‣ Paramètres ‣ Paramètres système, puis créez un
nouveau paramètre, ajoutez les valeurs suivantes et cliquez sur _Enregistrer_.

  * **Clé** : `point_of_sale.enforce_https`

  * **Valeur** : `True`

Pour plus d'infos

  * [Certificat auto-signé pour les imprimantes ePOS](epos_ssc.html)

