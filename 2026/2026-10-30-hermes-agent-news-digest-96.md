# Hermes Agent Quotidien #96

Cette édition revient sur les 147 pull requests fusionnées le 29 octobre, sur Nous-Girl, un robot de bureau StackChan dont Hermes Agent est le cerveau, et sur un Hermes Agent local qui tient 93 tok/s sur une RTX 5090.

## 147 pull requests fusionnées le 29 octobre

iamlukethedev a fait le compte le 30 octobre : Hermes a fusionné 147 pull requests le 29 octobre. Il met en avant deux changements. Les sessions en cours peuvent rafraîchir leur prompt, pour qu'un SOUL.md, des skills ou des fichiers de contexte modifiés s'appliquent sans tout recommencer. Les mots de passe enregistrés se remplissent désormais sur les pages du navigateur Camofox via browser_vault.

Le changelog précise le premier point : on met à jour les instructions, les skills ou les fichiers de contexte de l'agent, puis on rafraîchit manuellement les conversations en cours, sans les redémarrer. La pull request #143581 est de victor-kyriazakos.

Les autres changements à retenir :

- Les skills intégrées sont allégées : les skills optionnelles dépassées sont retirées, les skills de niche deviennent optionnelles, et les outils Office tiennent dans une seule skill.
- Les helpers Office et PDF ne perdent plus de contenu à la lecture : les tableaux imbriqués, les en-têtes et pieds de page et les titres de diapositives vides sont conservés, et les formulaires PDF sont aplatis sans perte.
- Un appel Bedrock qui ne répond plus échoue après un seul délai de lecture, plus après cinq.
- Une socket de passerelle morte ne tue plus le spinner et le dock de processus du CLI.
- Un superviseur unique de fin de propriétaire remplace plusieurs mécanismes pour fermer proprement les processus enfants quand Hermes s'arrête.
- Un écran de bot de bureau abandonné s'arrête de lui-même après la fenêtre d'inactivité.
- Le plugin signal-notify envoie une notification Signal quand une conversation se met en pause, échoue ou demande une intervention.
- Le catalogue accueille un plugin fournisseur Modular, transcription-dashscope pour transcrire l'audio et perf-hud pour afficher les statistiques de performance dans Desktop.
- La Webapp peut installer un plugin réservé au bureau directement depuis l'onglet.

> Sources : [@iamlukethedev, Hermes merged 147 PRs on October 29, 30 octobre 2026](https://x.com/iamlukethedev/status/2115987622552363453), [Hermes Bible, changelog du 29 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-29), [refresh-prompts, PR #143581](https://github.com/NousResearch/hermes-agent/pull/143581) et [browser_vault sur Camofox, PR #146240](https://github.com/NousResearch/hermes-agent/pull/146240)

## Nous-Girl, un robot StackChan dont Hermes est le cerveau

witcheer a annoncé le 29 octobre qu'un membre de la communauté a publié le code et un guide pour construire un robot piloté par Hermes Agent. Nous-Girl est un M5Stack StackChan qui se souvient de vous d'une conversation à l'autre. Quand on lui demande, Hermes Agent lui tourne la tête, change son visage et règle ses lumières, à travers un serveur MCP stackchan.

Le dépôt dax8it/nous-girl-stackchan précise le montage. Le robot est un StackChan K151 de M5Stack, un CoreS3 à ESP32-S3, qui tourne un firmware maison, actuellement en version v3.6.7-dj7 du 28 octobre. Le serveur vocal xiaozhi-esp32-server tourne en Docker sur son ordinateur et gère l'écoute et la parole avec des modèles locaux. Le cerveau est Hermes Agent, qui apporte la mémoire longue et les outils, ou un simple modèle local sous Ollama.

Le projet est présenté comme un loisir à un seul mainteneur, Alex Covo, bâti avec une forte assistance IA, en bêta. Sans Hermes, le robot parle mais repart de zéro à chaque conversation. Le firmware comprend des visages animés avec synchronisation labiale, deux mots de réveil, douze LED, des danses, un mode DJ, une voix multilingue en cinq langues, une caméra, un mode acteur, une boîte mail dédiée et un rapport de plantage. Le code et la documentation sont sous licence MIT, les visages de départ sous CC0. Seul macOS sur Apple Silicon est testé à ce jour.

> Sources : [@witcheer, your Hermes Agent can be the brain of a robot, 29 octobre 2026](https://x.com/witcheer/status/2115927909903069695) et [dax8it/nous-girl-stackchan, dépôt GitHub](https://github.com/dax8it/nous-girl-stackchan)

## 93 tok/s en local sur une RTX 5090

witcheer a mesuré le 29 octobre un Hermes Agent en local sur sa RTX 5090 : environ 93 tok/s, en moyenne sur une heure de vrai travail d'agent. La recette : un fichier Qwen3.8-27B en 6 bits, le brouillon MTP du modèle activé dans llama.cpp, un cache q8_0 et un contexte de 128k.

La mesure porte sur une session d'objectif d'une heure, pas sur un banc synthétique, ce qui la rend plus proche de l'usage réel. C'est le même modèle que celui mis en avant par la fonctionnalité modèles locaux de Hermes Agent, ajoutée début septembre.

> Source : [@witcheer, Hermes Agent on my RTX 5090 with a local model, 29 octobre 2026](https://x.com/witcheer/status/2115896456263487915)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
