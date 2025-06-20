# Produktinformationen
$produktname = "Tastatur"
$stückpreis = 25.99
$anzahl = 3
$mwstSatz = 0.19  # 19% Mehrwertsteuer

# Nettopreis berechnen (ohne MwSt)
$nettoGesamtpreis = $stückpreis * $anzahl

# Mehrwertsteuer berechnen
$mwstBetrag = $nettoGesamtpreis * $mwstSatz

# Bruttopreis berechnen (mit MwSt)
$bruttoGesamtpreis = $nettoGesamtpreis + $mwstBetrag

# Ausgabe
Write-Output "Produkt: $produktname"
Write-Output "Stückpreis: $($stückpreis.ToString("F2")) €"
Write-Output "Anzahl: $anzahl"
Write-Output "Nettopreis: $($nettoGesamtpreis.ToString("F2")) €"
Write-Output "Mehrwertsteuer (19%): $($mwstBetrag.ToString("F2")) €"
Write-Output "Gesamtpreis (brutto): $($bruttoGesamtpreis.ToString("F2")) €"

# Zwei Beispielzahlen
$a = 15
$b = 4

# Addition
$summe = $a + $b
Write-Output "`nAddition: $a + $b = $summe"

# Subtraktion
$differenz = $a - $b
Write-Output "Subtraktion: $a - $b = $differenz"

# Multiplikation
$produkt = $a * $b
Write-Output "Multiplikation: $a * $b = $produkt"

# Division
$quotient = $a / $b
Write-Output "Division: $a / $b = $quotient"

# Modulo (Rest bei Division)
$rest = $a % $b
Write-Output "Modulo: $a % $b = $rest" 
