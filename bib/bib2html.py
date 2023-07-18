import bibtexparser
import re

def _author_fmt(author):
    """Format an author's full name."""
    return author


def _andlist(ss, sep=', ', seplast=', and ', septwo=' and '):
    """Comma-separate a list of strings according to English rules.

    Enforces the Oxford comma.
    """
    if len(ss) <= 1:
        return ''.join(ss)
    if len(ss) == 2:
        return septwo.join(ss)
    return sep.join(ss[:-1]) + seplast + ss[-1]


def _author_list(authors):
    """Format a list of authors."""
    return _andlist(list(map(_author_fmt, authors)))


def _venue_type(entry):
    """Expand a venue type to a longer English description."""
    venuetype = ''
    if entry['ENTRYTYPE'] == 'inbook':
        venuetype = 'Chapter in '
    elif entry['ENTRYTYPE'] == 'techreport':
        venuetype = 'Technical Report '
    elif entry['ENTRYTYPE'] == 'phdthesis':
        venuetype = f'Ph.D. thesis, {entry["school"]}'
    elif entry['ENTRYTYPE'] == 'mastersthesis':
        venuetype = f'Master\'s thesis, {entry["school"]}'
    return venuetype


def _venue(entry):
    """Format an entry's venue data."""
    f = entry
    venue = ''
    if entry['ENTRYTYPE'] == 'article':
        venue = f['journal']
        try:
            if f['volume'] and f['number']:
                venue += ' {0}({1})'.format(f['volume'], f['number'])
        except KeyError:
            pass
    elif entry['ENTRYTYPE'] == 'inproceedings':
        venue = f['booktitle']
    elif entry['ENTRYTYPE'] == 'inbook':
        venue = f['title']
    elif entry['ENTRYTYPE'] == 'techreport':
        venue = '{0}, {1}'.format(f['number'], f['institution'])
    elif entry['ENTRYTYPE'] == 'phdthesis' or entry['ENTRYTYPE'] == 'mastersthesis':
        venue = ''
    else:
        venue = 'Unknown venue (type={})'.format(entry['ENTRYTYPE'])

    # remove curlies from venues -- useful in TeX, not here
    venue = venue.replace('{','').replace('}','')
    return venue


def _title(entry):
    """Format a title field for HTML display."""
    title = entry['title']
    # remove curlies from titles -- useful in TeX, not here
    title = re.sub(r"[^\(\)a-zA-Z가-힣0-9 ,_-]","",title)
    return title


def _main_url(entry):
    """Get an entry's URL field (url or ee)."""
    entry['url'] = f"https://lifs.hallym.ac.kr/pubs/{entry['ID'].lower()}.pdf"
    return entry['url']


def _sortkey(entry):
    """Generate a sorting key for an entry based on its date."""
    year = '{:04d}'.format(int(entry['year']))
    return year


import jinja2
import jinja2.sandbox

def verify_skip_year(entries):
    prev_year = 1900
    for entry in entries:
        if int(entry['year']) != prev_year:
            entry['skip_year'] = 'false'
            prev_year = int(entry['year'])
        else:
            entry['skip_year'] = 'true'
    return entries
    

def build_pubs_html(db,out_path):
    # Load the HTML template
    with open('publications.tmpl',"r",encoding="utf8") as template:
        # template = jinja2.Template(f.read())
        """Render a BibTeX .bib file to HTML using an HTML template."""
        tenv = jinja2.sandbox.SandboxedEnvironment()
        tenv.filters['author_fmt'] = _author_fmt
        tenv.filters['title'] = _title
        tenv.filters['venue_type'] = _venue_type
        tenv.filters['venue'] = _venue
        tenv.filters['main_url'] = _main_url
        tmpl = tenv.from_string(template.read())

    bib_sorted = sorted(db.entries, key=_sortkey, reverse=True)
    bib_sorted = verify_skip_year(bib_sorted)
    html = tmpl.render(entries=bib_sorted)
    # Write the HTML to the output file
    with open(f'{out_path}/pubs.html', 'w',encoding="utf8") as f:
        f.write(html)    

def build_single_html(db,out_path):
    with open('singlePage.tmpl',"r",encoding="utf8") as single_tp:
    # template = jinja2.Template(f.read())
        tenv = jinja2.sandbox.SandboxedEnvironment()
        tenv.filters['title'] = _title
        tenv.filters['venue_type'] = _venue_type
        tenv.filters['venue'] = _venue
        tenv.filters['main_url'] = _main_url
        tmpl = tenv.from_string(single_tp.read())
    for entry in db.entries:
        html = tmpl.render(entries=entry)
        title = _title(entry)
        titleus = title.replace(" ","_")
        year = entry['year']
        #titleus must match link in pubs.html
        holders = ["---","layout: default",f"title: {title}",f"permalink: /publications/{year}-{titleus}","---"]
        place_holder = "\n".join(holders)
        with open(f"{out_path}/{year}-{titleus}.html","w",encoding="utf8") as fw:
            fw.write(place_holder + "\n")
            fw.write(html)

'''
conda activate lifsblog
Creates html table for _includes/pubs.html --> creates permalinks as href, must match permalink in single page
Creates single pages with keywords and abstract in pubs/html

MUST verify alum link in people.yml
'''


def convert_bib_to_html(bib_file):
    # Parse the bib file
    with open(bib_file,"r",encoding="utf8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    build_pubs_html(bib_database, "../_includes")
    build_single_html(bib_database, "../pubs/html")
    
convert_bib_to_html("pubs.bib")