import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'putu'
)

cursor = con.cursor()

#buat database
# cursor.execute('create database putu')

#mengaktifkan database
#cursor.execute('use putu')

#buat table
# cursor.execute('''create table mahasiswa(
#                nama varchar (20) not null,
#                nim char (10) not null)
#                ''')


#isi table
# cursor.execute('''insert into buku(nama,nim)
#                values
#                ('musli','D0221068'),
#                ('putu','D0221078')
#                ''')
# con.commit()

#menampilkan isi table
# cursor.execute('select * from buku')
# hasil = cursor.fetchall()
# for i in hasil:
#     print(i)

#menampilkan table
# cursor.execute('show tables')
# hasil = cursor.fetchall()
# for i in hasil:
#     print(i)


#mengupdate table
# update = "update buku set nama='andre', nim='D0221080' where nama='putu'"
# cursor.execute(update)
# con.commit()

#menampilkan database
# cursor.execute('show databases')
# hasil = cursor.fetchall()
# for i in hasil:
#     print(i)

#menghapus database
# cursor.execute('drop database putu')

#menghapus table
# cursor.execute('drop table buku')

print('berhasil')
