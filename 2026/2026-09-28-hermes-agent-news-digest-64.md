# Hermes Agent Quotidien #64

Cette édition revient sur l'arrivée prochaine de Hermes Desktop dans le navigateur avec la commande `hermes webapp`, sur la commande `hermes send` présentée dans les Wingtips, sur Herald Family qui permet de partager un seul bot avec ses proches, sur les 200 pull requests fusionnées le 27 septembre, et sur la plateforme de sécurité NVIDIA qui accueille les agents Hermes dans ses sandboxes.

## Hermes Desktop dans le navigateur avec hermes webapp

Bear a présenté le 27 septembre sa pull request mise à jour : `hermes webapp` sert la véritable application Desktop depuis l'hôte Hermes, avec la discussion, les fichiers, Git, un terminal qui survit à un rafraîchissement et la connexion pour les liaisons distantes. Teknium a répondu le 28 septembre « Coming soon to all! », et Luke The Dev a confirmé le même jour que l'arrivée dans le navigateur est officielle.

La pull request 93508, signée BearHuddleston, ajoute `hermes webapp`, un mode hébergé dans le navigateur et authentifié pour le vrai moteur de rendu de Hermes Desktop. Ce n'est pas le tableau de bord web : il sert l'espace de travail Desktop centré sur la discussion et installe une implémentation navigateur de `window.hermesDesktop` adossée à l'hôte qui fait tourner Hermes. Les frontières d'autorité existantes sont conservées, sans cloner l'interface ni ajouter un backend parallèle. Le rendu est compilé séparément vers `apps/desktop/dist-webapp`, et l'authentification FastAPI par jeton de session ainsi que le ticket WebSocket à usage unique gardent la surface. Les capacités natives d'Electron sont absentes ou échouent explicitement plutôt que d'être imitées, et les liaisons non locales restent fermées par défaut derrière l'authentification configurée.

> Sources : [@BearHuddleston, Hermes Desktop, in any browser, 27 septembre 2026](https://x.com/BearHuddleston/status/2104109388780744775), [@Teknium, Coming soon to all!, 28 septembre 2026](https://x.com/Teknium/status/2104522071757967852), [@iamlukethedev, Hermes Desktop in a browser is officially coming soon!, 28 septembre 2026](https://x.com/iamlukethedev/status/2104523305181171748) et [feat(webapp): serve Desktop renderer in browsers, BearHuddleston, PR #93508](https://github.com/NousResearch/hermes-agent/pull/93508)

## Wingtips #86 : hermes send

witcheer a consacré le quatre-vingt-sixième numéro des Wingtips à `hermes send`, une commande qui envoie un message depuis n'importe quel script vers les plateformes sur lesquelles Hermes Agent est déjà configuré. Elle utilise les identifiants de bot de la passerelle et ne fait aucun appel au modèle. `hermes send --to telegram "deploy finished"` envoie le message, et tout peut aussi lui être passé par un pipe.

> Source : [@witcheer, Hermes Wingtips #86: hermes send, 28 septembre 2026](https://x.com/witcheer/status/2104531742686093765)

## Herald Family : partager un seul bot avec ses proches

Luke The Dev a présenté le 28 septembre Herald Family, un outil né d'un besoin simple : partager un bot Hermes avec sa femme sans lui donner accès à toute sa configuration. On choisit un bot, on sélectionne les fonctionnalités à partager, et on invite une personne avec un code QR ou un lien à usage unique. Une seule commande démarre un petit proxy de partage sur la machine qui fait tourner Hermes. La démonstration est en vidéo.

> Source : [@iamlukethedev, I wanted to share a Hermes Bot with my wife... So I built Herald Family, 28 septembre 2026](https://x.com/iamlukethedev/status/2104550126983282710)

## 200 pull requests fusionnées le 27 septembre

iamlukethedev a fait le compte le 28 septembre : Hermes a fusionné exactement 200 pull requests le 27 septembre. Parmi les plus notables :

- L'interface n'utilise plus la zone de transit pour les dépôts de fichiers du système local et conserve les références @ de fichiers en ligne.
- Le kanban indique pourquoi une tâche est bloquée et permet de la débloquer.
- Cmd/Ctrl 1 à 9 basculent vers l'onglet situé sous le pointeur.

> Source : [@iamlukethedev, Hermes merged 200 PRs on September 27, 28 septembre 2026](https://x.com/iamlukethedev/status/2104384576890212482)

## La plateforme NVIDIA Open Agent Safety et les agents Hermes

Jensen Huang a annoncé le 28 septembre la plateforme NVIDIA Open Agent Safety, présentée avec plus de cent partenaires industriels. Elle réunit OpenShell et Sentry. OpenShell applique les principes d'isolation d'un navigateur web au déroulement d'un agent : chaque session est mise en sandbox, chaque ressource est mesurée et chaque permission est vérifiée par l'exécution avant d'agir. Sentry est une conception de référence de surveillance hors bande qui tourne sur les DPU BlueField-4 et peut mettre en quarantaine un agent qui tente de sortir des limites définies, en quelques millisecondes.

Le lien avec l'écosystème Hermes passe par NemoClaw, la pile de référence open source de NVIDIA pour faire tourner des agents dans les sandboxes OpenShell. Elle propose notamment d'exécuter des agents Hermes en combinant la boucle compétences et mémoire de Nous Research avec les contrôles d'exécution d'OpenShell, pour des agents toujours actifs qui apprennent de leur expérience et réutilisent les flux de travail qui fonctionnent. Le lanceur `nemohermes onboard` sélectionne Hermes par défaut, et la couche d'intégration écrit la configuration d'exécution sous `/sandbox/.hermes`.

> Sources : [@JensenHuang, NVIDIA Open Agent Safety Platform, 28 septembre 2026](https://x.com/JensenHuang/status/2104499465055023424), [Building More Secure Agent Systems in the Open, NVIDIA Developer Forums, 28 septembre 2026](https://forums.developer.nvidia.com/t/building-more-secure-agent-systems-in-the-open/379140) et [NVIDIA NemoClaw, Deploy Safer AI Agents in a Single Command](https://www.nvidia.com/en-us/ai/nemoclaw/)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
