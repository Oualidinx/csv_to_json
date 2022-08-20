import json, csv, os, sys

if __name__=="__main__":
    if not sys.argv[1]:
        raise Exception('You need to add the dir path')
    try:
        dictionary = dict(columns=[], data=[])
        root_dir = os.chdir(sys.argv[1])
        current_file_dir = os.curdir
        if "output_files" not in os.listdir(root_dir):
            os.mkdir('output_files')
        print("Working on it...")
        for filename in os.listdir(root_dir):
            if filename.endswith(".csv"):
                print(f"loading {filename} ...",end="")
                with open(filename, "r") as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=",")
                    dictionary['columns']=list(csv_reader.fieldnames)
                    for row in csv_reader:
                        dict_row = dict()
                        for column in csv_reader.fieldnames:
                            dict_row[column] = row[column]
                        dictionary['data'].append(dict_row)
                print("done!")
                print(f'creating {filename.split(".")[0]}.json file...', end="")
                output_file = open(f'output_files/{filename.split(".")[0]}.json','w')
                json.dump(dictionary, output_file, indent=4)
                print('done!')       
        print(f'Output files generated successfully! \nyou can find them in ##{os.path.abspath("output_files")}## directory')
    except Exception as exception:
        print(str(exception))