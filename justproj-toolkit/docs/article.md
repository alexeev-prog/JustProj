# Управляем проектом и его документацией при помощи Python
Доброго времени суток, хабр! Управление проектом - это настоящее искусство, требующего внимания к деталям, навыков планирования. Документация, планы и структура проекта должна составляться в первую очередь, перед написанием кода.

Недавно я присоединился к команде, которая работает над одним амбициозным проектом, то мы сразу на первом созвоне осознали, что нам нужна структура проекта, правильное его управление, дорожная карта - все это позволит воплатить в жизнь и не бросить его.

Именно поэтому я решил создать библиотеку на Python, которая позволит легко создать базовую структуру документации проекта и контролировать ее изменение. Автоматизация рутинных процессов, проще говоря. В этой статье я об этом и расскажу. Уверен, что этот опыт будет полезен каждому, кто сталкивался с необходимостью организации и планирования проекта.

---

Что такое структура проекта? Структура проекта - это в первую очередь правильно упорядоченные мысли и планы по видению проекта.

И в этой статье мы создадим универсальную базовую python-библиотеку для создания архитектуры проекта и его документации. Мы сможем создавать секции документации вместе с подсекциями, связывать секцию с другой секцией, собирать секции в одни объекты (в нашей библиотеке это будут экземпляры класса Folder, в котором будет храниться список секций), а также генерировать базовую структуру проекта взависимости от языка.

И наш инструмент будет распространяться в виде python-библиотеки. В этой статье вы также сможете опубликовать его на PyPi, а это значит что в дальнейшем вы или другие люди смогут просто установить пакет и пользоваться вашим инструментом.

В мире программирования создание собственных библиотек - это не просто возможность пополнения своего портфолио или способ структурировать код, а настоящий акт творческого самовыражения (и иногда велосипедостроения). Каждый разработчик иногда использовал в нескольких своих проектах однообразный код, который приходилось каждый раз перемещать. Да и хотя-бы как упаковать свои идеи и знания в удобный и доступный формат, которым можно будет поделиться с сообществом.

Итак, как обычно начинается создание проектов на python? Банально создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate
```

Но в этом проекте я решил отойти от такого способа, и использовать вместо этого систему правлению проектами Poetry. Poetry — это инструмент для управления зависимостями и сборкой пакетов в Python. А также при помощи Poetry очень легко опубликовать свою библиотеку на PyPi!

В Poetry представлен полный набор инструментов, которые могут понадобиться для детерминированного управления проектами на Python. В том числе, сборка пакетов, поддержка разных версий языка, тестирование и развертывание проектов.

Все началось с того, что создателю Poetry Себастьену Юстасу потребовался единый инструмент для управления проектами от начала до конца, надежный и интуитивно понятный, который бы мог использоваться и в рамках сообщества. Одного лишь менеджера зависимостей было недостаточно, чтобы управлять запуском тестов, процессом развертывания и всем созависимым окружением. Этот функционал находится за гранью возможностей обычных пакетных менеджеров, таких как Pip или Conda. Так появился Python Poetry.

Установить poetry можно через pipx: `pipx install poetry` и через pip: `pip install poetry --break-system-requirements`. Это установит poetry глобально во всю систему.

Итак, давайте создадим проект при помощи poetry и установим зависимости:

```bash
poetry new <имя_проекта>
cd <имя_проекта>
poetry shell
poetry add ruff pycolor_palette_loguru
```

Библиотека `pycolor_palette_loguru` - эта та библиотека, которую мы создали в [статье о создании своей python-библиотеки](https://habr.com/ru/companies/timeweb/articles/847370/). Оттуда и будет взята инструкция по публикации своего пакета на PyPi через poetry.

[Ruff](https://pypi.org/project/ruff/) — это новый быстроразвивающийся линтер Python-кода, призванный заменить flake8 и isort.

Основным преимуществом Ruff является его скорость: он в 10–100 раз быстрее аналогов (линтер написан на Rust).

Ruff может форматировать код, например, автоматически удалять неиспользуемые импорты. Сортировка и группировка строк импорта практически идентична isort.

Инструмент используется во многих популярных open-source проектах, таких как FastAPI и Pydantic.

Настройка Ruff осуществляется в файле pyproject.toml.

Для использования ruff как линтер можно использовать следующие команды:

```bash
ruff check                          # Lint all files in the current directory (and any subdirectories).
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories).
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`.
ruff check path/to/code/to/file.py  # Lint `file.py`.
ruff check @arguments.txt           # Lint using an input file, treating its contents as newline-delimited command-line arguments.
ruff check . --fix 					# Lint all files in current directory and fix
```

