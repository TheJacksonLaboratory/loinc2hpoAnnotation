import csv



def get_nominal(row):
    return "?"

def get_curated_date(date):
    """
    remove the seconds etc, e.g.,  2018-07-15T16:20:55 => 2018-07-15
    """
    return date.strip().split('T')[0]

# transform to HPO:skoehler[2018-10-08] or HPO:skoehler[2018-10-08];JGM:azhang[2020-12-14]
def get_biocurated(row):
    createdOn = row['createdOn'] # e.g., '2018-07-15T16:20:55'
    createdBy = row['createdBy'] # e.g., 'JGM:azhang', 'lastEditedOn': '2018-09-28T14:38:47', '': 'JGM:azhang',
    lastEditedOn = row['lastEditedOn']
    lastEditedBy = row['lastEditedBy']
    curation_date = get_curated_date(createdOn)
    curated = "{}[{}]".format(createdBy, curation_date)
    if lastEditedOn != 'NA':
        curated = curated + ";{}[{}]".format(lastEditedBy, get_curated_date(lastEditedOn))
    return curated

def get_version(row):
    v = float(row['version'])
    v *= 10
    return str(int(v))


def get_outcome_and_code(row):
    code = row['code']
    system = row['system']
    valid_outcomes = {'H','L', 'N', 'POS','NEG'}
    if code in valid_outcomes:
        return code
    if system == 'snomed-ct':
        return "SNOMEDCT:{}".format(code)
    else:
        raise ValueError("Could not recognize code " + "-".join(row))


def process_comment(comment):
    if 'copied from' in comment and comment.endswith("@original comment:"):
        return "."
    elif comment == 'NA':
        return "."
    else:
        return comment




def print_row(row):
    id = row['loincId']
    scale = row['loincScale']
    code = row['code']
    hpoTermId = row['hpoTermId']
    isNegated = row['isNegated'] == True
    createdOn = row['createdOn']
    createdBy = row['createdBy']
    if isNegated:
        neg = "(negated)"
    else:
        neg = ""
    print("{} ({}/{}): {} {}; {}[{}]".format(id, scale, code, hpoTermId, neg, createdBy, createdOn))

header = ['loincId', 'loincScale', 'outcome', 'hpoTermId', 'supplementalTermId','curation', 'comment']
fh = open('loinc2hpo-annotations.tsv', 'wt')
fh.write("\t".join(header) + "\n")
acceptableScales = {'Qn', 'Ord', 'Nom'}


with open('annotations.tsv') as f:
    csvreader = csv.DictReader(f, delimiter='\t')
    for row in csvreader:
        isFinal = row['isFinalized']
        if isFinal != 'true':
            print(row)
            raise ValueError("Line was not finalized")
        
        if row['code'] == 'A':
            continue # Skip the A annotations since they are redundant compared to 'N'
        system = row['system']
        curated = get_biocurated(row)
        outcome = get_outcome_and_code(row)
        supplement = '.'
        comment = process_comment(row['comment'])
        scale = row['loincScale']
        if scale not in acceptableScales:
            print("Skipping annotation because scale=={}".format(scale))
            print_row(row)
            continue
        fields = [row['loincId'], row['loincScale'], outcome, row['hpoTermId'], supplement, curated, comment]
        fh.write("\t".join(fields) + "\n")
fh.close()

