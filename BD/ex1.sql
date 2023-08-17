SELECT
    ROUND(SYSDATE, 'MI')
FROM DUAL;

-- Ex 5
SELECT first_name,  MONTHS_BETWEEN(SYSDATE, hire_date) AS luni FROM employees
WHERE MONTHS_BETWEEN(SYSDATE, hire_date) = ROUND(MONTHS_BETWEEN(SYSDATE, hire_date));

-- Ex 6
SELECT employee_id, first_name, salary, TO_CHAR(salary + salary * 0.15, '9999.99') AS "Salariu nou", MOD(ROUND(salary + salary * 0.15, 0), 100) AS "Numar sute" FROM EMPLOYEES
WHERE MOD(salary, 1000) != 0;

-- Ex 7
SELECT first_name, salary,  LPAD('$', salary / 1000, '$') AS "Nivelul venitului" FROM employees;

-- Ex 8
SELECT
    SYSDATE + 30
FROM DUAL;

-- Ex 9
SELECT
    TO_DATE('31-DEC-' || TO_CHAR(SYSDATE, 'YYYY')) - SYSDATE
FROM DUAL;

-- Ex 10
SELECT
    SYSDATE + 0.5
FROM DUAL;

SELECT
    SYSDATE + 1/24/60 * 5
FROM DUAL;

-- Ex 11
SELECT
    last_name || first_name AS "Nume", hire_date,
    NEXT_DAY(ADD_MONTHS(HIRE_DATE, 6), 'Monday')
FROM employees;

-- Ex 12
SELECT
    first_name, ROUND(MONTHS_BETWEEN(SYSDATE, hire_date)) "Luni lucrate"
FROM employees
ORDER BY "Luni lucrate";

-- Ex 13
SELECT
    first_name,
    hire_date,
    TO_CHAR(hire_date, 'DAY') "Ziua saptamanii"
FROM employees
ORDER BY TO_CHAR(hire_date, 'D') ASC;

-- Ex 14
SELECT first_name, DECODE(commission_pct, null, 'Fara comision', '0' || TO_CHAR(commission_pct)) "Comision"
FROM employees;

-- Ex 15
SELECT first_name, salary, commission_pct, salary + salary * commission_pct "Venit lunar"
FROM employees
WHERE commission_pct IS NOT NULL AND salary + salary * commission_pct >= 10000
ORDER BY "Venit lunar" ASC;

