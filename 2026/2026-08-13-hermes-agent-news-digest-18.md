# Hermes Agent Quotidien #18

Les profils Hermes deviennent portables avec /export et /import, une nouvelle skill officielle transforme les appels API d'un site en client réutilisable, Grok 4.6 arrive dans Hermes Agent, la commande hermes claw migrate importe une installation OpenClaw, et le desktop laisse entrevoir un style inbox et un bot mode.

## /export et /import : les profils Hermes deviennent portables

Le 12 août, Nous Research a annoncé que les profils Hermes sont désormais portables et partageables. La commande /export sauvegarde un profil dans un fichier unique, sans les identifiants : skills, mémoire, persona, crons, plugins, réglages, thèmes et agencements du desktop. /import recharge le fichier et l'environnement est opérationnel.

Tonbistudio a montré l'usage en vidéo : exporter son agent par défaut depuis son PC vers une DGX Spark sous un nouveau nom, pour retrouver sur la machine les skills et mémoires accumulés. Witcheer a résumé : l'agent n'est plus lié à la machine sur laquelle il a grandi, et aucun identifiant ne voyage avec le fichier.

> Sources : [@NousResearch, 12 août 2026](https://x.com/NousResearch/status/2087592096769147377) - [@tonbistudio, 12 août 2026](https://x.com/tonbistudio/status/2087642578128921068) - [@witcheer, 12 août 2026](https://x.com/witcheer/status/2087596872378601748)

## Une skill officielle pour transformer un site en API réutilisable

Le 12 août, Teknium a présenté une nouvelle skill optionnelle : har-derived-api-client. Hermes exécute une ou plusieurs opérations sur un site web, observe les appels API effectués au passage, puis crée une API statique que l'agent ou ses scripts peuvent réutiliser ensuite. L'installation se fait avec la commande :

hermes skills install official/web-development/har-derived-api-client

Witcheer a commenté le lendemain : les meilleurs outils de son agent sont ceux qu'il a construits lui-même, car ils sont intégrés à son contexte. Hermes pilote un site une fois, regarde les appels API en dessous, et les distille en un client HTTP simple que ses scripts réutilisent. Chaque exécution suivante évite le navigateur : une requête bon marché au lieu d'un chargement complet de page.

> Sources : [@Teknium, 12 août 2026](https://x.com/Teknium/status/2087686461822996905) - [@witcheer, 13 août 2026](https://x.com/witcheer/status/2087775808374878524)

## Grok 4.6 disponible dans Hermes Agent

Le 12 août, Tommy (yeahfortommy) a annoncé que Grok 4.6 est disponible dans Hermes Agent. Le modèle de xAI est présenté comme une amélioration significative par rapport à Grok 4.5, au même prix. L'annonce a été relayée par Teknium et Nous Research.

> Sources : [@yeahfortommy, 12 août 2026](https://x.com/yeahfortommy/status/2087596559110185388)

## Hermes Wingtips #45 : hermes claw migrate

Le 13 août, witcheer a publié le quarante-cinquième numéro de sa série Hermes Wingtips. Le sujet : importer une installation OpenClaw existante dans Hermes Agent avec la commande hermes claw migrate, qui importe les réglages, les mémoires et les skills.

Deux précisions utiles : les clés API et tokens ne sont pas transférés sauf si on passe explicitement --migrate-secrets, et avant toute application, un zip de restauration du dossier Hermes home est écrit, ce qui rend le déplacement annulable. L'option --dry-run affiche seulement le plan sans rien toucher.

> Source : [@witcheer, 13 août 2026](https://x.com/witcheer/status/2087812081110147134)

## Desktop : un style inbox et un bot mode en préparation

Le 13 août, Brooklyn (imbabybrooklyn) a montré en vidéo un style inbox pour Hermes Agent Desktop. Nous Research et Teknium ont relayé la démonstration.

Le même jour, Teknium a laissé entendre qu'un bot mode pourrait arriver dans l'application desktop, avec une capture à l'appui. Rien n'est confirmé à ce stade.

> Sources : [@imbabybrooklyn, 13 août 2026](https://x.com/imbabybrooklyn/status/2087737281683620196) - [@Teknium, 13 août 2026](https://x.com/Teknium/status/2087819329605919196)

## Sources

- [@NousResearch - Profils portables, 12 août 2026](https://x.com/NousResearch/status/2087592096769147377)
- [@tonbistudio - Démo export/import, 12 août 2026](https://x.com/tonbistudio/status/2087642578128921068)
- [@witcheer - Commentaire portabilité, 12 août 2026](https://x.com/witcheer/status/2087596872378601748)
- [@Teknium - Skill har-derived-api-client, 12 août 2026](https://x.com/Teknium/status/2087686461822996905)
- [@witcheer - Commentaire skill API, 13 août 2026](https://x.com/witcheer/status/2087775808374878524)
- [@yeahfortommy - Grok 4.6 dans Hermes, 12 août 2026](https://x.com/yeahfortommy/status/2087596559110185388)
- [@witcheer - Wingtips #45, 13 août 2026](https://x.com/witcheer/status/2087812081110147134)
- [@imbabybrooklyn - Inbox style desktop, 13 août 2026](https://x.com/imbabybrooklyn/status/2087737281683620196)
- [@Teknium - Bot mode en préparation, 13 août 2026](https://x.com/Teknium/status/2087819329605919196)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
