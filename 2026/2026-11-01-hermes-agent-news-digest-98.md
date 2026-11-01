# Hermes Agent Quotidien #98

Cette édition revient sur l'ouverture de la bêta de l'application mobile officielle, sur Hermes Agent devenu blueprint officiel de NemoClaw chez NVIDIA, sur le runtime de passerelle unifié qui prend le relais de toutes les sessions locales, et sur un Hermes Agent qui tient 30 tâches hors ligne sur une carte de 32 Go.

## La bêta mobile officielle ouvre sur iOS et Android

Le 30 octobre, pendant NousCon 2026 à New York, Nous Research a ouvert la bêta de son application mobile officielle. La page d'inscription dédiée propose deux accès : iOS par TestFlight, Android par Firebase App Distribution. Le 31 octobre, iamlukethedev a relayé la nouvelle et annoncé qu'il continue de construire Herald, son propre client communautaire, au motif que plus il y a de clients, plus les gens font tourner leur agent eux-mêmes.

L'application se connecte à la passerelle Hermes que l'on fait déjà tourner sur sa propre machine. C'est un client, pas un agent séparé qui tournerait sur le téléphone : il permet de discuter en continu, d'approuver les appels d'outils, et de gérer ses bots et ses routines depuis n'importe où. Teknium, cofondateur et ingénieur principal de Hermes Agent, a confirmé sur X que les bêtas iPhone et Android ont démarré ensemble le jour de NousCon. Aucune date de sortie générale n'a été annoncée, et plusieurs clones tiers existent déjà ; les liens à utiliser sont ceux de la page officielle.

> Sources : [@iamlukethedev, The official Hermes app is open for beta on iOS and Android, 31 octobre 2026](https://x.com/iamlukethedev/status/2116661188495085748) et [Hermes Mobile Beta, page d'inscription Nous Research](https://hermes-agent.nousresearch.com/mobile)

## Hermes Agent, blueprint officiel de NemoClaw chez NVIDIA

iamlukethedev a annoncé le 1er novembre que NVIDIA a fait de Hermes Agent un blueprint officiel de NemoClaw. C'est l'un des trois harnesses retenus, aux côtés d'OpenClaw et de LangChain Deep Agents.

Le billet technique de NVIDIA, publié le 30 octobre par Nicola Sessions, détaille l'assemblage. Un blueprint NemoClaw réunit quatre composants autour du harness choisi : les modèles ouverts Nemotron pour le raisonnement, les outils NeMo (dont NeMo Relay pour observer et améliorer l'exécution), et OpenShell, le runtime sécurisé qui gouverne l'accès de l'agent aux fichiers, au réseau, aux identifiants et aux outils. La pile ne remplace pas l'agent existant : on garde Hermes Agent tel quel, et le blueprint assemble ce qui l'entoure sans avoir à le réécrire. Hermes Agent est présenté comme un harness qui s'améliore à l'usage, en capturant en skills durables les corrections et les workflows que l'on répète.

Le dépôt communautaire de NemoClaw embarque aussi une recette de « Chief of Staff » à mémoire, bâtie comme un profil Hermes déployable, où OpenShell garde les identifiants d'inférence et les connexions MCP hors de la sandbox, et où NeMo Relay ferme les traces aux frontières réelles de session.

> Sources : [@iamlukethedev, NVIDIA just made Hermes Agent an official NemoClaw blueprint, 1er novembre 2026](https://x.com/iamlukethedev/status/2116699490111652086) et [Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw, blog technique NVIDIA, 30 octobre 2026](https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/)

## Un seul runtime de passerelle pour toutes les sessions locales

Le 1er novembre, iamlukethedev a fait le compte d'octobre : malgré sa propre conférence, Nous a fusionné 130 pull requests dans Hermes en octobre. Il en retient une de taille : une seule passerelle possède désormais chaque session locale, du CLI classique à la TUI, au Desktop, à l'API, à ACP, aux bots et au cron, tous réunis dans un seul runtime.

La pull request #106742, signée teknium1 et fusionnée le 14 octobre, décrit le mécanisme. Avant elle, chaque surface lançait son propre agent sur le même state.db, et plusieurs pouvaient écrire la même conversation en même temps. Désormais, chaque profil a un processus de passerelle unique qui possède ses sessions, et toutes les surfaces s'y attachent comme client. Une conversation ouverte dans le CLI, la TUI, Desktop, un éditeur, un canal de bot, un webhook ou un cron est une seule conversation, avec une seule file FIFO, une seule file durable et un seul rédacteur. Les admissions en file survivent au redémarrage du propriétaire et s'exécutent dans l'ordre, une fois. Si une admission perd son propriétaire en cours de route, elle passe à l'état inconnu et n'est jamais rejouée automatiquement. Les approbations et les clarifications sont partagées : on y répond dans n'importe quelle fenêtre et tous les afficheurs se mettent d'accord.

> Sources : [@iamlukethedev, Last day of October, 1er novembre 2026](https://x.com/iamlukethedev/status/2116753893631864933) et [Unified gateway runtime, PR #106742, dépôt hermes-agent, fusionnée le 14 octobre 2026](https://github.com/NousResearch/hermes-agent/pull/106742)

## 30 tâches d'agent hors ligne sur une carte de 32 Go

witcheer a mesuré le 31 octobre ce qu'un Hermes Agent en modèle local arrive à faire selon la mémoire du GPU : une carte de 12 Go franchit déjà 27 des 30 tâches d'agent, une carte de 32 Go les 30.

Les 30 tâches tournent hors ligne dans Hermes Agent : renommer du code à travers plusieurs fichiers, résoudre un conflit de merge git, retrouver le mauvais commit dans un historique de 14 commits, corriger cinq bugs, et d'autres du même ordre. Le message ne précise ni le modèle ni la quantification employés, seulement le seuil de mémoire qui sépare un parcours presque complet d'un parcours complet.

> Source : [@witcheer, a 12 GB card already gets Hermes Agent through 27 of 30 agent tasks, 31 octobre 2026](https://x.com/witcheer/status/2116621479735693809)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
