# Hermes Agent Quotidien #37

Cette édition revient sur la grande release Hermes Agent v0.21.0 « The Pantheon Release », sur le passage du cap des 100 000 pull requests et sur le flux de contribution qui l'accompagne, ainsi que sur un usage qui transforme plusieurs agents Hermes en une petite équipe qui se parle.

## Hermes Agent v0.21.0, « The Pantheon Release »

Nous Research a publié le 31 août Hermes Agent v0.21.0, une release majeure qui rassemble tout depuis v0.20.0 : environ 5 800 commits, 2 475 pull requests fusionnées, près de 2 100 issues fermées et plus de 760 contributeurs. La version reprend aussi les fenêtres des tags correctifs v0.20.1 à v0.20.6, dont les notes étaient reportées ici.

Les changements notables :
- Bot Mode intégré et activé par défaut au bureau : chaque profil devient un agent nommé avec un visage d'avatar déterministe, des chats de groupe façon Discord, la mention de n'importe quel bot, des noms et des images de salles.
- `hermes peer` permet à un agent d'écrire à un autre par identifiant, entre profils et passerelles, depuis le CLI ou une conversation, avec réponse dans le Bot Chat canonique de chaque agent.
- Les tâches cron gagnent une mémoire persistante et l'option `continuity=true` porte la sortie d'une exécution à la suivante, avec un bloc-notes durable par tâche, un mode surveillant qui contourne le modèle quand rien n'a changé et une sortie possible dans un Bot Chat.
- `delegate_task` se pilote en direct : lister les sous-agents en cours, corriger leur trajectoire, les arrêter tôt en gardant le résultat partiel, valider leurs sorties sur un schéma JSON et afficher le coût par délégation.
- Le centre de commande MCP réunit serveurs et catalogue dans une même page, avec import par glisser-déposer, vérifications de santé en arrière-plan, vue de coût et d'usage sur trente jours et liens `hermes://` soumis à confirmation.
- Le CLI reçoit une palette de commandes floue (Ctrl+P), un sélecteur `/model` qui filtre pendant la frappe, un `/status` enrichi, des métriques en direct dans la barre d'état et un arrêt d'urgence global.
- L'agent pilote le navigateur intégré du bureau, et peut sortir les pages vers le navigateur système.
- Six fournisseurs arrivent (Meta Model API Muse Spark en intégré, CommandCode, Tencent TokenPlan, Nebius Token Factory, Ramp Router, Actual Computer) ; le catalogue accueille GLM-5.3-Flash, qwen3.8-max/flash, Gemini 3.7 Flash, MiniMax M3 et Nemotron 3.5 Lightning, et `model_overrides` permet de corriger soi-même fenêtre de contexte et prix d'un modèle.
- La sécurité est renforcée : écriture des fichiers d'instructions protégés soumise à approbation, passe de masquage des secrets (erreurs terminal, lectures de `.env`, points de contrôle, journaux ACP), commandes destructrices de Windows reconnues et permissions macOS stables aux mises à jour.

Deux nouveautés ont été annulées avant livraison : le mode Model Council (`/council`) et le moteur de contexte DCP, fusionnés puis retirés, ne font pas partie de cette release.

> Sources : [@NousResearch, Hermes Agent v0.21.0 : The Pantheon Release, 31 août 2026](https://x.com/NousResearch/status/2094515104670715940) et [Hermes Agent v0.21.0, notes de release, 31 août 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.31)

## 100 000 pull requests et l'intégration par récupération

Teknium a annoncé que Hermes Agent a franchi la barre des 100 000 pull requests venues des contributeurs et de l'équipe. Il a en parallèle clarifié le flux de contribution qui rend ce rythme tenable : les contributeurs n'ont pas à rebaser ni à garder leurs pull requests sans conflit, car l'équipe récupère le travail vers main quand elle est prête, garder une pull request à jour étant un effort impossible tant main évolue vite. C'est ce que reflètent les notes de release, où une partie des changements sont marqués comme récupérés d'issues ou de pull requests de la communauté.

> Sources : [@Teknium, We just crossed our 100,000th PR, 1er septembre 2026](https://x.com/Teknium/status/2094701489059197383) et [@Teknium, nous récupérerons votre PR vers main, 1er septembre 2026](https://x.com/Teknium/status/2094785645399171385)

## Plusieurs agents Hermes en petite équipe

witcheer décrit son installation comme une petite équipe : un agent réfléchit et rédige avec lui sur Discord, un autre exécute les tâches planifiées sur un Mac Mini, un troisième teste les modèles sur une machine GPU, et ils s'écrivent entre eux quand ils en ont besoin. Il souligne que depuis v0.21.0 ce schéma, l'échange direct d'agent à agent et le Bot Mode, est intégré nativement à l'application de bureau.

> Source : [@witcheer, my Hermes Agent setup is a small team, 1er septembre 2026](https://x.com/witcheer/status/2094733012751524191)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
