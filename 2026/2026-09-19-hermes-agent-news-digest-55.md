# Hermes Agent Quotidien #55

Cette édition revient sur le soixante-dix-septième numéro des Wingtips consacré
aux cloches sonores du CLI, sur le routage des messages par expéditeur vers un
profil, désormais intégré en amont dans le dépôt de Hermes Agent, sur
Hermes-Portal, la page web en lecture seule d'une installation, sur la
conclusion de la masterclass vidéo consacrée à l'application de bureau, sur
l'accueil de nouveaux membres dans les équipes Hermes et sur une routine
matinale offerte par un simple prompt. Aucune release n'a été publiée depuis la
v0.21.3 du 14 septembre.

## Wingtips #77 : les cloches de fin de tâche et d'invite

Le soixante-dix-septième numéro des Wingtips traite de
`display.bell_on_complete` et `display.bell_on_prompt`, deux réglages du CLI de
Hermes Agent pensés pour un usage en arrière-plan. On confie au CLI une tâche
longue et l'on s'éloigne : pendant l'absence, l'agent soit termine, soit
s'interrompt pour poser une question, demander une approbation, un mot de
passe sudo ou capturer un secret.

La page de configuration détaille les deux clés booléennes.
`display.bell_on_complete` joue la cloche du terminal quand l'agent a fini,
adapté aux longues tâches. `display.bell_on_prompt` joue la cloche quand une
invite bloquante s'ouvre, clarification, approbation, mot de passe sudo ou
capture de secret, et fonctionne aussi par SSH. Les deux drapeaux émettent en
outre une notification de bureau OSC 9, que Ghostty, iTerm2, Kitty et WezTerm
relèvent en alerte du système, et, sous Warp avec le protocole CLI-agent
annoncé, un événement `warp://cli-agent` OSC 777, signal `stop` à la fin d'une
tâche et `permission_request` sur une invite bloquante, de sorte que
l'onglet et la file de notifications de Warp suivent Hermes sans clé
supplémentaire.

