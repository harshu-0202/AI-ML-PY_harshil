import os
import datetime

class JournalManager:
    
    FILENAME = "journal.txt"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def _get_timestamp(self):
        return datetime.datetime.now().strftime(self.DATE_FORMAT)

    def add_entry(self):
        
        entry_text = input("\nEnter your journal entry:\n")
        timestamp = self._get_timestamp()
        try:
            with open(self.FILENAME, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {entry_text}\n")
            print("Journal entry added successfully.")
        except IOError as e:
            print(f"Error adding entry: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_all_entries(self):
        
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as f:
                content = f.read()
                if content:
                    print("\n========== All Journal Entries ==========")
                    print(content.strip())
                    print("=========================================")
                else:
                    print("Journal is empty. Add some entries!")
        except FileNotFoundError:
            print("No journal entries found. The file 'journal.txt' does not exist yet.")
        except IOError as e:
            print(f"Error reading entries: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_entry(self):
        
        keyword = input("\nEnter keyword or date to search: ").lower()
        found_entries = []
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    if keyword in line.lower():
                        found_entries.append(f"Line {i}: {line.strip()}")

            if found_entries:
                print(f"\n========== Search Results for '{keyword}' ==========")
                for entry in found_entries:
                    print(entry)
                print("==================================================")
            else:
                print(f"No entries found containing '{keyword}'.")
        except FileNotFoundError:
            print("No journal entries found. The file 'journal.txt' does not exist yet.")
        except IOError as e:
            print(f"Error searching entries: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_all_entries(self):
        
        if os.path.exists(self.FILENAME):
            confirmation = input(f"Are you sure you want to delete all entries in '{self.FILENAME}'? (yes/no): ").lower()
            if confirmation == 'yes':
                try:
                    os.remove(self.FILENAME)
                    print("All journal entries deleted successfully.")
                except PermissionError:
                    print(f"Permission denied: Could not delete '{self.FILENAME}'. Please check file permissions.")
                except OSError as e:
                    print(f"Error deleting file: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print("Deletion cancelled.")
        else:
            print("No journal file found to delete.")

    def run(self):
        
        while True:
            print("\n========== PERSONAL JOURNAL MENU ==========")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")
            print("===========================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_all_entries()
            elif choice == "3":
                self.search_entry()
            elif choice == "4":
                self.delete_all_entries()
            elif choice == "5":
                print("Exiting Personal Journal. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    journal_app = JournalManager()
    journal_app.run()