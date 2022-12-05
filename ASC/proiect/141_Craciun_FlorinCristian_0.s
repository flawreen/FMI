.data
    N: .space 4
    i: .space 4
    nr: .space 4
    nr_cerinta: .space 4
    legaturi: .space 400
    matrice: .space 40000
    citire: .asciz "%d"
    afisare: .asciz "%d "
    endl: .asciz "\n"
    trash: .space 4
.text

.globl main
main:
#   push $nr_cerinta
    pushl $N
    pushl $citire
    call scanf
    popl trash
    popl trash
#   pop trash

    xorl %ecx, %ecx
    lea legaturi, %esi
citire_legaturi:
    cmp N, %ecx
    je gata_citire_legaturi

    pushl %ecx
    pushl $nr
    pushl $citire
    call scanf
    popl trash
    popl trash
    popl %ecx

    movl nr, %ebx
    movl %ebx, (%esi, %ecx, 4)

    incl %ecx
jmp citire_legaturi

gata_citire_legaturi:
    xorl %ecx, %ecx
    lea matrice, %edi
citire_matrice:
    cmp N, %ecx
    je afisare_matrice
    
    movl N, %eax
    movl $4, %ebx
    mull %ebx
    mull %ecx  # i * 4N pentru matrice
    movl %eax, i

    movl (%esi, %ecx, 4), %ebx
    pushl %ecx
    xorl %ecx, %ecx
    initializare_linie:
        cmp N, %ecx
        je citire_noduri

        pushl %ecx
        addl i, %ecx
        movl $0, (%edi, %ecx, 4)
        popl %ecx

        incl %ecx
    jmp initializare_linie
    citire_noduri:
        cmp $0, %ebx
        je gata

        pushl $nr
        pushl $citire
        call scanf
        popl trash
        popl trash
        
        movl nr, %ecx
        addl i, %ecx
        movl $1, (%edi, %ecx, 4)

        decl %ebx
    jmp citire_noduri
    gata:
    popl %ecx
    incl %ecx
jmp citire_matrice

afisare_matrice:
xorl %ecx, %ecx
loop:
    cmp N, %ecx
    je et_exit
    
    movl N, %eax
    movl $4, %ebx
    mull %ebx
    mull %ecx  # i * 4N pentru matrice
    movl %eax, i

    movl (%edi, %ecx, 4), %ebx
    pushl %ecx
    xorl %ecx, %ecx
    afisare_linie:
        cmp N, %ecx
        je linie_noua

        pushl %ecx
        addl i, %ecx
        movl (%edi, %ecx, 4), %eax
        movl %eax, nr

        pushl nr
        pushl $afisare
        call printf
        popl trash
        popl trash

        pushl $0
        call fflush
        popl trash

        popl %ecx
        incl %ecx
    jmp afisare_linie
    linie_noua:
    pushl $endl
    call printf
    popl trash
    popl %ecx

    incl %ecx
jmp loop

et_exit:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