А если как форматтер:

```bash
ruff format                          # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
ruff format @arguments.txt           # Format using an input file, treating its contents as newline-delimited command-line arguments.
ruff format .						 # Format all files in current directory
```

Для конфигурации ruff'а просто можно изменить файл pyproject.toml (созданный poetry):

```toml
# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.8
target-version = "py38"

[lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
select = ["E4", "E7", "E9", "F"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"
```

## Пишем код
Итак, давайте обозначим основные возможности нашей библиотеки:

 + Создание секций и подсекций
 + Связывание секций между собой
 + Создание "папок", состоящих из секций
 + Создание markdown-файлов для описания объектов
 + Создание структуры взависимости от шаблона проекта
 + Единый класс управления проектом

Вот пример сгенерированной структуры, которую будет генерировать наша библиотека:

```
app
├── BUILDING.md
├── CHANGELOG.md
├── .clangd
├── .clang-format
├── .clang-tidy
├── CMakeLists.txt
├── CMakePresets.json
├── CMakeUserPresets.json
├── CODE_OF_CONDUCT.md
├── conanfile.py
├── CONTRIBUTING.md
├── docs
│   └── basic
│       ├── index.md
│       ├── Introduction_2.md
│       └── Introduction.md
├── examples
│   ├── example-1.txt
│   └── example-2.txt
├── HACKING.md
├── LICENSE
├── README.md
└── SECURITY.md

4 directories, 20 files
```

Выше - пример структуры, использующий шаблон C++ проекта. Директория example вместе с файлами внутри ее была создана по требованию пользователя, директория docs автоматически собирается из секций и папок.

Все остальные файлы являются либо стандартными, либо частью шаблона.

Для начала импортируем все нужные пакеты:

```python
import os
from abc import ABC
from enum import Enum
from typing import Dict, List, Any
from pycolor_palette_loguru import info_message, debug_message, warn_message

from utils import get_current_datetime
```

Модуль utils пока содержит одну функцию для получения строки времени:

```python
from datetime import datetime


def get_current_datetime() -> str:
	"""
	Gets the current datetime.

	:returns:   The current datetime.
	:rtype:     str
	"""
	return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```

### Секции и подсекции
Секция в контексте нашей библиотеки - это отдельные самостоятельные части документации проекта. Они могут быть связанными с другими секциями или иметь подсекции.

```python
class DocumentSubsection(ABC):
	"""
	This class describes a document subsection.
	"""

	def __init__(self, title: str, content: Dict[str, Any], main_section: "DocumentSection"):
		"""
		Constructs a new instance.

		:param      title:         The title
		:type       title:         str
		:param      content:       The content
		:type       content:       str
		:param      main_section:  The main section
		:type       main_section:  DocumentSection
		"""
		self.title = title
		self.content = content
		self.main_section = main_section
		self.creation_date = get_current_datetime()

	def set_new_main_section(self, new_main_section: "DocumentSection"):
		"""
		Sets the new main section.

		:param      new_main_section:  The new main section
		:type       new_main_section:  DocumentSection
		"""
		debug_message(f'Set new section for subsection "{self.title}"')
		self.main_section = new_main_section
```

Абстрактный класс DocumentSubsection имеет следующие параметры:

 + Заголовок
 + Контент (словарь)
 + Главная родительская секция (подсекция может иметь только одного родителя)

Также она имеет метод для смены родительской секции.

Следующий класс - секция:

