# Hermes Agent Quotidien #94

Cette édition revient sur les nouveaux abonnements Hermes Agent qui incluent un agent cloud, sur les 61 pull requests fusionnées le 27 octobre, sur le plugin officiel ElevenLabs SFX pour générer des bruitages, sur un agent doté de son propre compte GitHub, sur le conseil Wingtips #112 consacré aux tâches planifiées uniques et sur Ornith 1.5 122B qui tient sur une seule carte.

## Nouveaux abonnements, un agent cloud inclus

Nous Research a annoncé le 27 octobre la refonte des abonnements Hermes Agent. Chaque nouveau plan payant inclut désormais un agent cloud dès le départ, toujours allumé, sans laisser l'ordinateur portable ouvert. La consommation ne se compte plus en un bloc de crédits mensuel : elle passe sur des limites quotidiennes et hebdomadaires, auxquelles s'ajoute une allocation mensuelle. Les abonnés peuvent basculer vers les nouveaux plans à tout moment depuis la page de facturation du portail.

Teknium précise que tous les paliers payants du Nous Portal reçoivent une instance Hermes Agent et l'ordinateur qui va avec, avec une connexion en un clic depuis l'application Desktop et les applications de messagerie. witcheer écrit depuis un avion, son agent sur Hermes Cloud à l'œuvre malgré un wifi exécrable, et relève que l'agent cloud arrive avec chaque nouveau plan. iamlukethedev résume le changement : hébergement d'un agent cloud inclus, limites quotidiennes et hebdomadaires, et des prix revus à la hausse.

