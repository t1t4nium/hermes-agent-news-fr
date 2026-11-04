# Hermes Agent Quotidien #101

Cette édition revient sur la release stable v0.22.7, sur les 54 pull requests fusionnées le 3 novembre, sur la première place de Hermes Agent dans le classement Octoverse 2026 de GitHub, sur le modèle furtif Crouton Alpha, et sur l'ouverture de la liste d'attente de l'application mobile.

## Hermes v0.22.7 passe en stable

La note de release, publiée le 3 novembre par teknium1, marque le passage de Hermes v0.22.7 en stable. C'est une release de correctifs qui roule en stable les quelque 174 pull requests fusionnées depuis v0.22.6, pour le CLI et les installeurs, l'application Microsoft Store, Docker et Hermes Cloud. Mesurée au commit b200f5bc60e, la fenêtre contient 581 commits sans fusion sur 554 fichiers modifiés (+24 012 / -3 144) et 29 issues fermées. Les notes curées et complètes partiront avec v0.23.0.

La note liste aussi, sans les détailler, les changements marquants de la fenêtre :

- Le routage opt-in par chef de file pour les groupes de Desktop, avec un badge Lead sur l'en-tête de la pièce.
- Des tâches cron qui postent dans les groupes, une raison d'être et des notes partagées par pièce, et des pièces de groupe affichées dans une seule colonne de discussion avec l'état en direct de chaque membre.
- Des tableaux Kanban épinglés comme onglets de bascule rapide.
- Des libellés de diagrammes `$$TeX$$` et des diagrammes mermaid rendus via Pele.
- Une boîte d'erreur de mise à jour de Desktop qui montre la sortie de l'échec avec un lien de signalement.
- Web Access qui nomme l'étape sur laquelle Start se trouve, avec un compteur qui tourne.
- Telegram sur Team Gateway, configuré en liant un compte au bot partagé.
- Un silence `thread_followup_silence` opt-in pour Slack sur les réponses de fil sans suite.
- Un interrupteur Daybreak pour les modèles d'abonnement ChatGPT listés au catalogue.
- Une salve de nouvelles entrées au catalogue de plugins.

> Source : [Hermes Agent v0.22.7, note de release GitHub, 3 novembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.7)

## 54 pull requests fusionnées le 3 novembre

iamlukethedev a fait le compte le 4 novembre : Hermes a fusionné 54 pull requests le 3 novembre. Il en retient trois. Les tâches cron peuvent désormais poster dans les groupes et ne réveillent que les bots qu'elles mentionnent, et les pièces reçoivent une raison d'être et des notes partagées. Les pièces de groupe ressemblent désormais au chat natif et affichent l'état en direct de chaque bot. Et le routage opt-in par chef de file arrive pour les groupes.

Le changelog du 3 novembre précise et complète :

