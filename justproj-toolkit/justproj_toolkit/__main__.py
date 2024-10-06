from justproj_toolkit.baseproject.documentation import InitiationSection, DocumentSubsection, DocumentFolder, ProjectManager, ProjectTemplate

project_name = input('Project name > ')
project_short_description = input('Project short description > ')
project_description = input("Project description > ")

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
