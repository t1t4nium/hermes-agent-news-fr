# Hermes Agent Quotidien #99

Cette édition revient sur la migration en une commande des bots Grok Bot et OpenBot, sur les 40 pull requests fusionnées le 1er novembre, sur la commande /personality, sur les 23 thèmes Omarchy embarqués dans un plugin, et sur un Hermes Agent qui tient neuf tâches sur dix sans aucun paquet sortant.

## La migration Grok Bot et OpenBot en une commande

Le 2 novembre, iamlukethedev a annoncé que Hermes importe désormais toute une installation Grok Bot en une commande, après une fusion de Teknium dans hermes-agent main. `hermes migrate grok-bot` transforme les routines en tâches cron de Hermes, avec la même planification et le même fuseau horaire, et emporte les skills, les mémoires et le rôle du bot.

La pull request #147724, signée teknium1 et fusionnée le 2 novembre, décrit le mécanisme. Les personnes qui quittaient Grok Bot n'avaient aucun chemin d'entrée depuis `hermes setup` ou `hermes migrate` : seul le plugin agent-importers connaissait les autres agents, et rien ne connaissait Grok Bot. Désormais, `hermes setup` propose au premier lancement l'import Grok Bot et OpenBot à côté d'OpenClaw, Claude Code, Codex et Cursor, et `hermes migrate` (nu, ou `hermes migrate <agent>`) installe le plugin d'import s'il manque puis l'exécute.

Le plugin agent-importers 1.2.0 (#147799) porte les importeurs réels. Grok Bot garde ses bots, routines et skills dans son compte cloud sans bouton d'export, donc chaque bot s'exporte lui-même : la commande imprime un message à coller dans la conversation du bot, qui écrit `grok-bot-export.json` sans rien modifier. Les routines arrivent en pause pour ne pas tourner deux fois pendant que la copie Grok vit encore, et l'on les réactive avec `hermes cron resume` ou l'option `--activate-routines`. Une correction 1.2.1 (#147852) a suivi, ajustée au premier export réel.

> Sources : [@iamlukethedev, Hermes can now import your whole Grok Bot setup with one command, 2 novembre 2026](https://x.com/iamlukethedev/status/2117169020164256118), [Grok Bot and OpenBot users can move to Hermes, PR #147724, dépôt hermes-agent](https://github.com/NousResearch/hermes-agent/pull/147724), [agent-importers 1.2.0, PR #147799](https://github.com/NousResearch/hermes-agent/pull/147799) et [Import from Other Agents, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/import-from-other-agents)

## 40 pull requests fusionnées le 1er novembre

iamlukethedev a fait le compte le 2 novembre : Hermes a fusionné 40 pull requests le 1er novembre. Il en retient trois. On peut verrouiller une skill pour que l'agent ne la réécrive plus, par skill_manage, write_file, patch ou le terminal. Les plugins et les hooks shell peuvent bloquer un tour avant qu'il n'atteigne le modèle. Et les invites d'approbation révèlent l'Unicode caché au lieu de le masquer.

Le changelog du 1er novembre précise et complète :

- Verrouiller une skill la rend inaltérable par l'agent, quel que soit l'outil (#147557).
- Un plugin ou un hook shell peut arrêter un tour avant le modèle, via la directive de blocage pre_llm_call (#81434).
- Les invites d'approbation affichent l'Unicode, les octets de contrôle et le padding qu'elles masquaient, dans le CLI, la passerelle, la TUI et Desktop (#81403).
- Chaque passerelle ajoutée reste connectée et l'on bascule de l'une à l'autre sans confirmation ni liste vide (#147681).
- Un plafond opt-in limite la durée de vie totale d'une réponse en streaming, via agent.stream_max_lifetime (#80701).
- `/model reset` ramène une session au modèle configuré par défaut sans perdre l'historique (#80448).
- Les vidéos Telegram arrivent à l'agent au lieu d'être abandonnées (#147572).
- Hermes ne copie plus de jetons de bot sensibles dans les nouveaux profils (#147432).
- Sai, l'agent d'usage d'ordinateur de Simular, entre au catalogue de plugins (#146322).

> Sources : [@iamlukethedev, Hermes merged 40 PRs on November 1, 2 novembre 2026](https://x.com/iamlukethedev/status/2117131962657968410) et [Hermes Bible, changelog du 1er novembre 2026](https://www.hermesbible.com/changelog?date=2026-11-01)

## /personality, changer la voix de l'agent en une commande

witcheer a consacré le 114e numéro des Wingtips à `/personality`, la commande qui change la façon dont l'agent s'adresse à soi. `/personality` liste les styles disponibles, puis l'on en choisit un, par exemple `/personality pirate` ; `/personality none` le désactive. La commande fonctionne dans le terminal, dans les applications de messagerie et dans Hermes Desktop.

La documentation précise la mécanique. `/personality` est une surcouche de session qui modifie ou complète l'invite système courante, par opposition à SOUL.md, la personnalité par défaut durable. Hermes embarque des personnalités prêtes à l'emploi, dont concise, technical et teacher, et l'on peut ajouter les siennes sous `agent.personalities` dans config.yaml. `/personality none` (ou `default`, ou `neutral`) efface la surcouche et revient au comportement de base ; la commande sans argument liste les presets et marque celui qui est actif.

> Sources : [@witcheer, Hermes Wingtips #114: /personality, 2 novembre 2026](https://x.com/witcheer/status/2117174120756785245) et [Personality & SOUL.md, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)

## hermes-themes-pack, les 23 thèmes Omarchy dans Hermes

witcheer a présenté le 2 novembre hermes-themes-pack, un plugin qui fait suivre le thème d'Omarchy à son Hermes Agent : l'on choisit un thème dans Omarchy et l'agent bascule sur le même. Le pack embarque les 23 thèmes Omarchy, et `/theme <nom>` bascule à la main quand on en veut un autre.

La fiche du catalogue détaille le fonctionnement. Une skin est l'unité de thème de Hermes : le CLI, le TUI et Desktop se repeignent tous depuis elle en moins d'une seconde. Les 23 thèmes Omarchy, dont Tokyo Night, Catppuccin, Gruvbox, Nord, Rose Pine et Jade Horse, deviennent chacun une skin nommée, avec des versions retravaillées pour Tokyo Night et Jade Horse. Le plugin fonctionne sans Omarchy ; les parties Omarchy (`/theme omarchy`, `/theme follow`) sont optionnelles. `/theme follow on` installe un petit hook dans `~/.config/omarchy/hooks/theme-set.d/` qu'Omarchy exécute à chaque changement de thème. Le plugin exige Hermes 0.22.5 ou plus récent, et n'effectue aucun appel réseau.

> Sources : [@witcheer, if you use Omarchy, your Hermes Agent can follow it, 2 novembre 2026](https://x.com/witcheer/status/2117261697958510882) et [hermes-themes-pack, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/hermes-themes-pack)

## Neuf tâches sur dix sans aucun paquet sortant

witcheer a mesuré le 2 novembre ce qu'un Hermes Agent arrive à faire avec le réseau débranché : neuf tâches du quotidien sur dix passent encore, sans le moindre paquet sortant. Le message a été posté depuis un avion sans wifi, et l'agent du test n'en avait pas non plus. L'agent tourne hors ligne avec le modèle sur la même machine via une socket unix, et il peut encore éditer.

> Source : [@witcheer, Hermes Agent with the network unplugged: 9 of 10 everyday tasks, 2 novembre 2026](https://x.com/witcheer/status/2117052318445121638)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
