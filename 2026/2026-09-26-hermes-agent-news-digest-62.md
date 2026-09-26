# Hermes Agent Quotidien #62

Cette édition revient sur la clé `mcp.discovery_concurrency` qui plafonne la découverte des serveurs MCP au démarrage, sur la refonte de l'interface du kanban de Hermes Agent, sur l'invite qui fait rédiger à l'agent son propre manuel, et sur la commande vocale native ajoutée à Hermes OS.

## Wingtips #84 : mcp.discovery_concurrency

witcheer a consacré le quatre-vingt-quatrième numéro des Wingtips à `mcp.discovery_concurrency`, une nouvelle clé de Hermes Agent qui plafonne le nombre de serveurs MCP connectés en même temps. Les serveurs déclarés dans la configuration se connectent au démarrage de Hermes Agent, et chaque serveur local tourne dans son propre processus.

La documentation de la fonction MCP précise le réglage. Hermes découvre les serveurs MCP au démarrage et enregistre leurs outils dans le registre normal. Les serveurs sont connectés au maximum quatre à la fois par passe de découverte, au démarrage, sur `/reload-mcp` et sur l'observateur de configuration. Chaque serveur stdio lance son propre arbre de processus enfants, si bien qu'une passe sans plafond avec beaucoup de serveurs les lançait tous au même instant, avec un pic de CPU et de RAM et, sur les flottes multi-profils, une rafale d'appels fournisseur simultanés. La clé se règle dans `config.yaml` sous `mcp.discovery_concurrency`, quatre par défaut, la valeur zéro supprimant la limite.

> Sources : [@witcheer, Hermes Wingtips #84: mcp[.]discovery_concurrency, 26 septembre 2026](https://x.com/witcheer/status/2103850251220042077) et [MCP (Model Context Protocol), documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/)

## Le kanban de Hermes Agent passe à une vue à deux colonnes

Tony Simons a annoncé le 26 septembre une refonte majeure de l'interface du kanban de Hermes Agent, présentée comme bien plus qu'un simple rafraîchissement. La nouvelle vue de tâche à deux colonnes regroupe les commentaires, l'activité, les exécutions et les journaux de worker dans un même fil, les dépendances affichent les tâches réellement liées, le rendu Markdown est complet et les propriétés sont plus propres. La démonstration est en vidéo.

witcheer a complété le même jour : sur une tâche en cours, la zone de commentaire part directement vers le worker, ce qui permet de piloter la tâche depuis la même fenêtre.

> Sources : [@tonysimons_, Hermes Agent's Kanban just got a MASSIVE UI upgrade, 26 septembre 2026](https://x.com/tonysimons_/status/2103707278037631420) et [@witcheer, the comment box goes straight to the worker, 26 septembre 2026](https://x.com/witcheer/status/2103770155423600646)

## Hermes Agent rédige son propre manuel

witcheer a partagé le 26 septembre une invite qui fait écrire à Hermes Agent son propre manuel : modèle, fournisseur, plateformes, tâches cron, skills, emplacement de la mémoire et des sessions, et la marche à suivre pour la sauvegarde. L'agent vérifie chaque ligne sur la machine, et les clés s'affichent comme « set » ou « not set ». L'invite à copier-coller est donnée dans le premier commentaire.

> Source : [@witcheer, your Hermes Agent can write its own manual, 26 septembre 2026](https://x.com/witcheer/status/2103764777621147741)

## Hermes OS se pilote à la voix

iamlukethedev a montré le 25 septembre la commande vocale native qu'il vient d'ajouter : une seule consigne, « Crée un site web pour un salon de coiffure », et son agent s'est mis à écrire du code, à se déplacer entre les fenêtres et à construire le site sous ses yeux, le processus entier étant suivi en temps réel.

Le tweet s'appuie sur sa présentation de Hermes OS, son système sous Linux sur lequel il travaille côté bureau, lanceur d'applications et espaces séparés pour le personnel, le travail et les idées.

> Sources : [@iamlukethedev, I gave Hermes OS one voice command and watched it build a website, 25 septembre 2026](https://x.com/iamlukethedev/status/2103447385364185543) et [@iamlukethedev, Hermes OS is running on Linux, 21 septembre 2026](https://x.com/iamlukethedev/status/2101917441513414862)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
