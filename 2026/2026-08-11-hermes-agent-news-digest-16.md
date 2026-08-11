# Hermes Agent Quotidien #16

Douze outils navigateur remplacés par un seul (Browser Use CLI 3.0), une commande `hermes journey` pour voir l'évolution de son agent, Solar Pro 4 gratuitement sur Nous Portal, Hermes Pixel Office pour visualiser ses agents dans VS Code, et un guide sur les topics Telegram face aux profils.

## Automatisation navigateur : un seul outil au lieu de douze

Le 10 août, Nous Research a annoncé que les douze outils navigateur d'Hermes sont remplacés par un seul, piloté par Browser Use CLI 3.0. Au lieu d'un schéma par outil et d'un appel par clic, l'agent écrit un script pour le flux complet.

Teknium a détaillé le mécanisme : le schéma est passé de huit outils coûteux en contexte à un seul, et l'agent conduit le navigateur via du code au lieu d'actions individuelles. Dans leurs tests internes, la consommation de tokens par tâche a baissé de 48 à 66 %, sans perte de précision.

La configuration se fait avec `browser.backend: browser-use`. Teknium a précisé que cela fonctionne pour tout le monde : navigateur local, Browserbase, headless, et tous les backends supportés sauf camofox local.

Nous Research a relayé avec un lien vers la documentation complète de l'automatisation navigateur dans Hermes.

> Sources : [@NousResearch, 10 août 2026](https://x.com/NousResearch/status/2086881660658663469) - [@Teknium, 10 août 2026](https://x.com/Teknium/status/2086881909209252209) - [@Teknium, 10 août 2026](https://x.com/Teknium/status/2086882821910782270) - [@Teknium, 10 août 2026](https://x.com/Teknium/status/2086884484818096543)

## `hermes journey` : la chronologie de votre agent

Le 11 août, witcheer a présenté une nouvelle commande CLI. `hermes journey` dessine dans le terminal une frise chronologique de toutes les compétences et mémoires accumulées par l'agent, jour par jour.

La commande montre aussi bien les skills que les souvenirs, et permet de voir à quel moment l'agent a appris quelque chose, dans quel contexte. Witcheer a illustré avec son propre agent : neuf mois de trajectoire visibles d'un coup d'œil.

> Source : [@witcheer, 11 août 2026](https://x.com/witcheer/status/2087150634654896516)

## Solar Pro 4 gratuit sur Nous Portal, plus quatre autres modèles

Le 11 août, Nous Research a annoncé que Solar Pro 4, le nouveau modèle agentique d'Upstage, est disponible gratuitement pendant une semaine exclusivement sur Nous Portal. Conçu pour les tâches multi-étapes sur de longs documents, il sait reconnaître quand il lui faut plus d'informations plutôt que d'inventer une réponse.

Witcheer a complété le tableau : un abonnement Nous Portal donne aussi accès à quatre autres modèles gratuits : Hy3, Step 3.7 Flash, Laguna S et Laguna XS. En plus de la remise de 90 % sur DeepSeek V4 Flash (prolongée) et de 20 % sur le reste du catalogue.

> Sources : [@NousResearch, 11 août 2026](https://x.com/NousResearch/status/2087197502415974634) - [@witcheer, 11 août 2026](https://x.com/witcheer/status/2087202510314303789)

## Hermes Pixel Office : visualisez vos agents dans VS Code

Le 11 août, Teknium a publié Hermes Pixel Office. Une extension VS Code (à chercher sur le marketplace sous "Hermes Pixel Office") et un plugin Hermes Agent correspondant sur GitHub permettent de voir tous ses agents Hermes travailler en direct, représentés par des personnages pixel dans un bureau virtuel.

Teknium a confectionné le tout en une seule session, et le code source est ouvert :

- Extension VS Code : github.com/teknium1/hermes-pixel-office-vscode
- Plugin Hermes Agent : github.com/teknium1/hermes-pixel-office

La communauté a accueilli l'initiative avec enthousiasme, plusieurs utilisateurs demandant une intégration directe dans Hermes Desktop ou le Kanban.

> Sources : [@Teknium, 11 août 2026](https://x.com/Teknium/status/2086975696786829471) - [@Teknium, 11 août 2026](https://x.com/Teknium/status/2086975901829632363)

## Hermes Wingtips #43 : topics Telegram ou second agent

Le 11 août, witcheer a publié le quarante-troisième numéro de sa série Hermes Wingtips. Le sujet : comment organiser plusieurs projets quand on utilise un seul bot Telegram.

Deux options existent et ne font pas la même chose :

- `/topic` : conversations parallèles dans un même DM de bot. L'agent est toujours le même, ce qu'il apprend sur un projet nourrit les autres.
- `hermes profile create <nom>` : un second agent entier, avec son propre bot et sa propre mémoire.

Witcheer recommande les topics quand les projets doivent alimenter le même cerveau, et les profils quand on a besoin de vraies barrières entre eux. Les deux peuvent tourner sur la même machine.

> Source : [@witcheer, 11 août 2026](https://x.com/witcheer/status/2087071761040896227)

## Sources

- [@NousResearch - Browser Use mode, 10 août 2026](https://x.com/NousResearch/status/2086881660658663469)
- [@Teknium - Browser Use ~60% tokens, 10 août 2026](https://x.com/Teknium/status/2086881909209252209)
- [@Teknium - Schéma + CLI, 10 août 2026](https://x.com/Teknium/status/2086882821910782270)
- [@Teknium - Works for everyone, 10 août 2026](https://x.com/Teknium/status/2086884484818096543)
- [@witcheer - hermes journey, 11 août 2026](https://x.com/witcheer/status/2087150634654896516)
- [@NousResearch - Solar Pro 4 gratuit, 11 août 2026](https://x.com/NousResearch/status/2087197502415974634)
- [@witcheer - Modèles gratuits Portal, 11 août 2026](https://x.com/witcheer/status/2087202510314303789)
- [@Teknium - Hermes Pixel Office, 11 août 2026](https://x.com/Teknium/status/2086975696786829471)
- [@Teknium - Dépôt Pixel Office, 11 août 2026](https://x.com/Teknium/status/2086975901829632363)
- [@witcheer - Wingtips #43, 11 août 2026](https://x.com/witcheer/status/2087071761040896227)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
