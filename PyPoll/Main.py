def main():
    import pandas as pd
    import csv
    import os

    election_data = os.path.join("Resources", "election_data_2.csv")
    election_data_df = pd.read_csv(election_data, encoding="ISO-8859-1")
    election_data_df_noHead = pd.read_csv(election_data, encoding="ISO-8859-1", skiprows=1, header=None)

    num_of_votes = len(election_data_df_noHead)

    candidate_array = election_data_df['Candidate'].unique()
    cand1 = candidate_array[0]
    cand2 = candidate_array[1]
    cand3 = candidate_array[2]
    cand4 = candidate_array[3]

    cand1_count = 0
    cand2_count = 0
    cand3_count = 0
    cand4_count = 0

    with open(election_data, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        for row in csv_reader:
            if row[2] == str(cand1):
                cand1_count = cand1_count + 1
            if row[2] == str(cand2):
                cand2_count = cand2_count + 1
            if row[2] == str(cand3):
                cand3_count = cand3_count + 1
            if row[2] == str(cand4):
                cand4_count = cand4_count + 1

    highest_vote_count = 0
    election_winner = "No one"

    if cand1_count > cand2_count:
        highest_vote_count = cand1_count
        election_winner = str(cand1)
    if cand2_count > cand1_count:
        highest_vote_count = cand2_count
        election_winner = str(cand2)
    if cand3_count > highest_vote_count:
        highest_vote_count = cand3_count
        election_winner = str(cand3)
    if cand4_count > highest_vote_count:
        highest_vote_count = cand4_count
        election_winner = str(cand4)

    prop_of_cand1_votes = (cand1_count / num_of_votes)
    prop_of_cand2_votes = (cand2_count / num_of_votes)
    prop_of_cand3_votes = (cand3_count / num_of_votes)
    prop_of_cand4_votes = (cand4_count / num_of_votes)

    perc_of_cand1_votes = '{:.1%}'.format(prop_of_cand1_votes)
    perc_of_cand2_votes = '{:.1%}'.format(prop_of_cand2_votes)
    perc_of_cand3_votes = '{:.1%}'.format(prop_of_cand3_votes)
    perc_of_cand4_votes = '{:.1%}'.format(prop_of_cand4_votes)

    print("Election Results")
    print("-------------------------")
    print(str(cand1) + ": " + str(perc_of_cand1_votes) + " " + "(" + str(cand1_count) + ")")
    print(str(cand2) + ": " + str(perc_of_cand2_votes) + " " + "(" + str(cand2_count) + ")")
    print(str(cand3) + ": " + str(perc_of_cand3_votes) + " " + "(" + str(cand3_count) + ")")
    print(str(cand4) + ": " + str(perc_of_cand4_votes) + " " + "(" + str(cand4_count) + ")")
    print("-------------------------")
    print("Winner: " + election_winner)
    print("-------------------------")
main()
