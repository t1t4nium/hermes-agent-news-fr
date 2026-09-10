# Hermes Agent Quotidien #46

Cette édition revient sur l'installation de plugins Hermes depuis des dépôts
privés, sur une couche communautaire posée au-dessus de l'agent qui décide de
chaque exécution, sur le conseil des Wingtips dédié aux skills appelées comme
commandes slash, sur les astuces intégrées affichées dans le bureau, et sur une
mesure des drapeaux de llama-server.

## Installer des plugins Hermes depuis un dépôt privé

Teknium a annoncé le 10 septembre qu'il est désormais possible d'installer des
plugins Hermes Agent depuis des dépôts privés, en utilisant les identifiants
GitHub déjà stockés.

La documentation des plugins précise le mécanisme. `hermes plugins install`
clone sans interaction et ne demande jamais d'identifiant, donc un dépôt privé
a besoin d'un jeton que Hermes trouve seul : pour une source `https://`, dans
l'ordre, `GITHUB_TOKEN` ou `GH_TOKEN` depuis `.env` (GitHub uniquement), la
connexion de la ligne de commande `gh` (`gh auth login`, GitHub uniquement),
puis l'assistant d'identifiants git (`git credential fill`) pour cet hôte, ce
qui couvre GitLab, Bitbucket et les serveurs auto-hébergés. Le jeton part en
en-tête HTTP à usage unique pour cette installation ou mise à jour, il n'est
jamais écrit dans le `.git/config` du plugin. Cette résolution s'applique aussi
à `hermes plugins update`, aux installations MCP depuis git et aux
distributions de profil tirées d'une URL git.

