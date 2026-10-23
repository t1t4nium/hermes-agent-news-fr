# Hermes Agent Quotidien #89

Cette édition revient sur la release de correctifs v0.22.5, sur les 48 pull requests fusionnées le 22 octobre, sur le plugin Cua Spaces qui donne à Hermes une machine isolée, sur l'arrivée de Herald sur Android, sur l'offre Meshy à un dollar et sur Uncommon Web, le guide de bibliothèques web bâti par Hermes.

## Hermes Agent v0.22.5, correctifs et délégation branchable

Teknium a publié le 22 octobre la release de correctifs v0.22.5. Elle regroupe les 81 pull requests fusionnées depuis v0.22.4 dans une version stable pour la release GitHub (CLI et installateurs), l'application du Microsoft Store, Docker et Hermes Cloud. Mesurée au commit bf0203a794a, la fenêtre depuis v0.22.4 compte 231 commits sans fusion sur 804 fichiers modifiés (+35 212 / -17 885), 81 pull requests fusionnées et 30 tickets fermés. Les notes complètes et curées de cette fenêtre arriveront avec la v0.23.0. En attendant, la release liste les changements suivants :

- La connexion Nous est refaite : chaque connexion passe par le device login simple, l'invité du palier gratuit bascule vers le compte, le résultat affiche qui s'est connecté et les connecteurs proposent de se connecter au lieu d'ouvrir un invité.
- `hermes update` retient une release stable qu'il refuse au lieu de la proposer.
- Sur Windows, `hermes update` ne reste plus bloqué sur l'ancien lanceur après le changement de la version épinglée de Python.
- Les plans à fenêtre d'usage sont pris en charge : jauges de plan, cartes de limite et récupération de changement de modèle.
- Les backends de délégation deviennent branchables : les sous-agents se routent par carte de modèles ou par profil, changeable par session.
- Les commandes slash d'un plugin peuvent demander de choisir une option.
- `hermes import-agent` arrive, avec la migration OpenClaw.
- `hermes mcp serve` et le backend Singularity sortent du coeur vers les plugins, et l'installation propose l'importeur quand elle trouve un autre agent.
- Dans Desktop, épinglage par glisser-déposer dans la barre latérale et installation de plugins en un clic avec badges de palier.
- Passage à Electron 44 et à Pillow 13, avec une série de mises à jour de dépendances de sécurité.
- Un message clair s'affiche quand le dossier de travail d'une conversation a disparu.
- `hermes update` récupère les passerelles en pause après un `.git` endommagé.
- Les longues réponses Claude DirectSDK ne sont plus coupées par le minuteur de blocage.
- Les conversations de groupe de Desktop indiquent de nouveau quel bot travaille.
- Le client d'événements MCP en mode webhook, encore expérimental, fait son entrée.

> Sources : [Dépôt GitHub de Hermes Agent, Hermes Agent v0.22.5, 22 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.5)

## 48 pull requests fusionnées le 22 octobre

iamlukethedev a fait le compte le 23 octobre : Hermes a fusionné 48 pull requests le 22 octobre. Les changements mis en avant :

- La délégation devient branchable : on choisit un backend (défaut, carte de modèles ou profils), et Desktop gagne un écran de réglages avec un sélecteur de mode, un éditeur de routes de modèles et des routes de profils.
- La délégation avancée rejoint le catalogue officiel.

Le changelog du 22 octobre relève aussi le support des plans à fenêtre d'usage, la correction de la résolution des dépendances avec uv face à la dernière version de uv, le correctif du lanceur Windows après le changement de version épinglée de Python, la mise à jour de edge-tts qui lève l'erreur 403 de Edge TTS, le glisser-déposer des sessions pour les épingler dans la barre latérale, et la sortie de `hermes mcp serve` vers le plugin mcp-serve.

