# Hermes Agent Quotidien #60

Cette édition revient sur la release correctrice v0.21.5 publiée le 24 septembre, sur l'arrivée du Bot Screen qui diffuse en direct le bureau de chaque bot dans Hermes Desktop, sur le panneau latéral de l'extension de navigateur de Jon Komet, sur le quatre-vingt-deuxième numéro des Wingtips consacré au chien de garde des sessions figées, et sur Cua-S1-4B-0.2, le modèle de décision multimodal entraîné par Cua pour les tâches d'usage de l'ordinateur.

## Hermes Agent v0.21.5 (v2026.9.24)

Nous Research a publié le 24 septembre Hermes Agent v0.21.5, taguée v2026.9.24. C'est une release correctrice qui roule environ 460 demandes de tirage fusionnées depuis la v0.21.4 dans un tag stable destiné aux consommateurs en aval, images Docker, Hermes Cloud et déploiements hébergés. Les notes de release complètes de cette fenêtre sont reportées à la v0.22.0. Mesurée au commit f97608f, la fenêtre contient 1 610 commits hors fusions, 4 828 fichiers modifiés (+164 132 et -149 440 lignes), 460 demandes de tirage fusionnées et 475 issues fermées.

Les changements notables, volontairement non détaillés dans cette release :

- Une vague de SDK de plugins pour le bureau, avec une API de brouillon de compositeur, des emplacements de liste de sessions et de décoration de ligne, des préférences de navigation latérale, des fournisseurs d'étiquettes de modèle, des ponts typés vers les réglages, skills, jeux d'outils et profils, une primitive d'incorporation en bac à sable, un emplacement de réglage d'apparence et un pont d'événements public pour les backends de plugins.
- Le mode d'interface Simple ou Avancé pour le bureau.
- La page Connecteurs qui remplace l'onglet MCP, avec une connexion immédiate pour les serveurs MCP d'un plugin fraîchement installé et la mise en ligne des outils et skills des plugins installés dans chaque conversation ouverte.
- L'onboarding qui propose les plugins du catalogue à côté des connecteurs.
- Les catalogues du bureau complets en français, allemand et espagnol, ainsi qu'un réglage de sens de texte RTL et LTR.
- La saisie d'un modèle personnalisé depuis le compositeur et les sélecteurs de réglages.
- Des raccourcis de touches de fonction et de dictée vocale.
- L'arrêt, le démarrage et le redémarrage par profil sous le multiplexeur d'hôte, et `gateway.standalone` pour en exclure un profil.
- Le dock en direct qui affiche le `/goal` en cours et les invites en file dans le CLI et la TUI.
- Une passe de conception sur kanban, avec une fenêtre de ticket à deux colonnes et du texte de tâche en markdown.
- La mise en miroir des livraisons de webhook dans la session de discussion cible.
- Le Bot Screen sur les images hébergées `-desktop`.
- GPT-6 Sol, Terra et Luna ainsi que Claude Opus 5.5 dans les catalogues Nous et OpenRouter.
- Une intégration officielle Blender Lab et des plugins NVIDIA app et Broadcast.
- Une longue passe de performance sur le chargement de configuration, le registre d'outils, le traitement des messages de passerelle et le sélecteur de modèle.
- Des dizaines de nouveaux plugins communautaires au catalogue.

Les notes de release complètes de la fenêtre accompagneront la v0.22.0, qui documentera tout depuis la v0.21.0, avec les temps forts, les domaines de fonctionnalités et les crédits complets aux contributeurs. Rien de la fenêtre n'est écarté.

> Source : [Hermes Agent v0.21.5 (v2026.9.24), notes de release, 24 septembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.24)

## Le Bot Screen diffuse le bureau de chaque bot dans Hermes Desktop

NousResearch a annoncé le 23 septembre que l'on peut désormais regarder ses agents travailler en direct, Hermes Desktop diffusant en temps réel l'écran de n'importe quel bot ou session. On le voit piloter un navigateur, taper dans un terminal ou ouvrir une fenêtre, et l'on peut reprendre la main à tout moment pour interagir avec le Bot Screen ou saisir des identifiants, puis rendre le contrôle. Teknium a présenté la même fonction comme un passage de bureau en direct et interactif vers la même machine que son agent, pour chaque passerelle distante prise en charge. iamlukethedev a montré le geste de reprise : le Bot Screen donne à chaque bot sur une passerelle Linux son propre bureau, diffusé en direct dans Hermes Desktop, et c'est la passation qui rend la chose utile.

La documentation précise le fonctionnement. Sur un hôte de passerelle Linux sans écran, serveur, machine virtuelle cloud ou Hermes Cloud, chaque bot reçoit son propre bureau, un écran Xfce sur lequel agissent ses outils d'usage de l'ordinateur et son navigateur dirigé, diffusé en direct dans Hermes Desktop. On observe ce que fait le bot, on reprend la main face à une connexion, une double authentification, un CAPTCHA ou un paiement, puis on rend le contrôle et il poursuit avec la session fraîchement ouverte. Le bot continue à travailler une fois l'application fermée ou l'ordinateur portable éteint, puisque l'écran vit sur l'hôte de passerelle et non sur la machine locale. Chaque profil possède son propre écran, son propre profil de navigateur et ses propres cookies. Les écrans ne sont pas une frontière de sécurité : les bots partagent le compte utilisateur de l'hôte, ses fichiers et son réseau. Pendant qu'un humain tient le contrôle, les outils d'usage de l'ordinateur et de navigateur du bot sont refusés avec `human_has_control`. La reprise gagne la dernière reprise : deux spectateurs sur un même écran, c'est la prise de contrôle la plus récente qui l'emporte. Le démarrage demande TigerVNC et les composants Xfce, que Hermes n'installe jamais en silence : le panneau propose une installation en un clic ou affiche la commande à lancer, et les images officielles `-desktop` embarquent les paquets.

