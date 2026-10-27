# Hermes Agent Quotidien #93

Cette édition revient sur les 59 pull requests fusionnées le 26 octobre, sur l'arrivée de GPT-6.1 Terra dans Hermes Agent, sur le plugin officiel Advanced Delegation et ses deux modes de délégation, sur hermes webapp qui porte Desktop dans le navigateur, sur le plugin de montage vidéo kinocut, sur une montre Wear OS pour Hermes et sur deux rendez-vous Nous Research à New York.

## 59 pull requests fusionnées le 26 octobre

iamlukethedev a fait le compte le 27 octobre : Hermes a fusionné 59 pull requests le 26 octobre. Les changements mis en avant :

- GLM-5.3 devient le modèle par défaut silencieux.
- GitHub Copilot sort du coeur vers son propre plugin github-copilot (Hermes Labs), désormais listé au catalogue.
- Hermes démarre environ une seconde plus vite depuis un checkout git.

Le changelog du 26 octobre relève aussi le passage de toutes les lectures et écritures de config.yaml par une couture ConfigBackend ; la commande optimize-storage qui affiche la progression à chaque phase et finit en un peu plus d'une minute au lieu de près de vingt-cinq ; les fenêtres de Desktop sous Linux qui ne sont plus définitivement translucides ; le coût de frappe qui ne croît plus avec l'historique chargé ; et le démarrage qui n'attend plus la purge du répertoire scratch.

