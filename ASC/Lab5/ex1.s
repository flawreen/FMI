.data
    x: .long 5
    y: .long 6
.text
.globl main
suma:
    push %ebp
    movl %esp, %ebp
    push %ebx
    movl 8(%ebp), %eax
    movl 12(%ebp), %ebx

    addl %ebx, %eax
    
    popl %ebx
    popl %ebp
    ret

main:
    pushl y
    pushl xorl
    call suma
    pop %ebx
    pop %ebx
    # afisare %eax

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
