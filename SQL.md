# 📚 SQL Mastery Cheat Sheet (with Strategies & Patterns)

## 🧭 Strategies to Master SQL
1. **Pattern Recognition**
   - Identify query type: retrieval, aggregation, join, subquery, window function.
   - Ask: *Do I need row-level filtering (`WHERE`) or group-level filtering (`HAVING`)?*

2. **Brute Force → Optimize**
   - Start with a simple query, then refine with indexes, joins, or CTEs.
   - Example: nested subquery → rewrite as `JOIN` for efficiency.

3. **Complexity Awareness**
   - Know when queries scan entire tables (`SELECT *`) vs indexed lookups.
   - Always explain performance trade-offs in interviews.

4. **Edge Cases**
   - Empty tables, NULL values, duplicate rows.
   - Always test with sample data containing NULLs.

5. **Mix Practice Styles**
   - Write queries in a SQL editor for syntax speed.
   - Practice explaining queries aloud — clarity matters as much as correctness.

---

## 🔹 Common SQL Patterns

### 1. Top-N Queries
```sql
SELECT first_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 3;
```
- **Pattern:** Ranking or “nth highest” problems.
- ⚠️ **Pitfall:** In SQL Server, use `TOP 3` instead of `LIMIT`.

---

### 2. Aggregation + Grouping
```sql
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```
- **Pattern:** Group-level filtering.
- ⚠️ **Pitfall:** Using `WHERE` instead of `HAVING`.

---

### 3. Self-Join
```sql
SELECT e1.first_name, e2.first_name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.id;
```
- **Pattern:** Hierarchical relationships.
- ⚠️ **Pitfall:** Forgetting aliasing → confusing column references.

---

### 4. Subquery vs Join
```sql
-- Subquery
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Equivalent Join
SELECT e.first_name, e.salary
FROM employees e
JOIN (SELECT AVG(salary) AS avg_salary FROM employees) t
ON e.salary > t.avg_salary;
```
- **Pattern:** Compare row values to aggregate.
- ⚠️ **Pitfall:** Subquery may be slower — prefer join/CTE for clarity.

---

### 5. Window Functions
```sql
SELECT first_name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```
- **Pattern:** Ranking, running totals, moving averages.
- ⚠️ **Pitfall:** Confusing `RANK()` vs `ROW_NUMBER()` (ties handled differently).

---

## 📅 2 SQL Practice Plan

### 1: Foundations
- **Day 1–2:** SELECT, WHERE, ORDER BY.
- **Day 3–4:** Aggregations + GROUP BY.
- **Day 5–6:** Joins (inner, left, right).
- **Day 7:** Practice 5 mixed easy queries.

### 2: Advanced Patterns
- **Day 8–9:** Subqueries + CTEs.
- **Day 10:** Window functions (RANK, ROW_NUMBER, SUM OVER).
- **Day 11:** Case statements + conditional logic.
- **Day 12:** Indexes + performance tuning.
- **Day 13:** Complex joins (self-join, multi-table).
- **Day 14:** Mock test — 3 easy, 2 medium, 1 hard query.

---

## 🚨 General SQL Pitfalls
- Forgetting `WHERE` in `UPDATE`/`DELETE`.
- Using `SELECT *` in production queries.
- Mixing `WHERE` vs `HAVING`.
- Not aliasing tables in joins.
- Overusing indexes without considering write performance.
- Ignoring NULL handling in aggregates.

---


---

Here’s a **SQL Practice Problem Set** in Markdown format — aligned with the strategies and patterns we discussed. You can copy this directly into your notes and use it as a structured drill set 👇  

---

# 📝 SQL Practice Problem Set

## 🟢 Easy (Foundations)
1. **Retrieve all employees in the IT department.**
```sql
SELECT first_name, last_name 
FROM employees 
WHERE department = 'IT';
```

2. **List employees hired after 2020.**
```sql
SELECT first_name, hire_date 
FROM employees 
WHERE hire_date > '2020-01-01';
```

3. **Find the highest salary in the company.**
```sql
SELECT MAX(salary) AS highest_salary 
FROM employees;
```

---

## 🟡 Medium (Patterns & Optimization)
1. **Find the 3rd highest salary.**
```sql
SELECT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 2;
```
- ⚠️ In SQL Server:  
```sql
SELECT TOP 1 salary 
FROM (
    SELECT TOP 3 salary 
    FROM employees 
    ORDER BY salary DESC
) AS temp 
ORDER BY salary ASC;
```

2. **List departments with more than 5 employees.**
```sql
SELECT department, COUNT(*) AS emp_count 
FROM employees 
GROUP BY department 
HAVING COUNT(*) > 5;
```

3. **Show employees and their manager names.**
```sql
SELECT e.first_name AS employee, m.first_name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

4. **Find employees earning above the average salary.**
```sql
SELECT first_name, salary 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

## 🔴 Hard (Advanced & Tricky)
1. **Rank employees by salary within each department.**
```sql
SELECT department, first_name, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

2. **Find departments where the average salary is above 70,000.**
```sql
SELECT department, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 70000;
```

3. **List employees who have the same salary as someone else.**
```sql
SELECT first_name, salary 
FROM employees 
WHERE salary IN (
    SELECT salary 
    FROM employees 
    GROUP BY salary 
    HAVING COUNT(*) > 1
);
```

4. **Find employees with the highest salary in each department.**
```sql
SELECT department, first_name, salary
FROM (
    SELECT department, first_name, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 1;
```

---

# 🚨 Interview Pitfalls to Watch
- Forgetting `HAVING` for group filters.  
- Confusing `RANK()` vs `ROW_NUMBER()`.  
- Not handling **NULL values** in aggregates.  
- Using `SELECT *` instead of specific columns.  
- Forgetting `WHERE` in `UPDATE`/`DELETE`.  

---

✅ This set mirrors the **Easy → Medium → Hard ladder** like we did for arrays, but tailored for SQL. It gives you **practice queries + pitfalls** to sharpen interview readiness.  

---

