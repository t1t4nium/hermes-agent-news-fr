# Hermes Agent Quotidien #50

Cette édition revient sur un numéro des Wingtips consacré au déplacement du dossier
où l'agent écrit ses nouvelles skills, sur la méthode de test d'un prompt sur une
copie de son agent, sur le réglage des modèles auxiliaires décrit par Teknium, sur
le nouveau sélecteur d'effort de raisonnement du composeur du bureau, sur l'arrivée
de GPT Image 2.5 sur le portail Nous, sur le premier meetup de la communauté à
Bangkok, sur un prompt qui fait écrire par l'agent sa note hebdomadaire et sur ce
que les utilisateurs réclament le plus. Aucune release n'a été publiée depuis la
v0.21.2 du 11 septembre.

## Wingtips #72 : déplacer le dossier des skills créées par l'agent

witcheer décrit dans le soixante-douzième numéro des Wingtips ce que devient une
skill que l'agent s'écrit après une bonne session : elle atterrit dans le dossier
de skills du profil, sur cette machine et pour ce profil. La clé `create_dir`, sous
la section `skills` de `config.yaml`, déplace ce point de dépôt, pour viser par
exemple un dossier cerveau partagé, un dépôt suivi par git ou un volume de skills
commun à un parc de machines.

La documentation des skills détaille ce que le réglage change. Les nouvelles skills
créées par `skill_manage`, sous-catégories comprises, partent sous `create_dir` au
lieu du dossier local, et le répertoire est créé à la première écriture s'il
n'existe pas. Les instructions données à l'agent suivent la configuration : la
description de l'outil et les textes de prompt qui nomment le chemin de création
sont rendus dynamiquement, sans surcharge de prompt système ni détour par le
système de fichiers. Le dossier est pleinement intégré, ses skills étant scannées
avec celles du dossier local, présentes dans l'index, `skills_list`, `skill_view`
et les commandes slash, et modifiables ou supprimables comme les autres. Le reste
ne bouge pas : les skills existantes restent modifiées là où elles se trouvent, et
la synchronisation des skills livrées, le hub et le curateur continuent de
travailler sur le dossier local du profil. Les chemins acceptent l'expansion de
`~` et la substitution de variables, les chemins relatifs se résolvant contre le
répertoire Hermes. Laisser `create_dir` sur le dossier local revient à ne rien
régler.

