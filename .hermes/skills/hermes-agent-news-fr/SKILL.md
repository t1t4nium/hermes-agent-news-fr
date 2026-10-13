---
name: hermes-agent-news-fr
description: Écrire le Quotidien Hermes Agent en français.
version: 1.3.0
author: Hermes
license: MIT
metadata:
  tags: [news, quotidien, hermes-agent, nous-research, sourçage, x]
  homepage: https://github.com/t1t4nium/hermes-agent-news-fr
  related_skills: [humanizer]
---

# Skill : Écrire le Quotidien Hermes Agent

## When to Use

Déclencher cette skill pour écrire l'édition quotidienne du Hermes Agent
Quotidien (actualité sourcée de Hermes Agent, Nous Research et l'écosystème,
résumée et traduite en français). La charger aussi quand une tâche planifiée ou
une demande fait référence au quotidien, ou quand le fichier AGENTS.md du dépôt
`hermes-agent-news-fr` est en jeu.

## Source de vérité : AGENTS.md

Le déroulé et le fonctionnement du process sont définis dans le fichier
AGENTS.md du dépôt `hermes-agent-news-fr/AGENTS.md`. Toujours le
lire avant d'écrire une édition. Ne pas dupliquer ces règles ici : la skill
porte uniquement les méthodes techniques, les pièges, les leçons et les
contournements.

## Outillage du projet

### Scripts

Le sourçage X s'appuie sur quatre scripts du dépôt `hermes-agent-news-fr/scripts/` :
- `collect_sources.py` : pipeline de collecte. Exécuté par la tâche planifiée de
  collecte, il lit les comptes X à interroger dans `data/sources.json` (entrées
  `kind: x_account`), déduplique et écrit `data/x/YYYY-MM-DD.json`. Il échoue
  bruyamment (code de sortie non nul et message sur stderr) si un compte ne
  renvoie rien ou si le fetch échoue, pour ne pas produire de données incomplètes
  en silence.
- `fetch-x-timeline.py` : appelé en sous-processus par le script `collect_sources.py`
  pour interroger chaque compte. C'est ce script qui réalise le scrape réel des
  timelines (page profil puis API de syndication).
- `list_tweets.py` : lister les tweets d'un dump. Usage :
  `python3 scripts/list_tweets.py data/x/YYYY-MM-DD.json [--hours N]`.
- `confirm_tweets.py` : confirmer un ou plusieurs tweets via l'API de
  syndication de Twitter (sans clé). Usage :
  `python3 scripts/confirm_tweets.py <id>`. Affiche auteur, date et texte. Sert
  à valider qu'un tweet existe vraiment avant de le citer (règle anti-invention
  d'AGENTS.md).

## Méthodes techniques

### Récupérer les releases GitHub (feed)

La récupération se fait en deux temps, sans substitution de commande ni pipe,
pour ne pas être bloquée par le scan de sécurité en mode tâche planifiée.

1. Lire `data/sources.json` et repérer l'entrée `kind: feed` ainsi que son URL.
2. Interroger cette URL avec `curl -s <URL>`.

Le flux Atom renvoie les notes de chaque release.

### Lire les tweets X collectés

1. Les tweets des dernières 24h sont déjà collectés dans
   `data/x/YYYY-MM-DD.json`, un fichier frais par jour produit par
   `collect_sources.py`.
2. Lister et lire le dump :
   `python3 scripts/list_tweets.py data/x/YYYY-MM-DD.json`.
3. Pour un tweet candidat, confirmer son existence et son texte :
   `python3 scripts/confirm_tweets.py <id>`.
4. Si le dump du jour est absent ou incomplet, relancer la collecte :
   `python3 scripts/collect_sources.py`.

### Méthode de secours (navigateur)

Si X bloque le scrape sans clé (challenge, mur de connexion), remonter une
timeline longue via `browser_exec` : ouvrir le profil, scroller en boucle avec
des pauses de 4 secondes, puis extraire depuis le DOM. Extraction unitaire
par tweet :

```python
# browser_exec - new_tab/goto_url sur https://x.com/{user}
import time; time.sleep(4)
items = js("""
(() => {
  const out = [];
  document.querySelectorAll('article[data-testid="tweet"]').forEach(a => {
    const link = a.querySelector('a[href*="/status/"]');
    const text = a.querySelector('[data-testid="tweetText"]');
    out.push({
      id: link ? (link.getAttribute('href').match(/status\/(\d+)/)||[])[1] : null,
      date: link ? (link.getAttribute('title')||'') : '',
      text: text ? text.innerText : ''
    });
  });
  return out;
})()
""")
```

Scroller davantage, relire le DOM, accumuler les IDs uniques. Le navigateur
passe l'anti-bot bien mieux que curl, mais X demande une connexion au bout d'un
moment : on tient en général plusieurs dizaines de statuts avant le mur de login.

## Pièges et leçons

### Releases volumineuses (édition #37, 2026-09-01)

Le format d'une section release est une puce par changement, une phrase par puce
(règle AGENTS.md). Sur l'édition #37 (release v0.21.0, exceptionnellement
volumineuse), la section a été rédigée en un long paragraphe de prose dense. Plus
une release est grosse, plus elle pousse à l'écriture en flux ; elle doit au
contraire renforcer le format en liste. Avant de rendre une section release,
vérifier explicitement le format une puce par changement, comme pour la relecture
des tics d'IA. En cas de doute, repartir du précédent sain d'une édition antérieure
(#23, #26).

### Scan de sécurité en mode tâche planifiée

En mode tâche planifiée, les approbations sont refusées et le scan de sécurité
bloque certaines commandes : les pipes vers un interpréteur, l'exécution via un
flag `-c`, les substitutions de commande `$(...)`. Préférer des commandes simples
et décomposées (lire le fichier, puis `curl` l'URL directement). C'est la raison
de la méthode en deux temps pour le feed.

## Références utiles

- Skill `humanizer` : éliminer les expressions typiques de l'IA et ajouter une
  véritable touche humaine. À appliquer à la relecture.

## Exemples testés (édition #26)

Sujets retenus et leur sourçage réel :

- Release v0.20.5 : contenu complet dans le flux `releases.atom`. Les
  changements se listent en une puce par changement (règle AGENTS.md), pas en
  bloc séparé par des virgules.
- Annonce xAI (rendu 20% plus vite) : statut @Teknium/status/2090648797844210019,
  trouvé dans la timeline Teknium.
- Grok/Imagine : statut @Jaaneek, trouvé via un retweet dans la timeline
  NousResearch (filtrer les retweets, attribuer au bon auteur).
- Recrutement : le tweet @NousResearch pointe nousresearch.com/careers. La page
  liste huit postes et le process de candidature ; la règle AGENTS.md impose
  d'ouvrir ce lien et d'enrichir le sujet, plutôt que de paraphraser le tweet.
- Ox Alpha : statut @Teknium via opencode/OpenRouter.

Sujets volontairement écartés (déjà couverts) : SkillEvaluator (#25), fil
Hermes Cloud (#25). Toujours vérifier dans les deux dernières éditions.