> Sources : [@Teknium, You can now install plugins in Hermes Agent from private repos!, 10 septembre 2026](https://x.com/Teknium/status/2097958504904736893) et [Plugins, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)

## oh-my-hermes, une couche communautaire au-dessus de Hermes

witcheer a présenté le 10 septembre une couche construite par un membre de la
communauté qui se place au-dessus de Hermes et décide de ce qui entre dans
chaque exécution : quel modèle et quel effort une tâche reçoit, quelles skills
spécialisées se chargent, et ce qui compte comme terminé. La mémoire est la
pièce distincte : un candidat part sur une carte de revue, on approuve, refuse
ou reporte en notant la raison, et chaque enregistrement approuvé conserve sa
provenance et sa date de revue. La mémoire propre de Hermes reste intacte.

Le dépôt `rlaope/oh-my-hermes` se présente comme un plugin tout-en-un pour
Hermes Agent portant intelligence de codage, système de mémoire à long terme et
paquets de workflows optimisés par modèle. Le projet se décrit comme la couche
d'exploitation posée au-dessus des skills natives : il cadre le problème, choisit
le workflow et les barrières de preuve, et exécute les skills natives comme
capacités à l'intérieur de ce chemin gouverné, sans jamais remplacer Hermes ni
masquer un exécuteur derrière lui. Le dépôt compte environ 1 600 étoiles, 140
fourches et vingt-deux contributeurs, pour une dernière release v2.0.2 datée du
7 septembre, sous licence MIT.

> Sources : [@witcheer, a Hermes Agent community member built a layer that sits on top of Hermes, 10 septembre 2026](https://x.com/witcheer/status/2098020649662816503) et [rlaope/oh-my-hermes, dépôt GitHub](https://github.com/rlaope/oh-my-hermes)

## Wingtips #68 : une skill s'appelle par sa commande slash

Dans le soixante-huitième numéro des Wingtips, witcheer répond à une situation
courante : on a installé une skill, dit à l'agent de l'utiliser, et les
réponses reviennent inchangées. Or chaque skill installée est aussi une
commande slash. `/humanizer rewrite this reply in my voice` charge la skill
pour ce tour de conversation puis exécute la demande avec elle ; le simple nom,
sans argument, la charge et laisse l'agent demander ce dont on a besoin.

Plusieurs skills s'empilent dans un même message : chaque `/skill` en tête de
ligne est chargé, le reste de la ligne devient l'instruction. Pour qu'une skill
soit choisie sans être nommée, l'agent lit un court index de toutes les
descriptions ; une description qui commence par les conditions d'usage est
retenue, une qui commence par le contexte ne l'est pas. La documentation des
skills confirme la portée : chaque skill installée est automatiquement
disponible comme commande slash, jusqu'à cinq s'empilent, et l'analyse s'arrête
au premier jeton qui n'est pas une skill installée.

> Sources : [@witcheer, Hermes Wingtips #68 : /skill-name, 10 septembre 2026](https://x.com/witcheer/status/2097944804084556003) et [Skills System, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)

## Des astuces affichées dans le bureau Hermes

witcheer a rappelé le 9 septembre avoir demandé à la communauté où elle
souhaitait découvrir les fonctions de Hermes ; la réponse qu'il a préférée :
à l'intérieur de l'agent, au moment où la fonction devient utile. Cette réponse
existe désormais dans Hermes Desktop grâce à Brooklyn, sous forme d'astuces
intégrées. L'agent peut pointer une seule chose à l'écran avec une petite bulle
pendant qu'il parle, comme il le fait juste après avoir bâti un plugin, sans
qu'on le demande ; l'application affiche aussi de temps en temps une astuce de
son cru, seulement quand on est au repos.

Brooklyn confirme la mécanique en construisant un plugin radio pour Hermes
Desktop, alimenté par nightride.fm, et en constatant que Hermes lui-même se sert
des astuces intégrées pour pointer vers ce plugin sans qu'elle ait eu à penser
à quoi que ce soit.

> Sources : [@witcheer, in-app tips in Hermes Desktop, 9 septembre 2026](https://x.com/witcheer/status/2097693322974208108) et [@imbabybrooklyn, Hermes Desktop Radio plugin powered by nightride.fm, 10 septembre 2026](https://x.com/imbabybrooklyn/status/2097906057473671394)

## Six drapeaux de llama-server mesurés de sang-froid

witcheer a mesuré le 10 septembre les six drapeaux de llama-server dont tout le
monde débat, sur un prompt de 16 mille jetons, sur six modèles dans sa carte
RTX 5090 : Qwen3.8-27B, Gemma 4 31B, Qwen3.6-35B-A3B, Nemotron Lightning,
Ornith 35B et Qwopus Flash. Le relevé tranche plusieurs querelles récurrentes.

`--flash-attn on` ne change rien, l'option auto le choisit déjà. `--parallel 1`
est gratuit et rend dix pour cent de décodage en profondeur sur Gemma en
rendant 2,3 gigaoctets. Le cache KV en q8 est un levier de mémoire sur les
modèles denses uniquement, de 1 à 2,6 gigaoctets ; sur un MoE à 3 milliards
d'actifs il n'économise que 0,1 gigaoctet et coûte encore cinq à sept pour
cent. Le cache KV en q4 est la taxe : moins dix-sept, vingt-trois, vingt-sept,
vingt-trois, vingt-neuf et dix-sept pour cent de décodage sur un contexte de 16
mille, six sur six, sans perte de qualité au relevé GPQA (Ornith en f16, q8 et
q4 à 100, 100 et 98). La tête de brouillon MTP accélère par 2,2 sur Qwen3.8
(tête embarquée), 1,5 sur Gemma (tête communautaire), 0,7 sur Lightning, et
au-dessus de trois cents jetons par seconde la passe de vérification coûte plus
qu'elle ne rapporte. Le premier jeton sur un prompt de 16 mille met cinq à six
secondes à froid, 0,1 à 0,4 seconde une fois mis en cache.

> Source : [@witcheer, I measured the six llama-server flags everyone argues about, 10 septembre 2026](https://x.com/witcheer/status/2097921422005879100)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi
que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).