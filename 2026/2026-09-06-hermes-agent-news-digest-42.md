# Hermes Agent Quotidien #42

Cette édition revient sur la possibilité d'épingler les fournisseurs OpenRouter modèle par modèle, sur la reprise en un geste des sessions Claude Code et Codex dans Hermes, sur le soixante-quatrième numéro des Wingtips consacré au fichier personnel AGENTS.override.md, et sur une réduction de moitié sur les abonnements du Nous Portal jusqu'au 9 septembre.

## Choisir son fournisseur OpenRouter modèle par modèle

Teknium a annoncé le 6 septembre que les utilisateurs d'OpenRouter peuvent désormais épingler les fournisseurs par modèle dans la configuration de Hermes Agent. Auparavant, il fallait verrouiller un fournisseur, ou un ensemble, à l'échelle globale, ce qui rendait délicat le changement de modèle tout en conservant des contraintes de fournisseur.

La documentation détaille la nouvelle clé. La section `provider_routing` du fichier `config.yaml` accepte une entrée `models` dont chaque sous-entrée, nommée par identifiant de modèle, reprend les réglages `sort`, `only`, `ignore`, `order`, `require_parameters` et `data_collection` pour ne les appliquer qu'à ce modèle ; tout ce qui n'est pas réglé par modèle retombe sur les valeurs communes. L'exemple documenté interdit à un revendeur de servir `openai/gpt-6-astra` en posant `only: ["openai"]`, épingle `claude-fable-5.1` sur `anthropic`, ou impose à `kimi-k2.6` un ordre de fournisseurs avec un classement par débit. La correspondance tolère les écarts d'orthographe et le préfixe `openrouter/`, et l'épinglage suit le modèle courant : changement via `/model`, activation de bascule, tâches cron et sous-agents délégués sur un autre modèle reçoivent chacun leurs propres contraintes. Ces clés se règlent en éditant directement `config.yaml`, car les identifiants de modèle contiennent des points que `hermes config set` lit comme séparateurs de chemin. Le routage par fournisseur ne s'applique qu'à OpenRouter : le Nous Portal décide du routage de son côté et n'accepte pas de préférence venue de l'appelant.

> Sources : [@Teknium, You can now pin providers per model in your Hermes Agent config, 6 septembre 2026](https://x.com/Teknium/status/2096569635948900404) et [Provider Routing, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)

## Reprendre une session Claude Code ou Codex dans Hermes

Tonbi a publié le 5 septembre une vidéo montrant la commande qui permet de poursuivre dans Hermes Agent une conversation entamée dans Claude Code ou Codex, et Teknium l'a mise en avant le même jour.

Hermes lit les journaux de session de Claude Code, dans `~/.claude/projects/`, et les rollouts de Codex CLI, dans `~/.codex/sessions/`, sans jamais modifier ces fichiers étrangers. `hermes sessions import --from claude` importe la conversation, et `--from codex` suivi d'un chemin pointe un rollout précis. `hermes --resume @claude` et `hermes --resume @codex` font l'import puis ouvrent directement la conversation reprise. L'import crée une session titrée `Imported from Claude Code: <premier message utilisateur>`, ou l'équivalent pour Codex, et affiche une commande `hermes --resume <id>` prête à coller. Ce qui traverse, c'est la conversation ordonnée entre utilisateur et assistant, l'activité des outils étant condensée en courtes notes `[ran tool: ...]` dans les tours de l'assistant ; les prompts système, le contexte injecté, les traces de raisonnement et les sorties brutes d'outils restent derrière, pour un transcript propre plutôt qu'une relecture octet à octet.

> Sources : [@tonbistudio, Now there's a single command that makes this possible, 5 septembre 2026](https://x.com/tonbistudio/status/2096238168978645260), [@Teknium, Easily pick up your codex or Claude code sessions in Hermes, 5 septembre 2026](https://x.com/Teknium/status/2096239718824550439) et [Sessions, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)

## Wingtips #64 : AGENTS.override.md, sa surcouche personnelle de projet

Dans le soixante-quatrième numéro des Wingtips, witcheer rappelle que lorsqu'on ouvre Hermes Agent dans un projet, il lit à chaque tour l'`AGENTS.md` de ce projet, le fichier où l'équipe range ses règles : organisation du code, zones à ne jamais toucher, commandes à lancer. La question posée est de savoir comment appliquer ses propres instructions sans toucher au fichier suivi par le dépôt.

La documentation répond avec `AGENTS.override.md`. Un seul type de contexte de projet est chargé par session, la première correspondance gagne : `.hermes.md`, puis `AGENTS.override.md`, puis `AGENTS.md`, puis `CLAUDE.md` et `.cursorrules`. Quand un `AGENTS.override.md` se trouve à côté d'un `AGENTS.md`, la surcouche est chargée à la place du fichier engagé. On garde ainsi un fichier personnel, généralement ignoré par git, pour des instructions différentes de celles du référentiel sans éditer l'`AGENTS.md` suivi.

> Sources : [@witcheer, Hermes Wingtips #64 : AGENTS.override.md, 6 septembre 2026](https://x.com/witcheer/status/2096481734388858931) et [Context Files, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)

## Moitié prix sur les abonnements du Nous Portal jusqu'au 9 septembre

Nous Research a annoncé le 5 septembre une réduction de 50 % sur tout abonnement du Nous Portal jusqu'au 9 septembre, avec le code `LMH4FMJ2`. witcheer, qui voit dans cette offre le signe que beaucoup attendaient pour essayer Hermes Agent, rappelle qu'une seule souscription du portail ouvre l'accès au catalogue de modèles, à la passerelle d'outils hébergée et aux agents cloud du Nous Portal.

> Sources : [@NousResearch, Accelerate your labor with Hermes Agent, 5 septembre 2026](https://x.com/NousResearch/status/2096263611811320228) et [@witcheer, half price on any Nous Portal subscription, 5 septembre 2026](https://x.com/witcheer/status/2096265225183891468)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
