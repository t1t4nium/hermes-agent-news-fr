# Hermes Agent Quotidien #75

Cette édition revient sur l'arrivée de Hermes Agent sur le Microsoft Store, sur le plugin first-party TinyFish, sur le numéro 96 des Wingtips consacré à la commande /undo, sur les 88 pull requests fusionnées le 8 octobre, et sur les nouveaux ajouts de Herald OS.

## Hermes Agent arrive sur le Microsoft Store

Nous Research a annoncé le 8 octobre que Hermes Agent est désormais en ligne, et mis en avant, sur le Microsoft Store, pour une installation en un clic sous Windows. La société annonce d'autres mises à jour à venir pour l'écosystème Windows. witcheer résume la marche à suivre : ouvrir le Microsoft Store, chercher Hermes Agent, cliquer sur Obtenir.

La documentation d'installation précise les détails du paquet. Le MSIX autonome requiert Windows 11 22H2 ou plus récent, et intègre Python, Node et les dépendances de base, sans clonage ni compilation au premier lancement. Les alias d'exécution exposent hermes, hermes-agent et hermes-acp. La variante du Microsoft Store utilise l'identité de paquet du Partner Center et les mises à jour du Store, sans passer par le flux de sideload ; hermes update ne lance pas git sur les fichiers du paquet dans ce contexte.

> Sources : [@NousResearch, Hermes Agent is now live (and featured) in the Microsoft Store, 8 octobre 2026](https://x.com/NousResearch/status/2108231536772596193), [@witcheer, Windows friends, this one's for you, 8 octobre 2026](https://x.com/witcheer/status/2108232825107263658) et [Windows (Native) Guide, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)

## TinyFish : un plugin first-party pour chercher et naviguer

KeithZhai a annoncé le 9 octobre l'ajout de TinyFish comme plugin first-party de Hermes Agent. Le plugin permet de chercher et de récupérer le web en direct, gratuitement, à l'intérieur des outils que Hermes exécute déjà ; le navigateur et l'agent s'arrêtent et demandent avant de dépenser un crédit. L'installation se fait par hermes plugins install tinyfish. Teknium renvoie vers le backend de navigateur TinyFish sur le catalogue de plugins.

La page du catalogue détaille les trois capacités : Search et Fetch, gratuits, branchés derrière web_search et web_extract via le fournisseur web tinyfish ; Browser, qui route les outils de navigateur de Hermes vers des sessions distantes TinyFish, consommatrices de crédits ; et Agent, un outil tinyfish_agent d'automatisation pilotée par objectif sur un site réel. La voie d'installation recommandée passe par la CLI TinyFish (tinyfish connect hermes), qui installe le plugin depuis npm, dépose la clé API et branche les backends web. L'authentification repose sur une clé TINYFISH_API_KEY, résolue depuis la variable d'environnement ou depuis MCP_TINYFISH_API_KEY. Le plugin enregistre une commande hermes tinyfish (setup, status, doctor, credits, browser, usage) et une commande de session /tinyfish-status. Les dépenses sont encadrées par une politique de crédits à trois positions : request (approbation par défaut), allow et deny.

> Sources : [@KeithZhai, Hermes just added TinyFish as a first-party plugin, 9 octobre 2026](https://x.com/KeithZhai/status/2108354564437266697), [@Teknium, Check out the new TinyFish browser backend on the plugins catalog!, 9 octobre 2026](https://x.com/Teknium/status/2108382428427612589) et [tinyfish, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/tinyfish)

## Wingtips #96 : la commande /undo pour retirer le dernier échange

witcheer a consacré le numéro 96 des Wingtips à la commande /undo. Elle retire du fil le dernier message de l'utilisateur et la réponse de l'agent, puis l'agent reprend à partir du message précédent, ce qui permet de reformuler sa demande autrement. L'exemple d'usage : envoyer un message, se rendre compte qu'on voulait le formuler différemment, puis taper /undo et redemander.

La référence des commandes slash précise la mécanique. /undo retire le dernier échange utilisateur et assistant de l'historique. C'est une commande destructive, au même titre que /clear, /new et /exit --delete : le CLI ouvre une confirmation à trois choix, Approve Once, Always Approve ou Cancel, sauf à forcer l'exécution avec /undo -y ou /undo now. La désactivation globale se fait par approvals.destructive_slash_confirm: false dans config.yaml.

> Sources : [@witcheer, Hermes Wingtips #96: take back your last message, 9 octobre 2026](https://x.com/witcheer/status/2108518464134484398) et [Slash Commands Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## 88 pull requests fusionnées le 8 octobre

iamlukethedev a fait le compte le 9 octobre : Hermes a fusionné 88 pull requests le 8 octobre. Deux changements figurent dans le texte du message :

- Les appels d'outils Copilot Responses ne s'exécutent plus deux fois avec des arguments vides {}.
- /yolo est désormais un contrat de session unique à travers le CLI, le TUI, Desktop et la passerelle. Il survit aux redémarrages du backend et aux sessions reprises.

La documentation de sécurité rappelle ce que fait /yolo : c'est un basculeur qui court-circuite tous les prompts d'approbation des commandes dangereuses pour la session en cours, en positionnant HERMES_YOLO_MODE. Il ne lève pas la liste de blocage irréductible, celle des commandes catastrophiques que Hermes refuse d'exécuter quoi qu'il arrive.

> Sources : [@iamlukethedev, Hermes merged 88 PRs on October 8, 9 octobre 2026](https://x.com/iamlukethedev/status/2108422141679190067) et [Security, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security)

## Herald OS gagne un éditeur photo et une suite bureautique

iamlukethedev a continué d'étoffer Herald OS, son système d'exploitation autour de Hermes Agent, mis en open source le 7 octobre. Le 8 octobre, il a présenté Herald Canvas, un éditeur photo que l'on pilote à la voix : « Remplis ma sélection », « Détoure-la et floute l'arrière-plan », « Ajoute un titre gras avec un halo chaud ». L'IA tourne en local sur l'appareil, sans cloud.

Le 9 octobre, il a annoncé l'intégration de Word, Excel et PowerPoint dans Herald OS, tous propulsés par Hermes Agent et pilotables à la voix. « Rends ce document plus professionnel » fait réécrire le texte par Hermes ; « Calcule mes dépenses mensuelles » lui fait construire les formules ; « Transforme ce document en... » amorce une conversion.

> Sources : [@iamlukethedev, I built a photo editor into Herald OS, 8 octobre 2026](https://x.com/iamlukethedev/status/2108131773666168966) et [@iamlukethedev, I just built Word, Excel, and PowerPoint into Herald OS, 9 octobre 2026](https://x.com/iamlukethedev/status/2108520360052433317)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
