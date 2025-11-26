# Projet de Probabilités – Chaînes de Markov (SM301)

Ce dépôt fournit l'ossature LaTeX complète pour rédiger le rapport (20 pages max) et préparer la présentation orale sur les distributions limites des chaînes de Markov (énoncé : `Probability SM301 Project 2026.pdf`). Les contenus restent à renseigner, mais tout est prêt pour travailler dans VS Code ou en ligne de commande.

## Prérequis
- TeX Live / MacTeX / MiKTeX avec `latexmk` et `biber`.
- VS Code + extension **LaTeX Workshop** (optionnel mais pratique).

## Structure
- `main.tex` : point d'entrée, inclut toutes les sections.
- `tex/` : fichiers de sections (`01_introduction.tex`, `02_numerical_exploration.tex`, …), préambule (`preamble.tex`), page de titre et annexes.
- `references.bib` : références BibLaTeX.
- `input_data/matrix.txt` : matrice de transition 27×27 fournie.
- `images/` : illustrations (ex. `matrix_proba.pdf`) + place pour vos figures.
- `.latexmkrc` : sortie dans `out/` et configuration `biber`.
- `out/` : répertoire de compilation (généré par `latexmk`).

## Vue rapide de la structure
```
markov-limit-distributions/
├── main.tex               # Point d'entrée : assemble toutes les sections
├── tex/                   # Sections LaTeX
│   ├── preamble.tex       # Packages, styles, commandes
│   ├── titlepage.tex      # Page de titre à personnaliser
│   ├── abstract.tex       # Résumé
│   ├── 01_introduction.tex
│   ├── 02_numerical_exploration.tex
│   ├── 03_explanation.tex
│   ├── 04_extended.tex
│   ├── 05_conclusion.tex
│   └── appendix.tex       # Annexes (code, figures)
├── references.bib         # Bibliographie BibLaTeX
├── images/                # Illustrations (ex. matrix_proba.pdf) + vos figures
├── input_data/            # Données fournies (matrice 27×27)
│   └── matrix.txt
├── out/                   # Fichiers générés par latexmk (PDF, aux, log)
├── .latexmkrc             # Configuration latexmk (sortie out/, biber)
└── .vscode/settings.json  # VS Code LaTeX Workshop : sortie out/
```

## Compiler
Depuis la racine :
```bash
latexmk -pdf main.tex
```
Avec LaTeX Workshop, assurez-vous que la commande utilise `latexmk` (le fichier `.latexmkrc` force la sortie dans `out/`).

## Remplir le rapport
1) Compléter les métadonnées dans `tex/titlepage.tex` et le résumé dans `tex/abstract.tex`.  
2) Renseigner chaque question dans `tex/02_numerical_exploration.tex` (questions 1–7), `tex/03_explanation.tex` (questions 8–10), `tex/04_extended.tex` (questions 11–14) puis conclure dans `tex/05_conclusion.tex`.  
3) Ajouter les scripts/figures en annexe (`tex/appendix.tex`, dossier `images/`).  
4) Citer vos sources dans `references.bib` et \`\\parencite\` ou \`\\textcite\` dans le texte.

## Rappels livrables
- Rapport : 20 pages maximum, dépôt Moodle avant la date limite indiquée dans l'énoncé.
- Présentation orale (10–15 min) : synthèse sur l'existence des distributions limites avec nouveaux exemples et exécution de vos programmes.
