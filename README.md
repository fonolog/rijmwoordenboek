# rijmwoordenboek
Defines a rhyming dictionary for Dutch

The file rijmwoorden.py contains two dictionaries:

In 'rijmwoordenboek' the keys are phonetic transcriptions (in the SAMPA used in Dutch CELEX), and the value is a dictionary of Dutch words which have that phonetic transcription as their rhyming part in dictionary.

In 'hulprijmwoordenboek' a phonetic transcription is given for the rhyming part of every Dutch word in Celex.

In order to find the words rhyming with, say, 'sla', you have to look up the word in the hulprijmwoordenboek, and find a phonetic transcription, and then look up the phonetic transcription in rijmwoordenboek to find 'daarna', 'ga', etc.

Since this is a bit cumbersome, the last line of this script defines a function 'rijmwoorden' which does this for you: rijmwoorden('sla') == {'daarna', 'ga', ...}

The words and their phonetic transcriptions are derived from the CELEX database: http://celex.mpi.nl/. This means that the list is not completely up to date with respect to the current wordstock or the orthography, but it comes close enough.
