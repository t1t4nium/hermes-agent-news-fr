# Hermes Agent Quotidien #71

Cette édition revient sur le numéro 92 des Wingtips consacré à la mise en route de Nous Portal en une seule commande, sur le catalogue de plugins qui approche les 500 entrées, sur la collection de 68 profils Star Trek prêts à installer, sur le rappel des profils pour exécuter plusieurs agents, et sur une table de poker où des agents jouent au Hold'em.

## Wingtips #92 : Nous Portal en une commande

witcheer a consacré le numéro 92 des Wingtips à la commande `hermes setup --portal`. Sur une installation neuve, une seule commande connecte Hermes Agent à Nous Portal, définit Nous comme fournisseur de modèle et active le Tool Gateway. Le navigateur s'ouvre pour la connexion, on choisit un modèle, et l'agent est prêt à discuter.

La documentation du portail détaille le déroulé. La commande lance la connexion OAuth sur portal.nousresearch.com, enregistre le jeton d'actualisation dans `~/.hermes/auth.json`, laisse choisir un modèle Nous, fixe `model.provider: nous` dans `config.yaml` et active le Tool Gateway pour la recherche web, la génération d'images, la synthèse vocale et l'automatisation du navigateur. Sans abonnement, il faut d'abord s'inscrire sur portal.nousresearch.com/manage-subscription. Sur une installation déjà configurée avec un autre fournisseur, on peut ajouter le portail à côté via `hermes model` puis choisir Nous Portal, ou via `hermes portal`. La commande `hermes portal info` vérifie ensuite la connexion, le modèle et l'état du Tool Gateway.

> Sources : [@witcheer, Hermes Wingtips #92: Nous Portal in one command, 5 octobre 2026](https://x.com/witcheer/status/2106998344337731926) et [Nous Portal, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)

## Le catalogue de plugins approche les 500 entrées

Teknium a annoncé le 4 octobre que le catalogue de plugins grandit vite, avec près de 500 mods qui ajoutent des capacités, des fournisseurs de modèles, des améliorations de mémoire, des composants visuels et plus encore. Chaque entrée s'installe par nom avec `hermes plugins install <nom>`.

La page du catalogue, consultée le jour même, affiche 448 entrées réparties en neuf catégories, dont 9 officielles et 439 issues de la communauté. Les plus fournies sont les outils (122), Desktop (112), la mémoire (48), les modèles (35), l'automatisation (33) et le web et navigateur (33). Chaque entrée est épinglée à un commit précis et relue par l'équipe avant d'être référencée.

> Sources : [@Teknium, The plugins catalog had been growing fast! Nearly 500 mods to Hermes, 4 octobre 2026](https://x.com/Teknium/status/2106854087564378539) et [Plugin Catalog, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/)

## Une collection de 68 profils Star Trek prêts à installer

HermesWatcher a exhumé le 4 octobre une bibliothèque de 68 profils préfabriqués, publiée sous le compte GitHub teknium1 de Teknium. Le compte insiste : ce ne sont pas 68 peaux ou personnalités, chaque profil porte déjà son propre style de raisonnement, ses forces, sa méthode et son comportement. BkashJosi en donne quatre exemples : Spock pour investiguer pourquoi quelque chose casse, Data pour analyser un jeu de données, Picard pour peser une décision difficile et Worf pour revoir la sécurité.

Le dépôt hermes-star-trek-profiles contient les 68 distributions, inspirées des séries The Original Series, The Next Generation, Deep Space Nine et Voyager. Chaque personnage est une distribution de profil distincte, composée d'un `SOUL.md` substantiel couvrant l'identité, la voix, la vision du monde, la méthode, les forces, les angles morts, le comportement sous pression et le style de désaccord, plus une peau de terminal et un `config.yaml` neutre côté fournisseur. Aucun profil ne livre de secrets, de mémoire, de sessions, de modèle ni de tâche cron : la configuration de fournisseur reste celle de l'utilisateur. L'installation se fait via un script `manage.py` (un profil, une série entière ou toute la collection, avec `--alias`), et la distribution se présente comme une collection fan-made non officielle, sans lien avec Paramount ou CBS.

> Sources : [@HermesWatcher, Hermes has an entire library of 68 prebuilt profiles, 4 octobre 2026](https://x.com/HermesWatcher/status/2106806608529637493), [@BkashJosi, Stop writing every Hermes agent role from scratch, octobre 2026](https://x.com/BkashJosi) et [teknium1/hermes-star-trek-profiles, dépôt GitHub](https://github.com/teknium1/hermes-star-trek-profiles)

## Exécuter plusieurs agents avec les profils

witcheer a noté le 5 octobre que la question d'exécuter plusieurs agents est revenue souvent ce week-end, et résume l'essentiel. Pour séparer vie, travail et maison, on utilise les profils : un profil est un répertoire Hermes distinct, et il devient sa propre commande dès sa création.

La documentation précise la mécanique. Un profil est un répertoire d'accueil Hermes séparé, avec son propre `config.yaml`, son `.env`, son `SOUL.md`, sa mémoire, ses sessions, ses skills, ses tâches cron et sa base d'état. `hermes profile create coder` crée le profil et l'alias `coder`, puis `coder setup` configure les clés et le modèle, et `coder chat` démarre. Deux processus ne doivent jamais viser le même profil : chacun écrit la mémoire automatiquement et charge les écrits de l'autre au démarrage de session. Pour partir d'une base existante, `--clone` copie la configuration, les skills et la mémoire d'identité, `--clone-all` copie tout sauf l'historique de sessions et les tâches cron. Le plus rapide reste `hermes setup --portal` dans le nouveau profil pour câbler modèles et outils d'un coup.

> Sources : [@witcheer, running several agents with Hermes Agent came up a lot this weekend, 5 octobre 2026](https://x.com/witcheer/status/2107093853522088250) et [Profiles: Running Multiple Agents, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)

## Une table de poker pour agents

tonysimons_ a présenté le 5 octobre une table de poker pour agents Hermes : Agent Hold'em. Plusieurs agents s'assoient, jouent au Texas Hold'em, bluffent, misent, se couchent et tentent de se surpasser mutuellement. Voir des agents s'enfoncer dans de mauvaises décisions de poker est, selon lui, aussi divertissant que cela en a l'air.

> Source : [@tonysimons_, I built a poker table for Hermes Agents, 5 octobre 2026](https://x.com/tonysimons_/status/2106951334536622203)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
