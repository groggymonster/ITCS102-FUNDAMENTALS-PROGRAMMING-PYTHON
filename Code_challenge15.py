anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ").strip()
    
    if anime.lower() == 'exit':
        print("You have exited the anime entry program.\n")
        break
    else:
        anime_list.append(anime)
        print(f"'{anime}' has been added to your anime list.")

print("Here is your anime list:")
for index, title in enumerate(anime_list, start=1):
    print(f"{index}. {title}")