```python
class DocumentSection(ABC):
	"""
	This abstract metaclass describes a documentation section.
	"""

	def __init__(self, title: str, introduction: str, content: Dict[str, Any]):
		"""
		Constructs a new instance.

		:param      title:         The title
		:type       title:         str
		:param      introduction:  The introduction
		:type       introduction:  str
		:param      content:       The content
		:type       content:       { type_description }
		"""
		self.title = title
		self.introduction = introduction
		self.content = content
		self.linked_sections = {}
		self.linked_subsections = {}
		self.creation_date = get_current_datetime()
		self.modification_date = self.creation_date

	def link_new_subsection(self, linked_subsection: DocumentSubsection):
		"""
		Links a new subsection.

		:param      linked_subsection:  The linked subsection
		:type       linked_subsection:  DocumentSubsection
		"""
		self.linked_subsections[linked_subsection.title] = linked_subsection
		linked_subsection.set_new_main_section(self)
		info_message(f'Linked new subsection: "{linked_subsection.title}"')

	def link_new_section(self, linked_section: "DocumentSection"):
		"""
		Links a new section.

		:param      linked_section:  The linked section
		:type       linked_section:  DocumentSection
		"""
		self.linked_sections[linked_section.title] = linked_section
		self.linked_section.link_new_section(self)
		info_message(f'Linked new section: {linked_section.title}')

	def get_filename(self) -> str:
		"""
		Gets the filename.

		:returns:   The filename.
		:rtype:     str
		"""
		return f'{self.title.replace(" ", "_")}.md'

	def modify_title(self, new_title: str):
		"""
		Modify section title

		:param      new_title:  The new title
		:type       new_title:  str
		"""
		debug_message(f'Title modified: {self.title} -> {new_title}')
		self.title = new_title
		self.modification_date = get_current_datetime()

	def modify_description(self, new_description: str):
		"""
		Modify section description

		:param      new_description:  The new description
		:type       new_description:  str
		"""
		debug_message(f'Description modified: {self.description} -> {new_description}')
		self.description = new_description
		self.modification_date = get_current_datetime()

	def modify_content(self, new_content: Dict[str, Any]):
		"""
		Modify section content

		:param      new_content:  The new content
		:type       new_content:  Dict[str, Any]
		"""
		debug_message(f'Content modified: {self.content} -> {new_content}')
		self.content = new_content
		self.modification_date = get_current_datetime()

	def get_markdown_page(self) -> List[str]:
		"""
		Gets the page in markdown formatting
		
		:returns:   The markdown page.
		:rtype:     List[str]
		"""
		debug_message(f'Generating document section [{self.title}]...')
		page = [f'# {self.title}']
		page.append(f'{self.introduction}\n')
		page.append(f' + *Creation date*: {self.creation_date}\n + *Modification date*: {self.modification_date}\n')

		for key, value in self.content.items():
			page.append(f'## {key}\n{value}\n')

		if len(self.linked_subsections) > 0:
			page.append('---\n')
			page.append('## Subsections\n')

			for title, subsection in self.linked_subsections.items():
				page.append(f'### {title}')
				page.append(f'Creation date: {subsection.creation_date}\n')
				for key, value in subsection.content.items():
					page.append(f'#### {key}\n{value}\n')

		page.append('---\n')
		page.append('Created by [JustProj](https://github.com/alexeev-prog/JustProj)')

		info_message(f'Document section [{self.title}] successfully generated!')

		return page
```

Данный класс имеет следующие параметры:
 
 + Заголовок
 + Введение
 + Контент (словарь)

Далее она имеет методы для связывания с подсекциями и секциями - мы добавляем в специальный массив нужный объект, а после вызываем функцию секции link_new_section, или set_new_main_section для подсекции.

Далее функция get_filename для получения имени файла, потом идут файлы для модификации параметров секции. И в самом конце находится функция get_markdown_page для получения страницы секции в markdown-формате. Возвращает она список со строками страниц.

Далее давайте создадим класс, который будет наследоваться от абстрактного класса DocumentSection:

```python
class InitiationSection(DocumentSection):
	"""
	This class describes an initiation section.
	"""

	def __init__(self, title: str, introduction: str, content: Dict[str, Any]):
		"""
		Constructs a new instance.

		:param      title:         The title
		:type       title:         str
		:param      introduction:  The introduction
		:type       introduction:  str
		:param      content:       The content
		:type       content:       Dict[str, Any]
		"""
		self.title = f'Initiation-{title}'
		self.introduction = introduction
		self.content = content
		self.linked_sections = {}
		self.linked_subsections = {}
		self.creation_date = get_current_datetime()
		self.modification_date = self.creation_date
```

Класс InitiationSection является заготовком введения.

Продолжим, теперь создадим класс DocumentFolder - "папка" секций. Этот класс хранит в себе секции, которые обобщены заданной тематикой:

