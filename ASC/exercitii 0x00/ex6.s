//4. Sa se verifice daca un numar dat este prim (folositi ambele variante de structuri repetitive).
//1. Sa se determine maximul si numarul de aparitii al acestuia intr-un array.
.data
    x: .long 3
    # da: .asciz "Numarul este prim!\n" # 19
    nu: .asciz "Numarul nu este prim.\n" # 22
    v: .long 1, 2, 3, 3, 3, 5, 5, 7, 7, 12
    n: .long 10
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
    lea v, %edi
    xorl %ecx, %ecx
    xorl %ebx, %ebx
    movl (%edi, %ecx, 4), %eax
    jmp cautare_aparitii

fals:
    movl $4, %eax
    movl $1, %ebx
    mov $nu, %ecx
    movl $22, %edx
    int $0x80
    jmp etexit

cautare_aparitii:
    cmp n, %ecx
    jg etexit

    movl (%edi, %ecx, 4), %edx
    cmp x, %edx
    jne continuare1

    inc %ebx  # daca e aparitia lui x contorizeaza
continuare1:
    cmp %eax, %edx
    jle continuare2
    movl %edx, %eax  # daca e mai mare max=%edx
continuare2:
    inc %ecx
    jmp cautare_aparitii


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
