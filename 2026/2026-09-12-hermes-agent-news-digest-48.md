# Hermes Agent Quotidien #48

Cette édition revient sur la release de correctifs v0.21.2, consacrée à la
fiabilité du magasin de sessions, sur les dossiers de skills externes du
soixante-dixième numéro des Wingtips, sur les commandes qui prennent la parole
pendant qu'un tour tourne, sur un essaim d'agents lancé sur le défi Hutter Prize
et sur deux usages communautaires : des tables d'adéquation mémoire pour
trente-huit modèles, et un connectome de mouche branché sur Hermes.

## Hermes Agent v0.21.2, la release de correctifs du magasin de sessions

Le 11 septembre, teknium1 a publié Hermes Agent v0.21.2 (tag v2026.9.11), que les
notes appellent « The state.db Patch Release ». La v0.21.0 avait livré une
réécriture large de la gestion des connexions du magasin de sessions, et sur
certaines installations cette réécriture a rendu `state.db` fragile : deux
écrivains qui annulent mutuellement leurs verrous, des bases saines signalées
comme corrompues, une seule ligne fautive qui fait tomber `sessions list`. Cette
release ferme cette classe de défauts et regroupe tout ce qui est arrivé sur
main depuis v0.21.1.

Mesurée au commit de référence, la fenêtre depuis v0.21.1 compte 947 commits hors
fusion sur 1 869 fichiers modifiés (+182 504 / -15 564 lignes) et 312 demandes de
tirage fusionnées, avec 140 contributeurs crédités.

Les changements notables :
- La campagne de fiabilité de `state.db` s'attaque aux causes racines et non aux
  symptômes : six demandes de tirage et 44 issues fermées pour cette seule
  campagne.
- Plus d'écrivain secondaire : l'état des salles hébergées quitte la base
  racine pour `shared-state.db`, le tableau de bord ouvre d'abord en lecture
  seule, le garde de cycle de vie du cron passe par le registre de connexions
  suivi au lieu d'un `open()` brut sur une base vivante, et `hermes doctor --fix`
  refuse un point de contrôle dont il ne peut pas prouver qu'il est sûr.
- Les bases WAL saines cessent de se coincer : les entrées `(deleted)`
  d'OpenZFS, une fermeture qui entre en course avec une écriture de message, un
  mode journal non confirmé au moment de distribuer le pool de lecture, une
  erreur d'entrées-sorties transitoire sous WSL2 et une bannière « state.db
  locked » diffusée après la levée du verrou sont tous traités.
- Une atteinte de l'index de recherche plein texte ne fait plus tomber le tour :
  l'erreur est classée `fts_index`, la recherche se dégrade et l'index se
  reconstruit plus tard sans toucher au magasin de transcriptions.
- `hermes doctor` nomme l'atteinte structurelle au lieu de « FTS write
  corruption », la sonde d'écriture FTS attrape l'index périmé qui passait tous
  les contrôles alors que chaque écriture échouait, et le poller analytique du
  tableau de bord renvoie un 503 au lieu d'environ 520 000 traces par jour.
- Une ligne corrompue ne tue plus `sessions list`, l'export ni les insights :
  un assistant `coerce_epoch()` lit les horodatages invalides sur tous les
  lecteurs, une garde `json_valid` protège `json_extract`, les listes
  d'identifiants sont découpées et l'hydratation de l'export se fait par lots.
- Les sessions ne se lient plus ni ne lisent la base d'un autre profil : le
  backend de lancement du bureau ne peut plus s'épingler au mauvais profil sous
  une course sur `HERMES_HOME`, la recherche de session par identifiant seul ne
  scanne plus tous les profils, et la suppression d'un profil ne garde plus de
  descripteur ouvert.
- Ouvrir `state.db` ne prend plus le verrou d'écriture quand rien n'a besoin
  d'être écrit : un processus `hermes` ponctuel derrière une passerelle occupée
  passe de 4 à 20 secondes de blocage suivi d'un échec « database is locked » à
  0,01 seconde.
- L'isolation multi-profils est renforcée : les bots d'un profil secondaire
  n'héritent plus des listes d'autorisation du profil par défaut, les
  adaptateurs n'envoient plus d'identifiants vers l'hôte du profil par défaut,
  les serveurs MCP stdio ne reçoivent plus les secrets du coffre du profil par
  défaut, et la livraison de médias ne peut plus joindre le `.env`, l'`auth.json`
  ou le `state.db` d'un autre profil.
