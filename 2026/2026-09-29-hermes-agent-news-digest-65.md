# Hermes Agent Quotidien #65

Cette édition revient sur les 138 pull requests fusionnées le 28 septembre, sur le nouvel onglet Skills de Hermes Desktop en vue cartes, sur l'arrivée de Claude Sonnet 5.5 dans Hermes Agent, sur les dix prompts Hermes Autopilot de witcheer, et sur une plateforme de pronostics hippiques bâtie avec Hermes et Opus 5.5.

## 138 pull requests fusionnées le 28 septembre

iamlukethedev a fait le compte le 29 septembre : Hermes a fusionné 138 pull requests le 28 septembre, réparties entre l'interface (47), la voix et le temps réel (1), les outils et plugins pour développeurs (51), la sécurité et les secrets (7), les intégrations et la discussion (8) et la stabilité (24). Parmi les plus notables :

- Bot Screen, computer_use et le navigateur tournent désormais dans la sandbox du backend terminal.
- Desktop publie l'image de sandbox nousresearch/hermes-sandbox:desktop, avec une pile d'affichage pour ce backend.
- L'i18n devient complète : des packs de langue enfichables et superposables sur Core, TUI et Desktop, avec parité sur 16 locales.
- Desktop et TUI agissent sur le profil propriétaire de la session, et non plus sur le profil de lancement du backend.
- Les réglages de Desktop lisent et écrivent enfin le profil qu'ils affichent : approbation, backend, coffre et jetons.
- Sous multiplex, le cron suit le profil propriétaire de la tâche pour la livraison, les routes et les secrets.
- Claude Sonnet 5.5 rejoint les catalogues OpenRouter et Nous Portal.
- La télémétrie partagée opt-in montre les échecs, les taux de conservation et d'abandon, et le coût de la configuration et des modèles, avec le consentement de Desktop.
- La compaction suit de nouveau le seuil compression.threshold au lieu d'un plafond codé en dur de 256 000 jetons.
- Le catalogue de plugins accueille Nachos, unbrowse, antigravity OAuth, PIR8 brain graph, un émulateur Android et d'autres.
- Le statut OAuth Qwen affiche l'expiration du jeton, son aperçu et le chemin des identifiants.
- Les tâches cron à redémarrage sûr ne meurent plus sur un ruamel manquant sous multiplex.

> Sources : [@iamlukethedev, Hermes merged 138 PRs on September 28, 29 septembre 2026](https://x.com/iamlukethedev/status/2104754369455616484)

## Le nouvel onglet Skills de Hermes Desktop

witcheer a publié le 29 septembre une visite guidée de moins de trois minutes du nouvel onglet Skills de Hermes Desktop. La section Skills change d'apparence : une vue en cartes rejoint la vue en liste existante pour parcourir ses compétences et le catalogue complet. tonbistudio précise qu'on peut activer ou désactiver chaque compétence par profil, et chercher de nouvelles compétences à installer depuis le catalogue.

> Sources : [@witcheer, a quick tour of the new Skills tab in Hermes Desktop, 29 septembre 2026](https://x.com/witcheer/status/2104821633986765166) et [@tonbistudio, The Skills section of the Hermes Desktop app has a new look, 29 septembre 2026](https://x.com/tonbistudio/status/2104820279197540709)

## Claude Sonnet 5.5 disponible dans Hermes Agent

yeahfortommy a annoncé le 28 septembre que Claude Sonnet 5.5 est en ligne dans Hermes Agent. witcheer a invité le lendemain à donner un retour précoce sur le modèle dans Hermes Agent. L'arrivée figure aussi dans la liste des 138 pull requests fusionnées, qui ajoute anthropic/claude-sonnet-5.5 aux catalogues OpenRouter et Nous Portal.

> Sources : [@yeahfortommy, Claude Sonnet 5.5 is live in Hermes Agent, 28 septembre 2026](https://x.com/yeahfortommy/status/2104700597530214739) et [@witcheer, give us your early feedback on Sonnet 5.5 in Hermes Agent, 29 septembre 2026](https://x.com/witcheer/status/2104805758428733793)

## Les dix prompts Hermes Autopilot de witcheer

witcheer a regroupé le 29 septembre ses dix premiers prompts Hermes Autopilot sur une seule page, à coller chacun dans une nouvelle discussion Hermes Agent. La série couvre par exemple faire connaître sa façon de travailler à son agent, transformer ce qu'on vient de faire en compétence, auditer sa propre configuration, une revue du lundi qui s'écrit toute seule, ou encore l'AGENTS.md de son dépôt.

La page précise que chaque prompt s'appuie sur la mémoire, les compétences, l'historique de session et le terminal. Chacun est sûr par défaut : il montre le résultat et ne modifie rien tant qu'on n'a pas confirmé, et tous ont été exécutés sur un vrai poste Hermes Agent avant publication. Les prompts sont numérotés du plus ancien au plus récent, du premier entretien mémoire au dixième, qui tire une liste de tâches de documentation de ses pull requests ouvertes.

> Sources : [@witcheer, 10 Hermes Agent prompts so far, all on one page, 29 septembre 2026](https://x.com/witcheer/status/2104849784456565146) et [Hermes Autopilot prompts, notwitcheer, hermes-recipes](https://notwitcheer.github.io/hermes-recipes/prompts/)

## Une plateforme de pronostics hippiques bâtie avec Hermes et Opus 5.5

iamlukethedev a raconté le 29 septembre qu'un client lui a demandé une plateforme de pronostics hippiques avec analyse IA pour l'aider à décider ses paris. Hermes, associé à Opus 5.5, a construit la plateforme et intégré FormFav, qui fournit la forme, les statistiques et les données des courses par API. S'y ajoute une simulation de course en 3D. L'auteur précise qu'il livre du logiciel, pas des gains garantis.

> Source : [@iamlukethedev, Hermes + Opus 5.5 did it again, 29 septembre 2026](https://x.com/iamlukethedev/status/2104885630392234474)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
