# JustProj

<p align="center">A toolkit for creating documentation and project management diagrams in Python</p>
<br>
<p align="center">
	<img src="https://img.shields.io/github/languages/top/alexeev-prog/JustProj?style=for-the-badge">
	<img src="https://img.shields.io/github/languages/count/alexeev-prog/JustProj?style=for-the-badge">
	<img src="https://img.shields.io/github/license/alexeev-prog/JustProj?style=for-the-badge">
	<img src="https://img.shields.io/github/stars/alexeev-prog/JustProj?style=for-the-badge">
	<img src="https://img.shields.io/github/issues/alexeev-prog/JustProj?style=for-the-badge">
	<img src="https://img.shields.io/github/last-commit/alexeev-prog/JustProj?style=for-the-badge">
</p>

> [!CAUTION]
> At the moment, JustProj is under active development (alpha), many things may not work, and this version is not recommended for use (all at your own risk).

## Installion

```bash
pip3 install justproj_toolkit
```

Run example:

```bash
python3 -m justproj_toolkit
```

## Example

```python
from justproj_toolkit.baseproject.documentation import InitiationSection, DocumentSubsection, DocumentFolder, ProjectManager, ProjectTemplate

s1 = InitiationSection('Introduction', 'An introduction to JustProj Toolkit', {'Language': 'Python with some libs'})
s2 = InitiationSection('Introduction 2', 'An another introduction number 2 to JustProj Toolkit', {'Number': 'version 2'})
ss1 = DocumentSubsection('InitiationSubSection', {'Test2': 'hi'}, s1)
ss2 = DocumentSubsection('InitiationSubSection 2', {'Test3': 'hi wpr;d'}, s2)
s1.link_new_subsection(ss1)
s2.link_new_subsection(ss2)

folder = DocumentFolder('basic', 'app/docs', [s1, s2])

project_manager = ProjectManager('JustProj Toolkit', 'An another tool for project management and creation', 'Bla-bla-bla', 
							'alexeev-prog', 'JustProj', 'app',
							ProjectTemplate.CPP, [folder], [s1, s2])

project_manager.add_directory_to_structure('examples', ['example-1.txt', 'example-2.txt'])

project_manager.process_project()

```
