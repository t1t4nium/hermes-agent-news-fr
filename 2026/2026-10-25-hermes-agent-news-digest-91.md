# Hermes Agent Quotidien #91

Cette édition revient sur les 86 pull requests fusionnées le 24 octobre, sur le plugin crontab-ref qui lit les expressions cron, sur viajante qui cherche vols et hôtels depuis sa machine, sur hookspool qui garde les webhooks sur disque, et sur les 144 plugins ajoutés au catalogue cette semaine.

## 86 pull requests fusionnées le 24 octobre

iamlukethedev a fait le compte le 25 octobre : Hermes a fusionné 86 pull requests le 24 octobre. Les changements à retenir :

- Les plugins Desktop peuvent désormais afficher les médias que leurs propres outils produisent, directement dans l'application.
- Les utilisateurs de Desktop sous Windows peuvent enfin se connecter à des machines distantes en SSH Windows.
- Les réponses en streaming qui contiennent des images markdown affichent maintenant les vraies images plutôt que le texte.

Le changelog du 24 octobre relève aussi la suppression des clés API Context7 dans les journaux grâce à leur préfixe vendeur ; une allowlist MCP par tâche cron qui ne s'élargit plus à tous les serveurs activés ; les approbations d'écriture MCP non fiables qui montrent les arguments de l'appel, secrets masqués ; les résultats et les listes d'outils MCP de plus de 1 MiB qui passent désormais en Streamable HTTP ; l'audio simple envoyé en pièce jointe plutôt qu'en note vocale ; et les commandes /refine et /review qui fonctionnent sur une session laissée inactive. Côté catalogue, le plugin Blender s'installe désormais lui-même et détecte une installation du Microsoft Store.

> Sources : [@iamlukethedev, Hermes merged 86 PRs on October 24, 25 octobre 2026](https://x.com/iamlukethedev/status/2114183209747468607) et [Hermes Bible, changelog du 24 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-24)

## crontab-ref, lire une expression cron en mots clairs

witcheer a rappelé le 25 octobre le piège classique : « 0 9 1 * 1 » ne veut pas dire « le premier lundi du mois », mais « le 1er et chaque lundi ». crontab-ref est un plugin communautaire qui donne à l'agent la lecture en mots clairs de n'importe quelle expression cron. On écrit @crontab:"..." dans un message et Hermes la remplace par ce que chaque champ veut dire, par la réponse de /cron (acceptée ou non), par les cinq prochains déclenchements calculés dans le fuseau de Hermes, et par des notes sur les cas que les gens se trompent souvent. La lecture vient de croniter, la bibliothèque du planificateur de Hermes, donc rien d'autre ne s'installe. Installation : hermes plugins install crontab-ref --enable, à partir de Hermes 0.21.5, sans clé API ni configuration.

> Sources : [@witcheer, when does "0 9 1 * 1" run?, 25 octobre 2026](https://x.com/witcheer/status/2114360079285690629) et [crontab-ref, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/crontab-ref)

## viajante, chercher vols et hôtels depuis sa machine

witcheer a présenté le 24 octobre viajante, un plugin communautaire qui cherche des vols et des hôtels depuis sa propre machine, sans clé API et sans compte. Il lit les pages publiques de Google Flights et Google Hotels depuis l'adresse IP locale, renvoie les prix, les horaires et les liens, et donne à l'agent 22 outils plus une skill qui explique comment lire les résultats. Il ne réserve rien et ne stocke aucun identifiant. Le catalogue précise que le plugin est distribué sous licence MIT par felipebasurto, avec un serveur MCP épinglé (npx -y @viajante/mcp), et qu'il demande uv, Python 3.10 ou plus récent et Node.js.

> Sources : [@witcheer, viajante is a community plugin for Hermes Agent that searches flights and hotels, 24 octobre 2026](https://x.com/witcheer/status/2114046764202500179) et [viajante, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/viajante)

## hookspool, garder les webhooks sur disque

witcheer a annoncé le 25 octobre hookspool, un projet communautaire open source qui place une boîte de réception locale devant les routes webhook de Hermes : chaque événement reste sur disque jusqu'à ce que l'agent le traite. L'idée est que l'agent puisse prendre l'initiative quand un mail arrive, qu'un fichier est partagé ou qu'un build se termine, au lieu d'attendre la prochaine requête.

> Source : [@witcheer, your Hermes Agent can message you first, 25 octobre 2026](https://x.com/witcheer/status/2114318558788276703)

## 144 plugins ajoutés au catalogue cette semaine

witcheer a compté le 24 octobre que la communauté a ajouté 144 plugins au catalogue de Hermes cette semaine. Il en liste six à installer en premier, dont llmslim, qui compacte les anciennes sorties d'outils sur la machine sans appel de modèle pour que le cache de prompt continue de fonctionner, et hermes-memory-pane, qui affiche ce que l'agent a enregistré en mémoire.

> Source : [@witcheer, the community added 144 plugins to the Hermes plugin catalog this week, 24 octobre 2026](https://x.com/witcheer/status/2114069413016342629)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
