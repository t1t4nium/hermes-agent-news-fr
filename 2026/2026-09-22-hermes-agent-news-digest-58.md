# Hermes Agent Quotidien #58

Cette édition revient sur la release correctrice v0.21.4, qui met fin à une semaine sans nouvelle version, sur le retour de Claude Code dans Hermes Agent par un plugin officiel Direct SDK, sur le quatre-vingtième numéro des Wingtips consacré à l'épinglage des skills, sur l'arrivée de Grok 4.7 à moitié prix sur le portail Nous et sur la sortie des modèles omnimodaux Xiaomi MiMo-V2.6.

## Hermes Agent v0.21.4 (v2026.9.21)

Nous Research a publié le 21 septembre Hermes Agent v0.21.4, taguée v2026.9.21. C'est une release correctrice qui roule environ 1 800 demandes de tirage fusionnées depuis la v0.21.3 dans un tag stable destiné aux consommateurs en aval, images Docker, Hermes Cloud et déploiements hébergés. Les notes de release complètes de cette fenêtre sont reportées à la v0.22.0. Mesurée au commit 4b8a813, la fenêtre contient 5 071 commits hors fusions, 5 169 fichiers modifiés, 1 812 demandes de tirage fusionnées et 2 116 issues fermées.

Les changements notables :

- Un verrou de singleton de passerelle à l'échelle de l'hôte avec enregistrement de rendez-vous, et l'application de bureau qui s'attache au backend hôte déjà actif au lieu d'en lancer un second.
- Une opération de connecteur possédée par le backend, avec une carte de configuration sur le bureau, la TUI et le CLI.
- La sortie structurée `--format stream-json` en JSONL pour le CLI.
- `skills.auto_load` épingle des skills dans l'invite de chaque nouvelle session.
- Un sélecteur de police pour le chat et l'interface du bureau, des mises à jour locales du moteur en un clic, et la désinstallation de plugins depuis le hub des plugins.
- Un comportement `decline` pour les messages privés non autorisés sur la passerelle.
- Une limite de connexion configurable pour la découverte MCP (`mcp.discovery_concurrency`).
- Des bornes avant et après pour `session_search`, avec une relance de rappel relâchée par OU.
- La commande `hermes sessions set-journal-mode`.
- LTX 2.5 et Kling O3 dans les catalogues vidéo.
- Une page web pour chaque plugin et auteur du catalogue, avec readmes épinglés sur commit et tri par ajout ou mise à jour.
- Une douzaine de nouveaux plugins communautaires au catalogue : tailscale, ssh, shodan, terminal, rss, resetwatch, done-bell, kiwi, cognee, Octen.
- Une large passe de corrections sur l'isolation des profils et du multiplexage, cron, kanban, le bureau et state.db.

Les notes de release complètes de la fenêtre accompagneront la v0.22.0, qui documentera tout depuis la v0.21.0, avec les temps forts, les domaines de fonctionnalités et les crédits complets aux contributeurs. Rien de la fenêtre n'est écarté.

> Source : [Hermes Agent v0.21.4 (v2026.9.21), notes de release, 21 septembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.21)

## Le retour de Claude Code par le plugin Direct SDK

Teknium a annoncé le 21 septembre le retour de Claude dans Hermes Agent grâce à un nouveau plugin officiel qui utilise le SDK Claude sans les compromis, pour permettre aux abonnements Claude Code de fonctionner à nouveau dans Hermes Agent. tonbistudio a publié le même jour une vidéo qui montre l'installation du plugin Direct SDK et la prise en main de Fable 5.1.

La page du catalogue décrit le plugin `claude-subscription-directsdk`, affiché Claude Subscription DirectSDK (Experimental), maintenu par NousResearch. Il pilote l'exécutable officiel Claude Code, non modifié, comme client de modèle limité à la requête, sur un abonnement Claude Pro ou Max. Hermes garde sa boucle d'agent, ses outils, ses approbations et sa compaction. Malgré son nom, l'implémentation parle nativement en stream-json et n'exige pas le paquet Python de l'Agent SDK. Il faut Hermes Agent 0.21.4 ou plus récent, Python 3.10 ou plus, et le CLI Claude Code officiel installé et connecté. Le plugin ne détient aucun identifiant, tout passe par `claude`. L'installation tient en quelques commandes : `hermes plugins install claude-subscription-directsdk`, puis `claude auth login` et le choix du fournisseur.

La qualification en cours vient de la demande de tirage #105863 de @teknium1 et @unsupportedpastels, dont les parties génériques, profils de fournisseur à processus externe, transporteurs de rejeu natifs, contrôle du flux de configuration et plomberie du sélecteur, atterrissent dans le noyau via la PR #117451. Le plugin est marqué expérimental : il s'agit d'une construction de revue, pas d'une revendication de parité ni de maturité en production.

