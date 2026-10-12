# Hermes Agent Quotidien #78

Cette édition revient sur la release v0.21.7 qui regroupe 204 pull requests, sur l'intégration officielle de la skill Anatomy, sur les 42 pull requests fusionnées le 11 octobre, sur un thème open source pour le dashboard web, et sur cinq conseils pour contenir la consommation de jetons.

## v0.21.7, une release de correctifs qui regroupe 204 pull requests

Nous Research a publié la release v0.21.7, datée du 11 octobre 2026. C'est une release de correctifs qui regroupe les quelque 204 pull requests fusionnées depuis v0.21.6 en une version stable pour l'application de bureau (macOS Apple silicon, Windows), le Microsoft Store et MSIX, l'installeur, Docker et Hermes Cloud. Pour les installations depuis les sources (hermes update et la mise à jour de l'application de bureau sur un checkout git), quatre changements :

- Les mises à jour suivent désormais les releases étiquetées : une installation depuis les sources du dépôt officiel se met à jour vers la dernière release vX.Y.Z publiée au lieu de chaque commit de main, une installation déjà plus récente reste sur place sans retour en arrière, et hermes update --set-channel main permet de continuer à suivre chaque commit (les forks et miroirs continuent de suivre main).
- Le canal se choisit dans l'application de bureau : Réglages puis À propos puis Mises à jour propose un commutateur Canal de mise à jour (releases stables ou chaque commit) pour les installations depuis les sources, et la boîte de dialogue de mise à jour affiche le canal actif.
- Le raisonnement survit à la reprise : la réflexion signée est rejouée après hermes chat --resume et au tour suivant de la passerelle, et les modèles de raisonnement Bedrock Converse ne sont plus rejetés sur les sessions reprises.
- Les mises à jour ne bloquent plus derrière certains pare-feu : les installations sur main ne récupèrent plus un enregistrement de release qu'un pare-feu régional pouvait répondre par une 403, la vérification stable utilise le jeton GitHub quand il est défini (GITHUB_TOKEN ou gh auth login), et une limite de débit GitHub est signalée comme telle.

La fenêtre depuis v0.21.6, mesurée au commit 1fd1827, compte 740 commits sans fusion sur 4 156 fichiers modifiés (+86 775 / -26 980), 204 pull requests fusionnées et 69 issues fermées. Les notes complètes et rédigées pour cette fenêtre seront livrées avec v0.22.0.

> Sources : [Hermes Agent v0.21.7, release GitHub NousResearch, 11 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.21.7)

## Anatomy, une skill officielle pour dessiner des machines en SVG

Teknium a annoncé le 11 octobre qu'Anatomy devient une skill optionnelle officiellement intégrée à Hermes Agent. La skill génère des illustrations isométriques détaillées et interactives de machines et de systèmes complexes : des SVG soignés, avec des shaders WebGL et des effets 3D en option. On la trouve parmi les skills optionnelles intégrées du catalogue, ou on l'installe avec hermes skills install official/creative/anatomy.

C'est le portage sous licence MIT du projet wheresryan22/anatomy, signé Ryan. Le dépôt d'origine compte 5 000 étoiles, 370 forks et 87 commits. iamlukethedev situe l'ajout dans la chaîne de production : après la recherche, l'architecture, le code et les tests vient maintenant le prototypage.

