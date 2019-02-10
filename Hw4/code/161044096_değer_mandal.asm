              load R1, 00001011b
             load R2, 00010001b
             load R3, 00000001b
             load R4, 0
             load R5, 1
             move R7,R2
value:
            and RA,R1,R3
            and RB,R2,R3
           move R0,RA
           jmpEQ RB=R0,next
           jmp ready
next:
           addi R4,R4,R5
           ror R1, 1
           ror R2, 1
           move R0,R2
           jmpEQ R7=R0, ready
           jmp value
ready:
          load R9, 48
          addi R4,R9,R4
          move RF,R4
          halt
