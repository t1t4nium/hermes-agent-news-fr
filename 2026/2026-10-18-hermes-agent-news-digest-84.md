# Hermes Agent Quotidien #84

Cette édition revient sur les 113 pull requests fusionnées le 17 octobre, sur hermes-vcc-engine et by2kb, deux plugins qui arrivent au catalogue, sur cinq fonctionnalités à connaître dont les deux dernières pour la prochaine release, et sur le support dès le premier jour du Harness Pro, un écran de bureau pour agents.

## 113 pull requests fusionnées le 17 octobre

iamlukethedev a fait le compte le 18 octobre : Hermes a fusionné 113 pull requests le 17 octobre. Les changements mis en avant :

- Desktop affiche un tour perdu avec son bouton Discard quand la passerelle meurt en plein tour, et on peut piloter ou modifier une invite en file depuis Desktop.
- patch et write_file répondent en millisecondes, et les diagnostics LSP ne bloquent plus l'écriture.
- Les agents cessent de re-attendre un processus d'arrière-plan silencieux : Hermes les prévient à sa sortie, et une commande qui se termine par un & isolé tourne désormais comme tâche d'arrière-plan suivie au lieu d'être refusée.
- Les appels d'outils diffusés de LM Studio, Kimi et MiniMax ne se cassent plus.
- X Chat rejoint le catalogue comme plugin officiel, et Hermes tourne sous le compte que l'on connecte.
- DeepSeek v4.1 Flash entre dans les sélecteurs OpenRouter et Nous Portal, et llama.cpp gagne Nemotron 3.5 Bolt avec les brouillons DFlash.
- Ctrl+D en cours de tour dans le CLI détache de la passerelle au lieu de tuer l'exécution.
- Les secrets sont resserrés : les secrets figés de la configuration se lient à leurs points de terminaison résolus, et les clés intégrées restent hors des entrées personnalisées homonymes.
- Un balayage des messageries corrige WhatsApp, Telegram, Feishu, la voix Discord et les cas limites de Bot Chat.
- Le catalogue s'agrandit beaucoup : Unraid, Nextcloud Talk, Grok Voice via hermes-xai, Jina, pay, personae et d'autres.

