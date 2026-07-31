# Hermes Agent Quotidien #5

Classement coût de Composio, Hermes en tête, et benchmark tinyMMLU de GMI Cloud.

## Hermes Agent est le moins cher, selon le benchmark coût de Composio

Composio a publié le 31 juillet les résultats d'un classement des agent harnesses par coût par tâche. Hermes Agent et Pi Agent arrivent en tête, tandis que Claude Code coûte 3,7 fois plus cher :

- **0,39 $** Hermes Agent
- **0,40 $** Pi Agent
- **0,47 $** Codex
- **0,51 $** OpenCode
- **0,54 $** Kimi Code
- **1,47 $** Claude Code

Le coût médian raconte la même histoire : 0,29 $ pour Pi Agent et Hermes, 0,35 $ pour OpenCode, 0,38 $ pour Kimi Code, 0,39 $ pour Codex et 0,72 $ pour Claude Code. L'écart n'est pas tiré par quelques tâches coûteuses, il tient sur une tâche typique.

Les coûts ont été calculés en utilisant les prix listes de Kimi K3 : 3 $/1M tokens d'entrée, 0,30 $/1M tokens d'entrée en cache, et 15 $/1M tokens de sortie.

> Source : [@Composio relayé par @Teknium, 31 juillet 2026](https://x.com/Teknium/status/2083172515292283223)

## tinyMMLU : Hermes Agent plus rapide et plus économe que OpenCode sur Kimi K3 et GLM 5.2

GMI Cloud a testé trois modèles, GLM 5.2, Kimi K3 et DeepSeek V4 Pro sur le dataset tinyMMLU (Hugging Face), en utilisant Hermes Agent et OpenCode comme harness. Les résultats varient significativement selon l'appariement modèle-agent.

**Kimi K3 :** Hermes Agent en 40 secondes avec 110K tokens (96/100), contre OpenCode en 8 minutes 13 avec 149K tokens (93/100). Hermes est 12 fois plus rapide et plus efficace en tokens.

**GLM 5.2 :** Hermes Agent en 2 minutes 30 avec 195K tokens (94/100), contre OpenCode en 6 minutes 20 avec 432K tokens (94/100). Score identique, mais Hermes consomme moins de la moitié des tokens.

**DeepSeek V4 Pro :** OpenCode est ici plus efficace, 3 minutes 25 avec 795K tokens (95/100, 0,06 $), contre Hermes Agent en 3 minutes 44 avec 1,23M tokens (97/100, 0,15 $). Hermes obtient le meilleur score, OpenCode le meilleur coût.

GMI Cloud a utilisé sa propre API pour tous les modèles testés sur Hermes Agent, et pour GLM 5.2 et DeepSeek V4 Pro sur OpenCode. Kimi K3 sur OpenCode a été testé via un autre fournisseur.

> Source : [@gmi_cloud relayé par @Teknium, 31 juillet 2026](https://x.com/Teknium/status/2083003495020630108)

## Sources

- [@Composio relayé par @Teknium, 31 juillet 2026](https://x.com/Teknium/status/2083172515292283223)
- [@gmi_cloud relayé par @Teknium, 31 juillet 2026](https://x.com/Teknium/status/2083003495020630108)
