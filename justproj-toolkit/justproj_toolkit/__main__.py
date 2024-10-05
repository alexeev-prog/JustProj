from justproj_toolkit.baseproject.documentation import InitiationSection, DocumentSubsection, DocumentManager, DocumentFolder

s1 = InitiationSection('Introduction', 'An introduction to JustProj Toolkit', {'Language': 'Python with some libs'})
s2 = InitiationSection('Introduction 2', 'An another introduction number 2 to JustProj Toolkit', {'Number': 'version 2'})
ss1 = DocumentSubsection('InitiationSubSection', {'Test2': 'hi'}, s1)
ss2 = DocumentSubsection('InitiationSubSection 2', {'Test3': 'hi wpr;d'}, s2)
s1.link_new_subsection(ss1)
s2.link_new_subsection(ss2)

folder = DocumentFolder('basic', 'app', [s1, s2])

doc_manager = DocumentManager('JustProj Toolkit', 'Docs&Project manager', 'app', [folder])
doc_manager.generate_pages()
