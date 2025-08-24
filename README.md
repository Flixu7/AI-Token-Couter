# Token Cost Calculator

Kalkulator kosztów tokenów dla różnych modeli OpenAI. Program pozwala na obliczenie przybliżonych kosztów używania różnych modeli AI na podstawie liczby tokenów w tekście.

## Funkcje

- Tokenizacja tekstu używając kodowania GPT-3.5/4 (cl100k_base)
- Obliczanie kosztów dla różnych modeli OpenAI
- Interaktywny interfejs w terminalu z kolorowym wyświetlaniem
- Obsługa najnowszych modeli OpenAI (GPT-5, GPT-4.1, o1, etc.)

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/twoja-nazwa-uzytkownika/token-cost-calculator.git
cd token-cost-calculator
```

2. Stwórz wirtualne środowisko:
```bash
python -m venv venv
```

3. Aktywuj środowisko:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Zainstaluj zależności:
```bash
pip install tiktoken colorama
```

## Użycie

Uruchom program:
```bash
python main.py
```

Program poprowadzi Cię przez proces wyboru modelu i wprowadzania tekstu do analizy.

## Obsługiwane modele

- GPT-5, GPT-5-mini, GPT-5-nano
- GPT-4.1, GPT-4.1-mini, GPT-4.1-nano
- GPT-4o, GPT-4o-mini
- GPT-4.5
- o1, o1-pro
- GPT-3.5-turbo

## Struktura projektu

```
├── main.py          # Główny plik programu
├── pricing.py       # Cennik modeli OpenAI
├── README.md        # Ten plik
└── .gitignore       # Pliki ignorowane przez Git
```

## Licencja

MIT License
