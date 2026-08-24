# Hermes Agent Quotidien #29

Hermes permet de confier la vérification d'un travail à un modèle séparé via /review, witcheer détaille dans son cinquante-troisième numéro les quatre fichiers markdown qui façonnent un agent, et un membre de la communauté publie son playbook d'orchestration où un Hermes contrôle seul une branche main entouré d'une flotte de CLIs.

## Un modèle auxiliaire dédié à /review

Teknium a annoncé qu'on peut désormais donner à Hermes un modèle auxiliaire pour la relecture. Quand on lance /review, l'agent prend les dix derniers messages, ainsi que tout prompt ajouté après la commande, et la vérification est ensuite confiée à un sous-agent qui se sert de ce modèle. Cela répond à un besoin que Teknium ressent depuis un moment : il utilise Fable en premier, mais d'autres modèles de raisonnement voient ce que celui-ci peut manquer, et il voulait ce flux dans sa forme la plus simple.

Il précise que Hermes exécute cette vérification dans la session en cours, ce qui en fait le prix le plus bas possible : les tokens de la session sont déjà en cache.

> Sources : [@Teknium, le modèle auxiliaire de /review, 24 août 2026](https://x.com/Teknium/status/2091686997228478653) et [@Teknium, vérification bon marché en session, 24 août 2026](https://x.com/Teknium/status/2091731971672273266)

## Hermes Wingtips #53 : les quatre fichiers qui façonnent un agent

Le cinquante-troisième numéro de la série de witcheer passe en revue les quatre fichiers destinés à guider un Hermes, et le rôle de chacun. SOUL.md et AGENTS.md sont du ressort de l'utilisateur : le premier vit dans ~/.hermes/ et porte ce que l'agent est, la persona, le ton, pour qu'il reste identique partout, sur tous les projets et tous les canaux ; le second vit dans chaque dossier de projet et porte ses règles de structure et de conventions, si bien que les règles suivent le projet et non l'agent.

MEMORY.md et USER.md sont écrits par l'agent lui-même : l'un consigne ce qu'il a appris sur son environnement et ses leçons, pour cesser de redécouvrir les mêmes choses à chaque session, l'autre porte qui est l'utilisateur, ses préférences et son style de réponse. Witcheer résume : partout signifie SOUL.md, un projet signifie AGENTS.md, et la paire mémoire se prend en charge.

> Source : [@witcheer, Hermes Wingtips #53, les quatre fichiers, 24 août 2026](https://x.com/witcheer/status/2091778310783070649)

## Orchestration : un Hermes en contrôleur de branche

witcheer rapporte qu'un membre de la communauté fait tourner son Hermes Agent depuis trois mois comme le seul contrôleur autorisé à toucher sa branche main, autour d'une flotte de CLIs de code délégués au travail d'implémentation. Puisque les auto-évaluations des travailleurs ne valent pas preuve, le conducteur Hermes relance lui-même les tests avant tout merge, et chaque couloir travaille dans son propre worktree pour que deux tâches ne se réécrivent pas. Il a rendu le playbook entier open source.

Le dépôt correspondant compile ces schémas d'orchestration mis en production, issus de 18 tableaux kanban et plus de 250 cartes terminées. Hermes y tient le rôle intégrateur qui découpe, distribue, vérifie et intègre, tandis que des CLIs externes (Claude Code, OpenCode, Codex, MiMo, agy) exécutent le travail dans des worktrees isolés. La règle d'or est que l'orchestrateur n'implémente jamais et se contente de router ; c'est lui qui relance les tests des travailleurs et clôture une carte avec des preuves vérifiables plutôt qu'avec une simple affirmation.

> Sources : [@witcheer, une Hermes conductor de main branch, 24 août 2026](https://x.com/witcheer/status/2091814372603535791) et [forcewake/hermes-conductor, dépôt GitHub, 23 août 2026](https://github.com/forcewake/hermes-conductor)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).