> Sources : [@witcheer, Hermes Wingtips #72 : skills.create_dir, 14 septembre 2026](https://x.com/witcheer/status/2099370347153805667) et [Skills System, Redirecting Skill Creation, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#redirecting-skill-creation-skillscreate_dir)

## Tester un prompt sur une copie de son agent

witcheer explique le 13 septembre que chaque prompt de sa série Hermes Autopilot et
chaque commande qu'il publie dans un Wingtip passe d'abord sur une copie de son
agent, pas sur celui qu'il utilise toute la journée. La copie tient en une commande,
`hermes profile create test --clone`.

La référence des commandes précise ce que `--clone` emporte depuis le profil actif :
la configuration, le fichier `.env`, le `SOUL.md`, les skills et les fichiers de
mémoire curés `MEMORY.md` et `USER.md`. `--clone-all` copie tout l'état du profil,
et `--clone-from <source>` désigne un profil source, ce qui implique le clonage de
la configuration sauf s'il est associé à `--clone-all`.

> Sources : [@witcheer, every prompt I post in the Hermes Autopilot series, and every command I put in a Wingtip, gets run first on a copy of my agent, 13 septembre 2026](https://x.com/witcheer/status/2099161380284674255) et [CLI Commands Reference, hermes profile, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes-profile)

## Le réglage des modèles auxiliaires expliqué par Teknium

Teknium a répondu le 13 septembre à une question revenue souvent en montrant comment
il règle ses modèles auxiliaires dans Hermes Agent : Gemini Flash fait économiser
beaucoup, et le modèle astra lui donne un second point de vue quand il lance
`/review`.

La documentation des modèles auxiliaires rappelle l'enjeu : rien n'est à configurer
pour démarrer, mais sur un modèle de raisonnement coûteux les tâches auxiliaires
ajoutent une dépense notable, d'où l'intérêt de router chaque tâche vers un modèle
rapide et bon marché. La liste des tâches concernées comprend la vision, la
génération de titres, les étiquettes audio, la compression, le classificateur
d'approbation, le spécificateur de triage, le décomposeur kanban, le descripteur de
profil et la délégation, chaque entrée acceptant un fournisseur, un modèle et, au
besoin, un point de terminaison compatible OpenAI.

La référence des commandes complète le lien avec `/review` : la commande lance un
sous-agent relecteur indépendant, doté des mêmes privilèges, qui examine le travail
discuté dans les dix derniers messages, et son modèle dédié se fixe par
`auxiliary.review` dans `config.yaml`, le modèle principal servant par défaut.

> Sources : [@Teknium, here's how I setup my auxiliary models in Hermes Agent, 13 septembre 2026](https://x.com/Teknium/status/2099168594731106767), [Auxiliary Models, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#auxiliary-models) et [Slash Commands Reference, /review, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## Un sélecteur d'effort de raisonnement dans le composeur du bureau

Teknium a annoncé le 13 septembre que l'effort de raisonnement est devenu un
sélecteur distinct dans le composeur de l'application de bureau.

La documentation du bureau décrit le dispositif. Le sélecteur de modèle vit dans le
composeur, juste à gauche du microphone, et chaque ligne de modèle propose ses
options de réflexion, d'effort et de mode rapide. Une pastille de raisonnement
affiche le niveau actif, `Med` ou `High`, et ouvre les mêmes options sans avoir à
retrouver la ligne du modèle ; elle disparaît pour les modèles dont le catalogue ne
signale aucun réglage de raisonnement. Chaque modèle retient son effort et son choix
de mode rapide propres à l'application, réappliqués à la session quand on le
sélectionne, ces préférences ne touchant ni les tâches planifiées ni les sous-agents.

Un problème déclaré le 11 septembre montre un effet de bord du même mécanisme : le
composeur amorce son effort depuis la valeur globale `agent.reasoning_effort` et la
transmet à chaque création de session, ce qui masque les surcharges par modèle de
`agent.reasoning_overrides` pour toute la session. Le cas cité combine
`agent.reasoning_effort: high` et une surcharge `gpt-5.6-sol: none` : la requête
partait malgré tout avec `high`, et un point de terminaison qui refuse les outils
accompagnés d'un effort non nul renvoyait alors une erreur 400. La proposition est
d'écarter la valeur transmise quand elle est identique au défaut global, ce qui
laisse intactes les surcharges par modèle, et une demande de tirage est rattachée au
rapport.

> Sources : [@Teknium, Reasoning effort is now a seperate selector in the Hermes Agent desktop app's composer, 13 septembre 2026](https://x.com/Teknium/status/2099201403906625754), [Hermes Desktop, Choosing a model, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#choosing-a-model) et [Issue #107949, Desktop composer's echoed reasoning effort shadows agent.reasoning_overrides, DavidMetcalfe, 11 septembre 2026](https://github.com/NousResearch/hermes-agent/issues/107949)

## GPT Image 2.5 arrive sur le portail Nous

Teknium a annoncé le 14 septembre que ChatGPT-Image-2.5 est disponible sur le portail
Nous pour un usage dans Hermes Agent, aux côtés des routes directes FAL et ChatGPT
déjà prises en charge.

La documentation de la génération d'images détaille cette génération de modèles. Sous
le fournisseur OpenAI, GPT Image 2.5 Flare vise la création quotidienne rapide et
Sunburst la génération et l'édition de précision, avec `OPENAI_API_KEY` ; la qualité
est automatique par défaut et se fixe en suffixant le nom par `-low`, `-medium`,
`-high`, `-xhigh` ou `-max`, et les deux acceptent jusqu'à seize images de référence.
L'équivalent FAL se sélectionne par `openai/gpt-image-2.5/flare/text-to-image`, ou le
modèle Sunburst correspondant. La page rappelle la limite du chemin géré : la
disponibilité à travers la passerelle dépend de la liste des points de terminaison
autorisés par celle-ci et n'est pas déduite de la disponibilité chez FAL, un refus
HTTP 4xx sur un modèle donné signalant que le portail ne le relaie pas encore.

> Sources : [@Teknium, ChatGPT-Image-2.5 is now available on Nous Portal, 14 septembre 2026](https://x.com/Teknium/status/2099327677648015365) et [Image Generation, OpenAI API: GPT Image 2.5, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation#openai-api-gpt-image-25)

## Premier meetup Hermes Agent à Bangkok le 25 septembre

Jon Komet, auteur de l'extension navigateur Hermes, organise le premier meetup de la
communauté Hermes Agent à Bangkok le vendredi 25 septembre, à partir de 18 heures
locales chez Cleverse. Nous Research parraine l'événement, et witcheer a relevé le
13 septembre qu'il s'agit de la deuxième manifestation communautaire soutenue par
l'éditeur.

La page d'inscription donne le cadre : entrée gratuite sur réservation, jusqu'à cent
participants, porte ouverte à 18 heures et discours d'ouverture à 18 h 45, nourriture
et boissons fraîches fournies, au treizième étage du bâtiment Rungrojthanakul. Le
programme annoncé comprend des démonstrations de l'application de bureau, de la TUI,
de l'extension navigateur et du mode bot, une station NVIDIA DGX Spark tenue par le
co-hôte @sudoingX pour des flux d'agent entièrement locaux, une présentation de
l'architecture de Honcho, partenaire mémoire officiel, avec dix dollars de crédits
remis aux participants, puis une tombola de goodies Nous Research et de coupons de
calcul.

> Sources : [@jonkomet, the first official hermes agent meetup in bangkok is locked in, 13 septembre 2026](https://x.com/jonkomet/status/2099197030677770612), [@witcheer, Nous Research supports community events and Bangkok is the second one!, 13 septembre 2026](https://x.com/witcheer/status/2099214912719585416) et [Hermes Agent Meetup, Bangkok, page d'inscription Luma](https://luma.com/tua74l05)

## Une note hebdomadaire écrite par l'agent

witcheer a publié le 14 septembre un prompt à coller dans une conversation neuve pour
obtenir, le lundi matin, un compte rendu de ce que l'utilisateur et son agent ont
fait la semaine passée, rédigé par l'agent. Le prompt lui fait parcourir les sessions
des sept derniers jours, écrire une revue de dix lignes et montrer la tâche planifiée
correspondante, avec le jour et l'heure. Le texte du prompt se trouve dans l'image
jointe à la publication.

> Source : [@witcheer, want a Monday morning note on what you and your Hermes Agent did last week, written by the agent itself?, 14 septembre 2026](https://x.com/witcheer/status/2099485722545648017)

## Ce que les utilisateurs réclament le plus

witcheer a dépouillé le 14 septembre plus de 150 réponses à une question sur ce qui
manque, et en a tiré les demandes les plus fréquentes. En tête arrive une application
mobile, sur iOS et Android. Les jetons viennent ensuite, avec l'observation qu'un
agent qui lit des fichiers, exécute des outils et entretient sa mémoire fait plus de
travail par tour qu'une fenêtre de conversation. Le reste du dépouillement est dans
l'image jointe à la publication.

> Source : [@witcheer, I read the 150+ replies under this question, here is what you said, 14 septembre 2026](https://x.com/witcheer/status/2099448053295915352)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
