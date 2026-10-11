# Hermes Agent Quotidien #77

Cette édition revient sur la centralisation des plugins officiels de Hermes Agent dans un mono-répôt dédié, sur le modèle stealth MISSINGNO. mis à disposition sur Nous Portal, sur le numéro 97 des Wingtips consacré aux questions préalables, sur les 55 pull requests fusionnées le 10 octobre, et sur la connexion de Hermes Desktop à un backend distant.

## Un mono-répôt pour les plugins officiels

Teknium a annoncé le 11 octobre la consolidation des plugins officiels de Hermes Agent dans un mono-répôt unique, pour améliorer la visibilité des signalements et centraliser le code. Le dépôt s'appelle NousResearch/hermes-official-plugins et rassemble les plugins first-party construits et maintenus par Nous Research.

Le dépôt compte neuf plugins : Home Assistant, Spotify, Claude Subscription DirectSDK, Telegram Business Mode, Memory Wiki, Blender, Snyk, TouchDesigner et Accent Picker. Chaque répertoire forme un plugin autonome, que le catalogue installe par couple dépôt plus sous-répertoire à un commit épinglé ; Hermes ne récupère que ce répertoire via un clone épars sans historique, si bien qu'installer Spotify ne télécharge pas Home Assistant. La migration est pensée pour ne rien demander : les utilisateurs de Home Assistant ou de Spotify intégrés au cœur reçoivent le plugin automatiquement à la mise à jour, ceux qui l'ont installé depuis le catalogue suivent le mono-répôt au prochain hermes plugins update, et ceux qui l'ont installé par URL doivent le réinstaller une fois depuis le catalogue avec --force. Les anciens dépôts sont archivés et ne reçoivent plus de correctifs. La CI teste chaque plugin contre le cœur actuel sur Linux, macOS et Windows, à chaque push, pull request et passage nocturne.

> Sources : [@Teknium, We are consolidating the official plugins for Hermes Agent into the following mono-repo, 11 octobre 2026](https://x.com/Teknium/status/2109177877543682419) et [Hermes Official Plugins, dépôt GitHub NousResearch](https://github.com/NousResearch/hermes-official-plugins)

## MISSINGNO., un modèle stealth en accès libre sur Nous Portal

Nous Research a annoncé le 10 octobre un modèle « stealth » présenté comme « Wild MISSINGNO. » : un modèle de code et de raisonnement agentique, décrit comme très économe en jetons, gratuit pour une durée limitée sur Nous Portal. Teknium précise qu'il n'est disponible sur Nous Portal que pour un temps limité.

witcheer détaille la marche à suivre dans Hermes Agent : pour les nouveaux venus, hermes setup --portal ouvre la connexion à Nous Portal ; ensuite, /model stealth/missingno sélectionne le modèle dans n'importe quelle conversation ; ajouter --global en fait le modèle par défaut. Le message évoque 262 K de contexte et l'appel d'outils.

> Sources : [@NousResearch, Wild MISSINGNO. appeared!, 10 octobre 2026](https://x.com/NousResearch/status/2109012611555840069), [@Teknium, New stealth model, only on Nous Portal for a limited time!, 10 octobre 2026](https://x.com/Teknium/status/2109012782897356985) et [@witcheer, a wild model on Nous Portal, here's how to catch it in Hermes Agent, 10 octobre 2026](https://x.com/witcheer/status/2109016297375666268)

## Wingtips #97 : laisser l'agent poser ses questions avant de commencer

witcheer a consacré le numéro 97 des Wingtips à la clarification préalable. Ajouter « ask me a few questions first » à son message invite l'agent à vérifier les détails avant de se lancer. Dans le terminal, l'agent regroupe ses questions dans un panneau unique, avec des choix à cocher ou de la place pour une réponse libre.

Cette consigne s'appuie sur l'outil clarify. Il pose de une à cinq questions, chacune sous trois formes : choix unique parmi quatre options au plus (avec une voie « Other » pour taper sa propre réponse), choix multiple, ou question ouverte. Le terminal et le TUI affichent une liste compacte, Desktop présente toutes les questions sur une seule carte, et les plateformes de messagerie les posent une par une.

> Sources : [@witcheer, Hermes Wingtips #97: let your agent ask before it starts, 11 octobre 2026](https://x.com/witcheer/status/2109184368052777380) et [Toolsets Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference/)

## 55 pull requests fusionnées le 10 octobre

iamlukethedev a fait le compte le 11 octobre : Hermes a fusionné 55 pull requests le 10 octobre. Trois changements figurent dans le texte du message :

- Desktop gagne, dans Réglages puis À propos, le choix du canal de mise à jour pour les installations depuis les sources : versions stables ou chaque commit.
- hermes update et les mises à jour de Desktop suivent les versions stables par défaut.
- Les mises à jour de Desktop sur macOS ne refusent plus leur propre relais.

La documentation des mises à jour précise la mécanique du canal. Une installation depuis les sources suit désormais le canal stable : la dernière release vX.Y.Z publiée sur GitHub, jamais les brouillons, préversions ni tags canary, à son commit exact. hermes update --set-channel main fait suivre chaque commit de main, et --set-channel stable ramène aux releases. Le choix est stocké par installation sous update.installs dans config.yaml. Le blocage macOS, lui, venait du verrou de mise à jour qui refusait son propre relais (code de sortie 2) sur les installations antérieures à un certain commit : la mise à jour échouait avant même de récupérer le correctif, puisque la décision de refus intervenait avant le git pull.

> Sources : [@iamlukethedev, Hermes merged 55 PRs on October 10, 11 octobre 2026](https://x.com/iamlukethedev/status/2109076128594104448), [Updating & Uninstalling, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/updating) et [macOS Desktop in-app update deadlocks on pre-a28a5d03a9f installs, issue NousResearch/hermes-agent #135498](https://github.com/NousResearch/hermes-agent/issues/135498)

## Hermes Desktop peut piloter un backend distant

witcheer a répondu le 11 octobre à une question récurrente : peut-on faire tourner Hermes Desktop sur son portable pendant que l'agent vit sur une autre machine ? Oui. Par défaut, l'application démarre son propre backend local, mais elle peut être dirigée vers un backend Hermes sur un VPS, un serveur domestique ou un Mini derrière Tailscale.

La documentation de Desktop détaille le branchement. Le backend distant est un processus hermes dashboard en cours d'exécution sur la machine distante, que l'application ne démarre pas elle-même : un service systemd ou l'utilisateur le maintient en vie. Côté application, Réglages puis Passerelles puis Passerelle distante ouvre la configuration : on saisit l'URL du backend (par exemple http://hôte:9119), on s'authentifie, puis on enregistre et on se reconnecte. Deux fournisseurs d'authentification sont possibles : OAuth via Nous Portal, recommandé pour tout backend accessible au-delà de sa propre machine, ou un couple identifiant et mot de passe. L'hôte de la passerelle distante est configuré par profil, chaque profil pouvant pointer vers son propre backend distant.

> Sources : [@witcheer, Hermes Desktop on your laptop, your Hermes Agent on another machine, 11 octobre 2026](https://x.com/witcheer/status/2109255720411574606) et [Hermes Desktop, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
