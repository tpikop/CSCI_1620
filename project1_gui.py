import tkinter as tk
from tkinter import messagebox
from typing import Optional, Tuple

class GUI:
    def __init__(self):
        self.vote_result: Optional[Tuple[str, str]] = None

    def vote_menu(self) -> Optional[Tuple[str, str]]:
        """Display the vote menu and return the user's vote result.

        Returns:
            Optional[Tuple[str, str]]: A tuple containing the user's name and vote option.
                Returns None if the vote is invalid or the user cancels the operation.
        """
        root = tk.Tk()
        root.title("VOTE MENU")
        root.geometry("300x150")

        name_var = tk.StringVar()
        option_var = tk.StringVar()
        self.vote_result = None

        def vote() -> None:
            """Process the user's vote."""
            name = name_var.get().strip()
            option = option_var.get().strip().lower()

            if name:
                if option in ['v', 'x']:
                    root.destroy()
                    self.vote_result = (name, option)
                else:
                    messagebox.showwarning("Invalid Option", f"Invalid option (v/x): {option}")
                    self.vote_result = (name, 'invalid')  # Mark the vote as invalid
            else:
                messagebox.showwarning("Missing Name", "Please enter a name.")

        tk.Label(root, text="Name:").pack(pady=10)
        tk.Entry(root, textvariable=name_var).pack(pady=10)
        tk.Label(root, text="Vote (v/x):").pack(pady=10)
        tk.Entry(root, textvariable=option_var).pack(pady=10)
        tk.Button(root, text="Vote", command=vote).pack(pady=10)

        root.mainloop()

        return self.vote_result

    def candidate_menu(self) -> Optional[str]:
        """Display the candidate menu and return the user's selected candidate.

        Returns:
            Optional[str]: A string representing the user's selected candidate.
                Returns None if the user cancels the operation.
        """
        root = tk.Tk()
        root.title("CANDIDATE MENU")
        root.geometry("300x150")

        candidate_result = None  # Variable to store the candidate selection

        def select_candidate(candidate: str) -> None:
            """Process the user's selected candidate."""
            nonlocal candidate_result
            candidate_result = candidate
            root.destroy()

        tk.Button(root, text="John", command=lambda: select_candidate('1')).pack(pady=10)
        tk.Button(root, text="Jane", command=lambda: select_candidate('2')).pack(pady=10)

        root.mainloop()

        return candidate_result