> Sources : [@iamlukethedev, Hermes merged 48 PRs on October 22, 23 octobre 2026](https://x.com/iamlukethedev/status/2113578058162803014) et [Hermes Bible, changelog du 22 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-22)

## Cua Spaces, une machine isolée pour Hermes

Nous Research a annoncé le 22 octobre le plugin Cua Spaces. Il donne à Hermes son propre espace Linux, macOS ou Windows sur le matériel déjà possédé, et toute l'équipe peut l'ouvrir, regarder en direct, intervenir et rendre la main pendant que Hermes continue. iamlukethedev précise que le plugin déplace le terminal, les fichiers et l'exécution du code de Hermes vers une machine isolée, tandis que Hermes reste sur l'ordinateur : on peut regarder le travail en direct, cliquer pour reprendre la main, puis laisser Hermes continuer à côté. witcheer ajoute qu'une seule ligne de configuration suffit, `hermes config set terminal.backend cua`, et qu'à la fin de la tâche l'espace est supprimé.

> Sources : [@NousResearch, Your team and your Hermes can now share a computer, 22 octobre 2026](https://x.com/NousResearch/status/2113391397760041329), [@iamlukethedev, The Cua Spaces plugin moves Hermes's terminal, files and code runs, 22 octobre 2026](https://x.com/iamlukethedev/status/2113400693642150221) et [@witcheer, when a task needs a computer, 23 octobre 2026](https://x.com/witcheer/status/2113484931024245176)

## Herald arrive sur Android

iamlukethedev a annoncé le 23 octobre que Herald, l'application Hermes Bots, est désormais sur Android, au lendemain de sa bêta publique sur TestFlight. La mise en place reste la même : lancer une commande sur son ordinateur, scanner le code, et les bots Hermes arrivent dans la poche. On peut approuver une étape risquée depuis la notification, partager un lien depuis Chrome directement vers un bot, et créer des conversations de groupe où les bots interviennent à tour de rôle.

> Sources : [@iamlukethedev, Herald is on Android, 23 octobre 2026](https://x.com/iamlukethedev/status/2113434773901472088)

## Meshy propose un mois de Pro à un dollar

Nous Research a annoncé le 22 octobre que Meshy offre aux utilisateurs de Hermes un mois du plan Pro, qui comprend l'accès à l'API et 1 000 crédits, pour un dollar. Après l'abonnement et l'installation du plugin, on crée une clé sur meshy.ai puis on la colle dans Réglages, Plugins, Meshy dans Hermes Desktop. Teknium précise que Meshy a contacté l'équipe au lancement du plugin et fourni des coupons à distribuer. witcheer rappelle ce que le plugin permet depuis une conversation : transformer un prompt ou une photo en modèle 3D, le texturer, lui ajouter un rig, l'animer et le préparer à l'impression. Sur la grille tarifaire de Meshy, le plan Pro est normalement facturé 20 dollars par mois.

> Sources : [@NousResearch, Meshy is offering Hermes users a month of Pro for $1, 22 octobre 2026](https://x.com/NousResearch/status/2113375941431009526), [@Teknium, Meshy reached out when we were launching our plugin, 22 octobre 2026](https://x.com/Teknium/status/2113376247221022731), [@witcheer, Meshy is offering every Hermes users 1,000 credits for $1 a month, 23 octobre 2026](https://x.com/witcheer/status/2113463039005475117) et [Meshy, grille tarifaire](https://www.meshy.ai/pricing)

## Uncommon Web, le guide de bibliothèques web bâti par Hermes

Teknium a raconté le 22 octobre qu'on lui a montré une bibliothèque JavaScript de tramage, qu'il l'a donnée à Hermes Agent en demandant une page web pleine de démos de bibliothèques de styles et de composants peu connues, et qu'en vingt minutes le site était là. Il a continué à l'alimenter toute la journée, passant d'environ 75 trouvailles à 462 démos couvrant 425 bibliothèques dans 23 sections. Le site, Uncommon Web, se présente comme un guide de terrain des bibliothèques web stylistiquement inhabituelles : chaque démo est exécutable, accompagnée de la commande d'installation, d'un extrait de code et de la licence. Les sections vont du tramage, du pixel et de l'ASCII aux graphiques en braille et aux moteurs de jeu.

> Sources : [@Teknium, I gave it to Hermes Agent, make me a webpage full of demos, 22 octobre 2026](https://x.com/Teknium/status/2113265212484636929), [@Teknium, now at 462 demos covering 425 libraries in 23 sections, 23 octobre 2026](https://x.com/Teknium/status/2113505088572694769) et [Uncommon Web, webdev.teknium.io](https://webdev.teknium.io/)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
