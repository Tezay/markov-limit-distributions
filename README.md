# Projet de Probabilités – Chaînes de Markov (SM301)

Ce dépôt fournit l'ossature LaTeX complète pour rédiger le rapport (20 pages max) et préparer la présentation orale sur les distributions limites des chaînes de Markov (énoncé : `Probability SM301 Project 2026.pdf`). Les contenus restent à renseigner, mais tout est prêt pour travailler dans VS Code ou en ligne de commande.

## Prérequis
- TeX Live / MacTeX / MiKTeX avec `latexmk` et `biber`.
- VS Code + extension **LaTeX Workshop** (optionnel mais pratique).

## Installation rapide des dépendances LaTeX
- **macOS (Homebrew)**  
  ```bash
  brew update
  brew install texlive   # inclut latexmk et biber
  latexmk --version && biber --version
  ```
  (Si vous préférez MacTeX complet : `brew install --cask mactex`.)

- **Windows**  
  1. Installez MiKTeX depuis https://miktex.org/download ou via winget :  
     ```powershell
     winget install -e --id MiKTeX.MiKTeX
     ```
  2. Installez Perl (requis par `latexmk`) si vous ne l'avez pas déjà :  
     ```powershell
     winget install -e --id StrawberryPerl.StrawberryPerl
     ```
     Redémarrez la session pour que `perl` soit dans le PATH.
  3. Ouvrez la « MiKTeX Console » et ajoutez les paquets manquants (`latexmk`, `biber`) si non présents.  
  4. Vérifiez :  
     ```powershell
     latexmk --version
     biber --version
     ```

## Compiler
Depuis la racine :
```bash
latexmk -pdf main.tex
```

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

## Structure
- `main.tex` : point d'entrée, inclut toutes les sections.
- `tex/` : fichiers de sections (`01_introduction.tex`, `02_numerical_exploration.tex`, …), préambule (`preamble.tex`), page de titre et annexes.
- `references.bib` : références BibLaTeX.
- `input_data/matrix.txt` : matrice de transition 27×27 fournie.
- `images/` : illustrations (ex. `matrix_proba.pdf`) + place pour vos figures.
- `.latexmkrc` : sortie dans `out/` et configuration `biber`.
- `out/` : répertoire de compilation (généré par `latexmk`).