interest_in_computer_science = input("Are you interested in computer science? (y/n): ").lower() == 'y'
like_playing_computer_games = input("Do you like playing computer games? (y/n): ").lower() == 'y'
has_instagram_account = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print("\nSURVEY RESULTS:")
print(f"Interested in computer science: {'Yes' if interest_in_computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if like_playing_computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram_account else 'No'}")