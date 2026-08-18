# Hermes Agent Quotidien #23

Bot Mode sort officiellement dans Hermes Desktop, la release v0.20.4 consolide 74 PRs, et une fonctionnalité de widgets natifs permet de rendre des graphiques en direct dans le chat.

## Bot Mode sort officiellement dans Hermes Desktop

Le 17 août, Nous Research a annoncé la sortie de Bot Mode pour Hermes Agent Desktop : "Introducing Bot Mode for Hermes Desktop. Your agent profiles become a series of named Bots. Each Bot has its own role, model, memory, skills and profile picture; Bots can use any model and even communicate with each other. Build a specialist Bot once to use it forever."

Teknium a précisé le positionnement : Bot Mode est une alternative au mode sessions, où l'on a une conversation par profil d'agent, ou "bot". Chaque bot reçoit des tâches, une description, une photo de profil, et communique avec les autres bots. Ils conservent leur propre mémoire, leurs skills, leurs outils et leurs connexions externes.

Cette sortie succède à la bêta publique du 13 août (édition #19) et à la phase de packaging annoncée le 16 août (édition #22). La fonctionnalité est désormais intégrée à l'application desktop principale.

Tonbi a accompagné le lancement d'une démo de groupe de chats : plusieurs bots spécialisés se partagent un grand projet de jeu vidéo en s'appuyant sur leurs expériences respectives. L'un signale son projet terminé et propose son aide, un autre juge qu'il correspond au travail front-end de la phase suivante, un troisième suggère le ticket exact à prendre, et le bot retenu lit les documents liés avant de demander l'approbation pour s'en charger.

> Sources : [@NousResearch, Bot Mode pour Desktop, 17 août 2026](https://x.com/NousResearch/status/2089429432612147572) - [@Teknium, Bot Mode, 17 août 2026](https://x.com/Teknium/status/2089430781668303090) - [@tonbistudio, démo groupes de bots, 17 août 2026](https://x.com/tonbistudio/status/2089226021749030999)

## v0.20.4 : un tag qui consolide 74 PRs

Le 18 août, Hermes Agent a publié v0.20.4 (v2026.8.18). C'est une release patch qui rassemble environ 74 pull requests fusionnées depuis v0.20.3 (taggé le 17 août), soit environ 146 commits sur 265 fichiers (+21 697 / −2 217).

Les changements couvrent plusieurs surfaces :

- Desktop : travail sur la surface verre/translucidité (verre mat, sélecteur de givre, pré-sélection macOS).
- Desktop : barre latérale à onglets SESSIONS|BOTS avec masquage/affichage par bot.
- Bot Mode : corrections des groupes de chats (tours de membres longs, rendu Markdown, routage entre machines).
- Skills : scan d'avis NVIDIA SkillEvaluator Tier 1 à l'installation (contrôles de licence et de sécurité).
- Cron : durcissement de l'envoi de médias (délai configurable, pièces jointes en exécution manuelle, signalement des déclenchements manqués).
- Base de données : corrections du fil event-loop et des contentions SessionDB.
- CLI : honnêteté de `hermes update` sur les branches en attente.
- Kanban : notifications natives du système d'exploitation.

Les notes de release détaillées et le crédit complet des contributeurs arriveront avec v0.21.0, qui documentera tout depuis v0.20.0.

> Source : [Release Hermes Agent v0.20.4](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.18)

## Des widgets natifs rendus dans le chat

Le 17 août, imbabybrooklyn a montré une fonctionnalité de widgets natifs générés dans Hermes Agent. Le principe : une skill peut rendre un composant d'interface en ligne, directement dans la conversation. L'exemple donné est une skill `/get-price btc` qui affiche un graphique de prix en direct dans le chat, au lieu d'un texte.

La démonstration illustre la frontière entre commande et interface : la sortie d'une skill n'est pas limitée à du texte, elle peut produire un widget interactif embarqué.

> Source : [@imbabybrooklyn, widgets natifs, 17 août 2026](https://x.com/imbabybrooklyn/status/2089453432918753626)

## Sources

- [@NousResearch - Bot Mode pour Desktop, 17 août 2026](https://x.com/NousResearch/status/2089429432612147572)
- [@Teknium - Bot Mode, 17 août 2026](https://x.com/Teknium/status/2089430781668303090)
- [@tonbistudio - Démo groupes de bots, 17 août 2026](https://x.com/tonbistudio/status/2089226021749030999)
- [Release Hermes Agent v0.20.4](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.18)
- [@imbabybrooklyn - Widgets natifs, 17 août 2026](https://x.com/imbabybrooklyn/status/2089453432918753626)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
