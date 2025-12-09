# CodE Alltag<sub>XL</sub> GERMAN

CodE Alltag<sub>XL</sub> GERMAN is part of CodE Alltag, a German-language email corpus. It contains ~241.000 automatically pseudonymized emails on topics related to the German language.

CodE Alltag<sub>XL</sub> has been extracted from Usenet newsgroups and underwent merely rudimentary data cleansing. Although no demographic information on the authors has been collected, CodE Alltag<sub>XL</sub> is likely to contain a gender bias since taggers recognized more mentions of male given names (either authors or persons written about).

## Data Formats

The dataset is available in two formats:

1. **Individual Text Files**: Original format with 240,673 emails stored as separate `.txt` files in a hierarchical directory structure (directories `1-` through `9-`)
2. **CSV Format**: All emails consolidated in a single CSV file (`emails_dataset.csv`, ~88MB) with columns for file_id, directory, and email_text. See [CSV_FORMAT.md](CSV_FORMAT.md) for detailed documentation.

The CSV file is included in the repository and can be downloaded directly. Alternatively, to regenerate the CSV file from the text files, run:
```bash
python3 convert_to_csv.py
```

CodE Alltag<sub>XL</sub> is further described in the following papers:

```
@inproceedings{krieg-holz-etal-2016,
    title = "{C}od{E} Alltag: A {G}erman-Language {E}-Mail Corpus",
    author = "Krieg-Holz, Ulrike  and
      Schuschnig, Christian  and
      Matthies, Franz  and
      Redling, Benjamin  and
      Hahn, Udo",
    booktitle = "Proceedings of the Tenth International Conference on Language Resources and Evaluation ({LREC}'16)",
    month = may,
    year = "2016",
    address = "Portoro{\v{z}}, Slovenia",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/L16-1404",
    pages = "2543--2550",
}

@inproceedings{eder-etal-2020,
    title = "{C}od{E} Alltag 2.0 {---} A Pseudonymized {G}erman-Language Email Corpus",
    author = "Eder, Elisabeth  and
      Krieg-Holz, Ulrike  and
      Hahn, Udo",
    booktitle = "Proceedings of the Twelfth Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2020.lrec-1.550",
    pages = "4466--4477",
}

@inproceedings{eder-etal-2022,
    title = {{``}Beste Gr{\"u}{\ss}e, Maria Meyer{''} {---} Pseudonymization of Privacy-Sensitive Information in Emails},
    author = "Eder, Elisabeth  and
      Wiegand, Michael  and
      Krieg-Holz, Ulrike  and
      Hahn, Udo",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.79",
    pages = "741--752",
}
```
