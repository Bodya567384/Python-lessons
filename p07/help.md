# Заняття 7

## Цикл while. Кортеж, Словник

---

> [Повторення](https://learningapps.org/watch?v=pbusccoct20)

### Цикл while

Цикли використовуються для повторення виконання певного блоку коду. 
Наприклад, якщо нам потрібно показати певне повідомлення 
100 разів, ми можемо використати цикл. Це простий приклад, але 
за допомогою циклів ми можемо зробити багато всього.

Цикл __while__ використовується для виконання блоку коду доти, 
доки не буде досягнуто певної умови.

```
while умова:
    # блок коду для виконання

# Цикл while з i = 1 до 10
i = 1
n = 10
while i <= n:
    print(i)
    i = i + 1     
```

__Увага!__ Якщо умова циклу завжди істинна (True), цикл виконуватиметься 
нескінченну кількість разів (поки не заповниться пам’ять).

#### Цикл while з частиною else 

У Python цикл while може мати необов’язковий блок else, який 
виконуватиметься після того, як умова циклу стане False.

```
counter = 0
 
while counter < 3:
    print('Inside loop')
    counter += 1
else:
    print('Inside else') 
```

Блок else не виконуватиметься, якщо цикл while зупинено 
оператором break. 

```
counter = 0
 
while counter < 3:
    # Цикл завершує своє виконання через оператор break.
    # Блок else не виконується 
    if counter == 1:
        break
 
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')    
```

Цикл __for__ зазвичай використовується, коли відома кількість ітерацій.

Цикл __while__ зазвичай використовується, коли кількість ітерацій невідома.

### Кортеж (tuple)

Кортеж в Python схожий на список. Різниця між ними 
полягає в тому, що ми не можемо змінити елементи кортежу 
після присвоювання їм значень, тоді як елементи списку 
ми можемо змінити

Кортеж створюється шляхом розміщення всіх елементів у круглих 
дужках __()__, розділених комами. Круглі дужки необов’язкові, проте 
їх використання є хорошою практикою. Кортеж може містити будь-яку 
кількість елементів, і вони можуть бути різних 
типів (int, float, list, string тощо).


```
# Порожній кортеж
empty_tuple = ()
 
# Кортеж, що містить цілі числа
int_tuple = (1, 2, 3)
 
# Кортеж зі змішаними типами даних
mixed_tuple = (1, "Hello", 3.4)
 
# Вкладений кортеж
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

```

#### Доступ до елементів кортежу

Подібно до списку, кожен елемент кортежу представлений індексними 
номерами (0, 1, …), де індекс першого елемента 0. Номер індексу 
використовується для доступу до елементів кортежу.


```
# Створюємо кортеж
product = ('Sony', 'PlayStation', 480)
 
# Отримуємо доступ до елемента з індексом 0
print(product[1]) # виведе PlayStation 
```

### Словник (dict)

Словник — це впорядкований набір елементів. Він зберігає елементи 
в парах ключ-значення. Ключі — це унікальні ідентифікатори, 
пов’язані зі значеннями.

```
# Створюємо словник capital_city
capital_city = {'Ukraine': 'Kyiv', 'Japan': 'Tokio', 'Spain': 'Madrid'} 
```

Тут ми створили словник capital_city, у якому:

- ключі: 'Ukraine', 'Japan', 'Spain'.
- значення: 'Kyiv', 'Tokio', 'Madrid'.

> __Ключі__ використовуються для доступу до значень. Навпаки не працює.

```
print(capital_city['Ukraine'])  # виведе Kyiv 
```

#### Методи словника Python

Python має набір вбудованих методів, які можна використовувати у словниках.

- __clear()__ Removes all the elements from the dictionary
- __copy()__ Returns a copy of the dictionary
- __fromkeys()__ Returns a dictionary with the specified keys and value
- __get()__ Returns the value of the specified key
- __items()__ Returns a list containing a tuple for each key value pair
- __keys()__ Returns a list containing the dictionary's keys
- __pop()__ Removes the element with the specified key
- __popitem()__ Removes the last inserted key-value pair
- __setdefault()__ Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- __update()__ Updates the dictionary with the specified key-value pairs
- __values()__ Returns a list of all the values in the dictionary


### Оператор pass

Оператор pass — це порожній оператор, який можна використовувати як 
“заглушку” для майбутнього коду. Припустимо, ми маємо цикл або 
функцію, яка ще не визначена, але ми її визначимо в майбутньому. 
У таких випадках ми можемо використовувати оператор pass.

```
n = 20
 
# Використовуємо pass всередині конструкції if
if n > 10:
    pass
 
print('Hello') 
```

Зверніть увагу, що ми використали оператор pass всередині 
конструкції if. Але нічого не відбувається при виконанні оператора 
pass (виходить ситуація NOP, скор. від “No Operation”). 

В коді далі ми отримаємо повідомлення про помилку: 
IndentationError: expected an indented block

```
n = 10
 
if n > 10:
    # Тут буде код, але трохи пізніше
 
print('Hello') 
```

Різниця між коментарем та оператором pass у Python полягає в 
тому, що хоча інтерпретатор повністю ігнорує коментар, 
оператор pass не ігнорується.

Також ми можемо використати оператор pass у функції чи класі. 

```hs
def function(args):
    pass 
```

```hs
class Example:
    pass 
```

--- 

### PEP 8 – Style Guide for Python Code
> [ Style Guide for Python Code](https://peps.python.org/pep-0008/#maximum-line-length)