> Sources : [@iamlukethedev, Hermes merged 113 PRs on October 17, 18 octobre 2026](https://x.com/iamlukethedev/status/2111697506254164265)

## hermes-vcc-engine, compacter sans appeler le modèle

witcheer a signalé le 18 octobre l'entrée de hermes-vcc-engine au catalogue de plugins : l'agent compacte une longue conversation sans demander au modèle d'écrire le résumé. Sur un modèle local, l'attente après une compression serait environ neuf fois plus courte dans les tests de l'auteur. Le résumé garde chaque commande avec son code de sortie, les erreurs et les fichiers touchés, et chaque ligne renvoie au message d'origine, que Hermes conserve de toute façon.

La fiche du catalogue, signée danbiocchi (danbiocchi/hermes-vcc-engine, licence Apache-2.0), détaille le mécanisme. Le moteur remplace l'étape de résumé de la compression de Hermes par une projection déterministe de la conversation : demandes, commandes et codes de sortie, erreurs, correctifs et fichiers lus ou modifiés, chaque ligne portant une référence vers le message d'origine pour le rappel via session_search. Aucun appel modèle sur le chemin normal. Dans les mesures de l'auteur, un résumé standard prenait en médiane 195 secondes sur un modèle local, jusqu'à treize minutes, et a deux fois atteint le plafond de quinze minutes avant d'être abandonné ; l'étape vcc prend bien moins d'une seconde. La même entrée donne toujours la même sortie, donc le comportement se teste.

Le moteur sous-classe ContextCompressor de Hermes et ne remplace que la méthode _generate_summary ; quand compacter, ce qui reste verbatim, l'appariement des appels d'outils, la censure et l'archivage restent le code de Hermes. Il s'appuie sur des méthodes privées qui ne sont pas une API de plugin documentée, donc une mise à jour de Hermes peut les changer ; un contrôle au démarrage et un repli vers le compresseur standard existent pour cela. La configuration passe par context.vcc dans config.yaml : une ligne pour l'activer, une ligne pour remettre le compresseur d'origine.

> Sources : [@witcheer, hermes-vcc-engine is in the Hermes plugin catalog, 18 octobre 2026](https://x.com/witcheer/status/2111812039203295546) et [hermes-vcc-engine, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/hermes-vcc-engine)

## by2kb, des vidéos aux notes de révision

witcheer a présenté le 18 octobre by2kb, un outil communautaire pour les vidéos que l'on garde sous le coude. On donne un lien YouTube à son agent, il le transcrit sur sa propre machine et range les notes dans un dossier. Le court résumé indique même quand les notes longues ne valent pas la lecture.

La fiche du catalogue, signée Charlesmpc (Charlesmpc/by2kb), précise le fonctionnement. Le plugin transforme une vidéo Bilibili ou YouTube en trois artefacts Markdown durables : la transcription qui préserve les preuves, un court résumé « vaut-il la peine d'être lu », et des notes d'étude longues. Un hook pre_gateway_dispatch intercepte le lien, vérifie l'expéditeur, lance la transcription en arrière-plan, puis appelle le modèle hôte de Hermes pour les résumés, sans serveur MCP ni clé LLM séparée. La transcription passe d'abord par les sous-titres natifs, sinon par le flux audio avec une reconnaissance locale par Whisper par défaut, sans cloud. L'installation tient en `hermes plugins install by2kb`.

> Sources : [@witcheer, new community tool for Hermes Agent: by2kb, 18 octobre 2026](https://x.com/witcheer/status/2111744091608522998) et [by2kb, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/by2kb)

## Cinq fonctionnalités à connaître

witcheer a listé le 18 octobre cinq fonctionnalités de Hermes Agent. Les trois premières sont déjà dans v0.22.2, les deux dernières arrivent avec la prochaine release :

- Demander à Hermes d'installer les plugins et les skills soi-même : dans un chat de Hermes Desktop, on dit ce que l'on veut et il trouve le plugin ou la skill qui correspond. (#134052)
- Hermes Desktop a sa propre visite guidée : on demande à Hermes de faire visiter l'application, et il lance la visite prête à l'emploi, courte ou complète. (#134054)
- Les plugins trouvent l'application déjà installée : un plugin qui pilote une application de bureau comme Blender cherche désormais dans plusieurs emplacements habituels sur Windows, macOS et Linux, pas un seul dossier figé. (#134050)
- Les tâches répétées affichent leur prochaine exécution : un compte à rebours en direct reste à l'écran. (#139187)
- Hermes demande avant de jeter du code inachevé : fermer une session de codage latérale avec des changements en cours permet de la garder, de la mettre de côté, ou de la jeter. (#140603)

witcheer précise que tout cela vient des retours de la communauté.

> Sources : [@witcheer, five Hermes Agent features worth knowing about, 18 octobre 2026](https://x.com/witcheer/status/2111789391769129395)

## Harness Pro, support dès le premier jour

Teknium a annoncé le 18 octobre le support dès le premier jour de Hermes Agent pour le Harness Pro, un écran de bureau pour agents d'Autonomous, en reprenant un post de dee_hw qui présentait l'objet.

La page produit décrit le Harness Pro, vendu 299 dollars : un écran tactile carré de 720 par 720 pixels qui se branche en USB-C sur un Mac et dialogue avec l'application Harness. Celle-ci atteint les agents sur chaque machine que l'on utilise, pour regarder et diriger un agent depuis le bureau. Chaque agent occupe tout l'écran avec un animal de compagnie qui mime son travail ; on glisse pour passer au suivant. On tape sur l'agent pour lui parler, et il garde les écouteurs. Les agents continuent à travailler quand on ferme l'application ou l'ordinateur. L'appareil embarque un ESP32-P4 avec 16 Mo de flash et 32 Mo de PSRAM, trois microphones, un haut-parleur, et se met à jour par le câble.

> Sources : [@Teknium, Day 0 support for Hermes Agent!, 18 octobre 2026](https://x.com/Teknium/status/2111671559937232988) et [Harness Pro, page produit Autonomous](https://autonomous.ai/harness-pro)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
