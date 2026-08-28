# Hermes Agent Quotidien #33

Cette édition revient sur la navigation connectée en tant que soi grâce au profil Chrome, une fonctionnalité mise en avant par Nous Research et détaillée par witcheer, et sur un pont communautaire qui porte le Bot Mode de l'application de bureau vers Discord.

## Naviguer connecté en tant que soi, via un cliché du profil Chrome

Nous Research a annoncé la navigation réelle consentie, qui permet à l'agent de naviguer sur le web connecté avec vos identifiants. Le compte est repris d'une copie gérée du profil Chrome existant, sans toucher au profil d'origine.

witcheer détaille le mécanisme : Hermes copie les cookies, les identifiants enregistrés et les préférences du profil utilisé, puis pilote cette copie avec son propre Chromium embarqué. Le cliché se resynchronise à chaque nouveau lancement.

> Sources : [@NousResearch, Hermes Agent can now seamlessly browse as you, 27 août 2026](https://x.com/NousResearch/status/2093063359587348487) et [@witcheer, naviguer connecté en tant que soi, 27 août 2026](https://x.com/witcheer/status/2093076357261463772)

## Le Bot Mode d'Hermes ponté vers Discord

Daniel Ou a construit un pont qui apporte le Bot Mode d'Hermes, jusqu'ici réservé à l'application de bureau, à Discord, pour l'utiliser depuis son téléphone. Son dépôt `hermes-discord-botrooms` transforme de deux à six profils Hermes existants en une room de groupe sur Discord, chaque profil conservant son propre modèle, sa mémoire, ses outils, son SOUL et son identité de bot. Le plugin coordonne les réponses en série, le contexte de room persistant, les indicateurs de frappe, les pièces jointes, les approbations et la reprise après redémarrage.

Le projet, en bêta, exige un build Hermes compatible et une vérification de compatibilité obligatoire. L'installation recommandée passe par un agent qui découvre l'existant sans rien modifier, puis demande une double approbation avant d'installer et de reconfigurer. Les jetons de bot restent dans les magasins de credentials des profils existants.

witcheer salue ce travail de communauté, soulignant que les profils gardent chacun leur modèle, leur mémoire et leur identité dans le canal.

> Sources : [@imnotchalk, I brought Hermes Bot Mode to Discord, 28 août 2026](https://x.com/imnotchalk/status/2093180690926068069), [@witcheer, le Bot Mode porté sur Discord, 28 août 2026](https://x.com/witcheer/status/2093216196376097051) et [hermes-discord-botrooms, dépôt GitHub de Daniel Ou](https://github.com/DanielOu1208/hermes-discord-botrooms)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)

## Sponsor

Le quotidien Hermes Agent c'est l'actualité de Hermes Agent et de Nous Research ainsi que de tout l'écosystème, sourcée, résumée et traduite en français chaque jour, pour vous.
Vous appréciez le quotidien ? Il vous est utile ? Il vous fait gagner du temps ?
Soutenez-le en devenant sponsor : [github.com/sponsors/t1t4nium](https://github.com/sponsors/t1t4nium).
