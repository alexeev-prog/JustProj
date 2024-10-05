import os
from abc import ABC, abstractmethod, ABCMeta
from uuid import uuid4
from typing import Dict, List, Tuple, Callable, Any
from pycolor_palette_loguru import info_message, debug_message, warn_message, error_message
from rich import print as pprint

from justproj_toolkit.utils import get_current_datetime


class DocumentSubsection(ABC):
	"""
	This class describes a document subsection.
	"""
	__metaclass__ = ABCMeta

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


class DocumentSection(ABC):
	"""
	This abstract metaclass describes a documentation section.
	"""
	__metaclass__ = ABCMeta

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
		self.title = title
		self.introduction = introduction
		self.content = content
		self.linked_sections = {}
		self.linked_subsections = {}
		self.creation_date = get_current_datetime()
		self.modification_date = self.creation_date


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


class DocumentManager:
	"""
	This class describes a document manager.
	"""

	def __init__(self, project_name: str, project_description: str, project_root_dir: str, folders: List[DocumentFolder]):
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
		self.project_description = project_description
		self.project_root_dir = project_root_dir
		self.folders = folders

		os.makedirs(self.project_root_dir, exist_ok=True)

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
