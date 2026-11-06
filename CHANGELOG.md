# Changelog

## [1.0.0]

### Added
- Packaging with `pyproject.toml` (metadata, dependencies, tool configuration).
- NumPy-style docstrings for the public API.
- Public API exposed through `__init__.py` and `__all__`.
- Continuous integration with GitHub Actions and pre-commit hooks.

### Changed
- Project organised into packages (`casing`, `truncation`) with internal `_` modules.
- Code formatted with Black and checked with Ruff.

## [0.1.0]

- Ajout de `word_count` pour compter les mots.
- Ajout de `character_count` pour compter les caractères.
- Ajout de `reverse` pour inverser une chaîne de caractères.
- Ajout de `capitalize_words` pour mettre en majuscule la première lettre de chaque mot.
- Ajout de `truncate` pour raccourcir un texte à une longueur maximale avec un suffixe configurable.
- Création des tests unitaires pour vérifier les fonctions.
- Ajout de la documentation du projet.
- Ajout de la licence MIT.