> Sources : [@NousResearch, You can now watch your agents work live, 23 septembre 2026](https://x.com/NousResearch/status/2102873234819698877), [@Teknium, live desktop passthrough for every remote gateway, 23 septembre 2026](https://x.com/Teknium/status/2102875926317142488), [@iamlukethedev, Hermes can now share its screen and let you take the mouse, 23 septembre 2026](https://x.com/iamlukethedev/status/2102880682100068521) et [Bot Screen, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/bot-screen)

## Le panneau latéral de Jon Komet met Hermes dans le navigateur

witcheer a relayé le 24 septembre le travail de Jon Komet, qui a construit un panneau latéral plaçant son propre Hermes Agent dans Chrome, Edge ou n'importe quel navigateur Chromium. L'utilisateur garde le contrôle du navigateur, Hermes voit l'onglet qu'il choisit, et sur une passerelle locale ou auto-hébergée, l'extension fonctionne avec les modèles, outils, skills, mémoire et serveurs MCP de son installation.

Le dépôt confirme la portée. Hermes Browser Extension est une extension communautaire de Jon Komet, publiée sous licence MIT, qui relie le contexte web au runtime Hermes local via une passerelle locale, l'onglet d'agent Hermes Cloud ou une passerelle distante auto-hébergée. Elle vise à vivre en bordure de l'écosystème sans ajouter d'empreinte de schéma d'outil au noyau. Côté navigateurs, le panneau latéral Chrome, Edge, Brave, Comet ou tout Chromium avec l'API Side Panel est la cible publique principale, et Firefox 142 ou plus récent est pris en charge via le listing Mozilla Add-ons. Le dépôt affiche 1,6 k étoiles et 150 forks.

> Sources : [@witcheer, Jon Komet built a side panel that puts your own Hermes Agent inside Chrome, 24 septembre 2026](https://x.com/witcheer/status/2103116743556149700) et [abundantbeing/hermes-browser-extension, dépôt GitHub, 24 septembre 2026](https://github.com/abundantbeing/hermes-browser-extension)

## Wingtips #82 : agent.session_stall_timeout

witcheer a consacré le quatre-vingt-deuxième numéro des Wingtips à `agent.session_stall_timeout`. Si un bot Hermes a déjà envoyé le message « Agent session appears stalled », c'est un chien de garde, et il n'interrompt jamais le tour. Il s'exprime une seule fois quand on a envoyé une relance et que l'agent n'a montré aucune activité pendant cinq minutes.

La documentation de configuration détaille le réglage. La passerelle exécute un chien de garde d'arrêt uniquement notifiant, `agent.session_stall_timeout`, à 300 secondes par défaut, la valeur 0 le désactivant. Le message complet est « Agent session appears stalled (last activity N min ago). Try /new to reset. »

> Sources : [@witcheer, Hermes Wingtips #82: agent[.]session_stall_timeout, 24 septembre 2026](https://x.com/witcheer/status/2102997146660110386) et [Hermes Agent Configuration, Session Stall Watchdog, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#session-stall-watchdog)

## Cua-S1-4B-0.2, un modèle de décision pour l'usage de l'ordinateur

Cua a présenté le 23 septembre Cua-S1-4B-0.2, le premier modèle de décision multimodal entraîné avec RLOO sur des tâches d'usage de l'ordinateur en direct, en s'appuyant sur des récompenses d'achèvement de tâche. Les adaptateurs texte et multimodal sont publiés sous licence Apache-2.0. witcheer a relevé le même jour que l'équipe derrière le pilote d'usage de l'ordinateur dans Hermes Agent livre désormais aussi le côté modèle.

La fiche Hugging Face précise la nature du modèle. Cua-S1-4B-0.2 consiste en des adaptateurs LoRA sur la base gelée Qwen3.5-4B, destinés aux décisions d'élément et d'action à options fermées pour l'usage de l'ordinateur, avec des déroulés agentiques multi-étapes dans des environnements d'interface graphique en direct. Deux adaptateurs entraînés indépendamment sont proposés, texte et multimodal. Les poids des adaptateurs sont sous licence Apache-2.0, la base Qwen3.5-4B restant régie par sa propre licence et non redistribuée. Le modèle ne remplace pas cua-s1-4b-0.1, les deux sont publiés séparément. Il appartient à la famille de recherche Cua-S1, dont le code, les résultats et la méthodologie sont publiés sur le dépôt trycua/cua.

> Sources : [@trycua, Today we're introducing Cua-S1-4B-0.2, 23 septembre 2026](https://x.com/trycua/status/2102800643794591833), [@witcheer, the team behind the computer-use driver in Hermes Agent is now shipping the model side, 23 septembre 2026](https://x.com/witcheer/status/2102803912596353501), [cua-ai/cua-s1-4b-0.2, fiche Hugging Face](https://huggingface.co/cua-ai/cua-s1-4b-0.2) et [trycua/cua, dépôt GitHub](https://github.com/trycua/cua)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
