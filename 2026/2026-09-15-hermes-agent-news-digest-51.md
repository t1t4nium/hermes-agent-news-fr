# Hermes Agent Quotidien #51

Cette édition revient sur la sortie de la v0.21.3, sur l'ouverture du compte
Hermes Business et de l'offre Hermes Enterprise sur le Nous Portal, sur le
soixante-treizième numéro des Wingtips consacré aux horodatages de messages,
sur la visite guidée du centre de commande MCP du bureau et sur une soirée
Agentic AI à New York avec Nous Research.

## Hermes Agent v0.21.3 (v2026.9.14)

La note de release présente cette version comme une publication de maintenance
qui regroupe environ 338 demandes de tirage fusionnées depuis la v0.21.2 dans un
tag stable pour les consommateurs en aval que sont les images Docker, Hermes
Cloud et les déploiements hébergés, afin que les correctifs de connexion des
passerelles distantes atteignent les agents Cloud, lesquels se mettent à jour
vers le tag de release le plus récent.

Changements apportés :

- Les sessions du tableau de bord à distance n'expirent plus sur une rafale de
  rafraîchissements, les deux chemins de rafraîchissement de la passerelle
  regroupant désormais les requêtes concurrentes qui portent le même jeton
  rotatif, ce qui empêche une sortie de veille du bureau de rejouer un jeton
  déjà tourné et de faire révoquer la session entière.
- Le rafraîchissement sort de la boucle d'événements, si bien qu'un fournisseur
  d'identité lent ne fige plus `/api/status`.
- Les processus de longue durée ne fuient plus de descripteurs d'écriture
  dupliqués sur `state.db`, la passerelle, le back-end du tableau de bord et du
  bureau et les lecteurs ACP et CLI s'attachant en lecture seule tandis que les
  écrivains d'un même processus partagent le descripteur du registre.
- La fenêtre depuis la v0.21.2 totalise 1 036 commits hors fusion sur 2 642
  fichiers modifiés (+131 690 / -37 096) et 338 demandes de tirage fusionnées,
  relevés au commit 9b419a2d3c2657c192008e732149d61170b32c01.
- La note signale, sans les documenter, des requêtes JSON-RPC du serveur vers le
  client et un registre de contrats Pydantic avec du TypeScript et de l'OpenRPC
  générés pour la passerelle de la TUI et du bureau, ainsi que la sélection de
  l'effort de raisonnement sur chaque sélecteur de modèle, une pastille dans le
  composeur et un réglage par tâche auxiliaire dans le bureau.
- Toujours dans la fenêtre : la connexion OpenRouter en OAuth PKCE, le décodage
  des images HEIF, HEIC et AVIF, la refonte du réglage des pairs Honcho, des
  jetons de rafraîchissement OAuth des serveurs MCP liés à leur émetteur, un
  rappel quotidien de réauthentification MCP dans le bureau et le refus du WAL
  de `state.db` sur les systèmes de fichiers inter-machines.
- Les catalogues FAL accueillent Wan 3.0, Kling 3.0, Kling Image v3, MiniMax H3
  Max Turbo, Gemini Omni Flash 1.1 et Meta Muse, et la fenêtre apporte aussi les
  tableaux collés dans Slack, l'API Agent Sessions, l'isolation des profils
  multiplexés et des correctifs de vivacité de la passerelle.
- Les notes de release complètes de la fenêtre accompagneront la v0.22.0, qui
  documentera tout depuis la v0.21.0.
- La mise à jour se fait par `hermes update` ou par relance de l'installateur, et
  les images Docker et Hermes Cloud se construisent à partir de ce tag.

> Source : [Release v0.21.3 (v2026.9.14), teknium1, dépôt hermes-agent, 14 septembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.14)

## Hermes Business et Hermes Enterprise sur le Nous Portal

Nous Research a annoncé le 14 septembre l'ouverture du compte Hermes Business
sur le Nous Portal, qui permet d'inviter des collègues : l'équipe dispose
d'agents sur tous les canaux tout en partageant un solde unique avec des
plafonds par membre et une bibliothèque de skills commune. Hermes Enterprise
apporte les mêmes capacités en local ou dans le cloud du client, une pile d'IA
souveraine déjà utilisée par de grandes entreprises.

witcheer a publié le lendemain les réponses aux questions les plus posées sous
l'annonce. Les données vivent dans un locataire isolé par équipe sur
l'infrastructure de Nous Research, un déploiement Enterprise restant chez le
client. Le solde de l'équipe est distinct de celui de chaque personne,
l'invitation se fait par courriel depuis la page Team, et chaque membre reçoit
son propre agent hébergé qui puise dans le solde commun sous un plafond de
dépense fixé par l'organisation. Une skill construite par un membre est publiée
dans la bibliothèque de l'équipe et devient disponible à l'agent de chacun. Les
propriétaires et administrateurs gèrent les rôles, les plafonds et les clés
d'API, tandis que les membres se contentent de se connecter et d'utiliser leur
agent sur Discord, Telegram, Slack et WhatsApp via la passerelle d'équipe, en
plus du terminal, de l'application de bureau et du cloud. Côté modèles, tous
ceux de l'API d'inférence de Nous Research sont accessibles, ainsi que les clés
de fournisseur apportées par le client.

La page produit détaille les mêmes mécanismes et ajoute le cadre commercial.
Business tourne sur l'infrastructure de Nous Research en libre-service, tandis
qu'Enterprise s'installe sur l'infrastructure du client, avec authentification
unique, engagements de niveau de service et accompagnement à la mise en route.

