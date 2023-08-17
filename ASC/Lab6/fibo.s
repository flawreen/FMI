.data
formatprintf: .asciz "%d\n"

.text
fibo:
    pushl %ebp
    movl %esp, %ebp

    movl 8(%ebp), %ebx
    movl 12(%ebp), %edx
    movl 16(%ebp), %eax
    movl 20(%ebp), %ecx

    cmp %ebx, %edx
    je final

    pushl %ecx
    addl %eax, %ecx
    popl %eax
    incl %edx

    pushl %ecx
    pushl %eax
    pushl %edx
    pushl %ebx
    call fibo
    popl %edi
    popl %edi
    popl %edi
    popl %edi


    final:
    movl %ecx, %eax

    popl %ebp
    ret

.globl main
main:
    movl $2, %edx
    movl $9, %ebx
    movl $1, %eax
    pushl %eax
    pushl %eax
    pushl %edx
    pushl %ebx
    call fibo
    popl %edx
    popl %edx
    popl %edx
    popl %edx

    pushl %eax
    pushl $formatprintf
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
