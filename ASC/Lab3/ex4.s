.data
    x:.long 5
    y: .long 6
.text
   

.globl main
main:
    movl y, %eax
    addl x, %eax

    movl $1, %eax
    movl $0, %ebx
    int $0x80



