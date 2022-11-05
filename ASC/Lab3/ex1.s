.data
    v: .long 3, 5, 17, 27, 11, 10, 4
    n: .long 7
.text
.globl main
main:
    mov $v, %edi
    mov $0, %ecx  # pe post de index
    # for(i = 0; i < n; i++) {
    #    eax = v[i];
    #    //instr cu eax }
    
et_for:
    cmp n, %ecx
    je et_exit
    movl (%edi, %ecx, 4), %ebx  # obligatoriu sufixam cu tipul de date
    // instr cu %ebx
    incl %ecx
    jmp et_for
et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
