# Hermes Agent Quotidien #22

La version v0.20.2 regroupe environ 397 PRs, Bots Mode entre en phase de packaging pour le desktop, le projet franchit 2 500 contributeurs, et la limite de contexte des abonnements ChatGPT et Codex monte à 900K tokens.

## v0.20.2 : un tag qui consolide 397 PRs

Le 16 août, Hermes Agent a publié v0.20.2 (v2026.8.16). C'est une release patch : le tag rassemble environ 397 pull requests fusionnées depuis v0.20.1 en une version stable pour les consommateurs en aval (images Docker, déploiements hébergés, installations neuves).

La fenêtre compte environ 967 commits sur 1 279 fichiers (+128 522 / −7 622). Les changements couvrent plusieurs surfaces :

- Desktop : registre de connexions multi-gateways, rafraîchissements scopés par profil, vérifications d'état MCP et deep links.
- CLI : sondes de mise à jour Windows, protocole clavier Kitty, durcissement du chat avec l'option `-c`.
- Gateway : routes de modèles persistées, complétion de `/loop`, topics Telegram par DM.
- Cache de prompt pour LiteLLM Claude sur le fil OpenAI, durcissement du cron, résolution d'authentification à travers les scopes de profil, et installer plus fiable sur Linux et Windows.

Les notes de release détaillées et le crédit complet des contributeurs arriveront avec v0.21.0, qui documentera tout depuis v0.20.0.

> Source : [Release Hermes Agent v0.20.2](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.16)

## Bots Mode entre en phase de packaging

Le 16 août au soir, Teknium a annoncé qu'il emballait Bots Mode pour Hermes Agent Desktop en vue de la release : "Packaging up Bots Mode for Hermes Agent Desktop for release right now, stay tuned". L'édition #20 avait annoncé cette sortie autour du 17 août ; la phase de packaging est donc en cours.

Dans les réponses, Teknium a clarifié le périmètre. Bots Mode n'est qu'une couche d'UX par-dessus les profils d'agents, rien de plus. Chaque bot a son propre gateway, ce qui lui permet d'être un bot indépendant sur Telegram ou Discord. La possibilité de faire discuter plusieurs bots entre eux fait partie de la mise à jour.

> Sources : [@Teknium, packaging Bots Mode, 16 août 2026](https://x.com/Teknium/status/2089098159217918249) - [@Teknium, Bots Mode = UX pour profils, 16 août 2026](https://x.com/Teknium/status/2089131479561601296) - [@Teknium, gateway par bot, 16 août 2026](https://x.com/Teknium/status/2089111859903471667)

## Hermes Agent passe 2 500 contributeurs

Le 17 août, Teknium a indiqué qu'Hermes Agent a franchi les 2 500 contributeurs ce week-end. Il a souligné que l'équipe n'a encore intégré qu'une partie du travail de chacun : "nous avons à peine gratté la surface de la revue et de l'intégration du travail de tous ceux qui ont contribué".

> Source : [@Teknium, 17 août 2026](https://x.com/Teknium/status/2089186056973562102)

## Abonnements ChatGPT et Codex : limite à 900K tokens

Le 17 août, Teknium a annoncé que la limite de contexte des utilisateurs des abonnements ChatGPT et Codex passe à 900K tokens dans Hermes Agent. Pour en profiter, il faut mettre à jour Hermes. Dans le fil, une précision utile : le modèle GPT-5.6 Sol en 1M de contexte fonctionne désormais aussi pour l'usage via les comptes ChatGPT, alors que cela ne marchait auparavant que pour les clés API.

> Source : [@Teknium, 17 août 2026](https://x.com/Teknium/status/2089163355261214830)

## Laguna S 2.1 gratuit deux semaines de plus sur Nous Portal

Laguna S 2.1, le modèle de poolside, reste gratuit deux semaines de plus sur Nous Portal. Pour l'utiliser dans son agent, il suffit de choisir `poolside/laguna-s-2.1:free` dans `/model`.

> Sources : [@witcheer, 17 août 2026](https://x.com/witcheer/status/2089361292549108152) - [@yeahfortommy, 17 août 2026](https://x.com/yeahfortommy/status/2089359131933061161)

## Sources

- [Release Hermes Agent v0.20.2](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.16)
- [@Teknium - Packaging Bots Mode, 16 août 2026](https://x.com/Teknium/status/2089098159217918249)
- [@Teknium - 2 500 contributeurs, 17 août 2026](https://x.com/Teknium/status/2089186056973562102)
- [@Teknium - Limites ChatGPT/Codex à 900K, 17 août 2026](https://x.com/Teknium/status/2089163355261214830)
- [@witcheer - Laguna S 2.1 gratuit, 17 août 2026](https://x.com/witcheer/status/2089361292549108152)
- [@yeahfortommy - Laguna S 2.1 gratuit, 17 août 2026](https://x.com/yeahfortommy/status/2089359131933061161)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
