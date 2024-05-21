# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"E116500","system":"readv2"},{"code":"E117000","system":"readv2"},{"code":"E115000","system":"readv2"},{"code":"Eu31z00","system":"readv2"},{"code":"E117500","system":"readv2"},{"code":"E115500","system":"readv2"},{"code":"E117400","system":"readv2"},{"code":"E117300","system":"readv2"},{"code":"E117200","system":"readv2"},{"code":"E116000","system":"readv2"},{"code":"E117z00","system":"readv2"},{"code":"E117.00","system":"readv2"},{"code":"E117600","system":"readv2"},{"code":"E117100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bipolar-affective-disorder-and-mania-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bipolar-affective-disorder-and-mania-unspec---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bipolar-affective-disorder-and-mania-unspec---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bipolar-affective-disorder-and-mania-unspec---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
