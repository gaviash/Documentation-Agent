# DocumentationAgent

DocumentationAgent est un prototype de workflow multi-agents pour produire une documentation de codebase a partir d'un dossier cible.

L'idee du repo est de decomposer le travail de documentation en plusieurs etapes specialisees: cadrer la demande, explorer la codebase, preparer un plan de redaction, puis laisser les agents suivants produire les documents finaux.

## Principe general

Le projet s'appuie sur des agents LlamaIndex connectes a un modele LLM via Ollama. Chaque agent recoit un prompt specialise depuis `skills-prompts/` et dispose d'outils limites pour lire/ecrire des fichiers, lancer des commandes simples, chercher sur le web ou recuperer du contenu.

Le dossier a documenter est attendu dans `process/`. Les documents intermediaires et livrables de workflow sont ecrits dans `docs/`.

## Fonctionnement du workflow

Le workflow actuel est organise autour de trois agents principaux:

- `BrainstormingAgent`: comprend la demande, inspecte le projet, fait choisir une approche de documentation, puis ecrit un document de design/orientation et un fichier d'informations utiles.
- `ExplorationAgent`: lit les sorties du brainstorming et explore la codebase pour produire des rapports factuels destines au planificateur.
- `WritingPlanAgent`: lit uniquement les documents disponibles dans `docs/` et produit un plan de redaction Markdown.

Le `BrainstormingAgent` peut poser des questions pertinentes a l'utilisateur sur ses preferences de documentation: public vise, format, profondeur, priorites, exclusions ou choix entre plusieurs approches. Cela rend le workflow flexible et adaptable a differents types de documentation, plutot qu'a un seul format fixe.

Les prochaines etapes prevues sont:

- `WritingAgent`: redige la documentation a partir du plan, potentiellement en parallele si le provider LLM l'autorise.
- `ReviewAgent`: relit et verifie l'ensemble de la documentation produite.
- `DocAgent`: met en page et exporte la documentation dans le format demande par l'utilisateur.

Les prompts de ces agents se trouvent dans:

- `skills-prompts/brainstorming_agent.txt`
- `skills-prompts/brainstorming.md`
- `skills-prompts/codebase-exploration.md`
- `skills-prompts/redac-planning.md`
- `skills-prompts/general_prompt.md`

## Structure utile

- `app/agents.py`: declaration des modeles, agents et fonction commune de requete.
- `app/workflow.py`: orchestration de debug du workflow.
- `app/tools.py`: outils disponibles pour les agents.
- `skills-prompts/`: prompts et consignes de comportement des agents.
- `app/process/`: emplacement actuel du projet cible a documenter.
- `app/docs/`: documents generes par les agents.
- `ancient_docs/`: anciens essais et documents de reference.
- `suite.txt`: notes de travail et prochaines idees.

## Configuration

Le projet utilise un fichier `.env` pour les cles et parametres de modele. Les variables importantes sont notamment:

- `OLLAMA_MODEL`
- `OLLAMA_API_KEY`
- `PROMPTS_DIR`
- `TAVILY_API_KEY`
- variables Langfuse si l'observabilite est activee

Les outils respectent un workspace local et limitent les lectures/sorties longues pour eviter de saturer le contexte des agents.

## Etat actuel

Le repo est encore en construction. Plusieurs pieces sont deja presentes, mais le workflow complet n'est pas encore finalise. Les prochaines priorites notees sont le passage propre d'informations entre agents, la formalisation d'evenements de fin d'etape, et l'amelioration du chainage entre brainstorming, exploration et planification.

Ce README donne seulement une vue d'ensemble du fonctionnement et du principe du projet. Les details techniques precis doivent rester dans les prompts, les fichiers d'agent et les documents generes.
