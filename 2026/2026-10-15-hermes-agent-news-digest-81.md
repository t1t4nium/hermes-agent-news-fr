# Hermes Agent Quotidien #81

Cette édition revient sur la release v0.22.2, qui corrige un v0.22.1 parti du mauvais commit, sur les 66 pull requests fusionnées le 14 octobre, sur le plugin phone-harness qui donne à l'agent la main sur un vrai téléphone, et sur la Pet Room de Herald OS, qui donne à chaque agent sa propre silhouette.

## v0.22.2, la release que v0.22.1 devait être

Nous Research a publié v0.22.2 le 15 octobre 2026. v0.22.1 était parti du mauvais commit : il embarquait un travail de passerelle pas encore prêt, et l'application Microsoft Store pouvait rester bloquée sur `Connecting.`. v0.22.2 est donc la release que v0.22.1 devait être. Un défaut connu subsiste : les sessions qui ont tourné sous la passerelle 0.22.1 ne peuvent pas être supprimées en 0.22.2.

Deux correctifs sont mis en avant :

- La passerelle redémarre après un reboot. Au redémarrage, Linux peut attribuer un PID précoce à un processus sans rapport, et la passerelle pouvait le confondre avec une passerelle déjà active, ce qui empêchait une passerelle supervisée (systemd, launchd, Docker) de démarrer. Hermes note désormais le boot où il a démarré, et quand il ne peut pas trancher, il interroge le verrou d'hôte que seule une passerelle vivante détient. (#138594, corrige #133744)
- Les longs tours en modèle local survivent sur portable. Les requêtes locales diffusent leur progression de lecture du prompt dans la ligne de statut, les minuteries de blocage sautent le temps où la machine dormait, un serveur local récupéré reçoit une nouvelle tentative au lieu d'un disjoncteur qui échouait à chaque message suivant, et la compression ne dépasse plus son délai pendant que le serveur lit encore une longue conversation. Sur les machines Windows à mémoire unifiée, le lancement du modèle et le cache de prompt sont dimensionnés selon la mémoire libre. (#138560)

La release embarque aussi, depuis v0.22.0 :

- Le bundle Microsoft Store est scindé dans sa propre voie de build windows-store.
- Nemotron 3.5 Super VL gagne des paramètres par défaut et rejoint la liste des modèles par défaut de NVIDIA NIM, avec une liste de modèles sélectionnés placée en tête du sélecteur.
- Deux packs de langue entrent au catalogue : coréen (hermes-lang-ko) et portugais brésilien (hermes-lang-pt-br).
- Plusieurs plugins rejoignent le catalogue : teamorouter, author-feed, wait-ledger, lightningai, openinvest, hermes-agent-mixer et Hermes AAC. Kumiho Memory passe au rayon mémoire.

> Sources : [Hermes Agent v0.22.2, release GitHub NousResearch, 15 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.2)

## 66 pull requests fusionnées le 14 octobre

iamlukethedev a fait le compte le 15 octobre : Hermes a fusionné 66 pull requests le 14 octobre. Les changements mis en avant :

- Un runtime de passerelle unifié : une seule passerelle possède chaque session locale (CLI, TUI, Desktop, API, ACP, bots et cron).
- Le dialogue de mise à jour de Desktop affiche les vraies notes de release sur la voie stable et les dernières pull requests sur main.
- Un chemin spécifique au Microsoft Store.

> Sources : [@iamlukethedev, Hermes merged 66 PRs on October 14, 15 octobre 2026](https://x.com/iamlukethedev/status/2110524491088662583)

## phone-harness, la main sur un vrai téléphone

witcheer a présenté le 15 octobre phone-harness, un plugin du catalogue qui donne à Hermes Agent le contrôle d'un vrai téléphone en une seule installation. L'agent voit l'écran, tape, glisse et saisit du texte, ce qui fonctionne avec les applications qui n'ont ni API ni plugin propre.

La fiche du catalogue précise le mécanisme : le plugin, maintenu par ShawnPana et épinglé au commit 7e3ea6c, n'expose qu'un outil, phone_exec. Le modèle écrit un court script Python avec les helpers déjà importés, le plugin l'exécute sur le téléphone et renvoie ce qu'il a affiché. Chaque appel phone_exec demande une approbation avant de s'exécuter, via un hook pre_tool_call, et l'auto-exécution par classificateur est désactivée par défaut, car la heuristique peut être contournée. Les sous-agents se passent le téléphone à tour de rôle par un verrou interne, l'outil signalant le téléphone occupé au bout de 120 secondes. Aucune intégration de coffre de mots de passe : l'agent ne saisit jamais de mot de passe, de code PIN ni de code 2FA. L'installation passe par `hermes plugins install ShawnPana/phone-harness/integrations/hermes`. iPhone demande les droits Accessibilité et Enregistrement d'écran, Android un adb, et un téléphone cloud un `phone-harness cloud login`.

> Sources : [@witcheer, Hermes Agent can use your real phone the way you do, 15 octobre 2026](https://x.com/witcheer/status/2110664477301743817) et [phone-harness, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/phone-harness)

## La Pet Room de Herald OS

iamlukethedev a annoncé le 15 octobre la Pet Room de Herald OS : chaque agent Hermes vivant y apparaît comme son propre animal, et l'on regarde littéralement ce qu'il fait. S'il utilise le terminal, il se rend au terminal ; s'il ouvre le navigateur, il se dirige vers le navigateur.

Herald OS est le système d'exploitation open source autour de l'agent, signé Luke The Dev et sans affiliation avec Nous Research. La Pet Room prolonge l'intégration avec Petdex annoncée la veille : la mascotte Teknium vit sur le bureau, et désormais chaque agent actif a sa place dans la pièce.

> Sources : [@iamlukethedev, I gave every Hermes agent its own little life inside Herald OS, 15 octobre 2026](https://x.com/iamlukethedev/status/2110662685570499065)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
