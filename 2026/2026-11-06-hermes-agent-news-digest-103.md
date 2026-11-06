# Hermes Agent Quotidien #103

Cette édition revient sur la release v0.23.0 « The Hearth Release », la plus grosse fenêtre depuis v0.22.0, sur un Echo Dot recyclé en enceinte vocale Hermes via Home Assistant, et sur les premiers correctifs fusionnés le 6 novembre.

## Hermes v0.23.0 « The Hearth Release »

Le 5 novembre, Nous Research a publié Hermes v0.23.0, baptisée « The Hearth Release ». C'est la plus grosse fenêtre depuis « The Threshold Release » (v0.22.0) : environ 10 080 commits, 1 950 pull requests fusionnées, 850 issues fermées et 666 contributeurs, le catalogue passant d'environ 600 à plus de 1 050 plugins. La note roule et documente entièrement les releases correctives v0.22.1 à v0.22.7. Les points marquants :

- La Webapp sert tout l'espace de travail Desktop dans un onglet de navigateur, depuis sa propre passerelle ; elle reste désactivée tant que `webapp.enabled` ou Web Access n'est pas activé.
- Une seule passerelle possède désormais chaque session : le CLI, la TUI, Desktop, les éditeurs, les bots et les tâches cron s'y rattachent au lieu de lancer chacun leur propre agent.
- Les images collées et les captures s'affichent en ligne dans le terminal : vrais pixels sous kitty et Ghostty, blocs colorés ailleurs, pleine résolution dans VS Code.
- `/rewind` (ou deux fois Échap) remonte à un message précédent pour le modifier et le renvoyer, ou pour forker une nouvelle session ; la TUI peut lancer `/new` pendant qu'un tour tourne encore.
- Desktop garde toutes les passerelles connectées et bascule instantanément entre la machine locale, un hôte SSH ou une passerelle distante.
- Les Group Chats se gèrent tout seuls : un bot chef de file ou un routeur automatique choisit qui répond à un message qui ne nomme personne, et les bots cessent de se relancer en boucle.
- `hermes plugins update` met tous les plugins à jour d'un coup, et un interrupteur Auto-update maintient les plugins du catalogue et git à jour.
- Les outils MCP payants déclarent le coût de chaque appel ; Hermes affiche le prix et le total en cours, et demande avant de dépasser la limite du chat, même en mode YOLO.
- De nouveaux plugins officiels arrivent, dont Meshy, ElevenLabs Music et Sound Effects, X Chat, REA et bubblewrap, pendant que Camofox, mcp-serve, les importateurs et Singularity quittent le cœur.
- La délégation devient modulable : le plugin `advanced-delegation` envoie chaque sous-tâche vers un modèle nommé ou un profil séparé.
- Plus léger et plus rapide : cache de prompt partagé entre tâches cron, 1 570 jetons de prompt en moins par appel, et `patch` comme `write_file` répondent en millisecondes avec LSP activé.
- Le jeu de skills intégré passe de 58 à 44, avec Word, PowerPoint et Excel réunis dans `microsoft-office`, et `hermes curator lock` empêche l'agent de réécrire une skill éditée à la main.

La release impose quelques migrations. Les anciens outils de navigateur intégrés disparaissent au profit de `browser_exec`, et les homes qui utilisaient Camofox reçoivent le plugin automatiquement. Desktop passe à Electron 44, ce qui abandonne macOS 11, macOS 12 et Windows 32 bits. `hermes mcp serve` devient `hermes mcp-serve`. Enfin, la Webapp reste désactivée par défaut tant que rien n'est explicitement servi au navigateur.

Teknium a annoncé la release en soulignant la Webapp comme nouveauté de tête. iamlukethedev a fait le compte de la fenêtre, et tonbistudio a publié une vidéo d'explication de moins de cinq minutes, relayée par witcheer, qui a par ailleurs répondu aux questions posées sous la release.

> Sources : [Hermes Agent v0.23.0, note de release GitHub, 5 novembre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.0), [@NousResearch, Hermes Agent v0.23.0: The Hearth Release, 5 novembre 2026](https://x.com/NousResearch/status/2118479744979079669), [@Teknium, Hermes Agent v0.23 was just released, 5 novembre 2026](https://x.com/Teknium/status/2118481079728493015), [@iamlukethedev, Hermes v0.23.0 is absolutely massive, 6 novembre 2026](https://x.com/iamlukethedev/status/2118494648478142926), [@tonbistudio, Many great improvements in this latest Hermes Agent release, 6 novembre 2026](https://x.com/tonbistudio/status/2118512292178571759) et [@witcheer, the new Hermes Agent release is here, 6 novembre 2026](https://x.com/witcheer/status/2118596128279072991)

## Un Echo Dot recyclé en enceinte Hermes

Le 5 novembre, 0xdippo a montré un Echo Dot transformé en enceinte Hermes. Il a bâti une intégration Home Assistant qui relie l'appareil à un profil Hermes, avec sa mémoire et ses outils : on dit « hey hermes » et l'agent répond. Le versant Home Assistant est une skill, que l'agent installe et utilise lui-même.

Le projet, publié sous le nom hermes-voice (majorminorlabs), regroupe trois morceaux : le composant custom_components/hermes_voice, qui sert d'agent conversationnel Home Assistant pour un profil, la skill hermes-voice-setup qui met tout en place, et un modèle de mot de réveil « hey hermes » avec le pipeline qui l'a entraîné. Le code est sous licence MIT, mais le modèle de mot de réveil est réservé à un usage non commercial. L'auteur mesure environ 3,5 secondes par tour simple, presque entièrement dues au modèle. witcheer a relayé la démonstration.

> Sources : [@0xdippo, My old Echo Dot run Hermes now, instead of Alexa, 5 novembre 2026](https://x.com/0xdippo/status/2118355830882132184), [@witcheer, someone in the community turned an old Echo Dot into a Hermes Agent speaker, 5 novembre 2026](https://x.com/witcheer/status/2118377802093166887) et [majorminorlabs/hermes-voice, dépôt GitHub](https://github.com/majorminorlabs/hermes-voice)

## Les premiers correctifs du 6 novembre

Le changelog du 6 novembre recense 13 pull requests fusionnées au moment de la collecte. Parmi les changements visibles :

- `/undo` liste désormais les fichiers modifiés par les tours annulés, et `/rollback` ne supprime plus le dernier tour conservé (#149630).
- Un refus du filtre de sécurité ne bloque plus le chat : le message reste à l'écran mais sort de la mémoire du modèle (#149708).
- Les plugins gagnent des méthodes JSON-RPC et des événements liés à la session, ainsi qu'un identifiant de conversation stable après compression (#142005, #142007).
- Les clients locaux peuvent se rattacher à la passerelle avec `hermes gateway attach --json` (#142166).
- Les workspaces JavaScript passent de npm à pnpm (#149746).

> Sources : [Hermes Bible, changelog du 6 novembre 2026](https://www.hermesbible.com/changelog?date=2026-11-06) et [NousResearch/hermes-agent, pull requests fusionnées le 6 novembre 2026](https://github.com/NousResearch/hermes-agent/pulls?q=is%3Apr+merged%3A2026-11-06)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
