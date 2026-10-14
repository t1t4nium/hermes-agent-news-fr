# Hermes Agent Quotidien #80

Cette édition revient sur la release v0.22.0, la plus grosse fenêtre jamais livrée par Hermes, sur les 92 pull requests fusionnées le 13 octobre, sur deux plugins de mémoire et de voix entrés au catalogue, sur le coup d'envoi de l'application mobile, et sur l'intégration de Petdex dans Herald OS.

## v0.22.0, la release du seuil

Nous Research a publié la release v0.22.0, datée du 13 octobre 2026 et baptisée The Threshold Release. C'est la plus grande fenêtre livrée par Hermes, environ 2,5 fois le cycle v0.21.0 : quelque 24 200 commits, environ 6 080 pull requests fusionnées, environ 15 600 fichiers modifiés, environ 7 180 issues fermées et environ 2 520 contributeurs. Elle rassemble et documente entièrement les releases de correctifs v0.21.1 à v0.21.7. Les temps forts :

- Un premier lancement qui se règle tout seul : une installation desktop neuve ouvre un court chat de configuration, carte par carte (nom, couleur d'accent, applications à connecter, plugins à installer), qui tourne sur un modèle d'essai gratuit (nous/welcome, une fois par utilisateur du système), sans clé d'API ; l'agent gagne aussi l'outil set_theme pour restyler l'application.
- Des connecteurs pour agir dans ses applications : Gmail, Linear et Notion passent par la passerelle d'outils Nous, avec une identité gratuite réservée aux connecteurs, une page Connecteurs dans Desktop, et plusieurs comptes nommés par application.
- Des modèles locaux en un clic : Hermes installe et entretient llama.cpp pour CPU, CUDA, Metal, Vulkan ou ROCm, note chaque modèle du catalogue selon le GPU et la RAM, et propose le plus lourd qui tient sur la machine, sans compte ni clé.
- Des canaux de release stables : des releases SemVer testées, suivies par défaut par les installations depuis les sources, avec hermes update --set-channel main pour rester sur chaque commit.
- Des paquets desktop signés et un gestionnaire de paquets unique : Windows passe en MSIX signé (x64 et ARM64), macOS en build signé et notarié, et hermes pm possède chaque outil épinglé avec mise à jour qui ne bascule qu'une fois vérifiée.
- Un catalogue de 600 plugins relus, chacun épinglé à un commit vérifié, avec déplacement des fournisseurs de mémoire et de Home Assistant, Spotify et Langfuse vers le catalogue.
- La vague de modèles Claude 5.5 et GPT-6 : Claude Fable 5.1, Opus, Sonnet et Haiku 5.5, GPT-6 Astra, Sol et Luna, GPT-6.1 Sol et Gemini 4 Argon, sur Nous Portal, OpenRouter et les routes natives.
- La connexion aux sites avec son gestionnaire de mots de passe : 1Password, Bitwarden et le coffre chiffré de Hermes, sans que le modèle voie jamais le mot de passe.
- Bot Screen : un bot sur une passerelle Linux peut avoir son propre écran diffusé en direct, et l'on reprend la main pour un login, une 2FA ou un CAPTCHA avant de lui rendre le contrôle.
- Un seul backend et une seule passerelle par machine pour tous les profils, au lieu d'un processus par profil, avec migration automatique des anciennes installations.
- Voir et piloter ses sous-agents en direct, avec leur tâche, leur temps écoulé et leur transcript, plus des boutons Steer et Stop.
- Un sélecteur de modèle qui connaît vos plans : favoris, abonnement qui s'épuise, date de levée d'une limite de débit, et choix de l'effort de raisonnement.
- Hermes dans votre langue, partout : un catalogue de traduction unique avec couverture complète des 16 langues embarquées, et des langues supplémentaires livrables en plugins.
- Plus léger en tout point : le code passe d'environ 1,06 million à 698 000 lignes (moins 34 %), gateway/run.py de 34 847 à 5 512 lignes, et environ 2 100 jetons quittent le prompt fixe.
- De petits conforts : touches vim en option dans le CLI, un champ de branche git dans la barre d'état, Ctrl+C qui efface le brouillon, et un mode Simple sur Desktop.

> Sources : [Hermes Agent v0.22.0, release GitHub NousResearch, 13 octobre 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v0.22.0)

## 92 pull requests fusionnées le 13 octobre

iamlukethedev a fait le compte le 14 octobre : Hermes a fusionné 92 pull requests le 13 octobre. Les changements mis en avant :

- L'onboarding de premier lancement arrive sur Desktop : un chat, set_theme et un nouveau backend, l'ancien flux de configuration agentique étant supprimé.
- Le modèle gratuit ne se débloque que sur une première installation desktop, pour que les relances restent sur le plan choisi.
- Gemini 4 Argon rejoint les modèles disponibles.

> Sources : [@iamlukethedev, Hermes merged 92 PRs on October 13, 14 octobre 2026](https://x.com/iamlukethedev/status/2110203103144464788)

## qdrant-memory, une mémoire durable en plugin

witcheer a signalé le 14 octobre que quelqu'un sur r/hermesagent a construit qdrant-memory, un plugin de mémoire à long terme pour Hermes Agent. Le LLM déjà configuré dans Hermes extrait des faits des conversations, avec déduplication et niveau d'importance, et une nouvelle session peut chercher ces souvenirs pour répondre depuis eux. Par défaut, ils vivent dans un Qdrant local.

La fiche du catalogue précise le mécanisme : le plugin, maintenu par cnkang, est épinglé à la version 0.2.1 et compatible avec Hermes 0.21.5 et au-delà. Il enregistre un fournisseur de mémoire natif plus quatre outils limités à leur périmètre (qdrant_memory_search, qdrant_memory_add, qdrant_memory_update et qdrant_memory_delete). Les souvenirs vont dans Qdrant, en mode embarqué, en serveur auto-hébergé ou sur Qdrant Cloud, avec des embeddings configurables (par défaut Ollama qwen3-embedding:4b en 2560 dimensions). Un journal d'admission SQLite en mode WAL rend chaque écriture idempotente et rejouable après redémarrage, et migrate mem0 importe les exports Mem0 existants.

> Sources : [@witcheer, someone on r/hermesagent built qdrant-memory, a long-term memory plugin, 14 octobre 2026](https://x.com/witcheer/status/2110302092913181172) et [qdrant-memory, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/qdrant-memory)

## Fish Audio, pour faire parler l'agent avec Drama 3

witcheer a expliqué le 13 octobre que Fish Audio est un plugin de Hermes Agent : hermes plugins install fish-audio --enable, puis hermes fish login et /fish model drama-3-preview. Les réponses vocales, la lecture à voix haute et les notes vocales passent par lui, dans le CLI comme dans les applications de messagerie.

L'annonce citée vient de Fish Audio : Drama 3 est présenté comme le modèle de synthèse vocale le plus expressif et contrôlable, open-weight, porté par une levée de 52 millions de dollars et plus de 15 millions d'utilisateurs. La fiche du catalogue détaille le plugin, maintenu par Electric Sheep, épinglé à la version 1.5.2 et compatible avec Hermes 0.21.6 et au-delà : synthèse vocale expressive dans plus de 80 langues, reconnaissance vocale, bibliothèque de voix communautaire, clonage et design de voix. Il ajoute les outils fish_speak, fish_voices et fish_transcribe, les commandes /fish et hermes fish, et trois skills.

> Sources : [@witcheer, Fish Audio is a plugin in Hermes Agent, so your agent can talk with Drama 3, 13 octobre 2026](https://x.com/witcheer/status/2110088528231047187), [@FishAudio, Introducing Drama 3, 13 octobre 2026](https://x.com/FishAudio/status/2110038429199450126) et [fish-audio, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/fish-audio)

## Le chantier de l'application mobile démarre

fl_rn_st a annoncé le 13 octobre rejoindre Nous Research pour construire le mobile, et Teknium lui a répondu en lançant le coup d'envoi de l'application mobile. La fiche de poste correspondante, Software Engineer, Mobile sur nousresearch.com/careers, décrit un poste à distance qui possède l'expérience téléphone de bout en bout : les applications iOS et Android natives, la couche cross-platform qui les sous-tend, et le backend qui rend l'agent rapide dans la poche. L'offre demande de livrer des applications iOS ou Android en production, en Swift ou Kotlin, et d'être à l'aise avec React Native.

> Sources : [@fl_rn_st, I'm joining @NousResearch to build mobile, 13 octobre 2026](https://x.com/fl_rn_st/status/2110120909566853515), [@Teknium, Welcome Florian, the mobile app kickoff begins, 13 octobre 2026](https://x.com/Teknium/status/2110143163939877187) et [Software Engineer, Mobile, nousresearch.com/careers](https://nousresearch.com/careers/software-engineer-mobile)

## Herald OS intègre Petdex

iamlukethedev a annoncé le 14 octobre que Herald OS est désormais intégré à Hermes Petdex : Teknium, la mascotte de Petdex, vit sur le bureau de Herald OS et devient utile. Elle montre ce sur quoi Hermes travaille, remonte les demandes d'approbation quand l'agent a besoin d'une permission, et l'on peut lui déposer un fichier pour lui demander quelque chose.

Herald OS est un système d'exploitation open source construit autour de l'agent, signé Luke The Dev : plutôt que de naviguer dans des menus et des dossiers, on parle ou on tape à Hermes, qui ouvre les applications, trouve et range les fichiers, surveille ce qui tourne, retient ce qui compte et exécute des routines planifiées. Le projet est indépendant, sans affiliation avec Nous Research, en alpha 0.1, et il ne fourche pas Hermes : il installe un Hermes standard et ajoute ses capacités système par le plugin herald-os-bridge, chaque action qui modifie quelque chose passant par un système de permission contrôlé par l'utilisateur.

> Sources : [@iamlukethedev, Herald OS is now integrated with Hermes Petdex, 14 octobre 2026](https://x.com/iamlukethedev/status/2110296899563749782) et [iamlukethedev/Herald-OS, dépôt GitHub](https://github.com/iamlukethedev/Herald-OS)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
