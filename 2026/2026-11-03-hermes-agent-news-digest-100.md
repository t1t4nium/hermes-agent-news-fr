# Hermes Agent Quotidien #100

Cette édition revient sur la sortie stable de Hermes v0.22.6, sur les 190 pull requests fusionnées le 2 novembre, sur l'adapter Hermes du modèle LFM2.5-24B, sur l'abonnement Nous Portal refondu, et sur un plugin qui retrouve la vitesse d'un avion à partir du seul son.

## Hermes v0.22.6 passe en stable

Le 3 novembre, iamlukethedev a annoncé que Hermes v0.22.6 est passé en stable, avec 776 pull requests fusionnées depuis v0.22.5, disponible dans le CLI, l'application Microsoft Store, Docker et Hermes Cloud. Il en retient deux à essayer d'abord : `hermes migrate`, pour que les personnes venant de Grok Bot ou OpenBot arrivent avec leur installation, et `hermes webapp`, pour faire tourner la Webapp depuis sa propre passerelle.

La note de release, publiée le 2 novembre par teknium1, cadre la fenêtre. C'est une release de correctifs qui roule en stable les 776 pull requests de la fenêtre v0.22.5 vers v0.22.6. Mesurée au commit f0d94882e89, la fenêtre contient 3 448 commits sans fusion sur 4 316 fichiers modifiés (+248 579 / -94 077) et 385 issues fermées. Les notes détaillées et curées de toute la fenêtre partiront avec v0.23.0.

La note liste aussi, sans les détailler, les changements marquants de la fenêtre :

- La Webapp servie depuis le listener de sa propre passerelle (`hermes webapp`), avec un panneau Desktop pour l'ouvrir sur son réseau ou derrière sa propre URL, et des plugins Desktop chargés dans un onglet du navigateur.
- `/model reset` pour effacer l'épinglage de modèle d'une session sans perdre l'historique.
- Des verrous par skill contre les écritures autonomes, activables depuis le panneau Capacités de Desktop.
- La compaction préparée opt-in via `compression.prepare_ahead`.
- `hermes cron cancel`, une politique de gestion des exécutions manquées par job et un bouton Stop dans l'éditeur cron de Desktop.
- Les choix de `/delegation` conservés pour la session suivante.
- `hermes migrate` et `hermes setup` qui font arriver les personnes de Grok Bot et OpenBot.
- Le stockage opt-in de la clé de coffre dans le trousseau du système.
- Le champ `requires_hermes` du catalogue appliqué à l'installation et à la mise à jour des plugins.
- Des voix ElevenLabs choisies par l'agent dans `text_to_speech`.
- Un hook `pre_llm_call` qui peut bloquer un tour avant l'inférence.
- Le renommage, la dissolution, les mentions et le collage de pièces jointes dans les groupes Desktop.
- Chaque profil affiché comme une section de la barre latérale de Desktop.
- Les notes vidéo Telegram, les réactions emoji Slack en contexte de fil, et les téléchargements reprenables dans le gestionnaire de paquets.

