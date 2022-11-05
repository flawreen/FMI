.data
    x: .long 5
	y: .long 4
	z: .long 0
	q: .long 0
	vnot: .long 7
	vand: .long 10
	vor: .long 6
	vxor: .long 4
	vtest: .long 3
.text
.global main
main:
	# TODO: nu se updateaza flagurile, raman doar PF ZF IF
	movl vnot, %eax
    notl %eax
	movl %eax, vnot
	
	movl vand, %eax
	andl x, %eax
	movl %eax, vand

	movl vor, %eax
	orl x, %eax
	movl %eax, vor

	movl vxor, %eax
	xorl y, %eax
	movl %eax, vxor

	movl vtest, %eax
	testl x, %eax
	movl %eax, vtest

    mov $1, %eax
    mov $0, %ebx
    int $0x80
