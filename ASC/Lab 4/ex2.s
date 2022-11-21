.data
    str: .asciz "Sir de caractere"
    # nu mai avem nevoie de un n, deoarece il parcurgem pana ajungem la Byte-ul 0 (sau \0)
.text
.globl main
main:
    movl $str, %edi
    movl $0, %ecx

et_loop:
    # elementul curent din sir: vrem sa-l punem intr-un registru de un byte (al, ah, bl bh, cl ch, dl dh)
    movb (%edi, %ecx, 1), %ah
    cmp $0, %ah
    je et_exit

    # prelucrare %ah

    inc %ecx
    jmp et_loop

et_exit:
    movl $1, %eax
    movl $0, %ebx
    int $0x80

