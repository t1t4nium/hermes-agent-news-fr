# Hermes Agent Quotidien #74

Cette édition revient sur la release v0.21.6 et ses corrections de sécurité, sur la levée de fonds de 90 millions de dollars de Nous Research, sur l'arrivée de Hermes sur les PC ASUS ProArt RTX Spark, sur le numéro 95 des Wingtips consacré à la commande /loop, et sur les 107 pull requests fusionnées le 7 octobre.

## Release v0.21.6 : correctifs et durcissements de sécurité

Nous Research a publié le 8 octobre la release v0.21.6 de Hermes Agent. C'est une release de correctifs, la première produite par la nouvelle chaîne de release stable : une référence de tentative unique, une image Docker testée et un tag de réception à la publication. Elle embarque le tag, la release GitHub et l'image Docker ; l'application Desktop, les paquets Termux et le Microsoft Store restent sur leur build actuel et suivront à la prochaine release groupée.

La fenêtre mesurée au commit 818c13be1dc4fd28987e1e881a9408224afd4535 contient, depuis la v0.21.5, 8 867 commits hors merge sur 8 342 fichiers modifiés (plus 772 490, moins 225 600), 2 106 pull requests fusionnées et 3 027 issues fermées. Le tag roule ces quelque 2 100 PR dans une release stable pour Docker et Hermes Cloud. Les notes complètes et organisées de cette fenêtre arriveront avec la v0.22.0, qui documentera tout depuis la v0.21.0.

La release liste, sans les documenter ici, plusieurs changements de la fenêtre :

- la transcription en direct pendant que l'on parle, sur le CLI, le TUI et Desktop (stt.streaming) ;
- les tours vocaux parlés routés vers leur propre modèle (auxiliary.voice_chat), avec le raisonnement désactivé par défaut ;
- les plugins tiers exécutés dans un hôte de plugin par profil (plugins.isolation: host), et un espace unique Réglages > Plugins pour leurs pages de réglages ;
- les modèles favoris et épinglés en tête du sélecteur de Desktop, une pastille d'usage avant qu'un abonnement atteigne son plafond, et les fournisseurs limités en débit qui indiquent pourquoi et jusqu'à quand ;
- les modèles locaux dans hermes model, plus llama.cpp CUDA sur Linux x64 et arm64 ;
- des packs de langue empilables et par couches, sur le cœur, Desktop et le TUI ;
- un hermes status orienté résumé (--short, --full) ;
- un sélecteur de portée de diff dans le panneau de revue (Uncommitted, Branch, Last turn) et un maintien d'éveil qui suit le tour ;
- des avertissements cron, doctor et sur le canal maison quand le stockage cron devient inscriptible impossible ;
- des drapeaux d'approbation pour les dépôts d'identifiants et les caractères Unicode invisibles dans les commandes de terminal ;
- un paramétrage Discord qui vérifie le jeton du bot et affiche le lien d'invitation ;
- une définition de workflow Kanban unifiée ;
- activate.fish ;
- GPT-6.1 Sol, Claude Sonnet 5.5 et Haiku 5.5 au catalogue ;
- des dizaines de nouveaux plugins communautaires.

La release corrige aussi plusieurs problèmes de sécurité. Sur le durcissement de l'authentification du dashboard : des en-têtes X-Forwarded-For falsifiés pouvaient réinitialiser la limite de débit de la connexion par mot de passe ; des requêtes de connexion non authentifiées pouvaient écrire des valeurs non bornées dans le journal d'audit ; les routes publiques /auth/ n'avaient pas de limite de taille de corps de requête ; et la connexion native pouvait envoyer les codes de connexion vers une redirection non loopback, ce qui permettait une prise de session. Les quatre problèmes ont été signalés par Tenable Research (TRA-725 à TRA-728). Sur le durcissement des filtres git du dépôt : les appels git automatiques (instantané d'espace de travail, worktrees de sous-agents, kanban, nettoyage de worktree, hermes -w) pouvaient exécuter les programmes de filtre clean/smudge/process définis par la config d'un dépôt non fiable avant le premier prompt. Sur le durcissement de l'expéditeur de la passerelle email : un nom d'affichage entre guillemets dans l'en-tête From pouvait faire passer le message d'un attaquant comme expéditeur autorisé de la liste blanche.

