Dokladnie przeanalizowac dlaczego moja metoda nie zadzialala
1. Przy encodewithsignature nie mozna uzyc uint tylko trzeba uint256
2. Od wersji 0.7 lub 0.8 solidity sprawdza "do tylu" czy jakas zmienna nie over lub underflowuje
3. Sensowne zastosowanie tylko do 0.6 solidity
4. Mozna uzywać w 0.8 ale trzeba dodac unchecked na tym sprawdzeniu mappingu