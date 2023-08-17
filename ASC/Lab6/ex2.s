# Sa se citeasca un N > 0 si un array de N <= 100 elemente.
# Sa se scrie o proc max(&v, n) care det maximul
# si o procedura proc(&v, n) care det cate elemente sunt egale cu maximul si proc va apela intern procedura max.
# bogdan.macovei.fmi@gmail.com

.data
    n: .space 4
    v: .space 400
    x: .space 4
    citire: .asciz "%d"
    afisare: .asciz "%d "

.text
.globl main
max:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx

    movl 12(%ebp), %ecx
    decl %ecx
    movl 8(%ebp), %edi
    xorl %ebx, %ebx
    movl (%edi, %ebx, 4), %eax
    
    detmax:
        cmp $-1, %ecx
        je final
        
        movl (%edi, %ecx, 4), %ebx
        cmp %eax, %ebx
        jle mic
        movl %ebx, %eax
        mic:

        decl %ecx
    jmp detmax
    final:
    popl %ebx
    popl %ebp
    ret

proc:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx

    movl 12(%ebp), %ebx
    movl 8(%esp), %edi

    pushl %ebx
    pushl %edi
    call max
    popl %edx
    popl %edx
    

    popl %ebx
    popl %ebp
    ret


main:
    pushl $n
    pushl $citire
    call scanf
    addl $8, %esp

    xorl %ecx, %ecx
    movl $v, %edi
loop1:
    cmp n, %ecx
    je apelare

    pushl %ecx
    pushl $x
    pushl $citire
    call scanf
    addl $8, %esp
    popl %ecx

    movl x, %ebx
    movl %ebx, (%edi, %ecx, 4)

    incl %ecx
    jmp loop1

apelare:
    pushl n
    pushl $v
    call max
    addl $8, %esp

    pushl %eax
    pushl $afisare
    call proc
    addl $8, %esp

    pushl $0
    call fflush
    addl $4, %esp

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80

