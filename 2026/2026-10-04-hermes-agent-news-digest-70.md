# Hermes Agent Quotidien #70

Cette édition revient sur le numéro 91 des Wingtips consacré à l'envoi de fichiers sur Telegram, sur la sortie du SDK Hermes Gadget pour petits appareils vocaux ESP32, sur les 144 pull requests fusionnées le 3 octobre, sur la configuration de Discord simplifiée, et sur un plugin Stream Deck réalisé par la communauté.

## Wingtips #91 : envoyer des fichiers sur Telegram

witcheer a consacré le numéro 91 des Wingtips à l'envoi de fichiers sur Telegram. L'agent ne se limite plus au texte : il suffit de demander le format souhaité dans le message, par exemple « send me that as a PDF », et Hermes crée le fichier puis l'envoie. L'usage visé est de lire un document plus tard sur son téléphone ou de le transférer à quelqu'un.

La documentation Telegram précise la mécanique : la passerelle extrait les balises `MEDIA:/chemin/vers/fichier` des réponses de l'agent et expédie le fichier référencé comme pièce jointe native de la plateforme. Les extensions prises en charge couvrent les images, l'audio, la vidéo, les documents (pdf, txt, md, csv, json, etc.), les archives et les livres. L'API Bot publique de Telegram plafonne les téléchargements à 20 Mo ; un démon local telegram-bot-api relève ce plafond à 2 Go, et Hermes ajuste automatiquement sa limite interne dès qu'un `base_url` est configuré.

> Sources : [@witcheer, Hermes Wingtips #91: files in your Telegram chat, 4 octobre 2026](https://x.com/witcheer/status/2106632278839337357) et [Telegram, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)

## Hermes Gadget, un SDK ouvert pour appareils vocaux ESP32

adolandev a présenté le 4 octobre Hermes Gadget, un SDK ouvert pour petits appareils qui dialoguent avec son propre Hermes. Le principe tient dans son slogan : maintenir un bouton, poser sa question, écouter la réponse. On parle, Hermes écoute, réfléchit et répond à voix haute, pendant que l'écran montre ce qu'il est en train de faire ; s'il a besoin d'une autorisation, il la demande directement sur l'appareil. Teknium a salué la sortie d'un sobre « We got ESP32 at home ».

Le dépôt hermes-gadget-sdk, publié en version v0.1.0 le 4 octobre, détaille le projet : un cœur d'appareil portable en C++17 avec un portage firmware ESP32 et un simulateur de bureau, un plugin de plateforme Hermes (concentrateur d'appareils, adaptateur de passerelle, outils de l'agent), le protocole de communication, l'outillage et la documentation. L'appareil se couple comme un téléphone : il affiche un code que l'on approuve sur l'hôte Hermes, puis s'authentifie avec sa propre clé. Il déclare ses actions (LED, relais, buzzer) que Hermes peut déclencher, et peut afficher des cartes et lire des capteurs. Le plugin s'installe via `hermes plugins install` et s'intègre à `hermes gateway setup` ; un installateur dans le navigateur, publié via GitHub Pages, flashe le firmware en Web Serial avec esptool-js. Le projet se présente comme non officiel et non affilié à Nous Research.

> Sources : [@adolandev, Hermes Gadget is an open SDK for a small device..., 4 octobre 2026](https://x.com/adolandev/status/2106624035090059630), [@Teknium, We got ESP32 at home, 4 octobre 2026](https://x.com/Teknium/status/2106632146484162773) et [Adolanium/hermes-gadget-sdk, dépôt GitHub](https://github.com/Adolanium/hermes-gadget-sdk)

## 144 pull requests fusionnées le 3 octobre

iamlukethedev a fait le compte le 4 octobre : Hermes a fusionné 144 pull requests le 3 octobre. Deux entrées figurent dans le texte du message, le reste de la liste étant détaillé dans la capture jointe :

- Desktop traite Ultrafast comme un niveau de vitesse à part entière, et la fonction keep-awake peut ne maintenir la machine éveillée que pendant le travail.
- Les bots de Desktop conservent l'identité de chaque backend à travers les démarrages à froid, les reconnexions et les noms de profils partagés.

> Source : [@iamlukethedev, Hermes merged 144 PRs on October 3, 4 octobre 2026](https://x.com/iamlukethedev/status/2106621938118578278)

## La configuration de Discord devient plus simple

Teknium a annoncé le 4 octobre que configurer son Hermes avec Discord devrait être un peu moins déroutant et douloureux. witcheer, gros utilisateur de Discord, y voit une très bonne mise à jour pour son agent.

La documentation Discord précise le raccourci : après avoir créé l'application et copié le jeton du bot, `hermes gateway setup` vérifie le jeton auprès de Discord, signale si l'intention Message Content Intent est désactivée (avec un lien direct vers le réglage), affiche un lien d'invitation prêt à l'emploi pour le serveur et ajoute l'utilisateur à la liste des personnes autorisées, sans passer par le Developer Mode. Cette intention est la première cause des bots qui ne démarrent pas : sans elle, Discord refuse la connexion.

> Sources : [@Teknium, Setting up your Hermes with Discord should now be a little less confusing or painful, 4 octobre 2026](https://x.com/Teknium/status/2106563883058274541), [@witcheer, as a Discord heavy user, this is a wonderful update, 4 octobre 2026](https://x.com/witcheer/status/2106615308781797813) et [Discord, documentation Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)

## Un plugin Stream Deck réalisé par la communauté

witcheer a présenté le 3 octobre un plugin Stream Deck pour Hermes Agent réalisé par la communauté. Trois actions sont décrites dans le message : Start Run envoie un prompt enregistré à l'agent et affiche l'exécution en direct sur la touche, Steer Run ajoute une consigne pendant que l'agent travaille, et Stop Run met fin à l'exécution. Les prompts peuvent venir du presse-papiers ou d'un petit champ de saisie.

> Source : [@witcheer, a Stream Deck plugin for Hermes Agent, made by the community, 3 octobre 2026](https://x.com/witcheer/status/2106477981400957422)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