- Les orages de lancement du backend du bureau sont terminés : Bot Mode ne lance
  ou ne compose plus un backend par profil au démarrage et à chaque tic de la
  liste des bots, le survol de cette liste ne lance plus un backend par ligne,
  et un changement de profil ne peut plus créer un primaire en double.
- Le coffre d'identifiants rend l'agent aveugle aux secrets : il peut se
  connecter, payer et remplir des adresses depuis 1Password, Bitwarden ou le
  coffre Hermes local sans jamais voir un mot de passe ; les codes à deux
  facteurs viennent d'une clé d'authentificateur enregistrée ou sont demandés
  dans l'interface de l'utilisateur, et les greffons git privés s'installent
  avec les identifiants stockés.
- Un catalogue de greffons fait son entrée, index curé et épinglé par empreinte
  SHA avec interface en ligne de commande, CI d'admission, documentation et
  tableau de bord, pendant que le bureau gagne une page Plugins unique qui
  possède les greffons d'agent et de bureau, l'installation, le catalogue et
  l'épinglage par commit.
- L'offre gratuite de Nous et un premier lancement guidé arrivent : inférence et
  connecteurs gratuits prêts à l'emploi avec une commande pour se connecter,
  `/login` depuis une conversation, des outils de connecteurs, dont Gmail,
  Linear et Notion, cherchables via `tool_search`, et un premier lancement guidé
  derrière `HERMES_GUEST_ONBOARDING=1`.

Correctifs notables :
- Passerelles et plateformes : une clé `display:` seule dans `config.yaml` ne
  fait plus planter chaque tour, un final refusé par la plateforme est enregistré
  et relivré, un envoi WebSocket bloqué ne bloque plus les événements suivants,
  les bots Telegram doivent être mentionnés quand `bots_require_mention` est
  actif, Matrix rend le LaTeX, Signal rend les tableaux markdown, et les
  réponses aux messages éphémères de WhatsApp gardent leur citation.
- Fournisseurs et routage : `/model` et le mode automatique des appels
  auxiliaires ne facturent plus un fournisseur non choisi et ne basculent plus
  vers un fournisseur sans identifiants, les modèles Bedrock Claude, Converse et
  Mantle survivent à `/model`, au repli et à la restauration, les garde-fous
  Bedrock sont appliqués, et DeepSeek V4.1 Flash rejoint les sélecteurs du Nous
  Portal et d'OpenRouter.
- Boucle d'agent et compression : un rappel périodique bloqué n'arrête plus le
  renouvellement de bail, un pilotage en milieu de tour est persisté comme sa
  propre ligne utilisateur, un rejet pour plafond de mémoire d'inférence locale
  fait marche arrière au lieu de compresser l'historique, et la compression ne
  tombe plus en silence sur les réessais auxiliaires.
- Interface : `hermes -z --resume` reprend la session, la bascule Bureau vers TUI
  ne reconstruit plus le prompt système et ne casse plus le cache de prompt, les
  vérifications de mise à jour interrogent l'API GitHub une fois par jour au lieu
  de récupérer le dépôt toutes les trente minutes, et une soixantaine d'autres
  correctifs du bureau viennent surtout de @OutThisLife et @kshitijk4poor.
- Cron et kanban : une exécution immédiate hors créneau n'annule plus la
  prochaine exécution planifiée, une exécution manuelle tuée ne bloque plus la
  suivante pendant cinq minutes, un travail unique changé en récurrent continue
  de se déclencher, et `--clone-all` ne copie plus les tâches cron.
- Outils et mémoire : un serveur MCP stdio qui meurt en cours d'appel ne rejoue
  plus l'appel d'outil, une revue de fond limitée aux skills ne peut plus
  supprimer d'entrées de mémoire, `tool_search` ne renvoie plus cinq outils
  partageant un mot, et la lecture RSS et Reddit ne s'active plus par défaut.
- Entretien : les sauvegardes de `config.yaml` vivent dans un répertoire borné,
  `hermes backup` garde les trois archives les plus récentes, et la rétention des
  partages de débogage tombe à un jour sur le service de repli.

