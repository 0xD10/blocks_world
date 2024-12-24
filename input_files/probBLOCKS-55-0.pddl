(define (problem BLOCKS-55-0)
(:domain BLOCKS)
(:objects A1 V R1 L T1 I I1 X C1 Q1 H M F1 Y B D E H1 S1 J M1 W
          A2 C E1 N1 S V1 P1 R O G1 Z1 W1 P G K K1 B2 A T N O1 U1 
          J1 L1 X1 Z Y1 F B1 C2 U D1 Q)

(:INIT (CLEAR A1) (CLEAR V) (CLEAR R1) (CLEAR L) (CLEAR T1)
                    (ONTABLE I) (ONTABLE I1) (ONTABLE R1) (ONTABLE X)
                    (ONTABLE C1) (ON A1 Q1) (ON Q1 H) (ON H M) (ON M F1)
                    (ON F1 Y) (ON Y B) (ON B D) (ON D E) (ON E H1) (ON H1 S1)
                    (ON S1 J) (ON J M1) (ON M1 W) (ON W A2) (ON A2 C)
                    (ON C E1) (ON E1 N1) (ON N1 S) (ON S V1) (ON V1 P1)
                    (ON P1 R) (ON R O) (ON O G1) (ON G1 I) (ON V Z1)
                    (ON Z1 W1) (ON W1 P) (ON P G) (ON G K) (ON K K1)
                    (ON K1 I1) (ON L B2) (ON B2 A) (ON A T) (ON T N) (ON N O1)
                    (ON O1 U1) (ON U1 J1) (ON J1 L1) (ON L1 X1) (ON X1 Z)
                    (ON Z Y1) (ON Y1 F) (ON F B1) (ON B1 C2) (ON C2 X)
                    (ON T1 U) (ON U D1) (ON D1 Q) (ON Q C1) (HANDEMPTY))
(:GOAL (AND (ON E R) (ON R H1) (ON H1 X1) (ON X1 V1) (ON V1 B2) (ON B2 Q)
           (ON Q A) (ON A H) (ON H Y1) (ON Y1 I1) (ON I1 P) (ON P C) (ON C F)
           (ON F S) (ON S W1) (ON W1 A1) (ON A1 K1) (ON K1 S1) (ON S1 O1)
           (ON O1 D) (ON D G) (ON G E1) (ON E1 T1) (ON T1 Y) (ON Y B1)
           (ON B1 V) (ON V Q1) (ON Q1 C2) (ON C2 Z1) (ON Z1 F1) (ON F1 D1)
           (ON D1 L1) (ON L1 T) (ON T C1) (ON C1 N) (ON N K) (ON K R1)
           (ON R1 A2) (ON A2 N1) (ON N1 B) (ON B Z) (ON Z G1) (ON G1 X)
           (ON X O) (ON O J1) (ON J1 P1) (ON P1 M1) (ON M1 L) (ON L W)
           (ON W J) (ON J M) (ON M U) (ON U I) (ON I U1)))
)