# Hermes Agent Quotidien #67

Cette édition revient sur le tutoriel NVIDIA qui trace les exécutions de Hermes Agent avec NeMo Relay, sur l'ouverture du plugin système aux packs de langue, sur les 133 pull requests fusionnées le 30 septembre, sur la commande /context présentée dans les Wingtips, sur le geste pour attacher une page, un fichier ou un dossier dans un message, et sur la carte mémoire de Hermes Desktop.

## NVIDIA et Nous publient un tutoriel pour tracer les exécutions de Hermes Agent

NVIDIA et Nous Research ont publié le 30 septembre un tutoriel commun qui montre comment tracer et évaluer les exécutions de Hermes Agent avec NeMo Relay. Le billet, signé William Markito Oliveira, Maryam Najafian, Moon Chung et Teknium, part du constat qu'un agent peut terminer une tâche en empruntant un chemin inefficace, et qu'un contrôle de succès seul n'explique pas pourquoi l'agent s'est repris après une erreur d'outil, s'est arrêté tôt ou a enchaîné des appels de modèle superflus.

Hermes Agent intègre NeMo Relay nativement et représente ses sessions, tours, appels de modèle et appels d'outils dans la hiérarchie de portées de NeMo Relay. Une exécution produit trois représentations : le flux ATOF, journal JSONL des débuts et fins de portées avec identifiants et horodatages ; la trajectoire ATIF, enregistrement JSON pas à pas des interactions, appels d'outils et observations ; et des spans OpenTelemetry étiquetés OpenInference, à ouvrir dans un outil compatible comme Arize Phoenix.

Le tutoriel fait tourner deux exemples. Le premier, volontairement petit, lance dans un conteneur Docker isolé un script qui affiche VALUE=42, pour vérifier que le montage complet fonctionne. Le second est une tâche de recherche multi-outils : Hermes lit un dossier de voyage, cherche sur le web, vérifie une conférence sur son site officiel, écrit un rapport et doit renvoyer COLT 2026, tous les spans de modèle et d'outil étant envoyés à Phoenix.

Les auteurs prolongent avec une étude de cas Hermes ToolPerf qui compare, sur 108 exécutions, une révision de base et une révision corrigée : Qwen Coder 30B récupère davantage de tâches mais augmente les appels, les données échangées et la latence. witcheer résume le gain d'un trait : avec NeMo Relay, une exécution de Hermes Agent laisse une trace complète, chaque appel de modèle, appel d'outil, nouvelle tentative et erreur étant horodaté. Teknium ajoute que plus on a de données à regarder, mieux on peut s'en servir pour optimiser le harnais.

