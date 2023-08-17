.data

.text

.globl main
# g(x) = x + 1
g:
    pushl %ebp
    movl %esp, %ebp

    movl 8(%ebp), %eax
    incl %eax

    popl %ebp
    ret

# f(x) = 2 * g(x)
f:
    pushl %ebp
    movl %esp, %ebp

    # apelare g(x)
    pushl 8(%ebp)
    call g
    addl $4, %esp  # dezalocam

    movl $2, %ecx  # 2 * g(x)
    mull %ecx

    popl %ebp
    ret

main:



et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80

