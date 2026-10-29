# Hermes Agent Quotidien #95

Cette édition revient sur les 55 pull requests fusionnées le 28 octobre, sur Herald qui prépare une application de bureau réunissant tous les bots dans une seule fenêtre, sur le plugin communautaire Tracekit qui vérifie chaque appel d'outil avant son exécution, et sur le conseil Wingtips #113 consacré au changement de projet depuis le chat.

## 55 pull requests fusionnées le 28 octobre

Le changelog du 28 octobre relève 55 pull requests fusionnées. iamlukethedev a fait le compte et met en avant ce qui touche à la Webapp : elle se comporte désormais comme si l'on était sur sa propre machine. Les changements à retenir :

- La Webapp utilise la même identité que Desktop : les sessions et les conversations de groupe sont partagées entre les deux.
- Un backend autonome et la Webapp partagent une seule liste de conversations de groupe, et l'attachement de fichiers fonctionne sur le backend local.
- Les conversations de groupe reprises d'un backend autonome envoient de nouveau les messages et réveillent leurs membres.
- Le jeton de session de déploiement autorise l'accès au tableau de bord fermé, et le backend peut le lire depuis un fichier.
- web_extract signale désormais une réponse HTTP 4xx ou 5xx comme une erreur au lieu de la traiter comme une extraction réussie.
- Firecrawl revérifie la politique du site contre l'URL de redirection, après avoir suivi les redirections.
- capture_screenshot ne se bloque plus soixante secondes sur un onglet masqué.
- Les nouveaux agents hébergés sous Docker ne reconstruisent plus leur environnement virtuel au premier démarrage pour obtenir fal.

Le changelog relève aussi le plugin de configuration à distance Hermes Cloud, un mode opt-in qui permet à un administrateur de piloter les réglages depuis un service central au lieu des fichiers locaux.

> Sources : [Hermes Bible, changelog du 28 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-28) et [@iamlukethedev, Hermes merged 55 PRs on October 28, 29 octobre 2026](https://x.com/iamlukethedev/status/2115624153479098376)

## Herald prépare une application de bureau

iamlukethedev a annoncé le 29 octobre que Herald arrive sur le bureau. Déjà utilisateur de Hermes Agent sur Mac, Herald le trouve et, en un clic, réunit tous les bots dans une seule fenêtre. L'annonce détaille ce qui est prévu : des conversations de groupe où les bots travaillent ensemble, l'un pouvant même vérifier les calculs d'un autre, une vue partagée pour faire tourner deux chats côte à côte, et des images affichées dans le chat plutôt qu'un chemin de fichier.

Le projet se veut léger : 0,7 % de CPU au repos, un défilement de 2 000 messages à 120 images par seconde et des réponses à l'écran en 32 millisecondes. La sortie est annoncée comme prochaine. Herald est un projet indépendant de Luke The Dev, sans lien avec Nous Research, qui repose sur Hermes Agent ; il s'appuie sur son propre dépôt Herald-OS et le canal d'annonce du développeur.

> Sources : [@iamlukethedev, Herald is coming to the desktop, 29 octobre 2026](https://x.com/iamlukethedev/status/2115641501061697885) et [iamlukethedev/Herald-OS, dépôt GitHub](https://github.com/iamlukethedev/Herald-OS)

## Tracekit, chaque appel d'outil vérifié avant d'être exécuté

witcheer a présenté le 29 octobre Tracekit, un plugin communautaire de Cygnux Labs. Les appels d'outil de l'agent sont vérifiés avant de s'exécuter : autorisé, bloqué ou retenu jusqu'à l'approbation. Sa démonstration envoie trois appels scriptés, un ls autorisé, un téléchargement passé à un shell bloqué et un branchement distant.

Le catalogue précise le fonctionnement. Tracekit enregistre chaque appel d'outil comme un événement signé et chaîné par hachage, écrit par un signataire que l'agent ne contrôle pas. Un refus bloque l'appel, une demande d'avis attend l'approbation d'une personne. Chaque session Hermes forme un run, clos à la sortie de l'agent, exportable et vérifiable hors ligne. Le plugin enregistre deux hooks, pre_tool_call et post_tool_call, et rien d'autre. Il dépend de tracekit-ai 1.4.2 ou plus récent, et exige la variable TRACEKIT_SIGNER_TOKEN. Par défaut, sans signataire configuré, le premier appel démarre le signataire de développement du même utilisateur en local. En cas de refus ou de défaillance, l'appel est bloqué.

> Sources : [@witcheer, your Hermes Agent's tool calls get checked before they run, 29 octobre 2026](https://x.com/witcheer/status/2115639775789223991) et [tracekit, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/tracekit)

## Wingtips #113, changer de projet depuis le chat

witcheer a publié le 29 octobre le conseil Wingtips #113. Un projet dans Hermes Agent est un espace de travail nommé qui peut contenir plusieurs dossiers, par exemple un dépôt API et un dépôt web pour une même application. Dans Hermes Desktop, on peut déplacer un chat vers l'un d'eux en demandant simplement : switch this chat to my Recipe Box project. Hermes trouve le projet par son nom et déplace l'espace de travail du chat vers le dossier principal du projet. Demander quels projets existent les liste, en indiquant celui du chat courant.

La page de la série rappelle la documentation de l'outil de projet : l'action desktop_project couvre les trois verbes create, list et switch, et le changement est un appel d'outil explicite, jamais un effet de bord d'un cd.

> Sources : [@witcheer, Hermes Wingtips #113: switch projects from the chat, 29 octobre 2026](https://x.com/witcheer/status/2115817431616598488), [Hermes Wingtips #113, hermes recipes](https://notwitcheer.github.io/hermes-recipes/wingtips/113-switch-projects/) et [Built-in Tools Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/tools-reference)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
