//4. Sa se verifice daca un numar dat este prim (folositi ambele variante de structuri repetitive).
.data
    x: .long 3
    da: .asciz "Numarul este prim!\n" # 19
    nu: .asciz "Numarul nu este prim.\n" # 22
.text

.globl main
main:
    movl x, %ecx
    sar $1, %ecx  # stop = n/2 = %ecx

    movl x, %eax
    cmp $1, %eax
    je nrprim
    cmp $2, %eax
    je nrprim

    movl $1, %ebx
    jmp verif


nrprim:
    movl $4, %eax
    movl $1, %ebx
    mov $da, %ecx
    movl $19, %edx
    int $0x80
    jmp etexit

fals:
    movl $4, %eax
    movl $1, %ebx
    mov $nu, %ecx
    movl $22, %edx
    int $0x80
    jmp etexit

verifloop:
    cmp $1, %ecx
    je nrprim
    movl $0, %edx
    movl x, %eax
    divl %ecx
    cmp $0, %edx
    je fals
    loop verifloop

verif:
    cmp %ecx, %ebx
    jge nrprim
    inc %ebx
    movl $0, %edx
    movl x, %eax
    divl %ebx
    cmp $0, %edx
    je fals
    jmp verif

etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
