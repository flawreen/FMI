"""Subiectul 1 –limbajul Python –3 p.a)Scrieți o funcție palindromcare primește un număr variabil de cuvinte formate
doar din litere mici ale alfabetului englez și returnează informații despre cuvintele palindrom sub forma unui
dicționar de perechi {cuvant palindrom: lista de litere}. Cheia este  cuvântul  primit  ca  parametru dacă acesta
este palindrom, iar lista de litere este formată din vocalele cuvântului dacă numărul vocalelor  este mai mare decât
numărul consoanelor, altfel lista va fi formată din consoanele cuvântului. Listele de litere vor fi sortate   în
ordine   lexicografică.  De  exemplu,  pentru  apelul palindrom  ('asa', 'merem', 'palindrom')funcția va returna
dicționarul {'asa': ['a'], 'merem': ['m', 'r']}(1.5 p.) """


def palindrom(*ls):
	rez = {}
	for cuv in ls:
		stg = dr = len(cuv) // 2
		if cuv[:stg] == cuv[:dr:-1]:
			rez.setdefault(cuv, list())
			vocale = list(set([x for x in cuv[:stg+1] if x in ['a', 'e', 'i', 'o', 'u']]))
			consoane = list(set([x for x in cuv[:stg+1] if x not in ['a', 'e', 'i', 'o', 'u']]))
			if len(vocale) >= len(consoane):
				vocale.sort()
				rez[cuv].extend(vocale)
			else:
				consoane.sort()
				rez[cuv].extend(consoane)
	return rez


print(palindrom("asa", "merem", "palindrom", "aabbdbbaa"))


