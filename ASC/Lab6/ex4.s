.data
.text
.globl main
main:
    movl $1, %eax
    shl $0x1f, %eax
    shr $0x1f, %eax

    movl $1, %eax
    shl $31, %eax
    shr $0x1f, %eax

    movl $1, %eax
    shl $29, %eax
    shr $0x1f, %eax

    movl $2048, %edx
    sar $2, %edx



et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
