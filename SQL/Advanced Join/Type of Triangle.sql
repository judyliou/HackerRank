SELECT IF(A+B > C and B+C > A and A+C > B, IF(A=B and B=C, 'Equilateral', IF(A=B OR B=C OR C=A, 'Isosceles', 'Scalene')), 'Not A Triangle')
FROM TRIANGLES;
