# Hermes Agent Quotidien #34

Cette édition revient sur le nouvel épisode des Wingtips consacré à `delegate_task`, sur un plugin autonome pour BackSearch signé par Teknium, sur le modèle Ling-3.0-flash rendu gratuit dans Nous Portal, sur la commande `/btw` pour les tâches en parallèle et sur un portail de recherche privé propulsé par un Hermes headless.

## Hermes Wingtips #57 : la délégation avec `delegate_task`

Le cinquante-septième numéro de la série de witcheer porte sur `delegate_task`, l'outil intégré qui remplace le montage à la main d'équipes multi-agents. Au lieu de plusieurs profils, de dossiers partagés et d'un coordinateur qui finit par tout faire lui-même, `delegate_task` condense tout ce motif en une seule commande.

La documentation d'Hermes précise le fonctionnement : `delegate_task` lance des sous-agents avec un contexte isolé, des ensembles d'outils restreints et leurs propres sessions de terminal. Par défaut, trois sous-agents s'exécutent en parallèle, seuil configurable. L'agent parent peut être préconfiguré pour que la délégation ait accès au web, au terminal ou aux fichiers avant le démarrage de la conversation.

> Sources : [@witcheer, Hermes Wingtips #57, delegate_task, 29 août 2026](https://x.com/witcheer/status/2093591294740168760) et [Delegation & Parallel Work, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns)

## Un plugin Hermes pour BackSearch

Teknium a publié un plugin autonome qui apporte BackSearch à Hermes Agent. BackSearch est un SaaS proche d'une wayback machine, pensé pour les agents : chaque requête porte une date `as_of`, la recherche ne renvoie que des documents crawlé à cette date ou avant, et la récupération restitue le texte tel qu'archivé à ce moment-là.

Le plugin enregistre deux outils, `backsearch` et `backfetch`, tous deux conditionnés à la présence d'une clé `OPENREWARD_API_KEY`, sans laquelle ils n'apparaissent pas dans le schéma de modèles. L'archive de prévisualisation couvre les domaines d'actualité de décembre 2025 à juillet 2026. Initialement développé dans le PR #71207 de Hermes Agent, le plugin a été extrait dans un dépôt séparé, conformément à la politique qui veut que les intégrations de services tiers vivent dans des plugins plutôt que dans le cœur.

> Sources : [@Teknium, plugin Hermes pour BackSearch, 29 août 2026](https://x.com/Teknium/status/2093693127500648752) et [hermes-plugin-backsearch, dépôt GitHub](https://github.com/NousResearch/hermes-plugin-backsearch)

## Ling-3.0-flash gratuit dans Nous Portal

witcheer annonce un nouveau modèle gratuit dans Nous Portal : Ling-3.0-flash, le modèle MoE d'Ant Group via AntLingAGI. Il totalise 124 milliards de paramètres dont 5,1 milliards activés par jeton, un format rapide à exécuter et pensé pour les workloads d'agents : codage, recherche, recherche documentaire et usage d'outils.

> Sources : [@witcheer, nouveau modèle gratuit dans Nous Portal, 28 août 2026](https://x.com/witcheer/status/2093434928478224885) et [@yeahfortommy, Ling-3.0-flash gratuit dans Nous Portal, 28 août 2026](https://x.com/yeahfortommy/status/2093434483793866931)

## La commande `/btw` pour les tâches en parallèle

iamlukethedev met en avant `/btw`, une commande peu connue d'Hermes. Quand l'agent est au milieu d'une tâche et qu'un besoin complètement différent surgit, lire un autre fichier, tirer de la documentation, revoir des commits récents ou lancer une vérification de sécurité, `/btw` permet de le faire sans interrompre le travail en cours ni surveiller une autre fenêtre. Teknium relance la question à sa communauté en demandant qui utilise `/btw`.

> Sources : [@iamlukethedev, Hermes hidden gem, /btw, 29 août 2026](https://x.com/iamlukethedev/status/2093660966093541409) et [@Teknium, do you use /btw, 29 août 2026](https://x.com/Teknium/status/2093686619081679120)

## Un portail de recherche privé propulsé par un Hermes headless

witcheer relate la création, par un membre de la communauté, d'un portail de recherche entièrement privé dont le moteur est un Hermes Agent headless. Une requête est tapée dans une interface web locale et, derrière, une exécution Hermes déroule toute la passe de recherche : recherche, récupération et crawl à travers un serveur MCP.

> Source : [@witcheer, portail de recherche privé propulsé par un Hermes headless, 29 août 2026](https://x.com/witcheer/status/2093627322700005819)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
