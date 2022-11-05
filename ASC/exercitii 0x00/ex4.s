//3. Fie a, b, c trei numere salvate in memorie si min un spatiu alocat de 4 octeti. Sa se salveze
//in min cel mai mic numar dintre cele trei
.data
    a: .long 3
    b: .long 1
    c: .long 5
    min: .space 4
.text
.globl main
main:
    movl a, %eax
    movl b, %ebx
    cmpl c, %ebx
    jle bmin
    jmp cmin

bmin:
    cmp %eax, %ebx
    jle setbcmin
    jmp setamin

cmin:
    movl c, %ebx
    cmp %eax, %ebx
    jle setbcmin
    jmp setamin

setbcmin:
    movl %ebx, min
    jmp etexit

setamin:
    movl %eax, min
    jmp etexit


etexit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
