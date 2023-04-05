#Подключаемся к БД
import sqlite3  

#Спрашиваем по какому Id нужна информация 
id = int(input("Введите id студента: ")) 

#Определяем функцию подключения к БД
def get_connection(): 
  connection = sqlite3.connect('teatchers.db')
  return connection

#Определяем функцию отключения от к БД
def close_connection(connection):
  if connection:
    connection.close()

#Определяем функцию получения информации о студенте по его Id из двух связанных таблиц
def get_student_detail(Student_id):
 
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students RIGHT JOIN School ON School.School_Id = Students.School_Id WHERE Student_Id = ?  """
    cursor.execute(select_query,(Student_id,))
    records = cursor.fetchall()
    print ("Данные по студенту")
    for row in records:
      print ("ID Студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", row[4])
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных", error)

get_connection()
get_student_detail(id)
