# Hermes Agent Quotidien #10

Liquid AI sort LFM2.5-2.6B, un plugin HermesOffice transforme la suite bureautique, Hermes Agent s'installe dans le panneau latéral de X, et des utilisateurs poussent 3 agents + 10 sous-agents sur 16 Go de RAM.

## Liquid AI publie LFM2.5-2.6B, entraîné sur Hermes Agent

Le 4 août, Liquid AI a officiellement publié LFM2.5-2.6B, un modèle agentique de 2,6 milliards de paramètres conçu pour tourner entièrement sur l'appareil (téléphone, laptop, PC, robot). Les données ne quittent jamais le terminal, et le coût marginal de chaque exécution est proche de zéro.

Le modèle a été pré-entraîné sur 34 000 milliards de tokens, utilise l'architecture hybride LFM2.5, avec une fenêtre de contexte de 128K tokens et un vocabulaire de 128K tokens. La dernière étape de son post-entraînement a été réalisée via du RL agentique multi-tours dans Hermes Agent, Pi et OpenClaw (sujet couvert dans l'édition #9).

Les scores sont comparables ou supérieurs à des modèles jusqu'à 4x sa taille : ToolSandbox 77,83 (devant Qwen3.5-9B à 76,44), Multi-IF 80,07 (devant Gemma-4-E4B-it à 77,35), IFStruct 85,49 (devant Qwen3.5-9B à 78,50).

@0xSero a relayé le modèle comme "le meilleur modèle pour votre hardware local 8 Go - entraîné dans Hermes - entraîné sur une quantité ridicule de tokens - peut naviguer téléphones, ordinateurs et bots".

> Sources : [Liquid AI, 4 août 2026](https://x.com/liquidai/status/2084640749862236227) - [@0xSero relayé par @Teknium, 4 août 2026](https://x.com/0xSero/status/2084754963406975179)

## HermesOffice : la suite bureautique open-source pilotée par Hermes

Gustavo Caetano a publié le 4 août HermesOffice, une suite bureautique open-source (Word, Sheets, Slides, PDF) où l'assistant IA est un véritable agent Hermes tournant à 100 % sur votre machine. Pas de compte cloud, pas de proxy tiers. L'assistant qui édite vos documents est le même agent qui connaît vos fichiers, votre mémoire et vos outils.

Le projet est forké du moteur GenOffice (Apache-2.0) et disponible sur GitHub à l'adresse github.com/criptogus/HermesOffice. Teknium a relayé l'annonce en commentant "Looks useful!".

> Source : [@gustavocaetano relayé par @Teknium, 4 août 2026](https://x.com/gustavocaetano/status/2084770321962549371)

## Hermes Agent dans le panneau latéral de X

Marco Franzon (@mfranz_on), déjà connu pour Paper Agent (Hermes piloté depuis une liseuse ebook, édition #7), a intégré Hermes Agent dans un panneau latéral de X (Twitter). "I've added X into a side panel to have the full control over my agents while I am doomscrolling", explique-t-il.

Teknium a relayé le post le 5 août, poursuivant sa série de mises en avant des configurations hardware et desktop les plus créatives de la communauté.

> Source : [@mfranz_on relayé par @Teknium, 5 août 2026](https://x.com/mfranz_on/status/2084586127898427569)

## 3 agents + 10 sous-agents sur 16 Go de RAM

Josh Stevenson (@RecursiveIntell) a publié le 5 août une démonstration d'efficacité : 3 agents Hermes + 10 sous-agents + 3 onglets Chrome tournent simultanément sur une machine avec 16 Go de RAM (14 Go utilisables), avec 5,25 Go libres restants.

"J'avais l'habitude de penser que ça nécessitait 64 Go de RAM", écrit-il. Il propose d'aider à réduire l'empreinte mémoire et CPU d'Hermes en utilisant son travail sur l'efficacité ESP32. Teknium a relayé le constat.

> Source : [@RecursiveIntell relayé par @Teknium, 5 août 2026](https://x.com/RecursiveIntell/status/2084892532392276364)

## Sources

- [Liquid AI - LFM2.5-2.6B, 4 août 2026](https://x.com/liquidai/status/2084640749862236227)
- [@0xSero relayé par @Teknium - LFM2.5-2.6B, 4 août 2026](https://x.com/0xSero/status/2084754963406975179)
- [@gustavocaetano relayé par @Teknium - HermesOffice, 4 août 2026](https://x.com/gustavocaetano/status/2084770321962549371)
- [@mfranz_on relayé par @Teknium - Hermes in X panel, 5 août 2026](https://x.com/mfranz_on/status/2084586127898427569)
- [@RecursiveIntell relayé par @Teknium - Efficacité RAM, 5 août 2026](https://x.com/RecursiveIntell/status/2084892532392276364)

## Licence

Sous licence CC BY 4.0. - [hermes-agent-news-fr](https://github.com/t1t4nium/hermes-agent-news-fr)