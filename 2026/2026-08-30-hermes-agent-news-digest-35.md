# Hermes Agent Quotidien #35

Cette édition revient sur le skill officiel Box pour Hermes, sur la distinction désormais nette entre `/bg` et `/btw`, sur l'ajout de Brave parmi les navigateurs du profil réel, sur le modèle de crédits de Nous Portal et sur un usage astucieux de la communauté pour repérer les fenêtres de prix des fournisseurs.

## Le skill officiel Box pour Hermes

Nous Research met en avant le skill officiel Box pour Hermes Agent : l'agent agit comme l'utilisateur, dans la limite des permissions définies, pour gérer fichiers et versions en volume, chercher et extraire des données de documents, et interroger le système de fichiers cloud.

Le skill, version 1.0.0 sous licence MIT signée par Chris Kim et Hermes Agent, s'appuie sur le CLI Box et couvre l'organisation, l'upload, le versioning, le partage et la collaboration sur les fichiers, la recherche dans le contenu et les métadonnées, l'extraction d'informations ancrées dans un fichier, le traitement d'un dossier à l'échelle sans tout télécharger, et la construction d'applications adossées à Box. Il s'installe comme les autres skills officiels de Hermes via la commande d'installation dédiée.

> Sources : [@NousResearch, With the official @Box skill for Hermes, 29 août 2026](https://x.com/NousResearch/status/2093818374119739674) et [box/SKILL.md, dépôt GitHub NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent/blob/main/skills/productivity/box/SKILL.md)

## `/bg` et `/btw` : deux commandes aux rôles distincts

Après avoir mis en avant `/btw`, Teknium clarifie la différence entre `/bg` et `/btw`. `/bg` (background) lance une tâche séparée dans une session fraîche, dont la réponse est renvoyée dans la session de travail. `/btw` pose une question annexe sur la conversation en cours, sans l'interrompre.

La documentation distingue les deux mécanismes. `/bg <prompt>` exécute le prompt dans une session d'arrière-plan indépendante, la session courante reste libre pour d'autres travaux, et le résultat apparaît dans un panneau à la fin. `/btw <question>` déclenche un appel LLM auxiliaire sur un cliché en lecture seule du transcript, sans toucher à l'historique ni au cache de la session en cours. Tonbi a illustré la distinction dès sa sortie.

> Sources : [@Teknium, Thanks for the feedback on /btw, 29 août 2026](https://x.com/Teknium/status/2093707259432038402), [@tonbistudio, /bg pour les tâches d'arrière-plan, /btw pour les questions annexes, 30 août 2026](https://x.com/tonbistudio/status/2093948126977720419) et [Slash Commands Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## Brave rejoint les navigateurs du profil réel

Teknium annonce l'ajout de Brave Origin au support de la navigation avec le profil utilisateur réel dans Hermes Agent. La fonction, livrée cette semaine, permet à l'agent de naviguer connecté à partir d'une copie du profil de navigateur existant, sans toucher au profil d'origine.

> Source : [@Teknium, Added Brave Origin support for the real user profile browser, 30 août 2026](https://x.com/Teknium/status/2093869407382733180)

## Le modèle de crédits de Nous Portal

witcheer détaille le fonctionnement de Nous Portal : Hermes Agent y tourne sur des crédits, dépensés à l'usage. Un compte donne accès à plus de 300 modèles issus des laboratoires de pointe, dont des modèles gratuits et des modèles payants remisés sous le prix de liste, ainsi qu'à des outils hébergés regroupés dans l'abonnement.

> Source : [@witcheer, on Nous Portal your Hermes Agent runs on credits, 29 août 2026](https://x.com/witcheer/status/2093778755114213771)

## Suivre les fenêtres de prix avec un emoji en fin de message

witcheer relate un usage de la communauté : un membre a appris à son Hermes Agent à terminer chaque message par un emoji indiquant si son fournisseur de modèles est en période de prix élevé (surge) ou creux (off-peak). D'un coup d'œil, on peut lancer les tâches lourdes ou attendre la fenêtre la moins chère.

> Source : [@witcheer, someone taught their Hermes Agent to end every message with an emoji, 30 août 2026](https://x.com/witcheer/status/2093993367449260519)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
