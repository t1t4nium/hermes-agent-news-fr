# Hermes Agent Quotidien #36

Cette édition revient sur la chaîne de secours de fournisseurs de modèles présentée dans le cinquante-neuvième numéro des Wingtips, sur un retour d'usage qui aligne Hermes Agent avec un modèle local Qwen 3.8-27B sur le niveau d'Opus en tâches de codage, et sur la création de voxels propulsée par GLM 5.3 Flash dans le harnais Hermes.

## Wingtips #59 : une chaîne de secours pour les fournisseurs de modèles

Le cinquante-neuvième numéro de la série de witcheer porte sur le fallback de fournisseurs : Hermes Agent peut porter une chaîne de secours, des paires fournisseur-modèle de rechange, vers lesquelles il bascule automatiquement quand le modèle principal subit une limite de débit, une erreur serveur ou un échec d'authentification. La commande `hermes fallback` ouvre le gestionnaire interactif.

La documentation précise le mécanisme. `hermes fallback` réutilise le sélecteur de fournisseur de `hermes model`, avec les mêmes listes et validations, et propose les sous-commandes `add`, `list`, `remove` et `clear`. La configuration est stockée dans la liste `fallback_providers` de `config.yaml`, chaque entrée portant un `provider` et un `model`, l'ancienne clé unique `fallback_model` restant honorée pour la compatibilité. Le basculement se déclenche après épuisement des tentatives sur une limite de débit (429) ou une erreur serveur (500, 502, 503), et immédiatement sur un échec d'authentification (401, 403). Le déclenchement est par tour, pas par session : chaque nouveau message repart sur le modèle principal, et au plus une bascule a lieu à l'intérieur d'un tour pour éviter les boucles de failover. Les sessions CLI, la passerelle de messagerie, la délégation de sous-agents et les tâches cron héritent de la chaîne configurée.

> Sources : [@witcheer, Hermes Wingtips #59, une limite de débit ne doit pas arrêter votre session, 31 août 2026](https://x.com/witcheer/status/2094362454390129137) et [Fallback Providers, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)

## Hermes Agent et un Qwen 3.8-27B local au niveau d'Opus

HealthRanger relate son expérience de Hermes Agent couplé à un Qwen 3.8-27B exécuté en local. Sur l'ensemble des tâches de codage qu'il lui a confiées, le modèle ne lui en a fait échouer aucune, et il a poussé la complexité pour tenter de le faire tomber. Selon lui, le résultat est quasi parfait et comparable à Opus. Teknium partage l'enthousiasme en citant le message.

> Sources : [@HealthRanger, Hermes Agent + Qwen 3.8-27B local, une bête, 31 août 2026](https://x.com/HealthRanger/status/2094216564723564603) et [@Teknium, relance du message de HealthRanger, 31 août 2026](https://x.com/Teknium/status/2094321652977025281)

## Des voxels en neuf minutes avec GLM 5.3 Flash dans Hermes

Tech2Wild montre une création de voxels réalisée en neuf minutes avec GLM 5.3 Flash dans Hermes Agent, qu'il présente comme l'une de ses meilleures, en particulier dans le harnais Hermes. Teknium salue le résultat et envisage en plaisantant de peupler ce type d'environnement avec des agents Hermes pour en faire une vraie société.

> Sources : [@Tech2Wild, GLM 5.3 Flash a créé ceci en neuf minutes dans Hermes, 30 août 2026](https://x.com/Tech2Wild/status/2093900681014882754) et [@Teknium, GLM 5.3 Flash pour créer des voxels, 30 août 2026](https://x.com/Teknium/status/2094023729873596639)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
