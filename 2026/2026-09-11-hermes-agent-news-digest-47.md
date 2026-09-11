# Hermes Agent Quotidien #47

Cette édition revient sur la rencontre Hermes Power Users Berlin du 23 septembre,
sur le pilotage en direct des sous-agents, sur l'arrivée de DeepSeek V4.1 Flash
dans Hermes, sur les garde-fous de boucle d'outils du soixante-neuvième Wingtips,
sur le mode commentaire du navigateur du bureau, sur la configuration Telegram
par QR code, sur un kit communautaire qui habille la flotte de bots et sur un
prompt qui transforme une session en skill.

## Nous Research soutient une rencontre Hermes à Berlin

witcheer a annoncé le 11 septembre que Nous Research soutient des événements
communautaires, et que Berlin est le prochain. Le 23 septembre, cinquante
personnes qui utilisent Hermes au quotidien se retrouvent dans une salle à
Kreuzberg, avec du merchandising Nous Research et un temps de travail consacré
à ce que devient Nous x Berlin ensuite. L'invitation vise celles et ceux qui
utilisent déjà Hermes et peuvent en parler d'expérience, et propose de se
signaler pour accueillir le même format ailleurs.

La page d'inscription, tenue par le calendrier Circuit, détaille le déroulé. Le
lieu est le rez-de-chaussée de Circuit, Möckernstraße 120, dans l'arrondissement
de Friedrichshain-Kreuzberg. Les portes ouvrent à 17 h 50, les présentations
éclair commencent à 18 h et donnent soixante secondes à chacun pour dire ce
qu'il fait de Hermes, puis les échanges libres en petits groupes par cas
d'usage, boissons comprises, embarquent une séquence de planification sur la
forme à donner à une collaboration entre Nous Research et Berlin : soirées
hack, permanences, rencontre régulière, ou autre chose. La soirée se termine à
20 h. La salle est plafonnée à cinquante places et l'inscription est soumise à
approbation, avec deux à trois phrases à écrire sur son usage de Hermes et ses
attentes de format. La page précise qu'aucun intervenant de Nous Research ne
monte sur scène et que l'événement ne s'adresse pas aux personnes qui n'ont pas
encore installé Hermes.

