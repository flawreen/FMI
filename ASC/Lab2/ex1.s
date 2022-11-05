.data
    x: .long 5
    y: .long 3
.text
.globl main
main:
    movl x, %eax
    // movl y, %ebx
    // mul %ebx
    // pt a inmulti eax cu o variabila pot folosi mull (mul long): mull y, mull $2
    // mull y 
    mull y
    
    

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80