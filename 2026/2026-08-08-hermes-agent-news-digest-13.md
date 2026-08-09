# Hermes Agent Quotidien #13

Les plugins portables standard arrivent dans Hermes Agent, la commande /learn ingère des livres entiers en skills, le navigateur intégré du desktop fonctionne désormais avec la passerelle distante, et un utilisateur a conçu un jeu complet à l'intérieur de l'agent.

## Les plugins portables standard : Hermes lit les paquets Agent Plugins v1

Le 7 août, Teknium a annoncé que Hermes Agent supporte désormais le standard de plugins portables adopté par plusieurs grands acteurs de l'IA. Un dépôt compatible s'installe via le flux de plugins habituel, et Hermes charge ses skills namespacées en lecture seule ainsi que ses serveurs MCP stdio.

Les paquets s'installent désactivés et ne s'activent qu'après un accord explicite. Avant chargement, Hermes valide le manifeste, les métadonnées des skills, les chemins, les liens symboliques et la configuration MCP.

> "Agent plugins should not be trapped inside one platform."
>
> "Portable plugins give you compatibility. Native Hermes plugins give you the full platform, including custom tools, slash commands, hooks, Desktop, Dashboard, and deeper APIs."

Witcheer a complété le tableau le 8 août : les skills du paquet remontent dans le registre de skills normal, les serveurs MCP passent par le runtime MCP existant, et un manifeste natif prend toujours le dessus si le paquet en embarque un. Pour les commandes slash, les plugins GUI, le dashboard et les skins, l'API native reste la surface la plus grande.

> Source : [@Teknium, 7 août 2026](https://x.com/Teknium/status/2085780613005504687) - [@witcheer, 8 août 2026](https://x.com/witcheer/status/2086108907685003306) - [Documentation des plugins portables](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#portable-agent-plugins-v1-packages)

## /learn ingère des livres entiers en skills techniques

Le 7 août, Teknium a annoncé que la commande /learn intègre désormais le travail du dépôt book-to-skill. Hermes Agent peut ingérer un livre complet, PDF ou autre, pour en tirer des skills techniques détaillées.

> "Integrated the work of book-to-skill repo into our /learn command, and now Hermes Agent can ingest full books to create comprehensive detailed technical skills! Just /learn and point it to any pdf or book you have!"

Le dépôt source est github.com/virgiliojr94/book-to-skill. Un premier retour d'usage est arrivé dès le 8 août : @b3pl33 a nourri un agent spécialisé crochet avec vingt livres open-source dans un dossier, puis a laissé l'agent Hermes par défaut orchestrer le tout, pour un projet de patron de sac à main.

> Sources : [@Teknium, 7 août 2026](https://x.com/Teknium/status/2085761587550519420) - [@b3pl33, 8 août 2026](https://x.com/b3pl33/status/2086041266421424238)

## Le navigateur intégré fonctionne aussi avec la passerelle distante

L'édition #11 signalait que le navigateur intégré de Hermes Desktop restait limité à l'application locale et ne passait pas par une passerelle distante. La limitation a été levée : Brooklyn! (@imbabybrooklyn) a confirmé le 7 août que le navigateur fonctionne désormais avec la passerelle distante.

> "So if you were previously having issues with this when using remote gateway (it was only for local), @imbabybrooklyn confirmed it now works with remote gateway too!"

Tonbi a relayé la confirmation dans sa démonstration des usages du navigateur, relayée à son tour par Teknium : défiler un fil X et demander un résumé, suivre un tutoriel vidéo et en faire extraire le transcript ou implémenter les concepts, ou ouvrir des liens de recherche et les analyser ensemble.

> Sources : [@tonbistudio relayé par @Teknium, 7 août 2026](https://x.com/tonbistudio/status/2085600678156882389) - [@imbabybrooklyn, 7 août 2026](https://x.com/imbabybrooklyn/status/2085576851947221338)

## Un jeu complet conçu à l'intérieur de Hermes Agent

@Da7_Tech a montré le 7 août un jeu dont les fonds ont été générés avec MiniMax M3, tout le reste, y compris la conception complète du jeu, ayant été produit avec DeepSeek Flash, le tout à l'intérieur de Hermes Agent. Nous Research a relayé le post en soulignant que tout a été fait dans l'agent.

> Source : [@Da7_Tech relayé par @NousResearch, 7 août 2026](https://x.com/Da7_Tech/status/2085763279696122149)

## Sources

- [@Teknium - Plugins portables standard, 7 août 2026](https://x.com/Teknium/status/2085780613005504687)
- [@witcheer - Détails plugins portables, 8 août 2026](https://x.com/witcheer/status/2086108907685003306)
- [Documentation Hermes Agent - Plugins portables](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#portable-agent-plugins-v1-packages)
- [@Teknium - /learn et livres, 7 août 2026](https://x.com/Teknium/status/2085761587550519420)
- [@b3pl33 - Retour d'usage /learn, 8 août 2026](https://x.com/b3pl33/status/2086041266421424238)
- [@tonbistudio relayé par @Teknium - Navigateur et passerelle distante, 7 août 2026](https://x.com/tonbistudio/status/2085600678156882389)
- [@imbabybrooklyn - Works remotely now, 7 août 2026](https://x.com/imbabybrooklyn/status/2085576851947221338)
- [@Da7_Tech relayé par @NousResearch - Jeu conçu dans Hermes, 7 août 2026](https://x.com/Da7_Tech/status/2085763279696122149)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
