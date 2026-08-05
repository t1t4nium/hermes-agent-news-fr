# Hermes Agent Quotidien #9

La Herald Release v0.20.0 est en ligne, Liquid AI entraîne son modèle dans Hermes Agent, l'intégration iMessage via Photon se précise, et un plugin achievements arrive sur le desktop.

## Hermes Agent v0.20.0, la Herald Release, est publiée

La version v0.20.0 d'Hermes Agent, annoncée hier, est en ligne sur GitHub (tag v2026.8.3, 3 août). Nom de code Herald Release. Depuis v0.19.0, le dépôt compte environ 3 650 commits, 1 400 PR fusionnées, 5 200 fichiers modifiés et 1 200 issues fermées, avec plus de 650 contributeurs.

Les changements principaux, résumés :

- Voix conversationnelle : TTS en streaming phrase par phrase, barge-in (l'agent s'arrête si vous parlez), détection de silence, et mots de réveil locaux ("hey Hermes" ou un mot choisi), avec routage par profil et commande vocale "stop" sur toutes les surfaces.
- Voix sur toutes les plateformes : notes vocales transcrites sur WhatsApp, Feishu, DingTalk, LINE, QQ, Photon et Weixin, réponses TTS automatiques adaptées à chaque plateforme, STT entièrement configurable (catégorie hermes tools, toggles GUI, support de gpt-transcribe d'OpenAI).
- Protocole A2A v1.0 : un plugin intégré implémente le protocole Agent-to-Agent, Hermes peut découvrir, dialoguer avec et être piloté par d'autres agents compatibles A2A. Cela clôt l'issue #514, une des plus anciennes demandes du dépôt.
- Webhooks sortants : Hermes pousse des événements signés (HMAC) vers des endpoints HTTP, pour brancher la CI, la domotique ou des dashboards sans boucle de polling.
- Recherche sourcée : la skill grounded-citations fait correspondre chaque citation au texte réel des pages, avec des liens vers la preuve exacte et un mode fact-checking.
- Le desktop devient une plateforme : artefacts versionnés avec aperçu live sandboxé, SDK de plugins (Kanban est le premier plugin officiel), fenêtre de saisie rapide par raccourci global, plusieurs fenêtres GUI.
- CLI : mode shell avec !, commandes /init (génère un AGENTS.md), /diff, /context, /focus, et hermes import-agent pour migrer une config Claude Code ou Codex CLI.
- Redirections en cours de tour : taper une correction pendant que l'agent travaille redirige le tour actif sans tout relancer.
- Outils qui se réparent : sortie terminal tronquée vers un fichier, patch qui détecte les edits déjà appliqués, write_file qui vérifie le contenu sur disque, recherches avec quasi-correspondances ; limite d'itérations par défaut passée de 90 à 500.
- Compression : micro-compaction par tour, garantie de garder les N derniers messages utilisateur, seuils configurables par modèle en tokens absolus.
- Performances : démarrage à froid de hermes -w passé d'environ 14 s à 1,8 s, cache de prompt couvrant les schémas d'outils sur Anthropic natif, deuxième vague 60 fps sur le desktop.
- Buzz intégré comme plateforme gateway (messagerie Nostr de Block, transport WebSocket natif, auth NIP-42), retour modernisé des providers Vercel AI Gateway et Vercel Sandbox.
- Secrets : verrouillage des secrets avec Ironproxy, rotation de token en une commande, cache break-glass chiffré optionnel pour Bitwarden.

Teknium résume : "so much in the Herald Release", en listant aussi l'intégration Buzz, les nouveaux skills office/productivity et la réduction de 20 % sur tous les modèles du Nous Portal.

> Sources : [Release v0.20.0 sur GitHub](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3) - [@NousResearch, 3 août 2026](https://x.com/NousResearch/status/2084325600643445095) - [@Teknium, 3 août 2026](https://x.com/Teknium/status/2084344999513383195)

## Liquid AI entraîne son modèle dans Hermes Agent

Liquid AI a annoncé le 4 août que la dernière étape de post-entraînement de son nouveau modèle passe par du RL agentique multi-tours à travers trois harnesses réelles : Pi, Hermes Agent et OpenClaw. Chaque rollout tourne dans son propre sandbox, optimisé en GRPO contre une récompense de résultat (rubrique de jugement LLM, vérifications programmatiques, garde-fou de sécurité).

"Le modèle arrive en ayant déjà vu leurs outils, leurs system prompts et leurs schémas d'interaction", explique Liquid AI. Teknium a relayé l'annonce sans commentaire. C'est une validation de plus d'Hermes Agent comme environnement d'entraînement, pas seulement d'exécution.

> Source : [@liquidai relayé par @Teknium, 4 août 2026](https://x.com/liquidai/status/2084640749862236227)

## Hermes Agent relié à iMessage via Photon

Julie Chen (@0xJuliechen) a publié un tutoriel d'une minute pour connecter Hermes Agent à iMessage via Photon. "12k+ hermes users are already on it", écrit-elle, en évoquant une intégration officielle avec Nous Research et un réglage en 60 secondes. Teknium a relayé le tuto le 4 août.

> Source : [@0xJuliechen relayé par @Teknium, 4 août 2026](https://x.com/0xJuliechen/status/2084416774452412635)

## Un plugin achievements pour Hermes Desktop

Tony Simons (@tonysimons_) a publié hermes-desktop-achievements, un plugin qui ajoute les succès à l'application desktop : score en en-tête, filtres par palier, barres de progression, chip dans la barre de statut et commande ⌘K. "Backed by the plugin API Hermes already ships, zero new backend", précise-t-il. Il dit avoir débloqué 36 succès sur 60 sur sa machine.

> Source : [@tonysimons_ relayé par @Teknium, 3 août 2026](https://x.com/tonysimons_/status/2084124783893967221)

## Sources

- [Hermes Agent v0.20.0, release GitHub](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.3)
- [@NousResearch - Herald Release, 3 août 2026](https://x.com/NousResearch/status/2084325600643445095)
- [@Teknium - Récap Herald Release, 3 août 2026](https://x.com/Teknium/status/2084344999513383195)
- [@liquidai relayé par @Teknium - RL agentique, 4 août 2026](https://x.com/liquidai/status/2084640749862236227)
- [@0xJuliechen relayé par @Teknium - Photon iMessage, 4 août 2026](https://x.com/0xJuliechen/status/2084416774452412635)
- [@tonysimons_ relayé par @Teknium - Plugin achievements, 3 août 2026](https://x.com/tonysimons_/status/2084124783893967221)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
