# Lab-4
У модулі реалізовано 3 класи, що допомагають запустити гру-блукачку.
Клас Room має 10 методів, завдяки яким збирається і описується вся необхідна інформація про локацію, в якій перебуває гравець.(назва кімнати, вигляд, персонажі та предмети в кімнаті, сусідні кімнати)
Клас Enemy має 8 методів. У цьому класі описується персонаж, його репліка, слабкість та аналізується чи зміг гравець побороти ворога за допомогою його слабкості.
Клас Item має 5 методів. У ньому описується предмет та його назва.

Фрагмент запуску гри:

Kitchen
--------------------
A dank and dirty room buzzing with flies.
The Dining Hall is south
> south

Dining Hall
--------------------
A large room with ornate golden decorations on each wall.
The Ballroom is west
The Kitchen is north
Dave is here!
A smelly zombie
The [book] is here - A really good book entitled 'Knitting for dummies'
> take
You put the book in your backpack

Dining Hall
--------------------
A large room with ornate golden decorations on each wall.
The Ballroom is west
The Kitchen is north
Dave is here!
A smelly zombie
> fight
What will you fight with?
book
Dave crushes you, puny adventurer!
Oh dear, you lost the fight.
That's the end of the game