```python
class DocumentFolder:
	"""
	This class describes a document folder.
	"""

	def __init__(self, name: str, project_root_dir: str, sections: List[DocumentSection]):
		"""
		Constructs a new instance.

		:param      name:              The name
		:type       name:              str
		:param      project_root_dir:  The project root dir
		:type       project_root_dir:  str
		:param      sections:          The sections
		:type       sections:          List[DocumentSection]
		"""
		self.name = name.replace(' ', '_')
		self.project_root_dir = project_root_dir
		os.makedirs(self.project_root_dir, exist_ok=True)
		self.folderpath = os.path.join(self.project_root_dir, self.name)
		os.makedirs(self.folderpath, exist_ok=True)
		self.sections = sections

		self._create_index_file()

	def _create_index_file(self):
		"""
		Creates an index file.
		"""
		with open(os.path.join(self.folderpath, 'index.md'), 'w') as file:
			file.write(f'# {self.name}\n\n')

			for section in self.sections:
				file.write(f'## {section.title}\n{section.introduction}\n')
```

На вход DocumentFolder принимает название папки, корневой каталог проекта и список секций. Также есть параметр self.folderpath - путь до директории (корневой каталог + название папки). Все нужные директории создаются, если они не существуют.

А скрытая функция `_create_index_file` создает файл индекса в директории папки.

Переходим к менеджеру документации:

```python
class DocumentManager:
	"""
	This class describes a document manager.
	"""

	def __init__(self, project_name: str, short_project_introduction: str, project_description: str, repo_author: str, repo_name: str, 
				project_root_dir: str, folders: List[DocumentFolder]):
		"""
		Constructs a new instance.

		:param      project_name:         The project name
		:type       project_name:         str
		:param      project_description:  The project description
		:type       project_description:  str
		:param      project_root_dir:     The project root dir
		:type       project_root_dir:     str
		:param      folders:              The folders
		:type       folders:              List[DocumentFolder]
		"""
		self.project_name = project_name
		self.short_project_introduction = short_project_introduction
		self.project_description = project_description
		self.project_root_dir = project_root_dir
		self.folders = folders
		self.repo_author = repo_author
		self.repo_name = repo_name

		os.makedirs(self.project_root_dir, exist_ok=True)

	def generate_readme(self):
		"""
		Generate readme file
		"""
		debug_message('Generate README...')
		page = f'''# {self.repo_name}

<p align="center">{self.short_project_introduction}</p>
<br>
<p align="center">
	<img src="https://img.shields.io/github/languages/top/{self.repo_author}/{self.repo_name}?style=for-the-badge">
	<img src="https://img.shields.io/github/languages/count/{self.repo_author}/{self.repo_name}?style=for-the-badge">
	<img src="https://img.shields.io/github/license/{self.repo_author}/{self.repo_name}?style=for-the-badge">
	<img src="https://img.shields.io/github/stars/{self.repo_author}/{self.repo_name}?style=for-the-badge">
	<img src="https://img.shields.io/github/issues/{self.repo_author}/{self.repo_name}?style=for-the-badge">
	<img src="https://img.shields.io/github/last-commit/{self.repo_author}/{self.repo_name}?style=for-the-badge">
</p>

{self.project_description}

## Folders
DocumentFolders (is not directories):\n
'''
		for folder in self.folders:
			page += f'### {folder.name}\n'
			page += f'Path: {folder.folderpath}\n'

			for section in folder.sections:
				page += f'\n#### {section.title}\n'
				page += f'{section.introduction}\n'

				if len(section.linked_sections) > 0:
					page += '\nLinked sections:\n\n'

					for linked_section in section.linked_sections:
						page += f' + {linked_section.title}\n'

				if len(section.linked_subsections) > 0:
					page += '\nLinked subsections:\n\n'

					for linked_subsection in section.linked_subsections:
						page += f' + {linked_subsection}\n'

		with open(os.path.join(self.project_root_dir, 'README.md'), 'w') as file:
			file.write(page)

		info_message('README generated successfully!')

	def generate_pages(self):
		"""
		Generate pages of sections in folders
		"""
		docs_dir = os.path.join(self.project_root_dir, 'docs')
		os.makedirs(docs_dir, exist_ok=True)

		debug_message('Generating pages...')

		for folder in self.folders:
			for section in folder.sections:
				section_filename = os.path.join(folder.folderpath, section.get_filename())
				debug_message(f'Generating page "{section.title}" [{section_filename}]')
				page = section.get_markdown_page()

				with open(section_filename, 'w') as file:
					for line in page:
						file.write(f'{line}\n')

		info_message('Pages successfully generated!')
```

