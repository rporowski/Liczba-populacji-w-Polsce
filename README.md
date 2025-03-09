# Liczba-populacji-w-Polsce
Prognoza liczby populacji w Polsce na podstawie danych historycznych GUS (1946-2024)
Opis projektu
Niniejszy projekt ma na celu prognozowanie liczby ludności Polski do roku 2035 przy wykorzystaniu danych historycznych obejmujących okres od 1946 do 2024 roku. W projekcie zastosowano cztery różne modele uczenia maszynowego i analizy szeregów czasowych:

ARIMA – automatyczne dobieranie parametrów modelu z uwzględnieniem braku sezonowości (dla danych rocznych).
Holt–Winters (Triple Exponential Smoothing) – model z addytywnym trendem.
Prophet – model Facebook Prophet, przystosowany do danych rocznych, gdzie wyłączono dodatkową sezonowość.
Regresja liniowa – prosty model trendowy oparty na indeksie rocznym.
Wyniki prognoz zostały przedstawione na zbiorczym wykresie, umożliwiającym porównanie modeli. Wszystkie modele wykazały kontynuację trendu spadkowego liczby ludności Polski, co potwierdza stabilny trend obserwowany w danych historycznych.

Dane
Dane użyte w projekcie pochodzą z historycznych statystyk dotyczących ludności Polski (w tysiącach mieszkańców) od roku 1946 do 2024. Dane są przetwarzane w formie szeregu czasowego o częstotliwości rocznej (AS – Annual Start).

Metodologia
Przygotowanie danych:
Dane są wczytywane bezpośrednio jako słownik, a następnie konwertowane do DataFrame z indeksem datowym. Ustawiona jest częstotliwość roczna, a ewentualne braki uzupełniane metodą interpolacji.

Budowa modeli:

Model ARIMA: Automatyczne dobieranie parametrów przy użyciu funkcji auto_arima z ustawieniami odpowiednimi dla danych rocznych.
Model Holt–Winters: Wykorzystanie modelu Triple Exponential Smoothing bez sezonowości.
Model Prophet: Konwersja danych do formatu wymaganym przez Prophet i prognozowanie z wyłączoną sezonowością.
Model Regresji Liniowej: Utworzenie indeksu rocznego (Year_Index) i dopasowanie prostej regresji liniowej.
Prognoza i wizualizacja:
Prognozy dla każdego z modeli są generowane na ten sam horyzont (do 2035 roku). Wyniki są prezentowane na zbiorczym wykresie, który pokazuje dane historyczne oraz prognozy poszczególnych modeli.

Wnioski
Wyniki analizy wskazują, że na podstawie danych historycznych z lat 1946–2024 wszystkie zastosowane modele prognozują dalszy spadek liczby ludności Polski do roku 2035. Chociaż prognozy poszczególnych modeli są zbliżone, należy pamiętać, że wyniki te opierają się wyłącznie na analizie historycznych danych szeregu czasowego i nie uwzględniają czynników demograficznych, migracyjnych ani zmian polityk społeczno-ekonomicznych. Dlatego prognoza ma charakter orientacyjny.

Uruchomienie projektu
Projekt został stworzony z myślą o uruchomieniu w środowisku Google Colab. Aby uruchomić kod:

Skopiuj cały kod do notatnika Google Colab.
Uruchom kolejne komórki.
Wyniki prognozy zostaną wyświetlone na wygenerowanym wykresie, a wnioski zostaną przedstawione w konsoli.
Pliki w repozytorium
README.md – ten plik z opisem projektu.
Dodatkowe pliki: notatnik Google Colab (.ipynb).