> Sources : [@Teknium, Welcome back to Hermes Agent, Claude, 21 septembre 2026](https://x.com/Teknium/status/2102093483788107792), [@tonbistudio, Huge news for Claude subscribers!, 21 septembre 2026](https://x.com/tonbistudio/status/2102112767654441132) et [Claude Subscription DirectSDK (Experimental), catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/claude-subscription-directsdk)

## Wingtips #80 : skills.auto_load

witcheer a consacré le quatre-vingtième numéro des Wingtips à `skills.auto_load`. Hermes Agent charge une skill quand une tâche l'exige, mais certaines skills sont utiles à chaque session quelle que soit la tâche : un style maison, une liste de contrôle de relecture, la façon d'écrire les commits. La clé les épingle, chaque nom de la liste étant chargé dans chaque nouvelle session.

La documentation du CLI détaille le mécanisme. Pour avoir les mêmes skills actives au début de chaque session, sur toutes les surfaces, CLI, TUI, passerelle, cron et API, on les liste sous `skills.auto_load` dans config.yaml. La liste est résolue une fois, à la première construction de l'invite système de la session, et les octets rendus sont réutilisés pour toute la conversation, y compris aux changements de modèle et à la compaction, si bien que le cache d'invite reste intact ; les modifications de configuration prennent effet à la session suivante. Une skill absente ou désactivée journalise un avertissement et est ignorée, et `--ignore-rules` (ou `HERMES_IGNORE_RULES=1`) supprime le chargement automatique avec AGENTS.md, SOUL.md, .cursorrules et l'injection mémoire, les skills explicites `-s` restant chargées. Le réglage est propre au profil.

> Sources : [@witcheer, Hermes Wingtips #80: skills.auto_load, 22 septembre 2026](https://x.com/witcheer/status/2102275176138178793) et [CLI Interface, Preloading Skills at Launch, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/cli#preloading-skills-at-launch)

## Grok 4.7 à moitié prix sur le portail Nous

SpaceXAI a annoncé le 21 septembre Grok 4.7, présenté comme une amélioration notable sur Grok 4.6 à prix et vitesse identiques. NousResearch a relayé le même jour que Grok 4.7 est à moitié prix pendant une semaine dans Hermes Agent via le portail Nous.

witcheer a précisé le geste : Grok 4.7 est sur le portail Nous à 50 % pendant une semaine, et pour un agent qui tourne sur un compte Portal, le changement tient en une ligne dans n'importe quelle conversation, `/model`, choisir Grok 4.7, continuer. Il a rappelé plus tard dans la journée qu'une bonne partie des modèles frontières sont actuellement à la moitié de leur prix catalogue sur le portail, Grok 4.7, GPT-5.6 Sol et Sol Pro, Gemini 3.8 Flash et 3.7 Flash, Kimi K3, et qu'un lot de modèles sont gratuits, Ling 3.0 Flash, LongCat 2.0, Laguna S et XS, Step 3.7 Flash, Solar.

> Sources : [@SpaceXAI, Grok 4.7 is here, 21 septembre 2026](https://x.com/SpaceXAI/status/2102069815225586149), [@NousResearch, Grok 4.7 by @SpaceXAI is 50% off for one week, 21 septembre 2026](https://x.com/NousResearch/status/2102079445607629260), [@witcheer, Grok 4.7 is on Nous Portal, 50% off for one week, 21 septembre 2026](https://x.com/witcheer/status/2102123240093024539) et [@witcheer, a reminder: a lot of the frontier models are at half their list price, 22 septembre 2026](https://x.com/witcheer/status/2102376807018164256)

## Xiaomi MiMo-V2.6, deux modèles omnimodaux en open source

Xiaomi a annoncé le 21 septembre MiMo-V2.6, décliné en Pro et Flash. Il s'agit de deux modèles nativement omnimodaux, qui progressent par apprentissage par renforcement mis à l'échelle. Le Pro se situe à parité avec Claude Opus 5 et GPT-5.6 Sol sur la plupart des bancs d'essai d'agent, et obtient 46 sur l'indice Artificial Analysis Intelligence, le plus haut score d'un modèle ouvert à ce jour selon les relais de la communauté.

La page officielle détaille les résultats. Le Pro obtient par exemple 71,9 sur DeepSWE v1.1, 89,9 sur Terminal Bench 2.1 et 82,0 sur OSWorld-Verified ; le Flash vise le meilleur équilibre entre intelligence, efficacité et coût. Côté tarifs, le Flash est facturé 0,14 dollar en entrée hors cache et 0,28 dollar en sortie, le Pro 0,435 dollar en entrée et 0,87 dollar en sortie. Les poids sont publiés sous licence ouverte et déjà disponibles sur Hugging Face. La documentation des fournisseurs de Hermes Agent liste déjà un fournisseur Xiaomi MiMo (`hermes chat --provider xiaomi --model mimo-v2-pro`), ce qui laisse attendre l'arrivée du nouveau modèle au catalogue à mesure qu'il se déploie.

> Sources : [@XiaomiMiMo, Introducing Xiaomi MiMo-V2.6 Pro & Flash, 21 septembre 2026](https://x.com/XiaomiMiMo/status/2102138559952290106), [Xiaomi, MiMo-V2.6, page officielle](https://mimo.xiaomi.com/mimo-v2-6) et [LLM and Model Providers, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/providers)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