> Sources : [@iamlukethedev, Hermes v0.22.6 just went stable, 3 novembre 2026](https://x.com/iamlukethedev/status/2117567920544854166) et [Hermes Agent v0.22.6, note de release GitHub, 2 novembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.6)

## 190 pull requests fusionnées le 2 novembre

iamlukethedev a fait le compte le 3 novembre : Hermes a fusionné 190 pull requests le 2 novembre. Il en retient une de fond : la passerelle ne se fige plus chaque minute pour les coupes mémoire, et la passerelle comme `serve` ne retiennent plus la mémoire libre à travers environ 160 arènes malloc.

Le changelog du 2 novembre complète. StateJar entre au catalogue, un fournisseur de mémoire qui ne garde que le nécessaire et trace un journal d'audit des interactions (#147142). Un paquet corrompu en cache ne bloque plus toutes les installations (#146929). Les interrupteurs de capacités de Desktop affichent On/Off au lieu de Enable/Disable (#147813). Et une salve de plugins entre au catalogue communautaire : hermes-band pour composer et rendre de la musique en local, word-peek pour lire des passages HTML, switch402 pour des outils web x402 verrouillés par approbation, et hashference-provider pour joindre les modèles de Hashference.

> Sources : [@iamlukethedev, Hermes merged 190 PRs on November 2, 3 novembre 2026](https://x.com/iamlukethedev/status/2117421202755268957) et [Hermes Bible, changelog du 2 novembre 2026](https://www.hermesbible.com/changelog?date=2026-11-02)

## Un adapter Hermes pour LFM2.5-24B

Le 2 novembre, younes a annoncé avoir fini l'entraînement LoRA d'un adapter Hermes pour le modèle LFM2.5-24B de Liquid AI, sans baisse de précision sur les tâches de test tenues à part, avec 20 % de gain d'efficacité. Teknium a relayé la nouvelle.

La collection Hugging Face harness-hub/lfm25-24b-harness-adapters porte les poids. Elle regroupe des modèles entraînés par apprentissage par renforcement sur des adapters pour un développement agentique plus efficace, déclinés pour plusieurs harnesses : pi, claude-code et hermes, chacun en format d'origine et en GGUF. La version Hermes, LFM2.5-24B-A2B-hermes, est la plus récente de la collection, mise à jour la veille.

> Sources : [@yb2698, LFM2.5-24B harness adapter for @NousResearch hermes agent, 2 novembre 2026](https://x.com/yb2698/status/2117266739893567990) et [LFM2.5-24B Harness adapters, collection Hugging Face harness-hub](https://huggingface.co/collections/harness-hub/lfm25-24b-harness-adapters)

## L'abonnement Nous Portal refondu

Le 3 novembre, Teknium a invité à revoir ses a priori : chaque abonnement Nous Portal dans Hermes vient désormais avec un agent cloud et son propre ordinateur, des modèles à plafond d'usage élevé, et tous les outils, dont la recherche, le scraping, l'usage du navigateur et la génération d'images. witcheer précise que chaque plan payant inclut l'usage de Hermes Agent sur des plafonds qui se réinitialisent quotidiennement, hebdomadairement et mensuellement, un agent Hermes Cloud qui tourne 24 heures sur 24, et n'importe quel modèle, les gros sur leur propre plafond mensuel.

La page du portail détaille les paliers. Free reste gratuit, avec les modèles gratuits et zéro crédit mensuel. Plus à 20 dollars par mois inclut l'usage, un agent cloud de 4 Go de RAM et 25 Go de disque, et tout modèle, les grands sur plafond mensuel. Super à 100 dollars monte le disque à 100 Go. Ultra à 200 dollars passe à 8 Go de RAM et 100 Go de disque. On peut aussi connecter un compte ChatGPT éligible pour l'inférence, sans abonnement Nous payant.

> Sources : [@Teknium, Every nous portal sub in Hermes comes with a cloud agent and its own computer now, 3 novembre 2026](https://x.com/Teknium/status/2117513285440590035), [@witcheer, every paid plan now comes with, 2 novembre 2026](https://x.com/witcheer/status/2117357848459989124) et [Nous Portal, page d'abonnement](https://portal.nousresearch.com)

## La vitesse d'un avion mesurée à l'oreille

witcheer a montré le 3 novembre un Hermes Agent qui retrouve la vitesse d'un avion passé au-dessus de soi, et la distance minimale, à partir de la seule hauteur du son. Le plugin trace la fréquence dans un enregistrement et ajuste la courbe de décalage Doppler pour en tirer vitesse et distance de passage.

> Source : [@witcheer, your Hermes Agent can work out how fast a plane flew past you, 3 novembre 2026](https://x.com/witcheer/status/2117609992958382269)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