> Sources : [@witcheer, Hermes Wingtips #77: display.bell_on_complete and bell_on_prompt, 19 septembre 2026](https://x.com/witcheer/status/2101229280185270718) et [Configuration, Display Settings, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)

## Le routage des profils par expéditeur rejoint le gateway

weiszfeld a annoncé le 19 septembre que le routage des profils par expéditeur
venait d'atterrir en amont dans le dépôt NousResearch, une contribution rendue
possible par l'implémentation d'Italo Fernandes et le portage de Teknium. C'est
le premier des nombreux retours qu'il prévoit de faire à Hermes en s'appuyant
sur Hermes lui-même.

La demande de tirage #106019 détaille le mécanisme. `gateway.profile_routes`
ne pouvait discriminer que sur la provenance d'un message, `guild_id`,
`chat_id` ou `thread_id` : donner à deux personnes partageant un même canal
leur propre profil isolé obligeait donc à lancer deux bots. Le correctif ajoute
`user_id` comme quatrième critère, l'expéditeur du message entrant, confronté
par égalité exacte et conjointement aux champs de localisation, de sorte que
`user_id` plus `chat_id` désigne cette personne dans ce canal. L'auteur a
choisi de ne pas créer le mécanisme séparé demandé par l'issue #33548, puisqu'un
champ optionnel sur l'entrée de route existante suffit sans surface nouvelle :

```
gateway:
  multiplex_profiles: true
  profile_routes:
    - name: teams-owner
      platform: teams
      user_id: "00000000-0000-0000-0000-000000000000"
      profile: owner
```

La tâche cron est délibérément exclue : une tâche planifiée n'a pas d'expéditeur
entrant authentifié, une route `user_id` ne doit donc jamais autoriser une
livraison au bot partagé, et le document le précise désormais explicitement. Le
diff de production compte quarante-cinq ajouts et vingt et une suppressions sur
huit fichiers, et les tests ajoutés vérifient notamment qu'un canal partagé
sépare trois expéditeurs sur trois profils et que l'identifiant est confronté
par égalité exacte, sensible à la casse et conjointement au `chat_id`.

> Sources : [@weiszfeld, Sender-based profile routing just landed upstream, 19 septembre 2026](https://x.com/weiszfeld/status/2101217377387974657) et [PR #106019, feat(gateway): route inbound messages to profiles by sender user_id, dépôt hermes-agent, 8 septembre 2026](https://github.com/NousResearch/hermes-agent/pull/106019)

## Hermes-Portal, une vitrine en lecture seule de l'installation

witcheer a relayé le 19 septembre une page web en lecture seule construite par
un membre de la communauté, rpmalouin, pour tout ce qu'une installation Hermes
conserve : les skills et l'emplacement de chacune, les conversations passées
avec recherche, le planificateur cron, le coût de chaque session, la mémoire,
les plugins et la santé du système, lus directement dans les fichiers et les
bases.

Le dépôt GitHub qui porte la page, intitulé Hermes-Portal, est public, sous
licence MIT et comptait 53 étoiles au moment de la consultation. Le projet a
d'abord porté le nom Hermes-Dashboard avant d'être renommé le 17 septembre pour
ne pas passer pour un second tableau de bord à côté de celui que Hermes déploie
déjà sur le port 9119. L'ensemble est testé par 518 tests, et un contrôle de
dérive, promu au rang de tâche d'intégration continue sur chaque poussée, monte
des montages d'une installation Hermes, chacun cassé comme une mise à jour
peut la casser, une colonne renommée, un stockage cron reformaté, un état
remplacé par des octets aléatoires, puis assure que le rendu reste vivant et
que seuls les éléments réellement affectés s'affichent comme tels, une
vérification qui a trouvé les trois derniers bogues. L'image de démonstration est issue d'un
appareil de capture livré dans le dépôt, de sorte que la capture est
reproductible en quatre commandes.

> Sources : [@witcheer, a Hermes Agent community member built a read-only web page for everything a Hermes install keeps, 19 septembre 2026](https://x.com/witcheer/status/2101279655281955219) et [Hermes-Portal, dépôt GitHub rpmalouin, licence MIT](https://github.com/rpmalouin/Hermes-Portal)

## La masterclass de l'application de bureau se conclut

tonbistudio a publié le 18 septembre la troisième et dernière partie de sa
masterclass vidéo consacrée à l'application de bureau de Hermes Agent. Dans
cette ultime partie, il parcourt les éléments propres à l'application : les
plugins, le tableau Kanban, les profils, le mode bot, le navigateur, le mode
HUD et d'autres.

La vidéo clôt une série annoncée en trois volets. Les deux premières parties ont
posé les bases de l'application ; cette dernière s'attache aux éléments qui la
distinguent du simple client de discussion.

> Sources : [@tonbistudio, Today's video is Part 3, the final part of my Hermes Desktop App Masterclass, 18 septembre 2026](https://x.com/tonbistudio/status/2100949462453817566)

## De nouveaux membres dans les équipes Hermes

Teknium a accueilli le 19 septembre deux nouveaux arrivants. Calvin rejoint
l'équipe Hermes Cloud en qualité d'ingénieur, et Mark intègre l'équipe Hermes
Core, le noyau du produit.

Les deux nouveaux membres se sont présentés. Mark a annoncé entamer un nouveau
parcours chez Nous Research au sein de l'équipe Hermes Agent, et Calvin a
expliqué rejoindre l'équipe Hermes Cloud après avoir passé ces derniers mois à
explorer ce que peut devenir une intelligence artificielle pleinement intégrée
au quotidien, à la maison comme au travail. Ces embauches traduisent la montée
en charge conjointe des deux lignes du produit, le noyau de l'agent et la
plateforme hébergée.

> Sources : [@Teknium, welcome to the newest Hermes Core team member, Mark, 19 septembre 2026](https://x.com/Teknium/status/2101105535592636726), [@Teknium, welcome to our newest Hermes Cloud engineer, Calvin, 19 septembre 2026](https://x.com/Teknium/status/2101106454606549459), [@mark_nerdspeak, joining the Hermes Agent team, 18 septembre 2026](https://x.com/mark_nerdspeak/status/2101073065719235065) et [@calvinnwq, joining the Hermes Cloud team, 18 septembre 2026](https://x.com/calvinnwq/status/2100773570351972515)

## Une routine matinale en un prompt

witcheer a partagé le 18 septembre un prompt qui donne à Hermes Agent une
routine matinale : un point sur les sujets suivis, avec un lien de source sur
chaque ligne, à l'heure choisie, chaque jour. Il suffit de coller le prompt
dans une nouvelle conversation et de répondre à deux questions pour en
lancer la mise en place.

> Sources : [@witcheer, this prompt gives your Hermes Agent a morning routine, 18 septembre 2026](https://x.com/witcheer/status/2100954266038829170)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)