> Sources : [@NousResearch, We've revamped Hermes Agent subscriptions, 27 octobre 2026](https://x.com/NousResearch/status/2115120531611787323), [@Teknium, All nous portal paid tier subs now come with a Hermes Agent instance, 27 octobre 2026](https://x.com/Teknium/status/2115128618372522495), [@witcheer, that cloud agent now comes with every new Hermes Agent plan, 27 octobre 2026](https://x.com/witcheer/status/2115125992528171248), [@iamlukethedev, Hermes Agent plans just changed, 28 octobre 2026](https://x.com/iamlukethedev/status/2115234013707460741) et [Nous Portal, page facturation](https://portal.nousresearch.com/billing)

## 61 pull requests fusionnées le 27 octobre

Le changelog du 27 octobre relève 61 pull requests fusionnées. Les changements à retenir :

- Les réglages de Desktop et de la Webapp (thème, mode) se suivent désormais d'une fenêtre à l'autre sur la même machine.
- Le bouton de nouvelle session réutilise l'onglet brouillon vide au lieu d'en ouvrir un second.
- Les plugins Desktop peuvent se charger dans un onglet du navigateur, pour les développer et les tester sans application séparée.
- Après un redémarrage, le CLI indique que le dernier message n'est pas parti et donne la commande exacte pour reprendre.

Le même changelog relève aussi des correctifs de sécurité : en mode sans jeton, les requêtes venues d'un navigateur ou d'un hôte étranger sont refusées, et le contrôle d'URL écarte les adresses dont l'autorité se lit différemment selon les clients. Un message envoyé juste avant de fermer Desktop n'est plus perdu, et les mises à jour de Desktop ne cassent plus sur un gros state.db, les locales à virgule ou GNU date.

> Source : [Hermes Bible, changelog du 27 octobre 2026](https://www.hermesbible.com/changelog?date=2026-10-27)

## ElevenLabs SFX, des bruitages depuis Desktop

Teknium a présenté le 27 octobre le plugin officiel ElevenLabs SFX, qui poursuit la suite de capacités Game Dev Studio pour Hermes Agent. Nous Research résume l'usage : générer des effets sonores depuis Hermes Desktop, avec lecture en boucle, variations en un clic et une bibliothèque de tous les sons produits. witcheer, qui avait fait construire la semaine dernière un chevalier canard en 3D avec le plugin Meshy, note que l'agent peut maintenant en faire les bruits.

Le catalogue précise le fonctionnement. Le plugin ajoute un unique outil, elevenlabs_sound_effect, qui transforme une description texte en fichier audio de 0,5 à 30 secondes, en boucle parfaite si demandé. Il exige la clé ELEVENLABS_API_KEY, la même que pour la voix ElevenLabs. Il livre une skill de sound design et un script local qui normalise le volume, coupe les silences et emballe un pack avec manifest.json et zip via ffmpeg. Dans Desktop, chaque son s'affiche en carte avec forme d'onde, lecture en boucle et variantes, et une bibliothèque ouverte par raccourci liste tous les sons du profil. Installation : hermes plugins install elevenlabs-sound-effects. Chaque génération est facturée par ElevenLabs, environ 10 crédits par seconde quand la durée est fixée, ou un montant forfaitaire sinon.

> Sources : [@Teknium, Introducing the ElevenLabs SFX plugin, 27 octobre 2026](https://x.com/Teknium/status/2115219694622040322), [@NousResearch, Generate SFX with ElevenLabs straight from Hermes Desktop, 27 octobre 2026](https://x.com/NousResearch/status/2115220372228612579), [@witcheer, now it can make the sounds for it too, 27 octobre 2026](https://x.com/witcheer/status/2115223501300744623) et [elevenlabs-sound-effects, catalogue de plugins Hermes Agent](https://hermes-agent.nousresearch.com/docs/plugins/elevenlabs-sound-effects)

## Un compte GitHub pour l'agent

witcheer a montré le 28 octobre une façon de donner du travail à son agent : lui ouvrir son propre compte GitHub et le mentionner dans une issue ou un commentaire de pull request. lu4p_ l'utilise ainsi. Sur un rapport de bug de son lanceur Android, il a écrit « please fix », et le bot est revenu avec une correction, des tests et des captures d'écran de l'émulateur.

> Source : [@witcheer, your Hermes Agent can have its own GitHub account, 28 octobre 2026](https://x.com/witcheer/status/2115447242396176633)

## Wingtips #112, une tâche planifiée qui ne tourne qu'une fois

witcheer a publié le 28 octobre le conseil Wingtips #112. Pour lancer une tâche une seule fois, on ouvre la planification avec « in » : hermes cron create "in 2h" "Remind me to call the dentist before they close." La passerelle l'exécute une fois, deux heures plus tard, puis la tâche se retire d'elle-même de la planification.

> Source : [@witcheer, Hermes Wingtips #112: a scheduled job that runs once, 28 octobre 2026](https://x.com/witcheer/status/2115428373564375354)

## Ornith 1.5 122B tient sur une carte

witcheer a comparé le 27 octobre les deux tailles d'Ornith 1.5 en local. Le 122B, en fichier 3 bits de 46,1 Gio, tourne à 47,6 tok/s sur une RTX 5090, une partie de ses experts placée en RAM système. Le 35B, en Q4_K_M de 20,2 Gio, tient entièrement sur la carte et va environ six fois plus vite, tout en restant dans la marge d'erreur du 122B sur tous les tests sauf MMLU.

Ornith 1.5 est une famille de modèles ouverts sous licence MIT, lancée par le laboratoire Ornith en 397B, 35B et 9B, puis complétée en 122B pour remplir le créneau intermédiaire demandé par les amateurs de modèles locaux. Les poids sont sur Hugging Face, et le modèle tourne notamment dans Ollama et Hermes Agent.

> Sources : [@witcheer, Ornith 1.5 122B runs on one 32 GB card, 27 octobre 2026](https://x.com/witcheer/status/2115186775782281386), [Ornith-1.5, page du modèle, ornith.ai](https://ornith.ai/ornith_1_5.html) et [@AGTPinsights, Ornith just released Ornith-1.5-122B](https://x.com/AGTPinsights/status/2112586907981128010)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)
