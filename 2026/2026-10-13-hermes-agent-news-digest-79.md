# Hermes Agent Quotidien #79

Cette édition revient sur les 81 pull requests fusionnées le 12 octobre, sur le plugin redline qui permet de relire les documents et le code produits par l'agent, sur un journal d'usage de l'IA locale tenu par The Verge avec Hermes Agent, et sur un récapitulatif des fichiers de contexte lus par l'agent.

## 81 pull requests fusionnées le 12 octobre

iamlukethedev a fait le compte le 13 octobre : Hermes a fusionné 81 pull requests le 12 octobre. Les changements mis en avant :

- Les aperçus de session de Desktop reviennent à côté du chat et se remplissent même quand la fenêtre reste en arrière-plan.
- Arrêter met toujours fin au tour : Desktop peut supprimer n'importe quelle session, et chaque chemin de reprise répare l'espace de travail enregistré d'un profil nommé.
- Les clés Anthropic Console (sk-ant-usr, sk-ant-svc, sk-ant-admin et key_cmd) s'authentifient en x-api-key, plus en Bearer ni en OAuth.
- Langfuse quitte le cœur pour le plugin officiel langfuse, avec une migration automatique pour les utilisateurs existants.
- plugins validate prévient quand un plugin importe des modules privés du cœur de Hermes.
- L'API du cycle de vie des sous-agents achemine le fournisseur à chaque lancement et fonctionne en isolation d'hôte.
- Ctrl+C efface un brouillon en cours de saisie au lieu de tuer le tour qui tourne.
- Les installations de plugins fonctionnent sur n'importe quel miroir de paquets : l'ancienneté de la release est vérifiée au verrouillage côté Hermes (3 jours), pas sur les machines des utilisateurs.
- Home Assistant ne s'auto-installe plus dans les profils qui ne l'ont jamais utilisé ; les auto-installations de plugins en échec reculent au lieu de retenter toutes les heures.
- L'identité invitée apparaît à la première utilisation d'un connecteur, et les connecteurs du niveau gratuit emploient un jeton invité réservé aux connecteurs.
- Le préfixe fixe du prompt baisse de 2,1 k jetons par requête après le régime.
- L'avancement de la release stable se fie aux reçus au lieu de télécharger environ 33 Go, et les installations limitées au cœur comme hermes update fonctionnent de nouveau sur les miroirs sans horodatage de téléversement.

Au total, 81 nouvelles fonctionnalités et corrections.

> Sources : [@iamlukethedev, Hermes merged 81 PRs on October 12, 13 octobre 2026](https://x.com/iamlukethedev/status/2109794246282842502)

## redline, un plugin de relecture dans Desktop

witcheer a signalé le 13 octobre que la communauté a construit redline, un plugin de Hermes Desktop pour relire les documents et le code que l'agent écrit. Il ouvre le fichier dans un panneau à côté du chat : on sélectionne un passage pour laisser un commentaire, une question ou une demande de modification, on envoie une note immédiatement ou on en met plusieurs en file pour les envoyer en un seul lot, puis l'agent édite le fichier pendant que le panneau se rafraîchit, les notes étant enregistrées à côté du document.

Le plugin est au catalogue, maintenu par silentpr0, épinglé à la version 0.1.0 et compatible avec Hermes 0.21.5 et au-delà. La fiche du catalogue précise son périmètre : il lit un chemin local .md ou .markdown choisi par l'utilisateur (jusqu'à 1 Mo, liens symboliques résolus), écrit uniquement le fichier annexe <document>.md.redline.json à côté, et accroche transform_llm_output pour ajouter une ligne de directive ::redline aux réponses finales éligibles. Pas de réseau au-delà de la passerelle locale, pas d'identifiants, pas de télémétrie ni de sous-processus ; le panneau interroge le backend local toutes les trois secondes tant qu'il est ouvert. Il s'installe avec hermes plugins install redline.

