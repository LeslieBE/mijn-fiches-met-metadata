import os
import yaml
import pandas as pd

def parse_yaml_files(directory):
    """
    Parses all YAML files in a given directory and collects their data.

    Args:
        directory (str): The path to the directory containing YAML files.

    Returns:
        list: A list of dictionaries, where each dictionary represents the data from one YAML file.
    """
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith((".yaml", ".yml")):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data: # Zorg ervoor dat het bestand niet leeg is
                        all_data.append(data)
            except yaml.YAMLError as e:
                print(f"Fout bij het parsen van {filename}: {e}")
            except Exception as e:
                print(f"Algemene fout bij het verwerken van {filename}: {e}")
    return all_data

def export_data(data, csv_output_file, xlsx_output_file):
    """
    Exports a list of dictionaries to CSV and XLSX formats.

    Args:
        data (list): A list of dictionaries containing the data.
        csv_output_file (str): The path for the output CSV file.
        xlsx_output_file (str): The path for the output XLSX file.
    """
    if not data:
        print("Geen data gevonden om te exporteren.")
        return

    # Gebruik pandas DataFrame voor eenvoudige export
    df = pd.DataFrame(data)

    # Exporteer naar CSV
    try:
        df.to_csv(csv_output_file, index=False, encoding='utf-8')
        print(f"Data succesvol geëxporteerd naar {csv_output_file}")
    except Exception as e:
        print(f"Fout bij het exporteren naar CSV: {e}")

    # Exporteer naar XLSX
    try:
        df.to_excel(xlsx_output_file, index=False, engine='openpyxl')
        print(f"Data succesvol geëxporteerd naar {xlsx_output_file}")
    except Exception as e:
        print(f"Fout bij het exporteren naar XLSX: {e}")

if __name__ == "__main__":
    # De map waar je YAML fiches staan.
    # Als dit script in de root van je repository staat en je fiches in een map 'fiches',
    # dan is dit 'fiches'.
    # Pas dit pad aan naar de daadwerkelijke locatie van je YAML bestanden.
    yaml_directory = 'fiches' # Voorbeeld: 'fiches' of '.' als ze in dezelfde map staan

    # Output bestandsnamen
    output_csv_file = 'output_fiches.csv'
    output_xlsx_file = 'output_fiches.xlsx'

    print(f"Starten met parsen van YAML-bestanden in '{yaml_directory}'...")
    parsed_data = parse_yaml_files(yaml_directory)

    if parsed_data:
        print(f"Aantal fiches gevonden: {len(parsed_data)}")
        export_data(parsed_data, output_csv_file, output_xlsx_file)
    else:
        print("Geen YAML-bestanden geparsed of geen data gevonden.")