> Sources : [Hermes Agent v0.21.6, release GitHub, 8 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.21.6) et [Release notes from hermes-agent, flux Atom](https://github.com/NousResearch/hermes-agent/releases.atom)

## Une série B de 90 millions de dollars à 1,5 milliard de valorisation

Nous Research a confirmé le 7 octobre une levée de fonds de série B de 90 millions de dollars, pour une valorisation de 1,5 milliard de dollars, d'abord rapportée par le Wall Street Journal. Le tour est mené par Robot Ventures, avec la participation de Nvidia, M12 (Microsoft), Samsung Next, Union Square Ventures, Y Combinator et Menlo Ventures, entre autres. La levée porte le financement total de la société, fondée en 2023, à 158 millions de dollars.

Hermes Agent a été cloné plus de 24 millions de fois et, selon les estimations internes de la société, génère environ 2,5 % de l'usage mondial de jetons. Le capital financera l'entrée de Nous Research sur le marché de l'entreprise avec « Hermes for Businesses », qui permettra aux sociétés de déployer des agents personnalisés gérant des workflows en plusieurs étapes tout en gardant leurs données privées, ainsi que le développement d'une application mobile. Le Wall Street Journal rapporte un revenu annualisé d'environ 36 millions de dollars à la mi-septembre, avec l'objectif de dépasser 100 millions avant la fin de 2026.

Sur le billet publié par la société, Dillon Rolnick, directeur général, replace la levée dans la mission de Nous : construire une alternative ouverte et vérifiable à la centralisation de l'IA. Il rappelle que Hermes Agent a été publié sous licence MIT en février dernier et décrit la philosophie d'« user-alignment », un modèle qui adhère à la vision du monde de son utilisateur plutôt qu'à celle imposée par une entité.

> Sources : [@NousResearch, As reported in the @WSJ, we have raised a Series B, 7 octobre 2026](https://x.com/NousResearch/status/2107874963382538469), [TechCrunch, Nous Research confirms it hit $1.5B valuation, 7 octobre 2026](https://techcrunch.com/2026/10/07/nous-research-confirms-it-hit-1-5b-valuation-launches-ai-agents-for-business-users/) et [Nous Research, A Note on Our Fundraise, 7 octobre 2026](https://nousresearch.com/a-note-on-our-fundraise)

## Hermes sur les PC ASUS ProArt RTX Spark

ASUS a annoncé le 8 octobre ses PC Windows ProArt RTX Spark, avec Hermes Agent en couche agent. Les ordinateurs portables ProArt P16 et P14 et le mini PC ProArt GR1X embarquent NVIDIA RTX Spark, qui réunit un GPU Blackwell RTX, un CPU Grace et jusqu'à 128 Go de mémoire unifiée, pour jusqu'à 1 pétaflop de calcul IA en FP4. La gamme est pensée pour l'IA locale : faire tourner de grands modèles sans dépendre du cloud, et itérer sans frais par jeton.

Hermes Agent, présenté comme l'expert créatif personnalisé, pilote ComfyUI et MuseTree sur la machine, travaille sur les fichiers locaux et garde les workflows sur l'appareil. La skill Hermes dédiée se connecte à MuseTree, qui intègre FLUX et WAN pour une génération locale d'image et de vidéo sans jeton. Dillon Rolnick résume la position de Nous : Hermes fournit une intelligence que l'on possède vraiment, plutôt que de la louer. Les précommandes ont ouvert le 7 octobre pour une disponibilité au 16 octobre ; les portables démarrent à 2 599,99 dollars aux États-Unis, et le GR1X arrivera plus tard dans l'année.

> Sources : [ASUS Pressroom, ASUS ProArt RTX Spark Windows PCs Available for Immediate Pre-Order, 8 octobre 2026](https://press.asus.com/news/press-releases/asus-proart-rtx-spark-p16-p14-ai-pcs/), [@ASUS, Powered by NVIDIA & Hermes AI, the new RTX Spark PC ProArt P16 & P14, 8 octobre 2026](https://x.com/ASUS/status/2108109095689650334) et [@Teknium, Enjoy Hermes Agent on your new @ASUS RTX Spark, 8 octobre 2026](https://x.com/Teknium/status/2108111237427187873)

## Wingtips #95 : la commande /loop pour rejouer un prompt à intervalle

witcheer a consacré le numéro 95 des Wingtips à la commande /loop, qui fait rejouer un prompt à intervalle régulier dans la session en cours. Chaque réveil est un vrai tour d'agent : Hermes relit l'état à neuf, fait le travail, rend compte et se tait jusqu'au prochain tick. L'exemple donné : « /loop 5m check build.log and tell me when the build is done ».

La documentation des boucles récurrentes détaille la mécanique. Deux cadences coexistent : un intervalle fixe (/loop 5m) ou une cadence auto-rythmée, qui démarre à une minute et recule jusqu'à un plafond tant que les réponses ne changent pas. La boucle s'arrête quand l'agent se déclare terminé (LOOP_COMPLETE), quand un plafond de tours est atteint (--times N), quand une condition est vérifiée par le juge auxiliaire (--until), quand on l'arrête (/loop stop) ou quand le budget de sécurité (loops.max_ticks, 100 par défaut) est épuisé. Les sous-commandes /loop status, /loop pause, /loop resume et /loop stop la pilotent, et /proactive en est un alias. La commande fonctionne sur le CLI, le TUI, le dashboard web, Desktop et toutes les plateformes de messagerie. Quand le travail doit tourner sans surveillance, la documentation renvoie vers les tâches cron, qui vivent hors de toute session.

> Sources : [@witcheer, Hermes Wingtips #95: let your agent keep checking for you, 8 octobre 2026](https://x.com/witcheer/status/2108082465923649911) et [Recurring Loops, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)

## 107 pull requests fusionnées le 7 octobre

iamlukethedev a fait le compte le 8 octobre : Hermes a fusionné 107 pull requests le 7 octobre. Deux changements figurent dans le texte du message :

- Les tours vocaux peuvent désormais tourner sur leur propre modèle plus rapide via auxiliary.voice_chat, si bien que les réponses parlées n'attendent plus le modèle principal.
- Un disque plein ou en lecture seule n'arrête plus le planificateur cron ; les tâches se rattrapent une fois le stockage redevenu inscriptible.

> Source : [@iamlukethedev, Hermes merged 107 PRs on October 7, 8 octobre 2026](https://x.com/iamlukethedev/status/2108021404868452720)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