- Un chef de file désigné dans un groupe peut décider qui traite les messages qui ne nomment personne (#148417).
- Les groupes peuvent de nouveau accueillir des bots installés sur des machines différentes (#148418).
- Les skills optionnelles que couvrent le catalogue MCP, les plugins du catalogue, la recherche web intégrée ou les dépôts de skills des éditeurs sont retirées (#148639).
- L'installation et les releases Intel macOS disparaissent de la CI, pour se concentrer sur Apple Silicon (#148622).
- La boîte d'erreur de mise à jour de Desktop affiche la sortie de l'échec et un lien de signalement (#148355).
- Web Access indique l'étape en cours et le temps écoulé au démarrage (#148408).
- Des alertes de sécurité sont levées sur undici, zod, fast-uri, qs, pypdf, pyasn1, tornado, filelock et setuptools (#148630).

> Sources : [@iamlukethedev, Hermes merged 54 PRs on November 3, 4 novembre 2026](https://x.com/iamlukethedev/status/2117926919052378474) et [Hermes Bible, changelog du 3 novembre 2026](https://www.hermesbible.com/changelog?date=2026-11-03)

## Hermes Agent en tête du classement Octoverse 2026

Le 4 novembre, BkashJosi a relevé que le rapport Octoverse 2026 de GitHub place Hermes Agent premier du classement « most-engaged » parmi les dépôts open source pilotés par un seul éditeur. Il souligne que les étoiles ne comptent qu'un tiers du score.

Le rapport annuel de GitHub confirme le classement. Il sépare cette année les projets communautaires et indépendants des projets portés par un seul éditeur. Dans la colonne « single vendor / product-led », Nous Research arrive en tête avec NousResearch/hermes-agent, devant anomalyco/opencode et earendil-works/pi. Le score « most engaged » mélange les classements du dépôt en étoiles, en forks et en créateurs distincts de pull requests et d'issues.

> Sources : [@BkashJosi, GitHub's Octoverse 2026 ranks Hermes Agent #1 most-engaged among single-vendor open source, 4 novembre 2026](https://x.com/BkashJosi/status/2117980715942097225) et [Octoverse: Commits, pushes, reach new highs in 2026, GitHub Blog, 2026](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)

## Crouton Alpha, un modèle furtif gratuit sur le Nous Portal

Le 3 novembre, OpenRouter a annoncé Crouton Alpha, un nouveau modèle furtif de raisonnement pensé pour démultiplier le travail répétitif des agents : gratuit, 1 million de jetons de contexte, entrées texte, image, audio et vidéo, et aucune utilisation des données pour l'entraînement. witcheer a signalé qu'un nouveau modèle furtif gratuit était à essayer dans le Nous Portal, et yeahfortommy a confirmé que Crouton Alpha y est gratuit, à essayer avec son Hermes Agent.

La fiche OpenRouter détaille le modèle. Crouton Alpha est un modèle léger taillé pour les flux de codage, d'agent et multimodaux, idéal pour les sous-tâches d'agent, l'usage d'outils et l'analyse de documents en volume. Il se combine aux modèles de raisonnement de pointe pour exécuter les étapes bornées qui transforment un plan en action. Le fournisseur, un tiers anonyme pendant cet aperçu, peut conserver les requêtes mais ne s'en sert pas pour l'entraînement. Le modèle accepte outils, appels de fonction et sorties structurées en schéma JSON, rend du texte, et n'est pas disponible via le routage en région européenne.

> Sources : [@OpenRouter, New stealth model: Crouton Alpha, 3 novembre 2026](https://x.com/OpenRouter/status/2117712705901728199), [@yeahfortommy, Crouton Alpha is free in Nous Portal, 3 novembre 2026](https://x.com/yeahfortommy/status/2117724015066300499) et [Crouton Alpha, fiche modèle OpenRouter](https://openrouter.ai/stealth/crouton-alpha)

## Une liste d'attente pour l'application mobile

Le 3 novembre, Nous Research a remercié les personnes venues du monde entier à NousCon 2026 et rappelé que la bêta mobile, lancée pendant l'événement, s'est remplie plus vite que prévu. Teknium a annoncé qu'une liste d'attente est désormais ouverte pour rejoindre l'application au fur et à mesure que des places se libèrent, et witcheer a invité à s'y inscrire dans le post qui suit.

La bêta mobile officielle, couverte par une édition précédente, se connecte à la passerelle Hermes que l'on fait tourner sur sa propre machine. La liste d'attente ouvre la porte aux personnes qui n'ont pas eu de place à l'ouverture.

> Sources : [@NousResearch, Thank you to everyone who traveled from across the world to NousCon 2026, 3 novembre 2026](https://x.com/NousResearch/status/2117696344756252822), [@Teknium, You can now join the waitlist for the Hermes Agent mobile app, 3 novembre 2026](https://x.com/Teknium/status/2117702996478108060) et [@witcheer, join our Hermes Mobile app waitlist, 3 novembre 2026](https://x.com/witcheer/status/2117703516362092816)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
