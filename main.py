import SitesChecker

websites = [
    {
        'name': 'FitGirl_Repacks',
        'url': 'https://fitgirl-repacks.site/'
    },
    {
        'name': 'SteamRIP',
        'url': 'https://steamrip.com/'
    },
    {
        'name': 'AnkerGames',
        'url': 'https://ankergames.net/'
    },

]

def main():
    gameName = input("Enter the game name: ")

    for i, website in enumerate(websites, start=1):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"{i}. \nChecking {website['name']} @ {website['url']}")
        try:
            functionToCall = getattr(SitesChecker, website['name'])
            functionToCall(gameName)
        except Exception as e:
            print(f"Error occurred while checking {website['name']}: {e}")

        if(i < len(websites)):
            print("Moving onto the next website...")
        else:
            print("Finished!")

if __name__ == "__main__":
    main()

# TO DO:
# 1. Give the user a choice to output into a .txt file