# Hermes Agent Quotidien #43

Cette édition revient sur la recherche web utilisable dès l'installation sans aucune clé API, sur le regroupement des soixante-cinq Wingtips en une seule page accompagnée d'un fichier destiné aux agents, sur le conseil d'usage de Fable en orchestrateur avec Astra en sous-agents, sur un bot de la communauté dont le métier est de fabriquer d'autres bots spécialisés, et sur la rétroaction des utilisateurs autour de la découverte des fonctionnalités.

## La recherche web fonctionne sans clé d'installation

witcheer a rappelé le 7 septembre qu'une installation fraîche de Hermes Agent sait chercher sur le web avant même qu'on ajoute une seule clé API. Elle détaille ce qui se passe derrière et les options disponibles.

La documentation confirme le mécanisme. Sans aucun identifiant de connexion configuré, `web_search` et `web_extract` tirent leur service d'un palier sans clé, la rotation du tourniquet : les requêtes passent en alternance sur les tiers gratuits publics de quatre fournisseurs, Exa, Parallel, Firecrawl et Keenable, ce qui répartit la charge. Une requête limitée en débit est automatiquement réessayée sur le fournisseur suivant du tourniquet, jusqu'à ce qu'un serve l'appel ou que tous soient saturés. Ce palier reste un dernier recours, strictement : tout fournisseur configuré ou toute clé présente prend toujours le dessus, et on peut le couper entièrement avec `web.keyless_fallback: false`. Le choix entre gratuit et payant se fait dans `hermes tools`, où Exa, Parallel et Keenable apparaissent chacun sur deux lignes, et se conserve dans `web.provider_tier.<nom>`.

> Sources : [@witcheer, a fresh install of Hermes Agent can search the web before you have added a single API key, 7 septembre 2026](https://x.com/witcheer/status/2096902241777004650) et [Web Search & Extract, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)

## Les soixante-cinq Wingtips rassemblées sur une page

witcheer a publié le 7 septembre l'ensemble de sa série Hermes Wingtips au même endroit : une page qui réunit les soixante-cinq conseils testés, du numéro un au numéro soixante-cinq, et, à côté, un fichier unique pensé pour être pointé vers un agent.

La page, hébergée sur son dépôt hermes-recipes, se lit comme la série et présente un conseil à la fois, du plus récent au plus ancien ; chaque entrée reprend le texte publié sur X tel quel, et les cartes restent sur les publications d'origine. Pour les agents, `llms.txt` contient la même série dans un seul fichier, régénéré à partir des sources à chaque nouveau conseil. La collection couvre des sujets allant de `hermes sessions import`, le conseil numéro soixante-cinq, jusqu'à l'installation d'un agent Hermes dans un groupe Telegram, en passant par la compression de contexte, les fichiers SOUL.md, AGENTS.md, MEMORY.md et USER.md, ou la délégation de tâches.

> Sources : [@witcheer, I put every Hermes Wingtips post on one page, 7 septembre 2026](https://x.com/witcheer/status/2096942342901039582) et [Hermes Wingtips, hermes-recipes](https://notwitcheer.github.io/hermes-recipes/wingtips/)

## Fable en orchestrateur, Astra en sous-agents

Teknium a relayé le 7 septembre un conseil d'usage qu'il valide : utiliser Fable comme orchestrateur et Astra comme sous-agents chargés de l'implémentation. Il raconte que, sur sa propre session de refactorisation, Astra, après avoir épuisé toutes sortes d'orchestrations de sous-agents, a regardé sa session et lui a répondu de laisser Fable orchestrer.

L'anecdote illustre une distribution des rôles : le modèle d'orchestration pilote le découpage et la coordination, tandis que les modèles d'implémentation exécutent le travail délégué. Elle prolonge la mise en avant récente, par le même compte, des gains d'efficacité en jetons réalisés dans Hermes Agent ces dernières semaines.

> Sources : [@Teknium, Whoever said to use Fable as an orchestrator and Astra as the subagents for implementation was right, 7 septembre 2026](https://x.com/Teknium/status/2096931570498327003)

## Un bot dont le métier est de fabriquer d'autres bots

witcheer a mis en avant le 6 septembre un membre de la communauté qui a construit un bot dont l'unique rôle est de créer d'autres bots spécialisés. Pour elle, un nouveau bot devrait être plus qu'un profil copié auquel on colle un fichier de personnalité.

Le botmaker fonctionne comme un entretien d'embauche : il interroge sur la tâche visée, rédige le fichier SOUL du nouveau bot pour validation, puis prépare son agencement. L'approche revient à donner naissance à des agents dont la personnalité est déduite du poste à tenir plutôt que bricolée à la main, un usage communautaire du mode Bot de Hermes Agent.

> Sources : [@witcheer, a Hermes Agent community member built a bot whose only job is making other specialist bots, 6 septembre 2026](https://x.com/witcheer/status/2096524795839996181)

## Rendre les fonctionnalités de Hermes plus faciles à trouver

witcheer s'est attelé le 7 septembre aux réponses à sa question sur la découverte des fonctionnalités, après avoir reçu 389 réponses. Le retour lui paraît clair, et l'équipe compte s'en servir pour rendre les fonctionnalités de Hermes plus faciles à trouver depuis l'intérieur de l'agent.

Parmi les attentes exprimées, les utilisateurs veulent que l'agent remarque la tâche en cours plutôt que de les laisser chercher l'outil adapté dans des menus. La démarche s'inscrit dans une série d'initiatives communautaires de witcheer autour de la prise en main, dont la collection des Wingtips couverte plus haut fait partie.

> Sources : [@witcheer, I went through the answers on my feature-discovery question, 7 septembre 2026](https://x.com/witcheer/status/2096860855291781161)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
