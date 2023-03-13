# Subnetzmaske

## Was ist eine Subnetzmaske?

Die Subnetzmaske, auch Netzmaske gennant, sagt aus, wie viele Bits von der IP-Adresse für das Netzwerk fix sind. Die
restlichen Bits sind für die
Geräte im
Netzwerk vorgesehen. Die Geräte werden dann einfach durchnummeriert.

> Beispiel:  
> Die Subnetzmaske `255.255.255.0` sagt aus, dass die ersten 24 Bits der IP-Adresse für das Netzwerk fix sind.
> Wenn also ein Gerät im Netzwerk der IP-Adresse `192.168.0.1` hat, dann sind die ersten 24 Bits `192.168.0` und die
> restlichen 8 Bits `1`. Somit haben alle Geräte im Netzwerk eine IP-Adresse im Bereich `192.168.0.0`
> bis `192.168.0.255`.

## Suffix

Um bei der Subnetzmaske nicht immer die 4 Bytes einzeln schreiben zu müssen, gibt es einen Suffix. Dieser Suffix wird
der IP-Adresse angehängt und sagt aus, wie viele Bits für dieses Netzwerk fix sind.
Das Suffix hat die Form `/x`.

> Beispiel:  
> `192.168.0.0/24` in diesem Fall ist das Suffix /24 und sagt dasselbe aus wie im vorherigen Beispiel.

## Wie viele IP-Adressen gibt es im Subnetz?

Wir wissen, dass die IP-Adresse aus 4 Bytes besteht. Jedes Byte hat 8 Bits. Somit hat eine IP-Adresse 32 Bits.

Die Anzahl der im Netzwerk verfügbaren IP-Adressen ist 2 hoch die Anzahl der Bits, die für die Geräte im Netzwerk
vorgesehen sind.

> Beispiel:  
> Suffix `/24`  
> Es bleiben 8 Bits (32 Bits - 24 Bits) für die Geräte übrig. Somit sind $ 2^8 $ = 256 IP-Adressen im Netzwerk
> verfügbar.