# Named Tuple & Hashable – Clear Breakdown

---

## 1️⃣ What is a **Named Tuple**?

A **named tuple** is like a **regular tuple**, but each element has a **name**.

- Regular tuple: you access by **index** → confusing.
- Named tuple: you access by **name** → clear and readable.

### Example: Regular Tuple

```python
person = ("John", 25, "Nepal")

print(person[0])  # John
print(person[1])  # 25
```

❌ Problem: You have to remember which index is which.

### Example: Named Tuple

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "country"])
p = Person("John", 25, "Nepal")

print(p.name)     # John
print(p.age)      # 25
print(p.country)  # Nepal
```

✅ Advantage:

- You don't need to remember indexes
- Code is more readable
- Still immutable (like a tuple)

---

## 2️⃣ What does **hashable** mean?

**Hashable** = an object can be used as a **dictionary key** or added to a **set**.

- Python uses **hash values** to quickly find items in dict/set.
- Only immutable objects are hashable (like tuples, strings, numbers).
- Mutable objects (like list, dict, set) are **not hashable**.

### Example: Hashable

```python
t = (1, 2, 3)  # tuple is immutable → hashable
d = {t: "Hello"}  # ✅ Works
print(d[(1,2,3)])  # Hello
```

### Example: Not Hashable

```python
l = [1, 2, 3]  # list is mutable → not hashable
d = {l: "Hello"}  # ❌ Error
```

Output:

```
TypeError: unhashable type: 'list'
```

### Quick Analogy

- Hashable = has a **fixed identity**, like a **label on a box** → Python can always find it in dict/set.
- Non-hashable = can **change** → Python can't track it reliably.

---

## 3️⃣ Named Tuple + Hashable

- Named tuples are **immutable** → ✅ hashable
- You can use them as dictionary keys or in sets

```python
p1 = Person("Alice", 30, "Nepal")
d = {p1: "Engineer"}
print(d[p1])  # Engineer
```

---

## ✅ Summary

| Term         | Meaning                           | Example             |
| ------------ | --------------------------------- | ------------------- |
| Named tuple  | Tuple with **names** for elements | `Person(name, age)` |
| Hashable     | Can be used as dict key or in set | `t = (1,2,3)`       |
| Not hashable | Cannot be used as dict key or set | `[1,2,3]` (list)    |
