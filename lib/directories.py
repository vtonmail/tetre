"""Directory folders

This directory is a configuration file for all paths used by this application.

Todo:
    * Remove old style global variable filenames and use dictionary structure instead.

"""

dirs = {
    'models':                   {'path': 'models/'},
    'config':                   {'path': 'config/'},
    'annotated':                {'path': 'data/input/training/annotated/'},
    'transformed':              {'path': 'data/input/training/transformed/'},
    'microsoft_data':           {'path': 'data/input/training/gazette/microsoft_academic_data/'},
    'downloaded':               {'path': 'data/input/downloaded/text/'},
    'raw_input':                {'path': 'data/input/raw/'},
    'google_parsey_path':       {'path': 'external/bin/parsey/models/syntaxnet', 'root_distance': '../../../../../'},
    'stanford_ner_path':        {'path': 'external/bin/stanford/ner/'},
    'stanford_corenlp_path':    {'path': 'external/bin/stanford/corenlp/'},
    'output_openie':            {'path': 'data/output/openie/'},
    'output_rel':               {'path': 'data/output/rel/'},
    'output_ngram':             {'path': 'data/output/ngram/'},
    'output_html':              {'path': 'data/output/html/'},
    'output_cache':             {'path': 'data/output/cache/'},
    'output_comparison':        {'path': 'data/output/comparison/sentences/'},
    'output_allenai_openie':    {'path': 'data/output/comparison/allenai_openie/'},
    'output_stanford_openie':   {'path': 'data/output/comparison/stanford_openie/'},
    'output_mpi_clauseie':      {'path': 'data/output/comparison/mpi_clauseie/'},
    'html_templates':           {'path': 'templates/'}
}


models = 'models/'
config = 'config/'

annotated       = 'training/annotated/'
transformed     = 'training/transformed/'
microsoft_data  = 'training/gazette/microsoft_academic_data/'

downloaded = 'downloaded/'

google_parsey_path  = 'parsey/models/syntaxnet/'
stanford_path       = 'stanford/stanford-corenlp-full-2015-12-09/'

output_openie   = 'output/openie/'
output_rel      = 'output/rel/'
output_ngram    = 'output/ngram/'
output_html     = 'output/html/'
output_cache    = 'output/cache/'

output_comparison       = 'output/comparison/sentences/'
output_allenai_openie   = 'output/comparison/allenai_openie/'
output_stanford_openie  = 'output/comparison/stanford_openie/'
output_mpi_clauseie     = 'output/comparison/mpi_clauseie/'

raw_input = 'input/'

html_templates = 'templates/'
