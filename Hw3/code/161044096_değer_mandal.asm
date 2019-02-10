           load R0, 4                  ;4
           load R1, 2                  ;2

           load R2, 0                  ;0
           load R3, 1                  ;1

value:     addi    R2, R2, R3
           addi    R4, R4, R1
           store   R4, [20h]
           jmpEQ   R2=R0, print
           jmp    value


print:     load    RF, [20h]
