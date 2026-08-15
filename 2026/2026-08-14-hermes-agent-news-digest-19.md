# Hermes Agent Quotidien #19

Bot Mode officiellement lancé en bêta publique, pilotage des sous-agents en direct, Browser Use mode activé par défaut, dépôt de fichiers par glisser-déposer, et LongCat-2.0 gratuit une semaine sur Nous Portal.

## Bot Mode débarque en bêta publique

Le 13 août au soir, Teknium a officiellement lancé Bot Mode pour Hermes Agent, cette fois en bêta publique avec un plugin dédié. Bot Mode remplace le mode sessions par un mode où chaque profil d'agent devient un "bot" avec son propre historique, sa photo de profil, sa description et sa configuration. Les bots peuvent communiquer entre eux via un inbox dédié.

La bêta est accessible via le plugin disponible sur [github.com/NousResearch/Hermes-Bot-Mode](https://github.com/NousResearch/Hermes-Bot-Mode). Tonbistudio a publié une vidéo de démonstration montrant la barre latérale des bots, la création d'un nouveau bot, et l'inbox agent qui permet aux bots de s'échanger des messages. La fenêtre des cron jobs est aussi accessible par bot. Teknium prévoit d'intégrer le mode dans l'application desktop principale après la phase de test.

> Sources : [@Teknium, 13 août 2026](https://x.com/Teknium/status/2088003994904113614) - [@tonbistudio, 14 août 2026](https://x.com/tonbistudio/status/2088059838362501360) - [@witcheer, 13 août 2026](https://x.com/witcheer/status/2088028193590087994)

## Pilotage des sous-agents en temps réel

Le 13 août, Teknium a présenté une nouvelle capacité : l'agent Hermes peut maintenant diriger, arrêter et lire les transcriptions en direct de ses sous-agents. La fonction s'appuie sur les paramètres `steer`, `stop` et `list` de l'outil `delegate_task`, exploitant le mécanisme de live orchestration des enfants asynchrones. Concrètement, pendant qu'un sous-agent travaille en arrière-plan, l'agent parent peut lui envoyer une correction de trajectoire (`steer`), l'arrêter pour récupérer un résultat partiel (`stop`), ou consulter la liste des enfants actifs avec leur statut (`list`).

> Source : [@Teknium, 13 août 2026](https://x.com/Teknium/status/2087986084592709814)

## Hermes Wingtips #46 : Browser Use mode activé par défaut

Le 14 août, witcheer a publié le quarante-sixième numéro de sa série Hermes Wingtips. Le sujet : le mode Browser Use, un harness développé par l'équipe Browser Use. Contrairement à l'approche classique où l'agent pilote la page un appel d'outil par clic, l'agent écrit un script qui exécute tout le flux en une fois. Depuis la version v2026.8.13, le mode est activé par défaut. Une simple mise à jour suffit pour que les tâches web deviennent moins coûteuses, sans toucher à la configuration.

> Source : [@witcheer, 14 août 2026](https://x.com/witcheer/status/2088204444391399722)

## Déposer un fichier sur Hermes Agent

Le 14 août, witcheer a montré une fonctionnalité pratique : on peut glisser-déposer un fichier sur Hermes Agent. Le fichier devient partie de la conversation et on peut ensuite poser des questions et itérer dessus. Une vidéo démontre le geste : glisser un fichier dans l'interface, et l'agent le charge immédiatement comme contexte pour la suite de l'échange.

> Source : [@witcheer, 14 août 2026](https://x.com/witcheer/status/2088167034982932693)

## LongCat-2.0 gratuit une semaine sur Nous Portal

Le 13 août, Nous Research a annoncé que LongCat-2.0 de Meituan est gratuit sur Nous Portal pour une semaine. Le modèle est un MoE de 1,6 trillion de paramètres (environ 48B actifs par token) avec 1 million de tokens de contexte, conçu pour le codage agentique. Ses scores : 70,8 sur Terminal-Bench 2.1, 59,5 sur SWE-bench Pro, 77,3 sur SWE-bench Multilingue. L'architecture repose sur trois innovations : une attention sparse adaptée au long contexte (LSA), des experts à activation dynamique sans calcul mort (Zero-Compute Experts), et un routage par groupe de tâches (MOPD) qui aiguille chaque token vers l'expert spécialisé approprié (agent, raisonnement, interaction).

> Sources : [@NousResearch, 13 août 2026](https://x.com/NousResearch/status/2087970618167706023) - [@Teknium, 13 août 2026](https://x.com/Meituan_LongCat/status/2087943641956057322)

## v2026.8.13 : une vague de 656 PRs stabilisée

Le 13 août, le tag v2026.8.13 (v0.20.1) a été publié. Depuis v0.20.0 (3 août), ce sont 1 444 commits répartis sur 656 PRs qui ont été fusionnés, touchant 2 172 fichiers. Le patch rollup couvre le desktop, les plateformes gateway, les installateurs, le système d'outils et les catalogues de fournisseurs. 481 issues ont été fermées. Les notes de release complètes seront publiées avec v0.21.0. Mise à jour avec `hermes update`.

> Source : [Hermes Agent v0.20.1](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.13)

## Sources

- [@Teknium - Bot Mode, 13 août 2026](https://x.com/Teknium/status/2088003994904113614)
- [@tonbistudio - Démo Bot Mode, 14 août 2026](https://x.com/tonbistudio/status/2088059838362501360)
- [@witcheer - Bot Mode feedback, 13 août 2026](https://x.com/witcheer/status/2088028193590087994)
- [@Teknium - Pilotage sous-agents, 13 août 2026](https://x.com/Teknium/status/2087986084592709814)
- [@witcheer - Wingtips #46, 14 août 2026](https://x.com/witcheer/status/2088204444391399722)
- [@witcheer - Dépôt de fichiers, 14 août 2026](https://x.com/witcheer/status/2088167034982932693)
- [@NousResearch - LongCat-2.0, 13 août 2026](https://x.com/NousResearch/status/2087970618167706023)
- [Hermes Agent v0.20.1 - Release notes](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.13)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)