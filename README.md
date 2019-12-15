## Шифр Цезаря

*Шифр Цезаря* — один из самых ранних шифров. В этом шифре сообщение
шифруется путем замены каждой буквы в нем «сдвинутой» буквой. В криптографии зашифрованные буквы называются символами, потому что они мо-
гут быть буквами, числами или любыми другими знаками. Если вы сдвинете
букву **«А»** на одну позицию, то получите букву **«Б»**. Если сдвинете букву **«А»**
на две позиции, получите букву **«В»**.

Часто для удобства использования шифра Цезаря используют два 
насаженных на общую ось диска разного диаметра с нарисованными по 
краям дисков алфавитами. Изначально диски поворачиваются так, 
чтобы напротив каждой буквы алфавита внешнего диска находилась та же 
буква алфавита малого диска. Если теперь повернуть внутренний диск на 
несколько символов, то мы получим соответствие между символами 
внешнего диска и внутреннего — шифр Цезаря. Получившийся диск можно 
использовать как для шифрования, так и для расшифровки.

Если сопоставить каждому символу алфавита его порядковый номер 
(нумеруя с 0), то шифрование и дешифрование можно выразить 
формулами модульной арифметики:

<blockquote>
<code>y = (x + k) mod n</code><br>
<code>y = (x - k) mod n</code>
</blockquote>

**x** - символ открытого текста, **у** - символ шифрованного текста, 
**n** - мощность алфавита, **k** - ключ

Процесс дешифровки обратен процессу шифрования. Чтобы расшифровать слово,
зная ключ, нужно двигаться влево по символам. Например: нужно расшифровать 
слово **Ьмшф**. Мы знаем, что при шифровании буквы сдвинуты на 4 символа 
вправо, поэтому двигаемся влево:
- Ь - 4 = Ш
- м - 4 = и
- ш - 4 = ф
- ф - 4 = р

