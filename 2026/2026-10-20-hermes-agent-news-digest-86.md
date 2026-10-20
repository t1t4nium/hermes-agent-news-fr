# Hermes Agent Quotidien #86

Cette édition revient sur les 92 pull requests fusionnées le 19 octobre, sur le plugin Meshy qui se rapproche de sa sortie, sur un conseil pour lever la limite de débit du hub de skills, sur Footprint, un plugin qui fait l'inventaire du disque, et sur Beam 1.0, un modèle open-weight offert une semaine sur Nous Portal.

## 92 pull requests fusionnées le 19 octobre

iamlukethedev a fait le compte le 19 octobre : Hermes a fusionné 92 pull requests le 19 octobre. Les changements mis en avant :

- Les plugins peuvent connecter l'utilisateur à une API tierce sans jamais détenir le jeton : le plugin déclare le fournisseur et Hermes fait la requête à sa place, donc le secret ne passe pas dans le code du plugin.
- Un appel d'outil réussi n'est plus marqué comme un échec quand le résultat contient un champ « error » nul.
- Desktop relit la réponse finale à voix haute après les appels d'outils.
- Telegram gagne une option dm_topic_auto_transfer qui ouvre un sujet neuf pour les messages privés.
- Les plugins MCP peuvent transmettre des variables d'environnement optionnelles ; une variable ${VAR} non définie n'est plus envoyée telle quelle au serveur stdio.
- Le catalogue accueille kokoro-tts, hermes-wsl-terminal, runbox, post-cortex, proofable, anyapi, agent-station et git-tasks.

> Sources : [@iamlukethedev, Hermes merged 92 PRs on October 19, 19 octobre 2026](https://x.com/iamlukethedev/status/2112323816676528261) et [Hermes Bible, changelog du 19 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-19)

## Meshy, le plugin de modélisation 3D presque prêt

Teknium a montré le 20 octobre l'avancement du plugin Meshy pour Hermes Agent. Il comprend le MCP et une skill, et s'intègre à l'application de bureau pour afficher les modèles rendus dans la conversation, montrer les crédits dans la barre d'état et garder une galerie des modèles créés. Il a ajouté la veille la possibilité de choisir le type de fichier à télécharger depuis Meshy, directement dans le chat. La sortie était annoncée pour le lendemain.

> Sources : [@Teknium, Meshy plugin for Hermes Agent going well, 20 octobre 2026](https://x.com/Teknium/status/2112456282062065690) et [@Teknium, Added the ability to select the model file type to download from Meshy, 20 octobre 2026](https://x.com/Teknium/status/2112461624078664121)

## Hermes Wingtips #107, lever la limite du hub de skills

witcheer a publié le 20 octobre le conseil Hermes Wingtips #107. Le hub de skills lit les dépôts via l'API GitHub, qui plafonne à 60 requêtes par heure et par adresse réseau sans jeton. Poser un jeton GitHub dans le fichier .env, avec la commande `hermes config set` ou directement dans le fichier, place l'agent sur son propre budget de 5 000 requêtes par heure.

> Sources : [@witcheer, Hermes Wingtips #107: skill installs on a shared connection, 20 octobre 2026](https://x.com/witcheer/status/2112446219070968105)

## Footprint, l'inventaire de ce que l'agent laisse sur le disque

witcheer a présenté le 20 octobre Footprint, un plugin communautaire pour Hermes Agent qui montre ce que l'agent a laissé sur le disque et ce qui peut partir. Sur son essai : ce que chaque dossier représente pour Hermes, trié par taille ; les caches qui se reconstruisent au besoin, signalés comme à examiner ; et les fichiers écrits par les bots.

> Sources : [@witcheer, new community plugin for Hermes Agent: Footprint, 20 octobre 2026](https://x.com/witcheer/status/2112514184999030869)

## Beam 1.0, gratuit sur Nous Portal pendant une semaine

witcheer a annoncé le 20 octobre Beam 1.0 de Reflection, gratuit sur Nous Portal pendant une semaine. Le modèle est open-weight, 501 milliards de paramètres au total dont 23 milliards actifs par jeton, avec un contexte de 262 000 jetons sur la version gratuite, l'appel d'outils intégré et le raisonnement réglable de bas à haut. Pour le lancer :

`hermes chat --provider nous -m reflection/beam-1.0-501b-a23b:free`

> Sources : [@witcheer, Beam 1.0 from Reflection for free on Nous Portal!, 20 octobre 2026](https://x.com/witcheer/status/2112541414147903742) et [@yeahfortommy, Beam is FREE in Nous Portal for one week, 20 octobre 2026](https://x.com/yeahfortommy/status/2112536403200323783)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