> Sources : [@witcheer, the community built redline, a Hermes Desktop plugin for reviewing the documents and code your Hermes Agent writes, 13 octobre 2026](https://x.com/witcheer/status/2109954804613349697) et [redline, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins)

## The Verge tient un journal d'IA locale avec Hermes Agent

witcheer a relayé le 12 octobre un article de The Verge : le journaliste Antonio G. Di Benedetto ouvre un journal d'usage de l'IA locale, en installant Hermes Agent sur un Mac Studio M5 Ultra à 256 Go de mémoire unifiée. Son choix de modèle, Qwen 3.8 Flash Next, compte 125 milliards de paramètres pour environ 105 Go, et il pilote l'agent depuis son téléphone grâce à un bot Telegram.

Le journal détaille les premières tâches réelles. Un briefing matinal programmé par cron lit ses e-mails et son agenda et ajoute un bulletin météo, mais il a échoué plusieurs fois parce que le Mac dormait à l'heure prévue de 7 h 30. Le tri de sa bibliothèque Steam, plus de 400 jeux, a demandé de fournir une clé d'API Steam Web, supprimée aussitôt la tâche finie. Il a aussi confié à Hermes l'analyse de relevés financiers et un tableau comparatif de caractéristiques pour un ordinateur portable sous embargo. Le motif, pour lui, c'est la confidentialité : traiter sur sa propre machine des données qu'il ne veut pas envoyer dans le cloud. Il conclut sans enthousiasme : l'IA locale est un programme à faire tourner, pas un ami numérique.

> Sources : [@witcheer, The Verge started a local AI diary on a Mac Studio, with Hermes Agent doing the work, 12 octobre 2026](https://x.com/witcheer/status/2109596187863249270) et [Antonio G. Di Benedetto, Learning to use local AI is exciting, overwhelming, and frustrating, The Verge, 11 octobre 2026](https://www.theverge.com/ai-artificial-intelligence/1008484/learning-local-ai-hermes-qwen-model-mac-studio-testing-diary-progress)

## Les fichiers de contexte, cinq réponses

witcheer a publié le 13 octobre cinq réponses sur les fichiers de contexte de Hermes Agent :

- Lesquels sont lus ? Les consignes de projet vont dans un fichier .hermes.md ou AGENTS.md, et les fichiers déjà tenus pour d'autres outils de codage sont lus aussi. SOUL.md est à part : il vit dans ~/.hermes et règle la personnalité et le ton de l'agent.
- Lequel gagne ? Un seul type de fichier de projet se charge par session, au premier qui correspond : .hermes.md, puis AGENTS.md, puis les fichiers des autres outils. SOUL.md est hors de cet ordre et se charge à chaque session.
- Où les cherche-t-il ? Dans le répertoire de travail. Dans le CLI, c'est le dossier où l'on lance hermes. Sur messagerie, c'est terminal.cwd dans la config, et le dossier personnel quand il n'est pas défini.
- Et les sous-dossiers ? Dans un dépôt git, chaque AGENTS.md de la racine jusqu'au répertoire de travail se charge, les plus profonds prenant le dessus. Quand l'agent travaille dans d'autres sous-dossiers, il récupère leurs fichiers de contexte à la première lecture.
- Comment vérifier ce qui est chargé ? /context termine par la liste des fichiers de contexte, en montrant ceux qui sont chargés et ceux qui sont écartés parce qu'un fichier plus prioritaire l'a emporté. La commande tourne en local, sans appel de modèle.

La documentation ajoute un point de mécanique : les AGENTS.md d'un dépôt git sont chargés en une chaîne fusionnée au démarrage, et la découverte progressive n'injecte les fichiers de sous-dossiers qu'au moment où l'agent y lit quelque chose. SOUL.md, lui, est chargé uniquement depuis HERMES_HOME, jamais depuis le répertoire de travail.

> Sources : [@witcheer, context files in Hermes Agent, here are five tips, 13 octobre 2026](https://x.com/witcheer/status/2109977464307073043) et [Context Files, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
