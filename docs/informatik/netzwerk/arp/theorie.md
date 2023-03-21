# Address Resolution Protocol (ARP)

## Was ist das Address Resolution Protocol?

Das Address Resolution Protocol (ARP) ist ein Protokoll, welches verwendet wird, um die MAC-Adresse eines Geräts anhand
seiner IP-Adresse zu finden. Es kommt zum Einsatz, wenn ein Gerät eine Verbindung zu einem anderen Gerät aufbauen möchte.

## Wie funktioniert das Address Resolution Protocol?

Das ARP-Protokoll funktioniert folgendermassen:

1. Ein Gerät möchte eine Verbindung zu einem anderen Gerät aufbauen.
2. Das Gerät sendet eine Nachricht an alle Geräte im Netzwerk. In dieser Nachricht steht die IP-Adresse des Geräts, zu
   dem eine Verbindung aufgebaut werden soll: "Wer ist `192.168.0.1`?"
3. Das Gerät mit der IP-Adresse `192.168.0.1` sendet eine Antwort an das Gerät, welches die Nachricht gesendet hat. In
   dieser
   Antwort steht die MAC-Adresse des Geräts: "Ich habe die MAC-Adresse `00:00:00:00:00:00`"
4. Das Gerät, welches die Nachricht gesendet hat, speichert die MAC-Adresse des Geräts, zu dem eine Verbindung
   aufgebaut werden soll, in einer lokalen Tabelle ab. Diese Tabelle wird auch ARP-Cache genannt. Somit muss diese
   Prozedur nicht jedes Mal durchgeführt werden, wenn eine Verbindung zu diesem Gerät aufgebaut werden soll.