import bibtexparser
import yaml

POSSIBLE_TAGS = ['Hybrid devices', 'Vortex physics', 'CQED']

def read_bib_file(bib_file_path):
    with open(bib_file_path, 'r') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database

def clean_curly_brackets(text):
    return text.strip('{}')

def deduce_tags_from_title(title):
    tags = set()
    for possible_tag in POSSIBLE_TAGS:
        if possible_tag.lower() in title.lower():
            tags.add(possible_tag)

    return list(tags)

def convert_to_yaml(entry):
    tags_from_title = deduce_tags_from_title(entry['title'])

    doi_url = entry.get('doi', '')
    if doi_url:
        doi_url = f'http://doi.org/{doi_url}'

    yaml_entry = {
        'title': clean_curly_brackets(entry['title']),
        'authors': [{'name': clean_curly_brackets(author)} for author in entry['author'].split(' and ')],
        'publishedIn': {
            'name': entry['journal'],
            'date': f"{entry['month']} {entry['year']}",
            'url': doi_url
        },
        'paper': {
            'summary': entry.get('abstract', ''),
            'url': doi_url
        },
        'categories': tags_from_title.copy(),
        'tags': tags_from_title
    }
    return yaml_entry

def main():
    bib_file_path = 'publications.bib'  # Updated the BibTeX file name
    bib_database = read_bib_file(bib_file_path)

    # Sort entries by date in reverse chronological order
    bib_database.entries = sorted(bib_database.entries, key=lambda x: (x['year'], x['month']), reverse=True)

    publications = []
    for entry in bib_database.entries:
        yaml_entry = convert_to_yaml(entry)
        publications.append(yaml_entry)

    output_data = {'publications': publications}

    with open('publications.yaml', 'w') as output_file:  # Updated the output YAML file name
        yaml.dump(output_data, output_file, default_flow_style=False, indent=2)  # Added indentation for better readability

if __name__ == "__main__":
    main()
