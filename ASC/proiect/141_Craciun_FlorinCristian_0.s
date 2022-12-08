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
    subl $4, %esp
    movl %ebp, 0(%esp)
    movl %esp, %ebp
    subl $4, %esp
    movl %ebx, -4(%ebp)
    subl $4, %esp
    movl %esi, -8(%ebp)
    subl $4, %esp
    movl %edi, -12(%ebp)

    movl 8(%ebp), %edi
    movl 12(%ebp), %esi
    # 16(%ebp) - adresa lui mres
    # 20(%ebp) - N
    movl 20(%ebp), %eax
    movl $4, %ebx
    xorl %edx, %edx
    mull %ebx
    subl $4, %esp
    movl %eax, -16(%ebp)  # 4*N -16
    xorl %eax, %eax

    fork:
        test 20(%ebp), %eax
        je sfarsit
        subl $4, %esp
        movl %eax, -20(%ebp)  # k -20
        xorl %edx, %edx
        mull -16(%ebp)  # %eax k * 4N 

        xorl %ebx, %ebx
        fori:
            test $1, %ebx
            je fork
            subl $4, %esp
            movl %ebx, -24(%ebp)  # i -24
            
            xorl %edx, %edx
            forj:
                test 20(%ebp), %edx
                je fori
                subl $4, %esp
                movl %edx, -28(%ebp)  # j -28
                
                addl -28(%ebp), %eax  # k * 4N + j
                movl %eax, %ecx
                movl -28(%ebp), %eax
                xorl %edx, %edx
                mull -16(%ebp)  # j * 4N
                addl -24(%ebp), %eax  # j * 4N + i

                lea 8(%ebp), %edi
                lea 12(%ebp), %esi
                movl (%esi, %eax, 4), %ebx
                movl (%edi, %ecx, 4), %eax
                xorl %edx, %edx
                mull %ebx

                lea 16(%ebp), %edi
                movl %eax, %esi  # salvez in esi inmultirea
                movl -16(%ebp), %eax
                xorl %edx, %edx
                mull -20(%ebp)  # k * 4N + i este mres[k][i]
                addl -24(%ebp), %eax
                
                movl -28(%ebp), %edx
                cmpl $0, %edx
                jne suma
                movl $0, %ebx
                lea (%edi, %eax, 4), %ecx  # j=0 -> initializez mres[k][i]
                movl %ebx, (%ecx)
                suma:
                movl (%edi, %eax, 4), %ebx
                addl 0(%esi), %ebx
                movl %ebx, 0(%edi, %eax, 4)

                movl -28(%ebp), %edx
                addl $4, %esp
                incl %edx
            jmp forj

            movl -24(%ebp), %ebx
            addl $4, %esp
            incl %ebx
        jmp fori

        movl -20(%ebp), %eax
        addl $4, %esp
        incl %eax
    jmp fork

    sfarsit:
    addl $4, %esp  # sterg 4 * N de la poz -16
    movl -12(%ebp), %edi
    addl $4, %esp
    movl -8(%ebp), %esi
    addl $4, %esp
    movl -4(%ebp), %ebx
    addl $4, %esp
    movl 0(%ebp), %ebp
    addl $4, %esp
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
    pushl mres
    pushl m2
    pushl m1
    call matrix_mult
    popl trash
    popl trash
    popl trash
    popl trash
    
    # afisare k

    lea mres, %edi
    jmp afisare_matrice

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

