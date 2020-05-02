import sys

# print(*dir(sys), sep='\n')

# a = input('a')
# b = input('b')
#
# sys.exit()
# # doesn't work after exit
# c = input('c')


# stderr ve stdout
# Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.
#
# stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.
#
# stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.
#
# stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.
#
# Biz print() fonksiyonumuzu kullandığımızda aslında standard olarak stdout kullanılmaktadır. Ancak biz istersek *stderr'e de bir şeyler yazabiliriz.

sys.stderr.write('This is a error message\n')
sys.stderr.flush() # aslinda yazmasakta olur fakat buyuk dosyalarda bu direk bufferi bosaltiyor ve ekrana basiyor

sys.stdout.write('This is a regular text\n')

# sys.argv Python programlarını komut satırlarından çalıştırdığımızda yanına verdiğimiz argümanları taşıyan bir listedir.
print(sys.argv)