> Sources : [@iamlukethedev, Hermes merged 59 PRs on October 26, 27 octobre 2026](https://x.com/iamlukethedev/status/2114913432118169969) et [Hermes Bible, changelog du 26 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-26)

## GPT-6.1 Terra disponible dans Hermes Agent

Teknium a annoncé le 27 octobre que 6.1 Terra, le modèle qu'OpenAI vient de lancer, est disponible dans Hermes Agent via le Nous Portal et Open Router. OpenAI présente GPT-6.1 Terra comme un modèle d'usage ordinateur rapide et moins cher : il lit ce qui est à l'écran, agit entre les applications, écrit naturellement et tient la journée de travail grâce à son efficacité.

> Sources : [@Teknium, 6.1 Terra now available in Hermes Agent, 27 octobre 2026](https://x.com/Teknium/status/2114920088357032109) et [@OpenAI, GPT-6.1 Terra: delivering fast and capable computer use, 26 octobre 2026](https://x.com/OpenAI/status/2114780711664398349)

## Advanced Delegation, deux modes pour les sous-agents

Nous Research a présenté le 26 octobre le plugin officiel Advanced Delegation, qui ajoute deux modes de délégation au delegate_task intégré. Le premier, les routes de modèles, laisse l'agent choisir par tâche une route nommée que l'on définit (rapide, profonde, locale). Le second, les routes de profils, fait tourner le sous-agent comme l'un de ses profils Hermes, avec le modèle, les identifiants, les skills et le SOUL.md de ce profil.

Seuls le nom et la description d'une ligne que l'on écrit arrivent au modèle : le fournisseur, l'identifiant du modèle, le point d'accès et la clé ne deviennent jamais des paramètres d'outil. iamlukethedev résume : pas besoin du gros modèle pour chaque sous-agent, une route rapide pour les recherches et les résumés, une route profonde pour le dur, ou la main à un profil entier. witcheer a montré son essai du week-end : un résumé parti vers Haiku 5.5 et une énigme logique vers Opus 5.5, l'agent principal ayant choisi chaque route lui-même.

Le catalogue précise l'installation (hermes plugins install advanced-delegation, Hermes 0.22.5 minimum), la configuration via hermes delegation config et la commande slash /delegation pour changer de mode en cours de conversation. tonbistudio a publié une vidéo de prise en main.

> Sources : [@NousResearch, With the new Advanced Delegation modes plugin, 26 octobre 2026](https://x.com/NousResearch/status/2114753914939863260), [@Teknium, Two new modes for your subagent delegation, 26 octobre 2026](https://x.com/Teknium/status/2114755154977395012), [@iamlukethedev, Not every subagent needs the big model, 26 octobre 2026](https://x.com/iamlukethedev/status/2114793203564240951), [@witcheer, this is what I ran this week-end, 26 octobre 2026](https://x.com/witcheer/status/2114756140558889081), [@tonbistudio, Advanced Delegation video, 26 octobre 2026](https://x.com/tonbistudio/status/2114856291848138767) et [advanced-delegation, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/advanced-delegation)

## hermes webapp, Desktop dans le navigateur

tonysimons a annoncé le 26 octobre que la pull request de BearHuddleston est fusionnée : hermes webapp porte le vrai Hermes Desktop dans n'importe quel navigateur, depuis son propre hôte. Chat, fichiers, git, un terminal qui survit aux rafraîchissements et la connexion à distance. Teknium a relayé le 27 octobre en invitant à l'essayer tôt, en passant le canal de release de Hermes Agent sur main au lieu de stable.

> Sources : [@tonysimons, hermes webapp brings the REAL Hermes Desktop to ANY browser, 26 octobre 2026](https://x.com/tonysimons/status/2114598038568116579) et [@Teknium, Give it a try early by switching your release channel, 27 octobre 2026](https://x.com/Teknium/status/2114919004632764585)

## kinocut, montage vidéo local encadré

witcheer a présenté le 27 octobre kinocut, un plugin communautaire construit par Kyanite Labs pour le montage vidéo local. Il ajoute le serveur MCP Kinocut et deux skills, une pour l'édition et une pour les clips courts : on transforme un clip 16:9 en short 9:16 sous-titré sur sa propre machine.

Le catalogue et la pull request #142459 précisent le cadre : FFmpeg et ffprobe font le traitement local, les montages ordinaires ne demandent ni compte ni clé API, et les appels de vision optionnels sont désactivés par défaut. Il faut uv, FFmpeg sur le PATH et Python 3.11 ou plus récent. Le bundle 1.16.7 épingle le runtime 1.16.4, le plugin est signé simongonzalezdc et distribué sous Apache-2.0 par Kyanite Labs.

> Sources : [@witcheer, kinocut, a community plugin for guarded local video editing, 27 octobre 2026](https://x.com/witcheer/status/2115088632143053199), [kinocut, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/kinocut) et [plugin-catalog: add kinocut, PR #142459](https://github.com/NousResearch/hermes-agent/pull/142459)

## Une montre Wear OS pour Hermes

witcheer a montré le 27 octobre une autre montre pour Hermes Agent, cette fois sous Wear OS. L'application reconnaît la voix sur la montre et envoie le texte directement au serveur API de Hermes Agent, sans application de téléphone entre les deux. On maintient l'orbe, on parle, et la réponse est lue à voix haute.

Le code est ouvert sur jribnik/hermes-wear : une application Wear OS autonome, écrite pour une Pixel Watch (Wear OS 3 ou plus récent), qui dialogue en HTTP simple avec l'API compatible OpenAI de la passerelle, avec la seule permission Internet. La voix passe par le reconnaisseur du système, sans permission de micro supplémentaire.

> Sources : [@witcheer, another watch for Hermes Agent, this time on Wear OS, 27 octobre 2026](https://x.com/witcheer/status/2115044232302108808) et [jribnik/hermes-wear, dépôt GitHub](https://github.com/jribnik/hermes-wear)

## Deux rendez-vous Nous Research à New York

witcheer a annoncé le 27 octobre être à New York pour NousCon, qui se tient le 30 octobre à partir de 18 h. L'événement gratuit, sur approbation, est présenté comme une soirée avec ceux qui construisent l'intelligence ouverte : portes à 18 h, démonstrations et networking jusqu'à 21 h, puis fête jusqu'à minuit.

Plus tôt, Nous Research et Pangram ont annoncé un hackathon anti-slop au siège de Pangram à New York le 22 novembre, avec Reducto.

> Sources : [@witcheer, three days to NousCon, 27 octobre 2026](https://x.com/witcheer/status/2115074168110580146), [NousCon 2026, page événement, 30 octobre 2026](https://events.trymimetic.com/events/nyc/nouscon-2026-oct-2026), [@NousResearch, Join us at Pangram HQ for an anti-slop hackathon, 26 octobre 2026](https://x.com/NousResearch/status/2114780096204857522) et [@pangram, Non-Slop hackathon with NousResearch and Reducto, 26 octobre 2026](https://x.com/pangram/status/2114739467273544129)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