Данный класс отвечает за создание документации. На вход он принимает: название проекта, крактое описание проекта, полное описание проекта, автор и название репозитория, корневая директория проекта и список папок, которые нужно подключить.

Функция generate_readme создает README-файл в корне проекта, заполняя его базовым контентом.

Функция generate_pages создает нужные файлы и директории папок (и соответственно секций).

Теперь переходим к генератору структуры проекта. Для этого сначала создадим enum-класс шаблонов проекта:

```python
class ProjectTemplate(Enum):
	BASE = 0
	CPP = 1
	PYTHON = 2
```

Пока я решил сделать всего два, но вы можете больше.

И теперь создадим класс ProjectStructureGenerator:

```python
class ProjectStructureGenerator:
	"""
	This class describes a project structure generator.
	"""

	def __init__(self, project_root_dir: str,
					project_template: ProjectTemplate):
		"""
		Constructs a new instance.

		:param      project_root_dir:  The project root dir
		:type       project_root_dir:  str
		:param      project_template:  The project template
		:type       project_template:  ProjectTemplate
		"""
		self.project_root_dir = project_root_dir
		self.project_template = project_template
		os.makedirs(self.project_root_dir, exist_ok=True)
		self.structure = {}

	def add_directory(self, dir_name: str, dir_files: List[str]):
		"""
		Adds a directory.

		:param      dir_name:   The dir name
		:type       dir_name:   str
		:param      dir_files:  The dir files
		:type       dir_files:  List[str]
		"""
		self.structure[dir_name] = {
			'basic': dir_files
		}
		info_message(f'Add new directory: {dir_name}')

	def generate_structure(self):
		"""
		Generate project file structure
		"""
		debug_message('Generate structure...')
		self.structure['.'] = {
			'basic': ['README.md', 'LICENSE', 'BUILDING.md', 'CHANGELOG.md', 'CODE_OF_CONDUCT.md',
					'CONTRIBUTING.md', 'HACKING.md', 'SECURITY.md'],
		}

		if self.project_template == ProjectTemplate.CPP:
			files = ['CMakeLists.txt', 'CMakeUserPresets.json', 'CMakePresets.json', 'conanfile.py',
					'.clang-format', '.clang-tidy', '.clangd']
			
			for file in files:
				self.structure['.']['basic'].append(file)
		elif self.project_template == ProjectTemplate.PYTHON:
			files = ['pyproject.toml', 'requirements.txt']
			
			for file in files:
				self.structure['.']['basic'].append(file)

		for directory, content in self.structure.items():
			debug_message(f'[Structor Generator] Create files in directory "{directory}"')

			if directory != '.':
				current_dir = os.path.join(self.project_root_dir, directory)
				os.makedirs(os.path.join(self.project_root_dir, directory), exist_ok=True)
			else:
				current_dir = self.project_root_dir

			for file in content['basic']:
				debug_message(f'[Structor Generator] {file} processing...')
				with open(os.path.join(current_dir, file), 'w') as file:
					file.write(f'# {file}\n')

		info_message('Structure generated successfully!')
```

Класс принимает корневой каталог проекта и шаблон проекта. Также класс имеет метод для добавления директории в структуру (имя директория и файлы в этой директории). А в самом низу метод для генерации структуры файлов. Сама структура сохраняется в виде словаря. Если используется шаблон, отличный от стандартного, то мы будем добавлять туда нужные нам файлы. После мы создаем нужные файлы и директории.

Отлично! Нам осталось создать один класс - ProjectManager. Он будет содержать в себе экземпляры классов и нужные параметры. Вместо ручного создания экземпляров класса и запуска функций, ProjectManager автоматически все создает и помещает все функции по генерации проекта в один свой метод.

Вот код:

