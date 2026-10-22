# Hermes Agent Quotidien #88

Cette édition revient sur la release de correctifs v0.22.4, sur les 59 pull requests fusionnées le 21 octobre, sur Herald passé en bêta publique sur TestFlight, sur le plugin officiel Meshy, sur la démonstration Hermes qui a clos le keynote GTC Berlin de Jensen Huang, et sur le conseil Hermes Wingtips #108 consacré à la mémoire.

## Hermes Agent v0.22.4, correctifs et nouveaux plugins

Teknium a publié le 21 octobre la release de correctifs v0.22.4. Desktop n'affiche plus les pastilles de suggestion au-dessus du composeur, elles apparaissaient sans raison claire et poussaient surtout à configurer des serveurs MCP. Les autres changements :

- Un plugin qui n'installe aucune dépendance ne passe plus par l'étape de consentement aux dépendances.
- Dans le tableau de bord, WhatsApp peut être réapparié sans risque après une déconnexion.
- La révision des plugins de Desktop ne signale plus les écritures de prototype comme des erreurs de surface.
- La pastille du mode d'approbation suit le mode du profil actif.
- La vérification pré-build du paquet Desktop a désormais assez de temps pour valider les entrées archivées quand le stockage est lent.

La release ajoute aussi au catalogue bubblewrap, Singularity/Apptainer, mcp-serve (Hermes comme serveur MCP), agent-importers (avec Cursor désormais), inbox et workflow-record. Telegram Business rejoint le palier communautaire Hermes Labs. Mesurée au commit 4d04303818b, la fenêtre depuis v0.22.3 compte 14 commits sans fusion sur 82 fichiers modifiés (+1 475 / -3 022) et 13 pull requests fusionnées.

> Sources : [Dépôt GitHub de Hermes Agent, Hermes Agent v0.22.4, 21 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.4)

## 59 pull requests fusionnées le 21 octobre

iamlukethedev a fait le compte le 22 octobre : Hermes a fusionné 59 pull requests le 21 octobre. Les changements mis en avant :

- Les serveurs MCP peuvent déclarer le coût d'un outil et un plafond de dépense par conversation, et la demande d'approbation affiche le coût d'un appel avant de le valider.
- Gros jour pour le catalogue de plugins : Meshy, bubblewrap, Singularity/Apptainer, inbox et workflow-record y font leur entrée.

Le changelog du 21 octobre montre aussi une vague de mises à jour de dépendances pour corriger des failles de sécurité, dont simple-git, oauthlib, KaTeX et Vite.

> Sources : [@iamlukethedev, Hermes merged 59 PRs on October 21, 22 octobre 2026](https://x.com/iamlukethedev/status/2113082142855143529) et [Hermes Bible, changelog du 21 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-21)

## Herald, l'application Hermes Bots, en bêta publique sur TestFlight

iamlukethedev a annoncé le 22 octobre que Herald est en bêta publique sur TestFlight, une journée après son envoi en review chez Apple. La mise en place prend moins d'une minute : lancer une commande sur son ordinateur, scanner le QR code, et les bots Hermes arrivent sur l'iPhone. Herald comprend les notes vocales, les conversations de groupe, les approbations, un tableau Kanban, un écran pour les bots et l'Apple Watch.

> Sources : [@iamlukethedev, Herald is now in public beta on TestFlight, 22 octobre 2026](https://x.com/iamlukethedev/status/2113196811825664372)

## Le plugin officiel Meshy pour créer des modèles 3D

Nous Research a annoncé le 22 octobre le plugin officiel Meshy pour Hermes Agent. On peut demander un coffre au trésor de 70 millions de polygones pour Godot, ou transformer la photo d'une tasse en modèle à imprimer, et l'agent fait le travail via le serveur MCP de Meshy. Dans Hermes Desktop, les modèles sont rendus dans la conversation. Teknium ajoute qu'on peut créer n'importe quel modèle 3D, du personnage au dragon en passant par les armures de jeu et les figurines à imprimer, avec des modèles rendus, des animations et une galerie.

> Sources : [@NousResearch, Hermes Agent now has an official plugin for MeshyAI, 22 octobre 2026](https://x.com/NousResearch/status/2113077994315034967) et [@Teknium, Check out the new official MeshyAI plugin, 22 octobre 2026](https://x.com/Teknium/status/2113139938569179201)

## La démonstration Hermes clôt le keynote GTC Berlin de Jensen Huang

Nous Research a signalé le 21 octobre que Jensen Huang a clos son keynote GTC Berlin 2026 par une démonstration de Hermes Agent. Il a introduit le sujet en disant que la façon de construire un agent est de demander à un agent de le construire, puis il a installé et configuré un Hermes personnalisé en une seule requête avant de s'en servir. tonbistudio salue de son côté la reconnaissance de Hermes par Jensen dans ce keynote, et rappelle que l'open source est le seul moyen de vraiment posséder ses agents et de garder le contrôle des outils disponibles.

> Sources : [@NousResearch, Jensen closed his GTC Berlin 2026 keynote with this Hermes Agent demo, 21 octobre 2026](https://x.com/NousResearch/status/2113010017645244623) et [@tonbistudio, Incredible to see Hermes recognized by Jensen in this keynote, 22 octobre 2026](https://x.com/tonbistudio/status/2113102215028342998)

## Hermes Wingtips #108, installer un fournisseur de mémoire

witcheer a publié le 22 octobre le conseil Hermes Wingtips #108. Hermes Agent garde sa propre mémoire dans MEMORY.md et USER.md, et un fournisseur de mémoire tourne à côté pour ajouter la recherche sémantique, les graphes de connaissances et l'extraction automatique de faits. Une commande guide l'ajout d'un tel fournisseur.

> Sources : [@witcheer, Hermes Wingtips #108: hermes memory setup, 22 octobre 2026](https://x.com/witcheer/status/2113170993082765672)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
