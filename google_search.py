
import webbrowser
from googlesearch import search
def google_search():
    # to search
    query = input("Enter your google search: ")

    results = {}
    # Perform the search and store results in the dictionary
    for i, result in enumerate(search(query, num_results=10), start=1):
        results[i] = result

    # Print the results
    for key, value in results.items():
        print(f"{key}: {value}")

    user_inp = input("Enter the number of the link you want to open: ")
    print("Opening", results[int(user_inp)])
    webbrowser.open(results[int(user_inp)])