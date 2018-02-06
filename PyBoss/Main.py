def main():
    import pandas as pd
    import csv
    import os

    first_names = []
    last_names = []
    DOBs = []
    SSNs = []
    states = []

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

    employee_data = os.path.join("Resources", "employee_data2.csv")
    employee_data_df = pd.read_csv(employee_data, encoding="ISO-8859-1")

    with open(employee_data, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        next(csv_reader, None)

        for row in csv_reader:
            # Split the names
            name = row[1]
            first, last = name.split(" ")
            first_names.append(first)
            last_names.append(last)

            # Change the dates
            date = row[2]
            year, month, day = date.split("-")
            new_date = (str(month) + "/" + str(day) + "/" + str(year))
            DOBs.append(new_date)

            # Change the SSNs
            social = row[3]
            part1, part2, part3 = social.split("-")
            new_social = ("***-**-" + str(part3))
            SSNs.append(new_social)

            # Change the State to and Abbreviation
            new_state = us_state_abbrev[str(row[4])]
            states.append(new_state)

    # Drop the old values
    employee_data_df = employee_data_df.drop(['Name', 'DOB', 'State', 'SSN'], axis=1)

    # Add the new values
    employee_data_df['First Names'] = first_names
    employee_data_df['Last Names'] = last_names
    employee_data_df['DOB'] = DOBs
    employee_data_df['SSN'] = SSNs
    employee_data_df['States'] = states

    # Write the CSV file
    employee_data_df.to_csv('out.csv', sep=',', index=False)
main()
