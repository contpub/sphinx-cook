# -*- coding: utf-8 -*-

import sys, os, codecs

# Read index.rst configurations
lines = codecs.open('index.rst', 'r', 'utf-8').readlines()
rstconf = {}

rstconf['project'] = 'project'
rstconf['copyright'] = 'copyright'
rstconf['version'] = '1.0'
rstconf['release'] = '1.0'
rstconf['title'] = 'title'
rstconf['authors'] = 'authors'
rstconf['publisher'] = 'ContPub'
rstconf['basename'] = 'project'
rstconf['identifier'] = 'http://contpub.org/'

rstconf['latex_paper_size'] = 'a4'
rstconf['latex_font_size'] = '12pt'
rstconf['latex_documents_target_name'] = None
rstconf['latex_documents_title'] = None
rstconf['latex_documents_author'] = None
rstconf['latex_logo'] = None

rstconf['epub_basename'] = None
rstconf['epub_title'] = None
rstconf['epub_author'] = None
rstconf['epub_publisher'] = None
rstconf['epub_copyright'] = None
rstconf['epub_identifier'] = None
rstconf['epub_scheme'] = None
rstconf['epub_cover'] = ()

for line in lines:
	if line[:4] == '   @':
		idx = line.find(':')
		rstconf[line[4:idx]] = line[idx+2:len(line)-1]

if rstconf['latex_documents_target_name'] is None:
	rstconf['latex_documents_target_name']=rstconf['basename']+'.tex'
if rstconf['latex_documents_title'] is None:
	rstconf['latex_documents_title']=rstconf['title']
if rstconf['latex_documents_author'] is None:
	rstconf['latex_documents_author']=rstconf['authors']

if rstconf['epub_basename'] is None:
	rstconf['epub_basename']=rstconf['basename']
if rstconf['epub_title'] is None:
	rstconf['epub_title']=rstconf['title']
if rstconf['epub_author'] is None:
	rstconf['epub_author']=rstconf['authors']
if rstconf['epub_publisher'] is None:
	rstconf['epub_publisher']=rstconf['publisher']
if rstconf['epub_copyright'] is None:
	rstconf['epub_copyright']=rstconf['copyright']
if rstconf['epub_identifier'] is None:
	rstconf['epub_identifier']=rstconf['identifier']
if rstconf['epub_scheme'] is None:
	rstconf['epub_scheme']=rstconf['identifier']

#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

#needs_sphinx = '1.0'
extensions = []

templates_path = ['_templates']

source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'
project = rstconf['project']
copyright = rstconf['copyright']
version = rstconf['version']
release = rstconf['release']

#language = 'zh_TW'
#today = ''
#today_fmt = '%B %d, %Y'

exclude_patterns = ['_build']

#default_role = None
#add_function_parentheses = True
#add_module_names = True
#show_authors = False
pygments_style = 'sphinx'

#modindex_common_prefix = []

# -- Options for LaTeX output --------------------------------------------------

#latex_paper_size = 'letter'
latex_paper_size = rstconf['latex_paper_size']

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'
latex_font_size = rstconf['latex_font_size']

latex_documents = [
  ('index',
   rstconf['latex_documents_target_name'],
   rstconf['latex_documents_title'],
   rstconf['latex_documents_author'], 'manual'),
]

latex_logo = rstconf['latex_logo']

#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False

latex_preamble = '''\\usepackage[cm-default]{fontspec}
\\usepackage{xunicode}
\\usepackage{xcolor}
\\usepackage{fontspec}
\\usepackage{titlesec}
\\usepackage{fancyvrb,relsize}
\\usepackage[slantfont,boldfont]{xeCJK}
\\XeTeXlinebreaklocale "zh"
\\XeTeXlinebreakskip = 0pt plus 1pt
\\setmainfont[BoldFont=Apple LiGothic Medium]{Apple LiSung Light}
\\setCJKmainfont[BoldFont=Apple LiGothic Medium]{Apple LiSung Light}
\\setromanfont[BoldFont=Apple LiGothic Medium]{Apple LiSung Light}
\\setmonofont{Monaco}
\\renewcommand{\\baselinestretch}{1.25}
\\DefineVerbatimEnvironment{Verbatim}{Verbatim}{numbers=left, fontsize=\\relsize{-1}}
'''

#latex_appendices = []
#latex_domain_indices = True

# -- Options for ePub output --------------------------------------------------
epub_basename = rstconf['epub_basename']
epub_title = rstconf['epub_title']
epub_author = rstconf['epub_author']
epub_publisher = rstconf['epub_publisher']
epub_copyright = rstconf['epub_copyright']
epub_identifier = rstconf['epub_identifier']
epub_scheme = rstconf['epub_scheme']
epub_cover = rstconf['epub_cover']


