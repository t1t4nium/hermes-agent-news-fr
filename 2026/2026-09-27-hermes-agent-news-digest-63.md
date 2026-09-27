# Hermes Agent Quotidien #63

Cette édition revient sur le mode simple de Hermes Desktop, sur la commande `hermes pause` présentée dans les Wingtips, sur un tutoriel Twilio qui donne à un agent son propre numéro de téléphone par SMS, sur le premier événement Hermes officiel en Malaisie, sur le mode terminal natif `hermes --native`, et sur le tour d'horizon des 161 pull requests fusionnées le 26 septembre.

## Le mode simple de Hermes Desktop

witcheer a annoncé le 27 septembre l'arrivée d'un mode simple dans Hermes Desktop : la discussion uniquement, les panneaux techniques se replient. Trois façons de l'activer : par Cmd+K (Ctrl+K sous Windows et Linux) puis en tapant « simple », par Réglages → Apparence → Fenêtre et disposition → Mode d'interface, ou par Cmd+Shift+\ (Ctrl+Shift+\) pour ouvrir l'éditeur de disposition et choisir Simple.

> Source : [@witcheer, Simple mode in Hermes Desktop: chat only, the technical panes fold away, 27 septembre 2026](https://x.com/witcheer/status/2104254609661309025)

## Wingtips #85 : hermes pause et hermes resume

witcheer a consacré le quatre-vingt-cinquième numéro des Wingtips à `hermes pause`, une commande qui empêche Hermes Agent de démarrer de nouveaux travaux. Tant qu'elle est active, aucune tâche cron ne se déclenche, aucune tâche du kanban n'est envoyée et les bots de la passerelle ne démarrent aucun nouveau tour. `hermes resume` lève la pause. Elle sert notamment quand une tâche planifiée fait quelque chose que l'on préfère ne pas laisser tourner.

> Source : [@witcheer, Hermes Wingtips #85: hermes pause, 27 septembre 2026](https://x.com/witcheer/status/2104227606614757460)

## Un tutoriel Twilio pour joindre son agent par SMS

witcheer a relayé le 27 septembre un tutoriel du blog développeur Twilio qui donne à un agent Hermes son propre numéro de téléphone, par SMS. L'article, signé Amanda Lange le 21 septembre, détaille la marche à suivre : Hermes Agent installé sur un Mac Mini dédié, un modèle gratuit choisi via un compte Nous Research, puis les identifiants Twilio (AccountSID et Auth Token) et un numéro capable d'envoyer des SMS collés dans le tableau de bord.

L'autrice a demandé directement à l'agent de configurer un webhook, qu'il a mis en place seul, avant de créer un tunnel ngrok ; Hermes renvoyait même vers sa propre documentation SMS. Une fois le numéro configuré, un message envoyé au numéro Twilio revient depuis l'agent. Au matin, l'agent lui a adressé un SMS autonome pour signaler qu'il arrivait à court de jetons gratuits.

> Sources : [@witcheer, Twilio's developer blog has a Hermes Agent tutorial: your agent on its own phone number, over SMS, 27 septembre 2026](https://x.com/witcheer/status/2104206409881526365) et [Sending SMS with an Agentic AI using Twilio and Hermes Agent, Amanda Lange, 21 septembre 2026](https://www.twilio.com/en-us/blog/developers/tutorials/integrations/sending-sms-agentic-ai-using-twilio-hermes-agent)

## Le premier événement Hermes officiel en Malaisie

masterofnone a annoncé le 27 septembre le premier événement Hermes officiel en Malaisie, organisé par KrackedDevs avec Nous Research. Après des mois d'ateliers non officiels, deux journées complètes sont prévues les 3 et 17 octobre à la AI Builder School de KL Eco City. witcheer a salué l'annonce le même jour, en remerciant Danial et l'équipe Kracked Devs.

> Sources : [@masterofnone, The first official Hermes event in Malaysia, 27 septembre 2026](https://x.com/masterofnone/status/2104115270306680834) et [@witcheer, Malaysia, so happy to support this one, 27 septembre 2026](https://x.com/witcheer/status/2104162982569910507)

## Le mode terminal natif hermes --native

tonbistudio a présenté le 27 septembre le nouveau mode terminal natif de Hermes Agent, lancé par `hermes --native`. Il affiche l'interface dans le terminal lui-même plutôt que sur un écran alternatif : pas d'écran d'ouverture, et le terminal conserve le défilement après la sortie de l'interface. La différence est montrée en vidéo.

> Source : [@tonbistudio, Have you tried the new native terminal mode for Hermes Agent? hermes --native, 27 septembre 2026](https://x.com/tonbistudio/status/2104079178845032667)

## 161 pull requests fusionnées le 26 septembre

iamlukethedev a fait le compte le 27 septembre : 161 pull requests ont été fusionnées dans Hermes Agent le 26 septembre, réparties entre l'interface (26), la voix et le temps réel (1), les outils et plugins pour développeurs (79), la sécurité et les secrets (8), les intégrations et la discussion (14) et la stabilité (33). Parmi les plus notables :

- L'interface affiche enfin les tâches cron scriptées et leur historique d'exécution.
- Claude Opus 5.5 arrive dans les sélecteurs Anthropic et Bedrock, avec un contexte d'un million de jetons sur Bedrock Opus 5 et 5.5.
- Les réponses en streaming cessent de répéter un mot quand l'aperçu bascule vers un nouveau message.
- Une vraie clé OPENAI_API_KEY n'est jamais routée ni envoyée vers OpenRouter.
- Côté voix, le streaming TTS de xAI fonctionne, les clés Gemini ne traînent plus dans les URL et les fins de raisonnement ne sont plus prononcées.
- Les tâches cron continuent de se déclencher malgré des entrées corrompues dans jobs.json ou des compteurs de répétition infinis ou négatifs.
- Ctrl+C affiche la même réponse partielle que celle sauvegardée par la session, dans l'interface comme dans le bureau.
- L'interface ajoute un réglage File Browser dans Apparence, et les habillages CSS personnalisés survivent aux mises à jour.
- Le portail Cloud conserve la connexion en cas d'interruption de redirection, et macOS fait confiance aux autorités de certification du trousseau pour les passerelles distantes.

iamlukethedev avait détaillé la veille le cas des tâches cron scriptées : elles tournaient bel et bien, mais l'interface ne savait pas les afficher, d'où une description vide, l'absence de badge Script et un « aucune exécution » trompeur.

> Sources : [@iamlukethedev, Hermes merged 161 PRs on September 26, 27 septembre 2026](https://x.com/iamlukethedev/status/2104020319598149996) et [@iamlukethedev, Your Hermes cron job wasn't broken. Desktop just couldn't see it, 26 septembre 2026](https://x.com/iamlukethedev/status/2103993691816018264)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
