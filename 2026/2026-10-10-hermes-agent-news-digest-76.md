# Hermes Agent Quotidien #76

Cette édition revient sur l'arrivée du modèle Step 5 Preview de StepFun sur Nous Portal, sur le numéro 98 des Wingtips consacré au fuseau horaire de l'agent, et sur les 67 pull requests fusionnées le 9 octobre, dont la sortie de Spotify du cœur et la bulle de dialogue du pet dans le SDK de Desktop.

## Step 5 Preview de StepFun, gratuit une semaine sur Nous Portal

Nous Research a annoncé le 9 octobre que Step 5 Preview, le nouveau modèle de StepFun, est gratuit sur Nous Portal pendant une semaine. Le modèle affiche 600 milliards de paramètres au total pour 27 milliards d'actifs en mélange d'experts, un contexte d'un million de jetons et la vision. Nous Research l'a d'abord crédité de 33,89 au Hermes Index, le même score que GPT-6 Luna, avant de publier une correction le même jour : le score final est 32,83, légèrement derrière GPT-6 Luna (33,89) et GLM 5.3 Flash (34,95).

StepFun présente Step 5 Preview comme son nouveau modèle phare pour le travail agentique, avec des performances de premier plan en ingénierie logicielle et en travail de connaissance professionnel, et une force particulière en finance.

> Sources : [@NousResearch, Step 5 Preview from @StepFun_ai is free on Nous Portal for the next week, 9 octobre 2026](https://x.com/NousResearch/status/2108638389045960958), [@NousResearch, Slight Correction: Step 5 Preview's final score on Hermes Index has been updated to 32.83, 9 octobre 2026](https://x.com/NousResearch/status/2108645938403405896) et [@StepFun_ai, Step 5 Preview is our new flagship model for agentic work](https://x.com/StepFun_ai)

## Wingtips #98 : régler le fuseau horaire de l'agent

witcheer a consacré le numéro 98 des Wingtips au fuseau horaire de Hermes Agent. Quand l'agent tourne sur un serveur situé dans un autre fuseau, la commande `hermes config set timezone America/New_York` lui donne le vôtre : l'horloge de l'agent et les planifications cron suivent ce fuseau, si bien qu'une tâche fixée à 8 h s'exécute à 8 h là où l'on se trouve.

La documentation de configuration précise la mécanique. La clé `timezone` accepte n'importe quel identifiant de fuseau IANA, et la variable d'environnement `HERMES_TIMEZONE` la surcharge quand elle est définie. Le réglage influe sur la planification cron et sur l'heure injectée dans le prompt système, mais pas sur les fichiers de journalisation, dont chaque ligne reste horodatée à l'heure locale de la machine.

> Sources : [@witcheer, Hermes Wingtips #98: set your agent's timezone, 10 octobre 2026](https://x.com/witcheer/status/2108882539788050645) et [Configuration, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## 67 pull requests fusionnées le 9 octobre

iamlukethedev a fait le compte le 9 octobre : Hermes a fusionné 67 pull requests le 9 octobre. Deux changements figurent dans le texte du message :

- Spotify quitte le cœur pour rejoindre le plugin officiel du catalogue, avec migration automatique des utilisateurs existants.
- Desktop gagne une bulle de dialogue dans le SDK de plugin (`ctx.pet.say`) et abandonne le bandeau « This could run on your computer ».

La page Spotify du catalogue détaille la sortie du cœur. Le plugin officiel, maintenu par Nous Research dans NousResearch/hermes-spotify, expose sept outils (lecture, appareils, file d'attente, recherche, playlists, albums, bibliothèque) sur l'API Web de Spotify avec OAuth PKCE. La migration est transparente : tout profil qui utilisait déjà Spotify, par une connexion dans son auth.json ou le toolset spotify, reçoit le plugin automatiquement à la mise à jour ou au premier démarrage. Le seul changement visible est l'orthographe des commandes, `hermes auth spotify` devenant `hermes spotify login`, status et logout.

La documentation du SDK de Desktop décrit la bulle du pet. `ctx.pet.say` laisse un plugin afficher une ligne courte dans la bulle de dialogue du pet principal, à la place de la manipulation directe du DOM. La ligne est attribuée au plugin, expire après une durée configurable (six secondes par défaut, plafonnée à trente), est limitée à trois lignes vivantes par plugin et à dix appels par dix secondes. Quand le pet n'est pas affiché ou est désactivé, `ctx.pet.visible` permet au plugin de se rabattre sur sa propre pastille dans la barre d'état.

> Sources : [@iamlukethedev, Hermes merged 67 PRs on October 9, 9 octobre 2026](https://x.com/iamlukethedev/status/2108698207840813506), [Spotify, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify) et [Desktop Plugin SDK, dépôt Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/developer-guide/desktop-plugin-sdk.md)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
