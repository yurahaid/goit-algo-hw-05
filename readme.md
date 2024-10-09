# Результати порівняння алгоритмів
```
стаття 1 - Existing Substring - Boyer-Moore: 0.031713 seconds
стаття 1 - Existing Substring - KMP: 0.065236 seconds
стаття 1 - Existing Substring - Rabin-Karp: 0.161739 seconds
стаття 1 - Existing small Substring - Boyer-Moore: 0.052174 seconds
стаття 1 - Existing small Substring - KMP: 0.063266 seconds
стаття 1 - Existing small Substring - Rabin-Karp: 0.161017 seconds
стаття 1 - Non-existing Substring - Boyer-Moore: 0.019406 seconds
стаття 1 - Non-existing Substring - KMP: 0.099494 seconds
стаття 1 - Non-existing Substring - Rabin-Karp: 0.315023 seconds
стаття 2 - Existing Substring - Boyer-Moore: 0.032188 seconds
стаття 2 - Existing Substring - KMP: 0.091638 seconds
стаття 2 - Existing Substring - Rabin-Karp: 0.227036 seconds
стаття 2 - Existing smll Substring - Boyer-Moore: 0.022400 seconds
стаття 2 - Existing smll Substring - KMP: 0.027226 seconds
стаття 2 - Existing smll Substring - Rabin-Karp: 0.068735 seconds
стаття 2 - Non-existing Substring - Boyer-Moore: 0.026517 seconds
стаття 2 - Non-existing Substring - KMP: 0.140646 seconds
стаття 2 - Non-existing Substring - Rabin-Karp: 0.450726 seconds

```

Отже, для кожного тексту при пошуку існуючого та неіснуючого шаблону найкращі результати показав алгоритм Боєра-Мура
який дозволяє ефективно пропускати значні частини тексту. Проте його ефективність залежить від розміру шаблону - чим 
більше шаблон для пошуку тим більш ефективний цей алгоритм, для менших шаблонів також гарні результати показує алгоритм
Кнута-Моріса-Пратта. Найгірші результати показав алгоритм Робін-Карпа, для обох текстів він має найгріші результати

Загалом я б рекомендував до використання алогоритм Боєра-Мура для обох текстів та будь-яких розмірів шаблону пошуку
оскільки він стабільно показує найкращий результат серед цих трьох варіантів.