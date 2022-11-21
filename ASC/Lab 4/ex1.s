.data
    x: .space 4
    formatScanf: .asciz "%d"
.text
.globl main
main:
    push $x
    push $formatScanf
    call scanf
    popl %ebx
    popl %ebx
    movl x, %eax
et_exit:
....

