import tiktoken 
import colorama
from pricing import openai_pricing_input

def main():
    enc = tiktoken.get_encoding("cl100k_base")  # używany w GPT-3.5 i GPT-4

    print("Available models:" )
    for m in openai_pricing_input:
        print(f"- {m}")

    model = input(colorama.Fore.BLUE + "\nSelect a model: " + colorama.Fore.RESET).strip()

    if model not in openai_pricing_input:
        print(colorama.Fore.RED + "Invalid model! Defaulting to gpt-3.5-turbo." + colorama.Fore.RESET)
        model = "gpt-3.5-turbo"

    while True:
        print("\n" + "="*50)
        print(colorama.Fore.YELLOW + f"Welcome to the token cost meter for {model}" + colorama.Fore.RESET)
        text = input(colorama.Fore.BLUE + "Write your text here (or 'quit' to exit): " + colorama.Fore.RESET)

        
        if text == "quit":
            print(colorama.Fore.RED + "Goodbye!" + colorama.Fore.RESET)
            break

        if text.strip():
            tokens = enc.encode(text)
            token_count = len(tokens)

            price_per_minilion = openai_pricing_input[model]
            cost = (token_count / 1000000) * price_per_minilion
            print(colorama.Fore.GREEN + str(tokens) + colorama.Fore.RESET)    # lista ID tokenów
            print(colorama.Fore.RED + f"Token count: {token_count}" + colorama.Fore.RESET)
            print("Reconstructed tokens:", [enc.decode([t]) for t in tokens])
            print(colorama.Fore.YELLOW + f"Estimated INPUT cost: ${cost:.6f}" + colorama.Fore.RESET)        #tokeny w oryginalnym tekście
        else:
            print(colorama.Fore.RED + "You didn't write anything stupid bitch!" + colorama.Fore.RESET)
            continue

if __name__ == "__main__":
    main()