```python
class ProjectManager:
	"""
	This class describes a project manager.
	"""

	def __init__(self, project_name: str, short_project_introduction: str, project_description: str, repo_author: str, repo_name: str, project_root_dir: str,
						project_template: ProjectTemplate, folders: List[DocumentFolder], sections: List[DocumentSection], github: bool=True):
		"""
		Constructs a new instance.

		:param      project_name:         The project name
		:type       project_name:         str
		:param      project_description:  The project description
		:type       project_description:  str
		:param      repo_author:          The repo author
		:type       repo_author:          str
		:param      repo_name:            The repo name
		:type       repo_name:            str
		:param      project_root_dir:     The project root dir
		:type       project_root_dir:     str
		:param      project_template:     The project template
		:type       project_template:     ProjectTemplate
		:param      folders:              The folders
		:type       folders:              List[DocumentFolder]
		:param      sections:             The sections
		:type       sections:             List[DocumentSection]
		"""
		self.project_root_dir = project_root_dir
		self.project_name = project_name
		self.project_description = project_description
		self.short_project_introduction = short_project_introduction
		self.repo_author = repo_author
		self.repo_name = repo_name
		self.project_template = project_template
		self.folders = folders
		self.sections = sections
		self.is_github = github

		if self.is_github:
			self.url = f'https://github.com/{repo_author}/{repo_name}'
		else:
			warn_message('JustProj support only GitHub')

		self.structure_manager = ProjectStructureGenerator(project_root_dir, project_template)
		self.document_manager = DocumentManager(project_name, short_project_introduction, project_description, repo_author, repo_name, 
				project_root_dir, folders)

	def add_directory_to_structure(self, dir_name: str, files: List[str]):
		"""
		Adds a directory to structure.

		:param      dir_name:  The dir name
		:type       dir_name:  str
		:param      files:     The files
		:type       files:     List[str]
		"""
		self.structure_manager.add_directory(dir_name, files)

	def process_project(self):
		"""
		Process project creation
		"""
		info_message(f'Process project "{self.project_name}" creation...')
		self.structure_manager.generate_structure()
		self.document_manager.generate_pages()
		self.document_manager.generate_readme()
		info_message('Project created successfully!')
```

На вход менеджер проектов принимает следующие значения:

 + project_name - название проекта
 + short_project_introduction - краткое введение в проект
 + project_description - описание проекта
 + repo_author - имя автора репозитория
 + repo_name - название репозитория
 + project_root_dir - корневая директория проекта
 + project_template - шаблон проекта
 + folders - список папок
 + sections - список секций
 + github - флаг, используем ли мы гитхаб. Нужен только для того, чтобы вывести предупреждение, что наша библиотека не поддерживает gitlab и т.д. То есть в документации могут возникнуть проблемы - например в методе создания README бейджи могут показывать что страница не найдена. Такие вот ограничения.

То есть на вход менеджер проектов принимает все параметры, которые требуются остальным классам. Собственно, мы и их используем, когда создаем внутренние экземпляры классов.

После мы создаем функцию add_directory_to_structure, которая является внешней оболочкой для аналогичной функции из генератора структуры проекта.

И в конце главный метод process_project, который вызывает все функции генерации структуры проекта или документации.

---

Теперь давайте напишим файл `__main__.py` в директории нашей библиотеки. Это файл позволит запускать наш пакет через `python3 -m <название библиотеки>`:

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

Не забудьте изменить `justproj_toolkit` на ваше название.

И при запуске вы увидите что появилась директория app:

```
app
├── BUILDING.md
├── CHANGELOG.md
├── .clangd
├── .clang-format
├── .clang-tidy
├── CMakeLists.txt
├── CMakePresets.json
├── CMakeUserPresets.json
├── CODE_OF_CONDUCT.md
├── conanfile.py
├── CONTRIBUTING.md
├── docs
│   └── basic
│       ├── index.md
│       ├── Introduction_2.md
│       └── Introduction.md
├── examples
│   ├── example-1.txt
│   └── example-2.txt
├── HACKING.md
├── LICENSE
├── README.md
└── SECURITY.md

4 directories, 20 files
```

Теперь осталось дело за малым - публикация на PyPi.

