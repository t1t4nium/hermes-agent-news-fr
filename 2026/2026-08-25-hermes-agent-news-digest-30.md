# Hermes Agent Quotidien #30

Cette édition revient sur le HUD mode du bureau, qui transforme l'agent en calque flottant au-dessus des applications, sur les lanes de worktree qui laissent deux agents travailler sur le même dépôt sans se gêner, et sur un chiffre d'adoption relayé par Nous Research.

## Le HUD mode : Hermes devient un calque flottant

Hermes Desktop dispose d'un HUD mode documenté : la combinaison Cmd/Ctrl+Shift+H (ou le bouton de la barre de titre) détache le chat dans une barre flottante sans chrome, toujours au premier plan, posée au-dessus de l'application active. La fenêtre principale s'efface, le HUD conserve la conversation en cours et son champ de saisie. La position de la barre sert de contexte : elle indique à Hermes quelle application et quel écran on regarde, si bien que « ceci », « ici » ou « cette page » se résolvent en fonction de ce qui se trouve dessous.

imbabybrooklyn l'a montré en jouant à World of Warcraft tout en interrogeant l'agent : l'overlay permet de garder un œil sur la conversation ou de poser des questions pendant la partie, et peut servir de guide in-game, car l'agent est conscient du jeu affiché et peut aider visuellement. Nous Research a relayé la démonstration sous le mot d'ordre « prompt sans perdre le rythme ». La communauté relève d'autres usages de l'agent qui voit et exploite les applications sous-jacentes : lire des posts X, analyser des graphiques TradingView ou interagir avec un logiciel de montage vidéo directement à l'écran.

> Sources : [@imbabybrooklyn, le HUD mode pendant une partie de WoW, 24 août 2026](https://x.com/imbabybrooklyn/status/2091725936311910909), [@NousResearch, prompter sans interruption avec le HUD mode, 24 août 2026](https://x.com/NousResearch/status/2091893618801885456) et [Hermes Desktop, section HUD mode, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#hud-mode)

## Deux agents, un dépôt : les lanes de worktree

Hermes Desktop sait créer un worktree Git sur une nouvelle branche avec Cmd/Ctrl+Shift+B, ou via « New worktree » sur un projet de la barre latérale. L'agent travaille alors sur une copie parallèle du dépôt sans toucher au checkout, et le worktree apparaît comme sa propre lane sous le projet ; la retirer offre de supprimer le répertoire correspondant (la branche est conservée) ou de simplement masquer la lane.

witcheer illustre le cas d'usage typique : deux agents, un dépôt, en même temps, chacun avec sa branche et sa copie de travail, si bien qu'ils ne se touchent jamais les fichiers. Chaque lane est isolée et possède son propre /rollback. En cascade, ce mécanisme fournit la brique de base d'une orchestration où plusieurs agents avancent en parallèle sur le même projet sans conflit d'écriture.

> Sources : [@witcheer, deux agents, un dépôt, des lanes de worktree, 24 août 2026](https://x.com/witcheer/status/2091899279614873716) et [Hermes Desktop, section Git review & worktrees, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#git-review--worktrees)

## Hermes approche les 2,3 T de tokens par jour

@ani_pai, relayé par Nous Research, observe que pendant que les modèles open weight se commodifient entre eux, les harnesses continuent de gagner en vitesse plus vite que tout : le Hermes Agent consommerait environ 2,3 T de tokens par jour, en hausse de plus de 100 % par rapport au mois précédent.

> Source : [@ani_pai, la consommation de Hermes Agent, 23 août 2026](https://x.com/ani_pai/status/2091606477362311666)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