> Sources : [@Teknium, Anatomy skill is now an officially integrated optional skill in Hermes Agent, 11 octobre 2026](https://x.com/Teknium/status/2109351160843035106), [@iamlukethedev, Turn ideas into wireframes and interactive prototypes, 11 octobre 2026](https://x.com/iamlukethedev/status/2109367161487823117) et [wheresryan22/anatomy, dépôt GitHub](https://github.com/wheresryan22/anatomy)

## 42 pull requests fusionnées le 11 octobre

iamlukethedev a fait le compte le 12 octobre : Hermes a fusionné 42 pull requests le 11 octobre. Parmi les changements notables :

- Les comptes de connecteurs nommés arrivent sur Desktop, le TUI et le CLI : on choisit et on renomme plusieurs identifiants par application (avec /connectors et hermes connectors en ligne de commande).
- La régénération dans Desktop n'archive plus en silence les tours suivants ; les retours en arrière plus profonds demandent une confirmation explicite.
- Les plugins peuvent lancer des actions intégrées de l'application Desktop via ctx.runAction.
- browser_exec fait passer les pages localhost et du réseau local par le sidecar du navigateur cloud, et continue de fonctionner quand le fournisseur cloud échoue.
- La règle 17 du catalogue de plugins bloque les charges exécutables non analysables, avec une CI qui analyse les entrées épinglées.
- Le scanner d'installation lève une quinzaine de classes de faux positifs, faisant passer 38 épingles de « prudence » à « sûr ».
- Les complétions des agents délégués ne prennent plus le contrôle de la conversation parente.
- Le filtre de sécurité d'Alibaba clôt le tour avec un message clair au lieu d'une boucle de relance de quatre minutes.
- Les relecteurs voient chaque changement de prompt système et de schéma d'outil avant la fusion.

Au total, 42 nouvelles fonctionnalités et corrections.

> Sources : [@iamlukethedev, Hermes merged 42 PRs on October 11, 12 octobre 2026](https://x.com/iamlukethedev/status/2109508885086101771)

## Un thème open source pour le dashboard web

witcheer a signalé le 12 octobre qu'un utilisateur de r/hermesagent a ouvert le code d'un thème clair et sombre, arrondi, pour le dashboard web de Hermes Agent. Ce que ça change : une seule police (Inter) sur toute l'interface, avec les titres en police pixel remplacés ; des cartes, boutons, champs et cases arrondis, avec le grain de film désactivé ; la couleur réservée aux boutons, badges et marques d'état. Chaque thème est un fichier YAML : on le dépose dans ~/.hermes/dashboard-themes/ et il apparaît dans le sélecteur de thème à côté des thèmes intégrés.

Le dépôt Faultbendfold/hermesagent-dashboard-theming (licence MIT) contient deux thèmes, light-clean et dark-clean, une skill qui documente la construction de tels thèmes, un outil d'exploration de palette autonome (color-board.html) et un script qui compose des captures côte à côte. Le README rappelle une distinction utile : les thèmes du dashboard ne sont pas des skins du CLI. Le terminal se thème par display.skin et les fichiers de $HERMES_HOME/skins/, tandis que le dashboard se thème par dashboard.theme et les fichiers de $HERMES_HOME/dashboard-themes/. Un thème est un ajout à chaud, sans reconstruction ni fork, et il survit aux mises à jour de l'application.

> Sources : [@witcheer, someone on r/hermesagent open-sourced a light & dark, rounded theme, 12 octobre 2026](https://x.com/witcheer/status/2109637714492457293) et [Faultbendfold/hermesagent-dashboard-theming, dépôt GitHub](https://github.com/Faultbendfold/hermesagent-dashboard-theming)

## Cinq conseils pour contenir la consommation de jetons

witcheer a publié le 12 octobre cinq conseils pour maîtriser la dépense en jetons de son agent :

- Où vont les jetons ? /usage affiche la consommation de la session, le coût estimé et l'état de la fenêtre de contexte ; /insights couvre les usages sur les trente derniers jours ; hermes prompt-size donne le coût fixe de chaque message avant le début de la conversation.
- Ce qui part à chaque appel : le prompt système et les schémas d'outils de tous les outils activés. L'index des skills et les schémas d'outils grandissent avec le nombre de skills et d'outils : hermes tools coupe les toolsets inutilisés, hermes skills désinstalle ou désactive les skills superflues.
- Les longues sessions : Hermes compresse automatiquement les conversations longues, et /compress résume l'historique à la demande. Pour un plafond fixe par appel, hermes config set compression.threshold_tokens déclenche la compression au plus bas du seuil de ratio et du plafond.
- Les changements de modèle et les replis : la plupart des fournisseurs mettent en cache le début de la conversation, et les touches de cache coûtent nettement moins cher. Le cache est indexé par modèle et par compte, donc un changement de /model, un repli automatique ou une rotation du pool de credentials force la relecture complète au prix plein. hermes fallback affiche la chaîne de secours.
- Les sous-agents : chacun démarre avec une conversation neuve, et seule sa synthèse revient dans le chat. Un lot parallèle de sous-agents consomme en général la majorité des jetons d'une exécution ; on épingle les sous-agents sur un modèle peu coûteux avec hermes config set delegation.model.

> Sources : [@witcheer, keeping your Hermes Agent's token spend down, 12 octobre 2026](https://x.com/witcheer/status/2109615063321477480) et [Performance & cost, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/tips#performance--cost)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
