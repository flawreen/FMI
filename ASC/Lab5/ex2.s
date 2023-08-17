# Sa se scrie o procedura min3 care primeste 3 argumente si returneaza minimul dintre ele in %eax
.data
    x: .long 7
    y: .long 3
    z: .long 1
    minStr: .asciz "Minimul este %d.\n"
.text
.globl main
min3:
    pushl %ebp
    movl %esp, %ebp
    movl 8(%ebp), %eax
    movl 12(%ebp), %ebx
    movl 16(%ebp), %edx

    cmp %ebx, %eax
    jle min1
min2:
    cmp %ebx, %ecx
    jle ecxmin
    jmp ebxmin

min1:
    cmp %ecx, %eax
    jle rez
    jmp ecxmin

ebxmin:
    movl %ebx, %eax
    jmp rez
ecxmin:
    movl %ecx, %eax
rez:
    popl %ebp
    ret

main:
    pushl x
    pushl y
    pushl z
    call min3
    popl %edx
    popl %edx
    popl %edx

    pushl %eax
    pushl $minStr
    call printf
    popl %edx
    popl %edx

    pushl $0
    call fflush
    popl %edx

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
