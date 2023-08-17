-- NUME VARCHAR(20) dinamic     'ANDREI' -> 'ANDREI'
-- PRENUME CHAR(20)             'ANDREI' -> 'ANDREI         ..pana la 20'
SELECT '-7' +2  -- conversie implicita
FROM DUAL

-- conversie explicita: TO_CHAR, TO_DATE, TO_NUMBER

SELECT
    TO_NUMBER('$2,777.98', 'L9G999D99')
FROM DUAL;

SELECT SUBSTR('QWERTY', 2, 4) FROM DUAL;    -- 2 e indexul de unde incepe substr, 4 e lungimea substr-ului

SELECT
    LTRIM('XXYXINFORMATICA', 'X')   -- Daca al doilea parametru nu e specificat sterge blank-urile
FROM DUAL;                          -- Sterge gasirile de la stanga


-- opusul lui ltrim - lpad
SELECT
    LPAD('INFO', 6, 'X')            -- adauga X pana ajunge la len=6
FROM DUAL;                          -- daca parametrul e prea mare ca sa incapa in len-ul dat, adauga ce poate


SELECT
    INSTR('INONOWE', 'NO', 3, 2)    -- returneaza 0: cauta i 'NOWE' si e doar o aparitie a lui 'NO'
FROM DUAL;


SELECT
    TRANSLATE('$A$AAA', '$A', 'BC') --
FROM DUAL;

SELECT
    REPLACE('$A$AAA', '$A', 'BC')   -- Ia fiecare caracter in parte
FROM DUAL;

-- Ex 1
SELECT first_name || last_name || 'castiga' || salary
FROM employees;

-- Ex 2
SELECT LTRIM(RTRIM(first_name)) AS nume FROM employees
WHERE UPPER(first_name) LIKE 'J%' OR UPPER(first_name) LIKE 'M%' OR UPPER(first_name) LIKE '__A%'
ORDER BY LENGTH(first_name) DESC;

-- Ex 3
SELECT first_name, employee_id, last_name, department_id FROM employees
WHERE UPPER(first_name) LIKE '%STEVEN%';

-- Ex 4
SELECT first_name AS nume, employee_id AS cod, department_id AS departament, LENGTH(first_name) AS lungime, INSTR(first_name, 'a') AS pozitia FROM employees
WHERE LOWER(first_name) LIKE ('%e');

-- Ex 5
SELECT first_name,  MONTHS_BETWEEN((SELECT SYSDATE FROM DUAL), hire_date) AS luni FROM employees
WHERE MONTHS_BETWEEN((SELECT SYSDATE FROM DUAL), hire_date) = ROUND(MONTHS_BETWEEN((SELECT SYSDATE FROM DUAL), hire_date));