> Sources : [Tracing Agent Harness Behavior with NVIDIA NeMo Relay, blog technique NVIDIA, 30 septembre 2026](https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/), [@NVIDIAAI, We worked with @NousResearch/@Teknium on a hands-on walkthrough of NVIDIA NeMo Relay, 30 septembre 2026](https://x.com/NVIDIAAI/status/2105330651654508734), [@witcheer, with NeMo Relay, a Hermes Agent run leaves a full trace, 30 septembre 2026](https://x.com/witcheer/status/2105333798661742882) et [@Teknium, thanks to nemo relay we had a lot more to work with, 1er octobre 2026](https://x.com/Teknium/status/2105509432193081546)

## Le plugin système accueille les packs de langue

Teknium a annoncé le 1er octobre qu'on peut désormais ajouter des langues entières sur toutes les surfaces de Hermes via un plugin, en plus des seize déjà prises en charge. witcheer a condensé l'annonce en une phrase : l'agent parle maintenant n'importe quelle langue.

La mécanique passe par la déclaration `provides_locales` dans le fichier `plugin.yaml` d'un plugin. Un pack peut ajouter une langue d'interface ou réécrire la formulation d'une langue existante pour toutes les surfaces à la fois : le cœur Python (invites d'approbation, réponses de passerelle, verbes d'outils), l'interface TUI et l'application Desktop. Aucun code Python n'est requis, il suffit de déclarer la langue et de fournir les fichiers YAML correspondants dans le dossier `locales/` du plugin.

Les catalogues sont superposables et partiels. Un pack ne traduit que ce qu'il fournit, le reste retombe sur le catalogue de base ou sur l'anglais, jamais sur une clé brute. Ajouter une langue ne sélectionne pas la langue : le choix de l'utilisateur reste celui de `display.language`.

> Sources : [@Teknium, You can now add full new languages across all of Hermes' surfaces via Plugin, 1er octobre 2026](https://x.com/Teknium/status/2105520243481411791), [@witcheer, your Hermes Agent now speaks any language, 1er octobre 2026](https://x.com/witcheer/status/2105525651729940685) et [Build a Hermes Plugin, Ship a language pack, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)

## 133 pull requests fusionnées le 30 septembre

iamlukethedev a fait le compte le 1er octobre : Hermes a fusionné 133 pull requests le 30 septembre. Trois entrées figurent dans le texte du message, le reste de la liste étant détaillé dans la capture jointe :

- Épingler des modèles dans une section Favorites du sélecteur de modèles de Desktop.
- Une taille de texte de discussion réglable indépendamment, avec des valeurs par défaut d'interface compacte.
- Chaque discussion de Desktop peut installer des plugins et des skills du catalogue dans son propre profil.

imbabybrooklyn confirme la nouveauté côté Desktop et remercie HermesAgentTips pour la contribution.

> Sources : [@iamlukethedev, Hermes merged 133 PRs on September 30, 1er octobre 2026](https://x.com/iamlukethedev/status/2105591484104015936) et [@imbabybrooklyn, You can favourite a model in Hermes Desktop, 30 septembre 2026](https://x.com/imbabybrooklyn/status/2105434626512855423)

## Wingtips #88 : /context

witcheer a consacré le quatre-vingt-huitième numéro des Wingtips à la commande `/context`. La fenêtre de contexte de Hermes Agent contient bien plus que les messages : l'invite système, les définitions d'outils, la mémoire, les règles de projet et la conversation en cours. La commande affiche la part que chacun occupe.

La documentation des commandes précise le rendu. Sur CLI et TUI, `/context` affiche une grille de cent cellules où chaque cellule vaut environ un pour cent de la fenêtre du modèle, puis un tableau estimé par catégorie, invite système, définitions d'outils, règles, index des skills, MCP, sous-agents, mémoire et conversation, en regard de l'espace libre. Sur les plateformes de messagerie, la même décomposition arrive en texte simple avec une jauge d'usage. La commande est en lecture seule et calculée localement, sans appel au modèle ni impact sur le cache d'invite. L'alias `/ctx` existe, et `/context all` ajoute le coût détaillé par skill et par ensemble d'outils.

> Sources : [@witcheer, Hermes Wingtips #88: /context, 1er octobre 2026](https://x.com/witcheer/status/2105552884670550343) et [Slash Commands Reference, /context, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)

## Attacher une page web, un fichier ou un dossier dans un message

witcheer a montré le 30 septembre comment remettre une page web à son agent dans n'importe quel message. Dans la boîte de message, on tape `@`, on choisit `@ url:`, on colle le lien et on pose la question. La page est récupérée et jointe au message avant que l'agent ne la lise.

Le même menu attache un fichier ou un dossier, et la documentation des références de contexte détaille la syntaxe complète. `@file:chemin/vers/fichier.py` injecte le contenu du fichier, avec la possibilité de cibler une plage de lignes ; `@folder:chemin/vers/dossier` injecte l'arborescence du dossier avec ses métadonnées ; `@url:` récupère le contenu d'une page. Les références sont développées avant que le message n'atteigne le modèle, le contenu étant ajouté sous une section de contexte joint. Plusieurs références tiennent dans un même message, et dans le CLI interactif, le `@` déclenche la complétion.

> Sources : [@witcheer, you can hand your Hermes Agent a web page inside any message, 30 septembre 2026](https://x.com/witcheer/status/2105300357421179009) et [Context References, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)

## La carte mémoire de Hermes Desktop

witcheer a publié le 1er octobre une vidéo de la carte qui rassemble tout ce que son agent a appris depuis sa création. Les points dorés sont les skills, les losanges bleus les souvenirs, les plus anciens au centre. Passer la souris sur un point affiche de quelle skill ou de quel souvenir il s'agit, et un clic droit permet de l'éditer ou de le supprimer, une skill supprimée étant archivée.

La documentation du bureau décrit la fonction sous le nom de Memory Graph. C'est une carte interactive de ce que Hermes a appris, skills et souvenirs disposés en graphe de nœuds zoomable avec une ligne du temps, filtrable par tout, utilisé ou appris. On l'ouvre depuis la palette de commandes ou via `/journey`, dont les alias sont `/learning` et `/memory-graph`. Un contrôle d'export partage la disposition de la carte sous forme de code compact à coller ailleurs, sans le texte des souvenirs ni des skills, et le même code peut être importé.

> Sources : [@witcheer, everything my Hermes Agent has learned for me since I created it is here, 1er octobre 2026](https://x.com/witcheer/status/2105636918046183541) et [Hermes Desktop, Memory Graph, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
