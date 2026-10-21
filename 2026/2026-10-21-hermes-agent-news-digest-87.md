# Hermes Agent Quotidien #87

Cette édition revient sur la release stable v0.22.3, qui regroupe environ 620 pull requests, sur les 160 pull requests fusionnées le 20 octobre, sur Herald, l'application Hermes Bots partie en review Apple, sur Memory Pane et Draft Cards, deux nouveaux moyens de garder la main sur ce que l'agent retient et écrit, et sur le passage du catalogue de plugins au-dessus de 750 entrées.

## Hermes Agent v0.22.3, une release stable qui regroupe 620 pull requests

Teknium a publié le 21 octobre la release stable v0.22.3. C'est une release de correctifs qui rassemble les quelque 620 pull requests fusionnées depuis v0.22.2 dans une version stable pour le CLI et l'installateur, l'application du Microsoft Store, Docker et Hermes Cloud. Mesurée au commit 5b147ab036d, la fenêtre depuis v0.22.2 compte 2 911 commits sans fusion sur 4 206 fichiers modifiés (+360 278 / -64 308), environ 620 pull requests fusionnées et 326 tickets fermés. Les notes listent aussi, sans entrer dans le détail, ce qui a atterri dans la fenêtre :

- Le CLI classique retrouve un agencement rafraîchi : transcription en glyphes, ligne d'état sous le composeur, en-tête sur deux lignes.
- Les plugins déclarent des clients OAuth et Hermes assure la connexion puis le rafraîchissement des jetons.
- `hermes plugins update` propose toutes les mises à jour disponibles, avec un bouton de mise à jour dans Desktop pour les plugins installés via git.
- Depuis Desktop, une invite déjà en file peut être pilotée et modifiée, et un sous-agent se choisit un modèle et un fournisseur guidés.
- Un compte à rebours `/loop` s'affiche en direct dans le CLI et le TUI.
- Le transfert des sujets privés Telegram devient opt-in, et le hook plugin `post_compaction` arrive.
- Le catalogue des capacités fait son entrée, et le build Microsoft Store se publie automatiquement à chaque release.
- L'auto-prune des sessions revient en opt-in, avec une invite unique quand le disque se remplit.
- Nemotron 3.5 Bolt et les brouillons DFlash à un emplacement rejoignent le runtime local.

Les notes complètes et curées pour cette fenêtre arriveront avec la v0.23.0, qui documentera tout depuis la v0.22.0.

> Sources : [Dépôt GitHub de Hermes Agent, Hermes Agent v0.22.3, 21 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.3)

## 160 pull requests fusionnées le 20 octobre

iamlukethedev a fait le compte le 21 octobre : Hermes a fusionné 160 pull requests le 20 octobre. Les changements mis en avant :

- Krea 3 passe par la passerelle gérée et devient le modèle d'image par défaut des abonnés payants, avec des retouches guidées par instruction et plusieurs images de référence.
- Les outils MCP diffusent leur avancement en direct : une ligne dans Desktop, un spinner dans le CLI et un événement plugin pendant qu'ils travaillent.
- Le catalogue des capacités de Desktop, qui réunit skills, plugins, connecteurs et outils, a été redessiné.
- L'outil Git Review, dans Desktop, montre les changements de code et permet de citer des lignes précises dans le brouillon.
- Le plugin hermes-board ajoute un tableau blanc que l'agent remplit et que l'on édite dans un volet de Desktop.
- L'élément de barre d'état burnclock affiche le solde du fournisseur et l'autonomie estimée.

> Sources : [@iamlukethedev, Hermes merged 160 PRs on October 20, 21 octobre 2026](https://x.com/iamlukethedev/status/2112760406662168960) et [Hermes Bible, changelog du 20 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-20)

## Herald, l'application Hermes Bots envoyée en review Apple

iamlukethedev a annoncé le 21 octobre que Herald, l'application Hermes Bots, part enfin en review chez Apple. Il s'excuse du retard et explique qu'il aurait pu la sortir plus tôt, mais qu'il tenait à une application qu'il soit fier de faire payer. Il a reçu plus de 200 retours des personnes qui testaient Herald, les a passés en revue et en a retenu une partie avant l'envoi.

> Sources : [@iamlukethedev, Hermes Bots aka Herald is finally going to Apple for review, 21 octobre 2026](https://x.com/iamlukethedev/status/2112843319864959341)

## Memory Pane, voir ce que l'agent retient

Adolan a présenté le 21 octobre Memory Pane, un plugin pour Hermes Desktop qui répond à un reproche récurrent sur la mémoire de l'agent : savoir exactement ce qu'il enregistre, ce qu'il retiendra et ce qu'il écarte. Tout ce que Hermes sauvegarde, met à jour ou oublie s'affiche en direct à côté de la conversation, et chaque entrée peut être modifiée, supprimée ou annulée, sans appel réseau ni télémétrie. Le changelog du 20 octobre liste de son côté un panneau de mémoire ajouté à l'interface du chat, pour suivre en temps réel ce que l'agent mémorise et corriger ses erreurs.

> Sources : [@adolandev, Memory Pane for Hermes Desktop, 21 octobre 2026](https://x.com/adolandev/status/2112774433567891465), [@witcheer, Adolan built a plugin that does exactly that, 21 octobre 2026](https://x.com/witcheer/status/2112786467697447033) et [Hermes Bible, changelog du 20 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-20)

## Draft Cards, relire chaque brouillon avant l'envoi

witcheer a signalé le 21 octobre le plugin Draft Cards, pour celles et ceux qui veulent que leur agent écrive leurs courriels tout en gardant un oeil sur chaque message avant l'envoi. Le plugin affiche chaque brouillon sous forme de carte dans Hermes Desktop ; on demande alors des modifications ou on édite soi-même. Le changelog du 20 octobre le confirme : les brouillons s'affichent en cartes interactives plutôt qu'en texte brut, avec édition en place et suivi des versions.

> Sources : [@witcheer, Draft Cards show every draft in Hermes Desktop, 21 octobre 2026](https://x.com/witcheer/status/2112853908049502634) et [Hermes Bible, changelog du 20 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-20)

## Le catalogue de plugins passe la barre des 750 entrées

witcheer a annoncé le 21 octobre que le catalogue de plugins de Hermes Agent a dépassé les 750 entrées : mémoire, voix, messagerie, navigation et plus encore, construites par la communauté. Il demande d'ailleurs lequel tester et mettre en avant.

> Sources : [@witcheer, the Hermes plugin catalog has passed 750 plugins, 21 octobre 2026](https://x.com/witcheer/status/2112876556767150082)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
