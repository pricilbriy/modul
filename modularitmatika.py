# nama file : modularitmatika
import aritmatika1

def main():
    a = int(input('mauskkan nilai a : '))
    b = int(input('masukkan nilai b : '))

    print('a\t: %d' %a)
    print('b\t: %d' %b)

    print('a+b\t: %d' % aritmatika1.tambah(a, b))
    print('a-b\t: %d' % aritmatika1.kurang(a, b))
    print('a*b\t: %d' % aritmatika1.kali(a, b))
    print('a/b\t: %d' % aritmatika1.bagi(a, b))


if __name__=="__name__":
    main()
