# Hermes Agent Quotidien #14

Le mode HUD transforme le bureau en calque actif, le geste "this" remplace les descriptions d'application, une commande suggère une liste blanche des approbations récurrentes, l'abonnement unifie tous les outils sous un seul login, et Teknium promet une application mobile officielle.

## Le mode HUD : Hermes devient un calque sur votre bureau

Le 8 août, Brooklyn! (@imbabybrooklyn) a présenté le mode HUD dans Hermes Desktop. Au lieu d'une fenêtre qu'on doit atteindre en alt-tab, Hermes devient une couche semi-transparente flottant au-dessus des autres applications. On le déplace n'importe où sur l'écran, il se fond dans le décor quand on ne le lit pas, et un simple `Cmd+Shift+H` le réduit à une barre de composition avec la dernière réponse au-dessus.

Witcheer a précisé que la HUD se rabat automatiquement quand on arrête de la lire.

Teknium a ajouté le 9 août que le CLI affiche désormais le nom de la session dans la barre de contexte, à droite.

> Sources : [@imbabybrooklyn, 8 août 2026](https://x.com/imbabybrooklyn/status/2086130893811277833) - [@witcheer, 8 août 2026](https://x.com/witcheer/status/2086168393434984481) - [@Teknium, 9 août 2026](https://x.com/Teknium/status/2086365383637025119)

## Pointer du doigt : posez la barre et dites "this"

Le 9 août, Brooklyn! a montré l'étape suivante du mode HUD. Plus besoin de décrire à Hermes sur quelle application vous travaillez. On place la barre HUD par-dessus la fenêtre concernée, on dit "this", et Hermes comprend immédiatement le contexte : il voit l'application sous la barre, peut lire son contenu, analyser ce qui s'affiche.

> "You don't tell Hermes which app you mean anymore. Put the bar over it and say 'this'."

La fonction est disponible dès la mise à jour du desktop, sur Mac comme sur Windows. Brooklyn! a confirmé que la passerelle distante ne peut pas transmettre le geste ("it would require a wormhole").

Nous Research a relayé la démonstration avec un simple emoji d'étonnement.

> Sources : [@imbabybrooklyn, 9 août 2026](https://x.com/imbabybrooklyn/status/2086270328926240782) - [@NousResearch, 9 août 2026](https://x.com/NousResearch/status/2086270481305424201)

## Hermes Wingtips #41 : `hermes approvals suggest`

Witcheer a présenté le 9 août une nouvelle commande du CLI. `hermes approvals suggest` parcourt l'historique des approbations et propose une liste blanche des commandes récurrentes. Si vous approuvez la même action pour la troisième fois de la semaine, la commande vous évite de la réapprouver à chaque fois.

La commande ne fait que proposer : rien n'est écrit sans validation explicite. Witcheer a illustré avec un vrai résultat de son propre agent.

> Source : [@witcheer, 9 août 2026](https://x.com/witcheer/status/2086460177046286778)

## Un abonnement, un login pour tous les outils

Witcheer a rappelé le 9 août que l'abonnement Nous couvre bien plus que les modèles. Un seul login donne accès à la recherche web, à la génération d'images, à la synthèse vocale et à l'automatisation navigateur, le tout acheminé par la passerelle d'outils Nous (Nous Tool Gateway). L'agent n'a donc plus besoin d'un compte et d'une clé API distincts pour chaque outil.

> "Your agent stops needing a separate account and key for every tool."

> Source : [@witcheer, 9 août 2026](https://x.com/witcheer/status/2086473034148266167)

## Un plugin Shodan pour Hermes Agent

@adolandev a publié le 7 août un plugin Shodan pour Hermes Agent. Il permet de faire de la reconnaissance sur des hôtes (renseignement d'adresse IP, comptage à l'échelle d'Internet) sans clé API, en s'appuyant sur InternetDB. L'installation se fait en une commande, sans modification du noyau d'Hermes, grâce à l'API plugin.

Le dépôt est sur github.com/Adolanium/hermes-plugin-shodan. Teknium a relayé la publication.

> Source : [@adolandev, 7 août 2026](https://x.com/adolandev/status/2085655993371767172)

## Hermes Browser Extension : un studio de thèmes

@jonkomet a publié le 8 août un studio de thèmes pour l'extension navigateur Hermes. On peut importer n'importe quel thème VS Code dans le navigateur, ou demander à Hermes d'en générer un. L'extension prend ainsi l'apparence qu'on souhaite, en harmonie avec le reste de l'environnement de travail.

Un utilisateur a salué l'import de thèmes VS Code existants comme l'alternative sensée à un nouveau panneau de réglages.

Teknium a relayé l'annonce.

> Source : [@jonkomet, 8 août 2026](https://x.com/jonkomet/status/2086165169605165488)

## Une application mobile officielle en chemin

Le 8 août, Teknium a répondu à un utilisateur qui réclame une application iOS native : il a promis qu'une application mobile officielle pour Hermes Agent arrivera. Pas tout de suite : l'équipe veut la rendre aussi aboutie que possible avant toute diffusion publique.

> "I promise an official mobile app for Hermes Agent will come. Not too soon though, we want it to be truly as perfect as we can make it without public feedback."

Interrogé sur l'intérêt d'une application dédiée quand Hermes fonctionne déjà par messagerie, Teknium a répondu : "Because 50,000 people asked for it."

> Source : [@Teknium, 8 août 2026](https://x.com/Teknium/status/2086207583417954417)

## Sources

- [@imbabybrooklyn - Mode HUD, 8 août 2026](https://x.com/imbabybrooklyn/status/2086130893811277833)
- [@witcheer - HUD qui se fond, 8 août 2026](https://x.com/witcheer/status/2086168393434984481)
- [@Teknium - CLI affiche le nom de session, 9 août 2026](https://x.com/Teknium/status/2086365383637025119)
- [@imbabybrooklyn - Geste "this", 9 août 2026](https://x.com/imbabybrooklyn/status/2086270328926240782)
- [@NousResearch - Relai du geste "this", 9 août 2026](https://x.com/NousResearch/status/2086270481305424201)
- [@witcheer - Hermes Wingtips #41 : approvals suggest, 9 août 2026](https://x.com/witcheer/status/2086460177046286778)
- [@witcheer - Un login pour tous les outils, 9 août 2026](https://x.com/witcheer/status/2086473034148266167)
- [@adolandev - Plugin Shodan, 7 août 2026](https://x.com/adolandev/status/2085655993371767172)
- [@jonkomet - Theme studio extension navigateur, 8 août 2026](https://x.com/jonkomet/status/2086165169605165488)
- [@Teknium - Application mobile promise, 8 août 2026](https://x.com/Teknium/status/2086207583417954417)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)