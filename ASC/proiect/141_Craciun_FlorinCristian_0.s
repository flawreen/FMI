.data
    N: .space 4
    i: .space 4
    a: .space 4
    b: .space 4
    k: .space 4
    nr: .space 4
    nr_cerinta: .space 4
    legaturi: .space 400
    m1: .space 40000
    m2: .space 40000
    mres: .space 40000
    citire: .asciz "%d"
    afisare: .asciz "%d "
    rezult: .asciz "%d"
    endl: .asciz "\n"
    trash: .space 4
.text
matrix_mult:
    pushl %ebp
    movl %esp, %ebp
    movl 8(%ebp), %edi
    movl 12(%ebp), %esi
    pushl %ebx
    pushl %edi
    pushl %esi

    xorl %ecx, %ecx
    loopk:
        cmp 20(%ebp), %ecx
        je final
        
        xorl %ebx, %ebx
        loopi:
            cmp 20(%ebp), %ebx
            je gatai

            xorl %edx, %edx
            loopj:
                cmp 20(%ebp), %edx
                je gataj

                movl %ecx, %eax
                pushl %edx
                xorl %edx, %edx
                mull 20(%ebp)
                popl %edx
                addl %edx, %eax

                pushl %edx
                pushl %ecx
                movl (%edi, %eax, 4), %ecx

                movl %edx, %eax
                
                xorl %edx, %edx
                mull 20(%ebp)
                addl %ebx, %eax
                movl (%esi, %eax, 4), %edx
                movl %edx, %eax
                xorl %edx, %edx
                mull %ecx
                movl %eax, %edx
                popl %ecx

                movl 16(%ebp), %edi
                pushl %edx
                movl %ecx, %eax
                mull 20(%ebp)
                addl %ebx, %eax
                popl %edx
                addl %edx, (%edi, %eax, 4)
                movl 8(%ebp), %edi
                popl %edx
                incl %edx
            jmp loopj

            gataj:
            incl %ebx
        jmp loopi
        gatai:
        incl %ecx
    jmp loopk

    final:
    popl %esi
    popl %edi
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
    xorl %edx, %edx
    mull %ecx  # i * N pentru matrice
    movl %eax, i

    lea legaturi, %esi
    movl (%esi, %ecx, 4), %ebx
    pushl %ecx
    xorl %ecx, %ecx
    mov $m2, %esi
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

    pushl $k
    pushl $citire
    call scanf
    popl trash
    popl trash

    pushl $a
    pushl $citire
    call scanf
    popl trash
    popl trash

    pushl $b
    pushl $citire
    call scanf
    popl trash
    popl trash

    movl $1, %ebx
inmultire:
    cmp k, %ebx
    je rezultat
    
    cmp $1, %ebx
    jg reset_mat
    apelare:
    pushl N
    pushl $mres
    pushl $m2
    pushl $m1
    call matrix_mult
    popl trash
    popl trash
    popl trash
    popl trash
    jmp pas_urmator

    reset_mat:
    movl $m1, %edi
    movl $mres, %esi
    movl N, %eax
    xorl %edx, %edx
    mull N
    xorl %edx, %edx
    movl $4, %ecx
    mull %ecx
    xorl %ecx, %ecx
    resetare_matrice:
    cmp %eax, %ecx
    je apelare

    movl (%esi, %ecx, 1), %edx
    movl %edx, (%edi, %ecx, 1)
    movl $0, (%esi, %ecx, 1)

    addl $4, %ecx
    jmp resetare_matrice
    pas_urmator:
    incl %ebx
jmp inmultire

rezultat:
movl a, %eax
xorl %edx, %edx
mull N
movl b, %edx
addl %edx, %eax
movl $mres, %edi
movl (%edi, %eax, 4), %ecx

pushl %ecx
pushl $rezult
call printf
popl trash
popl trash

pushl $0
call fflush
popl trash

jmp et_exit
afisare_matrice:
xorl %ecx, %ecx
mov $m1, %edi
loop:
    cmp N, %ecx
    je et_exit
    
    movl N, %eax
    mull %ecx  # i * N pentru matrice
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
