-- Ex 1
-- Să se afișeze pacienții cărora li s-a prescris ’IBUPROFEN’.
SELECT DISTINCT P.NUME || ' ' || P.PRENUME AS NUME_COMPLET
FROM PACIENT P
JOIN CONSULTATIE C ON C.ID_PACIENT = P.ID_PACIENT
JOIN PRESCRIPTIE P2 ON P2.ID_CONSULTATIE = C.ID_CONSULTATIE
JOIN MEDICAMENT M ON M.ID_MEDICAMENT = P2.ID_MEDICAMENT AND UPPER(M.NUME) = 'IBUPROFEN';

-- Ex 2
-- Să se afișeze date (id, nume, prenume, sectie, salariu, numărul de consultații)
-- despre cei mai bine plătiți 2 doctori care au cel puțin 2 consultații. Vor fi afișați
-- în ordine descrescătoare după salariu, respectiv crescător după numărul de
-- consultații.
SELECT *
FROM (SELECT D.ID_DOCTOR, D.NUME, D.PRENUME, D.ID_SECTIE, D.SALARIU, COUNT(C.ID_DOCTOR) AS NR_CONSULTATII
      FROM DOCTOR D
               JOIN CONSULTATIE C ON D.ID_DOCTOR = C.ID_DOCTOR
      GROUP BY D.ID_DOCTOR, D.NUME, D.PRENUME, D.ID_SECTIE, D.SALARIU
      HAVING COUNT(C.ID_DOCTOR) >= 2
      ORDER BY D.SALARIU DESC, NR_CONSULTATII DESC)
WHERE ROWNUM < 3;

-- Ex 3
-- Pentru fiecare secție să se afișeze numele, prenumele și salariul celui mai bine
-- plătit doctor. Dacă o secție nu are doctori, atunci pe coloanele corespunzătoare
-- numelui și prenumelui se va afișa caracterul ’-’, iar pe coloana corespunzătoare
-- salariului, valoarea 0
SELECT COALESCE(D.NUME, '-') AS NUME,
       COALESCE(D.PRENUME, '-') AS PRENUME,
       COALESCE(D.SALARIU, 0) AS SALARIU,
       D.ID_SECTIE
FROM DOCTOR D
RIGHT JOIN (
SELECT S.ID_SECTIE, MAX(SALARIU) AS SALARIU
FROM SECTIE S FULL OUTER JOIN DOCTOR D ON D.ID_SECTIE = S.ID_SECTIE
GROUP BY S.ID_SECTIE
) G ON G.ID_SECTIE = D.ID_SECTIE
           AND (D.ID_SECTIE, D.SALARIU) IN (
SELECT S.ID_SECTIE, MAX(SALARIU) AS SALARIU
FROM SECTIE S FULL OUTER JOIN DOCTOR D ON D.ID_SECTIE = S.ID_SECTIE
GROUP BY S.ID_SECTIE
)
ORDER BY D.ID_SECTIE;

-- Ex 4
-- Să se afișeze pacienții din secțiile cu număr minim de consultații.
SELECT P.ID_PACIENT, P.NUME, P.PRENUME
FROM PACIENT P
JOIN (
        SELECT NR_SECTIE
        FROM
        (
            SELECT P.ID_SECTIE AS NR_SECTIE, COUNT(C.DATA) AS NR_CONSULTATII
            FROM SECTIE S
            FULL OUTER JOIN PACIENT P ON P.ID_SECTIE = S.ID_SECTIE
            FULL OUTER JOIN CONSULTATIE C ON C.ID_PACIENT = P.ID_PACIENT
            WHERE P.DATA_INTERNARE IS NOT NULL
            group by P.ID_SECTIE
            ORDER BY P.ID_SECTIE
        ) G
        WHERE G.NR_CONSULTATII =
        (
            SELECT MIN(G.NR_CONSULTATII) AS NR_MIN_CONSULTATII
            FROM (
                SELECT COUNT(C.DATA) AS NR_CONSULTATII
                FROM SECTIE S
                FULL OUTER JOIN PACIENT P ON P.ID_SECTIE = S.ID_SECTIE
                FULL OUTER JOIN CONSULTATIE C ON C.ID_PACIENT = P.ID_PACIENT
                WHERE P.DATA_INTERNARE IS NOT NULL
                group by S.ID_SECTIE
                ORDER BY S.ID_SECTIE
            ) G
            WHERE G.NR_CONSULTATII > 0
        )
    ) G2 ON G2.NR_SECTIE = P.ID_SECTIE;
