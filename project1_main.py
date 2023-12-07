from gui import GUI
from typing import Dict

class VotingSystem:
    def __init__(self):
        self.votes: Dict[str, str] = {}
        self.gui = GUI()

    def main(self) -> None:
        """Run the main voting system."""
        while True:
            result = self.gui.vote_menu()

            if result:
                name, option = result

                if option == 'v':
                    while True:
                        candidate = self.gui.candidate_menu()
                        if candidate == '1':
                            self.votes[name] = 'John'
                            print(f"{name} voted for John\n")
                            break
                        elif candidate == '2':
                            self.votes[name] = 'Jane'
                            print(f"{name} voted for Jane\n")
                            break
                elif option == 'x':
                    self.display_vote_details()
                    self.export_to_csv()
                    break

    def display_vote_details(self) -> None:
        """Display the details of the votes."""
        print("\nVote Details:")
        for user, vote in self.votes.items():
            print(f"{user} voted for {vote}")

    def export_to_csv(self) -> None:
        """Export the vote results to a CSV file."""
        with open('vote_results.csv', 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Vote']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for user, vote in self.votes.items():
                writer.writerow({'Name': user, 'Vote': vote})

        print("Vote results exported to vote_results.csv")

if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.main()
