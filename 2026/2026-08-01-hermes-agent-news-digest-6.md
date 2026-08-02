# Hermes Agent Quotidien #6

Premier plugin officiel Hermes Desktop avec SDK ouvert, et DeepSeek V4 Flash disponible.

## Plugin Hermes Desktop : SDK ouvert et premier plugin Kanban

Nous Research a annoncé le 31 juillet le premier plugin officiel pour Hermes Desktop : Kanban, un tableau de bord kanban natif, directement accessible depuis l'interface desktop.

L'annonce principale n'est pas Kanban en soi, mais le SDK qui le rend possible. Hermes Desktop peut maintenant être étendu comme VS Code, avec un système de plugins qui utilise la même interface de contribution qu'Hermes core, pas une couche séparée. Un plugin peut ajouter :

- des pages et panneaux complets
- une navigation sidebar
- des actions dans la palette de commandes
- des raccourcis clavier rebindables
- des thèmes
- des contrôles pour le Composer
- des actions dans la barre d'état
- des événements Gateway en direct
- ses propres endpoints backend

Le déploiement est immédiat : déposer un fichier ESM dans le dossier plugins, le sauvegarder, et Hermes le hot-reload en quelques secondes. Aucun clone de dépôt, aucune reconstruction de Desktop, aucune modification de l'application. Le Kanban est la première preuve de ce que le SDK permet de faire.

Brooklyn (@imbabybrooklyn) a démontré l'activation : Settings -> Plugins -> Enable Kanban. Luke (@iamlukethedev) a détaillé le fonctionnement du SDK dans son thread.

> Sources : [@NousResearch, 31 juillet 2026](https://x.com/NousResearch/status/2083257053338898730) - [@iamlukethedev relayé par @Teknium, 31 juillet 2026](https://x.com/iamlukethedev/status/2083260429426446662) - [@imbabybrooklyn relayé par @Teknium, 31 juillet 2026](https://x.com/imbabybrooklyn/status/2083260137301487939)

## DeepSeek V4 Flash disponible dans Hermes Agent

Teknium a annoncé le 31 juillet que DeepSeek V4 Flash est maintenant accessible dans Hermes Agent via Nous Portal et OpenRouter.

DeepSeek a publié la version officielle de l'API V4 Flash en beta publique le même jour, avec des capacités agentiques massivement améliorées par rapport à la preview V4 Pro. Le modèle supporte nativement le format Responses API et est entièrement adapté pour Codex.

Les premiers retours sont parlants : elshayib_ a rapporté avoir lancé une tâche avec un seul prompt dans Hermes Agent, terminée en 32 minutes pour 0,07 $ de coût total. Teknium commente que le modèle est assez puissant pour tourner sur deux Sparks NVIDIA. Brandon (@limchinhan) l'a testé avec Hermes sur une analyse de pattern Codex et le qualifie de très impressionnant, 100 fois meilleur que la preview.

Un problème de disponibilité des providers sur Nous Portal (qui ne relaye pas les modèles s'entraînant sur les données utilisateur) a été signalé puis résolu dans la journée. Plus de providers sont maintenant disponibles.

> Sources : [@Teknium, 31 juillet 2026](https://x.com/Teknium/status/2083232881342902562) - [@Teknium, 1er août 2026](https://x.com/Teknium/status/2083412067630055644) - [@elshayib_ relayé par @Teknium, 1er août 2026](https://x.com/elshayib_/status/2083243725447147595)

## Sources

- [@NousResearch - Plugin Kanban, 31 juillet 2026](https://x.com/NousResearch/status/2083257053338898730)
- [@iamlukethedev relayé par @Teknium - SDK plugins, 31 juillet 2026](https://x.com/iamlukethedev/status/2083260429426446662)
- [@imbabybrooklyn relayé par @Teknium - Activation Kanban, 31 juillet 2026](https://x.com/imbabybrooklyn/status/2083260137301487939)
- [@Teknium - DeepSeek V4 Flash, 31 juillet 2026](https://x.com/Teknium/status/2083232881342902562)
- [@Teknium - Plus de providers, 1er août 2026](https://x.com/Teknium/status/2083412067630055644)
- [@elshayib_ relayé par @Teknium - Tâche à 0,07 $, 1er août 2026](https://x.com/elshayib_/status/2083243725447147595)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
