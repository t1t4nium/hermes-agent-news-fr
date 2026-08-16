# Hermes Agent Quotidien #20

/loop arrive dans Hermes Agent, Bot Mode se prépare pour le desktop, la surface plugin est documentée en détail, et une campagne de phishing vise les contributeurs.

## /loop : une boucle qui vit dans la session

Le 14 août, Hermes Agent s'est doté d'une nouvelle commande slash : `/loop`. Le principe : `/loop 5m <prompt>` réexécute le prompt toutes les 5 minutes dans la même session. Si on laisse l'intervalle vide, Hermes s'auto-régule : il vérifie souvent au début, puis espace les itérations tant que rien ne change.

La valeur ajoutée par rapport à un cronjob classique : la boucle vit dans la session, avec tout le contexte de l'échange en cours. L'agent peut donc décider lui-même d'arrêter la boucle quand le job est terminé, via `--times N`, `--until <condition>`, ou en laissant l'agent juger. witcheer a illustré les cas d'usage : surveiller un déploiement ou un CI, lancer les tests et corriger les échecs jusqu'à ce qu'ils passent, ou garder un heartbeat sur un job long en continuant a faire autre chose dans la même session.

La commande fonctionne dans le CLI, le desktop et tous les canaux de messagerie. Teknium a précisé que c'est l'équivalent Hermes du `/loop` de Claude Code. La documentation est en ligne : [hermes-agent.nousresearch.com/docs/user-guide/features/loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops).

> Sources : [@NousResearch, 14 août 2026](https://x.com/NousResearch/status/2088367838977237029) - [@Teknium, 14 août 2026](https://x.com/Teknium/status/2088368313974047165) - [@witcheer, 15 août 2026](https://x.com/witcheer/status/2088491869000835146)

## Bot Mode : préparation de la release desktop

Teknium a confirmé le 15 août qu'il enchaîne une série d'optimisations, de corrections de bugs et d'améliorations de la qualité de vie sur l'application desktop GUI pour préparer la release de Bot Mode, probablement lundi (17 août). Il a également montré une nouveauté dans l'UX : pendant la création d'un nouveau bot, l'interface permet de parcourir le skills hub en mode avancé pour ajouter directement n'importe quelle skill au bot.

Un retour utilisateur d'EddieVi confirme l'intérêt : son bot de recherche Rick a reçu un sujet, est parti chercher l'information, a cité ses sources, et a renvoyé la réponse sous forme de message. Sa description : "Mes agents ressemblent à un équipage maintenant, pas à un fichier de config."

> Sources : [@Teknium, 15 août 2026](https://x.com/Teknium/status/2088579906217345228) - [@Teknium, 15 août 2026](https://x.com/Teknium/status/2088488103380205907) - [@Teknium, 14 août 2026](https://x.com/Teknium/status/2088328581953032238) - [@EddieVi35539602, 15 août 2026](https://x.com/EddieVi35539602/status/2088449423210656109)

## Expansion de la surface plugin : les détails

Le 13 août, Teknium avait annoncé une extension massive de la surface plugin d'Hermes Agent via le tracking issue [#64182](https://github.com/NousResearch/hermes-agent/issues/64182#issuecomment-5275487630). witcheer en a détaillé les intégrations principales le même jour :

- Les plugins peuvent intercepter le flux LLM en direct et les événements gateway au moment où ils se produisent.
- Un bus d'événements permet aux plugins de réagir les uns aux autres.
- Un système de déclaration de capacités avec consentement à l'installation : les surfaces de sécurité sont désactivées par défaut.
- Des plugin packs et un index de plugins consultable.
- Un scaffold et un Plugin Doctor pour les développeurs de plugins.

Toutes ces additions sont cumulatives : les anciens plugins continuent de fonctionner sans modification.

> Sources : [@witcheer, 13 août 2026](https://x.com/witcheer/status/2087950345162875106) - [@Teknium, 13 août 2026](https://x.com/Teknium/status/2087947369229009119)

## Alerte : campagne de phishing "HERMES Contributor Update"

Le 15 août, Teknium a signalé une tentative d'escroquerie par email ciblant les contributeurs Hermes Agent. Un mail frauduleux intitulé "HERMES Contributor Update" circule. Teknium précise qu'il ne faut cliquer sur aucun lien dans ce type de message. GitHub enquête sur l'affaire via Kevin Crosby.

> Sources : [@Teknium, 15 août 2026](https://x.com/Teknium/status/2088471683762119117)

## Sources

- [@NousResearch - /loop, 14 août 2026](https://x.com/NousResearch/status/2088367838977237029)
- [@Teknium - /loop, 14 août 2026](https://x.com/Teknium/status/2088368313974047165)
- [@witcheer - /loop détails, 15 août 2026](https://x.com/witcheer/status/2088491869000835146)
- [@Teknium - Bot Mode release desktop, 15 août 2026](https://x.com/Teknium/status/2088579906217345228)
- [@Teknium - Préparation Bot Mode, 15 août 2026](https://x.com/Teknium/status/2088488103380205907)
- [@Teknium - Skills hub dans Bot Mode, 14 août 2026](https://x.com/Teknium/status/2088328581953032238)
- [@EddieVi - Retour Bot Mode, 15 août 2026](https://x.com/EddieVi35539602/status/2088449423210656109)
- [@witcheer - Détails expansion plugins, 13 août 2026](https://x.com/witcheer/status/2087950345162875106)
- [@Teknium - Expansion plugins, 13 août 2026](https://x.com/Teknium/status/2087947369229009119)
- [@Teknium - Arnaque phishing, 15 août 2026](https://x.com/Teknium/status/2088471683762119117)
- [Documentation /loop](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
