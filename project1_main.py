from gui import GUI
import csv


class VotingSystem:
    def __init__(self):
        self.votes = {}
        self.gui = GUI()

    def main(self):
        while True:
            result = self.gui.vote_menu()

            if result:
                name, option = result

                if option == 'v':
                    while True:
                        candidate = self.gui.candidate_menu()
                        if candidate == '1':
                            self.votes[name] = 'John'
                            print("{} voted for John\n".format(name))
                            break
                        elif candidate == '2':
                            self.votes[name] = 'Jane'
                            print("{} voted for Jane\n".format(name))
                            break
                elif option == 'x':
                    self.display_vote_details()
                    self.export_to_csv()
                    break

    def display_vote_details(self):
        print("\nVote Details:")
        for user, vote in self.votes.items():
            print("{} voted for {}".format(user, vote))

    def export_to_txt(self):
        with open('vote_details.txt', 'w') as file:
            file.write('Name,Vote\n')
            for user, vote in self.votes.items():
                file.write('{},{}\n'.format(user, vote))
        print("Vote details exported to vote_details.txt")

    def export_to_csv(self):
        with open('vote_results.csv', 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Vote']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for user, vote in self.votes.items():
                writer.writerow({'Name': user, 'Vote': vote})

        print("Vote results exported to vote_results.csv")

        jane_count = 0
        john_count = 0

        with open('vote_results.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Vote'] == 'Jane':
                    jane_count += 1
                elif row['Vote'] == 'John':
                    john_count += 1

        with open('vote_results.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Count'])
            writer.writerow({})  # Empty row for better readability
            writer.writerow({'Name': 'Jane', 'Count': jane_count})
            writer.writerow({'Name': 'John', 'Count': john_count})

        print("Count exported to vote_results.csv")


if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.main()
