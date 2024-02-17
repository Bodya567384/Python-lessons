# Заняття 3

### Умовні оператори

---
 

#### Оператор __IF__

Оператор if використовується для перевірки умови: якщо умова 
виконується, ми виконуємо блок операторів (званий блоком if), 
інакше ми обробляємо інший блок операторів (званий блоком else).  

Слово __else__ необов'язкове.

<pre>
if x < 0:    
    print('Негативне число')
</pre>

<pre>
if x < 0:    
    print('Негативне число')    
elif x == 0:
    print('Нуль')
</pre>

Повна констукція:

<pre>
if x < 0:
    print('Негативне число')
elif x == 0:
    print('Нуль')
elif x == 1:
   print('Один')
else:
   print('Більше одного')
</pre>

#### Оператори порівняння 

`==` Дорівнює	_2 == 4 → False_

`!=` Не дорівнює	_2 != 5 → True_

`>` Більше ніж	_2 > 4 → False_

`<` Менше ніж	_2 < 4 → True_

`>=` Більше або Дорівнює	_2 >= 4 → False_

`<=` Менше або Дорівнює	_2 <= 4 → True_

#### Заокруглення числа

Функція __round()__

> round(number, ndigits=None)

<pre>
number = 13.46
r = round(13.46, 1)
print(r)
</pre>

_виведе: 13.5_  



---

### Markdown Basic Syntax
[MD Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

**VS Code** supports Markdown files out of the box
Markdown preview __Ctrl+Shift+V__

[Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)