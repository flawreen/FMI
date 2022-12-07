.data
    N: .space 4
    i: .space 4
    nr: .space 4
    nr_cerinta: .space 4
    legaturi: .space 400
    m1: .space 40000
    m2: .space 40000
    mres: .space 4
    citire: .asciz "%d"
    afisare: .asciz "%d "
    endl: .asciz "\n"
    trash: .space 4
.text
matrix_mult:
    push %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %esi
    pushl %edi

    movl 8(%ebp), %edi
    movl 12(%ebp), %esi
    # 16(%ebp) - adresa lui mres
    # 20(%ebp) - N



    popl %edi
    popl %esi
    popl %ebx
    popl %ebp
    ret
.globl main



main:
    pushl $nr_cerinta
    pushl $citire
    call scanf
    popl trash
    popl trash

    pushl $N
    pushl $citire
    call scanf
    popl trash
    popl trash

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
    lea m1, %edi
citire_matrice:
    cmp N, %ecx
    je alege_cerinta
    
    movl N, %eax
    movl $4, %ebx
    mull %ebx
    mull %ecx  # i * 4N pentru matrice
    movl %eax, i

    lea legaturi, %esi
    movl (%esi, %ecx, 4), %ebx
    pushl %ecx
    xorl %ecx, %ecx
    lea m2, %esi
    initializare_linie:
        cmp N, %ecx
        je citire_noduri

        pushl %ecx
        addl i, %ecx
        movl $0, (%edi, %ecx, 4)
        movl $0, (%esi, %ecx, 4)
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
        movl $1, (%esi, %ecx, 4)

        decl %ebx
    jmp citire_noduri
    gata:
    popl %ecx
    incl %ecx
jmp citire_matrice

alege_cerinta:
    movl nr_cerinta, %ecx
    cmp $1, %ecx
    je afisare_matrice
    
    pushl N
    pushl $mres
    pushl $m2
    pushl $m1
    call matrix_mult
    popl trash
    popl trash
    popl trash
    popl trash
    
    # afisare k

    jmp et_exit

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
