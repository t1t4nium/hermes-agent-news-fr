# Hermes Agent Quotidien #17

Le curator gagne un bouton annuler, Hermes tourne sur un Raspberry Pi à 2 Go RAM, Centaur accueille Hermes comme harnais de première classe, CopilotKit embarque Hermes dans n'importe quelle application, et la remise de 20 % sur le Nous Portal est prolongée de deux semaines.

## Hermes Wingtips #44 : le curator a un bouton annuler

Le 12 août, witcheer a publié le quarante-quatrième numéro de sa série Hermes Wingtips. Le sujet : les snapshots automatiques du curator et la commande de restauration.

Le curator est un processus de fond qui range les skills créées par l'agent : les compétences obsolètes sont archivées, les chevauchements sont fusionnés. witcheer rappelle que cette passe automatisée prend un instantané de tout le dossier des skills avant chaque exécution. Trois commandes suffisent pour naviguer dans l'historique :

- `hermes curator rollback --list` affiche tous les instantanés disponibles.
- `hermes curator rollback` restaure le plus récent.
- Même la restauration prend un instantané au préalable, donc rien n'est jamais perdu.

> Source : [@witcheer, 12 août 2026](https://x.com/witcheer/status/2087482141118435477)

## Hermes Agent tourne sur un Raspberry Pi 4 avec 2 Go de RAM

Le 12 août, witcheer a relayé une réalisation de la communauté : un utilisateur a fait tourner Hermes Agent sur un Raspberry Pi 4, le mini-ordinateur de la taille d'une carte de crédit à environ 50 $.

La clé du fonctionnement : Hermes Agent sépare le travail. L'agent lui-même tourne sur le Pi (boucle agent, mémoire et outils), tandis que le modèle est sollicité à distance via API. Le Pi ne fait jamais tourner le modèle localement, toute la charge lourde est déléguée à un serveur externe.

Le résultat est un agent allumé en permanence, sans coût de VPS, sur un matériel à très faible consommation électrique. witcheer souligne que le Pi 4 utilise 2 Go de RAM, soit moins que la plupart des téléphones actuels.

> Source : [@witcheer, 12 août 2026](https://x.com/witcheer/status/2087509716746326124)

## Centaur intègre Hermes Agent comme harnais de première classe

Le 11 août, Georgios Konstantopoulos (gakonst) a annoncé que la pull request de Teknium intégrant Hermes Agent dans Centaur a été fusionnée. Centaur est la plateforme de Paradigm pour déployer des agents de codage dans des sandboxes sécurisées, déjà compatible avec Codex, Claude Code, Amp et Nanocodex.

L'intégration préserve les spécificités d'Hermes :

- Continuité de session : une passerelle persistante par sandbox maintient la session Hermes d'un tour à l'autre, même après un redémarrage du sandbox.
- Boucle d'apprentissage : les revues de mémoire et de compétences après chaque tour persistent dans `HERMES_HOME` et se cumulent entre les sandboxes si un volume est monté.
- Cron jobs : un processus de fond exécute `hermes cron tick` pour que les tâches planifiées en conversation continuent de fonctionner tant que le sandbox est vivant.

L'activation se fait par le drapeau `--hermes` dans Slack, par `harness: hermes` dans la configuration des canaux, ou par la variable d'environnement `CENTAUR_DEFAULT_HARNESS=hermes`. La PR a été validée par des tests unitaires (10/10), un test de continuité de session sur deux tours, et la suite de tests Slack (45/45). witcheer a relayé le 12 août en soulignant que l'agent reste déployé sur sa propre infrastructure.

> Sources : [@gakonst, 11 août 2026](https://x.com/gakonst/status/2087301140849569851) - [@witcheer, 12 août 2026](https://x.com/witcheer/status/2087420375214792957) - [PR #1333 paradigmxyz/centaur](https://github.com/paradigmxyz/centaur/pull/1333)

## CopilotKit : intégrez Hermes dans n'importe quelle application via AG-UI

Le 10 août, CopilotKit a annoncé l'intégration d'Hermes Agent dans n'importe quelle application via le protocole AG-UI. L'agent peut être embarqué dans des applications React, React Native, Next.js, Angular, Slack et Microsoft Teams.

La vidéo de démonstration montre l'agent Hermes interagissant avec l'interface utilisateur de l'application hôte, avec des capacités de génération d'UI en temps réel et un contrôle humain dans la boucle. Nous Research a relayé l'annonce.

> Sources : [@CopilotKit, 10 août 2026](https://x.com/CopilotKit/status/2086846776116686973) - [@NousResearch, 11 août 2026](https://x.com/NousResearch/status/2087128736210813258)

## Nous Portal : 20 % de remise sur tous les modèles, prolongée de deux semaines

Le 11 août, Nous Research a annoncé la prolongation de la remise de 20 % sur tous les modèles du Nous Portal pour deux semaines supplémentaires. La remise s'applique à l'ensemble du catalogue, y compris les modèles frontières les plus coûteux, à l'exception de ceux déjà plus fortement discountés ou gratuits.

Teknium a commenté que Tommy Tibo (yeahfortommy) était à l'origine de cette prolongation. Les autres promotions en cours incluent les modèles gratuits (Solar Pro 4 pour une semaine, Hy3, Step 3.7 Flash, Laguna S et XS), la remise de 90 % sur DeepSeek V4 Flash pour encore deux jours environ, et 50 % sur GPT-5.6 Terra et Luna.

> Sources : [@NousResearch, 11 août 2026](https://x.com/NousResearch/status/2087250500110450863) - [@NousResearch, 11 août 2026](https://x.com/NousResearch/status/2087250998423085065) - [@Teknium, 11 août 2026](https://x.com/Teknium/status/2087253636477080038)

## Sources

- [@witcheer - Wingtips #44, 12 août 2026](https://x.com/witcheer/status/2087482141118435477)
- [@witcheer - Hermes sur Raspberry Pi, 12 août 2026](https://x.com/witcheer/status/2087509716746326124)
- [@gakonst - Centaur + Hermes, 11 août 2026](https://x.com/gakonst/status/2087301140849569851)
- [@witcheer - Relai Centaur, 12 août 2026](https://x.com/witcheer/status/2087420375214792957)
- [@CopilotKit - Hermes in ANY app, 10 août 2026](https://x.com/CopilotKit/status/2086846776116686973)
- [@NousResearch - Relai CopilotKit, 11 août 2026](https://x.com/NousResearch/status/2087128736210813258)
- [@NousResearch - 20 % off 2 weeks, 11 août 2026](https://x.com/NousResearch/status/2087250500110450863)
- [@NousResearch - Promotions récapitulatives, 11 août 2026](https://x.com/NousResearch/status/2087250998423085065)
- [@Teknium - Remerciements Tommy, 11 août 2026](https://x.com/Teknium/status/2087253636477080038)
- [PR #1333 - paradigmxyz/centaur](https://github.com/paradigmxyz/centaur/pull/1333)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)