La mise à jour se fait avec `hermes update`. Si la base a déjà été abîmée par
v0.21.0 ou v0.21.1, les notes renvoient vers `hermes doctor`, qui distingue
désormais l'atteinte structurelle de l'atteinte d'index, puis vers
`hermes sessions recover --inspect-only`, épinglé au profil.

> Sources : [Hermes Agent v0.21.2 (v2026.9.11), notes de release, teknium1, 11 septembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.11) et [flux des releases, dépôt hermes-agent](https://github.com/NousResearch/hermes-agent/releases.atom)

## Wingtips #70 : brancher des dossiers de skills externes

witcheer décrit dans le soixante-dixième numéro des Wingtips le cas où les skills
ne vivent pas toutes dans Hermes : on garde un même dossier pour tous les outils
d'agent qu'on utilise, ou l'équipe les range dans un dépôt partagé. Hermes Agent
sait scanner ces dossiers en plus du sien, par `external_dirs` sous la section
`skills` de `config.yaml`.

La documentation des skills détaille le comportement. Les chemins acceptent
l'expansion de `~` et la substitution de variables d'environnement, comme
`${SKILLS_REPO}/skills`. Les skills trouvées sont pleinement intégrées : elles
apparaissent dans l'index du prompt système, dans `skills_list`, dans
`skill_view` et comme commandes slash, sans différence avec les locales. En cas
de doublon de nom, la version locale l'emporte. Un dossier externe n'est pas une
frontière de protection en écriture : si le processus Hermes peut y écrire, les
actions de gestion de skills de l'agent peuvent y modifier des fichiers, et il
faut passer par les permissions du système de fichiers pour garder un dossier
partagé en lecture seule. Un chemin inexistant est ignoré en silence, ce qui
permet de déclarer un dossier optionnel absent de certaines machines. Les
nouvelles skills créées par l'agent continuent d'aller dans le dossier local.

En réponse à sa propre publication, witcheer donne le prompt à confier à l'agent
pour faire l'inventaire : lister tous les dossiers de la machine qui contiennent
des fichiers `SKILL.md` hors de `~/.hermes/skills`, dire lesquels méritent
d'entrer dans `skills.external_dirs`, et ne rien changer.

> Sources : [@witcheer, Hermes Wingtips #70 : skills.external_dirs, 12 septembre 2026](https://x.com/witcheer/status/2098679753960034724) et [Skills System, External Skill Directories, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#external-skill-directories)

## Parler à un agent qui travaille déjà

HermesAgentTips rappelle le 12 septembre qu'un message envoyé pendant que l'agent
travaille ouvre normalement un nouveau tour, et décrit les trois façons de faire
autrement. `/steer` suivi de la correction laisse l'outil en cours se terminer et
accroche la note au dernier résultat d'outil, sans interruption ni boucle
abandonnée. `/queue` retient un prompt pour le tour suivant. `/busy` règle le
comportement par défaut quand on écrit pendant que Hermes travaille.

La référence des commandes confirme les trois. `/steer <prompt>` injecte une note
en cours d'exécution qui arrive à l'agent après l'appel d'outil suivant, sans
interruption ni nouveau tour utilisateur : le texte est ajouté au contenu du
dernier résultat d'outil une fois l'outil terminé, ce qui donne du contexte
supplémentaire sans casser la boucle d'appels en cours, par exemple pour
rediriger vers un module précis pendant que les tests tournent. `/queue <prompt>`,
alias `/q`, met un prompt en file pour le tour suivant sans interrompre la
réponse en cours. `/busy [queue|steer|interrupt|status]` choisit ce qui se passe
quand on écrit pendant que Hermes travaille, dans le CLI comme dans la passerelle
de messagerie.

> Sources : [@HermesAgentTips, /steer, /queue et /busy, 12 septembre 2026](https://x.com/HermesAgentTips/status/2098742992819409293) et [Slash Commands Reference, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## Un essaim d'agents lancé sur le défi Hutter Prize

mervenoyann a annoncé le 11 septembre un essaim d'agents qui cherche le meilleur
algorithme de compression sans perte, dans le cadre du Hutter Prize, avec
Hugging Face comme terrain. Le principe : rejoindre l'organisation, donner à son
agent un jeton d'écriture pour celle-ci, cliquer sur « add your agent » et coller
l'extrait fourni dans Codex, Claude Code ou Hermes Agent. Teknium a relayé
l'annonce le même jour en invitant à mettre son agent à l'épreuve.

La page de l'organisation `agent-collaborations` décrit le dispositif. Ce sont
des espaces de travail partagés où des agents guidés par des humains travaillent
sur un même problème dans la durée, coordonnent leurs efforts et s'appuient sur
les avancées des autres, au lieu de repartir de zéro : les participants partagent
expériences, artefacts, solutions partielles, résultats négatifs et leçons, et
les humains restent dans la boucle pour orienter les pistes prometteuses et
débloquer les agents. Deux collaborations sont ouvertes, le Hutter Prize, qui
vise des compresseurs sans perte toujours plus compacts pour la Wikipédia
anglaise, et Trace Monitoring, consacré à la détection de sabotage discret dans
les trajectoires d'agents longues. Une fois connecté depuis le tableau de bord,
l'agent lit ce que les autres ont essayé, échange avec les autres agents, partage
artefacts et résultats et trouve du travail utile à apporter ; l'organisation
compte 31 membres, 25 espaces de stockage et neuf espaces de travail.

> Sources : [@mervenoyann, Join the agent swarm that finds the ultimate compression algorithm!, 11 septembre 2026](https://x.com/mervenoyann/status/2098396300785967129), [@Teknium, Put your Hermes Agent through the gauntlet!, 11 septembre 2026](https://x.com/Teknium/status/2098519011298611404) et [Agent Collaborations, Hugging Face](https://huggingface.co/agent-collaborations)

## Trente-huit modèles passés au crible de la mémoire vive

witcheer a publié le 12 septembre des tables d'adéquation mémoire tirées de sa
carte RTX 5090 : chaque ligne de ses relevés devient une table d'adéquation pour
les cartes de 8, 12, 16, 24 et 32 gigaoctets, avec le pic de mémoire vive mesuré
sur un prompt de 16 mille jetons plus 768 mébioctets de marge, rapporté à la
taille de la carte. Le relevé couvre trente-huit modèles et quantifications.

La légende distingue quatre cas : ce qui tient avec un contexte de 16 mille
jetons, ce dont le fichier tient mais pas le pic à 16 mille, ce qui est trop gros,
et ce qui passe par un déchargement d'experts sur le processeur. Le classement par
qualité de ce qu'une carte de 16 gigaoctets exécute à 16 mille jetons commence par
Qwen3.8-27B UD-IQ3_XXS, noté 92,7.

> Sources : [@witcheer, tables d'adéquation mémoire pour cartes de 8 à 32 Go, 12 septembre 2026](https://x.com/witcheer/status/2098648245731742089)

## Tonbi enchaîne avec la deuxième partie de sa masterclass du bureau

tonbistudio a publié le 11 septembre la deuxième partie de sa masterclass
consacrée à l'application de bureau Hermes, après une première partie sortie le
4 septembre sur l'installation et les réglages. Celle-ci porte sur le travail
réel dans l'application : les sessions, le composeur, la conversation vocale, les
sous-agents et la revue de code intégrée. Teknium l'a relayée le 12 septembre en
présentant la série comme le moyen de tirer le maximum du bureau.

> Sources : [@tonbistudio, Part 2 of my Hermes Desktop Masterclass, 11 septembre 2026](https://x.com/tonbistudio/status/2098451861275898085) et [@Teknium, Check out tonbistudio's new series on maximizing Hermes Agent's Desktop app, 12 septembre 2026](https://x.com/Teknium/status/2098624116815430080)

## Un connectome de mouche branché sur Hermes

adolandev a monté le 12 septembre un montage où Hermes propose des actions d'outil
et un modèle simplifié de cerveau de mouche, issu d'un connectome de drosophile,
choisit laquelle exécuter. Le résultat est modeste mais concret : le montage a
corrigé un vrai défaut, après avoir choisi de façon répétée le test qui échouait,
et il est présenté en vidéo.

> Source : [@adolandev, I wired a fruit fly connectome into Hermes, 12 septembre 2026](https://x.com/adolandev/status/2098620483864310268)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
