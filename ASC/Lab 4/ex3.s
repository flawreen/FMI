# ex: Se citeste de la STDOUTPUT(prin apel scanf) un sir de caractere fara spatii de max 50 caractere
# SSD numarul de vocale si sa se afiseze acest numar la STDOUTPUT printr-un apel la printf
.data
    nrVocale: .long 0
    str: .space 51
    citire: .asciz "%s"
    afisare: .asciz "%d\n"
.text
.globl main
main:
    push $str
    push $citire
    call scanf
    popl %ebx
    popl %ebx

    mov $str, %edi
    movl $0, %ecx
    movl $0, %edx

et_loop:
    xorl %eax, %eax
    movb (%edi, %ecx, 1), %ah
    cmp $0, %ah
    je et_exit

    cmp $'A', %ah
    je vocala

    cmp $'E', %ah
    je vocala

    cmp $'I', %ah
    je vocala

    cmp $'O', %ah
    je vocala

    cmp $'U', %ah
    je vocala

    cmp $'a', %ah
    je vocala

    cmp $'e', %ah
    je vocala

    cmp $'i', %ah
    je vocala

    cmp $'o', %ah
    je vocala

    cmp $'u', %ah
    je vocala

jmp continuare

vocala:
    addl $1, %edx

continuare:
    incl %ecx
    jmp et_loop

et_exit:
    pushl %edx
    pushl $afisare
    call printf
    popl %ebx
    popl %ebx

    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80

