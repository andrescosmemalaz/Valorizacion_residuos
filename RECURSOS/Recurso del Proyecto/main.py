#https://docs.python.org/es/3/tutorial/venv.html
import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #remote ip
            user ='root',
            password='12345',
            db='estudiantes'
        )

        self.cursor = self.connection.cursor()

        # print("Conexión establecida correctamente")

    def select_alumno(self,IdAlumno):
        sql = 'SElECT IdAlumno,Nombres,Apellidos,Edad,Curso FROM alumnos WHERE IdAlumno = {}'.format(IdAlumno)

        try:
            self.cursor.execute(sql)
            alumnos = self.cursor.fetchone()

            print('IdAlumno',':',alumnos[0])
            print('Nombres',':',alumnos[1])
            print('Apellidos',':',alumnos[2])
            print('Edad',':',alumnos[3])
            print('Curso',':',alumnos[4])

        except Exception as e:
            raise
    
    def select_all_alumnos(self):
        sql = 'SElECT IdAlumno,Nombres,Apellidos,Edad,Curso FROM alumnos '

        try:
            self.cursor.execute(sql)
            alumnos = self.cursor.fetchall()

            for alumno in alumnos:
                print('IdAlumno',':',alumno[0])
                print('Nombres',':',alumno[1])
                print('Apellidos',':',alumno[2])
                print('Edad',':',alumno[3])
                print('Curso',':',alumno[4])
                print('______\n')

        except Exception as e:
            raise

    def update_alumno(self,IdAlumno,Nombres):
        sql = "UPDATE alumnos SET Nombres = '{}' WHERE IdAlumno = {}".format(Nombres,IdAlumno)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 

    def close(self):
        self.connection.close()
        print("Conexión finalizada")


database = Database()

# database.update_alumno(102,'Andres')
database.select_all_alumnos()
database.close()