# Публикация на PyPi
[PyPi](https://pypi.org/) — официальный репозиторий Python для загрузки и скачивания пакетов. Это официальный ресурс пакетов для третьих лиц, которым управляет Python Software Foundation. После публикации на PyPI пакеты становятся доступными для установки.

Итак, вам потребуется аккаунт на PyPi. Зарегистрироваться можно по [этой ссылке](https://pypi.org/account/register/).

![](https://habrastorage.org/webt/iv/ju/c6/ivjuc67v8hrnfajqltuyxzfp5my.png)

Дальше вам нужно будет подключить 2FA для безопасности аккаунта:

![](https://habrastorage.org/webt/li/do/ma/lidomausio9jkpwvcpmeio1tove.png)

Аутентификация с помощью токена — это рекомендуемый способ проверки учетной записи PyPI в командной строке. При этом вместо имени пользователя и пароля можно использовать автоматически сгенерированный токен. Токены можно добавлять и отзывать в любое время; с их помощью можно предоставлять доступ к отдельным частям вашей учетной записи. Это делает их безопасными и значительно уменьшает риск взлома. Теперь создадим новый API-токен для учетной записи, для этого перейдите в настройки учетной записи:

![](https://habrastorage.org/webt/op/h2/qa/oph2qasaxymwfi46q5qkbde7eq8.png)

Прокрутите вниз и найдите раздел “API tokens”. Нажмите “Add API token”:

![](https://habrastorage.org/webt/jh/e7/ck/jhe7ck4yjhigmhqfxixb6whfodc.png)

Теперь с помощью этого токена можно настроить свои учетные данные в Poetry для подготовки к публикации. Чтобы не добавлять свой API токен к каждой команде, которой он нужен в Poetry, мы сделаем это один раз с помощью команды config:

```
poetry config pypi-token.pypi your-api-token
```

Добавленный API токен будет использоваться как учетные данные. Poetry уведомит о том, что ваши учетные данные хранятся в простом текстовом файле. Если использовать обычное имя пользователя и пароль для учетных данных, то это будет небезопасно. Хранение токенов безопасно и удобно, так как они легко удаляются, обновляются и генерируются случайным образом. Но также можно вводить свой API токен вручную для каждой команды.

Далее нам нужно будет собрать и опубликовать пакет через команды:

```bash
poetry build
poetry publish
```

Если на этапе публикации выяснилось, что имя проекта занято, то измените в файле pyproject.toml название проекта, а далее согласно ему измените директорию модуля, и заново запустите сборку и публикацию.

Вы можете просмотреть свои созданные проекты [по ссылке](https://pypi.org/manage/projects/).

В итоге, кстати, мой pyproject.toml получился такой:

```toml
[tool.poetry]
name = "pycolor_palette-loguru"
version = "0.1.2"
description = "Python library for color beautiful output and logging"
authors = ["Alexeev Bronislav <alexeev.dev@inbox.ru>"]
readme = "README.md"

[project]
name = "pycolor_palette-loguru"
description = "Python library for color beautiful output and logging"
readme = "README.md"
requires-python = ">=3.9"
keywords = ["color", 'icecream', 'loguru', 'logging', 'pycolor', "palette"]
license = {text = "MIT License"}
dynamic = ["version"]

[tool.poetry.dependencies]
python = "^3.12"
rich = "^13.8.1"
ruff = "^0.6.8"
loguru = "^0.7.2"
pygments = "^2.18.0"
colorama = "^0.4.6"
executing = "^2.1.0"
asttokens = "^2.4.1"
pytest = "^8.3.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# Exclude a variety of commonly ignored directories.
exclude = [
    ".bzr",
    ".direnv",
    ".eggs",
    ".git",
    ".git-rewrite",
    ".hg",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".nox",
    ".pants.d",
    ".pyenv",
    ".pytest_cache",
    ".pytype",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    ".vscode",
    "__pypackages__",
    "_build",
    "buck-out",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
]

# Same as Black.
line-length = 88
indent-width = 4

# Assume Python 3.8
target-version = "py38"

[lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
select = ["E4", "E7", "E9", "F"]
ignore = []

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[format]
# Like Black, use double quotes for strings.
quote-style = "double"

# Like Black, indent with spaces, rather than tabs.
indent-style = "space"

# Like Black, respect magic trailing commas.
skip-magic-trailing-comma = false

# Like Black, automatically detect the appropriate line ending.
line-ending = "auto"
```

---

Вы можете установить мою реализацию следующей командой:

```bash
pip3 install justproj_toolkit
```

# Заключение
Я надеюсь вам понравилась моя статья. Эта статья первая, во второй я исправлю недочеты, добавлю больше функционала и исправлю возможные ошибки.

Если у вас есть вопросы или предложения, пишите в комментарии, рад буду выслушать.

Репозиторий исходного кода доступен по [ссылке](https://github.com/alexeev-prog/JustProj).

Буду рад, если вы присоединитесь к моему небольшому [телеграм-блогу](https://t.me/hex_warehouse). Анонсы статей, новости из мира IT и полезные материалы для изучения программирования и смежных областей.