> Sources : [@NousResearch, Hermes Agent is open for business, 14 septembre 2026](https://x.com/NousResearch/status/2099599032037388404), [@witcheer, here are the answers to the questions you asked most under yesterday's Hermes Business announcement, 15 septembre 2026](https://x.com/witcheer/status/2099840448118309278) et [Hermes Business, Nous Portal](https://portal.nousresearch.com/business)

## Wingtips #73 : l'heure d'envoi des messages rendue au modèle

Le soixante-treizième numéro des Wingtips traite d'un angle mort du passage par
une messagerie : l'agent lit les messages reçus sur Telegram ou Discord, mais
ne voit pas quand ils ont été envoyés. La clé `message_timestamps`, sous la
section `gateway` de `config.yaml`, corrige cela. Activée, chaque message de
l'utilisateur porte son heure d'envoi en tête, pour le modèle seulement : la
conversation affichée ne change pas et les transcriptions sur disque restent
propres, l'agent pouvant ainsi distinguer ce matin de la semaine dernière et
repérer un long silence.

La page de la passerelle de messagerie précise les contours du réglage. Il est
désactivé par défaut, l'horodatage est ajouté sous une forme du type
`[Tue 2026-04-28 13:40:53 CEST]` devant chaque message de l'utilisateur dans le
contexte du modèle, et rien n'est ajouté aux réponses de l'agent ni au prompt
système. Le mécanisme sert au raisonnement temporel, par exemple pour répondre à
un « tu me l'as demandé ce matin » ou pour remarquer un écart de plusieurs jours.
L'horodatage est de toute façon conservé comme métadonnée du message, si bien
qu'activer le réglage plus tard fait aussi apparaître l'heure des messages
passés, sans que la relecture accumule des préfixes en double.

> Sources : [@witcheer, Hermes Wingtips #73: gateway.message_timestamps, 15 septembre 2026](https://x.com/witcheer/status/2099784645529276481) et [Messaging Gateway, Message timestamps in model context, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/messaging#message-timestamps-in-model-context)

## La visite guidée du centre de commande MCP du bureau

tonbi a publié le 15 septembre une vidéo de visite du centre de commande MCP,
dans l'onglet Capabilities de l'application de bureau, retravaillé dans la
dernière version : les serveurs MCP de chaque profil et le catalogue au même
endroit, avec un bouton d'import présenté comme le chemin le plus court pour
ajouter un serveur.

witcheer a complété le lendemain par les questions qui reviennent le plus dans la
communauté. Chaque profil garde ses propres serveurs MCP et ses propres
connexions, et l'onglet Capabilities propose un sélecteur de portée pour voir
l'ensemble du profil en cours. Quand l'agent tourne sur une autre machine,
l'application de bureau héberge le rappel OAuth sur la machine locale et
transmet l'autorisation à la passerelle. Le jeton est ensuite mis en cache et
réutilisé jusqu'à ce qu'il ne puisse plus être rafraîchi ; le serveur est alors
mis en pause et l'application prévient une fois par jour, avec un bouton de
connexion et un bouton de désactivation. Le catalogue, enfin, ne contient que
des entrées relues par Nous Research et fusionnées par demande de tirage, et
l'installation affiche la liste des outils du serveur pour décocher ceux que
l'agent ne doit pas voir.

La documentation MCP confirme ce fonctionnement et en donne les détails. Les
entrées du catalogue vivent sous `optional-mcps/` dans le dépôt, désactivées par
défaut, et le choix d'outils coché à l'installation est écrit dans
`mcp_servers.<nom>.tools.include`, la commande `hermes mcp configure <nom>`
rouvrant la liste avec la sélection courante. Certaines entrées à très grande
surface déclarent au contraire une liste d'exclusion et sautent l'écran de
sélection.

> Sources : [@tonbistudio, The MCP Command Center in the Hermes Desktop App Capabilities tab got a big upgrade in the latest release, 15 septembre 2026](https://x.com/tonbistudio/status/2099733569828794705), [@witcheer, a few things about MCP in Hermes Agent that come up a lot in the community, 15 septembre 2026](https://x.com/witcheer/status/2099752917179760995) et [MCP (Model Context Protocol), documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)

## Une soirée Agentic AI à New York avec Nous Research

AAIF New York et Nous Research organisent le mardi 15 septembre une Agentic AI
Night à Manhattan, salle comble, avec une liste d'attente ouverte. witcheer a
résumé le programme la veille : une table ronde sur l'autorisation et
l'alignement du comportement des agents à mesure qu'ils gagnent en autonomie,
une intervention sur l'isolation du harnais de Hermes Agent, une autre sur
l'évolution du harnais par l'apprentissage automatique, puis un temps d'échange
libre avec les personnes qui construisent des agents en ville.

La page d'inscription précise le cadre. La soirée se tient de 18 heures à
21 heures au 7 W 34th St, parrainée par AWS qui fournit la salle, la nourriture
et les boissons, et coorganisée par Nous Research et Antimetal. La table ronde
réunit Karan Malhotra, cofondateur de Nous Research, Jake Moshenko, directeur
général d'AuthZed, et Shreyas Iyer, cofondateur et directeur technique
d'Antimetal, sous la modération de Lahari Chowtoori d'AWS. Crispin Velez
Villazon, de Google, parle ensuite de l'optimisation du harnais d'agent par
évolution de code guidée par l'apprentissage automatique, et Michael Levan, de
Solo.io, traite de l'isolation du harnais de Hermes Agent.

> Sources : [@witcheer, New York, tomorrow night you get the Nous team in the room!, 14 septembre 2026](https://x.com/witcheer/status/2099596003338772497) et [AAIF NYC: Agentic AI Night with Nous Research, page d'inscription Luma, 15 septembre 2026](https://luma.com/aaif-kc6u)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