> Sources : [@witcheer, Nous Research supports community events and Berlin is the next one!, 11 septembre 2026](https://x.com/witcheer/status/2098426560730603982), [@circuit_ber, AI agents are everywhere. Very few actually master them, 11 septembre 2026](https://x.com/circuit_ber/status/2098362753765302430) et [Hermes Power Users Berlin, page d'inscription, Circuit](https://luma.com/hermesberlin)

## Les sous-agents visibles et pilotables en direct

Nous Research a annoncé le 10 septembre que Hermes Agent affiche désormais le
détail de l'activité de tous les sous-agents en direct, et qu'on peut les
piloter et les arrêter à la main depuis le CLI et l'application bureau. Teknium
a repris l'annonce comme une grande amélioration de l'observabilité et de la
gestion des sous-agents, et witcheer en a précisé la mécanique : chaque
travailleur siège dans la conversation elle-même, avec sa tâche en cours, son
temps écoulé et deux commandes à côté de lui. Le pilotage envoie une correction
à un travailleur en cours sans le tuer ; l'arrêt le termine plus tôt et le
résultat partiel remonte quand même. Le CLI et le bureau partagent cette vue.

La documentation de la délégation décrit les surfaces et les raccourcis. Dans
le CLI classique, le TUI et le bureau, une zone au-dessus du composeur montre le
nombre de travailleurs vivants, leurs noms de tâche, le temps écoulé et leur
dernière activité, le bureau en prévisualisant trois. Dans le CLI classique,
Ctrl+T ou F6 ouvre la liste plein écran, les flèches sélectionnent, Entrée
ouvre la fin de la transcription, `s` ouvre une saisie de pilotage séparée et
`x` puis `y` demande l'arrêt. Le TUI affiche un arbre de même ampleur avec
Ctrl+T ou `/agents`, `e` pilote le travailleur sélectionné, `x` l'arrête et `X` arrête
son sous-arbre. Dans le bureau, on déplie Subagents au-dessus du composeur, puis
on sélectionne un travailleur pour inspecter son activité et ses détails, avec
les commandes Steer et Stop. Le pilotage accuse réception d'une consigne mise en
file, consommée par l'enfant à un point de contrôle, et non d'une lecture
immédiate ; l'arrêt n'interrompt pas les travailleurs voisins. L'overlay
`/agents` du TUI ajoute l'arbre vivant groupé par parent, les cumuls de coût, de
jetons et de fichiers touchés par branche, les commandes d'arrêt et de pause, et
la relecture d'un sous-agent déjà rendu, tour par tour.

> Sources : [@NousResearch, Hermes Agent now displays detailed information on all subagent activities live, 10 septembre 2026](https://x.com/NousResearch/status/2098071687145365632), [@Teknium, Big upgrade for subagent observability and management in Hermes Agent, 10 septembre 2026](https://x.com/Teknium/status/2098073618144260505), [@witcheer, Hermes Agent workers now sit in the conversation itself, 10 septembre 2026](https://x.com/witcheer/status/2098075308654006710) et [Subagent Delegation, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)

## DeepSeek V4.1 Flash disponible dans Hermes

Teknium a indiqué le 10 septembre que DeepSeek Flash V4.1 est en service dans
Hermes Agent via le Nous Portal et d'autres fournisseurs, et l'a qualifié le
lendemain de modèle extrêmement puissant.

DeepSeek a présenté V4.1 Flash le 10 septembre comme le plus petit modèle de sa
nouvelle famille d'architecture, doté d'une compréhension visuelle native et
conçu pour plus de capacité, une inférence plus rapide, un débit plus élevé et
une montée en échelle vers de plus grands modèles. Le fil de présentation décrit
un mélange d'experts de 552 milliards de paramètres, une architecture
encodeur-décodeur causale qui n'active que 8 milliards de paramètres en entrée
et 16 milliards en sortie, de nouvelles méthodes de pré-entraînement et un
post-entraînement par apprentissage par renforcement à plus grande échelle, pour
des résultats de référence qui devancent les modèles phares, DeepSeek-V4-Pro
compris. Le sujet prolonge les modèles déjà signalés comme disponibles dans
Hermes par ce quotidien.

> Sources : [@Teknium, Deepseek Flash V4.1 is now live in Hermes Agent through Nous Portal and others!, 10 septembre 2026](https://x.com/Teknium/status/2098088984383725725), [@Teknium, Deepseek V4.1 Flash is an incredibly powerful model!, 11 septembre 2026](https://x.com/Teknium/status/2098325692278780291), [@deepseek_ai, Introducing DeepSeek-V4.1-Flash, 10 septembre 2026](https://x.com/deepseek_ai/status/2097930608790167907) et [@deepseek_ai, Asymmetric architecture, 10 septembre 2026](https://x.com/deepseek_ai/status/2097930613101838709)

## Wingtips #69 : les garde-fous de boucle d'outils

Dans le soixante-neuvième numéro des Wingtips, witcheer décrit le cas où l'agent
ouvre un fichier, le lit, décide de repartir de zéro et relit le même fichier.
Hermes Agent compte ces répétitions à l'intérieur d'un tour, en surveillant trois
motifs : le même appel qui échoue deux fois de suite, le même outil qui échoue
sur de nouveaux arguments, et un appel qui revient avec le même résultat alors
que rien n'a changé. Quand un seuil est atteint, l'avertissement est écrit dans
le résultat de l'outil lui-même, de sorte que le modèle le lit à l'étape
suivante et change de trajectoire.

Dans le CLI, le TUI et l'application bureau, l'affaire s'arrête là, puisqu'une
personne est là pour intervenir. Les exécutions en passerelle et en cron vont un
cran plus loin et coupent le tour, faute de témoin : l'arrêt met fin au tour et
non à la session, et l'agent indique quel motif a déclenché. La documentation de
configuration confirme le mécanisme et ses valeurs. Les avertissements sont
actifs par défaut ; les arrêts durs ne le sont pas sur les surfaces interactives,
mais ils le sont par défaut pour la passerelle et le cron, et l'activation
explicite partout se fait par `tool_loop_guardrails.hard_stop_enabled`. Les
seuils d'avertissement sont de 2 sur l'échec identique, 3 sur l'échec du même
outil et 2 sur l'absence de progrès, les seuils d'arrêt dur de 5, 8 et 5. Deux
plafonds par tour s'ajoutent, toujours actifs, à 50 recherches web et 50
sous-agents. Un dernier garde-fou, le `identical_call_streak_halt`, transforme en
arrêt dur une série d'appels identiques qui réussissent, quel que soit l'outil.

> Sources : [@witcheer, Hermes Wingtips #69 : tool_loop.guardrails, 11 septembre 2026](https://x.com/witcheer/status/2098290534758408306) et [Configuration, Tool-Loop Guardrails, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#tool-loop-guardrails)

## Un mode commentaire dans le navigateur du bureau

witcheer a montré le 11 septembre le mode commentaire du navigateur intégré à
Hermes Desktop. On ouvre une page, on active Comment, on clique l'élément à
corriger et on tape une note ; les épingles s'empilent au fil des remarques.
Ensuite, Add comments dépose chaque épingle dans le composeur sous forme de
capture recadrée accompagnée de la note, et pour un élément, la sélection, le
balisage et les styles sont joints aussi, ce qui permet à l'agent de retrouver
l'élément dans le code source au lieu de deviner à partir de l'image.

La documentation du bureau ajoute les détails qui comptent pour l'usage. Le
bouton s'appelle Annotate dans la barre du navigateur de prévisualisation, on
peut cliquer un élément ou tracer un cadre, et enregistrer une épingle n'envoie
jamais de tour : c'est le bouton Add N comments qui transmet le lot, l'envoi
restant à la main de l'utilisateur. Les valeurs des champs de mot de passe et
des champs masqués, ainsi que tout attribut qui ressemble à une clé ou à un
jeton, sont masqués sur la page avant que le balisage ne quitte celle-ci. Les
lots importants arrivent groupés par zone de la page, de sorte qu'une vingtaine
de commentaires devient une poignée de travaux, et comme ces groupes occupent
des sous-arbres DOM distincts ils touchent en général des fichiers distincts,
ce qui rend leur répartition entre travailleurs parallèles sûre. La
numérotation des épingles reste stable après suppression, et changer de
conversation vide la pile.

> Sources : [@witcheer, Hermes Desktop has a comment mode in its built-in browser, 11 septembre 2026](https://x.com/witcheer/status/2098392396425769186) et [Hermes Desktop, Chat, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)

## La configuration Telegram par QR code dans le bureau

Tony Simons a relevé le 10 septembre que la mise en place de Telegram dans
Hermes Desktop tient maintenant en un scan : la page Messaging puis Telegram
propose une configuration rapide par QR code, le code est scanné, et Hermes
s'occupe du reste. La documentation des passerelles confirme l'enchaînement. Le
bouton Create with QR est présent sur la page Messaging puis Telegram du tableau
de bord et de l'application bureau ; après le scan dans Telegram, Hermes crée
le bot, détecte l'identifiant Telegram de l'utilisateur, écrit
`TELEGRAM_BOT_TOKEN` et `TELEGRAM_ALLOWED_USERS` dans le fichier `.env` du
profil, puis redémarre la passerelle. La documentation du bureau ajoute qu'une
bannière Restart now reste affichée après l'enregistrement, l'effacement ou la
bascule d'un identifiant, tant que la passerelle n'a pas réellement redémarré,
et qu'elle persiste en cas d'échec pour permettre de réessayer.

> Sources : [@tonysimons_, Hermes Agent just made Telegram setup almost stupidly easy, 10 septembre 2026](https://x.com/tonysimons_/status/2098055240331215335), [Telegram, Quick setup, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram) et [Hermes Desktop, Management panes, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)

## hermes-bot-kit, un habillage communautaire de la flotte de bots

witcheer a présenté le 11 septembre un kit construit par un membre de la
communauté, qui change deux choses dans l'usage des bots de Hermes Desktop. La
première porte sur la conversation : la discussion principale d'un bot affiche
normalement chaque appel d'outil et chaque minuteur à côté des messages, alors
que le kit ne garde que les messages, en laissant passer les demandes
d'approbation et les messages entre bots. La seconde porte sur l'écran : quand
un bot se met au travail sur une machine, une vue en direct du bureau de cette
machine s'ouvre dans un panneau du bureau Hermes, et on passe d'une machine
cloud à un Mac de réserve ou à une machine Linux ; un greffon optionnel laisse
en plus le bot taper, cliquer et lancer des commandes à cet endroit. Le tout
s'installe sous forme de fichiers simples, sans étape de compilation.

Le dépôt `thomasbek3/hermes-bot-kit` détaille le contenu : cinq greffons, dont
Bubble Mode pour les bulles façon messagerie avec indicateur de saisie et
masquage du bruit d'outils, la vue Computer pour le bureau distant qui se
connecte dès que le bot prend sa machine, des sections nommées dans la liste des
bots, une liste de tâches épinglée au-dessus du composeur, et texting-style, un
greffon d'agent qui fait répondre les bots dans ce registre. Les greffons de
bureau sont des fichiers uniques, sans modification du cœur, rechargeables à
chaud et conçus pour retomber proprement sur l'affichage d'origine si une mise à
jour renomme les points d'accroche internes. Le projet demande Hermes Desktop
0.20.5 ou plus récent, se présente comme indépendant de Nous Research, et porte
66 étoiles, 10 fourches et 133 commits pour une dernière release v2026.09.07.2
datée du 7 septembre, sous licence MIT. Le dépôt a été renommé le 27 août 2026
en absorbant l'ancien `hermes-bubble-mode`.

> Sources : [@witcheer, a Hermes Agent community member built a kit that changes two things about running bots in Hermes Desktop, 11 septembre 2026](https://x.com/witcheer/status/2098361620493660493) et [thomasbek3/hermes-bot-kit, dépôt GitHub](https://github.com/thomasbek3/hermes-bot-kit)

## Transformer une session terminée en skill

witcheer a proposé le 10 septembre un prompt à recoller dans la conversation qui
vient de produire un travail réutilisable. L'agent relit la session, rédige une
skill à partir des étapes qui ont fonctionné, dans leur ordre, en y ajoutant les
pièges rencontrés, et montre le brouillon avant tout enregistrement. Sur accord,
le brouillon devient une commande slash réutilisable la prochaine fois. Le
prompt lui-même est placé dans la première réponse sous la publication.

> Source : [@witcheer, finished a task with your Hermes Agent that you will need again?, 10 septembre 2026](https://x.com/witcheer/status/2098058859189277008)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
